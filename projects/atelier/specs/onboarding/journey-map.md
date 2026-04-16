# Journey Map: Onboarding — First Launch to First Value
**Atelier — Onboarding flow**
Design agent — 2026-04-16

---

## Persona anchor

We are designing for the primary segment from context.md section 3: a fashion-conscious
individual, 22-35, phone-native, who already shops intentionally and curates outfits
mentally before they curate them digitally. They follow style accounts, save inspiration
to Notes or screenshots, and spend real money on clothes. They are aesthetically literate
enough to be annoyed by bad design. They downloaded Atelier because something about the
scan concept caught them — not because they wanted a new organizational app.

This person is not here for a tutorial. They want to know if the app is worth their
attention in the next 90 seconds.

---

## Entry points

**MVP answer: all entry points lead to the same first-launch experience.**

Possible entry points at beta/launch:
- TestFlight invitation (beta) — high-intent, patient
- App Store organic search — moderate intent, curious
- Social referral ("someone showed me this scan thing") — high curiosity, low commitment
- Web landing page CTA — intent varies

The entry point does not change the first-launch flow at MVP. The first-launch experience
must work for the coldest entry (App Store browse) and remain appropriate for the warmest
(direct referral). The differentiator — the scan — handles both: it demonstrates value
without requiring existing context.

Post-MVP: TestFlight and referral deep-links could pre-configure the entry with a brief
context note ("Sent by [name]" or "Beta tester"). Deferred.

---

## Definition of "first value" — the defended pick

### Three options evaluated

**(a) First successful scan with a useful match**
The user photographs or uploads an image, the AI identifies a garment, and at least one
product match is relevant. The user sees what the app is actually capable of.
- Pros: dramatic, memorable, immediately validates the core differentiator.
- Cons: depends on AI accuracy (SPIKE-001 not yet validated); if the scan is off, first
  value becomes first disappointment. Also: not all users may have a scan-worthy photo
  in reach in the first minute.

**(b) First wardrobe item added**
The user photographs or imports a garment into their digital wardrobe. The item appears
in their grid.
- Pros: always achievable; user sees immediate utility.
- Cons: this is not the differentiator. It is infrastructure. Adding a garment to a
  grid is not a "wow" moment; every photo-organization app does it. It validates the
  cold start, not the core promise.

**(c) Something else entirely — first recognition moment**
The user sees the scan working in any context: on their own garment, on a screenshot,
on an inspiration photo. What matters is not that they "added" something or "saved"
something — it is that they experienced the AI seeing what they see.
This is a sub-variant of (a), but it loosens the success criterion: partial results,
one garment identified, is still first value.

### Pick: (c) — first recognition moment, defined as:

**"The user has seen at least one garment detected and at least one product match
suggested, in any context, during the first session."**

### Defense

The whole product lives or dies on the scan being genuinely useful. The onboarding
must end with the user having experienced it — not just been told about it, and not
just having organized some clothes. A first recognition moment is irreversible: once
they have seen the AI identify "Straight-leg denim." and show them three places to buy
it, they understand the product emotionally, not just cognitively.

Wardrobe items are infrastructure for future value (looks, organization). Scan is
immediate, present-tense value. The definition of first value must match what the
product uniquely offers.

The slight widening from "(a)" to "(c)" — accepting partial results as first value — is
intentional. We cannot gate first value on SPIKE-001 achieving 80%+ accuracy; we
anchor it on the experience of recognition itself. Even an imperfect match demonstrates
what the app is trying to do. The user can forgive imperfect results at beta. They
cannot forgive never getting to the scan at all.

**Implication for the whole journey**: every screen in onboarding is navigating toward
this moment. Wardrobe import is offered as a side path, never as a gate. Account
creation is deferred until the user wants to save something. The first fork in the flow
asks: "what would you like to do?" — and both paths eventually lead to scan.

---

## The journey, beat by beat

### Beat 0: The first breath (t=0s, cold launch)

**What the user sees**: a quiet, full-screen moment. The Atelier wordmark, centered,
in PP Editorial New. Warm off-white field. No tagline, no illustration, no animation
other than a fade-in. It holds for approximately 1.5 seconds as the app initializes.

