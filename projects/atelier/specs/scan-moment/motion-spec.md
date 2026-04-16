# Motion Spec: The Scan Moment
**Atelier — US-010 | Scan ceremony choreography**
Design agent — 2026-04-16

All durations and easings reference or extend `design_system/tokens.yaml`
`effects.motion` section. Gaps are listed as NEW TOKEN proposals at the end.

---

## Global timing language

### Named easing curves

These four curves govern the entire scan moment. Reference them by name throughout.

**`ease-entrance`** (already in tokens: `entrance`)
`cubic-bezier(0.16, 1, 0.3, 1)`
Slow out. Expensive deceleration. Used for elements arriving in view.
Reads as: "landed, settled, unhurried."

**`ease-exit`** (already in tokens: `exit`)
`cubic-bezier(0.7, 0, 0.84, 0)`
Fast in, abrupt stop. Used for elements leaving view.
Reads as: "pulled away cleanly."

**`ease-ceremonial`** [NEW TOKEN: `ceremonial: "cubic-bezier(0.22, 1, 0.36, 1)"`]
`cubic-bezier(0.22, 1, 0.36, 1)`
Very slow out — softer than entrance, nearly floating. Used for the marker reveal
and the product card stagger. The "darkroom development" curve.
Reads as: "emerging, not appearing."

**`ease-collapse`** [NEW TOKEN: `collapse: "cubic-bezier(0.87, 0, 0.13, 1)"`]
`cubic-bezier(0.87, 0, 0.13, 1)`
Symmetrical fast-in, fast-out — the "snap". Used for photo compression when results
arrive. It is the one moment of sharpness in an otherwise slow choreography. The
contrast makes the card reveal feel weightier.
Reads as: "filing away."

---

### Duration ranges

**Micro** (100–200ms): state feedback only. Button press response, active state
highlight on garment selector, checkmark toggle in filter sheet. Never used for
content transitions.

**Standard** (300–400ms): UI chrome transitions. Chooser sheet rising, back arrow
appearing, sort/filter sheet open/close. Tokens: `fast: 200ms` and `normal: 400ms`.

**Ceremonial** (600–1200ms): content-level revelations. Marker appearance, photo
compression, product card stagger. Tokens: `slow: 600ms` and `cinematic: 900ms`.

**Rule**: these ranges never cross. A UI chrome element (back arrow, sort button) does
not get a ceremonial duration. A content reveal (marker, product card) never gets a
micro duration.

---

## Sequence 1: Scan button press → chooser sheet

**Trigger**: user taps scan button (any entry point).

| t | Element | Animation | Duration | Easing |
|---|---|---|---|---|
| t=0 | Scan button | Scale down to 0.94, opacity to 0.7 | 120ms | ease-exit |
| t=80ms | Scan button | Scale returns to 1.0, opacity to 1.0 | 180ms | ease-entrance |
| t=0 | Bottom sheet | Y-translate from +320px to 0, opacity 0→1 | 400ms | ease-entrance |

The sheet arrival and button press are nearly simultaneous — the button confirms first,
then the sheet arrives over it. Total elapsed: ~500ms.

**Reduced motion**: button press: opacity pulse only (no scale). Sheet: fade in (no
translate). Duration halved.

---

## Sequence 2: Pre-scan confirm → scan begins

**Trigger**: user taps "Scan" button on the confirm screen (State 5).

This is the transition from the authored space (user chose the photo) into the
ceremony (AI takes over). The transition must signal the shift.

| t | Element | Animation | Duration | Easing |
|---|---|---|---|---|
| t=0 | "Scan" button + "Choose another" | Fade out, opacity 1→0 | 200ms | ease-exit |
| t=0 | Bottom panel (dark region, 28%) | Height collapses to 0 | 500ms | ease-collapse |
| t=200ms | Photo | Scales up to fill 100% viewport (from ~72% height to full bleed) | 500ms | ease-entrance |
| t=400ms | Grain overlay | Fades in over photo, opacity 0→0.08 | 400ms | ease-entrance |
| t=600ms | Back arrow (cancel) | Fades in, opacity 0→1 | 200ms | ease-entrance |

