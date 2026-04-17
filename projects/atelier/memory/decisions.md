# Decisions — Atelier

Append-only log of significant decisions. Latest at top. Every entry includes context, options, reasoning, and revisit condition.

---

## 2026-04-17 — User access model & MVP social scope

**Who decided**: product owner (human)
**Context**: validation session reviewing pending decisions. The question of affiliate link access (anonymous vs logged-in) led to a broader clarification of the full access model.
**Decision**:
- Anonymous users: can browse public profiles and tap affiliate links (generates commission)
- Logged-in users: can scan, build wardrobe, create looks, like products → wishlist
- Account creation is deferred to first save action (consistent with prior design decision)
- Two scan intents: "I own this" → wardrobe / "I want this" → wishlist
- Light social (public profiles + wishlist via likes) moved from V2 into MVP
**Options considered**:
- Account required for affiliate links (rejected — unnecessary friction, kills anonymous commission)
- No social until V2 (rejected — public profiles are the mechanism that enables anonymous affiliate traffic)
**Consequences**: US-030, US-031, US-032 added to backlog. Full social feed (following, comments) remains V2.
**Revisit if**: App Store review flags public profiles; or legal review of anonymous affiliate tracking raises GDPR concerns.

---

## 2026-04-17 — Scan API: streaming (progressive reveal) from MVP

**Who decided**: product owner (human)
**Context**: choice between streaming (results arrive progressively) and batch (all results at once) for the scan API.
**Decision**: streaming from MVP — the progressive reveal is the core "scan moment" differentiator and must ship day one.
**Options considered**:
- Batch with animation (rejected — 6s static screen reads as broken; undermines "ceremonial reveal")
**Consequences**: backend must implement streaming endpoint (not batch); motion spec designed for streaming is validated.
**Revisit if**: streaming proves technically infeasible within MVP timeline (fallback: batch + subtle pulse animation).

---

## 2026-04-17 — Scan daily limit: 10 scans/day at MVP

**Who decided**: product owner (human)
**Context**: need to protect inference costs during beta while covering real usage.
**Decision**: 10 scans/day per user. At ~$0.02/scan, max cost = $0.20/user/day.
**Options considered**:
- Unlimited (rejected — cost risk before monetization model is set)
- 3/day (rejected — too restrictive for real use)
**Consequences**: rate limiting logic needed in backend; UI must communicate limit gracefully.
**Revisit if**: beta data shows limit being hit by >10% of users → increase or introduce paid tier.

---

## 2026-04-17 — neutral.400 token: darken globally to #7a7570

