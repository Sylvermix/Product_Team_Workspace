"""
Garment segmentation via GroundingDINO through the Roboflow Inference API.

Returns bounding boxes for every garment detected in a photo. Confidence
threshold and garment vocabulary are read from config so nothing is
hard-coded in this module.
"""

import os
import base64
import logging
from pathlib import Path

import requests

logger = logging.getLogger(__name__)

# Roboflow Inference API — hosted endpoint used for the spike so we avoid
# running the model locally (saves GPU setup time during feasibility testing).
ROBOFLOW_INFER_URL = "https://infer.roboflow.com"
GROUNDINGDINO_MODEL_ID = "grounding-dino"
GROUNDINGDINO_VERSION = "1"

ENV_VAR_ROBOFLOW_API_KEY = "ROBOFLOW_API_KEY"


def _read_api_key() -> str:
    """Read the Roboflow API key from environment; raise clearly if absent."""
    api_key = os.environ.get(ENV_VAR_ROBOFLOW_API_KEY)
    if not api_key:
        raise EnvironmentError(
            f"Missing required environment variable '{ENV_VAR_ROBOFLOW_API_KEY}'. "
            "Set it before running the pipeline."
        )
    return api_key


def _encode_image_to_base64(image_path: str) -> str:
    """Read an image from disk and return its base64-encoded string."""
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    if not path.is_file():
        raise ValueError(f"Path is not a file: {image_path}")
    with path.open("rb") as file_handle:
        return base64.b64encode(file_handle.read()).decode("utf-8")


def _build_text_prompt(garment_categories: list[str]) -> str:
    """
    GroundingDINO uses free-text prompts with dot-separated class labels.
    We join all garment categories so the model looks for all of them in
    one pass rather than making N calls.
    """
    return " . ".join(garment_categories)


def _parse_detection_response(
    response_json: dict,
    confidence_threshold: float,
) -> list[dict]:
    """
    Parse the Roboflow Inference API response into our internal format.

    Expected response structure:
    {
        "predictions": [
            {
                "class": "jacket",
                "confidence": 0.87,
                "x": 320, "y": 240, "width": 180, "height": 220
            },
            ...
        ]
    }

    We convert center-based (x, y, width, height) to corner-based
    (x1, y1, x2, y2) to match the rest of the pipeline's bbox contract.
    """
    predictions = response_json.get("predictions", [])
    garments = []

    for prediction in predictions:
        confidence = prediction.get("confidence", 0.0)
        if confidence < confidence_threshold:
            continue

        center_x = prediction["x"]
        center_y = prediction["y"]
        width = prediction["width"]
        height = prediction["height"]

        garments.append(
            {
                "label": prediction["class"],
                "confidence": round(confidence, 4),
                "bbox": [
                    round(center_x - width / 2),
                    round(center_y - height / 2),
                    round(center_x + width / 2),
                    round(center_y + height / 2),
                ],
            }
        )

    return garments


def segment_garments(image_path: str, config: dict) -> list[dict]:
    """
    Detect garments in an image using GroundingDINO via the Roboflow
    Inference API.

    Args:
        image_path: Absolute path to the input image file.
        config: Full pipeline config dict (as loaded from config.yaml).

    Returns:
        List of dicts, one per detected garment above the confidence
        threshold:
        [
            {
                "label": "jacket",
                "confidence": 0.87,
                "bbox": [x1, y1, x2, y2],  # pixel coordinates
            },
            ...
        ]

    Raises:
        EnvironmentError: ROBOFLOW_API_KEY env var not set.
        FileNotFoundError: image_path does not exist.
        requests.HTTPError: API returned a non-2xx status.
        ValueError: API returned a response we cannot parse.
    """
    seg_config = config["pipeline"]["segmentation"]
    confidence_threshold = seg_config["confidence_threshold"]
    garment_categories = seg_config["garment_categories"]

    api_key = _read_api_key()
    image_b64 = _encode_image_to_base64(image_path)
    text_prompt = _build_text_prompt(garment_categories)

    url = f"{ROBOFLOW_INFER_URL}/{GROUNDINGDINO_MODEL_ID}/{GROUNDINGDINO_VERSION}"
    payload = {
        "image": {"type": "base64", "value": image_b64},
        "text": text_prompt,
    }
    headers = {"Content-Type": "application/json"}
    params = {"api_key": api_key}

    logger.debug("Calling Roboflow Inference API for %s", image_path)

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            params=params,
            timeout=30,
        )
        response.raise_for_status()
    except requests.Timeout as error:
        raise requests.Timeout(
            f"Roboflow API timed out after 30s for image '{image_path}'"
        ) from error
    except requests.ConnectionError as error:
        raise requests.ConnectionError(
            f"Could not reach Roboflow API. Check network connectivity. "
            f"URL: {url}"
        ) from error
    except requests.HTTPError as error:
        raise requests.HTTPError(
            f"Roboflow API returned HTTP {response.status_code} for "
            f"image '{image_path}'. Response: {response.text[:500]}"
        ) from error

    try:
        response_json = response.json()
    except ValueError as error:
        raise ValueError(
            f"Roboflow API returned non-JSON response for image '{image_path}': "
            f"{response.text[:500]}"
        ) from error

    garments = _parse_detection_response(response_json, confidence_threshold)

    if not garments:
        logger.warning(
            "No garments detected above confidence %.2f in '%s'. "
            "This photo may not contain visible clothing or the threshold "
            "is too strict.",
            confidence_threshold,
            image_path,
        )

    logger.info(
        "Detected %d garment(s) in '%s'", len(garments), image_path
    )
    return garments
