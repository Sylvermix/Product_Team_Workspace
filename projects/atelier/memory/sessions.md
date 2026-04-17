# Sessions — Atelier

End-of-session summaries. Latest at top. Next session reads this to pick up cleanly.

---

## 2026-04-17 — human owner + orchestrator — Validation session: pending decisions + product model expansion

**Task**: Work through all pending validation points from the previous session (13 decisions across SPIKE-001, design blockers, DISC-001), and extend the product model with new AI-native features identified during the conversation.

**Worked on**:

**A. SPIKE-001 — all 5 blockers resolved**
- Claude API account created ($50 loaded) + SerpAPI account created (free tier sufficient for spike)
- Evaluators confirmed: product owner + Linh
- GPU: wait and provision on-demand only if primary pipeline fails
- Amazon PA-API: skipped — Google Shopping via SerpAPI covers multi-retailer (brands, ASOS, Vinted, Vestiaire, Depop, etc.)
- $20 API budget: already covered by the $50 Claude credit

**B. Design blockers — all 5 resolved**
- `neutral.400` → darken globally to `#7a7570` (WCAG AA fix)
- Scan API → streaming (progressive reveal) from MVP — not batch
- Daily scan limit → 10 scans/day at MVP (~$0.20/user/day max)
- Affiliate links → accessible without account (anonymous OK)
- Guest mode → permanent but limited (browse + affiliate only; account required to save)

**C. DISC-001 — deferred**
- User research interviews postponed; product owner will trigger when ready

**D. Product model — major expansion**

Four new decisions locked by product owner:
1. **User access model** — anonymous: browse + affiliate links; logged-in: scan, wardrobe, looks, wishlist, likes
2. **Two scan intents** — "I own this" → wardrobe (size mandatory); "I want this" → wishlist
3. **Light social in MVP** — public profiles + follow + wishlist via likes (full social feed deferred V2)
4. **AI Agent (prompt bar)** — persistent throughout app; conversational product search + style profile building; no forms

Five new epics added:
- **US-040** — AI agent prompt bar (conversational, wardrobe-aware, pushes to wishlist)
- **US-050/051/052** — Enriched product detail: multi-retailer price comparison (real-time), synthetic review summary (AI-aggregated), size social proof from matched users
- **US-060** — Mandatory size capture on wardrobe scan (implicit size profile by brand + category)
- **US-070** — Follow recommendations by style match + size match
- **US-200** — Creator commission sharing (V2; architecture defined now)

**E. Workspace infrastructure**
- Tier 2 agent memory: replaced `scope:user` approach with versioned files in `shared/agent-memory/` (product-lead.md, product-design.md, product-tech.md) — now Git-tracked and cross-project

**Outcome**:
- SPIKE-001 is fully unblocked and can start immediately
- Product model is significantly richer: AI-native from the ground up, social commerce architecture defined, creator economy roadmapped
- backlog.yaml updated with 7 new user stories across 4 new epics
- context.md updated with user access model table, new priorities section (7 epics), size profile strategy
- All decisions logged in memory/decisions.md (7 new entries)
- Workspace memory infrastructure upgraded

**Decisions made**: 7 new entries in `memory/decisions.md` (see file for full reasoning)
1. User access model + MVP social scope
2. Streaming scan API from MVP
3. Daily scan limit: 10/day
4. neutral.400: darken globally to #7a7570
5. Amazon PA-API: skipped
6. GPU: wait, don't pre-provision
7. AI Agent, size profile, product detail, creator economy (combined architectural decision)

**Open questions / next steps**:
- SPIKE-001 execution: start now. Product owner + Linh evaluate results independently on 100 photos
- SPIKE-002 (legal/affiliate API review): not yet started — assign owner and begin
- Onboarding specs need review: agent-based profile building replaces form-based onboarding; specs may need updating
- Design: wardrobe grid (US-003) not yet designed; AI agent UX (US-040) not yet designed
- Creator monetization (US-200): attribution tracking architecture needs to be scoped before MVP ships (even if reward UX is V2)
- DISC-001: to be triggered by product owner when ready