**What the user does**: nothing. They wait.

**What they feel**: neutral curiosity moving toward attention. The restraint signals
taste. The wordmark alone says "this is not going to be like other apps."

**What the system does**: performs cold-launch setup — reads local storage, checks
for existing session, loads tokens, queues font preload. If an existing user session
is found (returning user), routes to the home screen instead of onboarding.

**Decision branch**: new user → Beat 1. Returning user → Beat 10 (see second launch).

**Dropout risk**: none. The user just opened the app.

---

### Beat 1: The first question (t=1.5s)

**What the user sees**: the wordmark dissolves. A single full-screen view arrives.
Left-aligned, generous top padding. In display serif: "How old are you?" is not what
appears here — see age gate design. What appears is the first question of substance:
a clean screen with a number input and a brief note explaining why (legal requirement).

**Note on age gate sequencing**: The age gate (18+ per constraints) is the first
functional screen — before any other interaction. It is BLOCKING. It must appear at
first launch, before the user has invested anything, because it is non-waivable. The
design makes it feel like a natural first moment, not a legal wall.

**What the user does**: enters their birth year (or birth date if needed for precision).
Confirms. If under 18: a gentle, non-punitive "Atelier is for adults" screen with no
path forward. If 18+: advances to Beat 2.

**What they feel**: slight friction (it is an ask before anything has been given), but
the copy and design minimize the bureaucratic feeling. The screen should feel like a
knowing check, not a corporate disclaimer.

**What the system does**: validates age server-side or locally. Stores age-pass flag
to local storage. If under 18, app exits gracefully (shows a single screen with no data
collected).

**Decision branch**: under 18 → blocked (app unusable). 18+ → Beat 2.

**Dropout risk**: low — users who are underage exit, which is intended. Adults proceed.

---

### Beat 2: The offering (t=~20s)

**What the user sees**: the first screen that has a real proposition. This is the
emotional heart of onboarding. It is not a "welcome" screen. It does not enumerate
features. It presents a single sentence and two paths. (Full spec in mockup-spec.md.)

The screen reads (in display serif, large, left-aligned):
"Your clothes, finally seen."

Below that, in body sans, quieter:
"Scan anything. Build your wardrobe. Curate looks."

And then: two options, not framed as buttons but as surface-areas with different visual
weight. Not a fork with two equal choices — a primary invitation and a quieter secondary.

**Primary invitation** (heavier weight, full surface): "Scan a photo now"
**Secondary path** (quieter, below): "Start with my wardrobe"

**What the user does**: chooses one, or does neither yet (scrolling is not available;
the choice is the screen).

**What they feel**: clarity and a little curiosity. The copy is not instructional —
it is declarative. "Your clothes, finally seen" is a provocation, not a welcome.

**What the system does**: nothing yet. No account creation at this point.

**Decision branch**:
- "Scan a photo now" → Beat 3a (scan path — direct to first recognition moment)
- "Start with my wardrobe" → Beat 3b (wardrobe import path)

**Dropout risk**: some users will be uncertain which to pick. This is acceptable.
The copy helps: if you have a photo you want to scan, pick the first. If you have
photos of your clothes, pick the second. Both lead to scan eventually.

---

### Beat 3a: The scan path (immediate value route)

**What the user sees**: the scan chooser sheet rises from the bottom — the same
ScanChooserSheet used throughout the app. No special onboarding framing. The product
is speaking for itself.

**What the user does**: chooses camera or photo library. Picks a photo. Proceeds
through the scan ceremony (pre-scan confirm → scan → results). This is identical to
the full scan-moment spec (specs/scan-moment/).

**What they feel**: during the scan — the "studio reverence" emotional register from
the scan-moment spec. This is where the app reveals what it is. First encounter with
the ceremony: grain texture, stillness, marker reveal, display serif garment label.

**What the system does**: processes the scan. If account exists (it doesn't yet — this
is first launch), would save the scan; instead, holds scan results in session memory.
A soft prompt appears after the first successful result (see Beat 4a).

