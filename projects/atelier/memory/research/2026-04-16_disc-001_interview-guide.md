# Interview Guide: DISC-001 — Onboarding Effort Validation
**Atelier — User Research**
Product-lead — 2026-04-16

---

## Goal

This research exists to answer one decision question: **should we proceed with the current MVP scope — wardrobe building as a real effort the user invests in, scaffolded by the scan feature delivering instant gratification first — or should we reduce scope to a scan-only MVP and cut the wardrobe investment epic entirely?**

The current MVP bets that users will spend meaningful time (10+ minutes) building a digital wardrobe once they have experienced the scan delivering instant value. If that bet is wrong, we are building the wrong product. Five interviews cannot prove the hypothesis true; they can surface enough disconfirming evidence to prevent a costly misdirection. That is their job.

---

## Primary Hypothesis and Falsification Criteria

**Hypothesis (from DISC-001 backlog entry)**:
"Users will spend 10+ minutes building initial wardrobe IF the scan feature works without it — meaning scan delivers value before any wardrobe setup is required."

**What it means in practice**: the sequence matters as much as the activity. Scan first, wardrobe later. Users who experience scan value first are predicted to have high motivation to then catalog their wardrobe. Users who arrive at a wardrobe-building requirement with no prior payoff are not the same test.

### Falsification criteria — what evidence would change our minds:

| Finding | What it falsifies | Decision implication |
|---|---|---|
| Users describe wardrobe building as a chore they have already tried and abandoned (in existing apps or in their own photo rolls) | The effort investment hypothesis | Descope wardrobe to AI-assisted only (import-only, no manual tagging) |
| Users say scan alone would satisfy their need — they have no desire to own a catalog of their wardrobe | The wardrobe-as-complement hypothesis | Pursue scan-only MVP; wardrobe becomes optional/late feature |
| Users are enthusiastic about scan but express no interest in returning to add more items after the first session | The sustained investment hypothesis (10+ minutes implies multiple sessions or a long first session) | Shorten MVP wardrobe scope; design for single-session "enough wardrobe to do one look" |
| Users do not understand what "building a wardrobe" means or think it sounds unappealing when described | The concept clarity hypothesis | Reframe the value prop; wardrobe = "your clothes, organized" vs "a digital catalog" |
| Users who engage deeply with their clothing do not take photos of it / do not use photo roll for fashion | The photo-native behavior hypothesis | Rethink the photo import mechanic |
| Users express high interest in wardrobe but zero interest in scan — "I just want to organize what I own" | Curation hypothesis; also scan-first sequencing | Reconsider whether scan is actually the entry point or an accessory |

The interview is **broken** if the only possible result is "yes, users love wardrobes" or "yes, but...". These falsification criteria define what breaking looks like. A session that produces none of these signals is as informative as one that produces several — the absence of disconfirming signals is itself data, but only if the protocol genuinely invited them.

---

## Secondary Hypotheses to Test in This Round

| Hypothesis | What we're testing | Observable signal |
|---|---|---|
| Curation (looks creation) is the north-star behavior — not browsing or discovery | Whether fashion-conscious users already curate looks mentally, digitally, or physically — and whether this is a felt need or a latent one | Do participants describe combining clothes into looks as a behavior they do? Do they do it habitually or occasionally? |
| The first-offering pattern reads correctly — scan dominant, wardrobe as a sentence you follow | Whether the visual hierarchy (one dominant surface invitation, one quiet text link) communicates priority without hiding the secondary path | Concept reaction: does the participant see the wardrobe path without prompting? |
| Account creation can be deferred without losing the user | Whether users in this segment would exit if asked to create an account before seeing value | Past behavior: did they abandon other apps at account creation gates? |
| The audience is who we think it is | Whether segment 3 descriptions (fashion-conscious, intentional shoppers, 22-40, phone-native) map to real humans in this research | Demographics + behavior check in warm-up and current behavior sections |

---

## Session Structure (60 minutes)

```
00:00 – 05:00   Warm-up (5 min)
05:00 – 20:00   Current behavior probes (15 min)
20:00 – 40:00   Core hypothesis probes (20 min)
40:00 – 55:00   Concept reactions (15 min)
55:00 – 60:00   Closing (5 min)
```

The moderator should keep times loosely. If the core hypothesis section is producing rich material at the 35-minute mark, let it run. Never cut off a participant mid-thought to hit a time marker. Do cut the closing to 3 minutes if needed.

