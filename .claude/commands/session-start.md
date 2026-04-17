# /session-start

Loads the full project context at the start of a session so no agent cold-starts.

## Instructions

Follow these steps exactly, in order.

### Step 1 — Identify the project

If the user specified a project name in the command arguments, use it.
Otherwise, ask: "Which project are we working on today?"

The project root is `projects/[name]/`.

### Step 2 — Load context in order

Read the following files sequentially (order matters):

1. `CLAUDE.md` — team principles (already auto-loaded, but confirm it's in context)
2. `projects/[name]/context.md` — product vision, audience, stack, constraints
3. `projects/[name]/memory/sessions.md` — **last 3 entries only** — what was worked on recently, open questions
4. `projects/[name]/memory/decisions.md` — **last 20 lines only** — most recent decisions, to avoid re-litigating
5. `projects/[name]/backlog.yaml` — current stories, their status, and what's blocked
6. `projects/[name]/roadmap.yaml` — current milestones and sprint goal

### Step 3 — Load role-specific resources

Depending on which agent(s) will be active this session:

| Agent | Read at session start |
|---|---|
| product-lead | `projects/[name]/memory/decisions.md` (full, if making decisions that could revisit past ones) |
| product-design | `shared/accessibility_checklist.md` — always. `projects/[name]/design_system/tokens.yaml` if touching UI. |
| product-tech | `shared/code_standards.md` — always. `projects/[name]/adr/` — if making architecture decisions. |

Also read `shared/agent-memory/product-[role].md` to load cross-project patterns.

### Step 4 — Surface the current state

After loading, output a short brief (not a long report):

```
## Session brief — [Project] — [Date]

**Last session**: [one sentence from sessions.md]
**Sprint goal**: [from roadmap.yaml]
**Top of backlog**: [next 2-3 ready stories]
**Blockers**: [anything blocked + why]
**Open questions from last session**: [bullet list]
```

### Step 5 — Confirm and proceed

Ask the user: "What are we working on today?" — unless they already specified a task in the command arguments, in which case proceed directly.
