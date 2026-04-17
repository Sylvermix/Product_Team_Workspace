"""
Garment attribute extraction using Claude Vision (claude-sonnet-4-6).

Crops the detected garment from the photo, sends it to Claude with a
structured-output prompt, and returns a validated attribute dict. Token
usage is tracked per call so the pipeline can accumulate cost totals.
"""

import base64
import io
import json
import logging
import os
from pathlib import Path

import anthropic
from PIL import Image

logger = logging.getLogger(__name__)

ENV_VAR_ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"

VALID_COLOR_FAMILIES = frozenset(
    [
        "black",
        "white",
        "grey",
        "navy",
        "blue",
        "green",
        "red",
        "pink",
        "orange",
        "yellow",
        "purple",
        "brown",
        "beige",
        "cream",
        "camel",
        "burgundy",
        "multicolor",
        "pattern",
    ]
)

VALID_STYLE_REGISTERS = frozenset(
    [
        "casual",
        "smart-casual",
        "business-casual",
        "formal",
        "athletic",
        "streetwear",
        "bohemian",
        "minimalist",
        "preppy",
        "vintage",
        "luxury",
        "workwear",
    ]
)

VALID_PRICE_TIERS = frozenset(["budget", "mid", "premium"])

ATTRIBUTE_EXTRACTION_PROMPT = """\
You are a fashion expert. Analyze this garment image and return ONLY a JSON object \
with no additional text. Use this exact schema:

{
  "category": "<garment type, e.g. blazer, jeans, sneakers>",
  "color_family": "<one of: black, white, grey, navy, blue, green, red, pink, \
orange, yellow, purple, brown, beige, cream, camel, burgundy, multicolor, pattern>",
  "style_register": "<one of: casual, smart-casual, business-casual, formal, \
athletic, streetwear, bohemian, minimalist, preppy, vintage, luxury, workwear>",
  "price_tier": "<one of: budget, mid, premium>",
  "description": "<concise 1-2 sentence description for a shopping search query>"
}

Rules:
- color_family MUST be one of the listed values exactly
- style_register MUST be one of the listed values exactly
- price_tier MUST be one of: budget, mid, premium
- Return ONLY the JSON object — no markdown, no explanation
"""


def _read_api_key() -> str:
    """Read the Anthropic API key from environment; raise clearly if absent."""
    api_key = os.environ.get(ENV_VAR_ANTHROPIC_API_KEY)
    if not api_key:
        raise EnvironmentError(
            f"Missing required environment variable '{ENV_VAR_ANTHROPIC_API_KEY}'. "
            "Set it before running the pipeline."
        )
    return api_key


def _crop_and_encode_garment(image_path: str, bbox: list[int]) -> str:
    """
    Crop the image to the bounding box and return a base64-encoded JPEG.

    We re-encode as JPEG (80% quality) to keep payload size reasonable
    for the Vision API — raw PNGs from some cameras can be 8MB+.
    """
    x1, y1, x2, y2 = bbox

    with Image.open(image_path) as img:
        # Guard against bboxes that extend beyond the image boundary
        img_width, img_height = img.size
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(img_width, x2)
        y2 = min(img_height, y2)

        if x2 <= x1 or y2 <= y1:
            raise ValueError(
                f"Invalid bounding box {bbox} for image of size "
                f"{img_width}x{img_height}. After clamping: "
                f"[{x1},{y1},{x2},{y2}]"
            )

        cropped = img.crop((x1, y1, x2, y2))
        buffer = io.BytesIO()
        cropped.convert("RGB").save(buffer, format="JPEG", quality=80)
        buffer.seek(0)
        return base64.b64encode(buffer.read()).decode("utf-8")


def _validate_attributes(attributes: dict) -> dict:
    """
    Validate that Claude's response conforms to the expected schema.

    Raises ValueError with the problematic field if validation fails.
    """
    required_fields = {"category", "color_family", "style_register", "price_tier", "description"}
    missing = required_fields - attributes.keys()
    if missing:
        raise ValueError(f"Claude response missing required fields: {missing}")

    color = attributes["color_family"]
    if color not in VALID_COLOR_FAMILIES:
        raise ValueError(
            f"Invalid color_family '{color}'. "
            f"Must be one of: {sorted(VALID_COLOR_FAMILIES)}"
        )

    style = attributes["style_register"]
    if style not in VALID_STYLE_REGISTERS:
        raise ValueError(
            f"Invalid style_register '{style}'. "
            f"Must be one of: {sorted(VALID_STYLE_REGISTERS)}"
        )

    price = attributes["price_tier"]
    if price not in VALID_PRICE_TIERS:
        raise ValueError(
            f"Invalid price_tier '{price}'. "
            f"Must be one of: {sorted(VALID_PRICE_TIERS)}"
        )

    return attributes


def extract_attributes(
    image_path: str,
    bbox: list[int],
    config: dict,
) -> dict:
    """
    Extract structured fashion attributes from a garment crop using Claude Vision.

    Args:
        image_path: Absolute path to the original (full) image.
        bbox: Bounding box [x1, y1, x2, y2] in pixel coordinates.
        config: Full pipeline config dict (as loaded from config.yaml).

    Returns:
        Dict with keys:
        {
            "category": str,
            "color_family": str,
            "style_register": str,
            "price_tier": str,
            "description": str,
            "input_tokens": int,   # tracked for cost accounting
            "output_tokens": int,
        }

    Raises:
        EnvironmentError: ANTHROPIC_API_KEY env var not set.
        ValueError: Claude returned malformed or invalid JSON, or the
            response fails schema validation. Raw response included.
    """
    attr_config = config["pipeline"]["attribute_extraction"]
    model = attr_config["model"]
    max_tokens = attr_config["max_tokens"]

    api_key = _read_api_key()
    image_b64 = _crop_and_encode_garment(image_path, bbox)

    client = anthropic.Anthropic(api_key=api_key)

    logger.debug(
        "Sending garment crop to Claude (%s) for attribute extraction", model
    )

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_b64,
                        },
                    },
                    {
                        "type": "text",
                        "text": ATTRIBUTE_EXTRACTION_PROMPT,
                    },
                ],
            }
        ],
    )

    raw_text = response.content[0].text.strip()

    try:
        attributes = json.loads(raw_text)
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Claude returned malformed JSON. Raw response: {raw_text!r}"
        ) from error

    _validate_attributes(attributes)

    attributes["input_tokens"] = response.usage.input_tokens
    attributes["output_tokens"] = response.usage.output_tokens

    logger.info(
        "Attributes extracted: category=%s color=%s style=%s "
        "(tokens: %d in / %d out)",
        attributes["category"],
        attributes["color_family"],
        attributes["style_register"],
        attributes["input_tokens"],
        attributes["output_tokens"],
    )

    return attributes
