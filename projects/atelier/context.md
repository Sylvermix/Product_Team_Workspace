# Project Context: Atelier

> AI-native mobile app for wardrobe building, outfit curation, and shoppable content.

---

## 1. Identity

- **Project name**: Atelier (working name — French for "workshop / studio", evokes fashion craft)
- **One-line pitch**: An AI-native mobile app where you build your wardrobe, curate looks, share outfit content, and instantly find where to buy anything you see.
- **Stage**: `idea` (pre-MVP)
- **Started**: 2026-04-16
- **Links**: TBD (repo, staging URL, etc.)

---

## 2. Vision & outcome

- **North star metric**: **Weekly Active Stylists** — users who create or edit at least one look per week. Captures the core curatorial behavior, not passive scrolling.
- **Current value**: 0 (pre-launch)
- **12-month target**: 10,000 WAS post-launch (recalibrate after beta)
- **Secondary metrics**:
  - Look creation rate per active user
  - Product search-to-tap conversion (AI-identified product → user taps through to retailer)
  - Wardrobe completeness (items added per user)
- **Why this matters**: people spend money on clothes they never wear and waste time deciding what to wear. A digital wardrobe + AI-driven shopping intelligence turns "what do I have?" and "where can I get that?" into solved problems. The frontier unlocks this: AI can now actually *see* clothes, *identify* them, and *find* them.

---

## 3. Audience

- **Primary user segment**: fashion-conscious individuals, 20-40, who already shop intentionally, follow style content, and spend time planning outfits. Phone-native. Comfortable uploading photos and videos. Shop both online and in-store.
- **Secondary segments**:
  - People trying to organize their existing wardrobe (Marie Kondo energy)
  - Content creators already posting outfit videos, wanting shoppable tagging