**Files changed**:
- Modified: `projects/atelier/backlog.yaml` (7 new stories: US-030–032, US-040, US-050–052, US-060, US-070, US-200; US-103 updated)
- Modified: `projects/atelier/context.md` (user access model section, priorities rewritten, size profile strategy)
- Modified: `projects/atelier/memory/decisions.md` (7 new entries)
- Modified: `projects/atelier/memory/sessions.md` (this entry)
- Modified: `.claude/agents/product-lead.md`, `product-design.md`, `product-tech.md` (memory section updated)
- Created: `shared/agent-memory/product-lead.md`, `product-design.md`, `product-tech.md`

---



## 2026-04-16 — orchestrator — Parallel de-risking: SPIKE-001 plan + scan moment + onboarding + DISC-001 research

**Task**: with the project initialized earlier the same day (product-lead foundational session), advance all three sprint-1 de-risking workstreams in a single pass — technical feasibility plan, the two highest-impact design surfaces (scan moment + onboarding), and the user research scaffolding for DISC-001. Goal was to reach the 2026-05-01 feasibility gate with every stream ready to execute, bounded only by human-owner decisions.

**Worked on** (all via subagent delegation; see individual sessions below for depth):
- `product-tech` — produced `memory/experiments/2026-04-16_spike_ai-matching-plan.md` (10-section plan, 2026-04-16 → 2026-04-29 schedule)
- `product-design` (pass 1) — produced `specs/scan-moment/{aesthetic-direction,mockup-spec,motion-spec}.md` (13 states + motion choreography)
- `product-design` (pass 2) — produced `specs/onboarding/{journey-map,mockup-spec,aesthetic-direction}.md` (12 beats, 13 screens, hand-off into scan moment)
- `product-lead` — produced `memory/research/2026-04-16_disc-001_{interview-guide,recruitment,analysis-template}.md` (60-min protocol, n=5 with diversity allocation, falsification-first construction)

**Outcome**:
- Sprint 1 (2026-04-16 → 2026-04-30) is now execution-ready on all three planned items (SPIKE-001, SPIKE-002, DISC-001). Only SPIKE-002 (legal review) has not been touched this session.
- Scan moment and onboarding specs are mutually consistent — "studio reverence" (scan) and "studio invitation" (onboarding) are sub-tones of the same frame; onboarding hand-off into scan is explicit in the journey map.
- 16 product-design decisions logged in `memory/decisions.md` across the two design passes (metaphors, marker form, first value definition, account gating, first-offering pattern, sort default, stillness during scan, etc.).
- Accessibility system-level issue surfaced: `neutral.400 (#a09b90)` fails WCAG AA at xs on light surfaces. Appears in both scan-moment and onboarding specs (4 instances in onboarding, multiple in scan). Now a token-audit item, not a per-spec patch.

**Decisions made**: none by the orchestrator directly. All substantive decisions were made and logged by the respective subagents in `memory/decisions.md`. No new entries needed from this meta-session.

**Open questions / next steps**: there are now **13 decisions pending with the human owner**, spanning three streams. The next session should start with product-lead compiling a single consolidated decision brief rather than opening a new workstream.

Grouped by stream:

**A. SPIKE-001 execution blockers (5, needed ~2026-04-17)**
1. SerpAPI + Claude API accounts — active or need provisioning?
2. Second fashion-literate reviewer available for inter-rater reliability?
3. Pre-provision GPU for fallback pipeline, or wait?
4. Amazon PA-API affiliate account active?
5. $20 API credit budget approved?

**B. Scan + onboarding design → tech handoff blockers (5, before US-010 build)**
1. Streaming scan API at MVP, or batch acceptable with fallback?
2. Daily scan rate limit at MVP — value?
3. `neutral.400` token fix — darken globally (recommended) or per-use-case?
4. Anonymous affiliate deep-link click allowed, or gated on account?
5. Guest mode semantics — permanent, or onboarding-only deferral?

**C. DISC-001 recruitment blockers (5, needed by 2026-04-18 to hold 2026-04-28 interview week)**
1. Participant incentive + platform budget (~$500–700) approved?
2. Moderator assignment (internal vs freelance vs Respondent-supplied)?
3. Transcription tool (Otter.ai vs Rev)?
4. GDPR-compliant consent form — template exists or draft needed?
5. Interview week (2026-04-28) confirmed clear for moderator?

