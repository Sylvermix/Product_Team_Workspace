"""
SPIKE-001 Dataset Downloader
Downloads 55 fashion photos from Unsplash and Pexels, auto-populates manifest.

Usage:
    export UNSPLASH_ACCESS_KEY=your_key
    export PEXELS_API_KEY=your_key
    python -m dataset.download

APIs (both free):
    Unsplash: https://unsplash.com/developers  (50 req/hr on free tier)
    Pexels:   https://www.pexels.com/api/      (200 req/hr on free tier)

The remaining 45 photos (Wikimedia + consented + synthetic) are sourced manually.
See dataset/MANUAL_SOURCING.md for instructions.
"""

import os
import time
import yaml
import requests
from pathlib import Path
from dataclasses import dataclass, field

# ── Constants ────────────────────────────────────────────────────────────────

UNSPLASH_BASE = "https://api.unsplash.com"
PEXELS_BASE = "https://api.pexels.com/v1"

PHOTOS_DIR = Path(__file__).parent / "photos"
MANIFEST_PATH = Path(__file__).parent / "dataset_manifest.yaml"

# Download plan: (source, query, count, photo_type_tag)
# Targets the diversity breakdown from the spike plan.
DOWNLOAD_PLAN: list[tuple[str, str, int, str]] = [
    # ── Unsplash — ~30 photos ─────────────────────────────────────────────
    ("unsplash", "fashion blazer jacket outfit",         5, "on-body-editorial"),
    ("unsplash", "street style fashion outfit",          5, "street-style"),
    ("unsplash", "flat lay clothing outfit",             4, "flat-lay"),
    ("unsplash", "fashion dress editorial",              4, "on-body-editorial"),
    ("unsplash", "fashion accessories bag hat",          4, "on-body-editorial"),
    ("unsplash", "sneakers shoes fashion",               4, "e-commerce"),
    ("unsplash", "fashion mirror selfie outfit",         4, "mirror-selfie"),
    # ── Pexels — ~25 photos ───────────────────────────────────────────────
    ("pexels",   "fashion outfit street style",          5, "street-style"),
    ("pexels",   "clothing flat lay knolling",           4, "flat-lay"),
    ("pexels",   "mirror selfie fashion outfit",         4, "mirror-selfie"),
    ("pexels",   "fashion dress woman editorial",        4, "on-body-editorial"),
    ("pexels",   "shoes boots fashion product",          4, "e-commerce"),
    ("pexels",   "jacket coat fashion outdoor",          4, "street-style"),
]

# Maps query → garment category hint (for ground truth pre-fill)
QUERY_CATEGORY_HINTS: dict[str, list[str]] = {
    "blazer jacket outfit":     ["blazer"],
    "street style fashion":     ["jacket", "trousers"],
    "flat lay clothing":        ["shirt"],
    "dress editorial":          ["dress"],
    "accessories bag hat":      ["bag", "hat"],
    "sneakers shoes":           ["sneakers"],
    "mirror selfie":            ["top", "jeans"],
    "jacket coat":              ["coat"],
    "boots fashion":            ["boots"],
}

# ── Data classes ─────────────────────────────────────────────────────────────

@dataclass
class PhotoRecord:
    photo_id: str
    filename: str
    source: str
    license: str
    ready_for_eval: bool = False
    source_url: str = ""
    attribution: str = ""
    query: str = ""
    photo_type: str = ""
    category_hints: list[str] = field(default_factory=list)


# ── API clients ──────────────────────────────────────────────────────────────

def _unsplash_headers() -> dict[str, str]:
    key = os.environ.get("UNSPLASH_ACCESS_KEY", "")
    if not key:
        raise EnvironmentError("UNSPLASH_ACCESS_KEY is not set")
    return {"Authorization": f"Client-ID {key}"}


def _pexels_headers() -> dict[str, str]:
    key = os.environ.get("PEXELS_API_KEY", "")
    if not key:
        raise EnvironmentError("PEXELS_API_KEY is not set")
    return {"Authorization": key}


