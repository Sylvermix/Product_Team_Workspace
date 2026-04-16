# Sessions — [PROJECT NAME]

End-of-session summaries. Latest at top.

**Read the last 2-3 entries at the start of every session** — this is how agents pick up cleanly from where the previous session ended.

**Write a new entry at the end of every session**, even if the user doesn't ask for one.

See `../../MEMORY.md` for format.

---

## What to include

- **Task**: what the user asked for in their prompt
- **Worked on**: specific stories, files, artifacts touched
- **Outcome**: what is now in a different state than when the session started
- **Decisions made**: link to entries in `decisions.md` (don't duplicate the content)
- **Open questions / next steps**: what the next session should pick up
- **Files changed**: explicit list of files created or modified

## Length

Keep it tight — 5-10 bullet points per session. The goal is fast re-orientation, not a novel. If details matter, link to the artifact (spec, ADR, decision entry).

---

<!-- Template — copy this block for each session:

## YYYY-MM-DD — [agent-name] — [Short session title]

**Task**: what the user asked
**Worked on**: specific items
**Outcome**: what changed
**Decisions made**:
- [link to decisions.md entry]
**Open questions / next steps**:
- [what's blocking or waiting]
- [what should be picked up next]
**Files changed**:
- created: [file paths]
- modified: [file paths]

-->
