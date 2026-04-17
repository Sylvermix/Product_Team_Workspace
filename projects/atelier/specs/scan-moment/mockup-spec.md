# Mockup Spec: The Scan Moment
**Atelier — US-010 | Scan any photo to identify garments and find matching products**
Design agent — 2026-04-16

All token references are from `design_system/tokens.yaml` v0.1.0 unless marked [NEW TOKEN].

---

## State 1: Entry point — Scan button placement

### Where the button lives
The scan trigger appears in three locations per US-010 acceptance criteria:

**A. Home screen — persistent placement**
- Position: fixed bottom-right, 24px from right edge, 24px above the home indicator
  safe area.
- Form: a 56×56px circular touch target. Interior is the camera glyph (minimal, single
  path, 20×20px effective, `stroke: 1.5px`, color `color.brand.secondary #f6f3ed`)
  on a background of `color.brand.primary #1a1a1c`. No label visible by default.
- On long-press (300ms): a text label "Scan" slides out to the left of the button in
  PP Neue Montreal, `font-size: sm (14px)`, `letter-spacing: editorial (0.12em)`,
  color `color.brand.primary`. This is an affordance hint, not a permanent label.
- Accessibility: `aria-label="Scan photo to find garments"`, touch target 56×56px
  (exceeds 44px minimum). Screen reader: announces "Scan photo to find garments, button."

**B. Wardrobe screen — contextual placement**
- Same button form. Position: same bottom-right fixed position.
- On first visit (empty wardrobe state only): an inline text prompt appears above the
  button — "Scan inspiration from your camera roll" — in PP Neue Montreal,
  `font-size: sm`, `color.neutral.600 #5a5651`. This disappears once any garment
  is added. See State 12 (empty state / first scan).

**C. Any photo view (garment detail, look preview)**
- A secondary scan button appears in the top-right of the photo header:
  a 44×44px touch target containing the same camera glyph in `color.brand.primary`.
  Label: "Find similar" in `font-size: xs (12px)`, `letter-spacing: editorial (0.12em)`,
  `color.neutral.600`. This targets the specific item photo as scan input.

### Visual rationale
A fixed bottom-right position follows established native conventions while the circular
dark button is visually distinctive — it reads as a camera shutter reference without
being clichéd. No FAB-style shadow (shadows are decoration; this is editorial).

---

## State 2: Capture / upload chooser

**Trigger**: user taps any scan button.

**Presentation form**: a bottom sheet, not a modal overlay. The sheet rises from the
bottom, 320px tall on mobile, with `border-radius: lg (8px)` on top corners only.
Background: `color.surface.card (#fbfaf7)`. No scrim darkening the content behind it —
the sheet is a surface that arrives, not a lock-screen.

**Layout** (top to bottom, within sheet):
- A 4px × 36px drag handle, `color.neutral.200 (#e8e3d7)`, centered at top, 12px top
  margin. No label.
- Heading (16px top margin): "Scan a photo" — PP Editorial New, `font-size: xl (22px)`,
  `font-weight: 400`, `letter-spacing: tight (-0.02em)`, `color.brand.primary`.
- Two options (32px top margin), stacked vertically, 16px gap:

  **Option A — Camera**
  - Full-width touch target, 64px tall, no border, no background fill.
  - Left edge: camera glyph (20×20px, `stroke: 1.5px`, `color.brand.primary`)
  - Right of glyph (12px gap): "Take photo" in PP Neue Montreal, `font-size: base (16px)`,
    `color.brand.primary`
  - Sub-label beneath "Take photo": "Use your camera now" in `font-size: sm (14px)`,
    `color.neutral.400 (#7a7570)`
  - Tap: opens camera view (State 3).

  **Option B — Photo library**
  - Same form.
  - Glyph: a 2×3 grid of small squares (representing photo roll), `stroke: 1.5px`
  - Label: "Choose from library"
  - Sub-label: "Select from your camera roll"
  - Tap: opens native OS photo picker (State 4).

- 24px bottom safe area padding.

**URL paste / web URL input**: deferred from MVP. US-010 does not mention it and it adds
scope. Omitted. Flagged for potential v2 addition.

**Accessibility**: both options are full-width touchable regions ≥64px tall (exceeds
44px minimum). Screen reader announces each as a button with full label + sub-label.
Drag handle has `aria-hidden="true"`. Sheet close on Escape or swipe-down gesture.

