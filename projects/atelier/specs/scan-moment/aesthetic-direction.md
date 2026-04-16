# Aesthetic Direction: The Scan Moment
**Atelier — Scan Feature (US-010)**
Design agent — 2026-04-16

---

## What is this moment, emotionally?

The scan is a moment of recognition — the feeling of a conservator in a quiet archive
who places an unknown photograph under glass and waits for the light to reveal what is
there. Quiet authority. Not magic-trick delight. Not shopping-cart urgency. The word is
**recognition**: the app does not invent, it reveals what was already in the image.

This is deliberately different from the overall "editorial maximalism × studio minimalism"
tone, which governs the whole app. For the scan moment, we narrow to a sub-register:
**studio reverence**. The UI steps back. The photograph becomes an artifact. The
identification is the finding of something real.

---

## What we are rejecting

These are the anti-patterns that would make this look like every other app. Do not
introduce any of the following:

- **Google Lens reticle**: blue squares auto-detecting objects. Feels like
  developer tooling. No reticles, crosshairs, or bounding boxes.
- **Shopping-app price tags**: bright callout bubbles, bolded "€49" in a pin stuck to
  the garment mid-scan. The price is not the discovery — the garment is.
- **Spinning loaders or progress bars with percentages**: "Analyzing... 67%". This
  destroys ceremony. Progress is communicated through the reveal itself, not a meter.
- **Instagram shop tags**: the pin-with-arrow overlaid on a social post. Consumer-grade.
- **AR try-on vibe**: real-time overlay, gamified feel. Not what this is.
- **Sci-fi scan lines as a cliché**: horizontal sweep lines, glowing grids, neon halos.
  These read as "we saw this in a movie." They are references to science fiction, not
  fashion.
- **Haptic-heavy celebration**: no success fanfare, no confetti, no "match found!" pulse.
  Recognition is quiet. The result speaks.

---

## Visual metaphor: the contact sheet

The primary metaphor is **the darkroom contact sheet** — a grid of photographic
exposures, each one emerging from chemical development at its own pace. In a darkroom,
you do not watch a loading spinner; you watch the image arrive out of darkness.

The secondary metaphor is the **atelier pinboard**: a sample pinned to a backing sheet
with a small, precise paper label. Garment markers in this UI are not pins stuck in a
map — they are typographic calls-out in the margin, the way a pattern maker annotates
a photograph before cutting.

Together these two metaphors govern:
- The photo treatment during scan (coming out of darkness, not dissolving away)
- The marker form (margin-note typography, not pins or reticles)
- The product card reveal (emerging into view, not sliding in as commerce)
- The overall pace (development takes as long as it takes — but it is never anxious)

---

## Typography in this moment

The scan moment uses only two moments of display type — both earned, neither decorative.

**Display serif (PP Editorial New)**:
- Single use: the word or phrase that names what was found. When garment detection
  completes, the primary identified garment category appears in display serif beneath
  the photo, large, left-aligned — `font-family: display`, `font-size: 3xl (36px)`,
  `font-weight: 400`, `letter-spacing: tight (-0.02em)`, `line-height: tight (1.1)`.
  For example: "Trench coat." Period included. Like a caption in a fashion archive.
- This appears once, for the active/selected garment. It does not multiply per garment.

**Body sans (PP Neue Montreal)**:
- All secondary information: retailer name, price, number of results, filter labels,
  affiliate disclosure.
- The micro-caption beneath each garment marker (the number label).
- `font-size: sm (14px)`, `font-weight: 400`, `letter-spacing: editorial (0.12em)` for
  labels and category tags — this is the "margin note" voice.
- `font-size: xs (12px)` for affiliate disclosure and metadata.

**What is explicitly absent**: no bold weights in this moment. Weight = urgency. We have
no urgency here.

---

## Color usage during and after scan

**During scan (photo processing active)**:
- The photo is full-bleed. The surrounding UI drops to near-invisible.
- Background: `color.brand.primary (#1a1a1c)` — the UI shell goes dark, not the photo.
  The photo stays at full saturation and brightness.
- No UI chrome in the foreground during scanning. The scan button has already been used;
  it disappears. No navigation bar is visible.
- The single accent color (`color.brand.accent: #c85a3c`, terracotta) is held back
  entirely during scanning. It arrives only with the garment markers — as the label
  number associated with each detected garment. This is its singular, deliberate
  appearance. It signals: "this is what was found."