**Additional non-blocking next steps**:
- SPIKE-002 (legal/affiliate API review) still untouched — should be picked up by product-lead in parallel with decision-brief preparation.
- Design system: token audit pass for `neutral.400` + addition of new timing/motion tokens identified across the two design passes.
- Wardrobe grid (US-003) is the next high-visibility design surface not yet touched.

**Files changed**:
- Created: `memory/experiments/2026-04-16_spike_ai-matching-plan.md`
- Created: `specs/scan-moment/aesthetic-direction.md`, `mockup-spec.md`, `motion-spec.md`
- Created: `specs/onboarding/journey-map.md`, `mockup-spec.md`, `aesthetic-direction.md`
- Created: `memory/research/2026-04-16_disc-001_interview-guide.md`, `recruitment.md`, `analysis-template.md`
- Modified: `memory/sessions.md` (four subagent entries + this orchestrator entry)
- Modified: `memory/decisions.md` (16 decisions appended across design passes)

---

## 2026-04-16 — product-lead — DISC-001 research package (interview guide, recruitment, analysis template)

**Task**: Design the full research scaffolding for DISC-001: Onboarding Effort Validation. Three deliverables: interview guide, recruitment brief, analysis template. No interviews conducted; no synthetic findings produced.

**Worked on**:
- Read context.md (sections 2, 3, 7, 9), all memory files (sessions.md, decisions.md, learnings.md), backlog.yaml (DISC-001 entry), specs/onboarding/journey-map.md, specs/onboarding/mockup-spec.md (Screen 0 and 1).
- Created `projects/atelier/memory/research/2026-04-16_disc-001_interview-guide.md`
- Created `projects/atelier/memory/research/2026-04-16_disc-001_recruitment.md`
- Created `projects/atelier/memory/research/2026-04-16_disc-001_analysis-template.md`

**Outcome**:
- Full 60-minute interview protocol with 12 questions + probes across 5 sections. Includes 4 verbatim concept stimulus scripts (Stimuli A–D) covering the offering screen, scan ceremony, photo-roll import, and deferred account creation. Guide is handed-off ready for any competent moderator.
- Falsification criteria defined for the primary hypothesis and all 6 secondary hypotheses. The guide can produce disconfirming evidence — it is not structured to confirm.
- Recruitment brief with diversity allocation (3W/1M/1open gender; body diversity; skin tone; income mix; one "messy wardrobe" participant; one competitor-app abandoner). Respondent.io recommended as primary channel with selection-bias mitigations specified.
- Full 12-question screener with exact wording and disqualification logic.
- Analysis template with per-participant note template (P01–P05), cross-participant synthesis grid, decision recommendation branching (supported / partially supported / unsupported), and 6 mandatory bias checks.
- Timeline defined: 2026-04-18 recruitment open, 2026-04-28 interview week, 2026-05-14 final report.

**Key research decisions made**:
1. **n=5 defense**: appropriate for hypothesis scoping at this stage; second round of 3 triggered only if results split 2/3. Full rationale in recruitment brief.
2. **Channel choice**: Respondent.io primary (speed + screener tooling); personal network and fashion subreddits explicitly excluded due to selection bias. Prolific.co as supplement for harder-to-recruit profiles (plus size, non-tech-forward).
3. **Stimulus format**: concept descriptions read verbatim by moderator rather than shown on screen. Reason: no functional prototype exists; showing mockup-spec layouts would test visual design instead of behavioral hypotheses. The guide tests the concept logic, not the design execution.
4. **Compensation**: 60 GBP / 70 EUR / $75 USD per participant. Defends the sweet spot between serious-participant quality and professional-research-participant inflation.
5. **Competitor-app abandoner as intentional inclusion**: one participant who tried and left a wardrobe app is a mandatory target in the diversity allocation. Their abandonment story is the richest available evidence for effort failure modes.
6. **Bias check section mandatory**: 6 named bias checks (articulate-participant over-weighting, confirmation bias toward existing design, concept enthusiasm vs behavior evidence, false consensus, moderator performance, secondary hypothesis rigor) are required before the recommendation is signed off.

