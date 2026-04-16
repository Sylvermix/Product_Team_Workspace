# Recruitment Brief: DISC-001 — Onboarding Effort Validation
**Atelier — User Research**
Product-lead — 2026-04-16

---

## Participant Count: 5

### Defense

Five qualitative interviews are appropriate for this round because:

1. **This is hypothesis scoping, not hypothesis confirmation.** We are not trying to produce statistically significant findings; we are trying to decide whether the primary hypothesis is directionally viable before committing full MVP engineering effort to wardrobe building.
2. **Nielsen's saturation research** on usability testing (and widely replicated in qualitative behavioral research) suggests that 5 participants from a homogenous segment surface approximately 80% of the major themes. Our segment is relatively well-defined.
3. **Speed and cost discipline.** At this stage, moving quickly to validate or kill the hypothesis is more valuable than a large study that arrives after the MVP is half-built.
4. **This round is not the last.** Five interviews answers the "proceed or pivot" question. If results are ambiguous (see below), a second round of 3-5 participants can be scheduled immediately after synthesis.

### Follow-up rounds — when to run them

| Result | Trigger | Follow-up |
|---|---|---|
| Hypothesis clearly supported | 4-5 participants show strong past-behavior evidence of effort investment and clear enthusiasm for the conditional scan-first model | No immediate follow-up; run beta validation instead |
| Hypothesis clearly unsupported | 4-5 participants show effort avoidance, abandoned previous wardrobe attempts, or express scan-only preference | Run immediate pivot workshop (product-lead); no second round needed |
| Results split 2/3 or ambiguous | 2 participants support, 2 oppose, 1 neutral; or the condition (scan-first) was not consistently tested | 3-participant follow-up within 2 weeks, sharper focus on the conditional question. Also check: was the H4 question landing correctly? |
| Secondary hypotheses produce surprising results | Curation vs discovery result contradicts our assumption strongly | Domain-specific second round on curation behavior only |

---

## Must-Have Screening Criteria

All participants must meet every criterion below to qualify.

**SC1 — Age**: 22–40 years old.
*Rationale*: matches context.md section 3 primary audience. Lower bound of 22 (not 20) to ensure post-education adult life stage where wardrobe investment begins. Upper bound of 40 per primary segment definition.

**SC2 — Device**: owns a smartphone (iOS or Android), uses it as their primary internet device, and takes photos with it at least several times per week.
*Rationale*: the entire product is phone-native. A participant who rarely uses their phone camera is not the target user.

**SC3 — Fashion intentionality**: self-describes as someone who thinks about and cares about what they wear — not necessarily in fashion industry terms, but as someone for whom clothing is an active choice rather than a background activity.
*Screening proxy*: see screener question SQ4 below.

**SC4 — Online shopping recency**: has shopped for clothing online within the last 60 days.
*Rationale*: establishes active engagement with fashion as a consumption behavior, not purely a physical-retail or inherited-wardrobe behavior.

**SC5 — Outfit planning time**: spends at least 10 minutes per week thinking about outfits, combining items, or planning what to wear in advance.
*Threshold defense*: 10 minutes/week is a deliberately low bar. It captures anyone who makes intentional outfit decisions (vs completely passive dressing). This keeps the pool large enough to recruit 5 without forcing over-specification. What we are filtering OUT is the participant who says "I just grab whatever."
*Screening proxy*: see screener question SQ5.