Total elapsed: ~800ms. The user watches the photo expand to fill the screen. The
controls disappear. The grain arrives. The ceremony has begun.

**Note on the photo scale animation**: the photo was at ~72% screen height in the
confirm screen, letterboxed. When the bottom panel collapses, the photo grows downward
to fill the newly available space. The photo does not stretch — it reveals more of
itself (background `color.brand.primary` was hiding the lower portion). This is done by
changing the container height and animating it, not by scaling the image element.

**Reduced motion**: bottom panel collapses instantly (no duration). Photo fills
instantly. Grain fades in only.

---

## Sequence 3: The detection reveal — THE moment

This is the signature. Timing must feel measured and inevitable, not anxious.

### 3a: Baseline (scan in flight, no detections yet)

The photo is full-bleed. Grain is present. Back arrow is present. Nothing else moves.
Stillness is intentional — it is not a frozen state, it is a waiting state.

If AI returns within 2 seconds (fast path): the stillness lasts <2s. That is fine.
If AI takes longer: see Section 6 (variable latency handling).

---

### 3b: First garment detection (t=0, relative to first detection event)

The AI returns the first garment bounding box. This event triggers the following:

| Relative t | Element | Animation | Duration | Easing |
|---|---|---|---|---|
| t=0 | Luminance lift (radial, 80px radius) at garment center | Opacity 0→0.06 | 300ms | ease-ceremonial |
| t=0 | Underline (GarmentMarker) | Scale X: 0→1, transform-origin: left. Y stays fixed | 400ms | ease-ceremonial |
| t=100ms | Number label | Opacity 0→1, Y: +4px→0 | 300ms | ease-entrance |
| t=700ms | Luminance lift | Opacity 0.06→0 | 400ms | ease-exit |

Total for first marker: ~700ms from detection event.

The underline grows from left to right, as if being drawn. The number fades up
slightly after the line has started (100ms stagger). The light arrives with the line
and fades away once the line has settled. This is the "light catching the photograph"
moment.

---

### 3c: Subsequent garments detected (staggered)

If the AI returns multiple garments in one batch (most likely), they are staggered
with an 80ms delay between each marker activation.

```
Garment 1 marker: t=0
Garment 2 marker: t=80ms
Garment 3 marker: t=160ms
Garment 4 marker: t=240ms
Garment 5 marker: t=320ms (max 5 garments displayed)
```

Each marker follows the same animation from Section 3b. The luminance lifts overlap
in time if multiple garments are detected rapidly — this is intentional and creates a
"multiple recognitions" effect, like multiple photographs being developed simultaneously.

If the AI returns detections progressively (one at a time over several seconds), each
detection fires its marker sequence independently. No artificial stagger needed.

---

### 3d: Detection complete beat — the pause

**When**: all detections are received and all markers have completed their entrance
animations (or a maximum of 400ms after the last detection, whichever comes later).

This beat exists before the results state arrives. It is a deliberate pause — the
moment between "the photograph has been read" and "here is what we found."

Duration: **400ms of stillness**. Nothing moves. The photo with its markers sits in
frame, full-bleed. This is the held breath.

At t=0 of the pause (immediately when detection is confirmed complete):
- Screen reader `aria-live` announces: "Analysis complete. [N] garments identified.
  Results loading."

At t=400ms: Sequence 4 begins.

**Why the pause exists**: in user experience terms, a pause before a reveal increases
the perceived value of the reveal. In aesthetic terms, it is the moment between a
curator placing an object on the table and beginning to speak about it.

**Reduced motion**: pause is preserved. Motion stops; the pause is not motion.

---

### 3e: Product cards enter — the results reveal

