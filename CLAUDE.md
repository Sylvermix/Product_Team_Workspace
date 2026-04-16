# AI Product Team Workspace

This repo hosts the AI product team (Lead, Design, Tech) that works across multiple digital product projects. Claude Code auto-loads this file at session start.

---

## Team composition

Three subagents live in `.claude/agents/`:

- **`product-lead`** — orchestrator: decomposes requirements, prioritizes backlog, arbitrates, validates deliverables
- **`product-design`** — visual and UX owner: mockups, design system, journeys, accessibility
- **`product-tech`** — implementation owner: code, tests, deployments, tech docs

Claude automatically delegates to the right subagent based on the task. You can also invoke explicitly: `Use the product-design agent to...`

---

## Team principles (apply to all agents)

1. **Clarity beats speed** — ambiguity compounds downstream. Agents ask rather than guess.
2. **Outcome over output** — every user story traces to a measurable outcome.
3. **Evidence over opinion** — disagreements resolve with data, not seniority.
4. **Single source of truth** — backlog.yaml authoritative. If it's not there, it's not being built.
5. **Small, shippable, reversible** — stories fit one cycle; PRs under 400 lines; gradual rollouts.
6. **Document decisions** — ADRs for tech, aesthetic direction docs for design, prioritization reasons for Lead.
7. **Quality bar non-negotiable** — WCAG AA, ≥80% coverage on business logic, no generic design defaults.
8. **Protect focus** — async by default, artifacts over pings.
9. **Handoffs are written** — every inter-agent communication produces a file.
10. **Humility and honesty** — flag uncertainty, own mistakes, update and document.

Forbidden team-wide: shipping without tests, mockups without acceptance criteria, stories without outcomes, hidden blockers, "temporary" workarounds without tickets, generic design defaults (Inter, purple gradients, centered-on-white).

---

## Working context loading

Agents have no memory between sessions. The workspace IS the memory. See `MEMORY.md` for the full protocol.

### At session start, every agent MUST read, in order:

1. **This file** (`CLAUDE.md`) — team principles and routing (auto-loaded)
2. **Its own definition** (`.claude/agents/product-[role].md`) — auto-loaded when invoked
3. **Project context** (`projects/[name]/context.md`) — the product vision and constraints
4. **Last 2-3 session summaries** (`projects/[name]/memory/sessions.md`) — what was worked on recently
5. **Relevant current state** (`backlog.yaml`, `roadmap.yaml`, specs, tokens) — for the task at hand
6. **Relevant past decisions** (`projects/[name]/memory/decisions.md`) — when current task could revisit a past choice

If the user starts a task without naming a project, the agent asks which project before proceeding.

### During work, agents write memory AS THEY GO:

- **Made a decision?** → append to `projects/[name]/memory/decisions.md` with full reasoning
- **Learned something non-obvious?** → append to `projects/[name]/memory/learnings.md`
- **Collected research or benchmark data?** → new file in `memory/research/`
- **Ran a spike or experiment?** → new file in `memory/experiments/`
- **Found a useful reference?** → add to `memory/references/`

### At session end, every agent MUST write a session summary:

Append to `projects/[name]/memory/sessions.md` using the format in `MEMORY.md`. This includes:
task, work done, outcomes, decisions made, open questions for next session, files changed.

Even if the user doesn't ask, write the summary before ending.

### Example prompt

```
Work on atelier. Decompose this requirement:
"Add shoppable product tagging on user-posted videos"
```

The agent auto-loads atelier/context.md, atelier/memory/sessions.md, atelier/backlog.yaml,
then does the work, then appends to atelier/memory/sessions.md and atelier/memory/decisions.md.

---

## Folder structure

```
workspace/
├── CLAUDE.md                    ← you are here
├── MEMORY.md                    ← memory protocol (READ THIS)
├── .claude/
│   └── agents/                  ← Claude Code subagents (auto-discovered)
│       ├── product-lead.md
│       ├── product-design.md
│       └── product-tech.md
├── projects/                    ← one folder per product
│   └── _template/               ← copy to start a new project
│       ├── context.md
│       ├── backlog.yaml
│       ├── roadmap.yaml
│       ├── changelog.md
│       ├── memory/              ← project memory (persistent)
│       │   ├── decisions.md     ← decision log with reasoning
│       │   ├── learnings.md     ← what we've learned
│       │   ├── sessions.md      ← end-of-session summaries
│       │   ├── research/        ← user research, benchmarks
│       │   ├── experiments/     ← spike results, A/B tests
│       │   └── references/      ← inspiration, competitive intel
│       ├── design_system/
│       │   ├── tokens.yaml
│       │   └── components.yaml
│       ├── specs/
│       └── adr/
└── shared/                      ← reusable across projects
    ├── code_standards.md
    ├── accessibility_checklist.md
    └── skill_templates/
        └── artifacts.yaml
```

---

## Quickstart

### Start a new project

```bash
cp -r projects/_template projects/my_project
# Fill in projects/my_project/context.md
# Initialize backlog.yaml with first user stories
```

### Work on a project

```bash
claude    # launches Claude Code in this repo
```

Then in the conversation:

```
Use the product-lead agent to decompose this: "<your requirement>"
Project context is in projects/my_project/context.md.
```

Or just describe the task — Claude auto-routes to the right agent.

### Multi-agent workflow (sequential)

```
Use the product-lead agent to turn this requirement into user stories,
then use the product-design agent to design the first story,
then use the product-tech agent to assess feasibility.
```

Each subagent runs in its own context, returns a summary, and the next picks up from there.

---

## Enable Agent Teams (experimental, optional)

For direct agent-to-agent communication without passing through you:

Add to your Claude Code `settings.json`:
```json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }
```

Requires Claude Code v2.1.32 or later. Then agents can message each other directly via a shared task list.

---

## Shared resources

- `shared/code_standards.md` — transversal coding rules (consumed by product-tech)
- `shared/accessibility_checklist.md` — WCAG AA checklist (consumed by product-design and product-tech)
- `shared/skill_templates/artifacts.yaml` — YAML schemas for every inter-agent artifact

These are read on demand by agents when they need them.
