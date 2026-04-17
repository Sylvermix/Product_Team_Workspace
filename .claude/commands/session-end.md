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

### Step 5 — Commit and push

Stage and commit all memory files changed:
```
git add projects/[name]/memory/sessions.md projects/[name]/memory/decisions.md
git commit -m "docs([name]): session summary YYYY-MM-DD — [short title]"
git push -u origin [current-branch]
```

### Step 6 — Confirm to the user

Print a short summary:
- Session title
- Number of decisions logged
- Files committed
- What the next session should start with (top open question)
