"""
Batch evaluation runner for SPIKE-001.

Reads all photos listed in dataset_manifest.yaml (filtered to those marked
ready_for_eval), runs the full pipeline on each, writes results to a YAML
file, and prints a cost/latency summary.

Usage:
    python -m evaluation.run_eval --config config.yaml --output results/results_v1.yaml
"""

import logging
import sys
from pathlib import Path
from typing import Any

import click
import yaml

# The spike root is the parent of the evaluation package. We need this on
# sys.path so we can import pipeline.* without installing the package.
_SPIKE_ROOT = Path(__file__).resolve().parent.parent
if str(_SPIKE_ROOT) not in sys.path:
    sys.path.insert(0, str(_SPIKE_ROOT))

from pipeline.pipeline import run_pipeline  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

MANIFEST_FILENAME = "dataset_manifest.yaml"
DATASET_DIR = "dataset"
PHOTOS_DIR = "photos"


def _load_yaml(path: Path) -> Any:
    """Load and parse a YAML file; raise clearly if missing."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    with path.open("r", encoding="utf-8") as file_handle:
        return yaml.safe_load(file_handle)


def _load_config(config_path: str) -> dict:
    return _load_yaml(Path(config_path))


def _load_manifest(spike_root: Path) -> list[dict]:
    """Return the list of photo entries from dataset_manifest.yaml."""
    manifest_path = spike_root / DATASET_DIR / MANIFEST_FILENAME
    manifest = _load_yaml(manifest_path)
    return manifest.get("photos", [])


def _resolve_ready_photos(
    manifest_entries: list[dict],
    spike_root: Path,
) -> list[tuple[str, Path]]:
    """
    Filter manifest to photos marked ready_for_eval and return (photo_id, path) pairs.

    Photos without a matching file on disk are skipped with a warning so a
    missing file never aborts the whole run.
    """
    ready: list[tuple[str, Path]] = []
    photos_dir = spike_root / DATASET_DIR / PHOTOS_DIR

    for entry in manifest_entries:
        if not entry.get("ready_for_eval", False):
            continue

        photo_id = entry.get("photo_id", "UNKNOWN")
        filename = entry.get("filename", "")
        image_path = photos_dir / filename

        if not image_path.exists():
            logger.warning(
                "Photo '%s' marked ready_for_eval but file not found: %s",
                photo_id,
                image_path,
            )
            continue

        ready.append((photo_id, image_path))

    return ready


def _print_progress(
    index: int,
    total: int,
    photo_id: str,
    result: dict,
) -> None:
    """Print a one-line progress update for a completed photo."""
    garment_count = len(result.get("garments", []))
    cost_usd = result.get("cost", {}).get("total_cost_usd", 0.0)
    latency_ms = result.get("latency", {}).get("total_ms", 0.0)
    print(
        f"[{index:03d}/{total:03d}] {photo_id}"
        f" — {garment_count} garment(s) detected"
        f" — ${cost_usd:.4f}"
        f" — {latency_ms:.0f}ms"
    )


def _print_summary(
    results: list[dict],
    error_count: int,
) -> None:
    """Print a cost/latency/error summary after the full batch completes."""
    total_cost = sum(r.get("cost", {}).get("total_cost_usd", 0.0) for r in results)
    latencies = [
        r.get("latency", {}).get("total_ms", 0.0)
        for r in results
        if r.get("latency", {}).get("total_ms") is not None
    ]
    avg_latency = sum(latencies) / len(latencies) if latencies else 0.0

    print("\n" + "=" * 60)
    print(f"  Photos processed : {len(results)}")
    print(f"  Photos with errors: {error_count}")
    print(f"  Total cost        : ${total_cost:.4f}")
    print(f"  Avg latency       : {avg_latency:.0f}ms")
    print("=" * 60)


def run_evaluation(
    config_path: str,
    output_path: str,
    spike_root: Path,
) -> list[dict]:
    """
    Core evaluation logic. Separated from the CLI entry point for testability.

    Returns the list of pipeline result dicts written to output_path.
    """
    config = _load_config(config_path)
    manifest_entries = _load_manifest(spike_root)
    ready_photos = _resolve_ready_photos(manifest_entries, spike_root)

    if not ready_photos:
        logger.warning(
            "No photos are marked ready_for_eval in %s/%s/%s. "
            "Set ready_for_eval: true for each photo you want to process.",
            spike_root,
            DATASET_DIR,
            MANIFEST_FILENAME,
        )
        return []

    total = len(ready_photos)
    results: list[dict] = []
    error_count = 0

    for index, (photo_id, image_path) in enumerate(ready_photos, start=1):
        try:
            result = run_pipeline(str(image_path), config)
            results.append(result)
            _print_progress(index, total, photo_id, result)
        except Exception as error:  # noqa: BLE001 — never abort the full run on a single photo
            logger.error(
                "Pipeline failed for photo '%s' (%s): %s",
                photo_id,
                image_path,
                error,
            )
            error_count += 1
            results.append(
                {
                    "photo_id": photo_id,
                    "image_path": str(image_path),
                    "garments": [],
                    "latency": {},
                    "cost": {},
                    "errors": [{"step": "pipeline", "message": str(error)}],
                }
            )
            _print_progress(index, total, photo_id, results[-1])

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open("w", encoding="utf-8") as file_handle:
        yaml.dump(results, file_handle, default_flow_style=False, allow_unicode=True)

    logger.info("Results written to %s", output_path)
    _print_summary(results, error_count)

    return results


@click.command()
@click.option(
    "--config",
    "config_path",
    default="config.yaml",
    show_default=True,
    help="Path to config.yaml",
)
@click.option(
    "--output",
    "output_path",
    default="results/results_v1.yaml",
    show_default=True,
    help="Where to write the results YAML",
)
def main(config_path: str, output_path: str) -> None:
    """Run the SPIKE-001 evaluation batch over all ready photos."""
    # Resolve spike_root relative to this file so the CLI works regardless
    # of the working directory from which it is invoked.
    spike_root = Path(__file__).resolve().parent.parent
    run_evaluation(config_path, output_path, spike_root)


if __name__ == "__main__":
    main()