**Who decided**: product owner (human)
**Context**: neutral.400 (#a09b90) fails WCAG AA for small text on light backgrounds. Two options: darken globally or fix per use-case.
**Decision**: darken globally to #7a7570 across the design system.
**Options considered**:
- Per-use-case fix (rejected — creates inconsistency; harder to maintain)
**Consequences**: token audit pass required; all instances of neutral.400 in specs updated before tech handoff.
**Revisit if**: #7a7570 feels too dark in specific contexts (dark surfaces, large display text) — allow neutral.600 substitution case-by-case.

---

## 2026-04-17 — Amazon PA-API: skipped for MVP

**Who decided**: product owner (human)
**Context**: Google Shopping (via SerpAPI) covers multi-retailer results including brands, multi-brand sites, and 2nd-hand platforms (Vinted, Vestiaire, Depop). Amazon adds little value on fashion in Europe.
**Decision**: skip Amazon PA-API. Google Shopping is sufficient for MVP.
**Consequences**: no affiliate dependency on Amazon at launch. Revisit if catalogue gaps appear in post-launch data.
**Revisit if**: US market launch where Amazon fashion is stronger.

---

## 2026-04-17 — GPU: wait, don't pre-provision

**Who decided**: product owner (human)
**Context**: SPIKE-001 primary pipeline (GroundingDINO + Claude Vision + SerpAPI) runs via API — no GPU needed. GPU only required if primary pipeline fails and fallback (SAM 2 + CLIP) is needed.
**Decision**: provision GPU on-demand only if primary pipeline scores below 75%.
**Consequences**: saves cost; adds ~1 day delay if fallback is needed (acceptable).

---

## 2026-04-17 — SPIKE-001 evaluators: product owner + Linh

**Who decided**: product owner (human)
**Context**: inter-rater reliability requires two independent human evaluators with fashion literacy.
**Decision**: product owner + Linh serve as the two evaluators for the 100-photo test set.
**Consequences**: both must evaluate independently before comparing scores.

---

## 2026-04-16 — Onboarding: form of the first-offering surface (dark primary panel, not two-button fork)

**Who decided**: product-design
**Context**: the offering screen (the first screen that accepts user input, after the
age gate) needed a visual form for presenting two paths: scan vs wardrobe import.
**Options considered**:
- Two equal buttons side-by-side: (rejected — implies parity; scan is primary)
- Two equal stacked buttons: (rejected — button pair looks like an onboarding modal;
  implies the user must choose before seeing anything)
- A single dominant surface (full-width, dark) with primary path + a quiet text link
  below for the secondary path: (chosen)
- An illustration with two zones (tap illustration region): (rejected — illustration
  adds editorial image we don't want in onboarding; see aesthetic direction)
- A single "Start" button leading to a modal fork: (rejected — extra step, no value)
**Decision**: full-width 80px dark surface (`color.brand.primary`) with PP Editorial New
display copy "Scan a photo now" + sub-label "Point at anything with clothes". Secondary
path is a text link with 1px underline below: "Start with my wardrobe". Primary is a
surface you enter; secondary is a sentence you can follow.
**Reasoning**: the visual weight asymmetry reinforces the product priority. Scan is the
differentiator — it should be the invited primary, visually dominant. The text-link for
wardrobe import is not de-emphasized to the point of invisibility; it is clear and tappable.
The dark surface also introduces the `brand.primary` as an active element before any other
usage — it acquaints the user with the ink palette immediately.
**Consequences**:
- +: scan is visually primary without hiding the wardrobe path
- +: avoids the "which button should I press?" decision paralysis of equal options
- +: the dark surface is distinctive — not a generic onboarding button form
- −: some users may not scroll or look for the secondary path below the fold.
  Mitigation: the secondary path sits close enough to the primary (24px gap) to read
  in the same glance.
**Revisit if**: user testing shows >20% of users who intend to start with wardrobe
miss the text-link path and default to scan unwillingly, or show frustration.
**Related**: `specs/onboarding/mockup-spec.md` Screen 2

---

## 2026-04-16 — Onboarding: account creation gating (deferred to first save action)

**Who decided**: product-design
**Context**: the onboarding must not gate first value behind account creation, per the
cold-start mitigation in context.md section 9 and the DISC-001 hypothesis that users
will engage with scan before committing to an account. The question is when exactly
to request account creation.
**Options considered**:
- Account creation as step 1 (before anything): (rejected — maximum friction before
  any value has been delivered; standard onboarding anti-pattern)
- Account creation after age gate, before offering: (rejected — same problem, slightly
  later)
- Account creation after first scan result (automatically, as a "you found something"
  moment): (rejected — interrupts the scan ceremony; account creation should not
  arrive inside a ceremonial flow)
- Account creation deferred until first save/wishlist action: (chosen) — the user
  sees scan results fully without an account. The gate only appears when they try
  to persist something (save to wishlist, return to app with unsaved session).
- Account creation deferred indefinitely (true guest mode): (considered, not fully
  resolved) — flagged as open question for product-lead.
**Decision**: account creation is deferred. The scan results screen is fully accessible
without an account. When the user taps "Save to wishlist" or returns with unsaved
session data, a bottom sheet ("Keep what you found.") presents account creation as
the natural response to a felt need.
**Reasoning**: "Keep what you found." is a statement about the user's situation, not a
pitch for the product. The timing is when the user has already gotten value and wants
to retain it — the highest-intent moment for account creation. This is supported by
standard conversion data: account creation gates at value-delivery points convert
significantly better than gates before value.
**Consequences**:
- +: first value (scan recognition moment) is achievable without registration friction
- +: account creation prompt arrives at maximum user intent
- −: users who close the app before creating an account lose their scan session.
  This is intentional — the copy "Keep what you found." is the solution.
- −: anonymous users can access affiliate deep-links (open question: is this intended?)
**Revisit if**: analytics show high drop-off at account creation after first save (would
indicate the timing is right but the form is wrong) OR very low account creation rates
overall (would indicate too little motivation to create account in the flow).
**Related**: `specs/onboarding/mockup-spec.md` Screen 7, `specs/onboarding/journey-map.md` Beat 5

---

## 2026-04-16 — Onboarding: definition of "first value" (first recognition moment)

**Who decided**: product-design
**Context**: needed to define what "first value" means for onboarding, to anchor all
design decisions around the correct destination.
**Options considered**:
- (a) First successful scan with a useful match (high bar — depends on AI accuracy)
- (b) First wardrobe item added (low bar — this is infrastructure, not differentiator)
- (c) First recognition moment — first garment detected + at least one product match
  visible, in any context, with any confidence level (chosen)
**Decision**: first recognition moment (option c, widened from option a).
**Reasoning**: the whole product lives or dies on the scan being genuinely useful. First
value must be the experience of the AI seeing what the user sees — not just organizing
photos. Wardrobe items are future value; recognition is immediate, present-tense value.
Widening from "useful match" to "any match" is necessary because we cannot gate first
value on SPIKE-001 achieving 80%+ accuracy. Even a partial or approximate result
demonstrates what the product is trying to do, and the user can calibrate from there.
The key: the experience of recognition (the garment label in display serif, the product
cards appearing) must happen in onboarding.
**Consequences**:
- +: onboarding is anchored on the product's core differentiator, not on setup
- +: even an imperfect scan is "first value" — forgiving definition for MVP
- −: depends on the scan working at all in the MVP timeframe (SPIKE-001 prerequisite
  for US-010 is still outstanding)
- Neutral: users who choose the wardrobe-first path will reach first value later,
  only after navigating back to scan. The design accommodates this via the wardrobe
  contextual scan prompt (scan-moment spec State 12).
**Revisit if**: SPIKE-001 shows scan is below useful threshold at MVP launch. In that
case, "first value" must be redefined to "first wardrobe item added" as a fallback,
and the onboarding emphasis shifts accordingly.
**Related**: `specs/onboarding/journey-map.md` (Definition of first value section),
context.md section 9 (cold start risk), backlog.yaml US-010, SPIKE-001

---

## 2026-04-16 — Scan moment: visual metaphor (darkroom contact sheet + atelier pinboard)

**Who decided**: product-design
**Context**: the scan ceremony needed a visual metaphor to anchor all downstream design
decisions (photography treatment, marker form, pace, motion language). Without a
metaphor, individual choices are made in isolation and lose coherence.
**Options considered**:
- Darkroom contact sheet — photographer reviewing negatives on a light table (chosen,
  primary)
- Atelier pinboard — samples pinned to a backing with paper labels (chosen, secondary)
- X-ray scan — clinical reveal of structure beneath surface (rejected: too cold, sci-fi
  connotations, conflicts with editorial register)
- Magnifying glass on a contact sheet — zoom and scrutiny (rejected: too literal,
  implies the user is doing the looking, not the AI)
- App store AR scan (Lens-style) — real-time detection (rejected: cliché, already owned
  by Google/Snapchat)
**Decision**: darkroom contact sheet (primary) + atelier pinboard (secondary)
**Reasoning**: both metaphors are rooted in fashion and photography craft, consistent
with the brand's editorial identity. They govern: grain texture as darkroom paper,
slow reveal as development, marker as paper label, desaturation as "archived photo",
the detection pause as the moment before speaking.
**Consequences**:
- +: every design decision has a test ("does this feel like a darkroom / an atelier
  pinboard?")
- +: differentiates immediately from Google Lens, Instagram Shop, and AR try-on
- −: grain texture requires a real asset (PNG); CSS-only solution is insufficient
**Revisit if**: user testing shows the metaphor reads as "old" or "antique" rather
than "editorial" to the 20-40 target audience. (Risk is low — System Magazine / COS
aesthetic is familiar to this cohort.)
**Related**: `specs/scan-moment/aesthetic-direction.md`

---

## 2026-04-16 — Scan moment: marker form (numbered underline, not pin/reticle/box)

**Who decided**: product-design
**Context**: garment markers on the photo surface are the most visible element of the
scan ceremony. Their form directly communicates the app's aesthetic register and
differentiates from competitors.
**Options considered**:
- Numbered underline: 1px terracotta line + number label (chosen) — textile sample card
  reference
- Bounding box / rectangle: standard ML output form (rejected — reads as developer tool)
- Circular reticle: crosshair or ring (rejected — sci-fi, Google Lens association)
- Pin/bubble tag: shopping app convention (rejected — commerce-first, not editorial)
- Solid highlight fill: color overlay on garment region (rejected — crude, loses photo)
- Dot with line connecting to margin label: editorial magazine annotation style
  (considered seriously — deferred to v2 if numbered underline tests poorly; requires
  more complex coordinate math)
**Decision**: numbered underline (1px, 20px wide, terracotta #c85a3c) with PP Neue
Montreal xs number label above the line, positioned at garment center-of-mass with
small offset toward lower-left.
**Reasoning**: minimum surface intervention on the photo. The underline is typographic,
not graphical. It reads as an annotation, not a selection. The number creates a
catalogue system (garment 1, 2, 3) that connects to the product panel below.
**Consequences**:
- +: visually unique in the fashion-app space
- +: consistent with the atelier pinboard metaphor
- +: minimum complexity to implement (no path-drawing, no segmentation mask display)
- −: relies on accurate center-of-mass from AI bounding box; if bounding box is poor,
  marker may sit in the wrong place. Acceptable for MVP.
**Revisit if**: SPIKE-001 reveals that AI bounding boxes are too imprecise to place
markers meaningfully. In that case, fall back to a single non-positioned label.
**Related**: `specs/scan-moment/aesthetic-direction.md`, `specs/scan-moment/mockup-spec.md`

---

## 2026-04-16 — Scan moment: no progress spinner, stillness as confidence signal

**Who decided**: product-design
**Context**: during AI processing (1.5–5.5s), the user is waiting. Every conventional
app fills this with a progress indicator. We need to decide what to show.
**Options considered**:
- Spinner / activity indicator: standard loading pattern (rejected — communicates
  "struggling", destroys ceremony)
- Progress bar with percentage: (rejected — false precision, antithetical to the
  darkroom metaphor)
- Pulsing glow or animated marker placeholder: (rejected — decorative loading, cliché)
- Skeleton screens: (rejected — no meaningful skeleton for an unknown photo)
- Stillness: the grain-textured photo, no movement, no progress. With a single
  "Still analyzing…" text line appearing only after 4s. (chosen)
**Decision**: stillness during scan. No progress indicator. Grain texture is the only
surface effect. "Still analyzing…" text appears at 4s as a single-line acknowledgment.
**Reasoning**: stillness communicates confidence. The darkroom doesn't apologize for
taking time to develop. A spinner says "the system is working on it"; stillness says
"the photograph is being read." The 4s text line is a safety valve only — most scans
complete before it appears.
**Consequences**:
- +: ceremony is preserved, no visual noise
- +: differentiating — no other app does this
- −: if AI is slow (>4s frequently), the "Still analyzing…" line appears often and
  the experience may feel uncertain. Mitigation: ensure AI pipeline targets <3.5s P90.
**Revisit if**: user testing shows the stillness reads as "broken" rather than
"deliberate." Fallback is a very subtle pulse on the grain texture (not a spinner).
**Related**: `specs/scan-moment/motion-spec.md`, `context.md#7-constraints` (6s budget)

---

## 2026-04-16 — Scan moment: pre-scan confirm beat retained

**Who decided**: product-design
**Context**: after the user selects or takes a photo, do we auto-launch the scan, or
show a confirm screen? Friction vs. ceremony trade-off.
**Options considered**:
- Auto-launch scan immediately after photo selection: lower friction (rejected — the
  user is a passive spectator; removes the beat of intention)
- Show confirm screen with "Scan" button: chosen
**Decision**: confirm screen retained. The "Scan" button is the user's choice to begin.
**Reasoning**: the confirm screen is the title page before the essay — a moment of
authorship before the ceremony. It also reduces accidental scans. The added friction
is ~0.5s and one tap; the gained intentionality is worth it for a ceremonial feature.
**Revisit if**: user testing shows the confirm screen is skipped quickly or frustrates
users who selected the wrong photo (suggests they want more editing, not less friction).
**Related**: `specs/scan-moment/mockup-spec.md` State 5

---

## 2026-04-16 — Scan moment: product sort default is best-match, not price-ascending

**Who decided**: product-design
**Context**: US-010 requires sort by price ascending/descending. We must also define a
default sort order for the results state.
**Options considered**:
- Price ascending (cheapest first): common e-commerce default (rejected — prioritizes
  cheapest over most relevant; conflicts with editorial register)
- Price descending (most expensive first): (rejected — arbitrary, no editorial logic)
- Best match (AI relevance score): (chosen) — highest-quality match shown first
**Decision**: default sort is best match (AI relevance). Price sorts are available via
the sort control.
**Reasoning**: the core promise of the scan is "find what matches this garment." If we
default to price, we undermine that promise. Users who want cheap first can sort; users
who want the best match see it by default.
**Revisit if**: A/B test shows price-ascending default drives higher tap-through rate
(business reason to override). This is a product-lead decision when data is available.
**Related**: `specs/scan-moment/mockup-spec.md` State 7

---

---

## 2026-04-16 — Project working name: "Atelier"

**Who decided**: product-lead (proposed), pending human confirmation
**Context**: project needed a working name to start files and conversations
**Options considered**:
- Atelier — French for workshop/studio, evokes fashion craft (chosen)
- Studio — too generic
- Runway — over-claimed in fashion space
- Closet — too literal, low brand potential
**Decision**: Atelier
**Reasoning**: evocative, memorable, signals craft + personal space. Available as a domain class.
**Consequences**:
- +: sets editorial tone for brand
- −: requires trademark search before public launch
- Neutral: not a final product name; can rebrand before launch
**Revisit if**: trademark conflict found OR user strongly prefers another direction
**Related**: `context.md#1-identity`

---

## 2026-04-16 — North star metric: Weekly Active Stylists (WAS)

**Who decided**: product-lead
**Context**: needed a single measurable metric that reflects the core value, not vanity
**Options considered**:
- DAU / MAU — too generic, doesn't measure the core curatorial behavior
- Wardrobe items added — one-time action, doesn't measure engagement
- Looks created per week — the actual creative behavior (close to chosen)
- Weekly Active Stylists (user with ≥1 look created/edited this week) (chosen)
**Decision**: Weekly Active Stylists
**Reasoning**: captures active curation, distinguishes from passive scrolling, composable (WAS × retention = growth model)
**Consequences**:
- +: forces design to support the curatorial loop
- +: filters out passive users from "engaged" count
- −: high bar — first weeks of usage may look low
**Revisit if**: user research shows curation is not the primary value people get
**Related**: `context.md#2-vision`

---

## 2026-04-16 — Aesthetic direction: editorial maximalism × studio minimalism

**Who decided**: product-lead proposed direction; product-design to execute and refine
**Context**: fashion app category is saturated with Instagram-clone aesthetics; needed a distinctive point of view
**Options considered**:
- Conventional app design (Inter, card UI, neutral palette) — rejected, looks like every other app
- Playful / Gen Z maximalism (bright colors, chunky type) — rejected, doesn't match target audience (20-40)
- Editorial maximalism × studio minimalism (chosen)
- Pure luxury minimalism (à la Hermès) — rejected, too cold for curation + sharing
**Decision**: editorial maximalism × studio minimalism
- Serif display (PP Editorial New / GT Super / Apoc) + humanist sans (PP Neue Montreal / Söhne)
- Near-black ink on warm off-white
- One seasonal accent color (start: terracotta)
- Radical asymmetry in layout
- Cinematic motion (400ms+ easings)
- "Scan" moment as signature interaction
**Reasoning**: differentiates immediately, matches audience sophistication, lets product imagery (our primary content) dominate
**Consequences**:
- +: memorable first impression
- +: harder to clone (requires actual taste)
- −: higher design execution bar than generic defaults
- −: font licensing costs (PP Editorial New commercial licenses are non-trivial)
**Revisit if**: user testing reveals the aesthetic feels exclusionary to target audience
**Related**: `context.md#4-aesthetic-direction`, `design_system/tokens.yaml`

---

## 2026-04-16 — Proposed stack: React Native + Expo, Python FastAPI, CLIP + SAM 2

**Who decided**: product-lead proposed; product-tech to validate via SPIKE-001
**Context**: need to ship iOS + Android quickly with heavy AI/ML pipelines
**Options considered**:
- Native Swift + Kotlin — rejected (2× engineering cost at MVP)
- Flutter — rejected (weaker ML/camera ecosystem)
- React Native + Expo (chosen) — fastest to MVP, native modules where needed
- Node.js backend — rejected (would need separate Python service for ML anyway)
- Python FastAPI backend (chosen) — dominant ML ecosystem
**Decision**: React Native + Expo frontend, Python FastAPI backend, CLIP + SAM 2 for AI pipelines
**Reasoning**: minimizes engineering effort at MVP, aligns with where ML talent and libraries are strongest
**Consequences**:
- +: one codebase for both platforms
- +: direct access to ML ecosystem
- −: some native performance compromises vs pure native (acceptable at MVP)
- −: managed Expo has some limitations; may need to eject later
**Revisit if**: SPIKE-001 reveals performance bottlenecks that can't be solved in React Native
**Related**: `context.md#5-tech-stack`, SPIKE-001

---

## 2026-04-16 — MVP scope: wardrobe core + scan + looks. Deferred: feed, social, measurements, video

**Who decided**: product-lead
**Context**: original requirement was broad (wardrobe + looks + posting + AI scan + measurements + social comparison); needed to scope MVP
**Options considered**:
- Ship everything at MVP — rejected (18+ weeks minimum, core value not yet validated)
- Ship wardrobe only — rejected (not differentiated enough; scan is the wow)
- Wardrobe + scan + looks, defer social/video/measurements (chosen)
**Decision**: 3 epics in MVP — wardrobe core, scan (core differentiator), looks. Social feed, video posts, body measurements all deferred to v2.
**Reasoning**: scan is the differentiator and must work; wardrobe + looks provide daily use even if scan underperforms; social adds cost and moderation complexity without proving core hypothesis
**Consequences**:
- +: 8-12 week MVP timeline
- +: clean hypothesis test — does scan + curation generate WAS?
- −: defers monetization pathway (affiliate clicks from scan are primary; content monetization comes later)
**Revisit if**: beta shows strong user demand for posting/sharing BEFORE scan accuracy issues (would mean social is the real pull)
**Related**: `backlog.yaml`, `roadmap.yaml`
