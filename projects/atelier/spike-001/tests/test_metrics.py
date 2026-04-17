"""
Tests for evaluation/metrics.py — compute_metrics().

This function drives the SPIKE-001 go/no-go decision, so 100% coverage
is required. All edge cases and the primary threshold (≥0.75 top-3 rate)
are explicitly tested.

Structure: one test class per logical group, parametrize for variant cases.
"""

import sys
from pathlib import Path

import pytest

# Allow imports from spike root without installing the package
_SPIKE_ROOT = Path(__file__).resolve().parent.parent
if str(_SPIKE_ROOT) not in sys.path:
    sys.path.insert(0, str(_SPIKE_ROOT))

from evaluation.metrics import (  # noqa: E402
    _percentile,
    _safe_rate,
    compute_metrics,
)


# ---------------------------------------------------------------------------
# Helpers — shared fixtures
# ---------------------------------------------------------------------------


def _make_garment(
    *,
    useful_match: bool,
    top1_useful: bool = False,
    has_price_and_url: bool = True,
    no_results: bool = False,
    category: str = "blazer",
) -> dict:
    return {
        "category": category,
        "useful_match": useful_match,
        "top1_useful": top1_useful,
        "has_price_and_url": has_price_and_url,
        "no_results": no_results,
    }


def _make_photo(
    photo_id: str,
    garments: list[dict],
    total_ms: float = 1500.0,
    total_cost_usd: float = 0.01,
) -> dict:
    return {
        "photo_id": photo_id,
        "total_ms": total_ms,
        "total_cost_usd": total_cost_usd,
        "garments": garments,
    }


# ---------------------------------------------------------------------------
# Core rate tests — the five required cases
# ---------------------------------------------------------------------------


class TestComputeMetricsTopLevelRate:
    """Tests for the primary top3_useful_match_rate metric."""

    def test_all_useful_matches_returns_rate_of_one(self) -> None:
        """When every garment is a useful match, rate should be exactly 1.0."""
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=True),
                _make_garment(useful_match=True),
            ]),
            _make_photo("P002", [
                _make_garment(useful_match=True),
            ]),
        ]

        result = compute_metrics(graded)

        assert result["top3_useful_match_rate"] == 1.0

    def test_no_useful_matches_returns_rate_of_zero(self) -> None:
        """When no garment is a useful match, rate should be exactly 0.0."""
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=False),
                _make_garment(useful_match=False),
            ]),
        ]

        result = compute_metrics(graded)

        assert result["top3_useful_match_rate"] == 0.0

    def test_mixed_exactly_at_threshold_returns_0_75(self) -> None:
        """3 useful out of 4 garments should equal exactly the 0.75 threshold."""
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=True),
                _make_garment(useful_match=True),
                _make_garment(useful_match=True),
                _make_garment(useful_match=False),
            ]),
        ]

        result = compute_metrics(graded)

        assert result["top3_useful_match_rate"] == 0.75

    def test_empty_input_raises_value_error(self) -> None:
        """An empty list must raise ValueError — not silently return zero."""
        with pytest.raises(ValueError, match="must not be empty"):
            compute_metrics([])

    def test_single_photo_single_useful_garment_returns_1_0(self) -> None:
        """Single photo, single garment, useful — rate must be 1.0."""
        graded = [
            _make_photo("P001", [_make_garment(useful_match=True)])
        ]

        result = compute_metrics(graded)

        assert result["top3_useful_match_rate"] == 1.0

    def test_single_photo_single_not_useful_garment_returns_0_0(self) -> None:
        """Single photo, single garment, not useful — rate must be 0.0."""
        graded = [
            _make_photo("P001", [_make_garment(useful_match=False)])
        ]

        result = compute_metrics(graded)

        assert result["top3_useful_match_rate"] == 0.0


# ---------------------------------------------------------------------------
# Secondary metric tests
# ---------------------------------------------------------------------------


class TestSecondaryMetrics:
    """Tests for top1, price discovery, no_results, totals."""

    def test_top1_useful_match_rate_computed_independently(self) -> None:
        """top1_useful_match_rate uses top1_useful flag, not useful_match."""
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=True, top1_useful=True),
                _make_garment(useful_match=True, top1_useful=False),
            ]),
        ]

        result = compute_metrics(graded)

        assert result["top3_useful_match_rate"] == 1.0
        assert result["top1_useful_match_rate"] == 0.5

    def test_price_discovery_rate_counts_garments_with_price_and_url(self) -> None:
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=True, has_price_and_url=True),
                _make_garment(useful_match=False, has_price_and_url=False),
                _make_garment(useful_match=False, has_price_and_url=True),
            ]),
        ]

        result = compute_metrics(graded)

        assert result["price_discovery_success_rate"] == pytest.approx(2 / 3, rel=1e-4)

    def test_no_results_rate_counts_zero_product_garments(self) -> None:
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=False, no_results=True),
                _make_garment(useful_match=False, no_results=True),
                _make_garment(useful_match=True, no_results=False),
                _make_garment(useful_match=True, no_results=False),
            ]),
        ]

        result = compute_metrics(graded)

        assert result["no_results_rate"] == 0.5

    def test_total_photos_and_garments_counted_correctly(self) -> None:
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=True),
                _make_garment(useful_match=False),
            ]),
            _make_photo("P002", [
                _make_garment(useful_match=True),
            ]),
        ]

        result = compute_metrics(graded)

        assert result["total_photos"] == 2
        assert result["total_garments"] == 3

    def test_photo_with_no_garments_counts_toward_total_photos(self) -> None:
        graded = [
            _make_photo("P001", []),
            _make_photo("P002", [_make_garment(useful_match=True)]),
        ]

        result = compute_metrics(graded)

        assert result["total_photos"] == 2
        assert result["total_garments"] == 1


