# SPIKE-001 Plan: AI Product Identification Feasibility

**Spike ID**: SPIKE-001
**Author**: product-tech
**Date**: 2026-04-16
**Sprint**: 2026-04-16 → 2026-04-30
**Blocks**: US-010 (Scan feature — core differentiator)
**Status**: planned

---

## 1. Spike Summary

### Hypothesis

With current off-the-shelf AI models (SAM 2 or GroundingDINO for segmentation, CLIP-based embeddings for retrieval, SerpAPI / Amazon PA-API for product search), we can achieve a **≥75% top-3 useful match rate** on a diverse test set of 100 fashion photos within the 6-second latency budget and the $0.02/scan cost ceiling.

### What "useful match" means operationally

This definition is the single most consequential design choice of the spike. We define a match as useful using a **substitutability test**, not an exact-item test:

> A match is **useful** if a user who sees the detected garment in the source photo would seriously consider purchasing the matched product as an equivalent or compelling alternative — same general category, close color family, compatible style register (casual/smart/formal), and within a price range ±50% of the visible garment's estimated price tier.

This breaks down into four testable criteria, all of which must pass:

| Criterion | Definition | Grading |
|---|---|---|
| **Category** | Matched item is the same garment type (e.g., cropped blazer → blazer; midi skirt → skirt). Shoes do not match pants. | Pass / Fail |
| **Color family** | Matched item's dominant color is within the same family (black, white, red, blue/navy, green, brown/tan, grey, pink, yellow, purple, orange, print/pattern). Adjacent families acceptable (navy → black). One family away = fail. | Pass / Fail |
| **Style register** | Both items share the same dressing context: streetwear, casual, smart-casual, formal/tailored, athleisure, eveningwear. A tuxedo jacket does not substitute a denim jacket. | Pass / Fail |
| **Not absurd price tier** | If the visible garment is clearly budget (e.g., H&M-tier), matching to $800 items fails. If it is clearly luxury, matching to $15 items fails. Three tiers: budget (<$80), mid ($80-$350), premium (>$350). Must match within the same tier or one adjacent. | Pass / Fail |

A match that passes all four criteria is a **useful match**. Top-3 useful match rate = fraction of test photos where at least one of the top three returned products is a useful match for the most prominent garment in the photo.

**Why this definition, not exact-item matching**: exact-item matching is nearly impossible without product barcodes or indexed-retailer partnerships — it would guarantee failure before we start. Substitutability is what users actually want ("where can I get something like that?"). The context.md vision statement says "find similar items," not "find the exact item."

**Why not simpler (category only)**: category-only matching is too low a bar — returning any shirt when the user photographs a silk blouse is not useful. We need enough precision to drive real tap-through behavior.

### Pass/fail threshold

| Outcome | Top-3 useful match rate | Decision |
|---|---|---|
| **Pass** | ≥75% | Commit to US-010 as specced |
| **Partial** | 60–74% | Run extended spike; propose scope changes to US-010 |
| **Fail** | <60% | Halt; reassess core hypothesis; document pivot options |

---

## 2. Pipeline Under Test

The end-to-end flow we are validating. Each step is named with the candidate service.

```
INPUT PHOTO
    │
    ▼
[Step 1] GARMENT SEGMENTATION
    Candidate: SAM 2 (Meta, local inference) OR GroundingDINO (text-prompted)
    Output: per-garment segmentation masks + bounding boxes
    │
    ▼
[Step 2] GARMENT ATTRIBUTE EXTRACTION
    Candidate A: CLIP ViT-L/14 (zero-shot) — embeddings + category/color probing
    Candidate B: OpenFashionCLIP (fashion-fine-tuned CLIP) — same interface, better domain
    Candidate C: Claude Vision (claude-sonnet-4-6) — structured JSON output for category/color/style
    Output: per-garment { category, color, style_register, description_text }
    │
    ▼
[Step 3] PRODUCT RETRIEVAL (two parallel paths)
    Path A — Text-to-product search:
        Build search query from attributes → SerpAPI Google Shopping OR Amazon PA-API
        Output: ranked product list with image, title, price, retailer, URL
    Path B — Embedding-based similarity search (if catalog indexed):
        CLIP/FashionCLIP embedding of garment crop → nearest-neighbor search in Qdrant
        Output: ranked product list from indexed catalog
    │
    ▼
[Step 4] RESULT RANKING + DEDUP
    Merge Path A + Path B results, deduplicate, re-rank by relevance signal
    Output: top-5 products per garment
    │
    ▼
DISPLAYED RESULTS
```

