# Mockup Spec: Onboarding Flow
**Atelier — First launch to first value**
Design agent — 2026-04-16

All token references are from `design_system/tokens.yaml` v0.1.0 unless marked [NEW TOKEN].
Component references: existing scan-moment components are reused wherever they apply.
New components flagged at the end.

Status legend per screen:
- [BLOCKING] — user cannot proceed without completing this
- [SKIPPABLE] — user can bypass entirely without losing the thread
- [OPTIONAL-INVITED] — offered, easy to accept, easy to decline

---

## Screen 0: Cold launch — the first breath

**Status**: [BLOCKING — automatic, no user action]

### What this moment is

Not a loading screen. Not a splash screen in the "please wait while assets load" sense.
This is the app's opening sentence. It runs for approximately 1.5s while the app
initializes. The design must make those 1.5s intentional, not apologetic.

### Layout

- Background: `color.surface.background (#f6f3ed)` — full screen, warm off-white.
- Centered vertically and horizontally: the wordmark "Atelier" in PP Editorial New,
  `font-size: 4xl (52px)`, `font-weight: 400`, `letter-spacing: tight (-0.02em)`,
  `color.brand.primary (#1a1a1c)`.
- Nothing else on screen. No tagline, no illustration, no animation loops, no version
  number, no gradient.

### Motion

- On mount: wordmark fades in, `opacity 0→1`, duration `slow (600ms)`,
  `easing: entrance`. Starts immediately on app open (no deliberate delay — the fade-in
  is the hold).
- On advance: wordmark fades out, `opacity 1→0`, duration `normal (400ms)`,
  `easing: exit`. Runs simultaneously with the arrival of Screen 1.
- Reduced motion: wordmark appears at full opacity instantly. No transition. Holds 1.5s.
  Then advances without animation.

### Rationale

The first breath earns trust before any feature or ask. A single word, a single font,
a warm background. The user already knows this is not a generic app. The restraint is
the message. Any addition — tagline, illustration, progress bar — would dilute it.

### Accessibility