**Open questions for human owner — must resolve before recruitment can start**:
1. **Budget approval**: approximately $500–700 in participant incentives (5 × ~$75 USD equivalent) plus Respondent.io platform fee. Confirm budget line and payment mechanism.
2. **Moderator assignment**: who conducts the 5 sessions? Options: a designated team member, a freelance UX researcher (Respondent can sometimes supply moderators), or the product owner. The moderator must be trained in behavioral interviewing; the guide is written for a competent moderator, not a first-time interviewer. Confirm assignment by 2026-04-18.
3. **Transcription preference**: Otter.ai (fast, AI, ~$0 beyond subscription) vs Rev (human, higher accuracy, ~$90/session). Confirm before interview week.
4. **Recording consent mechanism**: confirm the consent form template and whether a standard company consent form exists, or one needs to be drafted. GDPR-compliant consent is required per context.md constraints.
5. **Interview week scheduling**: the timeline proposes 2026-04-28 to 2026-05-02. Confirm this window is clear for the moderator before recruitment window opens.

**Files changed**:
- Created: `projects/atelier/memory/research/2026-04-16_disc-001_interview-guide.md`
- Created: `projects/atelier/memory/research/2026-04-16_disc-001_recruitment.md`
- Created: `projects/atelier/memory/research/2026-04-16_disc-001_analysis-template.md`
- Modified: `projects/atelier/memory/sessions.md` (this entry)

---

## 2026-04-16 — product-design — Onboarding flow design (first launch to first value)

**Task**: Design the full onboarding flow from cold launch to first value. Three
deliverables: journey-map.md, mockup-spec.md, aesthetic-direction.md. Two hard
constraints: no onboarding tour; scan reachable without wardrobe setup.

**Worked on**:
- Read context.md (sections 3, 4, 6, 9), sessions.md, decisions.md, backlog.yaml
  (US-001, US-002, US-003, US-010), design_system/tokens.yaml,
  design_system/components.yaml, specs/scan-moment/ (all three files),
  shared/accessibility_checklist.md.
- Created `projects/atelier/specs/onboarding/journey-map.md`
- Created `projects/atelier/specs/onboarding/mockup-spec.md`
- Created `projects/atelier/specs/onboarding/aesthetic-direction.md`
- Appended to `memory/decisions.md`

**Outcome**:
- Complete onboarding journey (12 beats, branching diagram, resumption/error states).
- 13 screens/states spec'd with full accessibility audit table.
- Aesthetic direction locked: sub-tone is "studio invitation" within the global
  editorial maximalism × studio minimalism frame. Continuous with scan's "studio
  reverence" — same surface, same pace, same typeface from wordmark to garment label.
- 8 new components identified for design_system/components.yaml: AgeGateInput,
  OfferingScreen, ImportGrid, ImportProgressScreen, ImportCompleteBeat,
  AccountGateSheet, EmptyStateGrid, FirstBreathScreen.
- Token gaps identified: beat_hold (2000ms), first_breath (1500ms), acknowledgment
  (3000ms) timing tokens + onboarding semantic flags.
- WCAG AA verified on all text combinations. 4 blocker instances found (same root
  cause as scan-moment spec: neutral.400 on light surfaces failing 4.5:1). All
  have actionable fixes (use neutral.600 or increase to 14px bold).

**Key onboarding design decisions made** (see `memory/decisions.md`):
1. First value = "first recognition moment" (first garment detected + one product
   match seen), not "first wardrobe item added."
2. Account creation deferred to first save/wishlist action — not a blocking gate
   in onboarding. Scan results visible anonymously.
3. First-offering surface: a full-width dark primary surface with display serif
   copy ("Scan a photo now"), not two equal buttons. Secondary path is a quiet
   text link below.
4. Age gate is first screen (before offering) — early, respectful, non-punitive.
5. Photo-roll import: offered via a dedicated screen with "Skip for now" always
   present; 10-photo max; numbered selection badges; AI tags run in background.
6. "Your first find." — quiet right-aligned xs note, 4s visible, no confetti.
   First value acknowledged in editorial register, not celebrated.