| Relative t | Element | Animation | Duration | Easing |
|---|---|---|---|---|
| t=0 | Photo | Height compresses from 100% to 55% of viewport | 600ms | ease-collapse |
| t=0 | Photo desaturation | Saturation filter: 100%→90% | 600ms | ease-ceremonial |
| t=0 | Vignette gradient | Opacity 0→0.28 on bottom edge of photo | 400ms | ease-ceremonial |
| t=200ms | Grain overlay | Opacity 0.08→0 | 400ms | ease-exit |
| t=300ms | Garment label (display serif) | Opacity 0→1, Y: +8px→0 | 500ms | ease-ceremonial |
| t=400ms | Match count + sort/filter | Opacity 0→1 | 300ms | ease-entrance |
| t=500ms | Product card 1 | Opacity 0→1, Y: +16px→0 | 500ms | ease-ceremonial |
| t=580ms | Product card 2 | Opacity 0→1, Y: +16px→0 | 500ms | ease-ceremonial |
| t=660ms | Product card 3 | Opacity 0→1, Y: +16px→0 | 500ms | ease-ceremonial |
| t=740ms | Product card 4 | Opacity 0→1, Y: +16px→0 | 500ms | ease-ceremonial |
| t=820ms | Product card 5 | Opacity 0→1, Y: +16px→0 | 500ms | ease-ceremonial |
| t=600ms | Affiliate disclosure | Opacity 0→1 | 200ms | ease-entrance |

Total elapsed from detection-complete beat start: ~1320ms for all cards.

The photo snaps downward with `ease-collapse` — it is fast, decisive, final. The grain
disappears as the photo "returns from development." The product cards stagger upward
with ease-ceremonial — they emerge, they do not slide. The label arrives before the
cards, so the user reads "Trench coat." before seeing the products. Context before
commerce.

---

## Sequence 4: Total end-to-end timing budget

Performance budget from `context.md`: **< 6 seconds** (upload → first results visible).

| Phase | Duration | Notes |
|---|---|---|
| Photo upload + processing (network + AI) | 1500–5000ms | Variable. Design for 3500ms target. |
| State 2 → State 5 (chooser + confirm) | ~300ms | User action, not AI wait |
| Confirm → ceremony start | 800ms | Sequence 2 |
| Stillness (waiting for first detection) | 0–4000ms | Variable. Overlaps AI processing. |
| Marker reveals (all garments) | 400–700ms | Staggered; starts when first detection arrives |
| Detection complete pause | 400ms | Always present |
| Results reveal (photo compress + cards) | 1320ms | Always present |

**The design is front-loaded**: the "waiting for AI" period is the only variable
component. All animation sequences are fixed. The total AI-side + animation ceiling is:

- **Best case** (AI returns in 1.5s): total ~4.0s
- **Target case** (AI returns in 3.5s): total ~5.7s
- **Ceiling case** (AI returns in 5s): total ~6.5s (slightly over budget)

The ceiling case is acceptable if progressive results are used: the backend should
stream detection events rather than waiting for all garments before returning. The first
marker fires as soon as the first garment is detected, not after all detections complete.
This must be flagged to tech: **the scan API must support streaming/progressive
responses (SSE or WebSocket) for the motion choreography to land correctly.**

---

## Section 6: Handling variable latency

The choreography must feel consistent whether the AI takes 2 seconds or 5.5 seconds.

### Strategy: pad the fast path, cap the slow path.

**Fast path (AI returns < 2s)**:
- We hold the ceremony in the stillness phase (Section 3a) for a minimum of 1200ms
  before firing the first marker — even if the AI has already returned. This prevents
  the reveal from feeling trivial ("too fast, like a trick"). Minimum ceremony duration
  regardless of AI speed: 1200ms of stillness.
- The 1200ms floor is not communicated to the user. It is a perceived quality floor.
- If AI returns in 800ms, we wait 400ms. If it returns in 300ms, we wait 900ms.
  Maximum artificial hold: 1200ms from ceremony start.

**Slow path (AI takes > 5s)**:
- At t=4000ms from ceremony start (not from app launch), if no detections have arrived:
  the "Still analyzing…" micro-copy fades in (see mockup spec State 6). This is the
  only signal. The ceremony continues.