---

## Full Question List with Probes

### Warm-up (0–5 min)

**Purpose**: build rapport; confirm participant fits the profile; surface their general context. Do not yet discuss the app concept.

---

**W1. Can you tell me a bit about yourself — not your job, but more like your daily life? What does a typical day look like for you?**

*Why this question*: opens relaxed. Reveals lifestyle context (commute, social life, pace) without directly asking about fashion. Let the participant choose what to share.

Follow-up probes:
- "Where do you spend most of your time — home, office, out and about?"
- "What's on your phone right now that you use every single day — like habitually?"

---

**W2. When you think about getting dressed in the morning — what's that actually like for you? Quick decision, or is there more to it?**

*Why this question*: anchors the session in a real daily behavior. Avoids "how important is fashion to you?" (triggers social desirability). Surfaces natural vs effortful relationship with clothing.

Follow-up probes:
- "Is there a difference between weekday and weekend morning for you?"
- "Do you have go-to outfits, or do you rethink it every time?"

---

### Current Behavior Probes (5–20 min)

**Purpose**: understand what participants actually do — not what they would theoretically do. Anchor everything in past behavior. This section should feel like a conversation about their life, not a research interview.

---

**B1. When you buy something new to wear — what does that process look like from start to finish? Take me through the last time you bought a piece of clothing.**

*Why this question*: reveals shopping behavior (online/offline, browsing vs intentional), price sensitivity, platform usage, and how much they track what they buy.

Follow-up probes:
- "Where do you usually start — are you browsing or do you have something specific in mind?"
- "Once you found it, how did you decide to actually buy it?"
- "What did you do with it after you got it home — did anything change about how you dressed that week?"

---

**B2. Have you ever taken a photo of something you were wearing, or of a piece of clothing — not to post it, just for yourself? Tell me about the last time that happened.**

*Why this question*: this is the most important behavior probe for the photo-native hypothesis. It surfaces whether participants already use their photo roll as a wardrobe reference without any app prompting them. Anchor explicitly in a real past instance, not general tendency.

Follow-up probes:
- "What did you take the photo for — like what were you going to do with it?"
- "Did you go back to that photo? How often?"
- "Is there a folder or album you keep these in, or are they just mixed in with everything else?"

---

**B3. What do you do when you see something someone else is wearing — on the street, on social, anywhere — and you want to find out what it is or where to get it?**

*Why this question*: surfaces existing product-search behavior. Maps to the scan feature's use case. If participants already have workarounds (screenshot + Google Lens, screenshot + asking friends, manually searching descriptions), the scan addresses a real felt need.

Follow-up probes:
- "Has that worked for you — does your current method get you to the actual product?"
- "How many times out of ten would you say you successfully track down the item?"
- "What happens the other times?"

---

**B4. When you think about your wardrobe — the clothes you actually own right now — how well do you feel like you know it? Like, could you picture every item?**

*Why this question*: calibrates how much mental overhead participants already spend on wardrobe awareness. A participant who says "I have no idea what's in the back of my wardrobe" has a different relationship to organization than one who says "I know exactly what I own."

Follow-up probes:
- "Have you ever gone to put something on and realized you'd forgotten you owned it?"
- "Is there anything in your wardrobe that you own but never wear — do you know why?"
- "Have you ever done anything to try to get more organized with your clothes — anything digital or physical?"

---

**B5. You mentioned [reference their answer to B4]. Have you ever tried any app or tool to keep track of your wardrobe or plan outfits? If yes: tell me about that. If no: has the idea ever occurred to you?**

*Why this question*: surfaces competitor app experience without naming competitors. Reveals past investment and abandonment patterns. Critical for understanding effort tolerance.

Follow-up probes (if they have tried an app):
- "How did you use it — did you set it up fully, or try it and let it go?"
- "What made you stop, or what made you keep going?"
- "What was the part that felt like the most work?"

Follow-up probes (if they have not tried an app):
- "What would have to be true for something like that to be worth your time to set up?"
- "What would make it feel like too much work?"

---

**B6. When you're planning an outfit — for something specific, or just a normal day — what does that actually look like? Do you think about it in advance, lay things out, look at photos?**

*Why this question*: surfaces look-curation behavior. The north-star hypothesis is that curation is the goal, not discovery. This question reveals whether curation is already a natural behavior or an aspirational one.

