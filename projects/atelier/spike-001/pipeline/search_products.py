"""
Product search via SerpAPI Google Shopping.

Translates extracted garment attributes into a search query and returns
ranked product results. Never raises on empty results — the caller is
responsible for deciding how to handle a zero-result garment.
"""

import logging
import os

from serpapi import GoogleSearch

logger = logging.getLogger(__name__)

ENV_VAR_SERPAPI_KEY = "SERPAPI_KEY"

SERPAPI_ENGINE = "google_shopping"


def _read_api_key() -> str:
    """Read the SerpAPI key from environment; raise clearly if absent."""
    api_key = os.environ.get(ENV_VAR_SERPAPI_KEY)
    if not api_key:
        raise EnvironmentError(
            f"Missing required environment variable '{ENV_VAR_SERPAPI_KEY}'. "
            "Set it before running the pipeline."
        )
    return api_key


def _build_search_query(attributes: dict) -> str:
    """
    Compose a Google Shopping query from garment attributes.

    Format: "{color_family} {category} {style_register}"
    Example: "navy blazer smart-casual"

    Keeping the query short and categorical produces better Shopping results
    than long descriptive sentences — empirically confirmed during spike design.
    """
    color = attributes.get("color_family", "")
    category = attributes.get("category", "")
    style = attributes.get("style_register", "")
    return f"{color} {category} {style}".strip()


def _parse_shopping_result(raw_result: dict, position: int) -> dict:
    """
    Normalise a single SerpAPI Shopping result into our internal format.

    SerpAPI returns heterogeneous keys depending on the retailer; we
    extract only the fields we care about and default missing ones to None
    so downstream code has a stable schema to work with.
    """
    return {
        "title": raw_result.get("title"),
        "price": raw_result.get("price"),
        "currency": raw_result.get("extracted_price") and "USD",
        "retailer": raw_result.get("source"),
        "url": raw_result.get("link"),
        "thumbnail_url": raw_result.get("thumbnail"),
        "position": position,
    }


def search_products(attributes: dict, config: dict) -> list[dict]:
    """
    Search Google Shopping for products matching the garment's attributes.

    Args:
        attributes: Dict from extract_attributes — must include at least
            category, color_family, style_register.
        config: Full pipeline config dict (as loaded from config.yaml).

    Returns:
        List of product dicts (may be empty if no results found):
        [
            {
                "title": str | None,
                "price": str | None,       # formatted, e.g. "$89.99"
                "currency": str | None,
                "retailer": str | None,
                "url": str | None,
                "thumbnail_url": str | None,
                "position": int,
            },
            ...
        ]
        Length is capped at config.pipeline.product_search.results_per_garment.

    Raises:
        EnvironmentError: SERPAPI_KEY env var not set.
        Exception: Any unexpected SerpAPI error is logged and re-raised so
            the pipeline can record it as a non-fatal per-garment error.
    """
    search_config = config["pipeline"]["product_search"]
    results_per_garment = search_config["results_per_garment"]
    country = search_config["country"]

    api_key = _read_api_key()
    query = _build_search_query(attributes)

    logger.debug("Searching Google Shopping for: '%s'", query)

    search_params = {
        "engine": SERPAPI_ENGINE,
        "q": query,
        "gl": country,
        "api_key": api_key,
        "num": results_per_garment,
    }

    try:
        search = GoogleSearch(search_params)
        results = search.get_dict()
    except Exception as error:
        logger.error(
            "SerpAPI search failed for query '%s': %s", query, error
        )
        raise

    shopping_results = results.get("shopping_results", [])

    if not shopping_results:
        logger.warning(
            "No Google Shopping results for query '%s'.", query
        )
        return []

    parsed = [
        _parse_shopping_result(raw, position=index + 1)
        for index, raw in enumerate(shopping_results[:results_per_garment])
    ]

    logger.info(
        "Found %d product result(s) for query '%s'", len(parsed), query
    )
    return parsed