---

## State 3: Camera view

**Layout**: full-bleed camera preview, 100% of viewport.

**Framing guide**: none. No reticle, no rectangle guide. The viewfinder is the world.
This is a deliberate choice: garment detection does not require a precise frame; guiding
with a box would suggest otherwise and creates false precision anxiety.

- Top bar (44px safe area + 16px padding): a single back-arrow (24×24px glyph, white
  `#f6f3ed`) on the left. `aria-label="Cancel scan"`. Nothing else in the top bar.
- Bottom tray (fixed, 100px tall + bottom safe area): centered shutter button.

**Shutter button**:
- 72×72px outer ring (1px stroke, `#f6f3ed` at 60% opacity).
- 56×56px inner filled circle, `#f6f3ed` at 100%.
- No text label. Its form communicates its function.
- Tap: captures photo, advances to State 5 (pre-scan confirm) or directly to State 6
  depending on confirm decision (see State 5).
- `aria-label="Take photo"`, touch target 72px (exceeds minimum).

**Flash / torch toggle**: not in MVP. Deferred.

**Switch to upload**: a text link in the bottom tray, right-aligned: "Library" in
PP Neue Montreal, `font-size: sm (14px)`, `color.neutral.100 (#f6f3ed)`.
`aria-label="Choose from photo library instead"`.

**Responsive**: full-bleed camera preview works identically on all screen sizes; the
tray is fixed at the bottom.

---

## State 4: Upload / photo roll selection

**Native OS picker**: we use the native system photo picker (iOS PHPickerViewController,
Android PhotoPicker). No custom picker in MVP. The native picker:
- Requires no additional photo library permissions on iOS 14+
- Is well-understood by users
- Requires no design work — it is a system surface

**Post-selection**: after user selects a photo, the native picker dismisses. The app
receives the photo. Advance to State 5 (pre-scan confirm).

**Multi-select**: US-010 specifies one scan at a time (not batch). However, US-002
allows multi-select for wardrobe adds. The scan flow is single-photo only in MVP.
If a user attempts to select multiple (native picker may allow it), we accept only the
first and ignore the rest — no error message needed; the picker itself should be
configured for single selection.

---

## State 5: Pre-scan confirm — the beat of intention

**Decision**: we include a confirm beat. Here is the defense.

The confirm screen serves two purposes that exceed friction-reduction math:
1. It gives the user one moment of authorship — "this is the photo I chose." Without
   it, the scan fires automatically and the user is a passive spectator. With it, they
   choose to proceed. This matches the emotional register of "recognition" — it should
   feel intentional.
2. It is the last moment before the ceremony begins. A breath before the reveal. In
   editorial terms: a title page before the essay.

**Layout**:
- The chosen photo fills the top 72% of the screen, full-width, no crop (letterboxed if
  needed — black bars using `color.brand.primary #1a1a1c`).
- Bottom 28%: `color.brand.primary #1a1a1c` background.
- In the bottom region, centered vertically:

  **Primary action — "Scan"**
  - Form: full-width text label only (no icon). Width: screen width minus 32px
    horizontal margin. Height: 56px. No border radius (sharp, editorial).
  - Background: `color.brand.secondary (#f6f3ed)`.
  - Text: "Scan" — PP Neue Montreal, `font-size: base (16px)`, `font-weight: 400`,
    `letter-spacing: editorial (0.12em)`, color `color.brand.primary`.
  - Tap: begins scan (State 6).
  - `aria-label="Scan this photo"`, touch target 56px height.

  **Secondary action — "Choose another"**
  - Below primary button, 12px gap.
  - Text only, no button background. "Choose another photo" — PP Neue Montreal,
    `font-size: sm (14px)`, `color.neutral.400 (#7a7570)`.
  - Returns user to State 2 chooser.

- Top-left: back arrow (24×24px, white) to dismiss entirely.

**Copy**: no instructional copy. No "We'll identify the garments in this photo." The
user knows. The button says Scan. That is enough.

**Accessibility**: primary button contrast — `#1a1a1c` text on `#f6f3ed` = 16.7:1 (pass).
Photo: `alt="Selected photo for scanning"`.

---

## State 6: Scanning — "the ceremony"

