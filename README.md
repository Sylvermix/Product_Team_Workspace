# AI Product Team Workspace

A Claude Code multi-agent workspace: three AI agents (Lead, Design, Tech) work across multiple digital product projects, with persistent memory in each project.

## Quickstart

```bash
# Clone this repo
git clone <your-remote-url>
cd <repo-name>

# Install Claude Code if you don't have it
npm install -g @anthropic-ai/claude-code

# Launch
claude
```

In the Claude Code session:

```
Use the product-lead agent to decompose this requirement:
"<your requirement>"

Project: projects/my_project
```

## What's where

- **`CLAUDE.md`** — team principles and routing rules, auto-loaded by Claude Code every session
- **`MEMORY.md`** — memory protocol: how agents read/write persistent memory
- **`.claude/agents/`** — the three subagents, auto-discovered by Claude Code
- **`projects/`** — one folder per product. Every project has the same structure
- **`shared/`** — transversal standards (code, accessibility) and artifact schemas
- **`GIT_SETUP.md`** — how to push this to GitHub/GitLab

## Agents

| Agent | Role | When Claude uses it |
|---|---|---|
| `product-lead` | Product Builder | Decomposing requirements, prioritizing, validating deliverables, arbitrating |
| `product-design` | Designer | Mockups, design system, journeys, accessibility |
| `product-tech` | Developer | Implementation, tests, deployments, refactoring |

Full definitions in `.claude/agents/product-*.md` — each has Identity, Context, Skills, Hooks, I/O Contracts, Memory, Guardrails.

## Every project inherits the same structure

When you create a new project, it inherits everything from `projects/_template/`:

```
projects/[name]/
├── README.md                    ← project overview
├── context.md                   ← vision, audience, aesthetic, stack, constraints
├── backlog.yaml                 ← prioritized user stories
├── roadmap.yaml                 ← sprint plan + milestones
├── changelog.md                 ← shipped history (append-only)
├── memory/                      ← persistent memory
│   ├── decisions.md             ← decision log with reasoning
│   ├── learnings.md             ← what we've learned
│   ├── sessions.md              ← end-of-session summaries
│   ├── research/                ← user research, benchmarks
│   ├── experiments/             ← spike results, A/B tests
│   └── references/              ← inspiration, competitive intel
├── design_system/               ← project-specific tokens + components
│   ├── tokens.yaml
│   └── components.yaml
├── specs/                       ← feature specs
└── adr/                         ← architecture decision records
```

**Every project gets the full memory system automatically**. No setup required — just copy the template.

## Adding a new project

```bash
# Copy the template — everything including memory comes with it
cp -r projects/_template projects/my_project

# Then start a session with the Lead agent
claude
```

In the Claude Code session:

```
> Initialize projects/my_project. The project is: [describe your idea]
```

The Lead agent will:
1. Fill in `context.md` with vision, audience, stack, constraints
2. Customize `design_system/tokens.yaml` for the aesthetic
3. Seed `backlog.yaml` with first user stories
4. Log initial decisions in `memory/decisions.md`
5. Capture open hypotheses in `memory/learnings.md`
6. Write the kickoff summary in `memory/sessions.md`

## Memory: the key to continuity

Agents have no native memory between sessions. **The file system IS the memory.**

- Every significant decision → logged in the project's `memory/decisions.md`
- Every learning → logged in `memory/learnings.md`
- Every session → summarized in `memory/sessions.md`
- Every piece of data collected → stored in `memory/research/` or `memory/experiments/`

This applies to **every project**, not just specific ones. It's enforced by the protocol in `MEMORY.md` and by the agent definitions in `CLAUDE.md`.

## More docs

- `CLAUDE.md` — detailed workspace guide (principles, routing, memory loading)
- `MEMORY.md` — full memory protocol with templates and anti-patterns
- `GIT_SETUP.md` — push to a remote, branching strategy
- `.claude/agents/*.md` — full agent definitions
