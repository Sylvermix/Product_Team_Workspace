# Aesthetic Direction: Onboarding
**Atelier — First launch to first value**
Design agent — 2026-04-16

---

## What this moment is, emotionally

The scan moment's register is "studio reverence" — ceremonial, still, authoritative.
Onboarding is what comes before: the studio door is open, the light is on, someone is
expecting you. The sub-tone for onboarding is **"studio invitation."**

Not warm in a friendly-app way. Warm in the way a space is warm when it has been
prepared. The first breath screen, the age gate, the offering — these are the threshold.
The product is not performing welcome. It is simply present, composed, and ready.

Studio invitation means:
- Confident without being cold
- Hospitable without being effusive
- Quiet in a way that reads as preparation, not emptiness

The user is being let into somewhere. The product is not chasing them.

---

## What the app is saying when it first speaks

The posture is **confident and curious in equal measure.** Not shy — there is nothing
tentative about "Your clothes, finally seen." But not declarative in a boastful way —
the period at the end of the headline ("finally seen.") is a breath, not a shout.

The app knows what it is. It does not need to prove it. It is extending an invitation,
not pitching a product. The difference matters: a pitch shows you the slides, an
invitation opens the door.

The copy carries this posture completely. The design's job is to give the copy room
to land: generous top spacing, a single serif headline, nothing competing with it.

---

## Typography

**Display serif (PP Editorial New)**: arrives in two moments in onboarding.

First: the wordmark at cold launch — "Atelier", 52px, weight 400. This is the app's
signature. Before any feature, before any ask, this is the name, in the typeface that
will carry every significant label throughout the product's life. It is not decorative;
it is identity.

Second: the offering screen headline — "Your clothes, finally seen." at 52px, left-
aligned, with generous top padding. This is the first sentence the product speaks. The
serif establishes that this will be an editorial product: considered, textured, not
a utility.

Subsequent onboarding screens (age gate, import offering) use the display serif for
their headings at smaller sizes (36px, 28px). The serif scales down gracefully — it
does not become less distinct at smaller sizes, because the letterforms are characterful
at any scale.

**Body sans (PP Neue Montreal)**: carries all the explanation, instruction, and secondary
copy. It is never strained — it is not trying to be elegant, it is just clear. The
relationship between serif and sans in onboarding mirrors the relationship throughout
the app: the serif speaks first (the claim, the label, the heading), the sans follows
(the context, the instruction, the option).

The body sans is used at `letter-spacing: editorial (0.12em)` for short labels and
button copy — this gives it the atelier-register feeling even at small sizes. For body
paragraphs (auth sheet body copy, import rationale), it uses `letter-spacing: normal`
for readability.

---

## Copy voice

The voice in three adjectives: **precise, unhurried, knowing.**

**Precise**: no filler words. No "Simply enter your date of birth to get started."
Just: "One thing first." and "Your birth year." The copy always takes the direct path.

**Unhurried**: there is no urgency in the copy. No "now", no "instantly", no
"in just seconds." The product is not in a hurry to sell itself. "Your clothes,
finally seen." — "finally" implies a wait, a long wait, that is now resolved. It
is the opposite of urgent.

**Knowing**: the copy assumes the user is fashion-literate and phone-native. It does not
explain what a wardrobe is. It does not describe what scanning means. "Scan a photo now."
is enough. The sub-label "Point at anything with clothes" is contextual, not a tutorial.

**Three example lines**:

1. The opening line — "Your clothes, finally seen." — is not a welcome. It is a
   recognition. The word "finally" speaks to a felt gap (organizing clothes is always
   slow, imprecise, effortful) and closes it without inflation. It does not say "easily"
   or "automatically" or "in seconds." It says "seen" — which is both literal (the
   camera) and emotional (understood).

2. A permission ask — "Atelier uses your photo library to let you add clothes from
   existing photos and scan inspiration images you've saved." — is straightforward but
   the construction "inspiration images you've saved" is knowing. It assumes the user
   already has a folder of screenshots and saved posts, because our primary audience
   does. It is not explaining a use case; it is naming a behavior the user already has.

3. A skip label — "Skip for now" — is the bare minimum. Not "Maybe later", not
   "I'll do this later", not "No thanks." "Skip for now" is honest and neutral. It
   does not express disappointment ("Are you sure?") or sycophancy ("No worries!").
   It is just the name of the action.

**Lines we would never write**:
- "Welcome to Atelier" — the product doesn't greet you, it opens the door.
- "Let's get started" — implies the user needs encouragement. They don't.
- "Your personal style assistant" — assistant is the wrong register (servile, utility).
- "Curate your closet" — "closet" is American English and too casual for the brand register.
- "Discover your style" — vague, every app says this.
- "Create your digital wardrobe in minutes" — urgency and time-claim, both wrong.

---

## Use of imagery

**No stock editorial imagery in onboarding.** The reasoning:

Stock fashion imagery would immediately establish a comparison point the app cannot
control. The user might think: "this photo is not my style." Or: "this model doesn't
look like me." Or simply: it looks like every other fashion app.

The only imagery during onboarding is the user's own photos — appearing in the scan
ceremony (which they select themselves) or in the multi-select import grid (their own
camera roll). This is the only correct use of imagery in onboarding: the user's own
clothes, their own images, seen for the first time as a wardrobe.

When the user first sees their own garment detected and labeled "Oversized blazer." —
that is the only image that matters. No stock photo could compete with it.

The off-white background and the editorial type are the visual foundation. Negative
space is the "imagery." The product does not need to perform visual richness in
onboarding — the scan ceremony will provide that at the exact right moment.

---

## Transitions from onboarding into the app

The visual through-line is threefold:

**Color**: warm off-white `#f6f3ed` is the background from Screen 0 through the home
screen. There is no mode-change. The surface the user is on when they first see "Atelier"
is the same surface they are on when they see their wardrobe grid. The app is not
putting on a different outfit for onboarding.

**Typography**: PP Editorial New appears in the wordmark (Screen 0), the age gate heading,
the offering headline, the import complete beat, and then — in the scan results — as the
garment label "Trench coat." The user experiences the same typeface in the same weight
throughout. When the garment label arrives in the scan ceremony, it is not a new voice;
it is the same voice that has been speaking since the wordmark.

**Pace**: the deliberate unhurriedness of onboarding (600ms fade-in on the wordmark,
400ms stagger on the offering, the held pause of the import complete beat) directly
prepares the user for the scan ceremony's pace. The user who has moved through onboarding
has been calibrated to expect slow, weighted transitions. When the scan's 400ms detection
pause arrives — the held breath before the results — it reads as natural, not odd.
The onboarding is a temporal training, not just an introduction.

The transition from "studio invitation" to "studio reverence" is a deepening, not a
break. When the ScanChooserSheet rises from the bottom — first time the user sees it,
triggered by tapping "Scan a photo now" — it is the same component that will rise every
time they scan, for the life of the product. The onboarding does not have its own
version. The product has already begun.