**Primary pipeline for the spike** (cheapest-first approach):
Step 1: GroundingDINO (API-accessible, no GPU required to start)
Step 2: Claude Vision for attribute extraction (best structured output, no fine-tuning overhead)
Step 3: SerpAPI Google Shopping (text query from extracted attributes)

**Alternative pipeline** (to A/B if primary underperforms):
Step 1: SAM 2 (requires GPU; richer masks but no text prompt — needs Step 2 first for category)
Step 2: OpenFashionCLIP embeddings
Step 3: Qdrant vector search over a pre-indexed product catalog (Shopstyle feed or scraped dataset)

The primary pipeline is faster to set up and eliminates the catalog-indexing overhead of Path B. If the text-query approach achieves ≥75%, we do not need to build a vector index for MVP. If it falls short, Path B becomes the priority investigation.

---

## 3. Models and Services to Evaluate

### 3.1 Segmentation

| Model | Approach | Pros | Cons | Spike verdict |
|---|---|---|---|---|
| **SAM 2** (Meta) | Promptable segmentation via point/box | Best mask quality; handles occlusion well; open-source | Needs GPU for real-time; complex prompting without a detector upstream; no garment awareness natively | Secondary option — valuable if GroundingDINO masks are too coarse |
| **GroundingDINO** | Text-prompted open-set object detection | API-accessible (via Roboflow hosted or HuggingFace Inference); returns bounding boxes with text labels; garment-aware when prompted with clothing categories | Bounding boxes not pixel masks; may miss layered garments | **Primary choice** — low barrier, no GPU, testable on day 1 |
| **Fashionpedia-trained models** | Fine-tuned on Fashionpedia dataset (27 fine-grained categories) | Best garment taxonomy accuracy | Models are older (2020-era); need self-hosting; limited community maintenance | Evaluate only if GroundingDINO + SAM 2 both fail on niche garments |

**Recommended path**: Start with GroundingDINO (bounding box). If mask quality matters for the attribute extraction step, layer SAM 2 on top of GroundingDINO's bounding boxes (GroundingDINO → SAM 2 is a known effective combo).

### 3.2 Classification and Attribute Extraction

| Model | Approach | Pros | Cons | Spike verdict |
|---|---|---|---|---|
| **CLIP ViT-L/14** (OpenAI) | Zero-shot image-text similarity | Fast, cheap inference; well-documented; cosine probe for color/category | Generic training — not fashion-specific; struggles with fine-grained style distinctions | Baseline / fallback |
| **OpenFashionCLIP** | CLIP fine-tuned on e-commerce fashion data | Better fashion-domain accuracy than base CLIP; open weights | Less documentation; smaller community; requires self-hosting | A/B test vs Claude Vision |
| **Claude Vision** (claude-sonnet-4-6) | Structured JSON extraction via prompt | Highest accuracy for nuanced attribute extraction; handles edge cases (pattern, texture); returns structured output natively; style register judgment | Higher latency (~2-3s per garment); higher cost (~$0.003-0.005 per garment crop); API rate limits | **Primary choice** for attribute extraction in spike |
| **GPT-4V / Gemini** | Same VLM approach | Comparable quality | Vendor diversification; not materially better for this task | Do not evaluate in this spike — focus resources on Claude Vision; revisit if cost is a blocker |

**Why Claude Vision as primary**: the spike needs to understand the ceiling of what's achievable. Claude Vision gives the best attribute extraction we can get today without fine-tuning. If the pipeline fails with the best possible attributes, the problem is in retrieval, not extraction. If it passes, we evaluate whether a cheaper model (OpenFashionCLIP) can match it in a follow-on cost-reduction pass.