**Accessibility note (inherited blocker from scan-moment spec)**:
`color.neutral.400 (#a09b90)` on `color.surface.background (#f6f3ed)` or
`color.surface.card (#fbfaf7)` = approximately 2.9:1 — fails WCAG AA for small text.
This blocker appears in 4 places in the onboarding spec:
- "Skip for now" text (Screen 6)
- Legal footnote body (Screen 7)
- Legal footnote links (Screen 7, at xs)
- "Forgot password" link (Screen 8)
Fix for all: substitute neutral.600 (#5a5651, 7.4:1) for secondary/tertiary text
not meeting large-text threshold. Links that must use terracotta accent: increase
to 14px + bold (weight 500) to meet 3:1 large-text threshold.
This is now a systemic design system issue. Recommend product-lead request a token
audit pass before tech handoff on both scan and onboarding specs.

**Open questions for product-lead**:
1. **Deep-link without account**: Should tapping a product card in scan results
   (opening a retailer URL) require an account, or can anonymous users deep-link
   through? Only "Save to wishlist" clearly requires persistence — retailer
   deep-links may not. A business decision: anonymous affiliate clicks are revenue;
   gating them on account creation may suppress conversion. Recommend allowing
   anonymous tap-through.
2. **Guest mode**: is "Maybe later" on account creation a permanent guest mode or
   a temporary onboarding deferral? The current spec treats scan results as session-
   only without an account. If guest mode is permanent, the UX implications are
   larger (what persists between sessions for a guest?).
3. **neutral.400 token**: should neutral.400 be darkened globally (to ~#7a7570,
   which would clear AA at xs) or should each use-case be handled individually?
   A global darkening is cleaner but changes the scan-moment spec too. Design
   recommends the global fix. Product-lead and Tech to be aware.
4. **Photo heuristics for import**: the multi-select grid claims to pre-filter for
   "likely clothing photos." What is the on-device heuristic? On iOS 16+, smart
   albums (PHAssetCollection) may surface clothing/fashion categories. On Android,
   similar. Tech to advise feasibility and fallback (if no heuristic available,
   the grid just shows all recent photos; the spec remains valid).
5. **Social auth (Apple/Google) in onboarding**: Screen 7 proposes Apple and Google
   sign-in options. App Store policies may require specific handling for apps with
   affiliate links or in-app purchase. Tech + legal to validate before implementing.

**Files changed**:
- Created: `projects/atelier/specs/onboarding/journey-map.md`
- Created: `projects/atelier/specs/onboarding/mockup-spec.md`
- Created: `projects/atelier/specs/onboarding/aesthetic-direction.md`
- Modified: `projects/atelier/memory/sessions.md` (this entry)
- Modified: `projects/atelier/memory/decisions.md`

---

## 2026-04-16 — product-design — Scan moment design (US-010)

**Task**: Design the ceremonial "scan" interaction — the app's signature moment where
a user photographs or uploads an image and the AI identifies garments, then reveals
matching products. Three deliverables: aesthetic direction, mockup spec, motion spec.

**Worked on**:
- Read context.md (section 4 aesthetic direction, section 6 priorities), backlog.yaml
  (US-010 acceptance criteria), all memory files, design_system/tokens.yaml,
  shared/accessibility_checklist.md.
- Created `projects/atelier/specs/scan-moment/aesthetic-direction.md`
- Created `projects/atelier/specs/scan-moment/mockup-spec.md`
- Created `projects/atelier/specs/scan-moment/motion-spec.md`
- Appended to `memory/decisions.md`

**Outcome**:
- Complete design spec for all 13 states of the scan flow (entry through error).
- Aesthetic direction locked: emotional register is "studio reverence" (sub-tone of
  editorial maximalism × studio minimalism). Visual metaphors: darkroom contact sheet
  + atelier pinboard.
- Signature marker form defined: numbered underline (1px terracotta line + number
  in PP Neue Montreal xs, margin-note style). Not a pin, reticle, or bounding box.
- Full motion choreography specified with named easing curves, stagger timings, and
  the 6s latency budget handled via minimum-ceremony hold (1200ms floor on fast path).
- 8 new components identified for design_system/components.yaml: ScanButton,
  ScanChooserSheet, GarmentMarker, GarmentSelector, ProductCard, AffiliateDisclosure,
  ScanConfirmButton, GrainOverlay.
- Token gaps identified: ceremonial + collapse easing curves, grain opacity, photo
  split proportions, scan duration constants — proposed additions listed in specs.
- WCAG AA verified on all text combinations in spec (verified ratios: ink on card
  16.7:1, white on ink 16.7:1, neutral.400 on card 2.9:1 — see note below).

**Key design decisions made** (see `memory/decisions.md`):
1. Scan moment emotional register: "studio reverence"
2. Visual metaphor: darkroom contact sheet + atelier pinboard
3. Marker form: numbered underline (not pin, reticle, or bounding box)
4. No progress spinner during scan — stillness signals confidence
5. Pre-scan confirm beat retained (intentionality over friction reduction)
6. Low-confidence partial match is a distinct state from no-match
7. Product sort default: best match first, not price-ascending
8. Affiliate disclosure: single persistent footer per session, not per-card

**Accessibility note**: `color.neutral.400 (#a09b90)` on `color.surface.card (#fbfaf7)`
computes to approximately 2.7:1. This fails 4.5:1 for small text. It is used for
sub-labels (retailer name, affiliate disclosure) at `font-size: xs (12px)`. This is a
known gap — these elements must either increase to 14px+ bold (3:1 threshold for large
text) or the neutral.400 value must darken to ≥#7a7570 for AA compliance on xs text.
This is flagged as a blocker before handoff to tech. Product-lead: no action needed.
Design: iterate on one of the two solutions before marking spec as tech-ready.

**Open questions for product-lead**:
1. **Streaming API requirement**: the motion spec requires the scan backend to support
   progressive/streaming detection responses (SSE or WebSocket) for markers to appear
   one-by-one. If the API only returns a batch at the end, the choreography degrades
   (all markers appear simultaneously). This is a product decision with tech impact.
   Should streaming be required for MVP or is batch acceptable with a fallback?
2. **Confidence threshold for low-confidence state**: the spec proposes 0.65 as the
   threshold below which we show "Approximate match." The actual useful threshold
   depends on SPIKE-001 results. Flag for tech + lead after spike completes.
3. **Rate limiting (State 11c)**: the spec describes a rate-limit state but no
   quota is defined. Product-lead to decide whether MVP has a scan limit per day, and
   if so what the value is.
4. **"Scan" as app name / feature name**: context.md uses "Scan" as the feature name.
   Content agent (when invoked) should review all copy in the spec for brand voice
   consistency. "Scan" may become a more branded term (e.g. "Identify", "Look up",
   "Find").

**Handoff notes for tech**:
- Specs are written-only; no Figma file exists yet. Tech should treat spec as
  implementation reference. Coordinate with design if any layout ambiguity arises.
- GrainOverlay: must use a pre-rendered 256×256 seamless PNG tiled at multiply blend
  mode. CSS `filter: noise()` is not consistent across platforms. Asset needs to be
  created.
- Luminance lift (radial brightness on garment region): implemented as a composited
  white radial gradient at 6% opacity over the photo, not as a CSS filter on the image.
  Coordinates come from AI bounding box.
- `prefers-reduced-motion` must be checked at the animation orchestration level, not
  per-element. One flag, all animations respect it.
- The 1200ms minimum ceremony hold (fast path floor): this is a deliberate UX decision,
  not a bug. Do not optimize it away.

**Files changed**:
- Created: `projects/atelier/specs/scan-moment/aesthetic-direction.md`
- Created: `projects/atelier/specs/scan-moment/mockup-spec.md`
- Created: `projects/atelier/specs/scan-moment/motion-spec.md`
- Modified: `projects/atelier/memory/sessions.md` (this entry)
- Modified: `projects/atelier/memory/decisions.md`

---

## 2026-04-16 — product-tech — SPIKE-001 planning

**Task**: produce a detailed, actionable plan for SPIKE-001 (AI product identification feasibility spike) — the gate that blocks US-010, the core differentiator.

**Worked on**:
- Read full project context: context.md, backlog.yaml, roadmap.yaml, decisions.md, sessions.md, shared/code_standards.md
- Wrote spike plan: `projects/atelier/memory/experiments/2026-04-16_spike_ai-matching-plan.md`

**Outcome**:
- Complete 10-section spike plan covering: hypothesis + "useful match" definition, pipeline under test, model/service evaluation, test dataset composition (100 photos with diversity breakdown), evaluation methodology (metrics, grading protocol, Cohen's kappa check), deliverables, day-by-day timeline (2026-04-16 to 2026-04-29), cost estimate (~$2-$8 depending on path), risks, and exit criteria.

**Decisions embedded in the plan**:
- "Useful match" defined as substitutability across 4 criteria (category + color family + style register + price tier) — not exact-item matching
- Primary pipeline: GroundingDINO (segmentation) + Claude Vision (attribute extraction) + SerpAPI Google Shopping (retrieval) — chosen for lowest setup cost and best ceiling measurement
- Alternative pipeline (Phase 3b): SAM 2 + OpenFashionCLIP + Qdrant — evaluated only if primary lands in 60-74% partial range
- Ground truth must be locked BEFORE any model runs (anti-anchor-bias rule)
- Model-switching is banned before Day 8 (anti-rabbit-hole rule)

**Open questions requiring human decision before work starts**:
1. Does the human owner have active SerpAPI and Claude API accounts, or do new accounts need to be provisioned? (Day 1 blocker)
2. Is there a second fashion-literate reviewer available for the 20-photo inter-rater reliability check? (Required for grading validity)
3. Should GPU access (for SAM 2 Phase 3b) be pre-provisioned in Phase 1 as insurance, or wait to see if Phase 3b is needed? (Risk vs cost trade-off)
4. Is the Amazon PA-API affiliate account active? (Determines whether Amazon is a product source in the spike)
5. Confirm budget: $20 in API credits covers the full spike with headroom — is this approved?

**Files changed**:
- Created: `projects/atelier/memory/experiments/2026-04-16_spike_ai-matching-plan.md`
- Modified: `projects/atelier/memory/sessions.md` (this entry)

---

## 2026-04-16 — product-lead — Project initialization

**Task**: turn vague requirement ("AI-native wardrobe app with scan and social features") into a structured, scoped, prioritized project.

**Worked on**:
- `context.md` — full project definition (vision, audience, aesthetic, stack, constraints, risks)
- `backlog.yaml` — 10 MVP stories across 3 epics + 3 discovery spikes
- `roadmap.yaml` — sprint plan with 6 milestones through public launch
- `design_system/tokens.yaml` — initial design tokens derived from aesthetic direction
- `memory/decisions.md` — logged 5 foundational decisions
- `memory/learnings.md` — captured 6 open hypotheses to validate

**Outcome**:
- Project scoped from "everything" to wardrobe + scan + looks at MVP
- Social features, video posting, body measurements explicitly deferred to v2 (icebox)
- 3 de-risking spikes identified as gates before committing full MVP effort
- Aesthetic direction committed ("editorial maximalism × studio minimalism")
- Stack proposed (React Native + Expo, Python FastAPI, CLIP + SAM 2) pending feasibility

**Decisions made** (see `memory/decisions.md`):
- Working name: Atelier
- North star: Weekly Active Stylists
- Aesthetic direction: editorial maximalism × studio minimalism
- Proposed stack
- MVP scope (3 epics, 4 deferred)

**Open questions / next steps**:
1. **SPIKE-001** (highest priority): product-tech to validate AI product identification accuracy. Cannot commit to US-010 without this.
2. **SPIKE-002**: product-lead to run legal review of retailer APIs + affiliate networks.
3. **DISC-001**: product-lead to run 5 user interviews to validate onboarding investment hypothesis.
4. Human owner to confirm working name "Atelier" and run trademark search.
5. Design agent not yet invoked — first design work should be the "scan" moment and onboarding flow (the two highest-impact visual moments).

**Files changed**:
- Created: `context.md`, `backlog.yaml`, `roadmap.yaml`, `README.md`, `memory/decisions.md`, `memory/learnings.md`, `memory/sessions.md`
- Modified: `design_system/tokens.yaml` (from template to atelier-specific)

---

<!-- Template for future sessions:

## YYYY-MM-DD — [agent-name] — [Session title]

**Task**:
**Worked on**:
**Outcome**:
**Decisions made**:
**Open questions / next steps**:
**Files changed**:

-->
