# Decisions — [PROJECT NAME]

Append-only log of significant decisions for this project. Latest at top.

**Read this file before making any decision that could overlap with past ones.**
**Write to this file every time you make a decision worth remembering.**

See `../../MEMORY.md` for the full protocol.

---

## What to log here

- Scope changes (adding or removing a feature)
- Architecture or stack choices
- Aesthetic direction commitments
- Anything expensive to reverse
- Anything that resolves a prior ambiguity
- Any time Lead arbitrates between Design and Tech

## What NOT to log here

- Routine implementation choices covered by `shared/code_standards.md`
- Small design tweaks within an already-approved aesthetic direction
- Day-to-day prioritization adjustments (those live in `backlog.yaml`)

---

## Initial project decisions to capture

When this project is initialized, the first decisions are usually:

- [ ] Project name
- [ ] North star metric
- [ ] Primary audience definition
- [ ] Aesthetic direction
- [ ] Tech stack
- [ ] MVP scope (what's in, what's explicitly deferred)

Delete this checklist once all are logged below.

---

<!-- Template — copy this block for each decision:

## YYYY-MM-DD — [Short decision title]

**Who decided**: [agent-name] or [human-name]
**Context**: what was the situation that required a decision
**Options considered**:
- Option A: ... (chosen / rejected because...)
- Option B: ... (chosen / rejected because...)
**Decision**: what was chosen
**Reasoning**: why this option over the others
**Consequences**:
- +: positive implications
- −: trade-offs accepted
- Neutral: side effects
**Revisit if**: condition that would trigger reopening this decision
**Related**: links to stories (US-###), ADRs (ADR-###), specs

-->
