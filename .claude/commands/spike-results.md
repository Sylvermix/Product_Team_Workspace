# /spike-results

Captures the results of a completed spike or discovery experiment, updates the backlog accordingly, and logs everything to memory.

## Instructions

Follow these steps exactly, in order.

### Step 1 — Identify the spike and project

If the user specified a spike ID (e.g. `SPIKE-001`) and project in the arguments, use them.
Otherwise ask: "Which spike are we closing, and for which project?"

Read the spike entry from `projects/[name]/backlog.yaml` to get the hypothesis, deliverables, and what it blocks.

### Step 2 — Collect results

Ask the user to provide (or infer from conversation context):
- **Match rate / key metric**: the primary measurement (e.g. "78% top-3 match rate")
- **Cost**: per-unit cost if applicable (e.g. "$0.018 per scan")
- **Pass / Fail / Partial**: did it meet the exit criteria defined in the spike?
- **Key findings**: what worked, what didn't, surprises
- **Recommendation**: proceed / pivot / run fallback pipeline

### Step 3 — Write the experiment file

Create `projects/[name]/memory/experiments/[date]_spike_[id]-results.md`:

```markdown
# [SPIKE-ID] Results — [Short title]
Date: YYYY-MM-DD
Hypothesis: [copy from backlog.yaml]

## Verdict: PASS / FAIL / PARTIAL

## Key metric
[Primary measurement vs exit criteria]

## Findings
### What worked
- bullet list

### What didn't
- bullet list

### Surprises
- bullet list

## Cost
[Cost per unit / total cost of spike]

## Recommendation
[One paragraph: what we do next and why]

## Blocked stories now unblocked (or cancelled)
- [US-XXX]: [ready / cancelled — reason]
```

### Step 4 — Update backlog.yaml

Based on the verdict:

**PASS**:
- Move spike from `discovery` to `done`
- For each blocked story: change status from `blocked` to `ready`
- Update confidence score on unblocked stories if it changed

**FAIL**:
- Move spike to `done` with `outcome: failed`
- For each blocked story: either move to `icebox` with reason, or create a new spike

**PARTIAL**:
- Document partial result
- Create a follow-up spike entry if needed
- Leave blocked stories as `blocked` until follow-up completes

### Step 5 — Sync GitHub issues

- Update the spike GitHub issue: add results summary as a comment, close the issue (`state_reason: completed` for pass, `not_planned` for fail)
- For each unblocked story: update its GitHub issue label from `status: blocked` to `status: ready`
- For each cancelled story: close its GitHub issue with `state_reason: not_planned` and a comment explaining the spike outcome

### Step 6 — Log to memory

Append to `projects/[name]/memory/decisions.md`:

```markdown
## YYYY-MM-DD — [SPIKE-ID] verdict: [PASS/FAIL/PARTIAL]

**Who decided**: tech + human owner (based on spike results)
**Decision**: [proceed with US-XXX / pivot to fallback / cancel]
**Evidence**: [key metric] — [pass/fail vs threshold]
**Consequences**: [what's now unblocked or cancelled]
**Revisit if**: [condition that would reopen]
```

### Step 7 — Commit and push

```
git add projects/[name]/memory/experiments/ projects/[name]/backlog.yaml projects/[name]/memory/decisions.md
git commit -m "feat([name]): [SPIKE-ID] results — [PASS/FAIL] — [key metric]"
git push -u origin [current-branch]
```

### Step 8 — Confirm to the user

Print:
- Verdict + key metric
- Stories now unblocked (or cancelled)
- Next action recommended