**After scan (results state)**:
- The photo shrinks to the top ~55% of screen and receives a subtle desaturation (10%
  toward grayscale, not full gray) and a thin vignette on the bottom edge only. This
  is the signal that the photo has been "read" and analysis is complete. It also
  separates the photo plane from the product card plane below without a visible divider.
- The product cards surface on `color.surface.card (#fbfaf7)`.
- The accent color (#c85a3c) appears on the active garment marker and on the active
  garment selector tab (if multiple garments). Inactive markers and tabs revert to
  `color.neutral.400 (#a09b90)`.
- Prices: `color.brand.primary (#1a1a1c)`, same weight as any other body text. No color
  emphasis on price. It is information, not a call to action.

---

## Contrast and hierarchy

The hierarchy rule for this moment has two phases:

**Phase 1 — scanning**: Photo is absolute hero. Everything else is either invisible or
peripheral. The photo occupies 100% of the viewport. No competing elements.

**Phase 2 — results**: Two planes exist in hierarchy.
- Plane A (top, 55%): the photo — reduced saturation, vignette, with garment markers.
  This is the reference plane. The user looks here to understand what was found.
- Plane B (bottom, 45%+): product cards — full brightness, card surface, high contrast.
  This is the action plane.
- The planes are separated by distance (the photo compresses upward when cards arrive),
  not by a rule or divider line. No hairlines. No "shelf" between photo and cards.

Product cards must not compete with the photo in the results state. They have lower
visual weight: no drop shadows as decoration, image is square at left edge of card,
text is compact.

---

## Photography treatment during scan

During the scan (while AI is processing):
- The photo is shown full-bleed at 100% saturation and brightness.
- A subtle photographic grain texture is layered over the image at ~8% opacity using a
  grain asset (not CSS noise — use a 256×256 seamless grain PNG, tiled, blended at
  multiply). This evokes darkroom paper. It does not simulate loading; it is a material
  presence.
- No desaturation during active scan. The desaturation comes AFTER — as a "developed"
  state signal.

During the garment detection reveal (markers appearing progressively):
- Each garment region receives a brief, very subtle luminance lift (~+6% brightness on
  the region only), as if light is catching that part of the photograph. This is
  implemented via a composited radial highlight, not a filter on the whole image.
  Duration: 300ms, `easing: entrance`. Fades back to neutral over 400ms.
- This replaces any bounding-box or scan-line effect. The garment is illuminated, not
  boxed.

After detection completes:
- The photo descends into its reduced saturation state (10% toward gray) over 600ms.
  This is the signal: the photo has been archived. Now let's look at what we found.

---

## Iconography philosophy

As few marks on the photo as possible. What is placed on the photo must look like it
belongs to the editorial tradition of the app — not a developer debug overlay.

**Garment marker form: the numbered underline.**

When a garment is detected, a thin horizontal underline (1px, terracotta `#c85a3c`,
20px wide) appears beneath the garment's center-of-mass point, and a number (1, 2, 3…)
appears directly above it in PP Neue Montreal, `font-size: xs (12px)`,
`letter-spacing: editorial (0.12em)`, in the same terracotta.

This is the typographic language of a textile sample card — a number refers to a
catalogue entry. It is editorial. It is not a pin, not a tag, not a reticle.

The underline and number are the complete marker. Nothing else on the photo surface.

**Active vs inactive marker state**:
- Active (user has selected this garment): underline is terracotta `#c85a3c`, full
  opacity. Number is terracotta.
- Inactive (other garments): underline is `color.neutral.400 (#a09b90)`, 60% opacity.
  Number is same.

**No icon for the scan trigger itself**: the scan entry point uses a typographic label
("Scan") with a minimal camera outline, described in the mockup spec. No custom icon
needed for MVP.

---

## Recommended token additions (tokens.yaml gaps)

The following tokens are needed for this moment and are not present in v0.1.0:

```yaml
effects:
  motion:
    easing:
      ceremonial: "cubic-bezier(0.22, 1, 0.36, 1)"   # slow-out for marker reveal
      collapse:   "cubic-bezier(0.87, 0, 0.13, 1)"   # fast-in for photo compression

atelier:
  scan_overlay:
    grain_opacity: 0.08
    garment_desaturation_after: 0.10   # 10% toward gray in results state
    vignette_opacity: 0.28             # bottom edge only
    marker_underline_width: "20px"
    marker_underline_height: "1px"
    photo_split_results: "55%"         # photo occupies this % of viewport in results
    photo_split_fullbleed: "100%"
  
  scan_duration:
    fast_path: "2000ms"     # minimum scan feels
    target:    "3500ms"     # design for this
    ceiling:   "6000ms"     # performance budget from context.md
```
