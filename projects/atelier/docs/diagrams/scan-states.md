# State Machine — Scan Moment
**Atelier — US-010 · 13 states**
Last updated: 2026-04-17

```mermaid
stateDiagram-v2
    direction TB

    [*] --> S1 : Tap scan button

    S1 : S1 · Entry point
    S12 : S12 · Empty state\n(first scan ever)
    S2 : S2 · Chooser sheet\n📷 Camera or 🖼 Library
    S3 : S3 · Camera view
    S4 : S4 · Photo library\n(native OS picker)
    S5 : S5 · Pre-scan confirm\n"The beat of intention"
    S6 : S6 · Scanning\n"The ceremony"
    S7 : S7 · Results\nStreaming reveal
    S8b : S8b · Product detail\nexpanded sheet
    S8c : S8c · Sort / Filter
    S8d : S8d · Save to wishlist
    S8e : S8e · Add to wardrobe\n+ size picker
    S9 : S9 · No match found
    S10 : S10 · Low-confidence\npartial match
    S11a : S11a · Offline
    S11b : S11b · Server error
    S11c : S11c · Rate-limited\n(10 scans/day)
    S11d : S11d · Not a fashion photo
    S13 : S13 · Affiliate disclosure\n(persistent in results)

    S1 --> S12 : first scan ever\n(no scan history)
    S12 --> S2 : tap scan
    S1 --> S2 : returning user

    S2 --> S3 : choose camera
    S2 --> S4 : choose library
    S2 --> S11a : device offline

    S3 --> S5 : photo taken
    S4 --> S5 : photo selected

    S5 --> S6 : tap "Scan"
    S5 --> S2 : "Choose another"
    S5 --> [*] : back arrow

    S6 --> S7 : match found\n(streaming reveal)
    S6 --> S9 : no garment detected
    S6 --> S10 : confidence < 0.65
    S6 --> S11b : server error (5xx)
    S6 --> S11c : daily limit reached
    S6 --> S11d : not a fashion photo

    S7 --> S13 : results panel open
    S7 --> S8b : tap product card
    S7 --> S8c : tap Sort or Filter
    S7 --> S2 : scan another

    S8b --> S8d : "Save to wishlist"
    S8b --> S8e : "Add to wardrobe"
    S8b --> S7 : close sheet

    S8d --> S7 : saved · sheet closes
    S8e --> S7 : saved · sheet closes

    S8c --> S7 : apply filters

    S9 --> S2 : "Try another photo"
    S10 --> S7 : show results anyway

    S11a --> S2 : dismiss
    S11b --> S6 : retry
    S11b --> S2 : dismiss
    S11c --> [*] : come back tomorrow
    S11d --> S2 : try another photo

    note right of S6
        No spinner.
        Stillness = confidence.
        Grain texture overlay.
        Numbered underline markers
        appear progressively.
    end note

    note right of S8e
        Size picker mandatory.
        Brand-aware options.
        Pre-filled if brand known.
        Account gate if not logged in.
    end note
```

## State inventory

| State | Name | Key design decision |
|-------|------|---------------------|
| S1 | Entry point | 3 locations: home, wardrobe, photo view |
| S2 | Chooser sheet | Bottom sheet — not modal overlay |
| S3 | Camera view | No reticle, no guide — full viewfinder |
| S4 | Photo library | Native OS picker — no custom implementation |
| S5 | Pre-scan confirm | "Beat of intention" — retained by design |
| S6 | Scanning ceremony | No spinner — stillness signals confidence |
| S7 | Results | Photo stays full-bleed, panel rises from bottom |
| S8b | Product detail | Bottom sheet (70% viewport) — not full-screen push |
| S8c | Sort / Filter | Best match default (not price ascending) |
| S8d | Save to wishlist | Optimistic UI · terracotta underline acknowledgment |
| S8e | Add to wardrobe | Mandatory size picker before save |
| S9 | No match | Editorial treatment — copy on photo, no illustration |
| S10 | Low confidence | Same layout as S7 + calibration note — no warning color |
| S11a-d | Errors | Inline, minimal — no error illustrations |
| S12 | Empty state | Contextual prompt above scan button — no modal |
| S13 | Affiliate disclosure | Persistent footer — one per results session |