This is the signature moment. Every design decision here is load-bearing.

**Layout**: the photo is full-bleed, 100% of viewport. No chrome visible except the
cancel affordance.

**Top**: a back arrow (white, 24×24px, top-left, within safe area). No label.
`aria-label="Cancel scan"`. This is the only UI element during scanning.

**Photo treatment**:
- Photo fills the screen at 100% saturation and brightness.
- A grain texture layer sits over the photo at 8% opacity [NEW TOKEN: `grain_opacity`],
  blended at multiply. This is present from the moment scanning begins.
- No animated scan line. No pulsing glow. No progress ring. The grain and the marker
  reveal are the only surface effects.

**Garment detection reveal — progressive sequence**:

When a garment is detected by the AI (which returns detections progressively or as a
batch — the reveal handles both; see motion spec for timing):

Each detected garment receives a **numbered underline marker**:
- A 20px wide, 1px tall horizontal line in `color.brand.accent #c85a3c` [NEW TOKEN:
  `marker_underline_width: 20px`], positioned beneath the garment's visual
  center-of-mass.
- Directly above the line (4px gap): the garment number in PP Neue Montreal, `font-size:
  xs (12px)`, `letter-spacing: editorial (0.12em)`, `color.brand.accent #c85a3c`.
- The underline and number animate in together (see motion spec).

**Position of marker**: the marker sits on the garment itself. For a jacket, it would
sit at approximately chest height. For trousers, at thigh. Not at the garment's very
center (too obvious) — slightly offset toward the lower-left of the detected region,
following the atelier pinboard metaphor (labels sit below and to the left of a sample).
Exact coordinates are computed from the AI segmentation bounding box center-of-mass,
with a -10% Y offset from center and -5% X offset from center.

**The luminance lift**: as each marker appears, the garment's region receives a subtle
radial brightness lift (implementation: a white radial gradient at 6% opacity,
composited over the photo at the marker position, radius 80px). Duration: 300ms in,
400ms out. This is the "light catching the photograph" effect from the aesthetic
direction. It is not a glow; it is closer to a sheen.

**Text during scan**: none. No "Identifying garments…" caption. No label, no status
copy. The ceremony does not narrate itself.

**If the scan takes longer than 4 seconds with no markers appearing**: after 4s, a
single line of text fades in at the very bottom of the screen (above bottom safe area),
centered: "Still analyzing…" — PP Neue Montreal, `font-size: sm (14px)`,
`color.neutral.400 (#7a7570)` at 80% opacity. It fades out when the first marker
appears. This is the only progress signal. It is an acknowledgment, not an apology.

**Accessibility during scan**:
- `aria-live="polite"` region at the bottom. When scanning begins: announces "Scanning
  photo for garments." When first marker appears: announces "Garment 1 detected." For
  each subsequent: "Garment [N] detected." When complete: "Analysis complete.
  [N] garments identified. Results loading."
- Screen readers do not wait for the visual reveal — they announce immediately as data
  arrives.
- Reduced-motion: no grain, no luminance lift, no staggered marker arrival. Markers
  appear simultaneously at detection complete. See motion spec.

---

## State 7: Results — primary state

**Layout**:
- The photo compresses to occupy the top 55% of the viewport [NEW TOKEN:
  `photo_split_results: 55%`]. It does not scroll. It is fixed.
- The bottom 45% (plus any scroll extension) is the product panel.

**Photo plane (top 55%)**:
- Photo is desaturated 10% toward gray [NEW TOKEN: `garment_desaturation_after: 0.10`].
- A vertical vignette gradient sits on the bottom edge only: from `transparent` to
  `rgba(26,26,28, 0.28)` [NEW TOKEN: `vignette_opacity: 0.28`], occupying the bottom
  80px of the photo plane. This creates the plane separation without a visible line.
- Garment markers remain visible. Active garment marker is terracotta. Inactive markers
  are `color.neutral.400` at 60% opacity.
- Garment selector tabs appear at the bottom of the photo plane (overlapping the
  vignette region), left-aligned, 16px from left edge. These are numbered pill tabs
  (see State 8 for multiple garments).

**Product panel (bottom 45%+)**:
- Background: `color.surface.card (#fbfaf7)`.
- No visible border between photo plane and product panel — the vignette + color change
  creates the separation.