**SC6 — Photo behavior**: has taken at least one photo of clothing (their own or someone else's) in the last 6 months for any reason other than a social post.
*Rationale*: tests for the photo-native behavior that the scan feature assumes. A participant who never photographs clothing is a user we may eventually serve, but not the one who will validate the current product hypothesis.

---

## Must-Avoid (Disqualifiers)

| Criterion | Reason for exclusion |
|---|---|
| Works in UX / product design / user research | Trained to perform enthusiastic helpfulness in interviews; will give us what they think we want |
| Works in fashion retail, styling, or fashion publishing | Expert users with professional frameworks; will not represent the primary consumer segment |
| Works at a technology startup in a product or design role | High familiarity with app concepts inflates enthusiasm and suppresses real-behavior anchors |
| Currently active daily user of a direct competitor app (e.g., Stylebook, Whering, Cladwell) | **Exception**: include one participant who has tried and abandoned a competitor app — their abandonment story is invaluable. Disqualify active daily users only. |
| Under 22 or over 40 | Outside primary segment |
| Participated in any product research session about a fashion or shopping app in the last 3 months | Research-conditioned behavior; will give "research participant" answers |
| Does not take photos with their phone regularly | Not phone-native |

**On the competitor app exception**: one participant who tried and abandoned a wardrobe/outfit app (Stylebook, Combyne, Whering, Cladwell, etc.) should be recruited intentionally. Their abandonment narrative is our richest source of evidence about the real failure mode of effort investment. Ask at screener: "Have you ever tried an app to organize your wardrobe or plan outfits? If yes, do you still use it?" If they tried one and stopped, flag as a desirable inclusion.

---

## Diversity Requirements

At n=5, full diversity is a constraint, not an optimization. These are mandatory minimums.

**Gender mix (3 women, 1 man, 1 any/open)**
*Defense*: fashion app category skews heavily toward female-coded recruitment. Recruiting 5 women would produce findings that do not generalize and would bias our audience definition. At n=5, we cannot represent the full spectrum, but we must not produce an all-female sample. One man and one participant who identifies outside the binary minimum — not for box-checking, but because men who care about fashion are a real and underserved segment in this product space.

**Body diversity (at minimum: do not recruit 5 participants with similar body types)**
Aim for at least one participant who wears above a US size 14 (EU 44). Fashion apps, especially AI-driven ones, often fail on non-standard sizes — both in catalog matching and in body self-image around photography. Their reaction to the photo-upload mechanic and AI categorization is high-signal for product risk.

**Skin tone diversity**
At minimum: do not recruit 5 participants with similar skin tones. AI garment detection and product matching quality varies across skin tones due to training data distribution. One participant with a very deep skin tone (Fitzpatrick VI) is minimum. This is a product quality risk as much as a fairness one — surfaces it early.

**Geography (minimum 2 cities; recommend remote sessions)**
At minimum: participants from two different cities, and at least one participant from outside a major fashion hub (London, Paris, Milan, New York). Urban-suburban split matters: the suburban participant may have a different relationship to getting dressed (more car-based, less street-fashion influence) and potentially a larger wardrobe and more practical relationship to organization.

**Income range (premium + value shoppers)**
At minimum: one participant who primarily shops at fast fashion or mass-market retailers (ZARA, H&M, ASOS), and one who primarily shops at premium or luxury retailers (Self-Portrait, COS, Cos, Sandro, or above). The product serves both. The AI scan's utility differs at different price points (product matching quality may be higher for more widely indexed products). Surfacing this early is valuable.

**Tech comfort (one "average user")**
At minimum: one participant who does not self-describe as tech-forward, does not use multiple apps for any single purpose, and for whom the idea of an AI analyzing their photos is new rather than familiar. This participant is our best calibration against early-adopter enthusiasm bias.

**Organized vs disorganized (one "messy wardrobe" POV)**
Mandatory: at least one participant who explicitly describes their wardrobe as disorganized, chaotic, or hard to manage. This participant anchors the "cold start" risk (context.md section 9). Their friction point with the catalog-building effort may be different from — and more predictive than — the organized participant's.

### Diversity allocation target for 5 participants

| # | Gender | Body size | Shopper profile | Tech comfort | Wardrobe state |
|---|---|---|---|---|---|
| P01 | Woman | Standard | Premium | Average | Organized |
| P02 | Woman | Plus (US 14+) | Value | Tech-forward | Disorganized |
| P03 | Man | Any | Mid-market | Average | Any |
| P04 | Woman | Any | Value | Any | Any |
| P05 | Any/open | Any | Premium | Tech-forward | Any |

This is a target, not a rigid spec. The must-avoid criteria and must-have criteria take precedence. If recruitment produces a partial mismatch (e.g., the man is tech-forward), that is acceptable.

---

## Recruitment Channels

### Recommended: Respondent.io (primary)

**Why**: fast turnaround (typically 3-5 business days), professional screener tooling, and participants are pre-verified with identity checks. Researchers can specify demographic targets precisely.
**Selection bias**: Respondent users tend to skew toward tech-adjacent urban professionals who are experienced interview participants. Mitigate by: (a) including the disqualifier for people who have done product research in the last 3 months, and (b) specifically requesting non-tech-adjacent participants for P01 and P03 slots.
**Cost estimate**: approximately $60–80 per participant as a research incentive (handled by Respondent); platform fee additional. Total: approximately $500–700 for 5 participants plus platform costs. Confirm with human owner.

### Optional: Prolific.co (supplementary for harder-to-find profiles)

**Why**: larger pool than Respondent for niche profiles (e.g., "plus size, premium shopper, non-tech-forward"). Better for body-diversity and income-diversity targeting.
**Selection bias**: similar to Respondent but with a slightly more academic skew. Same mitigations apply.

### Avoid (with reasons)

| Channel | Reason to avoid |
|---|---|
| Personal/founder network | Friendlies; will not give honest critical feedback; skewed demographics |
| Instagram fashion tags outreach | Skewed toward content creators; over-represents fashion-forward behavior vs average user |
| Fashion subreddits (r/femalefashionadvice, r/malefashionadvice) | Over-engaged users with strong opinions; high social desirability to perform fashion knowledge |
| User testing agency | Slow (10-14 days typical); cost-inefficient for 5 sessions |
| LinkedIn | Wrong context; professional identity frame suppresses personal behavior honesty |

---

## Compensation

**Recommendation**: 60 GBP / 70 EUR / $75 USD per participant (adjust for local currency at recruitment time).
*Defense*: 60-minute qualitative interview at professional research rates. This is above casual survey incentives to attract participants who take the session seriously. Below the level that attracts professional research participants who do this for income. The sweet spot.
*Format*: Amazon gift card or PayPal transfer, delivered within 48 hours of the session. Do not use cash. Do not make payment contingent on any particular response or completion of any specific question.
*Disclosure*: compensation amount is stated in the recruitment screener. No surprises.

---

## Screener Questionnaire

The following questions are sent to all applicants before scheduling. Applicants who do not meet criteria are thanked and declined (politely, with no explanation of the specific reason for disqualification).

Target screener length: 8–10 minutes to complete.

---

**SQ1. How old are you?**
[ ] Under 22 → disqualify
[ ] 22–30
[ ] 31–40
[ ] Over 40 → disqualify

---

**SQ2. Which of the following best describes your primary smartphone?**
[ ] iPhone (iOS)
[ ] Android phone
[ ] I don't have a smartphone → disqualify

---

**SQ3. Roughly how often do you take photos on your phone?**
[ ] Multiple times a day
[ ] Once a day or so
[ ] A few times a week
[ ] Once a week or less → disqualify

---

**SQ4. When you're getting dressed in the morning, which of these sounds most like you?**
[ ] I just grab whatever is closest or clean — it's not something I think much about → disqualify
[ ] I usually have a rough sense of what I want to wear, but it's quick
[ ] I think about what I'm going to wear, sometimes plan it in advance → include
[ ] Getting dressed is something I genuinely enjoy and put thought into → include

*Note to screener admin*: the second option is borderline — include if needed to hit recruitment targets, but prioritize the third and fourth options. The first option is a hard disqualify.

---

**SQ5. Roughly how much time per week do you spend thinking about outfits — choosing combinations, looking at what you have, planning ahead?**
[ ] Almost none — I don't really think about it → disqualify
[ ] 5–10 minutes a week
[ ] 10–30 minutes a week → include
[ ] More than 30 minutes a week → include
[ ] Hard to say — I think about it throughout the day → include

---

**SQ6. In the last 60 days, have you bought any clothing or accessories online?**
[ ] Yes
[ ] No → disqualify

---

**SQ7. Have you ever taken a photo of a piece of clothing — yours or someone else's, in real life or from a screen — for any reason other than posting it on social media?**
[ ] Yes, I do this fairly regularly
[ ] Yes, I've done it a few times
[ ] Maybe once or twice, I'm not sure
[ ] No, I don't think so → note (does not disqualify alone, but flag if combined with other low-engagement signals)

---

**SQ8. What is your current job or occupation? (Free text)**

*Screener admin note*: review responses and disqualify per the must-avoid criteria (UX/product research/fashion industry/tech startup). Flag any responses near the boundary for human review before disqualifying.

---

**SQ9. Have you ever used an app specifically to organize your wardrobe, plan outfits, or keep track of your clothing? Examples: Stylebook, Whering, Cladwell, Combyne, or similar.**
[ ] Yes, I currently use one regularly → disqualify (active daily competitor user)
[ ] Yes, I tried one but stopped using it → flag as desirable — this is the competitor-abandonment profile we want one of
[ ] I tried one briefly but never really used it
[ ] No, I've never tried one

---

**SQ10. Have you participated in a paid user research session (interview, focus group, usability test) for any technology product in the last 3 months?**
[ ] Yes → disqualify
[ ] No

---

**SQ11. (Optional, for diversity) What size do you typically wear in women's tops or dresses? (Skip if not applicable)**
Free text — used for body-diversity targeting. Not a disqualifying criterion. Treat all responses as acceptable.

---

**SQ12. Which of the following best describes your relationship to technology?**
[ ] I'm usually one of the first people I know to try new apps or devices
[ ] I try new technology when I hear enough good things about it
[ ] I tend to wait until something is well established before I try it
[ ] I prefer to keep things simple — I use the same apps I know

*Note*: this is a targeting variable. We want at least one participant from the bottom two options (average/late adopter) and no more than two from the first option.

---

## Logistics

### Remote vs in-person

**Recommendation: remote sessions via video call.**
*Defense*: at n=5 with a geographically distributed target sample, remote sessions allow recruiting from multiple cities without travel cost or logistic complexity. For this research, the relevant behaviors (phone use, photo habits, wardrobe relationship) do not require in-person presence. Concept stimuli are read aloud, not shown on screen, so screensharing is not critical.
*Caveat*: remote sessions suppress non-verbal observation (body language, environmental context). For this round, verbal data is the primary evidence source; this is an acceptable trade-off.

### Recording and transcription tool

**Recommendation: Zoom with built-in recording + Otter.ai or Rev for transcription.**
*Why Zoom*: universal familiarity; no download required for participants on web; reliable recording quality; participants are comfortable with the interface.
*Why not Lookback or UserTesting.com*: Lookback is appropriate for prototype testing with screen interaction. Since our stimuli are read aloud (no prototype), Lookback adds friction and cost without benefit for this round.
*Transcription*: Otter.ai (faster, AI-generated, good for English) or Rev (human transcription, higher accuracy, slower, ~$1.50/minute). Recommend Rev for sessions where audio quality is uncertain. Budget ~$90/session for Rev transcription; ~$0 beyond subscription for Otter. Confirm with human owner.
*Recording consent*: confirmed at screener and verbally at session start. Sessions not recorded if participant declines (note-only session acceptable).

### Scheduling

Use Calendly or a scheduling link. Offer slots in two-hour windows (to allow for 60-minute session + buffer). Do not schedule back-to-back sessions — the moderator needs 20 minutes between sessions for notes.

Provide participants with a confirmation email including: session link, duration, compensation details, and right-to-withdraw reminder.

---

## Timeline (2026-04-16 to 2026-05-14)

**Target completion**: DISC-001 deliverable by week 4 (approximately 2026-05-14).

| Dates | Activity | Owner |
|---|---|---|
| 2026-04-16 – 2026-04-18 | Human owner approves budget, moderator assignment, and recruitment channel. Research guide reviewed. | Human owner |
| 2026-04-18 – 2026-04-19 | Screener published on Respondent.io (or designated platform). Screening begins. | Moderator / recruiter |
| 2026-04-18 – 2026-04-25 | Recruitment window open. Screener responses reviewed daily. Participants selected and confirmed. | Moderator / recruiter |
| 2026-04-25 – 2026-04-28 | Scheduling window. Sessions booked for the week of 2026-04-28. Reminder emails sent 24h before. | Moderator |
| 2026-04-28 – 2026-05-02 | **Interview week.** 5 sessions conducted (target: 1-2 per day, M-F). | Moderator |
| 2026-05-02 – 2026-05-05 | Buffer for rescheduled or no-show sessions. Transcripts prepared. | Moderator |
| 2026-05-05 – 2026-05-10 | **Analysis week.** Per-participant notes completed. Cross-participant synthesis completed using analysis template. | Analyst (product-lead or designated) |
| 2026-05-12 | Draft report reviewed with human owner. | Product-lead + human owner |
| 2026-05-14 | **Final report out. DISC-001 deliverable complete.** | Product-lead |

*Note*: this timeline assumes the human owner approves budget and moderator by 2026-04-18. A 2-day delay at this stage compresses the interview window. The latest the interviews can start and still hit the 2026-05-14 deadline is 2026-05-05 (giving 5 business days for analysis).