- **Not our users**:
  - Casual dressers who don't care about outfit curation
  - Ultra-luxury shoppers (price discovery isn't their use case)
  - Under-18 users (no minors feature — privacy/safety)
- **Key insights to validate in discovery**:
  - Do users want to *build* a digital wardrobe (high effort) or just *discover* products? Answer shapes MVP scope.
  - How accurate must AI product identification be before it's useful vs annoying? Target: 80%+ top-3 match rate.
  - Is body measurement data something users will share? Privacy-sensitive — may need alternatives (fit preferences, not exact measurements).

---

## 4. Aesthetic direction (default)

The Design agent uses this as the starting point. Fashion apps that fail all look the same: Instagram clone grid, generic sans-serif, neutral palette. We go the other way.

- **Tone**: **"editorial maximalism meets studio minimalism"** — product imagery is maximalist (full-bleed, generous, rich color) while UI chrome is radically minimal (sparse, architectural). Think COS store interior × *System Magazine* layout.
- **Typography pairing**:
  - **Display**: a characterful serif — `PP Editorial New`, `GT Super`, or `Apoc Revelations`. Editorial, not corporate. Generous tracking at large sizes.
  - **Body**: a humanist sans — `PP Neue Montreal`, `Söhne`, or `ABC Diatype`. Never Inter/Roboto/SF Pro.
- **Color strategy**:
  - **Dominant**: near-black ink (`#1a1a1c`) on warm off-white (`#f6f3ed`) — high contrast, editorial, lets product imagery breathe
  - **Accent**: one bold seasonal color that rotates (launch with warm terracotta `#c85a3c` or deep mauve `#7a4e5a`)
  - **No gradients**, no purple, no candy colors
- **Spatial approach**: radical asymmetry. Products break the grid. Text sits in unexpected alignments. Generous whitespace at the top of every screen (breathing room), dense content below.
- **Motion intent**:
  - Luxurious, slow, purposeful — 400ms+ easings
  - One staggered reveal per screen load
  - Product cards have subtle parallax on scroll
  - No playful bounces, no springs, no haptic-heavy interactions
- **Memorable differentiator**: **the "scan" moment**. When the user takes/uploads a photo, the AI identifying products is a ceremonial reveal — the image stays full-bleed, UI dims, subtle scan lines or highlight markers trace across garments as they're detected, then product cards slide up from the bottom with tactile weight. The 5 seconds people screenshot and share.

### Anti-patterns for this project specifically
- No generic Instagram-clone feed
- No "shop now" CTAs shouting at the user
- No excessive filter/category chips cluttering the UI
- No heart/like icons doing heavy lifting (find an alternative)
- No onboarding tour — let the product speak

---

## 5. Tech stack

### Proposed decisions (validate with product-tech)

- **Frontend**: **React Native with Expo** (ship iOS + Android from one codebase)
  - Rationale: fastest to MVP, native modules available for camera/ML
  - Rejected: native Swift + Kotlin (2× engineering cost at MVP)
  - Rejected: Flutter (smaller ML/camera ecosystem)
- **Camera**: Expo Camera + custom native modules for advanced capture if needed
- **State**: Zustand or Jotai (not Redux at MVP)
- **Styling**: NativeWind (Tailwind for RN) + custom design system on tokens
- **Animations**: Reanimated 3 + Moti for orchestrated sequences

- **Backend**: **Python (FastAPI)** + worker queues (Celery + Redis) for ML pipelines
  - Rationale: Python dominates ML ecosystem; image/ML pipelines are core
  - Rejected: Node.js (weaker ML ecosystem, would need a Python service anyway)

- **Database**:
  - **Postgres** for structured data (users, wardrobes, looks, posts)
  - **Object storage** (S3-compatible) for images and videos
  - **Vector DB** (Pinecone, Qdrant, or Postgres pgvector) for image embeddings (similarity search)

- **AI stack**:
  - **Garment segmentation**: SAM 2 (Meta) or GroundingDINO — isolate garments in an image
  - **Garment classification**: CLIP fine-tuned, or Claude Vision / GPT-4V for category/color/style attributes
  - **Product search**: SerpAPI (Google Shopping), Amazon PA-API, retailer-specific APIs (ASOS, Zalando, etc.)
  - **Image-to-product matching**: CLIP embeddings + vector search across indexed product catalog
  - **Video analysis**: frame sampling + per-frame garment detection + temporal dedup

- **Third-party APIs (to evaluate)**:
  - SerpAPI / Google Shopping — product search by image/text
  - Amazon Product Advertising API — catalog + affiliate
  - RapidAPI marketplaces — aggregate retailer APIs
  - Shopstyle / Rakuten Advertising — affiliate networks + product feeds
  - Trustpilot / review aggregators — customer reviews

- **Infra**:
  - **Hosting**: AWS or GCP (ML-friendly regions, GPU for embeddings)
  - **CDN**: Cloudflare (images + video)
  - **Auth**: Clerk or Auth0 (faster than DIY)
  - **Analytics + flags**: PostHog
  - **Errors**: Sentry
  - **CI/CD**: GitHub Actions → EAS Build (Expo) + backend deploy

- **Testing**: Vitest (FE units), Detox (mobile e2e), pytest (BE), visual regression on design system

### Architecture style
Modular monolith backend to start. Microservices only if justified later. ML inference decoupled from API as worker jobs.

### Deployment strategy
- Backend: gradual rollout with feature flags (PostHog)
- Mobile: phased TestFlight / Play Console releases, gradual store rollout

---

## 6. User access model (validated 2026-04-17)

| Action | Anonymous | Logged-in |
|--------|-----------|-----------|
| Browse public profiles | ✅ | ✅ |
| Tap affiliate product links | ✅ | ✅ |
| Scan a photo | ❌ | ✅ |
| Build wardrobe | ❌ | ✅ |
| Create looks | ❌ | ✅ |
| Like products / wishlist | ❌ (prompted to sign up) | ✅ |

Account creation is deferred to the first "save" action. Scan results are visible before account creation.

Scan intent splits into two flows:
- **"I own this"** → adds to wardrobe (requires account)
- **"I want this"** → adds to wishlist (requires account; anonymous sees results but can't save)

## 7. Current priorities

Top 7 epics for MVP:

1. **Wardrobe core** — scan garments, mandatory size capture per item, AI auto-tags. Foundation for everything.
2. **Scan** — AI identifies garments in any photo. Two intents: add to wardrobe (size required) or save to wishlist.
3. **Look creation** — assemble saved garments into named outfits.
4. **AI Agent (prompt bar)** — persistent throughout the app. Handles conversational product search, style profile building, and pushes products to wishlist. No forms — everything collected naturally through conversation and scan.
5. **Product detail enriched** — multi-retailer price comparison (real-time, sorted), synthetic review summary (AI-aggregated), size social proof from users with similar profiles.
6. **Public profiles + social discovery** — public wardrobe/looks, follow recommendations based on style match + size match.
7. **Creator monetization (V2)** — commission sharing with users who drive sales via their profiles. Architecture defined; implementation deferred.

## 7b. Size profile strategy

Size is collected **implicitly and mandatorily** through wardrobe scans — never via a standalone form. Every garment added requires a size. After 5+ items, the app has a brand-aware size profile per category. This feeds:
- Size social proof on product detail ("users like you chose M at Sandro")
- Follow recommendations (size match as a filter)
- Future fit intelligence

The AI agent also collects style preferences, taste, and aesthetic direction conversationally — no onboarding questionnaire.

**Explicitly deferred (v2):**
- Posting videos/photos to a feed
- Full social feed (following, comments)
- Body measurements (needs careful privacy design)
- Shoppable video content
- Creator monetization

---

## 8. Constraints

### Legal / compliance
- **GDPR (EU)**: users can export/delete all data; photos + measurements are personal data with elevated sensitivity
- **CCPA (California)**: similar rights
- **Minors**: no accounts under 18 (birthdate gate at signup)
- **Photo/image usage**: user photos private by default; retailer product imagery used under affiliate/fair-use terms (verify per-retailer)
- **Affiliate disclosure**: FTC-equivalent disclosure where affiliate links appear

### Performance budgets (mobile, critical)
- App launch → home in < 2s cold, < 500ms warm
- Photo upload → scan result visible in < 6s (progressive reveal OK)
- Wardrobe grid scrolls 60fps with 500+ items
- Image loading: LQIP → full within 300ms on 4G

### Budget targets
- AI inference per scan: < $0.02 (hosted + own embeddings)
- Infra cost per MAU: < $0.50 at 10k MAU

### Device support
- iOS 16+ (~95% of iOS users)
- Android 10+ / API 29+ (~90% of Android users)

### Timeline (aggressive — adjust after feasibility)
- MVP beta: 12 weeks from start
- Public launch: 16-20 weeks from start

---

## 9. Key decisions history

*Appended as decisions are made.*

- **2026-04-16** — Project initialized. Working name "Atelier". Aesthetic direction set to editorial-maximalism / studio-minimalism. React Native + Python FastAPI + CLIP-based product matching proposed as default stack (pending feasibility validation).

---

## 10. Active risks

- **AI product identification accuracy** — could kill the core value prop if < 70% useful match rate. **Mitigation**: dedicate first spike to validating matching quality before committing full MVP.
- **Product catalog access** — retailer APIs may have restrictive terms, rate limits, high cost. **Mitigation**: stack multiple sources; plan graceful degradation.
- **Inference cost at scale** — per-photo analysis is expensive. **Mitigation**: aggressive embedding cache, only re-run on new photos, batch where possible.
- **Cold start** — empty wardrobe is useless. **Mitigation**: onboarding imports 5-10 items via photo roll; scan feature works without a wardrobe (instant value).
- **Legal gray areas** — scraping, retailer imagery, affiliate terms. **Mitigation**: legal review before public launch; legitimate APIs + affiliate networks from day one.
- **Body data privacy** — users may not share measurements. **Mitigation**: make measurements optional; never public; consider fit-preferences alternative.
- **App store policies** — shoppable content + body data may trigger enhanced review. **Mitigation**: review Apple/Google policies during design phase; build disclosure UX early.

---

## 11. Team & stakeholders (human side)

*Fill in by the human owner.*

- **Product owner**: [name] — decision authority on scope, priority, business
- **Engineering lead**: [name]
- **Design lead**: [name]
- **Key stakeholders**: [names]
- **AI advisor**: [recommended for an ML-heavy project]
- **Legal advisor**: [recommended before public launch]
- **Decision-making**: product owner has final call on scope; engineering on feasibility; design on visual direction within aesthetic guardrails.