**Garment label — the display serif moment**:
- At the top of the product panel (16px from top of panel, 16px from left edge):
  the identified garment category name in PP Editorial New, `font-size: 3xl (36px)`,
  `font-weight: 400`, `letter-spacing: tight (-0.02em)`, `line-height: tight (1.1)`,
  `color.brand.primary (#1a1a1c)`.
- Examples: "Trench coat." / "Straight-leg denim." / "Leather loafer."
- Period at the end of the label. This is editorial. It signals finality, like a
  caption in a fashion editorial.
- Below the label (4px gap): match count and sort/filter controls (see below).

**Match count and controls** (below garment label):
- "12 matches" in PP Neue Montreal, `font-size: sm (14px)`, `color.neutral.600
  (#5a5651)`, `letter-spacing: editorial (0.12em)`. Left-aligned.
- Right-aligned on the same row: "Sort" and "Filter" — both are text-only links, no
  button chrome. PP Neue Montreal, `font-size: sm (14px)`, `color.neutral.600`. A
  thin vertical separator (`color.neutral.200`, 1px, 12px tall) between them.
  Touch targets: each has 44px minimum tap area via invisible padding.

**Product cards** (scrollable, below match count):
- Cards are stacked vertically (single column) with 1px separator between them
  (`color.neutral.200 #e8e3d7`). No card borders or individual card backgrounds —
  cards sit on the panel background.
- Card anatomy (64px minimum height, comfortable scroll):
  - Left: product image, 64×64px, `border-radius: sm (2px)`, object-fit: cover.
  - Right of image (12px gap): two rows of text.
    - Row 1: retailer name in PP Neue Montreal, `font-size: xs (12px)`,
      `letter-spacing: editorial (0.12em)`, `color.neutral.400 (#7a7570)`, uppercase.
    - Row 2: product description (max 2 lines) in PP Neue Montreal, `font-size: sm
      (14px)`, `color.brand.primary`.
    - Row 3: price on left, review score on right — both in PP Neue Montreal,
      `font-size: sm (14px)`. Price: `color.brand.primary`. Review score: 
      `color.neutral.600`, preceded by a thin star glyph (14px, same color).
  - Far right: a right-facing chevron (16×16px, `color.neutral.400`) — the tap affordance.
  - Card tap area: full row. Deep links to retailer.

- Cards are sorted by default: best match first (AI relevance score, not price).
  Rationale: price-ascending default would prioritize cheapest, which is not our
  aesthetic. Match quality first; user can reorder.

- Minimum 3, maximum 5 cards shown per garment per US-010 (3-5 matching products).

**Affiliate disclosure**: a single line of text pinned above the bottom safe area,
persistent while the results panel is open. Fixed, does not scroll with cards.
Content: "Some links are affiliate links. Tapping may earn Atelier a commission." —
PP Neue Montreal, `font-size: xs (12px)`, `color.neutral.400 (#7a7570)`, centered.
`background: color.surface.card (#fbfaf7)`, 8px top padding.
See State 13 for full affiliate surface spec.

**Accessibility**:
- Garment label: `role="heading" aria-level="1"`.
- Product cards: each card is a link element with `aria-label="[Retailer] — [Product
  name] — [Price] — [N] stars — Opens retailer"`.
- Match count: `aria-live="polite"` — announced when sort/filter changes result count.
- Affiliate disclosure: `role="note"`, always present in DOM even if scrolled past.

---

## State 8: Results — secondary states

### 8a: Multiple garments detected — switching between them

**Garment selector** (in photo plane, overlapping vignette):
- A horizontal row of numbered pills. Each pill: 32×32px, `border-radius: full`.
- Active pill: `background: color.brand.accent (#c85a3c)`. Number in white `#f6f3ed`.
  PP Neue Montreal, `font-size: xs (12px)`, `font-weight: 400`.
- Inactive pill: `background: transparent`. Number in `color.neutral.400`.
  `border: 1px solid color.neutral.400 (at 60% opacity)`.
- Tap a pill: switches active garment, updates garment marker highlight, updates the
  display serif label and product cards below.
- Scroll behavior: pills are horizontally scrollable if >5 garments detected. In
  practice, we cap the display at 5 (AI returns top-5 most prominent garments).
