# AI Product Team Workspace

A Claude Code multi-agent workspace: three AI agents (Lead, Design, Tech) work across multiple digital product projects.

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

Then in the Claude Code session:

```
Use the product-lead agent to decompose this requirement:
"Add guest checkout to reduce cart abandonment"

Project: projects/_template (copy to projects/my_project first)
```

## What's where

- **`CLAUDE.md`** — team principles and routing rules, auto-loaded by Claude Code every session
- **`.claude/agents/`** — the three subagents, auto-discovered by Claude Code
- **`projects/`** — one folder per product, copy `_template` to start a new one
- **`shared/`** — transversal standards (code, accessibility) and artifact schemas
- **`GIT_SETUP.md`** — how to push this to GitHub/GitLab

## Agents

| Agent | Role | When Claude uses it |
|---|---|---|
| `product-lead` | Product Builder | Decomposing requirements, prioritizing, validating deliverables, arbitrating |
| `product-design` | Designer | Mockups, design system, journeys, accessibility |
| `product-tech` | Developer | Implementation, tests, deployments, refactoring |

Full definitions in `.claude/agents/product-*.md` — each has Identity, Context, Skills, Hooks, I/O Contracts, Memory, Guardrails.

## Adding a project

```bash
cp -r projects/_template projects/my_project
# Edit projects/my_project/context.md with vision, stack, constraints
# Initialize backlog.yaml with first user stories
```

## More docs

- `CLAUDE.md` — detailed workspace guide (team principles, workflow, agent teams)
- `GIT_SETUP.md` — push to a remote, branching strategy
- `.claude/agents/*.md` — full agent definitions