- If the response arrives at t=5500ms: the ceremony fires immediately upon receipt.
  The total end-to-end may reach 7.5s. This is acceptable in edge cases; the 6s budget
  is a P90 target, not a hard ceiling.
- There is no "timeout" error before t=30s. After 30s with no response, fire State 11b
  (server error). Do not show this before 30s.

**Why no spinner**: a spinner communicates uncertainty about duration and implies the
system is struggling. The held stillness communicates confidence. The ceremony says:
"we are looking." The spinner would say: "we are loading." These are different things.

---

## Section 7: Micro-interactions in results

### Garment selector pill tap
- Tapped pill: scale 1.0→0.94→1.0, 150ms total, `ease-entrance`. Background color
  crossfades from inactive to active over 200ms.
- Photo: garment highlight crossfades. Inactive marker fades to `color.neutral.400` over
  200ms. New active marker brightens to terracotta over 200ms.
- Garment label (display serif): the text cross-fades (opacity out → new text → opacity
  in), 200ms each, ease-exit/ease-entrance. It does not scroll or slide — it dissolves.
- Product cards: the card list fades out (opacity 0, 200ms) then the new list fades in
  and staggers (200ms offset, 300ms each, ease-ceremonial). Not a full re-entry — a
  lighter version of the initial reveal (shorter Y offset: +8px, not +16px).

### Product card tap
- Card: background flash to `rgba(26,26,28,0.04)` on press, 100ms, snaps back on
  release.
- Deep-link sheet rises: Y from +400px to 0, opacity 0→1, 400ms, ease-entrance.

### Sort / filter sheet open
- Sheet enters from bottom: Y +300px→0, 400ms, ease-entrance. Scrim: opacity 0→0.4,
  same duration.

### Save to wishlist
- "Save to wishlist" text: opacity 0.6→0 over 150ms.
- "Saved" text + terracotta underline: opacity 0→1, underline scale X 0→1 from left
  (same animation as GarmentMarker underline, 300ms, ease-ceremonial).
- Card left-border appears: opacity 0→0.4, 400ms, ease-ceremonial.
- Haptic: single soft impact on "Saved" state (see Section 10).
- Sheet auto-close: 800ms delay, then sheet translates down +400px, 300ms, ease-exit.

### Scroll behavior on product panel
- No parallax on the photo during product card scroll (parallax would feel playful;
  editorial = static photo).
- Cards scroll normally. No sticky headers within the card list at MVP.

---

## Section 8: Exit transition

**Trigger**: user taps back arrow at any point in the scan flow.

### From scan ceremony (State 6):
- Back arrow tap: all scan UI elements fade to opacity 0 over 300ms, ease-exit.
- Photo: scale 0.94, opacity 0→0, 400ms, ease-exit. It "recedes" rather than
  sliding away.
- Returns to previous screen (confirm state if photo was selected; home/wardrobe if
  scan was cancelled at State 3).

### From results (State 7):
- Back arrow tap: product panel translates down +500px over 400ms, ease-exit.
- Photo expands back to 100% viewport height over 400ms, ease-entrance (mirror of
  the collapse). Photo de-saturation reverses over 400ms.
- Then the full photo fades out over 300ms, ease-exit.
- Returns to the screen that launched the scan.

### Why the photo expands before fading:
The exit is a reverse of the reveal. The photo "un-archives" — it returns to full-bleed
prominence for a moment before disappearing. This feels like closing a book properly
rather than slamming it shut.

---

## Section 9: Haptics

Per context.md aesthetic direction: no heavy haptic interactions. The app does not
celebrate with vibration. Two precisely chosen moments:

**Haptic 1: Detection complete** (when all markers have settled and the pause begins)
- Pattern: single soft impact (iOS: `UIImpactFeedbackGenerator.impactOccurred(style:
  .light)`, Android: `VibrationEffect.createPredefined(EFFECT_CLICK)`).
- Why: this is the quiet signal that "it found something." Not a celebration — an
  acknowledgment. Like a photographer clicking the lens cap onto the camera when they
  are done. It marks the end of the AI's work before the reveal begins.