- Left edge: 16px from screen left.
- Touch targets: 44×44px minimum — the pill is 32px visually, but tap region is 44px.

### 8b: Product card expanded / deep view

**Trigger**: tap the chevron on a product card.

**Presentation**: a bottom sheet rises (not a full-screen push). Sheet height: 70% of
viewport. The photo plane + garment selector remain visible above the sheet.

**Sheet contents** (top to bottom):
- Drag handle (4px × 36px, centered, 12px top margin).
- Product image: full-width, 200px tall, object-fit: cover. No border-radius.
- Product name: PP Editorial New, `font-size: xl (22px)`, `font-weight: 400`,
  `color.brand.primary`, 16px horizontal margin.
- Retailer + price row (8px below name): retailer in `font-size: sm`, `color.neutral.400`
  uppercase; price in `font-size: xl (22px)`, `color.brand.primary`. Same horizontal
  margin.
- Review score (4px below price): "Rated 4.2 by 318 customers" in `font-size: sm`,
  `color.neutral.600`.
- Affiliate disclosure: same `font-size: xs` text, `color.neutral.400`, 8px below review.
- CTA: full-width "View at [Retailer]" button — same form as the Scan confirm button
  (State 5): `background: color.brand.primary`, `color: #f6f3ed`, 56px tall, no border
  radius, PP Neue Montreal, `font-size: base`, `letter-spacing: editorial`. Deep links
  to retailer. 16px horizontal margin (so it does not bleed to edges).
- Save actions: below CTA, 12px gap. Two stacked text-only links, 8px gap between them:
  - Primary text link: "Add to wardrobe" — PP Neue Montreal, `font-size: sm`,
    `color.brand.primary`. Triggers size picker sheet (see State 8e). Account gate
    applies: if no account, triggers account creation bottom sheet first.
  - Secondary text link: "Save to wishlist" — PP Neue Montreal, `font-size: sm`,
    `color.neutral.600`. See State 8d for wishlist save behavior.

### 8c: Sort / filter interaction

**Sort**: a bottom sheet with 3 options (no radio buttons — each is a tappable full-row
option):
- "Best match" (default — editorial relevance)
- "Price: low to high"
- "Price: high to low"
Active option has a 2px left border in terracotta `#c85a3c`. PP Neue Montreal,
`font-size: base`, `color.brand.primary`. Sheet: 220px tall.

**Filter**: a bottom sheet with two filter groups:
- Retailer (multiple select): list of retailers present in results. Each row is a
  toggleable option — tapping adds/removes a checkmark (the checkmark is the only icon
  in this view: a 12×12px check in terracotta).
- Price range: a dual-handle range slider. Handles: 24×24px filled circles in
  `color.brand.primary`. Track: `color.neutral.200`. Active track fill:
  `color.brand.accent (#c85a3c)`. Min/max labels in `font-size: xs`,
  `color.neutral.600`.
- Apply button at bottom (same form as primary button). "Show [N] results" — count
  updates live as filters change.

### 8e: "Add to wardrobe" — size picker flow

**Trigger**: user taps "Add to wardrobe" from the expanded product sheet (State 8b).
Account gate applies first: if no account exists, the account creation bottom sheet
appears before this sheet (see Beat 5 in the journey map). Once authenticated, the
size picker sheet rises.

**Presentation**: a bottom sheet rises over the expanded product sheet. Sheet height:
auto (content-driven), minimum 280px. `border-radius: lg (8px)` on top corners only.
Background: `color.surface.card (#fbfaf7)`.

**Sheet contents** (top to bottom):
- Drag handle (4px × 36px, `color.neutral.200 (#e8e3d7)`, centered, 12px top margin).
- Sheet heading (16px top margin): "What size is this?" — PP Editorial New,
  `font-size: xl (22px)`, `font-weight: 400`, `letter-spacing: tight (-0.02em)`,
  `color.brand.primary`.
- Brand detected (8px below heading, if brand is available from scan): brand name in
  PP Neue Montreal, `font-size: sm (14px)`, `color.neutral.600 (#5a5651)`. Example:
  "Detected brand: Acne Studios". If no brand data, this line is omitted.