Follow-up probes:
- "Do you ever mix things from your wardrobe that you haven't combined before?"
- "Have you ever saved a specific outfit combination — to repeat it or to remember it?"
- "Do you share outfit ideas with anyone? How?"

---

### Core Hypothesis Probes (20–40 min)

**Purpose**: get as close as possible to what participants would actually do in the real scenario — not what they say they'd do. Use past-behavior anchors and hypothetical framing only when necessary.

---

**H1. Think about the last time you tried something new on your phone — a new app, a new feature — and actually stuck with it. What made it stick?**

*Why this question*: surfaces what drives sustained engagement for this participant. The answer reveals whether they are effort-tolerant if the payoff is clear, or effort-averse regardless of payoff.

Follow-up probes:
- "Was there a specific moment where you thought 'okay, this is worth keeping'?"
- "How long did it take before you felt like you 'got it'?"
- "Have you deleted an app for the opposite reason — it asked too much too soon? Tell me about that."

---

**H2. If you found an app that could look at any photo — a magazine, a screenshot, something someone's wearing on the street — and tell you what the clothes are and where to buy them: what would your first move be?**

*Why this question*: maps to the scan-first path in onboarding. Surfaces whether participants would immediately scan (and what they'd scan), or whether they'd hesitate. Do not describe Atelier yet. This is a concept probe on the functional value, not the app.

Follow-up probes:
- "Do you have a photo in your phone right now that you'd immediately want to try it on?"
- "What would you hope it found? What would you be disappointed by?"
- "How many times would you try it before deciding whether it worked?"

---

**H3. Now imagine that same app also offered to help you build a catalog of your own wardrobe — your actual clothes, organized, searchable. The catch is you'd need to photograph each item, or let it pull from your photo roll. What's your honest reaction to that?**

*Why this question*: this is the central effort-investment probe. The wording is neutral — it names both the benefit and the cost ("the catch is"). It explicitly invites the honest reaction. Do not soften the effort ask.

Follow-up probes:
- "Is that something you'd do in one sitting, or a bit at a time?"
- "How many items do you think you own? Does that change your answer?"
- "What would have to be in it for you — what would the catalog have to do — for that effort to feel worth it?"
- "At what point would you give up and stop adding things?"

---

**H4. Let's say you tried the scan feature first — you took a photo of something, it found the item and showed you where to buy it, and it worked really well. After that experience, would your reaction to building the wardrobe catalog change?**

*Why this question*: tests the IF in the DISC-001 hypothesis. The hypothesis is conditional: effort is contingent on scan working first. This question surfaces whether the conditionality actually holds for this participant.

Follow-up probes:
- "Why or why not — what would have changed for you?"
- "Would you feel differently if the scan result was only approximate — close but not exact?"
- "What if the scan took 10 seconds? 30 seconds? At what point would the first experience stop feeling like it was worth it?"

---

**H5. Have you ever organized something on your phone that required a real time investment — a playlist, a collection, a folder of photos, anything like that — and actually finished it? Tell me about that.**

*Why this question*: past-behavior anchor for sustained organizational effort. Participants who have never invested effort in digital organization are less likely to invest in wardrobe building, regardless of what they say. Participants who have done it elsewhere have demonstrated the capacity.

Follow-up probes:
- "How long did it take before it felt like it was worth the effort?"
- "Did you come back to it, or was it a one-time thing?"
- "Is there anything like that on your phone right now that you set up and still use?"

---

**H6. Imagine you'd spent 15 minutes scanning and organizing about 20 items in your wardrobe. Then you closed the app. And then you opened it again the next morning. What would you expect to see? What would make you glad you spent that 15 minutes?**

*Why this question*: surfaces what the return value looks like to participants — what "keeping" a wardrobe catalog means to them. The answer reveals whether they're imagining it as a reference tool, a creative tool, a shopping tool, or something else.

Follow-up probes:
- "Would you expect to use it daily, or more occasionally?"
- "What's the thing you'd do with the catalog that you can't do now without it?"

---

### Concept Reactions (40–55 min)

**Purpose**: expose participants to the specific bets we've made in the onboarding design and observe reactions. This section uses written concept descriptions, not a working prototype. The moderator reads each stimulus aloud and then invites reaction. Do not show the stimuli on a screen if possible — read them. This avoids participants reacting to visual design choices (which are not yet ready for testing) rather than the concept.

For each stimulus: read aloud, then pause, then ask the reaction question. Do not explain the concept after reading. If the participant misunderstands, that is data.

---

**Stimulus A: The scan moment (the first-offering screen)**

*Moderator reads aloud*:

"Imagine you open the app for the first time. The first thing you see after the opening screen is a large dark panel that takes up most of the screen. On it, in large serif type, it says: 'Scan a photo now.' Underneath, smaller: 'Point at anything with clothes.' Below that panel, separate from it, a simple text link: 'Start with my wardrobe.' That's all that's on the screen."

*Reaction question*: "What's your first instinct looking at that — what would you do?"

Follow-up probes:
- "What do you think the 'Start with my wardrobe' option does?"
- "Is there anything you'd expect to see on that screen that isn't there?"
- "If you wanted to do the wardrobe thing instead of the scan, would you know how?"

---

**Stimulus B: The scan ceremony**

*Moderator reads aloud*:

"When you take or upload a photo, the app doesn't show a loading spinner. Instead, it just holds your photo, full screen, still. After a few seconds, small underline marks appear on different items of clothing in the photo, each with a number. Then a panel slides up from the bottom showing product matches for each numbered item — where to buy them, prices. The first garment label appears in large type: 'Straight-leg denim.' Then the product cards arrive underneath."

*Reaction question*: "What's your reaction to that — does that feel right to you for this kind of feature?"

Follow-up probes:
- "What would you do in those few seconds while the photo is just sitting there?"
- "What would you expect to see for the product matches — just photos and prices, or something more?"
- "What would make that experience feel like it worked, vs didn't work?"

---

**Stimulus C: The photo-roll import invitation**

*Moderator reads aloud*:

"When you choose 'Start with my wardrobe,' you see a screen that says: 'Your wardrobe might already be in here.' Underneath: 'We'll find the photos most likely to be clothing.' Then it offers to show you a selection from your camera roll — you can pick up to 10 photos — and it will automatically add and tag those items to your wardrobe in the background. There's always an option that says 'Skip for now.'"

*Reaction question*: "What's your honest reaction to that? Would you let it pull from your photo roll?"

Follow-up probes:
- "What would make you say yes to that?"
- "What would make you say no, or be nervous about it?"
- "If it pulled up 10 photos — and some of them were clothes, some weren't — what would you do?"

---

**Stimulus D: The deferred account creation**

*Moderator reads aloud*:

"You've done your first scan, you've seen some product matches. There's no account, no login — you went straight to using it. Then you tap on a product you like to save it. At that point, a sheet slides up from the bottom. It says: 'Keep what you found.' Below that: 'Create an account to save products, build your wardrobe, and pick up where you left off.' You can also tap 'Maybe later' to skip account creation and keep browsing."

*Reaction question*: "What do you think of that timing — does it feel right, or would you expect the account part to happen earlier or differently?"

Follow-up probes:
- "If you tapped 'Maybe later' — what would you expect to happen to the things you found?"
- "Have you had experiences with apps that asked you to create an account before you could do anything? How did you feel about that?"
- "What would it take for you to create an account at this point in the experience?"

---

### Closing (55–60 min)

**Purpose**: surface anything the structured questions missed. End on a concrete, actionable note.

---

**C1. Thinking about everything we've talked about — if you were actually going to try this app, what's the one thing that would make you delete it in the first week?**

*Why this question*: surfaces deal-breakers that the protocol may not have named. Gives the participant permission to be critical in concrete terms.

Follow-up probes:
- "Has something like that happened with another app you tried?"
- "Is that a general thing, or specific to something about this kind of app?"

---

**C2. What's the thing that would make you keep it — or tell someone about it?**

*Why this question*: surfaces the value proposition as the participant actually imagines it, in their own words. Often differs from what we'd predict.

Follow-up probes:
- "Would it be more about what the app does, or about how it does it?"

---

**C3. Is there anything we didn't talk about that you think is important — anything about how you dress, shop, or use your phone that feels relevant?**

*Why this question*: open invite for topics the protocol didn't reach. Participants often save their most honest observations for this moment.

---

## Do-Not-Ask List

The following questions are explicitly prohibited. All moderators should review this before the session.

| Prohibited question | Why |
|---|---|
| "Would you use this app?" | Users notoriously say yes to almost any concept when asked directly; the question creates social pressure to be positive. The answer tells us nothing. |
| "Would you pay for this?" | Same problem, compounded by the participant not having used the product. Past behavior on app purchases is more informative. |
| "What features would you like to see?" | Participants design for their immediate imagination, not for what would actually change their behavior. (Henry Ford: if I asked people what they wanted, they'd have said faster horses.) |
| "Is the scan idea interesting to you?" | Interesting ≠ useful ≠ sticky. Ask about actual behavior, not intrinsic interest. |
| "Do you think this is a good idea?" | Invites evaluative judgment, not behavioral insight. Not our question to ask. |
| "How much time do you spend on fashion?" | Triggers social desirability bias — participants overstate. Ask about specific behaviors instead. |
| "Have you heard of [competitor app name]?" | Anchor bias — immediately frames the concept against a known reference. Ask about behavior first; if they bring up competitors themselves, follow up. |
| "What do you think about the design?" | This session is not a design review. We are testing behavioral hypotheses, not visual preferences. If participants volunteer aesthetic observations, note them; don't invite them. |

---

## Concept Stimulus Descriptions — Full Text for Moderator Use

These are the verbatim scripts for each stimulus in the concept reaction section. Moderators read these exactly as written. No paraphrasing.

(See the Concept Reactions section above for full Stimulus A–D texts. These are already written as moderator-read scripts.)

---

## Moderator Tips — Specific to This Audience

**On wardrobe size**: asking "how many items do you own?" triggers self-consciousness. Most people genuinely don't know and will feel embarrassed by either extreme ("I don't have much" = low status; "I have too much" = excessive). Instead: "if you had to guess — like a rough number — how many pieces do you think are hanging in your wardrobe right now?" Framing it as a rough guess defuses the judgment.

**On price sensitivity**: do not ask participants to name prices they spend on clothes. Instead anchor to behavior: "when you're buying something online, do you tend to have a rough budget in mind before you start looking, or does the price reveal itself as you browse?" This surfaces price-consciousness without triggering status anxiety.

**On social desirability in fashion context**: fashion is an identity domain. Participants will present a more intentional, curated self than they actually experience. Counteract this by anchoring relentlessly to specific past events ("tell me about the last time...") rather than general tendencies ("do you usually..."). The last specific time is harder to idealize than a general pattern.

**On photo privacy**: when asking about photo roll access (Stimulus C), some participants will express hesitation they'd actually override in the moment. Do not rush to reassure them that "it's safe." Their hesitation is data. Ask what specifically concerns them. Only clarify after they've expressed their honest reaction.

**On early adopter vs average user dynamics**: participants who describe themselves as fashion-forward or tech-forward will be enthusiastic. The most valuable probes are with the "average user" participant. Spend extra time on H3 (wardrobe effort) with this participant — their resistance (or absence of it) is load-bearing.

**On silences**: after reading each concept stimulus, allow 5 full seconds of silence before prompting. Many participants fill silence with their real reaction. Early prompting cuts off the most honest moments.

---

## Research Ethics

**Informed consent**: participants receive a written consent form before the session begins. It states: the purpose of the research, that the session will be recorded (audio and/or video), who will have access to the recording, how data will be stored and for how long, that they can withdraw at any time without consequence, and that their name will not appear in any report (participant IDs P01–P05 only).

**Recording**: sessions are recorded with explicit consent. Recordings are stored in a password-protected folder, accessible only to the research team. Recordings are deleted 90 days after the final report is complete.

**Transcription**: if AI transcription is used, the transcript is reviewed for accuracy. Any mention of participant names, employers, or identifying details is redacted before the transcript is shared with the broader team.

**GDPR alignment**: in line with context.md constraints, participants are EU-data-compliant. Consent is documented. Data minimization principle applies: we collect only what is necessary for the research. Right to erasure: if a participant requests deletion of their session data after the fact, we comply.

**No minors**: per context.md, no participants under 18. The screener enforces a 22-minimum age (matching the primary audience) and moderators verbally confirm age at session open.

**Compensation disclosure**: compensation amount and form are disclosed in the recruitment screener and repeated at session start. Compensation is not contingent on any particular response or outcome. Participants know this.

**Right to stop**: moderators state explicitly at the start: "You can stop or skip any question at any time without explaining why. If you want to stop the session entirely, just say so." This is not a legal formality — it is true, and participants need to believe it for the research to be valid.
