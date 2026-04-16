# Memory Protocol

How agents remember what they do, what they learn, and what they build.

**Core principle: agents have no native memory between sessions. Files ARE the memory.** Anything not written to a file is lost.

---

## Two tiers of memory

### Tier 1 — Workspace memory (versioned in Git, shared)

Lives in each project under `projects/[name]/memory/`. Shared across all sessions, humans, and agents. Versioned in Git.

```
projects/[name]/memory/
├── decisions.md          ← append-only log of significant decisions + reasoning
├── learnings.md          ← what we discovered, patterns, surprises
├── sessions.md           ← end-of-session summaries (handoffs between sessions)
├── research/             ← user research, interviews, surveys, benchmarks
├── experiments/          ← spike results, A/B test outcomes, prototypes tested
└── references/           ← external sources, inspiration, competitive intel
```

### Tier 2 — Agent memory (Claude Code built-in, per-agent)

Lives at `~/.claude/agent-memory/product-[role]/` on each machine. Personal to the agent across all projects. Accumulates patterns, preferences, reusable insights.

Activate by giving the subagent `User scope` during creation. Each agent uses it for things like:
- `product-tech`: common code patterns, recurring bug types, tooling preferences
- `product-design`: aesthetic references that keep working, accessibility edge cases
- `product-lead`: prioritization heuristics, estimation calibration

---

## Protocol: what agents MUST do

### At session start

Every agent reads, in order:

1. `CLAUDE.md` (auto-loaded)
2. Its own definition (`.claude/agents/product-[role].md`)
3. The project's `context.md`
4. The project's `memory/sessions.md` — last few session summaries (what was being worked on)
5. Relevant files for the current task (e.g. `backlog.yaml`, `memory/decisions.md` if making a decision that may revisit past ones)

If the user starts a task without giving full context, the agent asks:
> "Which project are we working on?"

Then it loads the context above before answering.

### During work

Agents write to memory **as they go**, not only at the end. Specifically:

- **Made a decision?** → append to `memory/decisions.md`
- **Learned something non-obvious?** → append to `memory/learnings.md`
- **Collected data (user interview, benchmark, spike result)?** → create a file in `memory/research/` or `memory/experiments/`
- **Found a great reference?** → add to `memory/references/`

### At session end

The agent produces a session summary. Format (append to `memory/sessions.md`):

```markdown
## YYYY-MM-DD — [Agent name] — [Short session title]

**Task**: what was the user's goal
**Worked on**: specific stories/artifacts touched
**Outcome**: what was delivered, what's now in different state
**Decisions made**: (links to decisions.md entries if any)
**Open questions / next steps**: what the next session should pick up
**Files changed**: list of files created or modified
```

If the user doesn't ask for a summary, the agent still writes a concise one before ending.

---

## Templates

### `decisions.md` entry

```markdown
## YYYY-MM-DD — [Short title]

**Who decided**: [agent] (or [human] if escalated)
**Context**: what was the situation
**Options considered**:
- Option A: ... (chosen / rejected because...)
- Option B: ...
**Decision**: what was chosen
**Reasoning**: why
**Consequences**: positive, negative, neutral
**Revisit if**: condition that would reopen this
**Related**: links to stories, ADRs, specs
```

### `learnings.md` entry

```markdown
## YYYY-MM-DD — [Short title]

**Context**: where the learning came from (experiment, user research, build session)
**Learning**: what we now know (1-3 sentences, specific)
**Evidence**: data or observation that supports it
**Implications**: what this changes about our approach
**Confidence**: low / medium / high
```

### `research/` file naming

`research/YYYY-MM-DD_[method]_[topic].md`

Examples:
- `research/2026-04-20_interviews_onboarding-friction.md`
- `research/2026-04-22_benchmark_competitor-scan-features.md`
- `research/2026-05-05_survey_body-measurement-privacy.md`

### `experiments/` file naming

`experiments/YYYY-MM-DD_[type]_[what].md`

Examples:
- `experiments/2026-04-18_spike_ai-product-matching.md`
- `experiments/2026-05-10_ab-test_scan-cta-placement.md`

---

## What counts as "significant" (must log)

**Decisions** that must be logged:
- Scope changes (adding or removing a feature)
- Architecture or stack choices
- Aesthetic direction commitments
- Anything that would be expensive to reverse
- Anything that resolves a prior ambiguity

**Learnings** that must be logged:
- User research finding (even negative)
- Validated or invalidated hypothesis
- Technical constraint discovered during implementation
- Pattern that keeps working across features
- Anti-pattern discovered (something we thought worked but didn't)

When in doubt, log it. The cost of over-logging is tiny. The cost of losing a decision is re-litigating it 3 months later.

---

## Anti-patterns

- **Writing memory into chat only** — if the agent says "I decided X" and you accept, but nobody writes it down, it's not remembered.
- **Memory without a date** — entries without `YYYY-MM-DD` make it impossible to trace when things were known.
- **Decisions without reasoning** — "we chose React Native" without why is useless; future sessions will second-guess it.
- **Dumping raw research** — research files must have a summary at the top; don't leave future sessions to re-derive insights from raw notes.
- **Forgetting to reload memory** — at the start of any session, the agent must check `sessions.md` and relevant files. "Cold-starting" every time loses continuity.

---

## Memory hygiene

- Review `memory/learnings.md` every sprint — promote stable learnings into the project's `context.md` (they become assumptions, not hypotheses)
- Review `memory/decisions.md` every quarter — archive decisions older than 6 months into `memory/decisions_archive_YYYY.md` to keep the active log scannable
- `memory/sessions.md` grows quickly — archive entries older than 1 month the same way

---

## Setting up Claude Code agent memory (Tier 2)

When creating or editing your subagents via `claude agents`, select `User scope` to enable persistent memory at `~/.claude/agent-memory/[agent-name]/`. The agent will accumulate insights there across all projects.

This is different from Tier 1: Tier 1 is project-specific and versioned; Tier 2 is agent-personal and local to your machine.

Recommendation: enable Tier 2 for all three agents. It's especially valuable for `product-tech` (learns codebase patterns) and `product-design` (learns your aesthetic preferences that keep landing).