- Size options (20px top margin): a horizontally scrollable row of pill options.
  Pill form: `border-radius: full (9999px)`, 36px tall, horizontal padding 16px.
  - Unselected pill: `background: transparent`, `border: 1px solid color.neutral.300`,
    label in PP Neue Montreal, `font-size: sm`, `color.brand.primary`.
  - Selected pill: `background: color.brand.primary (#1a1a1c)`, label in
    `color.brand.secondary (#f6f3ed)`, no border.
  - Size options vary by detected garment category:
    - Tops / outerwear: XS, S, M, L, XL, XXL
    - Bottoms: 28, 30, 32, 34, 36, 38 (waist), or 34, 36, 38, 40 (EU sizing)
    - Shoes: 36, 37, 38, 39, 40, 41, 42, 43, 44, 45 (EU) or 6, 7, 8, 9, 10, 11 (US)
  - Pre-selected state: if the user has previously worn (added to wardrobe) a garment
    from this brand + category combination, the matching size pill is pre-selected on
    sheet open. Pre-selection is a convenience affordance — not locked; user can change.
  - If no matching history: no pre-selection; first tap selects.
- "Enter size manually" (12px below pill row): text link — PP Neue Montreal,
  `font-size: sm (14px)`, `color.neutral.600`. Tap opens a single-field text input
  (replaces the pill row with a text field, `placeholder: "e.g. 38, XL, 9.5"`). An
  "← Sizes" text link returns to the pill row. Manual entry is for non-standard or
  international sizes not covered by the pill set.
- Primary CTA (24px below pills or text field): "Add to wardrobe" — full-width, 56px
  tall, no border radius (sharp, editorial). `background: color.brand.primary (#1a1a1c)`,
  `color: #f6f3ed`, PP Neue Montreal, `font-size: base (16px)`,
  `letter-spacing: editorial (0.12em)`. Identical form to the Scan confirm button
  (State 5). The button is disabled (50% opacity, not tappable) if no size is selected
  or entered.
- 24px bottom safe area padding.

**On confirm (CTA tap)**:
- Item saved to wardrobe with the selected size recorded against brand + category.
- Visual acknowledgment: "Add to wardrobe" CTA text transitions to "Saved to wardrobe."
  with a thin underline (1px, 20px wide, terracotta `#c85a3c`) — the same visual
  language as the wishlist save confirmation (State 8d). Holds for 800ms.
- Sheet closes automatically after 800ms.
- The product card in the results list gains a faint terracotta left-border (2px,
  `#c85a3c` at 40% opacity) — same as wishlist saved state, signaling persistence.

**Haptic**: one soft impact haptic on save confirmation (matching State 8d).

**Accessibility**:
- Sheet announced via `aria-live="polite"`: "Size picker. Select the size for this
  garment before adding to wardrobe."
- Pill row: `role="radiogroup"`, each pill is `role="radio"` with `aria-checked`.
- Pre-selected pill: `aria-checked="true"` on open.
- CTA disabled state: `aria-disabled="true"`, screen reader announces "Add to wardrobe,
  select a size first."
- Touch targets: pills are 36px tall — below 44px minimum. Invisible vertical padding
  of 4px top + 4px bottom applied to each pill wrapper to reach 44px. Visual size
  unchanged.

---

### 8d: Saving a product to wishlist — the gesture

**Trigger**: "Save to wishlist" tap from expanded product sheet (State 8b).

**Behavior**: no confirmation dialog. The text changes immediately:
- "Save to wishlist" → "Saved" with a thin underline beneath (1px, 20px wide,
  terracotta `#c85a3c`) — the same underline form as the garment marker. The save is
  acknowledged in the same visual language as the detection. This is intentional.
- After 800ms: the sheet closes automatically. The product card in the results list
  gains a faint terracotta left-border (2px, `#c85a3c` at 40% opacity) indicating it
  is saved. This persists for the session.

**Haptic**: one soft impact haptic on "Saved" state confirm (see motion spec).

---

## State 9: No match found

**When**: AI detected 0 garments, or detected garments but found 0 product matches.

**Layout**: the photo stays full-bleed (no compression to 55% — there are no product
cards to show). The dark overlay (`rgba(26,26,28,0.72)`) covers the lower 50% of the
photo.

**Content in the overlay area** (centered vertically in bottom 50%):

- Primary text: PP Editorial New, `font-size: 2xl (28px)`, `font-weight: 400`,
  `letter-spacing: tight`, `color: #f6f3ed`. Left-aligned, 24px left margin.
  "Nothing found."

