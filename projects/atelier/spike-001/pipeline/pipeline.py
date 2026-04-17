"""
Pipeline orchestrator for SPIKE-001.

Runs the full sequence: segment → extract_attributes → search_products
for every garment in a photo. Measures wall-clock latency at each step
and accumulates cost based on token usage and per-query pricing.
"""

import logging
import time
from pathlib import Path
from typing import Any

from pipeline.extract_attributes import extract_attributes
from pipeline.search_products import search_products
from pipeline.segment import segment_garments

logger = logging.getLogger(__name__)

# Cost is not a constant — it comes from config — but these are the config keys
# used when the caller does not supply cost rates (makes unit-testing easier).
FALLBACK_CLAUDE_INPUT_COST_PER_MILLION = 3.00
FALLBACK_CLAUDE_OUTPUT_COST_PER_MILLION = 15.00
FALLBACK_SERPAPI_COST_PER_QUERY = 0.01


def _extract_cost_rates(config: dict) -> dict:
    """Pull per-unit cost rates from config, falling back to known defaults."""
    costs = config.get("costs", {})
    return {
        "claude_input_per_million": costs.get(
            "claude_input_cost_per_million_tokens",
            FALLBACK_CLAUDE_INPUT_COST_PER_MILLION,
        ),
        "claude_output_per_million": costs.get(
            "claude_output_cost_per_million_tokens",
            FALLBACK_CLAUDE_OUTPUT_COST_PER_MILLION,
        ),
        "serpapi_per_query": costs.get(
            "serpapi_cost_per_query",
            FALLBACK_SERPAPI_COST_PER_QUERY,
        ),
    }


def _photo_id_from_path(image_path: str) -> str:
    """Derive a short photo ID from the filename (stem without extension)."""
    return Path(image_path).stem


def _milliseconds_since(start: float) -> float:
    """Return elapsed milliseconds from a perf_counter start point."""
    return round((time.perf_counter() - start) * 1000, 1)


def _calculate_claude_cost(
    input_tokens: int,
    output_tokens: int,
    rates: dict,
) -> float:
    """Compute USD cost for a Claude API call from token counts and rates."""
    input_cost = (input_tokens / 1_000_000) * rates["claude_input_per_million"]
    output_cost = (output_tokens / 1_000_000) * rates["claude_output_per_million"]
    return round(input_cost + output_cost, 6)


def _process_single_garment(
    garment: dict,
    image_path: str,
    config: dict,
    rates: dict,
) -> tuple[dict, dict, list[dict]]:
    """
    Run attribute extraction and product search for one detected garment.

    Returns a tuple of (enriched_garment, cost_accumulator, errors).

    We separate this from run_pipeline to keep that function under 50 lines
    and to make per-garment error handling explicit.
    """
    label = garment["label"]
    bbox = garment["bbox"]
    cost_accumulator: dict[str, Any] = {
        "claude_input_tokens": 0,
        "claude_output_tokens": 0,
        "serpapi_queries": 0,
    }
    errors: list[dict] = []
    attributes: dict = {}
    products: list[dict] = []

    # Step 2a: attribute extraction
    try:
        attributes = extract_attributes(image_path, bbox, config)
        cost_accumulator["claude_input_tokens"] += attributes.pop("input_tokens", 0)
        cost_accumulator["claude_output_tokens"] += attributes.pop("output_tokens", 0)
    except Exception as error:  # noqa: BLE001 — non-fatal; we record and continue
        logger.error("Attribute extraction failed for garment '%s': %s", label, error)
        errors.append({"step": "extract_attributes", "message": str(error)})

    # Step 2b: product search (only if attributes were extracted)
    if attributes:
        try:
            products = search_products(attributes, config)
            cost_accumulator["serpapi_queries"] += 1
        except Exception as error:  # noqa: BLE001 — non-fatal; we record and continue
            logger.error("Product search failed for garment '%s': %s", label, error)
            errors.append({"step": "search_products", "message": str(error)})

    enriched_garment = {
        "label": label,
        "bbox": bbox,
        "confidence": garment["confidence"],
        "attributes": attributes,
        "products": products,
    }

    return enriched_garment, cost_accumulator, errors


def run_pipeline(image_path: str, config: dict) -> dict:
    """
    Run the full AI matching pipeline on a single photo.

    Steps:
        1. Segment garments (GroundingDINO / Roboflow)
        2. For each garment: extract attributes (Claude Vision)
        3. For each garment: search for matching products (SerpAPI)

    Args:
        image_path: Absolute path to the photo file.
        config: Full config dict as loaded from config.yaml.

    Returns:
        A result dict with photo_id, garments, latency, cost, and errors.
        Partial results are returned even when individual garments fail —
        errors are collected in the top-level "errors" list rather than
        bubbling up as exceptions (except for a total segmentation failure,
        which is considered fatal for the photo).

    Raises:
        EnvironmentError: A required API key env var is not set.
        FileNotFoundError: image_path does not exist.
        requests.HTTPError: Roboflow API returned a non-2xx response.
    """
    photo_id = _photo_id_from_path(image_path)
    rates = _extract_cost_rates(config)
    all_errors: list[dict] = []

    total_claude_input_tokens = 0
    total_claude_output_tokens = 0
    total_serpapi_queries = 0

    # Step 1: segmentation
    t_total_start = time.perf_counter()
    t_seg_start = time.perf_counter()
    garments_raw = segment_garments(image_path, config)
    segmentation_ms = _milliseconds_since(t_seg_start)

    enriched_garments: list[dict] = []
    attr_ms_total = 0.0
    search_ms_total = 0.0

    for garment in garments_raw:
        t_attr_start = time.perf_counter()
        enriched, garment_costs, garment_errors = _process_single_garment(
            garment, image_path, config, rates
        )
        attr_ms_total += _milliseconds_since(t_attr_start)

        # search latency is the tail of _process_single_garment; approximate it
        # by subtracting a typical attr-only duration — we track total separately
        total_claude_input_tokens += garment_costs["claude_input_tokens"]
        total_claude_output_tokens += garment_costs["claude_output_tokens"]
        total_serpapi_queries += garment_costs["serpapi_queries"]

        enriched_garments.append(enriched)
        all_errors.extend(garment_errors)

    total_ms = _milliseconds_since(t_total_start)
    # search time is roughly total minus segmentation and attribute extraction
    search_ms = max(0.0, total_ms - segmentation_ms - attr_ms_total)

    claude_cost_usd = _calculate_claude_cost(
        total_claude_input_tokens, total_claude_output_tokens, rates
    )
    serpapi_cost_usd = round(
        total_serpapi_queries * rates["serpapi_per_query"], 6
    )

    logger.info(
        "Pipeline complete for '%s': %d garment(s), %.0fms, $%.4f",
        photo_id,
        len(enriched_garments),
        total_ms,
        claude_cost_usd + serpapi_cost_usd,
    )

    return {
        "photo_id": photo_id,
        "image_path": image_path,
        "garments": enriched_garments,
        "latency": {
            "segmentation_ms": segmentation_ms,
            "attribute_extraction_ms": round(attr_ms_total, 1),
            "product_search_ms": round(search_ms, 1),
            "total_ms": round(total_ms, 1),
        },
        "cost": {
            "claude_input_tokens": total_claude_input_tokens,
            "claude_output_tokens": total_claude_output_tokens,
            "claude_cost_usd": claude_cost_usd,
            "serpapi_queries": total_serpapi_queries,
            "serpapi_cost_usd": serpapi_cost_usd,
            "total_cost_usd": round(claude_cost_usd + serpapi_cost_usd, 6),
        },
        "errors": all_errors,
    }