**Decision branch**:
- Successful scan result → Beat 4a (recognition moment — first value achieved)
- No match / error → returns to the offering screen (Beat 2) with a quiet note:
  "Try a different photo, or start with your wardrobe."
- User cancels → returns to Beat 2.

**Dropout risk**: moderate. If the user doesn't have a good scan photo immediately
to hand, they may not complete the scan. Design mitigates this by making "Start with
my wardrobe" equally reachable from any point. The scan path should never feel like
the only path.

---

### Beat 3b: The wardrobe import path (investment route)

**What the user sees**: a quietly animated prompt to import from their photo roll.
"Your wardrobe might already be in here." with a sub-note: "We'll find the photos
most likely to be clothing." This is the photo-roll import offering.

**What the user does**: accepts (photo library permission is requested if not granted)
or declines and adds manually.

**What they feel**: invited, not demanded. The copy emphasizes discovery ("we'll find")
rather than labor ("you need to add").

**What the system does**: if permission granted, presents a multi-select photo grid
pre-filtered to likely clothing photos (via on-device heuristics or asking the user
to select). Up to 10 photos selected. AI auto-tags in background.

After import (or skip):
- If 1+ items imported → arrives at wardrobe grid with items (a small first reward)
- From wardrobe: the scan button is visible with the State 12 contextual prompt:
  "Scan anything." — "A photo, a screenshot, an inspiration image." This is the
  natural next step from wardrobe. The path reaches scan, just via a longer route.

**Decision branch**:
- Imports photos → wardrobe grid → scan from there → eventually Beat 4a
- Skips import → bare wardrobe empty state → scan prompt is immediately visible
- At any point: "Add manually" (camera) is available

**Dropout risk**: low-moderate. Photo import is satisfying when it works (seeing your
clothes organized is immediately useful). Risk: if the photo heuristics surface many
non-clothing photos, it breaks the magic.

---

### Beat 4a: The recognition moment — first value achieved

**What the user sees**: scan results. The display serif label has appeared.
"Trench coat." or "Oversized blazer." — whatever the AI found. Product matches below.

This is the moment the journey has been navigating toward.

**What the user does**: reads the result. Possibly taps a product card. Possibly saves
to wishlist — which is the first action that requires an account.

**What they feel**: recognition. If the match is good: a quiet delight — "it knows
what it's looking at." If the match is approximate: curiosity — "close enough, let
me look." The design does not over-celebrate. The result is the event.

**What the system does**: if the user taps a product card or "Save to wishlist" — this
is the gate for account creation (see Beat 5). The scan result itself is visible without
an account. Saving or tapping through requires one.

**Decision branch**:
- Taps product card (deep-links to retailer) → account gate (Beat 5)
- Saves to wishlist → account gate (Beat 5)
- Exits scan, goes to wardrobe → Beat 6 (home state)
- Does another scan → repeat Beat 3a

---

### Beat 5: Account creation — the deferred gate

**What the user sees**: a soft prompt, not a wall. Arrives only when the user takes
an action that requires persistence (saving to wishlist, or returning to home after
first scan). It is not an interruption of the scan ceremony — it comes after, in the
cool-down.

The prompt appears as a bottom sheet (not full screen). Copy:
Heading (display serif): "Keep what you found."
Body: "Create an account to save products, build your wardrobe, and pick up where you left off."
Two options: "Create account" (primary) and "Maybe later" (text link — skip)

If "Maybe later": the user can continue browsing the current scan results in session
memory. Scan results held in-session. If they exit the app, results are lost (by design
— not a blocker, just the natural consequence). Next launch will prompt account creation
again.