### 3.3 Embedding and Retrieval

| Approach | Setup | Pros | Cons | Spike verdict |
|---|---|---|---|---|
| **Text query → SerpAPI Google Shopping** | SerpAPI API key ($50/5k queries) | No catalog needed; searches live inventory; broad coverage | No visual similarity; results depend on query quality; SerpAPI cost; rate limits | **Primary for spike** — test this first |
| **CLIP embeddings + pgvector** | Postgres + pgvector extension | In-stack; no extra infra; familiar | Need to index a catalog; CLIP embeddings not fashion-optimized | Evaluate in phase 2 of spike if text search underperforms |
| **OpenFashionCLIP embeddings + Qdrant** | Self-hosted Qdrant (free tier), Python client | Fashion-optimized embeddings; fast ANN search | Catalog indexing work upfront; Qdrant ops overhead | Evaluate in phase 2 — if text search falls short |

**Decision logic**: if SerpAPI text-query approach achieves ≥75%, vector search is deferred to a post-spike optimization. If text query lands at 60-74%, vector search over a pre-indexed catalog becomes the spike extension.

### 3.4 Product Search APIs

| Source | Access model | Coverage | Cost | Constraints |
|---|---|---|---|---|
| **SerpAPI (Google Shopping)** | REST API, paid | Broad global coverage; major retailers | ~$0.001/query (50k queries = $50/mo) | ToS restricts scraping; API use is legitimate — verify commercial terms |
| **Amazon PA-API** | Official affiliate API | Amazon catalog only; very deep | Free with affiliate tag | Requires active affiliate account; 1 req/s rate limit; strict ToS on caching |
| **Bing Visual Search API** | Azure Cognitive Services | Visual query path available | $1/1000 transactions | Requires Azure account; not battle-tested for fashion |
| **Shopstyle / Rakuten** | Product feed + API | Fashion-focused; 12M+ products | Free with affiliate agreement | Requires application; fashion-native is a plus |
| **ASOS / Zalando APIs** | Partner programs | Focused retailer coverage | Free with partnership | Requires retailer partnership application; not available immediately |

**For the spike**: SerpAPI (broad coverage, minimal setup) + Shopstyle/Rakuten feed (fashion-native depth). Amazon PA-API is worth including if affiliate account is already in place.

---

## 4. Test Dataset

### Size and rationale

Target: **100 photos**. This is sufficient to detect a ≥75% rate with a 95% confidence interval of approximately ±8.5 percentage points (binomial CI). Not publication-grade, but adequate for a go/no-go spike. If results cluster near the threshold (70-80%), we extend to 150 photos in the partial outcome path.

### Composition breakdown

The 100 photos must be deliberately diverse. Over-indexing on any single cell biases results and gives false confidence.

| Dimension | Breakdown |
|---|---|
| **Garment category** | Tops 25 (t-shirt, shirt, blouse, jacket, coat), Bottoms 20 (trousers, jeans, skirt, shorts), Full-body 15 (dress, jumpsuit, suit), Footwear 15 (trainers, boots, heels, sandals), Accessories 15 (bag, hat, scarf, sunglasses), Outerwear 10 (puffer, trench, blazer) |
| **Photo type** | Flat lay 15, On-body (editorial/styled) 25, Street style / candid 25, Mirror selfie 20, E-commerce product shot (control) 15 |
| **Lighting** | Studio/bright 35, Natural outdoor 40, Indoor ambient 15, Low light / mixed 10 |
| **Skin tone** | Distributed across Fitzpatrick scale I-VI; no single tone >20% of on-body shots |
| **Body type** | On-body shots distributed across straight, curvy, petite, tall; no single archetype >25% |
| **Gender presentation** | Masc-presenting 35, Femme-presenting 40, Androgynous/non-binary 15, Children's/teen 10 |
| **Season / color palette** | Warm tones 25, Cool tones 25, Neutral/monochrome 25, Pattern/print 25 |
| **Niche garment types** | 15 "hard" cases: kimonos, sarees, traditional garments, highly patterned items, heavily layered looks |

