# Learnings — Atelier

What we've discovered as we build. Append-only. Latest at top. Promote stable learnings into `context.md` when they become assumptions we build on.

---

## 2026-04-16 — Open hypotheses to validate (not yet learnings)

These are things we're assuming but haven't yet validated. They'll move out of this section once tested.

| Hypothesis | How we'll test it | Confidence |
|---|---|---|
| AI can identify garments accurately enough (≥75% top-3 useful match rate) | SPIKE-001: test harness on 100 fashion photos | Medium |
| Users will invest 10+ min building a wardrobe IF scan works without it | DISC-001: 5 prototype user tests | Low |
| Retailer APIs + affiliate networks legally accessible for our use | SPIKE-002: legal review + API evaluation | Medium |
| Editorial aesthetic resonates with 20-40 fashion-conscious audience (vs feeling exclusionary) | Beta user testing | Medium |
| Curation is the primary value, not social sharing | Measure WAS vs post/feed engagement once both exist | Low |
| Inference cost per scan can stay below $0.02 | SPIKE-001: measure cost during spike | Low |

## 2026-04-17 — Setup friction : Python + pip absent sur Mac par défaut

**Context**: tentative de lancer le script de download SPIKE-001 depuis le Mac du Product Builder
**Learning**: `pip` et `python` ne sont pas disponibles par défaut sur macOS récent. Le Product Builder n'avait ni Homebrew, ni Python installé — setup de 0 requis avant tout run local.
**Evidence**: `pip command not found`, `brew command not found` rencontrés lors de la session
**Implications**: documenter les prérequis système dans le README du spike ; envisager un script d'installation ou un Makefile `install` pour éviter ce blocage à chaque nouveau contributeur
**Confidence**: high — reproductible sur tout Mac neuf

---

<!-- Learning template — use this when adding real learnings:

## YYYY-MM-DD — [Short title]

**Context**: where the learning came from (experiment, user research, build)
**Learning**: what we now know (1-3 specific sentences)
**Evidence**: data or observation supporting it
**Implications**: what this changes about our approach
**Confidence**: low / medium / high

-->