**What they feel**: understood, not trapped. The timing ("you found something worth
keeping") makes the ask feel logical rather than bureaucratic.

**What the system does on "Create account"**: enters the auth flow (email + password
or social sign-in). Deduplication check for existing accounts. Session data migrated
to the new account on creation.

**Decision branch**:
- Creates account → full app experience unlocked. Scan results saved. Beat 6.
- "Maybe later" → limited session continues. Account creation prompt re-appears on
  next save action or next launch.

**Dropout risk**: moderate. Some users will decline account creation permanently.
This is acceptable — the app should still be usable in a limited session mode. Product-
lead to decide if guest mode is a permanent feature or a soft onboarding onramp.

---

### Beat 6: Home — the post-onboarding state

**What the user sees**: depends on path taken.

After scan path (0 wardrobe items):
- Home screen with the scan button prominent (fixed bottom-right), the contextual
  "Scan anything." prompt visible. Wardrobe tab shows empty state (see mockup-spec.md
  for empty state design). Looks tab shows empty state.
- The empty states are editorial, not sad. They say something about what the space
  is for, not that nothing is there.

After wardrobe import path (1-10 items):
- Wardrobe grid has items. The import gives the home screen life immediately.
- The scan button is visible. The contextual prompt is present.
- First value has been partially delivered: the wardrobe exists. Full first value
  requires completing a scan.

In both cases: the app is not "finished" but it is open. The user has a clear next
action at all times. The product is speaking.

---

## Key moments — the 3 emotional peaks

**Peak 1: First breath (Beat 0)**
Why it is a peak: it sets the entire aesthetic register in one wordmark, one quiet
hold. Users who respond to it are self-selected — they have the taste we are designing
for. The restraint communicates more than any feature carousel would. It is a promise.

**Peak 2: The first offering (Beat 2)**
Why it is a peak: "Your clothes, finally seen." is the first sentence the app speaks
to the user. It must earn that moment. The screen is sparse enough that the copy
carries full weight. The copy either lands or it doesn't — there is nothing else on
the screen to dilute or rescue it.

**Peak 3: The recognition moment (Beat 4a)**
Why it is a peak: this is the app delivering on its promise. The scan ceremony
(which the user is experiencing for the first time) combined with the garment label
in display serif — "Trench coat." — is the product's first proof. It is not explained,
not narrated, not celebrated. It just works, or it mostly works, and the user knows
what it means.

---

## The hand-off to scan

The transition from onboarding into the scan experience (specs/scan-moment/) must be
**seamless — no mode change signal, no "now entering the scan feature" framing**.

When the user selects "Scan a photo now" (Beat 2), the ScanChooserSheet rises in
exactly the same form and with exactly the same animation as it will every time they
use the scan feature thereafter. The onboarding does not have its own variant of this
sheet. It is the same component, same copy, same motion.

The emotional register of the hand-off: from the "studio invitation" tone of onboarding
(hospitable, quiet, unhurried) into the "studio reverence" tone of scan (ceremonial,
still, authoritative). The transition is a deepening, not a break. The user moves from
being invited into the studio to encountering what the studio actually does.

The through-line: the warm off-white surface, the PP Editorial New display type, the
deliberate pace. The offering screen (Beat 2) already uses the typographic and spatial
language of the scan results (same serif, same left-alignment, same generous top space).
When the scan results arrive, the user is already inside the design system.

---

## Post-onboarding state (what the user lands on after onboarding)

**0 wardrobe items, scan completed**:
- Wardrobe grid: empty state (editorial treatment — not empty state in the system-
  error sense; see mockup-spec.md).
- Scan results from first scan: accessible from home via scan history (if account
  created) or present in current session (if no account).
- Scan button: visible and contextually prompted.
- Navigation: home, wardrobe, looks — all tabs present. Looks tab has empty state.

**1-10 items, via import**:
- Wardrobe grid: populated. The user has a digital wardrobe.
- Scan button: visible. Contextual prompt nudging toward scan.
- Home: reflects items. Not "complete" but not empty.

**In both cases**: the app is not in "setup mode" after onboarding. It is in use mode.
There is no "complete your profile" banner, no progress bar, no checklist widget.
The empty states themselves are the next invitations.

---

## Journey diagram

```
LAUNCH
  │
  ▼
[Beat 0] First breath — wordmark, 1.5s, auto-advance
  │
  ▼
[Beat 1] Age gate — BLOCKING — enter birth year
  │
  ├─ < 18 → OUT (graceful exit screen)
  │
  └─ 18+ ──────────────────────────────────────────────┐
                                                        ▼
                                              [Beat 2] The offering
                                        "Your clothes, finally seen."
                                               ↙              ↘
                          "Scan a photo now"         "Start with my wardrobe"
                                 ↓                              ↓
                       [Beat 3a] Scan path              [Beat 3b] Import path
                       (ScanChooserSheet)                (photo roll offer)
                       Camera or Library                      ↓
                             ↓                     [Permission: photo library]
                      Select photo                      Accept │ Skip
                             ↓                           ↓         ↓
                    Pre-scan confirm             Multi-select  Manual add
                    (same as scan spec)          (up to 10)    (camera)
                             ↓                           ↓
                       Scan ceremony              AI auto-tags
                             ↓                    (background)
                    ┌────────┴────────┐                 ↓
                  Match         No match          Wardrobe grid
                    ↓               ↓                   ↓
             [Beat 4a]         "Try another    Scan button visible
         Recognition moment    photo" → B2      (State 12 prompt)
              (FIRST VALUE)                           ↓
                    │                          Eventually: scan
                    ▼
           Tap product / Save
                    ↓
             [Beat 5] Account gate
             (bottom sheet, soft)
                    │
             ┌──────┴──────┐
           Create       Maybe later
           account       (session)
               ↓              ↓
         [Beat 6] Home    [Beat 6] Home
          (full mode)    (session mode)
```

---

## Onboarding resumption

If the user closes the app mid-onboarding:

- **Before age gate**: re-opens to Beat 1 (age gate). No data has been stored.
- **After age gate, before Beat 2**: re-opens to Beat 2 (the offering). Age pass
  is in local storage; no need to re-enter.
- **After Beat 2, no scan completed**: re-opens to Beat 2. Same offering.
  No "welcome back" modal — the user sees the product as if they are starting fresh.
  This is intentional: onboarding is non-linear for most users.
- **After scan completed, no account**: re-opens to the home screen in session mode.
  Scan results from previous session are lost (no persistence without account).
  A soft prompt at the top of the home screen (not a banner — a quiet inline note):
  "Last session's scan isn't saved. Create an account to keep your finds."
  Dismisses on tap. Appears once per session.
- **After account created**: normal returning user flow (Beat 10).

---

## Returning user — second launch (Beat 10)

**What the user sees**: if account exists, the app goes straight to the home screen.
No splash hold. The home screen loads with whatever state they left: wardrobe items
visible, last scan accessible.

The small acknowledgment: the first time a returning user opens the app within 24 hours,
a single quiet line appears at the top of the home screen for 3 seconds, then fades:
"Welcome back." — PP Neue Montreal, `font-size: sm`, `color.neutral.400`.
Not a notification. Not a banner. Just a line of type, present and gone.

On subsequent returns (within the same day): nothing. The app simply is.
After 7+ days away: no special re-engagement screen. The product's state is its own
re-engagement: the wardrobe is there, the scan is there.

---

## Error / offline states during onboarding

**Offline at age gate**: the age gate can be processed locally (client-side). No
network call needed for the age check itself. Proceeds normally.

**Offline at account creation (Beat 5)**: the "Create account" button is visually
unchanged but on tap shows a quiet inline note beneath the email field: "No connection.
Your account will be created when you reconnect." Alternatively: defer to reconnect.
The "Maybe later" path remains available and works offline.

**Offline during photo import (Beat 3b)**: photos are queued. The import UI shows a
quiet state: "Your photos will upload when you're connected." The wardrobe grid
shows the local thumbnails immediately (LQIP quality) — AI tagging happens when
connection returns.

**Permission denied (camera)**: if the user denies camera permission during Beat 3a,
the camera option in ScanChooserSheet is replaced with a quiet note: "Camera access is
off. Enable in Settings to take photos." The photo library option remains available.
A text link: "Open Settings" performs the deep-link to OS settings.

**Permission denied (photo library)**: same treatment for the library option.

**Auth failure during account creation**: inline error below the relevant field.
Specific messages — "That email is already registered. Sign in instead?" with a
"Sign in" text link. "Something went wrong. Try again." for server errors. No error
illustration, no modal.
