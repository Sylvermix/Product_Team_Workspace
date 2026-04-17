# Agent Memory — Product Lead

Cross-project patterns, heuristics, and calibrations accumulated over time.
Append-only. Latest entries at top.

---

## 2026-04-17 — Atelier — GitHub issues as the human-facing backlog mirror

**Context**: Setting up a board for a product owner who needed to create tickets and track progress visually.
**Pattern**: Keep `backlog.yaml` as source of truth for agents, GitHub issues as the mirror for human interaction. Sync is one-directional: backlog → GitHub. Never let humans edit backlog.yaml directly — they create GitHub issues and agents sync back.
**Evidence**: Product owner immediately used issues to understand scope; JTBD section was the first thing requested as an addition.
**Applies to**: Any project where a human product owner needs a visual board without losing the structured YAML backlog.

---

## 2026-04-17 — Atelier — JTBD as the most valuable single addition to a ticket

**Context**: Product owner asked to add a JTBD section to every GitHub issue.
**Pattern**: "When [situation], I want to [motivation], so I can [expected outcome]." — one sentence, written from the user's perspective. This is the first thing a stakeholder reads and it anchors every other field. Add it as the first section, before user story.
**Evidence**: Request came immediately after seeing the first batch of issues — it was the only structural addition requested.
**Applies to**: All projects. Every issue, every story, every ticket format.
