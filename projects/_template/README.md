# [PROJECT NAME]

[One-line pitch — what is this project?]

## Current state

- **Stage**: `idea` | `mvp` | `growth` | `mature`
- **Active sprint**: see `roadmap.yaml`
- **North star metric**: [what's the one metric that matters]

## Files

- `context.md` — vision, audience, aesthetic, stack, constraints (read this first)
- `backlog.yaml` — prioritized user stories
- `roadmap.yaml` — current sprint + milestones
- `changelog.md` — append-only shipped history
- `memory/` — persistent memory (decisions, learnings, sessions, research, experiments)
- `design_system/` — project-specific tokens and components
- `specs/` — feature specs produced by Design for Tech
- `adr/` — architecture decision records

## First-session checklist (when project is created)

The `product-lead` agent should handle these in the first session:

- [ ] Fill in `context.md` completely (vision, audience, stack, constraints)
- [ ] Customize `design_system/tokens.yaml` for this project's aesthetic
- [ ] Log initial decisions in `memory/decisions.md` (name, north star, aesthetic, stack, scope)
- [ ] Capture open hypotheses in `memory/learnings.md`
- [ ] Seed `backlog.yaml` with first user stories and any discovery spikes
- [ ] Write the kickoff session summary in `memory/sessions.md`

## Starting a session on this project

In Claude Code:

```
Work on projects/[this-folder-name]. [Describe your task]
```

The relevant agent (`product-lead`, `product-design`, `product-tech`) auto-delegates based on the task. Before working, agents automatically read:

1. This project's `context.md`
2. Last entries in `memory/sessions.md`
3. Current `backlog.yaml`
4. Any relevant past decisions in `memory/decisions.md`