**Bias audit**: before finalizing the dataset, verify that:
- No single source contributes >40% of photos (avoids style-source overfit)
- Western fashion editorial does not dominate (cap at 50%)
- Body type distribution is not just straight-size — include at least 20 photos with plus-size or non-normative body types

### Sourcing

| Source | Volume | Notes | License |
|---|---|---|---|
| **Unsplash** (fashion tag) | ~30 photos | High quality, broad styles | CC0 / Unsplash license — usable for research |
| **Pexels** (fashion / style tags) | ~25 photos | Similar quality to Unsplash | CC0 — usable |
| **Wikimedia Commons** (fashion photography category) | ~15 photos | Includes editorial and cultural dress | Varies by image — verify per photo |
| **Public editorial archives** (Vogue runway public web images) | ~10 photos | High-end editorial; good for styled looks | Fair use for internal evaluation only — do NOT include in any distributed dataset |
| **Creator-consented photos** (solicit from human owner's network) | ~10 photos | Real-user phone photos; mirror selfies; street style | Explicit consent required; store consent record |
| **Synthetic / generated** (Stable Diffusion fashion LoRAs) | ~10 photos | Fill gaps in underrepresented categories | No license issues — generated by us |

**Licensing note**: the dataset is for internal spike evaluation only. It is not redistributed. This is the lowest-risk licensing posture. If the spike is published externally or used for fine-tuning, re-evaluate each source's terms.

### Ground truth labeling

Each photo gets a ground truth record before evaluation:

```yaml
photo_id: "P042"
source: "unsplash"
garments:
  - category: "blazer"
    color_family: "black"
    style_register: "smart-casual"
    price_tier: "mid"
    notes: "Single-button, slightly oversized, worn open over white tee"
grader_initials: "SL"
graded_at: "2026-04-18"
```

Ground truth is defined by the human owner (or a designated fashion-literate reviewer) before running any model output — to avoid anchoring bias. No model should be run before ground truth is locked for each photo.

### Storage and versioning

- Photos stored in `/spike-001/dataset/photos/` in the project S3 bucket (or local during spike)
- Ground truth stored as `dataset_ground_truth.yaml` in the same directory
- Dataset is **version-tagged** (`v1.0`) before any evaluation run
- No modifications to the dataset after evaluation begins — if a photo must be replaced, create a `v1.1` with a change log

---

## 5. Evaluation Methodology

### Primary metric

**Top-3 useful match rate**: fraction of photos where at least one of the top three returned matches is a useful match (per the definition in Section 1) for the primary garment in the photo.

### Full metric suite

| Metric | Definition | Target |
|---|---|---|
| Top-1 useful match rate | Useful match in position 1 | Track only — no target |
| Top-3 useful match rate | **Primary gate metric** | ≥75% |
| Top-5 useful match rate | Useful match in first 5 | Track only — directional |
| Category accuracy | Matched item's category correct | Track by category |
| Color family accuracy | Matched item's color family correct | Track — expect high |
| Price discovery success | At least 1 result has a buyable URL + visible price | ≥90% — table-stakes |
| Cost per scan | Total API spend / number of scans | Measure; target <$0.02 production ceiling |
| Latency p50 / p95 | Measured end-to-end: upload receipt → final results JSON | p50 <3s, p95 <6s |

### Segmentation before matching

We also log, per photo: did the segmentation correctly detect the primary garment? This separates pipeline failures: "segmentation missed the garment" is a different failure mode from "segmentation correct but retrieval failed." Log segmentation precision separately.

### Human grading protocol

**Who grades**: the human owner of the project, or a designated fashion-literate reviewer. For inter-rater reliability, a 20% random sample (20 photos) is graded independently by a second reviewer.

**Grading rubric** (per result):

```
For each top-3 result, for each garment in the photo:
1. Category match?           [yes / no]
2. Color family match?       [yes / no]
3. Style register match?     [yes / no]
4. Price tier match?         [yes / no / cannot_tell]
5. Overall useful?           [yes / no]   ← recorded in aggregates

Notes: [optional — flag ambiguous cases]
```

The grader makes the `useful` call based on all four criteria. If any criterion fails, the match is not useful. Graders should not know the model version when grading (where possible) to reduce confirmation bias.

**Inter-rater reliability**: calculate Cohen's kappa on the 20 overlapping photos. If kappa < 0.7, the rubric is ambiguous — convene a calibration session before proceeding.

**Grading tooling**: a simple local Python script or Google Sheet with the photo displayed alongside the top-3 results. No special tooling required for the spike.

### Cost measurement

Cost per scan = sum of:
- Segmentation API calls (GroundingDINO hosted: measured per call)
- Attribute extraction (Claude Vision: measured via API usage logs, typically $0.003-0.008 per garment depending on image size)
- Product search (SerpAPI: measured at $0.001 per query × queries per scan; typically 1-3 queries per detected garment)
- Embedding generation (if path B is evaluated: OpenAI or self-hosted, near-zero at spike scale)

Track cost per photo in a spreadsheet. Project to: cost per scan at 1k/day, 10k/day, 100k/day (with assumed caching rates).

### Latency measurement

Measure wall-clock time at each pipeline stage:
1. Upload receipt → segmentation complete
2. Segmentation complete → attributes extracted
3. Attributes extracted → product search results returned
4. Results returned → response JSON assembled

Log p50 and p95 across all 100 photos. The 6-second budget (from context.md) is the non-negotiable ceiling. If p95 exceeds 6s, flag immediately — this is a pipeline architecture concern, not a model accuracy concern.

**Latency during the spike is not production-optimized** (no caching, no parallelism). Document what parallelization and caching would save. For example, garment crops can be sent to Claude Vision in parallel; product searches for multiple garments can run in parallel.

### Failure mode catalog

Document every failure case encountered:

| Failure mode | Example | Root cause | Mitigation to test |
|---|---|---|---|
| Missed garment | Accessory not detected | Segmentation threshold too high | Lower confidence threshold; use explicit category list in GroundingDINO prompt |
| Wrong category | Blazer labeled as shirt | Ambiguous boundary cases | Prompt engineering; fallback to broader category |
| Color hallucination | Black item matched to navy | Color extraction inaccurate | Add color verification step; use CLIP color probe |
| Style register mismatch | Formal blazer → streetwear results | Style signal lost in text query | Include style register in query construction |
| No results returned | Niche traditional garment | Out-of-distribution; not in retail search index | Graceful fallback: broader category search |
| Latency spike | Complex multi-garment scene | Sequential API calls | Identify which step is the bottleneck |
| Price tier misalignment | Luxury item matched to fast fashion | No price signal in query | Add tier qualifier to search query |
| Layered garments | Coat over dress — only outer detected | Segmentation limited to dominant items | Acceptable for MVP; note as known limitation |
| Occlusion | Garment only 20% visible | Insufficient signal | Threshold: <30% visible → skip that garment |
| Pattern / print | Bold floral — color family unclear | Pattern breaks color heuristics | Treat prints as a separate color token ("floral-print") |

---

## 6. Deliverables

SPIKE-001 is complete when all five deliverables are in place:

### 6.1 Test harness code

**Location**: `projects/atelier/spike-001/` in the workspace repository.

Structure:
```
spike-001/
├── README.md               ← how to run the harness end-to-end
├── requirements.txt        ← Python dependencies (pinned versions)
├── config.yaml             ← API keys via env vars; model choices; thresholds
├── pipeline/
│   ├── segment.py          ← Step 1: garment segmentation
│   ├── extract_attributes.py  ← Step 2: attribute extraction
│   ├── search_products.py  ← Step 3: product retrieval
│   └── pipeline.py         ← orchestrates steps 1-3 end-to-end
├── evaluation/
│   ├── run_eval.py         ← processes all 100 photos; writes results.yaml
│   ├── grade_ui.py         ← simple local UI for human grading (optional)
│   └── metrics.py          ← computes all metrics from graded results
├── dataset/
│   ├── photos/             ← 100 test photos (not committed to git if large)
│   ├── dataset_ground_truth.yaml
│   └── dataset_manifest.yaml  ← photo IDs, sources, licenses
└── results/
    ├── results_v1.yaml     ← raw pipeline output per photo
    └── evaluation_v1.yaml  ← graded results + computed metrics
```

Code standards (per shared/code_standards.md): single-responsibility functions, typed parameters, explicit error handling (never silent), constants for all magic strings (API endpoints, model IDs, thresholds), pytest unit tests for the metrics computation functions (100% coverage on that logic since it drives the go/no-go decision).

### 6.2 Results report

**Location**: `projects/atelier/memory/experiments/2026-04-16_spike_results.md` (written at spike completion)

Must contain:
- Summary verdict (pass / partial / fail) with the exact metric
- Full metric table (all metrics from Section 5)
- Per-category breakdown (which garment types performed well, which poorly)
- Cost per scan breakdown (itemized by pipeline step)
- Latency breakdown (per step, p50 + p95)
- Failure mode frequency table
- Recommended production pipeline (or "do not proceed" verdict)

### 6.3 Cost-per-scan estimate with scaling projections

A table showing projected monthly cost at:
- 1,000 scans/day (early beta)
- 10,000 scans/day (growth)
- 100,000 scans/day (scale)

For each volume: itemized API cost, estimated caching reduction, projected cost per scan, total monthly API spend.

### 6.4 Recommended production architecture OR "do not proceed" verdict

If spike passes: an ADR draft (`projects/atelier/adr/ADR-001-ai-matching-pipeline.md`) documenting the validated pipeline choices, with rationale and rejected alternatives.

If spike fails: a structured pivot options document for product-lead, covering: (a) manual tagging fallback, (b) narrowed scope (fewer categories), (c) human-in-the-loop assisted matching, (d) alternative value prop that doesn't require high-accuracy product identification.

---

## 7. Timeline

Sprint window: **2026-04-16 → 2026-04-30** (14 calendar days, target: results ready by 2026-04-28 to allow 2 days for reporting before the 2026-05-01 feasibility gate).

### Phase 1: Setup (days 1-3, 2026-04-16 to 2026-04-18)

| Day | Task | Owner | Output |
|---|---|---|---|
| Day 1 (Apr 16) | Provision API accounts: SerpAPI, Claude API (check if existing), Roboflow for GroundingDINO hosted | Human owner | API keys in env; accounts active |
| Day 1 (Apr 16) | Set up spike-001/ project structure; scaffold pipeline modules | Tech | Directory structure + stub files |
| Day 2 (Apr 17) | Assemble 60 of 100 photos from Unsplash + Pexels | Tech / Human | 60 photos in dataset/photos/ |
| Day 2 (Apr 17) | Write ground truth for first 60 photos | Human owner (fashion-literate review) | dataset_ground_truth.yaml (partial) |
| Day 3 (Apr 18) | Source remaining 40 photos (Wikimedia + consented + synthetic fill) | Tech / Human | 100 photos; full ground truth locked |

**Phase 1 blocks Phase 2**. Ground truth must be locked before any model runs.

### Phase 2: Primary pipeline implementation + evaluation (days 4-8, 2026-04-19 to 2026-04-23)

| Day | Task | Parallelizable? | Output |
|---|---|---|---|
| Day 4 (Apr 19) | Implement segment.py (GroundingDINO API) | No — foundation | Garment bounding boxes for test photos |
| Day 4 (Apr 19) | Implement extract_attributes.py (Claude Vision) | Yes — parallel with testing segment.py | Structured attribute JSON per garment |
| Day 5 (Apr 20) | Implement search_products.py (SerpAPI) | Yes — parallel with attribute extraction | Product results per garment |
| Day 5 (Apr 20) | Implement pipeline.py orchestrator; wire steps 1-3 end-to-end | No — requires steps 1-3 done | End-to-end run on 5 test photos |
| Day 6 (Apr 21) | Run full 100-photo batch; capture results_v1.yaml; measure latency + cost | No | results_v1.yaml; latency + cost spreadsheet |
| Day 7 (Apr 22) | Human grading of 100 results (primary grader) | Human owner | evaluation_v1.yaml (partially filled) |
| Day 7 (Apr 22) | Inter-rater grading of 20-photo sample (second grader) | Human owner (second reviewer) | Cohen's kappa validation |
| Day 8 (Apr 23) | Run metrics.py; compute all metric values; check kappa | No | Primary pipeline verdict |

**By end of day 8 (Apr 23)**: we know whether the primary pipeline passes, fails, or is in partial range.

### Phase 3a: If primary passes (days 9-10, 2026-04-24 to 2026-04-25)

| Task | Output |
|---|---|
| Document failure modes; identify categories that underperformed | Failure mode catalog |
| Write draft ADR-001 | Architecture recommendation |
| Draft results report | results report + cost projections |
| Buffer / polish | Ready for feasibility gate review |

### Phase 3b: If primary is in partial range (days 9-12, 2026-04-24 to 2026-04-27)

| Task | Output |
|---|---|
| Implement alternative pipeline (SAM 2 + OpenFashionCLIP + Qdrant) | Alternative pipeline code |
| Index a small product catalog (Shopstyle feed sample, ~50k products) | Qdrant index |
| Run alternative pipeline on same 100 photos | results_v2.yaml |
| Human grading of delta (only results different from primary) | evaluation_v2.yaml |
| Compare primary vs alternative; pick best | Decision: which pipeline to recommend |
| Draft results report + scope-change proposal for product-lead | Spike deliverables |

### Phase 3c: If primary fails (days 9-10, 2026-04-24 to 2026-04-25)

| Task | Output |
|---|---|
| Diagnose root cause (segmentation failure? attribute failure? retrieval failure?) | Failure analysis |
| Document pivot options for product-lead | Pivot options document |
| No further pipeline implementation | Halt and escalate |

### Final reporting (days 13-14, 2026-04-28 to 2026-04-29)

| Task | Output |
|---|---|
| Finalize results report | experiments/2026-04-16_spike_results.md |
| Write cost projections table | Included in results report |
| Write ADR-001 draft (if pass) or pivot doc (if fail) | adr/ or memory/experiments/ |
| Append session summary to sessions.md | Updated sessions.md |
| Brief product-lead on outcome | Verbal / written handoff |

**Hard deadline**: results report delivered by 2026-04-29 EOD. Feasibility gate review: 2026-05-01.

---

## 8. Cost Estimate (Spike Only)

The spike itself can spend more than the $0.02 production target — we are evaluating the ceiling, not optimizing yet.

| Item | Quantity | Unit cost | Total |
|---|---|---|---|
| **SerpAPI** (Google Shopping queries) | ~300 queries (100 photos × avg 3 garments × 1 query/garment) | $0.001 | ~$0.30 |
| **Claude Vision** (attribute extraction) | ~300 garment crops × avg 0.5 MP image | ~$0.004/garment | ~$1.20 |
| **GroundingDINO hosted** (Roboflow Inference API) | 100 images | ~$0.002/image (estimated; verify current pricing) | ~$0.20 |
| **Amazon PA-API** | 100 queries (if account in place) | Free (affiliate) | $0.00 |
| **Qdrant** (if Phase 3b triggered) | Self-hosted on free tier OR cloud trial | $0 | $0.00 |
| **GPU compute** (if SAM 2 triggered in Phase 3b) | ~4 hours A100 on Lambda Labs or RunPod | ~$1.10/hr | ~$4.40 |
| **Dataset storage** (S3 or local) | 100 photos avg 3 MB = 300 MB | Negligible | <$0.01 |
| **Dataset labeling / grading time** | 100 photos × 5 min/photo grading | Human time, not $$ | — |
| **Shopstyle feed indexing** (if Phase 3b) | One-time batch | CPU only | $0.00 |

**Primary pipeline total (no GPU)**: approximately $1.70

**If Phase 3b triggered** (alternative pipeline with SAM 2): approximately $6.10 additional → **total ~$7.80**

**Budget ask**: $20 in API credits covers the spike with 2.5× headroom for iteration and re-runs. If the human owner already has Claude API credits and SerpAPI credits, the incremental cost is under $5.

**Cheaper fallback if budget is constrained**: replace Claude Vision with OpenFashionCLIP embeddings (free, self-hosted on CPU — slower but eliminates vision API cost). This reduces attribute extraction accuracy but cuts cost to near-zero for the spike. Flag this trade-off clearly in results.

---

## 9. Risks and Unknowns

These risks could invalidate the spike itself, independent of the product.

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| **Dataset too small / not diverse enough** | Medium | Results may not generalize; kappa check may catch this | Strict composition plan (Section 4); extend to 150 if results cluster near threshold |
| **Grading subjectivity** — "useful" is ambiguous | High | Inflated or deflated metrics; inter-rater conflict | Run kappa check; calibration session if kappa <0.7; rubric is intentionally concrete |
| **SerpAPI ToS blocks commercial use** | Low-Medium | Cannot use this source in production | Read terms before spending money; have Shopstyle/Amazon as fallbacks |
| **Claude Vision API rate limits** | Low | Spike slows; batch processing delayed | Run photos in batches of 10 with backoff; use async calls; extend timeline by 1 day |
| **GroundingDINO hosted service changes pricing / availability** | Low | Segmentation step blocked | Self-host GroundingDINO on CPU (slower but works); or use HuggingFace Inference API |
| **Model-choice rabbit hole** | High | Team spends too long evaluating models instead of evaluating results | HARD RULE: evaluate primary pipeline fully before touching alternatives. No model switching before Day 8. |
| **Ground truth anchor bias** — grader sees model output while labeling | Medium | Inflated useful-match ratings | Lock ground truth BEFORE running any model. This is non-negotiable. |
| **Niche garments have zero retail search results** | Medium | 15 "hard" photos return nothing; metric looks worse than production would | Log "no results" separately from "wrong results"; both are failure modes but have different mitigations |
| **SAM 2 GPU access delayed** (if Phase 3b needed) | Medium | Alternative pipeline cannot be evaluated in time | Pre-provision GPU access in Phase 1 even if not immediately needed |
| **Amazon PA-API affiliate account not active** | Medium | One less product source | Tech does not block on this — SerpAPI is the primary source for the spike |

---

## 10. Exit Criteria

### Pass (top-3 useful match rate ≥75%)

- Commit to US-010 as specced in backlog.yaml
- Proceed with the validated pipeline as the production architecture baseline
- File ADR-001 documenting the pipeline decision
- SPIKE-001 removed from discovery; US-010 moves to sprint planning
- Product-lead to confirm SPIKE-002 (legal review) as the remaining gate before US-010 development begins

### Partial (60–74%)

- Do NOT commit to US-010 as specced
- Product-lead reviews the following proposed scope changes (choose one or combine):
  - Narrow to the 3-4 best-performing garment categories only (e.g., tops + bottoms; defer footwear + accessories)
  - Add a human-in-the-loop assisted matching step (user selects the category + color before retrieval — lowers AI burden, increases accuracy)
  - Reduce the match threshold in US-010's acceptance criteria (e.g., "65% top-3 match rate" instead of 75%) — requires product-lead sign-off
- Run extended spike (15 more photos in the hard-case categories; try alternative pipeline if not yet tested)
- Timeline impact: 1-week delay before US-010 commitment

### Fail (<60%)

- Halt US-010 work entirely
- Product-lead receives a structured pivot options document covering:
  1. **Manual tagging fallback**: users tag their own garments; AI only assists categorization (no product search)
  2. **Narrowed scope + human curation**: AI identifies category only; human curators maintain a product lookup table per category (works at small scale, does not scale)
  3. **Different retrieval modality**: visual search APIs (Bing Visual Search, Pinterest Lens API) instead of text query — requires re-spiking
  4. **Pivot value prop**: drop product identification from MVP; focus purely on wardrobe + looks; add product identification as a v2 only after ML state-of-art improves or budget allows fine-tuning
- Product-lead makes the pivot call; product-tech provides technical input but does not decide
- All other MVP stories (wardrobe core, looks) are unaffected and can proceed in parallel

---

*Plan version: 1.0. Author: product-tech. Last updated: 2026-04-16.*
