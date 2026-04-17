# SPIKE-001: AI Product Identification Test Harness

Validates whether GroundingDINO + Claude Vision + SerpAPI can achieve
**≥75% top-3 useful match rate** on 100 fashion photos.

## Prerequisites

### System requirements

- **Python 3.11+** — check with `python3 --version`
- If Python is not installed on macOS:
  ```bash
  # Install Homebrew first (https://brew.sh)
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  # Then install Python
  brew install python
  ```

### API keys

Four API keys required. Create a `.env` file at the workspace root (never commit it — already in `.gitignore`):

```
ANTHROPIC_API_KEY=sk-ant-...
SERPAPI_KEY=...
ROBOFLOW_API_KEY=...
UNSPLASH_ACCESS_KEY=...   # only needed for dataset download
PEXELS_API_KEY=...        # only needed for dataset download
```

Load them before running:
```bash
source ../../../.env
```

Free tiers sufficient for the spike:
- Unsplash: unsplash.com/developers (50 req/hr)
- Pexels: pexels.com/api (200 req/hr)
- SerpAPI: serpapi.com (100 free searches/month)
- Roboflow: roboflow.com (free inference tier)

## Setup

```bash
pip3 install -r requirements.txt
```

Python 3.11+ required.

## Run the pipeline on a single photo

```python
import yaml
from pipeline.pipeline import run_pipeline

with open("config.yaml") as f:
    config = yaml.safe_load(f)

result = run_pipeline("/absolute/path/to/photo.jpg", config)
print(result)
```

## Run the full evaluation batch

1. Add photos to `dataset/photos/` and register them in `dataset/dataset_manifest.yaml`
   (set `ready_for_eval: true` for each photo to include).
2. Run:

```bash
python -m evaluation.run_eval --config config.yaml --output results/results_v1.yaml
```

Progress is printed as each photo completes. A cost/latency summary is printed at the end.

## Grade results

```bash
python -m evaluation.grade_ui --results results/results_v1.yaml
```

For each garment, you will see its attributes and top-3 product results.
Answer `y` (useful), `n` (not useful), or `s` (skip) for each.

To resume an interrupted grading session:

```bash
python -m evaluation.grade_ui --results results/results_v1.yaml --resume
```

Grades are saved to `results/evaluation_v1.yaml` after every photo.

## Compute metrics

```python
import yaml
from evaluation.metrics import compute_metrics

with open("results/evaluation_v1.yaml") as f:
    graded = yaml.safe_load(f)

metrics = compute_metrics(graded)
print(metrics)
```

## Pass / Fail thresholds

| Metric | Target | Source |
|---|---|---|
| `top3_useful_match_rate` | **≥ 0.75** | PRIMARY — go/no-go |
| `price_discovery_success_rate` | ≥ 0.60 | Supporting |
| `no_results_rate` | ≤ 0.10 | Supporting |
| `avg_cost_per_scan_usd` | ≤ $0.05 | Cost gate |
| `p95_latency_ms` | ≤ 5000ms | Latency gate |

The spike **passes** if `top3_useful_match_rate ≥ 0.75` on a 100-photo graded dataset.

## Run tests

```bash
python -m pytest tests/ -v
```
