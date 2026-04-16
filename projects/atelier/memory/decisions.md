# Decisions — Atelier

Append-only log of significant decisions. Latest at top. Every entry includes context, options, reasoning, and revisit condition.

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