- Secondary text (8px below): PP Neue Montreal, `font-size: sm (14px)`,
  `color.neutral.200 (#e8e3d7)` at 80% opacity, left-aligned, 24px left margin.
  "Try a photo with better lighting, or where the garment is clearly visible."

- Two options (24px below secondary text), stacked:
  - "Try another photo" — same text-button form (no background, `#f6f3ed`, `font-size:
    base`, 56px tap area). Returns to State 2.
  - "Search manually" — `font-size: sm`, `color.neutral.400` — deferred to v2 (this
    option is omitted from MVP). Not shown.

**What we do not show**: an error illustration, a sad-face icon, or any decoration.
The photo remains the whole screen. The words sit on it, editorial — like a caption
over a photograph that didn't come out.

**Accessibility**: overlay region has `role="alert"`. "Nothing found" is announced
immediately. Both options have 56px touch targets.

---

## State 10: Low-confidence partial match

**Decision**: this state is distinct from no-match and should be treated differently.

**Rationale**: A low-confidence match exists but we are not confident the AI found the
right garment category. The user has something to look at, but they should be calibrated
before browsing. Treating it identically to a confident match would erode trust when
the results are off.

**Visual treatment**: identical to the confident results state (State 7) with one
addition:

- Below the display serif garment label, before the match count, a single line:
  "Approximate match — results may vary." — PP Neue Montreal, `font-size: xs (12px)`,
  `color.neutral.400 (#7a7570)`, `letter-spacing: editorial (0.12em)`. Left-aligned.
  No icon. No warning color (warning yellow would feel alarming; this is a
  calibration note, not an error).

- The same 3-5 cards are shown. The "best match" sort order still applies.

**Threshold for showing this state**: determined by the AI confidence score from the
backend. Proposed threshold: confidence < 0.65 triggers this state. Exact threshold to
be determined by SPIKE-001 results. Flag for tech: the API response must include a
`confidence` field per detected garment.

---

## State 11: Error states

### 11a: No internet connection
**When**: user taps Scan but device is offline.

The bottom chooser sheet (State 2) does not open. Instead, a small inline notification
appears above the scan button (home screen) or inline near the scan trigger (other
surfaces). Form: a pill-shaped container, `background: color.brand.primary`,
`color: #f6f3ed`, `font-size: xs`, `border-radius: full (9999px)`, max-width 280px,
centered horizontally. Text: "No connection. Scan requires internet." Auto-dismisses
after 4s. `aria-live="assertive"`.

### 11b: Server error (5xx)
**When**: scan request fails after photo upload.

The photo remains full-bleed (same as State 9 layout). Overlay on bottom 50%.
Primary text: "Something went wrong." (PP Editorial New, `2xl`, `#f6f3ed`).
Secondary: "The scan failed. Please try again." (PP Neue Montreal, `sm`, `e8e3d7`).
Options: "Try again" (retries the scan with the same photo), "Dismiss".

### 11c: Rate-limited
**When**: user has exceeded 10 scans in the current day (rate limit confirmed: 10 scans/day).
Same layout as 11b. Primary text: "You've scanned 10 times today." (PP Editorial New,
`2xl`, `#f6f3ed`). Secondary text: "Come back tomorrow for more." (PP Neue Montreal,
`sm`, `#e8e3d7`). No upsell copy in MVP — monetization path deferred to v2.

### 11d: Photo rejected (corrupt, not a garment photo)
**When**: AI returns a "no garment detected" confidence because the image is not a
fashion photo (e.g., landscape, document).

Use State 9 (No match found) with modified secondary text:
"This doesn't look like a fashion photo. Try a photo of clothing or an outfit."

### General error accessibility
All error states announce via `aria-live="assertive"`. Retry buttons have 56px touch
targets and descriptive labels ("Retry scan", "Dismiss error").

---

## State 12: Empty state — first scan

**When**: user opens scan for the first time, no scan history exists.

**Trigger point**: this applies to the entry point on the home screen before any scan
has been completed.