- Screen reader: `aria-label="Atelier"` on the wordmark.
- Wordmark text meets contrast: `#1a1a1c` on `#f6f3ed` = 16.7:1 (pass AA, pass AAA).
- No interactive elements. No focus state needed.
- Duration capped at 1.5s — does not require a skip affordance (it is not a "skip
  intro" situation; 1.5s is within acceptable splash range).

---

## Screen 1: Age gate

**Status**: [BLOCKING — legal requirement; cannot be skipped or softened into optionality]

### Purpose and sequencing rationale

Age gate comes first — before the offering, before any engagement — because the under-18
exit must happen before the user has invested any time or formed any attachment to the
product. Asking after the first scan ("by the way, how old are you?") would be
manipulative. The gate is respectful precisely because it is early.

It is designed to feel like a knowing moment between adults, not a legal checkbox. The
user who is 25 years old and enters their birth year does not need to be apologized to.
The design does not apologize.

### Layout

- Background: `color.surface.background (#f6f3ed)`.
- Top region (top 40% of screen): text block, left-aligned, `padding-left: spacing.8
  (32px)`, `padding-top: spacing.20 (80px)`.
  - Heading: "One thing first." — PP Editorial New, `font-size: 3xl (36px)`,
    `font-weight: 400`, `letter-spacing: tight (-0.02em)`, `line-height: tight (1.1)`,
    `color.brand.primary`.
  - Sub-copy (8px below heading): "Atelier is for adults." — PP Neue Montreal,
    `font-size: base (16px)`, `font-weight: 400`, `line-height: relaxed (1.7)`,
    `color.neutral.600 (#5a5651)`.

- Input region (top 60%, below heading block):
  - Label (above input): "Your birth year" — PP Neue Montreal, `font-size: sm (14px)`,
    `letter-spacing: editorial (0.12em)`, `color.neutral.600`, left-aligned,
    `padding-left: 32px`.
  - Input field: full-width minus 32px each side. Height 56px. `border-radius: none`
    (sharp, editorial). Border: `1px solid color.neutral.200 (#e8e3d7)`.
    Background: `color.surface.card (#fbfaf7)`.
    Text inside (on entry): PP Neue Montreal, `font-size: xl (22px)`, `font-weight: 400`,
    `color.brand.primary`. Placeholder: "YYYY" — `color.neutral.400 (#a09b90)`.
    Keyboard type: numeric. `autocomplete="bday-year"`.
  - No "confirm" button shown until 4 digits are entered. On 4th digit entered:
    a right-facing chevron appears inside the right edge of the input field,
    `color.brand.primary`, 24×24px. Tapping it (or pressing Return on keyboard) confirms.
    The chevron replaces typing as confirmation, removing the need for a separate button
    on a screen that should be as spare as possible.

- Confirmation behavior:
  - If age ≥ 18: fade to Screen 2 (the offering).
  - If age < 18: input is replaced by a single quiet message. No animation, no fanfare.
    "Atelier is for adults 18 and over." — PP Neue Montreal, `font-size: base`,
    `color.neutral.600`, left-aligned, 32px left padding. The chevron disappears.
    No "try again" affordance — the gate is final. The back of the input remains
    visible but non-interactive. App goes quiet. (Design note: we do not store age
    data for failed age gates; the session data is discarded.)

### What we do NOT show

- No "By proceeding you agree to our Terms of Service" footnote on this screen.
  Terms and privacy are handled at account creation (Beat 5), not at the age gate.
  The age gate is a safety check, not a consent collection point.
- No birth date picker (day/month/year wheels). A year is enough to determine ≥18.
  The day/month would add friction for no legal gain.

### Accessibility

- Input has a visible label: "Your birth year" (text node, not placeholder-only).
- `aria-label="Birth year"`, `aria-required="true"` on the input.
- Screen reader: announces "One thing first. Atelier is for adults. Birth year, required.
  Edit text."
- The chevron is `aria-label="Confirm age"`, appears when 4 digits are entered.
- Touch target for chevron inside input: 44px (the input height is 56px; the chevron
  tap region is the right 44px of the field).
- Under-18 message: `role="alert"` so screen readers announce immediately.
- Error contrast: under-18 message uses `color.neutral.600` on `#f6f3ed` = 7.4:1 (pass).

---

## Screen 2: The offering

**Status**: [OPTIONAL-INVITED — "Start with my wardrobe" is always reachable; scan path is the invited primary]

### Purpose

This is the first screen that speaks as a product. It does not welcome the user ("Welcome
to Atelier"). It does not list features. It makes a single declarative claim and invites
the user to prove it or build toward it. The copy carries the entire weight.

This screen replaces what a traditional onboarding carousel would do — but it does it
in one breath, not five slides.

### Layout

- Background: `color.surface.background (#f6f3ed)`.
- Top region (spanning top 55% of screen):
  - `padding-top: spacing.24 (96px)` — generous breathing room. The eye needs space
    before the statement lands.
  - `padding-left: spacing.8 (32px)`, `padding-right: spacing.8 (32px)`.
  - Headline (left-aligned): "Your clothes, finally seen." — PP Editorial New,
    `font-size: 4xl (52px)`, `font-weight: 400`, `letter-spacing: tight (-0.02em)`,
    `line-height: tight (1.1)`, `color.brand.primary`.
  - Sub-copy (24px below headline): "Scan anything. Build your wardrobe. Curate looks." —
    PP Neue Montreal, `font-size: base (16px)`, `font-weight: 400`,
    `line-height: normal (1.5)`, `color.neutral.600 (#5a5651)`. Left-aligned.

- Action region (bottom 45% of screen):
  - Primary action surface:
    - Full-width, height 80px (intentionally taller than a normal button — it is a
      surface you enter, not a button you press). No border radius (sharp corners).
      `margin-horizontal: 0` (bleeds to screen edges). `border-top: 1px solid
      color.neutral.200`. Background: `color.brand.primary (#1a1a1c)`.
    - Left-aligned text (24px from left): "Scan a photo now" — PP Editorial New,
      `font-size: xl (22px)`, `font-weight: 400`, `letter-spacing: tight`,
      `color.brand.secondary (#f6f3ed)`.
    - Sub-label below (4px gap): "Point at anything with clothes" — PP Neue Montreal,
      `font-size: sm (14px)`, `color.neutral.400 (#a09b90)`.
    - Right edge: a right-facing arrow glyph (20×20px, `stroke: 1.5px`,
      `color: #f6f3ed` at 60% opacity), centered vertically within the surface.
      24px from right edge.
    - Tap: triggers ScanChooserSheet (same as all other scan entry points).

  - Secondary path (below primary surface, 24px top margin):
    - Left-aligned text (32px from left): "Start with my wardrobe" — PP Neue Montreal,
      `font-size: base (16px)`, `color.neutral.600`.
    - A thin 1px underline beneath the text, `color.neutral.200`, same width as text.
      This is not a button. It is a text link styled as editorial annotation.
    - Touch target: the full-width row, 44px tall (invisible extension above/below
      the text line).
    - Tap: advances to Screen 6 (wardrobe import offering).

  - Very bottom (spacing.8 = 32px above bottom safe area):
    - "Already have an account?" — PP Neue Montreal, `font-size: sm (14px)`,
      `color.neutral.400`, centered.
    - "Sign in" — same text, but with terracotta `#c85a3c` color (the only use of
      accent color on this screen). Tap: opens auth flow directly.

### What we do NOT show

- No "Get started" button. "Get started" is a placeholder. It says nothing.
- No feature illustrations, screenshots of the app UI, or carousel dots.
- No "Skip" affordance (there is nothing to skip yet; the offering is not mandatory
  — it is just the entry point to something).

### Motion

- Screen arrives via a simple fade-in: `opacity 0→1`, `normal (400ms)`, `ease-entrance`.
- Headline animates first, sub-copy staggered 80ms after, primary surface 80ms after
  that. Three-beat stagger total. Feels like the app composing itself before the user.
- Primary surface: on hover/press, background lightens very slightly to `#2a2a2e`
  (barely perceptible, not a dramatic hover state). Duration: `fast (200ms)`.
- Reduced motion: all arrive simultaneously at full opacity. No stagger.

### Accessibility

- Headline contrast: `#1a1a1c` on `#f6f3ed` = 16.7:1 (pass).
- Sub-copy contrast: `color.neutral.600 (#5a5651)` on `#f6f3ed` = 7.4:1 (pass).
- Sub-label contrast: `color.neutral.400 (#a09b90)` on `#1a1a1c` = approximately
  5.7:1 (pass AA for small text ≥4.5:1 required at 14px weight 400).
  — This passes because the background is the dark primary surface, not the light card.
  Verify: `#a09b90` on `#1a1a1c` = 5.7:1. Pass.
- Primary surface touch target: 80px tall — exceeds 44px minimum.
- "Start with my wardrobe" touch target: 44px tall — meets minimum.
- Screen reader order: headline → sub-copy → "Scan a photo now, button" → "Start with
  my wardrobe, link" → "Already have an account? Sign in, link."
- Primary surface: `role="button"`, `aria-label="Scan a photo now — point at anything
  with clothes"`.
- Secondary link: `aria-label="Start with my wardrobe"`.

---

## Screen 3: Permission asks

**Status**: [BLOCKING for their respective paths — camera for scan/photo; not blocking overall onboarding]

### Philosophy

Permissions are asked in context, not pre-emptively at launch. The user is never shown
a system dialog without first understanding why. The design follows Apple HIG and
Google best practices: custom rationale screen → system dialog.

### 3a: Camera permission (triggered on first tap of "Scan a photo now" → Camera)

**Custom rationale (pre-system-dialog screen)**:
- Appears as a bottom sheet (320px tall, `border-radius: lg (8px)` on top corners,
  background `color.surface.card (#fbfaf7)`).
- Drag handle (4px × 36px, `color.neutral.200`, centered, 12px top margin).
- Heading (16px top margin): "Use your camera" — PP Editorial New, `font-size: xl (22px)`,
  `font-weight: 400`, `color.brand.primary`.
- Body (12px below heading): "Atelier needs your camera to take photos for scanning
  and adding clothes to your wardrobe." — PP Neue Montreal, `font-size: base (16px)`,
  `line-height: relaxed (1.7)`, `color.neutral.600`.
- Primary button (24px below body): full-width, 56px, sharp corners, `background:
  color.brand.primary`, text `#f6f3ed`, PP Neue Montreal `font-size: base`,
  `letter-spacing: editorial`. Copy: "Continue"
  — tapping fires the system camera permission dialog.
- Secondary (12px below primary): text-only link centered: "Not now" — `font-size: sm`,
  `color.neutral.400`. Dismisses sheet. Routes to photo library option instead.
- 24px bottom safe area.

**After system dialog — if denied**:
The ScanChooserSheet camera option is replaced with:
"Camera access is off." — PP Neue Montreal `sm`, `color.neutral.600`.
"Open Settings" — terracotta, tappable, deep-links to OS Settings. 44px touch target.

### 3b: Photo library permission (triggered on "Choose from library" or wardrobe import)

**Custom rationale (pre-system-dialog)**:
Same bottom sheet form as 3a.
Heading: "Access your photos"
Body: "Atelier uses your photo library to let you add clothes from existing photos and
scan inspiration images you've saved."
Primary button: "Continue" → fires system photo library permission dialog.
Secondary: "Not now" → dismisses; photo library option grayed out.

**After system dialog — if denied**:
Library option shows:
"Photo access is off."
"Open Settings" in terracotta.

**iOS note on photo library**: on iOS 14+, the native PHPickerViewController requires
no explicit permission for limited selection. Our custom rationale screen still appears
as a pre-explanation, but on iOS 14+ the "Continue" tap opens PHPickerViewController
directly (no system permission dialog). On iOS 13 and earlier (below our iOS 16 floor —
so N/A), a dialog would appear. Since we support iOS 16+, the pre-explanation + picker
flow is sufficient.

### 3c: Notifications permission (NOT asked during onboarding)

**Decision**: notifications permission is not requested during onboarding. It is deferred
until the user has experienced first value and has a reason to want notifications.
The first trigger is: after first wishlist save, a contextual moment: "Get notified when
saved products go on sale?" — bottom sheet, optional. This is out of scope for this
spec (it belongs to US-011 or a future story), but the decision to defer is recorded here.

### Accessibility for permission screens

- Rationale sheet: `role="dialog"`, `aria-labelledby` pointing to heading element.
- Drag handle: `aria-hidden="true"`.
- "Continue" button: 56px tall (pass).
- "Not now": text with 44px minimum touch target via invisible vertical padding.
- If permission denied: "Open Settings" link has `aria-label="Open Settings to enable
  camera access"` (or equivalent).

---

## Screen 4: The scan path (hand-off to scan-moment spec)

**Status**: [SKIPPABLE — user can exit at any point; scan path is the invited primary route]

### The hand-off

When the user proceeds from Screen 2 ("Scan a photo now") through permission handling,
they enter the ScanChooserSheet — the same component spec'd in `specs/scan-moment/
mockup-spec.md` State 2. There is no onboarding-specific wrapper.

This is intentional. The product speaks for itself from this moment. The scan ceremony
(spec'd in its entirety in scan-moment/mockup-spec.md) runs in full:
State 2 (chooser) → State 3 or 4 (camera / library) → State 5 (pre-scan confirm) →
State 6 (ceremony) → State 7 (results).

**Onboarding-specific behavior during first scan**:
One difference from subsequent scans: if the user reaches State 7 (results) during
onboarding (no account exists), the product card deep-link and "Save to wishlist" action
trigger the account gate (Screen 7) rather than executing immediately. The scan results
themselves are fully visible without an account.

**First-scan contextual note** (State 12 treatment from scan-moment spec):
On the home screen before the first scan, the contextual prompt "Scan anything." /
"A photo, a screenshot, an inspiration image." is visible above the scan button. This
is spec'd in scan-moment/mockup-spec.md State 12 and is already part of that spec.
No duplication needed here.

**Error state during first scan**:
If the scan returns no match (State 9) or an error (State 11) during the user's first
scan, the return path is to Screen 2 (the offering) rather than to a generic home screen.
Copy modification: below the "Try another photo" option, a quiet secondary line appears:
"Or start with your wardrobe." — `font-size: sm`, `color.neutral.400`. Tap routes to
Screen 6 (wardrobe import). This ensures the user never hits a dead end on their first
attempt.

---

## Screen 5: The recognition moment — first value landing

**Status**: [OPTIONAL — this "moment" is the scan results state; no separate screen]

### What this is (and is not)

There is no separate screen for "first value achieved." The recognition moment is the
scan results screen (scan-moment/mockup-spec.md State 7) — the display serif label
"Trench coat." and the product cards below it. The first value is delivered by the
product itself, not by a screen that says "You did it!"

**What we explicitly do not do**:
- No confetti, no success overlay, no "Great, you just scanned your first photo!"
- No badge or achievement notification.
- No toast message.

**What the design does instead**:
The editorial weight of the moment is in the typography and the silence. "Trench coat."
in 36px PP Editorial New, followed by product matches, is the celebration. It does not
need annotation.

**The sole onboarding-context addition**: after the user has been on the results screen
for 3+ seconds (they have read the garment label and at least scrolled through one
product card), a very quiet contextual note appears at the top of the screen — not a
banner, not a toast — a single line of type, right-aligned, above the photo plane,
8px below the top safe area:

"Your first find." — PP Neue Montreal, `font-size: xs (12px)`,
`letter-spacing: editorial (0.12em)`, `color.neutral.400`, opacity 0.6. Appears with
a simple fade-in (`normal 400ms`). Disappears after 4 seconds (fade-out `normal 400ms`).
Not interactive. No tap area.

This is the only acknowledgment. It is present and gone. Like a caption on a photograph.

**Accessibility**: `aria-live="polite"` region announces: "Your first find." when the
line appears. `aria-hidden="true"` on the element after it disappears.

**Rationale for this instead of nothing**: purely from a retention perspective, the
first session should contain one moment of felt acknowledgment — not celebration, but
witnessing. "Your first find." is the app noticing, not applauding. It names what happened
without inflating it. The editorial restraint of the phrase matches the register.

---

## Screen 6: Photo-roll import offering — wardrobe path

**Status**: [OPTIONAL-INVITED — "Skip for now" always available; 0 friction to decline]

### Purpose

The photo-roll import is the cold-start mitigation from context.md section 9. The user
may have dozens of clothing photos already on their phone. This screen offers to turn
them into a wardrobe in under a minute.

It is offered, not required. The design must make declining as effortless as accepting.

### Layout

- Background: `color.surface.background (#f6f3ed)`.
- Top region, `padding-top: spacing.20 (80px)`, `padding-horizontal: spacing.8 (32px)`:
  - Heading: "Your wardrobe might already be on your phone." — PP Editorial New,
    `font-size: 2xl (28px)`, `font-weight: 400`, `letter-spacing: tight`,
    `line-height: tight (1.1)`, `color.brand.primary`. Max 2 lines.
  - Sub-copy (16px below heading): "We'll show you photos that look like clothing.
    Pick the ones that belong in your wardrobe." — PP Neue Montreal, `font-size: base`,
    `line-height: relaxed (1.7)`, `color.neutral.600`. Left-aligned.

- Action region:
  - Primary action (48px below sub-copy): full-width, 56px tall, sharp corners,
    `background: color.brand.primary`, text `#f6f3ed`. PP Neue Montreal `base`,
    `letter-spacing: editorial`. Copy: "Browse my photos"
    — triggers photo library permission (Screen 3b), then multi-select view (Screen 6b).

  - Secondary (16px below primary): text-only, centered.
    "Add clothes one by one instead" — PP Neue Montreal `sm`, `color.neutral.600`.
    Tap: opens wardrobe camera (US-001 camera flow).

  - Tertiary — the skip (24px below secondary):
    "Skip for now" — PP Neue Montreal `sm`, `color.neutral.400`. Centered.
    Tap: advances to home screen (Screen 9 — empty wardrobe state).

- Important note: no illustration, no mock photo grid preview, no decorative element.
  The screen is typographically spare. The copy earns the action.

### Accessibility

- Heading contrast: 16.7:1 (pass).
- Sub-copy contrast: 7.4:1 (pass).
- "Skip for now" contrast: `color.neutral.400 (#a09b90)` on `#f6f3ed` = 2.9:1 — this
  FAILS AA for small text (requires 4.5:1 at 14px weight 400).
  **BLOCKER**: "Skip for now" must either increase to 16px+ (large text threshold 3:1) or
  use `color.neutral.600 (#5a5651)` which is 7.4:1. Recommended fix: use `color.neutral.600`
  for skip text. This is the same `neutral.400` blocker identified in the scan-moment spec
  and now inherited here.
- Primary button touch target: 56px (pass).
- "Skip for now" touch target: 44px minimum via invisible vertical padding (pass visually).
- Screen reader: heading → sub-copy → "Browse my photos, button" → "Add clothes one by
  one instead, link" → "Skip for now, link".

---

## Screen 6b: Multi-select photo grid — import

**Status**: [OPTIONAL-INVITED — continues from Screen 6; "Done" with 0 selected is equivalent to skip]

### Layout

- Navigation bar (top, 44px + safe area):
  - Left: close (×) glyph, 24×24px, `color.brand.primary`, `aria-label="Cancel import"`.
  - Centered: "Choose photos" — PP Neue Montreal, `font-size: base`, `color.brand.primary`.
  - Right: "Done" — PP Neue Montreal, `font-size: base`, `color.brand.accent (#c85a3c)`.
    Active when 0 or more photos selected (always tappable — selecting 0 is valid;
    it means "import nothing / skip").

- Selection count (below nav bar, 8px below, left-aligned 16px):
  "0 selected" — updates live as photos are selected. PP Neue Montreal `sm`,
  `color.neutral.600`. Max shown: 10. When 10 are selected, count reads "10 selected
  (maximum)". Photos above 10 cannot be selected — tap shows a brief inline note:
  "Maximum 10 photos. Deselect one to choose another." — `color.neutral.600`, `sm`.

- Photo grid: 3 columns, 2px gaps, square thumbnails. Full-screen below nav.
  Photos sorted by recency (most recent first). On initial load, the grid is
  filtered to show likely clothing photos (heuristic: photos with aspect ratios
  suggesting portrait shots, or if on-device ML is available, clothing classifier).
  Non-clothing photos are not hidden — they are just not the default top of the list.
  A quiet filter label at the top: "Showing likely clothing photos. Scroll to see all."
  — PP Neue Montreal `xs`, `color.neutral.400`. Tap: removes filter, shows all photos.

- Selected state per thumbnail:
  - A small filled circle in the top-right corner of the thumbnail. Circle is 22×22px,
    `background: color.brand.accent (#c85a3c)`. The selection number (1–10) sits inside
    the circle in white `#f6f3ed`, PP Neue Montreal, `font-size: xs`, centered.
    The number indicates the order of selection (and consequently the order items will
    appear in the wardrobe).
  - Selected thumbnail: 2px terracotta border on all edges. No overlay, no darkening —
    the photo remains fully visible.
  - Unselected thumbnail: no border, no overlay.

- Thumbnails: `border-radius: none` (sharp, consistent with grid aesthetic).

- "Done" tap behavior:
  - If 0 selected: equivalent to "Skip for now" — advances to home empty state.
  - If 1-10 selected: triggers import. UI advances to Screen 6c (import in progress).

### Accessibility

- Thumbnails: `role="checkbox"`, `aria-checked="true/false"`,
  `aria-label="Photo from [relative date], [checked/unchecked]"`.
- Selection count: `aria-live="polite"`, announces "[N] photos selected" on each change.
- "Done" button: always enabled (0-selected = skip). `aria-label="Done, [N] photos
  selected"` — updates dynamically.
- Touch targets: thumbnail cells expand to fill the grid cell (minimum 44px square
  at 3-column layout on 375px = 124px — exceeds minimum).
- Keyboard/VoiceOver: navigates grid sequentially. Space bar toggles selection.

---

## Screen 6c: Import in progress

**Status**: [BLOCKING — cannot leave mid-import without canceling; can cancel]

### Layout

- Background: `color.surface.background (#f6f3ed)`.
- Center-aligned content block:
  - Top spacing: 40% from top of screen.
  - Label: "Adding to your wardrobe" — PP Editorial New, `font-size: 2xl (28px)`,
    `font-weight: 400`, `letter-spacing: tight`, `color.brand.primary`.
  - Sub-label (12px below): PP Neue Montreal, `font-size: sm`, `color.neutral.600`.
    Cycles through: "Analyzing garments." / "Sorting by type." / "Almost there."
    Each line appears on a 3s rotation (fade-out old, fade-in new, `normal (400ms)`).
    These are editorial, not technical. They do not claim accuracy ("Detecting trouser
    type"); they claim work ("Analyzing garments.").
  - Quiet cancel (below sub-label, 48px gap): "Cancel import" — PP Neue Montreal `sm`,
    `color.neutral.400`. Tap: cancels import, dismisses to home empty state. Does not
    delete any items that have already been uploaded and processed.

- A subtle horizontal progress indicator: a thin 1px line at the very bottom of the
  screen (touching the bottom safe area). This line fills left-to-right from `0%` to
  `100%` over the import duration. Color: `color.brand.accent (#c85a3c)`.
  Width: full screen width. It is the only motion on screen.
  Why a line rather than a spinner: it is quantified progress, not spinning uncertainty.
  The 1px height keeps it utterly peripheral — it is there if you look, invisible if you
  don't. The import is estimated to complete in 3-15s depending on photo count and network.

- **Offline handling during import**: if connection drops mid-import, the line stops
  animating and a quiet note appears above the cancel link: "Waiting for connection…"
  — `color.neutral.400`, `sm`. Resumes when connection returns.

### Accessibility

- The rotating sub-label has `aria-live="polite"` so screen readers hear each update.
- The progress line: purely visual; screen reader ignores it (`aria-hidden`).
- "Cancel import" touch target: 44px minimum (invisible padding).
- Progress completion: `aria-live="polite"` announces "Wardrobe updated." on completion
  before transition to Screen 6d.

---

## Screen 6d: Import complete

**Status**: [SKIPPABLE — no skip needed; this is an auto-advance transition beat, 2s hold]

### Layout

A brief, quiet acknowledgment before the user lands on the wardrobe grid.
Holds for 2 seconds, then auto-advances to Screen 9 (populated wardrobe state).

- Background: `color.surface.background (#f6f3ed)`.
- Centered vertically:
  - Single line (display serif): "[N] pieces." — PP Editorial New, `font-size: 4xl (52px)`,
    `font-weight: 400`, `letter-spacing: tight`, `color.brand.primary`.
    "[N]" is the actual count of items successfully imported (e.g., "7 pieces.").
    The period is editorial — same language as the garment label in scan results.
  - Sub-line (8px below): "Added to your wardrobe." — PP Neue Montreal, `font-size: base`,
    `color.neutral.600`.

- No button. No animation. No illustration. Two lines of type, full screen, 2 seconds.
  Then transition to wardrobe grid.

- Why: this is the same principle as the detection complete pause in the scan ceremony.
  The brief hold before the result makes the result land with more weight. After the
  progress screen's gentle cycling text, this quiet finality reads as arrived.

### Accessibility

- The "[N] pieces." line has `role="status"`, announced on mount.
- Auto-advance cannot be interrupted by the user (2s is within acceptable range for
  an uninterruptible transition). However: if VoiceOver is active, the screen holds
  until VoiceOver has had time to read both lines (minimum 3s instead of 2s).

---

## Screen 7: Account creation / auth gate

**Status**: [OPTIONAL-INVITED — triggered by save/deeplink action, never proactively blocking onboarding]

### When this screen appears

Not as a step in the onboarding sequence. It surfaces as a bottom sheet when the user
takes any action requiring persistence:
1. Tapping "Save to wishlist" on a product card (scan results)
2. Tapping a deep-link to a retailer (this is arguable — we can allow anonymous
   tap-through; see note below)
3. Re-opening the app after a session with unsaved scan results (a gentle version)

**Note on deep-linking without account**: deep-linking to a retailer's product page does
not require a user account (it is a browser open). Consider allowing this without the
account gate — it lowers friction to the affiliate tap-through, which is a revenue event.
Product-lead should decide. If allowed: only the "Save to wishlist" action gates on account.
This is flagged as an open question.

### Layout (bottom sheet form)

- Sheet height: 380px + bottom safe area.
- `border-radius: lg (8px)` on top corners. Background: `color.surface.card (#fbfaf7)`.
- Drag handle (4px × 36px, `color.neutral.200`, centered, 12px top margin).
- Heading (20px below handle): "Keep what you found." — PP Editorial New,
  `font-size: 2xl (28px)`, `font-weight: 400`, `letter-spacing: tight`,
  `color.brand.primary`. Left-aligned, 24px left padding.
- Body (12px below heading): "Create an account to save this, build your wardrobe, and
  pick up where you left off." — PP Neue Montreal, `font-size: base`, `line-height:
  relaxed`, `color.neutral.600`. 24px horizontal padding.

- Auth options (32px below body):
  - Email option: full-width, 56px, sharp corners, `background: color.brand.primary`,
    text `#f6f3ed`. "Continue with email" — PP Neue Montreal `base` `letter-spacing:
    editorial`.
  - Social options (if implemented — Apple and Google): secondary form, outlined,
    `border: 1px solid color.neutral.200`, `background: transparent`, `color.brand.primary`,
    56px. "Continue with Apple" / "Continue with Google". Note: social auth is subject
    to Apple/Google approval review for apps with in-app purchasing or affiliate links.
    Product-lead to validate policy compliance.
  - Gap between email and social: 12px.

- "Maybe later" (24px below last auth option): text only, centered.
  PP Neue Montreal `sm`, `color.neutral.400`. Tap: dismisses sheet. Scan results
  remain in session. If the triggering action was wishlist save: item not saved,
  but results remain visible.

- Legal footnote (12px above bottom safe area): "By continuing, you agree to our
  Terms of Service and Privacy Policy." — PP Neue Montreal, `font-size: xs (12px)`,
  `color.neutral.400`. Terms of Service and Privacy Policy are tappable links
  in terracotta `#c85a3c`. `font-size: xs` on `#fbfaf7`:

  **Accessibility note — WCAG blocker**:
  `color.neutral.400 (#a09b90)` on `color.surface.card (#fbfaf7)` = approximately
  2.9:1. This FAILS AA for small text at xs (12px, weight 400). Same blocker as
  identified in the scan-moment spec session summary, now re-encountered here.
  **Fix**: use `color.neutral.600 (#5a5651)` for the legal footnote body text
  (7.4:1 on `#fbfaf7`). The terracotta links pass: `#c85a3c` on `#fbfaf7` = 3.7:1 —
  fails AA at xs (12px weight 400), which requires 4.5:1. Options:
  (1) Increase the links to 14px (3:1 threshold for large text at 14px bold — but
  weight 400 is not bold). (2) Bold the links at 14px (makes 3:1 threshold).
  (3) Use `color.brand.primary` for the links instead of terracotta.
  Recommended fix: increase footnote text to `font-size: sm (14px)` bold (weight 500)
  which meets 3:1 threshold for large text. The aesthetic cost is minimal at this size.
  **This is a blocker before handoff to tech.**

- Sheet closes on: drag down, tap outside, or "Maybe later".

### Returning user — sign in path

If user selects "Sign in" from Screen 2, the same sheet appears but with:
- Heading: "Good to have you back." — PP Editorial New, same spec.
- Auth options as above, but labeled "Sign in with email" / "Sign in with Apple" etc.
- "Don't have an account? Create one" text link replacing "Maybe later".

### Accessibility

- Sheet: `role="dialog"`, `aria-labelledby="account-sheet-heading"`.
- Buttons: 56px touch targets (pass).
- "Maybe later": 44px touch target via padding (pass).
- Keyboard: focus is trapped inside the sheet while open. Escape dismisses.

---

## Screen 8: Email / password auth form

**Status**: [BLOCKING once entered — must complete or cancel]

### Layout

Full-screen (not a sheet — email auth is a committed action).

- Back arrow top-left: 44×44px, `color.brand.primary`. Returns to the offering sheet.
- Top spacing: `spacing.16 (64px)`.
- Heading: PP Editorial New, `font-size: 2xl (28px)`, `font-weight: 400`,
  `color.brand.primary`, 32px left margin.
  "Create account." (for new accounts) or "Sign in." (for returning users).

- Form fields (24px below heading):
  - Email field:
    Label: "Email" — PP Neue Montreal `sm`, `letter-spacing: editorial`,
    `color.neutral.600`. Left-aligned, 32px left.
    Input: same form as age gate input (height 56px, sharp corners, `border-radius: none`,
    `border: 1px solid color.neutral.200`, background `color.surface.card`). Keyboard
    type: email. `autocomplete="email"`.
  - Password field (16px below email, for new accounts):
    Label: "Password". Input: same form. Password type (show/hide toggle inside field
    right edge: a 24×24px eye-glyph toggle, `color.neutral.400`. Toggle turns plain-text
    and back.)
    For sign-in only: no "confirm password" field.
  - New accounts only — "Confirm password" field (16px below password). Omitted for
    sign-in.

- Inline error states (per field):
  Below the relevant field, 4px gap. Single-line error in PP Neue Montreal `sm`,
  `color.semantic.danger (#9b3a3a)`. Left-aligned. Examples:
  - "Enter a valid email address."
  - "Password must be at least 8 characters."
  - "That email is already registered. Sign in instead?" with "Sign in" as an
    inline text link in terracotta, opening sign-in variant of this screen.
  Error fields: `border-color: color.semantic.danger`. `aria-invalid="true"`,
  `aria-describedby="[field]-error"`.

- Primary action (32px below last field):
  Full-width, 56px, sharp, `background: color.brand.primary`, `color: #f6f3ed`.
  PP Neue Montreal `base` `letter-spacing: editorial`.
  New account: "Create account" / Sign in: "Sign in".
  Loading state: text replaced by a quiet inline note "Creating your account…" or
  "Signing in…" — same text, but the button is non-interactive. No spinner. The button
  dims slightly (`background: #2a2a2e`). Consistent with the "stillness as confidence"
  aesthetic established in the scan ceremony.

- Forgot password (sign-in only, 12px below primary): text link centered.
  "Forgot password?" — PP Neue Montreal `sm`, `color.neutral.400`.
  Tap: sends a reset email and shows an inline confirmation: "Check your email."

### Accessibility

- All inputs have visible labels (not placeholder-only).
- `autocomplete` attributes on all applicable fields.
- Error messages: specific, useful, associated to fields via `aria-describedby`.
- Touch targets: all controls ≥ 44px.
- `color.semantic.danger (#9b3a3a)` on `#f6f3ed` = approximately 5.8:1 (pass AA).
- "Forgot password" contrast: `color.neutral.400` on `#f6f3ed` = 2.9:1 — FAILS AA.
  Fix: use `color.neutral.600`. Same fix as elsewhere.

---

## Screen 9: Home — empty wardrobe state

**Status**: [SKIPPABLE — this is the base state of the app, not an action]

### The empty state philosophy

The empty wardrobe state is not a "no results" screen. It is the first page of a
blank sketchbook. It should feel like potential, not absence. The editorial approach:
a magazine before the first article is written is still a magazine — the grid is there,
the structure is there, the intent is there.

### Layout (0 items — first visit after onboarding)

- Navigation: standard app navigation (Wardrobe | Looks tabs, or bottom tab bar).
  Tab bar: PP Neue Montreal, `font-size: xs`, `letter-spacing: editorial`.
  Tabs: "Wardrobe", "Looks". Potentially "Home" as landing tab — architecture TBD
  with product-lead.

- Wardrobe tab empty state:
  - The wardrobe grid is present as structure: 2-column grid with `spacing.1 (4px)` gaps
    on `color.surface.background (#f6f3ed)`. But instead of garment thumbnails, the grid
    cells are empty — they are not placeholder cards, they are negative space.
    The grid is drawn by the spacing and the alignment of the headings below,
    not by visible cell borders.

  - Left-aligned text block, positioned at vertical center of screen (adjusted for
    the top and bottom fixed elements), 32px left margin:

    Heading: "Nothing here yet." — PP Editorial New, `font-size: 2xl (28px)`,
    `font-weight: 400`, `letter-spacing: tight`, `color.brand.primary`.

    Sub-copy (12px below heading): "Add a garment to start." — PP Neue Montreal,
    `font-size: base`, `line-height: relaxed`, `color.neutral.600`.

  - The scan button (ScanButton component from scan-moment spec) is visible at
    bottom-right as always. The State 12 contextual prompt from the scan-moment spec
    is present: "Scan anything." / "A photo, a screenshot, an inspiration image."

  - Asymmetric composition: the text block sits at 40% from the top (not centered —
    the empty grid space above carries visual weight, making the text feel grounded
    rather than floating).

### Layout (1-4 items — partial wardrobe)

- The imported items occupy the first cells of the grid (3/4 portrait aspect ratio,
  tight gaps).
- Remaining grid space: empty as above, negative space.
- No "add more" prompt in the grid itself — the FAB camera button (US-001) handles
  this, per acceptance criteria: "Camera button on wardrobe empty state and persistent FAB."
- The editorial quality of a small wardrobe is that it looks intentional: a curated
  selection, not a cluttered dump.

### Layout (5+ items)

- Grid fills with real content. The empty-state text disappears.
- Grid is architectural in its own right (scan-moment spec State 1 entry point from
  wardrobe notes this: "Scan button accessible from wardrobe screen").
- AI auto-tags show on item thumbnails as small text labels (part of US-003 spec —
  separate from this spec).

### Looks tab empty state

- Heading: "No looks yet." — PP Editorial New, `font-size: 2xl`.
- Sub-copy: "Pick garments from your wardrobe to create one." — PP Neue Montreal, `base`,
  `color.neutral.600`.
- No illustration, no sample look. The grid structure is visible.

### Accessibility

- Empty state heading: `role="heading" aria-level="1"`.
- "Nothing here yet" text: screen reader announces it as a heading.
- The empty grid cells: `aria-hidden="true"` (they are visual structure, not content).
- FAB camera button: same accessibility spec as scan-moment spec (56×56px, `aria-label`).

---

## Screen 10: Returning user — second launch

### Behavior

The second launch (account exists) goes directly to the home screen. No splash hold
(the first-breath moment is only for the very first launch — it is an onboarding moment,
not a permanent splash screen).

**Performance target from context.md**: app launch → home in < 2s cold, < 500ms warm.

**The single small acknowledgment**:
Within the first 24 hours since signup, a one-time quiet note at the very top of the
screen (below the navigation bar, above the first content):

"Welcome back." — PP Neue Montreal, `font-size: sm (14px)`, `color.neutral.400`.
Right-aligned, 16px right margin. Fades in `normal (400ms)` on home screen mount.
Fades out after 3s automatically. `aria-live="polite"`, announced once.

Not a banner. Not a notification chip. One line of text, right-aligned, present and gone.
The right-alignment is deliberate: the user's eye is scanning left (where content is);
the acknowledgment is peripheral, noticed without demanding attention.

On subsequent opens (same day, or after 24 hours): nothing. The product is its own
re-engagement.

---

## Screen 11: Onboarding resumption

### Logic

The app tracks onboarding completion state in local storage via a progression flag:
- `age_verified: true/false`
- `first_offering_seen: true/false`
- `onboarding_complete: true/false` (set after first scan result seen OR after wardrobe
  import completes — whichever comes first)

On re-open:
- `age_verified: false` → restart from Screen 1 (age gate).
- `age_verified: true`, `onboarding_complete: false` → restart from Screen 2 (offering).
  No "welcome back" framing. The offering is simply there.
- `onboarding_complete: true` → home screen. Normal returning user path.

There is no "Resume where you left off" UI. The user does not need to be told where
they are in a flow that has no progress bar. The offering screen is simple enough to
re-encounter without confusion.

---

## Screen 12: Error states during onboarding

### Auth failure (Screen 8)

Inline errors per field (specified in Screen 8 above). No full-screen error state.
The form recovers in place.

**Network failure during account creation**: the "Create account" button shows the loading
state (dimmed, no spinner). If the request times out after 10s, the button returns to
active state and a quiet inline note appears below it (not above — the user's eyes are
near the button):
"Something went wrong. Try again." — PP Neue Montreal `sm`, `color.semantic.danger`.
`aria-live="assertive"`.

### No connection on import (Screen 6b / 6c)

Specified in Screen 6c above. Photos upload when connection returns. User is not blocked.

### Camera/library permission denied (Screen 3a / 3b)

Specified in Screen 3 above. Alternative path (library vs camera) remains available.
If both are denied, the only option is "Add manually" (camera) via Settings.
The app is still usable — it just requires the user to fix permissions separately.

### Under-18 gate (Screen 1)

The app shows a single message and does not allow further interaction. This is not an
error state in the UX sense — it is the intended behavior.

---

## New components to add to design_system/components.yaml

These components are introduced by this spec. Do not edit components.yaml yet — this
is the handoff list.

1. **AgeGateInput** — Year input field with built-in confirmation chevron that appears
   on 4-digit entry. Variant: single (no multi-field date picker). States: `default`,
   `filled` (chevron visible), `error` (under-18 message).

2. **OfferingScreen** — Full-screen typographic surface with primary action surface
   (dark panel, left-aligned display serif) and secondary text link. Used for key
   first-impression screens. States: `default`, `pressed` (primary surface).

3. **ImportGrid** — Multi-select photo grid for wardrobe import. Tokens: 3-column,
   2px gaps, square thumbnails. States: `unselected`, `selected` (terracotta border
   + numbered badge), `max-reached` (non-selectable styling).

4. **ImportProgressScreen** — Full-screen import progress state with cycling
   editorial sub-copy and thin bottom progress line. States: `in-progress`, `offline`,
   `complete`.

5. **ImportCompleteBeat** — 2-second auto-advance screen showing "[N] pieces." in
   display serif. States: `default` only (not interactive).

6. **AccountGateSheet** — Bottom sheet for deferred account creation / sign-in.
   Variants: `create-account`, `sign-in`. States: `default`, `loading`.
   Reuses: drag handle pattern from ScanChooserSheet.

7. **EmptyStateGrid** — Wardrobe grid empty state. Negative-space grid with
   left-aligned editorial text block. Variants: `wardrobe-empty`, `looks-empty`.
   States: `0-items`, `1-4-items`.

8. **FirstBreathScreen** — Single-wordmark full-screen moment. Used once at cold
   launch. States: `default`, `fading-out`.

---

## Proposed new tokens

These gaps in tokens.yaml become apparent during onboarding spec. Do not edit
tokens.yaml — list only.

```yaml
# Onboarding-specific timing
effects:
  motion:
    duration:
      beat_hold: "2000ms"        # import complete beat hold (Screen 6d auto-advance)
      first_breath: "1500ms"     # Screen 0 hold duration
      acknowledgment: "3000ms"   # "Your first find." and "Welcome back." hold

# Onboarding progress tracking (not a visual token — a semantic flag)
atelier:
  onboarding:
    age_gate_year_digit_count: 4   # digits before chevron appears
    import_max_photos: 10          # hard cap for photo roll import
    first_breath_duration: "1500ms"
    import_complete_beat_duration: "2000ms"
```

---

## WCAG AA Accessibility Audit Summary

| Screen | Element | Status | Ratio | Fix required |
|---|---|---|---|---|
| Screen 0 | Wordmark on background | PASS | 16.7:1 | None |
| Screen 1 | Heading on background | PASS | 16.7:1 | None |
| Screen 1 | Sub-copy on background | PASS | 7.4:1 | None |
| Screen 2 | Headline on background | PASS | 16.7:1 | None |
| Screen 2 | Sub-copy on background | PASS | 7.4:1 | None |
| Screen 2 | Sub-label on dark surface | PASS | ~5.7:1 | None |
| Screen 2 | Sign-in link (terracotta on bg) | PASS | 3.7:1 (14px+) | Must be 14px+ to use 3:1 threshold |
| Screen 6 | "Skip for now" (neutral.400 on bg) | **FAIL** | 2.9:1 | Use neutral.600 |
| Screen 7 | Legal footnote (neutral.400 on card) | **FAIL** | 2.9:1 | Use neutral.600 + increase to 14px |
| Screen 7 | TOS/PP links (terracotta on card) | **FAIL** | 3.7:1 at xs | Increase to 14px bold |
| Screen 8 | Error text (danger on background) | PASS | ~5.8:1 | None |
| Screen 8 | "Forgot password" (neutral.400 on bg) | **FAIL** | 2.9:1 | Use neutral.600 |
| All screens | Touch targets ≥ 44px | PASS | — | Verified per screen |
| All screens | prefers-reduced-motion | PASS | — | Specified per screen |

**Note**: the `neutral.400 (#a09b90)` on light backgrounds (card `#fbfaf7` and
background `#f6f3ed`) contrast failure is a systemic issue first identified in the
scan-moment spec session. The fix — substituting `neutral.600 (#5a5651)` for all
secondary/tertiary text that is not large and bold — should be applied globally
across both specs before tech handoff. Product-lead: no action needed. Design:
this is a design system token correction, not a redesign.