# ---------------------------------------------------------------------------
# Category breakdown tests
# ---------------------------------------------------------------------------


class TestCategoryBreakdown:
    """Tests for per-category top3 useful match rates."""

    def test_category_breakdown_groups_garments_correctly(self) -> None:
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=True, category="blazer"),
                _make_garment(useful_match=False, category="blazer"),
                _make_garment(useful_match=True, category="sneakers"),
            ]),
        ]

        result = compute_metrics(graded)

        breakdown = result["category_breakdown"]
        assert breakdown["blazer"]["total"] == 2
        assert breakdown["blazer"]["top3_useful_rate"] == 0.5
        assert breakdown["sneakers"]["total"] == 1
        assert breakdown["sneakers"]["top3_useful_rate"] == 1.0

    def test_category_with_zero_useful_has_rate_zero(self) -> None:
        graded = [
            _make_photo("P001", [
                _make_garment(useful_match=False, category="hat"),
                _make_garment(useful_match=False, category="hat"),
            ]),
        ]

        result = compute_metrics(graded)

        assert result["category_breakdown"]["hat"]["top3_useful_rate"] == 0.0

    def test_category_breakdown_missing_category_key_defaults_to_unknown(self) -> None:
        """Garments without a category key should land in 'unknown' bucket."""
        graded = [
            _make_photo("P001", [
                {"useful_match": True, "top1_useful": False,
                 "has_price_and_url": True, "no_results": False}
                # no "category" key
            ]),
        ]

        result = compute_metrics(graded)

        assert "unknown" in result["category_breakdown"]
        assert result["category_breakdown"]["unknown"]["total"] == 1


# ---------------------------------------------------------------------------
# Latency and cost tests
# ---------------------------------------------------------------------------


class TestLatencyAndCost:
    """Tests for p50/p95 latency and average cost computation."""

    def test_p50_latency_is_median_of_photo_latencies(self) -> None:
        graded = [
            _make_photo("P001", [_make_garment(useful_match=True)], total_ms=1000.0),
            _make_photo("P002", [_make_garment(useful_match=True)], total_ms=2000.0),
            _make_photo("P003", [_make_garment(useful_match=True)], total_ms=3000.0),
        ]

        result = compute_metrics(graded)

        assert result["p50_latency_ms"] == 2000.0

    def test_p95_latency_selects_high_percentile_value(self) -> None:
        # 20 photos with latencies 100ms..2000ms in steps of 100ms
        latencies = [float(i * 100) for i in range(1, 21)]
        graded = [
            _make_photo(f"P{i:03d}", [_make_garment(useful_match=True)], total_ms=lat)
            for i, lat in enumerate(latencies, start=1)
        ]

        result = compute_metrics(graded)

        # p95 of 20 values: rank = max(1, round(0.95 * 20)) = 19 → 1900.0
        assert result["p95_latency_ms"] == 1900.0

    def test_avg_cost_per_scan_computed_correctly(self) -> None:
        graded = [
            _make_photo("P001", [_make_garment(useful_match=True)], total_cost_usd=0.01),
            _make_photo("P002", [_make_garment(useful_match=True)], total_cost_usd=0.03),
        ]

        result = compute_metrics(graded)

        assert result["avg_cost_per_scan_usd"] == pytest.approx(0.02, rel=1e-4)

    def test_missing_latency_data_returns_zero(self) -> None:
        """Photos without total_ms should produce zero latency metrics, not crash."""
        graded = [
            {"photo_id": "P001", "garments": [_make_garment(useful_match=True)]}
            # no total_ms or total_cost_usd
        ]

        result = compute_metrics(graded)

        assert result["p50_latency_ms"] == 0.0
        assert result["p95_latency_ms"] == 0.0
        assert result["avg_cost_per_scan_usd"] == 0.0


# ---------------------------------------------------------------------------
# Parametrized threshold boundary tests
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "useful_count, total_count, expected_rate",
    [
        (0, 1, 0.0),
        (1, 1, 1.0),
        (3, 4, 0.75),
        (75, 100, 0.75),
        (74, 100, 0.74),
        (76, 100, 0.76),
        (1, 4, 0.25),
        (2, 3, 0.6667),
    ],
)
def test_top3_useful_match_rate_boundary_values(
    useful_count: int,
    total_count: int,
    expected_rate: float,
) -> None:
    """Parametrized boundary tests to confirm rate calculation at key thresholds."""
    garments = (
        [_make_garment(useful_match=True)] * useful_count
        + [_make_garment(useful_match=False)] * (total_count - useful_count)
    )
    graded = [_make_photo("P001", garments)]

    result = compute_metrics(graded)

    assert result["top3_useful_match_rate"] == pytest.approx(
        expected_rate, abs=1e-4
    )


# ---------------------------------------------------------------------------
# Unit tests for internal helpers (ensuring 100% line coverage)
# ---------------------------------------------------------------------------


class TestInternalHelpers:
    """Direct tests for helper functions to close any coverage gaps."""

    def test_safe_rate_zero_denominator_returns_zero(self) -> None:
        assert _safe_rate(5, 0) == 0.0

    def test_safe_rate_normal_case(self) -> None:
        assert _safe_rate(1, 4) == 0.25

    def test_percentile_empty_list_returns_zero(self) -> None:
        assert _percentile([], 50) == 0.0

    def test_percentile_single_element(self) -> None:
        assert _percentile([42.0], 95) == 42.0

    def test_percentile_p100_returns_max(self) -> None:
        assert _percentile([1.0, 2.0, 3.0], 100) == 3.0

    def test_percentile_p0_returns_first(self) -> None:
        # rank = max(1, round(0)) = 1 → first element
        assert _percentile([10.0, 20.0, 30.0], 0) == 10.0
