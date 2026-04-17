"""
CLI grading tool for SPIKE-001 evaluation.

Displays each photo's garment attributes and top-3 product results (text
only — no image rendering), prompts the grader to mark each as useful or
not, and saves grades to an evaluation YAML file.

Usage:
    python -m evaluation.grade_ui --results results/results_v1.yaml
    python -m evaluation.grade_ui --results results/results_v1.yaml --resume
"""

import sys
from pathlib import Path
from typing import Any

import click
import yaml

_SPIKE_ROOT = Path(__file__).resolve().parent.parent
if str(_SPIKE_ROOT) not in sys.path:
    sys.path.insert(0, str(_SPIKE_ROOT))

# Number of top products shown per garment during grading
TOP_K_DISPLAY = 3

GRADE_YES = "y"
GRADE_NO = "n"
GRADE_SKIP = "s"
VALID_GRADES = {GRADE_YES, GRADE_NO, GRADE_SKIP}

EVALUATION_OUTPUT_DEFAULT = "results/evaluation_v1.yaml"


def _load_yaml(path: Path) -> Any:
    """Load and parse a YAML file. Raises FileNotFoundError if absent."""
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with path.open("r", encoding="utf-8") as file_handle:
        return yaml.safe_load(file_handle) or []


def _save_yaml(data: Any, path: Path) -> None:
    """Write data to a YAML file, creating parent directories if needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file_handle:
        yaml.dump(data, file_handle, default_flow_style=False, allow_unicode=True)


def _load_existing_grades(eval_path: Path) -> dict[str, Any]:
    """
    Load previously saved grades indexed by photo_id.

    Returns an empty dict if the file does not exist yet — this is the
    normal state on first run.
    """
    if not eval_path.exists():
        return {}
    existing = _load_yaml(eval_path)
    return {entry["photo_id"]: entry for entry in (existing or [])}


def _format_attributes(attributes: dict) -> str:
    """Format garment attributes as a compact readable string."""
    if not attributes:
        return "(no attributes — extraction failed)"
    parts = [
        f"category={attributes.get('category', '?')}",
        f"color={attributes.get('color_family', '?')}",
        f"style={attributes.get('style_register', '?')}",
        f"tier={attributes.get('price_tier', '?')}",
    ]
    description = attributes.get("description", "")
    return "  " + " | ".join(parts) + (f"\n  desc: {description}" if description else "")


def _format_product(product: dict, rank: int) -> str:
    """Format a single product result for display."""
    title = product.get("title") or "(no title)"
    price = product.get("price") or "(no price)"
    retailer = product.get("retailer") or "(unknown retailer)"
    url = product.get("url") or "(no URL)"
    return f"  [{rank}] {title}\n      {price} @ {retailer}\n      {url}"


def _prompt_for_grade(prompt_text: str) -> str:
    """
    Prompt the grader for a y/n/s answer. Repeats until a valid answer is given.
    """
    while True:
        answer = input(prompt_text).strip().lower()
        if answer in VALID_GRADES:
            return answer
        print(f"  Please enter y (yes), n (no), or s (skip). Got: '{answer}'")


def _grade_garment(
    garment: dict,
    garment_index: int,
    total_garments: int,
) -> dict:
    """
    Display a garment and its products, collect a useful_match grade.

    Returns a graded garment dict ready for inclusion in evaluation output.
    """
    label = garment.get("label", "unknown")
    attributes = garment.get("attributes", {})
    products = garment.get("products", [])

    print(f"\n  Garment {garment_index}/{total_garments}: {label}")
    print(_format_attributes(attributes))

    top_products = products[:TOP_K_DISPLAY]

    if not top_products:
        print("  (no product results)")
        top1_useful = False
        useful_match = False
        has_price_and_url = False
        no_results = True
    else:
        print(f"\n  Top-{len(top_products)} product results:")
        for rank, product in enumerate(top_products, start=1):
            print(_format_product(product, rank))

        has_price_and_url = any(
            product.get("price") and product.get("url")
            for product in top_products
        )
        no_results = False

        grade = _prompt_for_grade(
            "\n  Is this a useful match (any of the top results)? [y/n/s(kip)]: "
        )

        if grade == GRADE_SKIP:
            return {
                "label": label,
                "skipped": True,
                "useful_match": None,
                "top1_useful": None,
                "has_price_and_url": has_price_and_url,
                "no_results": no_results,
            }

        useful_match = grade == GRADE_YES

        if useful_match and len(top_products) >= 1:
            top1_grade = _prompt_for_grade(
                "  Is the TOP-1 result specifically useful? [y/n/s(kip)]: "
            )
            top1_useful = top1_grade == GRADE_YES
        else:
            top1_useful = False

    return {
        "label": label,
        "skipped": False,
        "useful_match": useful_match,
        "top1_useful": top1_useful,
        "has_price_and_url": has_price_and_url,
        "no_results": no_results,
    }


def grade_results(
    results_path: str,
    eval_output_path: str,
    resume: bool,
) -> None:
    """
    Core grading logic. Separated from CLI entry point for testability.
    """
    results_file = Path(results_path)
    eval_file = Path(eval_output_path)

    pipeline_results = _load_yaml(results_file)
    existing_grades = _load_existing_grades(eval_file) if resume else {}

    graded_photos: list[dict] = list(existing_grades.values())
    already_graded_ids = set(existing_grades.keys())

    photos_to_grade = [
        photo
        for photo in pipeline_results
        if photo.get("photo_id") not in already_graded_ids
    ]

    if not photos_to_grade:
        print("All photos have already been graded. Nothing to do.")
        print(f"Grades are in: {eval_file}")
        return

    total_photos = len(photos_to_grade)
    print(f"\nGrading {total_photos} photo(s). Grades saved to: {eval_file}")
    print("For each garment, you will see its attributes and top products.")
    print("Grade: y = useful match, n = not useful, s = skip\n")

    for photo_index, photo in enumerate(photos_to_grade, start=1):
        photo_id = photo.get("photo_id", f"photo_{photo_index}")
        garments = photo.get("garments", [])

        print(f"\n{'=' * 60}")
        print(f"Photo {photo_index}/{total_photos}: {photo_id}")
        print(f"{'=' * 60}")

        if not garments:
            print("  (no garments detected — skipping)")
            graded_photos.append(
                {"photo_id": photo_id, "garments": [], "skipped": True}
            )
            _save_yaml(graded_photos, eval_file)
            continue

        graded_garments: list[dict] = []
        for garment_index, garment in enumerate(garments, start=1):
            graded_garment = _grade_garment(garment, garment_index, len(garments))
            graded_garments.append(graded_garment)

        graded_photo = {"photo_id": photo_id, "garments": graded_garments}
        graded_photos.append(graded_photo)

        # Save after every photo so a Ctrl+C does not lose work
        _save_yaml(graded_photos, eval_file)
        print(f"\n  Grades saved ({photo_index}/{total_photos} photos done)")

    print(f"\nGrading complete. Results written to: {eval_file}")


@click.command()
@click.option(
    "--results",
    "results_path",
    default="results/results_v1.yaml",
    show_default=True,
    help="Pipeline results file to grade",
)
@click.option(
    "--output",
    "eval_output_path",
    default=EVALUATION_OUTPUT_DEFAULT,
    show_default=True,
    help="Where to write graded evaluation YAML",
)
@click.option(
    "--resume",
    is_flag=True,
    default=False,
    help="Resume from the last graded photo (skip already-graded photos)",
)
def main(results_path: str, eval_output_path: str, resume: bool) -> None:
    """Grade pipeline results — display attributes + products, record useful/not-useful."""
    grade_results(results_path, eval_output_path, resume)


if __name__ == "__main__":
    main()
