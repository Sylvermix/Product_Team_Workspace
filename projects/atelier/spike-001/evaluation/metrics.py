"""
Metrics computation for SPIKE-001 evaluation.

Takes graded results (human-labelled useful/not-useful per garment) and
computes the headline and supporting metrics that drive the go/no-go
decision for the spike.

This module contains only pure computation — no I/O, no API calls.
100% pytest coverage is required here because this function is the
sole source of truth for the go/no-go recommendation.
"""

import statistics
from typing import Any


def _validate_graded_results(graded_results: list[dict]) -> None:
    """
    Raise ValueError with a descriptive message if graded_results is empty
    or structurally invalid.
    """
    if not graded_results:
        raise ValueError(
            "graded_results must not be empty. "
            "Pass at least one photo with at least one garment."
        )


def _collect_garment_level_metrics(
    graded_results: list[dict],
) -> dict[str, Any]:
    """
    Walk every garment across all photos and accumulate raw counts.

    Returns a dict of counters and per-category breakdowns that
    compute_metrics() assembles into the final output.
    """
    total_garments = 0
    top3_useful_count = 0
    top1_useful_count = 0
    price_discovery_count = 0
    no_results_count = 0
    category_totals: dict[str, int] = {}
    category_top3_useful: dict[str, int] = {}

    for photo in graded_results:
        for garment in photo.get("garments", []):
            total_garments += 1
            category = garment.get("category", "unknown")
            category_totals[category] = category_totals.get(category, 0) + 1

            if garment.get("useful_match", False):
                top3_useful_count += 1
                category_top3_useful[category] = (
                    category_top3_useful.get(category, 0) + 1
                )

            if garment.get("top1_useful", False):
                top1_useful_count += 1

            if garment.get("has_price_and_url", False):
                price_discovery_count += 1

            if garment.get("no_results", False):
                no_results_count += 1

    return {
        "total_garments": total_garments,
        "top3_useful_count": top3_useful_count,
        "top1_useful_count": top1_useful_count,
        "price_discovery_count": price_discovery_count,
        "no_results_count": no_results_count,
        "category_totals": category_totals,
        "category_top3_useful": category_top3_useful,
    }


def _collect_latency_and_cost(graded_results: list[dict]) -> dict[str, Any]:
    """
    Extract per-photo latency (ms) and cost (USD) for statistical aggregation.

    Photos without latency/cost data are skipped — graded results may be
    joined from a separate pipeline output file.
    """
    latencies: list[float] = []
    costs: list[float] = []

    for photo in graded_results:
        latency = photo.get("total_ms")
        if latency is not None:
            latencies.append(float(latency))

        cost = photo.get("total_cost_usd")
        if cost is not None:
            costs.append(float(cost))

    return {"latencies": latencies, "costs": costs}


def _safe_rate(numerator: int, denominator: int) -> float:
    """Return numerator / denominator rounded to 4dp, or 0.0 if denominator is zero."""
    if denominator == 0:
        return 0.0
    return round(numerator / denominator, 4)


def _percentile(sorted_values: list[float], percentile: int) -> float:
    """
    Compute a percentile from a pre-sorted list of floats.

    Uses nearest-rank method — consistent, simple, no scipy dependency.
    """
    if not sorted_values:
        return 0.0
    rank = max(1, round(percentile / 100 * len(sorted_values)))
    return sorted_values[rank - 1]


def compute_metrics(graded_results: list[dict]) -> dict:
    """
    Compute all evaluation metrics from human-graded pipeline results.

    Args:
        graded_results: List of photo-level dicts. Each photo has:
            {
                "photo_id": str,
                "total_ms": float,         # optional — from pipeline output
                "total_cost_usd": float,   # optional — from pipeline output
                "garments": [
                    {
                        "category": str,           # optional — for breakdown
                        "useful_match": bool,      # top-3 contains ≥1 useful result
                        "top1_useful": bool,       # position-1 result is useful
                        "has_price_and_url": bool, # ≥1 result has price + URL
                        "no_results": bool,        # product search returned nothing
                    },
                    ...
                ]
            }

    Returns:
        {
            "top3_useful_match_rate": float,      # PRIMARY METRIC (target ≥0.75)
            "top1_useful_match_rate": float,
            "price_discovery_success_rate": float,
            "no_results_rate": float,
            "avg_cost_per_scan_usd": float,
            "p50_latency_ms": float,
            "p95_latency_ms": float,
            "total_photos": int,
            "total_garments": int,
            "category_breakdown": {
                "<category>": {
                    "total": int,
                    "top3_useful_rate": float,
                }
            },
        }

    Raises:
        ValueError: graded_results is empty.
    """
    _validate_graded_results(graded_results)

    counts = _collect_garment_level_metrics(graded_results)
    perf = _collect_latency_and_cost(graded_results)

    total_garments = counts["total_garments"]
    sorted_latencies = sorted(perf["latencies"])

    category_breakdown = {
        category: {
            "total": counts["category_totals"][category],
            "top3_useful_rate": _safe_rate(
                counts["category_top3_useful"].get(category, 0),
                counts["category_totals"][category],
            ),
        }
        for category in counts["category_totals"]
    }

    avg_cost = (
        round(statistics.mean(perf["costs"]), 6) if perf["costs"] else 0.0
    )

    return {
        "top3_useful_match_rate": _safe_rate(
            counts["top3_useful_count"], total_garments
        ),
        "top1_useful_match_rate": _safe_rate(
            counts["top1_useful_count"], total_garments
        ),
        "price_discovery_success_rate": _safe_rate(
            counts["price_discovery_count"], total_garments
        ),
        "no_results_rate": _safe_rate(
            counts["no_results_count"], total_garments
        ),
        "avg_cost_per_scan_usd": avg_cost,
        "p50_latency_ms": _percentile(sorted_latencies, 50),
        "p95_latency_ms": _percentile(sorted_latencies, 95),
        "total_photos": len(graded_results),
        "total_garments": total_garments,
        "category_breakdown": category_breakdown,
    }
