# AI Product Team Workspace

A shared team of AI agents (Lead, Design, Tech) that works across multiple digital product projects. The agents are defined once and carry their principles across every project; each project provides its own context, backlog, and state.

---

## Folder structure

```
workspace/
├── README.md                    ← you are here
│
├── team/                        ← agent definitions (shared across all projects)
│   ├── agent_lead.md            ← Product Builder
│   ├── agent_design.md          ← Designer
│   ├── agent_tech.md            ← Developer
│   └── team_principles.md       ← transversal values
│
├── projects/                    ← one folder per product
│   ├── _template/               ← copy this to start a new project
│   │   ├── context.md           ← vision, audience, stack, constraints
│   │   ├── backlog.yaml         ← prioritized user stories
│   │   ├── roadmap.yaml         ← current + upcoming milestones
│   │   ├── changelog.md         ← history of shipped work
│   │   ├── design_system/       ← tokens + components for this project
│   │   ├── specs/               ← feature specs (mockups, design + tech)
│   │   └── adr/                 ← architecture decision records
│   │
│   ├── project_alpha/           ← your first real project
│   └── project_beta/            ← another project
│
└── shared/                      ← reusable across projects
    ├── code_standards.md        ← transversal coding standards
    ├── accessibility_checklist.md
    └── skill_templates/         ← YAML schemas for agent artifacts
        └── artifacts.yaml
```

---

## How to start a new project

1. Copy `projects/_template/` → `projects/your_project_name/`
2. Fill in `context.md` (vision, audience, stack, constraints)
3. Customize `design_system/tokens.yaml` with project-specific design tokens
4. Initialize `backlog.yaml` with first user stories
5. Start your first session (see below)

---

## How to start a work session

When you start a session with an agent, load this context in order:

1. **Agent definition** — `team/agent_[lead|design|tech].md`
2. **Team principles** — `team/team_principles.md`
3. **Project context** — `projects/[project_name]/context.md`
4. **Current state** — relevant files from the project (backlog, current specs, etc.)

Example prompt to start a Design session:

```
You are the Design agent defined in team/agent_design.md.
Team principles: team/team_principles.md.
Today you're working on project_alpha — context in projects/project_alpha/context.md.
Current backlog: projects/project_alpha/backlog.yaml.
Task: design the onboarding flow (US-101).
```

---

## Single source of truth rules

- **Agent definitions** live in `team/` — never duplicated per project. Improvements flow to all projects.
- **Project context** lives in `projects/[name]/context.md` — everything project-specific goes here, not in the agent files.
- **Design system** lives in `projects/[name]/design_system/` — each project has its own, but structure follows `shared/` templates.
- **Backlog** is authoritative. If work isn't in `backlog.yaml`, it's not being built.
- **Changelog** is append-only. Every shipped story gets an entry.

---

## How agents work together across projects

The same agent (e.g. Design) can work on project_alpha in the morning and project_beta in the afternoon. What changes between sessions:

- The **project context** (loaded at session start)
- The **state files** (backlog, design system, specs)

What stays the same:

- The agent's **identity, skills, hooks, guardrails** (from `team/`)
- The **team principles** (from `team/team_principles.md`)
- The **transversal standards** (from `shared/`)

---

## Versioning recommendation

Put this whole workspace in Git. Every change (new spec, shipped story, updated design token) is a commit. You get history, diff, branching, and easy collaboration.