def search_unsplash(query: str, count: int, page: int = 1) -> list[dict]:
    resp = requests.get(
        f"{UNSPLASH_BASE}/search/photos",
        headers=_unsplash_headers(),
        params={"query": query, "per_page": count, "page": page, "orientation": "portrait"},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json().get("results", [])


def search_pexels(query: str, count: int, page: int = 1) -> list[dict]:
    resp = requests.get(
        f"{PEXELS_BASE}/search",
        headers=_pexels_headers(),
        params={"query": query, "per_page": count, "page": page, "orientation": "portrait"},
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json().get("photos", [])


# ── Download helpers ──────────────────────────────────────────────────────────

def _download_file(url: str, dest: Path) -> bool:
    try:
        resp = requests.get(url, timeout=30, stream=True)
        resp.raise_for_status()
        dest.write_bytes(resp.content)
        return True
    except requests.RequestException as e:
        print(f"    ✗ Download failed: {e}")
        return False


def _category_hints_for_query(query: str) -> list[str]:
    for fragment, hints in QUERY_CATEGORY_HINTS.items():
        if any(w in query for w in fragment.split()):
            return hints
    return []


# ── Core download logic ───────────────────────────────────────────────────────

def download_unsplash_batch(
    query: str, count: int, photo_type: str, start_id: int
) -> list[PhotoRecord]:
    print(f"  Unsplash [{count}] '{query}'")
    results = search_unsplash(query, count)
    records: list[PhotoRecord] = []

    for i, photo in enumerate(results[:count]):
        photo_id = f"P{start_id + i:03d}"
        filename = f"{photo_id}.jpg"
        dest = PHOTOS_DIR / filename
        url = photo["urls"]["regular"]

        print(f"    → {photo_id} ", end="", flush=True)
        ok = _download_file(url, dest)
        if ok:
            print("✓")
            records.append(PhotoRecord(
                photo_id=photo_id,
                filename=filename,
                source="unsplash",
                license="unsplash",
                ready_for_eval=True,
                source_url=photo["links"]["html"],
                attribution=f"Photo by {photo['user']['name']} on Unsplash",
                query=query,
                photo_type=photo_type,
                category_hints=_category_hints_for_query(query),
            ))
        time.sleep(0.5)  # stay within 50 req/hr

    return records


def download_pexels_batch(
    query: str, count: int, photo_type: str, start_id: int
) -> list[PhotoRecord]:
    print(f"  Pexels  [{count}] '{query}'")
    results = search_pexels(query, count)
    records: list[PhotoRecord] = []

    for i, photo in enumerate(results[:count]):
        photo_id = f"P{start_id + i:03d}"
        filename = f"{photo_id}.jpg"
        dest = PHOTOS_DIR / filename
        url = photo["src"]["large"]

        print(f"    → {photo_id} ", end="", flush=True)
        ok = _download_file(url, dest)
        if ok:
            print("✓")
            records.append(PhotoRecord(
                photo_id=photo_id,
                filename=filename,
                source="pexels",
                license="pexels",
                ready_for_eval=True,
                source_url=photo["url"],
                attribution=f"Photo by {photo['photographer']} on Pexels",
                query=query,
                photo_type=photo_type,
                category_hints=_category_hints_for_query(query),
            ))
        time.sleep(0.3)

    return records


# ── Manifest helpers ──────────────────────────────────────────────────────────

def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        with MANIFEST_PATH.open() as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data.get("photos"), list):
            data["photos"] = []
        return data
    return {"version": "1.0", "total_photos": 0, "photos": []}


def save_manifest(manifest: dict, records: list[PhotoRecord]) -> None:
    existing_ids = {p["photo_id"] for p in manifest["photos"]}
    for r in records:
        if r.photo_id not in existing_ids:
            manifest["photos"].append({
                "photo_id": r.photo_id,
                "filename": r.filename,
                "source": r.source,
                "license": r.license,
                "ready_for_eval": r.ready_for_eval,
                "source_url": r.source_url,
                "attribution": r.attribution,
                "query": r.query,
                "photo_type": r.photo_type,
                "category_hints": r.category_hints,
            })
    manifest["total_photos"] = len(manifest["photos"])
    manifest["photos"].sort(key=lambda p: p["photo_id"])
    with MANIFEST_PATH.open("w") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"\nManifest updated → {manifest['total_photos']} photos total")


# ── Entry point ───────────────────────────────────────────────────────────────

def run_download() -> None:
    PHOTOS_DIR.mkdir(exist_ok=True)
    manifest = load_manifest()
    existing_ids = {p["photo_id"] for p in manifest["photos"]}

    # Figure out next available ID
    taken_nums = {int(pid[1:]) for pid in existing_ids if pid.startswith("P") and pid[1:].isdigit()}
    next_id = max(taken_nums, default=0) + 1

    all_records: list[PhotoRecord] = []

    print("\n── Downloading dataset photos ──────────────────────────────────")
    for source, query, count, photo_type in DOWNLOAD_PLAN:
        try:
            if source == "unsplash":
                records = download_unsplash_batch(query, count, photo_type, next_id)
            else:
                records = download_pexels_batch(query, count, photo_type, next_id)
            all_records.extend(records)
            next_id += len(records)
        except EnvironmentError as e:
            print(f"  ✗ Skipping {source}: {e}")
        except requests.HTTPError as e:
            print(f"  ✗ API error on '{query}': {e}")

    save_manifest(manifest, all_records)

    downloaded = len(all_records)
    print(f"\n✓ Downloaded {downloaded} photos")
    print(f"  Photos dir: {PHOTOS_DIR}")
    print(f"  Manifest:   {MANIFEST_PATH}")
    print(f"\nNext: add remaining ~45 photos manually (see dataset/MANUAL_SOURCING.md)")
    print(      "Then: run ground truth labeling BEFORE any model evaluation")


if __name__ == "__main__":
    run_download()
