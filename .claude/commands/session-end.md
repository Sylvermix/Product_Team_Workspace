# /session-end

Closes the current working session for a project by writing a session summary, logging decisions, and updating ALL documentation to reflect the session's work.

## Instructions

Follow these steps exactly, in order.

### Step 1 — Identify the project

If the user specified a project name in the command arguments, use it.
Otherwise, infer it from recent conversation context (files modified, stories mentioned).
If still unclear, ask: "Which project are we closing the session for?"

The project root is `projects/[name]/`.

### Step 2 — Read session context

Read the following files to reconstruct what happened this session:
- `projects/[name]/memory/sessions.md` — last 2 entries (to match the format and avoid duplication)
- `projects/[name]/memory/decisions.md` — first 30 lines (most recent entries already logged)
- `projects/[name]/backlog.yaml` — current state
- Any files modified during this session (infer from conversation)

### Step 3 — Write the session summary

Append to `projects/[name]/memory/sessions.md` at the TOP (after the header, before the previous entry). Use this exact format:

```markdown
## YYYY-MM-DD — [agent/human] — [Short session title, max 10 words]

**Task**: one sentence — what was the user's goal for this session

**Worked on**:
- Bullet list of specific stories, specs, files, or artifacts touched

**Outcome**:
- Bullet list of what was delivered or changed state

**Decisions made**:
- List decisions with a one-line summary each. Write "See decisions.md entries dated YYYY-MM-DD" if already logged there.
- Write "None" if no decisions were made.

**Open questions / next steps**:
- Bullet list of what the next session should pick up first
- Any blockers or pending human decisions

**Files changed**:
- List every file created or modified, one per line
```

Rules:
- Date is today: $CURRENT_DATE
- Keep each section tight — no padding, no repetition
- If a decision was already logged in `decisions.md` during the session, reference it here rather than restating it in full
- Latest entry always goes at the TOP of the file, right after the `---` separator following the header

### Step 4 — Log pending decisions

Review the conversation. For every significant decision made during this session that is NOT yet in `projects/[name]/memory/decisions.md`, append it now using this format:

```markdown
## YYYY-MM-DD — [Short title]

**Who decided**: Product Builder / agent
**Context**: what was the situation that prompted this decision
**Options considered**:
- Option A: ... (chosen/rejected because...)
- Option B: ...
**Decision**: what was chosen, in one clear sentence
**Consequences**: what this changes or enables
**Revisit if**: condition that would reopen this decision
```

Rules:
- Only log decisions that are not already present
- A "significant decision" is: scope change, architecture/stack choice, aesthetic commitment, anything expensive to reverse, anything that resolves a prior ambiguity
- Conversational clarifications that don't affect the product are NOT decisions

### Step 5 — Full documentation sweep

Review every category below. For each file: read it, ask "is it still accurate given what happened this session?", update it if stale, skip it if unchanged. **Do not update files just to add timestamps — only update when content changed.**

#### 5a — Project core files

| File | Update if... |
|---|---|
| `projects/[name]/context.md` | Vision, audience, stack, constraints, priorities, or access model changed |
| `projects/[name]/backlog.yaml` | Story status changed, new stories captured, priorities shifted, spikes resolved |
| `projects/[name]/roadmap.yaml` | Sprint goal, milestone dates, or candidate stories changed |
| `projects/[name]/changelog.md` | A story or feature was completed and shipped this session |

#### 5b — Memory files

| File | Update if... |
|---|---|
| `projects/[name]/memory/learnings.md` | A non-obvious insight was confirmed or disproved (user behavior, tech constraint, design assumption) |
| `projects/[name]/memory/decisions.md` | Already handled in Step 4 |
| `projects/[name]/memory/sessions.md` | Already handled in Step 3 |
| `projects/[name]/memory/research/` | New research, benchmarks, or interview data was collected |
| `projects/[name]/memory/experiments/` | A spike or experiment produced results |
| `projects/[name]/memory/references/` | A useful reference was identified |

#### 5c — Design system

| File | Update if... |
|---|---|
| `projects/[name]/design_system/tokens.yaml` | New tokens were identified, existing tokens were modified or removed |
| `projects/[name]/design_system/components.yaml` | New components were identified or specified |

#### 5d — Specs

| File | Update if... |
|---|---|
| `projects/[name]/specs/**` | A decision this session changed a spec's content, flow, or acceptance criteria |

Only update specs that were directly affected — do not sweep all specs.

#### 5e — Diagrams

| Diagram | Update if... |
|---|---|
| `projects/[name]/docs/diagrams/team-agents.md` | Team roles, responsibilities, or skills changed |
| `projects/[name]/docs/diagrams/onboarding-flow.md` | Onboarding flow, beats, or account gating changed |
| `projects/[name]/docs/diagrams/scan-states.md` | Scan flow states, intents, or error handling changed |
| `projects/[name]/docs/diagrams/user-access-model.md` | Permissions table, anonymous vs logged-in model changed |
| `projects/[name]/docs/diagrams/epic-dependencies.md` | New epics added, dependencies changed, stories moved |
| `projects/[name]/docs/diagrams/technical-architecture.md` | Stack, pipeline, ERD, budget, or infra decisions changed |

Update `Last updated:` date on any diagram you modify.

#### 5f — Tier 2 agent memory (cross-project patterns)

For each agent active this session, check if the session produced a reusable insight worth appending to their memory file in `shared/agent-memory/`:

| Agent | File | What to log |
|---|---|---|
| product-lead | `shared/agent-memory/product-lead.md` | Prioritization heuristics, estimation patterns, discovery shortcuts |
| product-design | `shared/agent-memory/product-design.md` | Aesthetic patterns, accessibility edge cases, motion principles |
| product-tech | `shared/agent-memory/product-tech.md` | Code patterns, API quirks, tooling preferences, performance tricks |

Format (append at top, after the header):
```markdown
## YYYY-MM-DD — [Project] — [Short title]

**Context**: one sentence on where this came from
**Pattern**: what was learned or confirmed, stated as a reusable rule
**Evidence**: what in this session supports it
**Applies to**: which types of projects or situations this generalises to
```

Only append if there is a genuinely reusable insight — not every session produces one.

#### 5g — Workspace-level files

| File | Update if... |
|---|---|
| `CLAUDE.md` | Team principles, folder structure, or skill list changed |
| `.claude/agents/product-lead.md` | Lead's protocols, tools, or responsibilities changed |
| `.claude/agents/product-design.md` | Design's protocols, tools, or responsibilities changed |
| `.claude/agents/product-tech.md` | Tech's protocols, tools, or responsibilities changed |
| `shared/code_standards.md` | A new coding rule or pattern was established |
| `shared/accessibility_checklist.md` | A new accessibility finding or rule was confirmed |

These change rarely — only update if the session explicitly changed something at this level.

### Step 6 — Commit, merge into main, and push

Stage ALL files changed during this session (memory + docs + any updated files):
```
git add -A
git commit -m "docs([name]): session summary YYYY-MM-DD — [short title]"
git push -u origin [current-branch]
```

Then merge the session branch into main and push:
```
git checkout main
git merge [current-branch] --no-edit
git push origin main
git checkout [current-branch]
```

If the merge produces conflicts, stop and ask the user to resolve them before continuing.

### Step 7 — Confirm to the user

Print a short summary:
- Session title
- Files updated in the documentation sweep (by category)
- Number of decisions logged
- Tier 2 entries added (or "none")
- Branch merged into main: yes/no
- What the next session should start with (top open question)