- Reduced motion: haptic is NOT reduced-motion-dependent. It is retained even when
  visual motion is suppressed, because it is informational (not decorative).

**Haptic 2: Wishlist save confirmed**
- Pattern: single soft impact, same style.
- Why: confirms a persistent action (saving to wishlist). The underline animation is
  visual; the haptic is the physical punctuation.
- No haptic for: scan button tap, garment selector switch, sheet open/close, deep-link
  open. These are navigation, not confirmations.

**What we are explicitly not doing**: no success pattern (multiple taps), no error
rumble, no "loading" pulse. These register as noise in an editorial experience.

---

## Section 10: Reduced-motion fallback

`prefers-reduced-motion: reduce` is honored on all animated elements.

### Reduced motion rule: the reveal still happens, it is just static.

The three states (scanning, markers visible, results visible) still transition. The user
still sees the progression. What changes:

| Element | Full motion | Reduced motion |
|---|---|---|
| Chooser sheet | Translates in from bottom | Fades in (opacity only) |
| Scan begin (photo expand) | Photo fills screen over 800ms | Immediate fill, no transition |
| Grain overlay | Fades in | Not shown (omit grain entirely) |
| Luminance lift | Radial glow on garment region | Not shown |
| Marker appearance | Scale X draw from left + number fade | Markers appear at 100% opacity, no animation |
| Detection pause | 400ms hold (preserved — not motion) | 400ms hold (preserved) |
| Photo compression | Snaps downward over 600ms | Instant snap |
| Product card stagger | Staggered fade + Y translate | All cards fade in simultaneously, 300ms |
| Garment label | Fade + Y translate | Fade only, 300ms |
| Wishlist save | Underline draws + text crossfade | Text crossfade only |
| Exit | Photo expands then fades | Immediate fade |

**The detection pause is always preserved**, even in reduced motion. It is a structural
beat, not a motion effect. The pause before the reveal is the experience.

**Background music / sound**: not in this version. When/if audio is added, it must be
user-initiated, not automatic.

---

## Section 11: Screen reader announcements during the sequence

The sequence must be navigable by VoiceOver/TalkBack users. The following `aria-live`
announcements are fired during the ceremony:

| Moment | Region type | Announcement |
|---|---|---|
| Scan begins (confirm tapped) | `aria-live="polite"` | "Scanning photo for garments. Please wait." |
| First garment marker detected | `aria-live="polite"` | "Garment 1 detected." |
| Subsequent garments | `aria-live="polite"` | "Garment [N] detected." |
| Still analyzing (t=4s) | `aria-live="polite"` | "Still analyzing. Please wait." |
| Detection complete | `aria-live="assertive"` | "Analysis complete. [N] garments found." |
| Results visible | `aria-live="polite"` | "[Garment name]. [N] matches found. Browse results below." |
| No match | `aria-live="assertive"` | "No matches found. [Secondary instruction text]" |
| Error | `aria-live="assertive"` | Error message text verbatim |

**VoiceOver does not wait for visual animations**. Announcements fire as events arrive,
regardless of where the visual choreography is in its sequence. This is correct
behavior — visual ceremony is for sighted users; VoiceOver users get the information
directly.

**After results are announced**: VoiceOver focus moves to the garment label (the
display serif heading). From there, sequential navigation via swipe reaches: garment
selector pills → product cards (each as a link) → sort → filter → affiliate disclosure.
This is the logical reading order and it matches the visual hierarchy.

---

## Recommended token additions (tokens.yaml gaps for motion)

These easing values must be added to `effects.motion.easing` in tokens.yaml:

```yaml
effects:
  motion:
    easing:
      ceremonial: "cubic-bezier(0.22, 1, 0.36, 1)"    # marker reveal, card stagger
      collapse:   "cubic-bezier(0.87, 0, 0.13, 1)"    # photo compression
    duration:
      # Additions to existing fast/normal/slow/cinematic:
      micro:       "120ms"    # button press feedback
      hold:        "400ms"    # detection complete pause (same as normal but named)
      stagger_gap: "80ms"     # delay between each staggered card/marker
```
