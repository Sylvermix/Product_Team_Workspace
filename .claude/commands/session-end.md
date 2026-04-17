# /session-end

Closes the current working session for a project by writing a session summary and logging all decisions made.

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
- `projects/[name]/memory/decisions.md` — first 30 lines (to see the most recent entries already logged)
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

**Who decided**: agent / human owner
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

### Step 5 — Update Tier 2 agent memory

Tier 2 memory lives in `shared/agent-memory/`. It stores **cross-project, reusable** patterns — not project-specific decisions (those go in `decisions.md`).

For each agent that was active this session, check if the session produced any reusable insight worth appending to their memory file:

| Agent | File | What to log |
|---|---|---|
| product-lead | `shared/agent-memory/product-lead.md` | Prioritization heuristics, estimation patterns, discovery shortcuts, recurring stakeholder dynamics |
| product-design | `shared/agent-memory/product-design.md` | Aesthetic patterns that worked, accessibility edge cases, component combinations, motion principles |
| product-tech | `shared/agent-memory/product-tech.md` | Code patterns, recurring bugs, tooling preferences, API quirks, performance tricks |

**Format for each entry** (append at top of the relevant file, after the header):

```markdown
## YYYY-MM-DD — [Project] — [Short title]

**Context**: one sentence on where this came from
**Pattern**: what was learned or confirmed, stated as a reusable rule
**Evidence**: what in this session supports it
**Applies to**: which types of projects or situations this generalises to
```

**Rules**:
- Only append if there is a genuinely reusable insight — not every session produces one
- Do NOT copy project-specific decisions here — those stay in `decisions.md`
- If nothing reusable was learned, skip this step entirely (write nothing)

### Step 6 — Commit and push

Stage and commit all memory files changed:
```
git add projects/[name]/memory/sessions.md projects/[name]/memory/decisions.md shared/agent-memory/
git commit -m "docs([name]): session summary YYYY-MM-DD — [short title]"
git push -u origin [current-branch]
```

### Step 7 — Confirm to the user

Print a short summary:
- Session title
- Number of decisions logged
- Tier 2 entries added (or "none" if nothing reusable)
- Files committed
- What the next session should start with (top open question)