**Treatment** (on the home/wardrobe screen, not inside the scan flow itself):
- Above the persistent scan button (bottom-right), a text block appears:
  12px above the button. Max-width: 200px. Right-aligned (matching button position).
  Text line 1: "Scan anything." — PP Editorial New, `font-size: xl (22px)`,
  `font-weight: 400`, `color.brand.primary`.
  Text line 2 (4px below): "A photo, a screenshot, an inspiration image." — PP Neue
  Montreal, `font-size: sm (14px)`, `color.neutral.600`.
- This text dismisses on first scan completion (or on explicit dismiss via a tap).
- No illustration. No onboarding modal. The product explains itself.

**Rationale**: consistent with the project anti-pattern of no onboarding tour. The copy
does the work. The proximity to the button creates immediate context.

---

## State 13: Affiliate disclosure surface

**FTC compliance requirement**: affiliate links must be clearly and conspicuously
disclosed. "Conspicuous" means visible without scrolling, in a readable size, near the
links it applies to.

**Design decision**: one persistent disclosure per results session, pinned at the bottom
of the product panel (not repeated per card, not on a separate "legal info" screen).
This satisfies FTC guidance (conspicuous, near the links) without visual pollution of
every card.

**Form**:
- Fixed to the bottom of the screen while the results panel (State 7) is open.
- Height: 32px (including 8px top padding).
- Background: `color.surface.card (#fbfaf7)` with a 1px top border in
  `color.neutral.200 (#e8e3d7)`.
- Text: "Some links earn Atelier a commission." — PP Neue Montreal, `font-size: xs
  (12px)`, `color.neutral.400 (#7a7570)`, centered.
- Tapping the disclosure text opens an inline info sheet (swipes up 120px) with
  expanded text: "When you tap a product and make a purchase, Atelier may earn a small
  commission at no extra cost to you. This doesn't influence which products we show."
  — PP Neue Montreal, `font-size: sm`, `color.neutral.600`, 24px horizontal padding.
- The info sheet dismisses on tap-outside or swipe-down.

**Accessibility**:
- Disclosure has `role="note"` in the DOM at all times while results are visible.
- Screen reader: the disclosure is announced after the last product card when navigating
  sequentially by touch.
- The disclosure's info sheet has `aria-label="Affiliate disclosure"`.

---

## New components to add to design_system/components.yaml

The following components are introduced by this spec and should be registered. This
list is a hand-off to the design system — do not implement in this pass.

1. **ScanButton** — Circular fixed-position trigger. Variants: `home`, `contextual`.
   States: `default`, `long-press-revealed`, `pressed`.

2. **ScanChooserSheet** — Bottom sheet with camera / library options. States: `default`,
   `loading` (after option selected). No variants at MVP.

3. **GarmentMarker** — Numbered underline marker overlaid on a photo. Tokens: accent
   color underline, xs number label. States: `active`, `inactive`, `appearing`
   (animation state). Variants: none (all markers are identical in form; position is
   computed).

4. **GarmentSelector** — Horizontal row of numbered pills for switching between detected
   garments in results. States: `active`, `inactive`. Scroll behavior: horizontal
   when >3 pills.

5. **ProductCard** — Scan result item. Contains: product image (64×64px), retailer
   label, description (2-line max), price, review score, tap chevron. States: `default`,
   `saved` (terracotta left border), `pressed`.

6. **AffiliateDisclosure** — Fixed-bottom single-line persistent notice with expandable
   sheet. States: `collapsed` (default), `expanded`.

7. **ScanConfirmButton** — Full-width sharp-cornered text button used in State 5 and
   product deep-view CTA (State 8b). Variants: `primary` (dark background), `ghost`
   (text only). This may generalize to a broader button component later.

8. **GrainOverlay** — Photographic grain texture layer component used during scan
   ceremony. Takes any photo surface and applies the grain at 8% opacity. Used by scan
   flow only. States: `active` (during scan), `inactive` (removed in results).

---

## Responsive notes

The scan moment is primarily a mobile (375px) experience. The spec above assumes a
375px viewport.

**Tablet (768px)**:
- Photo plane in results: top 50% (photo is wider; it needs less vertical space
  proportionally).
- Product panel: max-width 560px, centered with auto horizontal margins.
- Garment cards: still single-column within that max-width.

**Desktop (1280px)**:
- Not a priority for MVP (mobile-first for app). If a web version is built later,
  the results layout would use a side-by-side: photo left (55% width), product panel
  right (45% width). To be designed separately.
