# Code Standards

Transversal coding rules for the Tech agent. Project-specific stack details live in `projects/[name]/context.md`; these rules apply everywhere.

---

## Naming

- Descriptive names over short names: `userEmailAddress` not `uem`
- No Hungarian notation: `isActive` not `bIsActive`
- Boolean prefixes: `is`, `has`, `can`, `should`
- Functions are verbs: `calculateTotal()`, `sendEmail()`
- Classes/types are nouns: `User`, `OrderService`
- Constants in SCREAMING_SNAKE: `MAX_RETRY_COUNT`
- Avoid abbreviations unless industry-standard (URL, HTML, ID)

---

## Function design

- Single responsibility — one function does one thing
- Max 50 lines; if longer, extract
- Max 4 parameters; if more, pass an options object
- No side effects where a pure function would work
- Early returns over deep nesting
- Explicit return types in typed languages

---

## File organization

- Max 400 lines per file; if longer, split by concept
- One primary export per file (the name matches the file)
- Co-locate tests: `user.ts` + `user.test.ts` in same folder
- Barrel exports (`index.ts`) only at package boundaries, not for internal folders

---

## Error handling

- Never swallow errors silently. Either:
  - Handle and log (with context), or
  - Rethrow (wrap with more context if useful)
- Errors include: what failed, inputs, what was expected
- Use typed errors where the language supports it
- Async: every `await` is either inside try/catch or has a `.catch()` upstream

---

## Tests

- Coverage target: 80%+ on business logic, 100% on security-critical paths
- Structure: `describe` for the unit, `it('should...')` for behavior
- One assertion per test where possible
- Given/When/Then structure for complex tests
- No logic in tests (no loops, no conditions) — test code should be obvious
- Test names describe behavior, not implementation: `should reject invalid email` not `test_email_regex`

---

## Dependencies

Every new dependency requires justification:
- **Size**: bundle impact (check with bundlephobia or equivalent)
- **Maintenance**: last release date, open issues, maintainer activity
- **License**: must be compatible with project license
- **Alternative**: was a standard library or existing dep considered?

Document justification in ADR if non-trivial.

---

## Comments

- Explain *why*, not *what*. The code shows what.
- ❌ `// increment counter` before `counter++`
- ✅ `// retry up to 3 times because upstream API is flaky`
- TODO/FIXME must include: owner + issue ticket. Bare TODOs are banned.
- JSDoc/docstrings for public APIs only (not internal functions)

---

## Performance

- No premature optimization without measurement
- Benchmark before optimizing
- Watch for: N+1 queries, synchronous I/O on hot paths, unnecessary re-renders
- Define performance budgets per feature in spec; verify before ship

---

## Security

- Input validation at every boundary (API, forms, URL params)
- Never log: passwords, tokens, PII beyond what's necessary
- No secrets in code or config committed to repo — use env vars / secret manager
- SQL: parameterized queries only
- HTML: never inject user input without sanitization
- HTTPS everywhere; HSTS headers in production

---

## Git hygiene

- Commit messages: imperative mood, reference story ID
  - `US-101: Add guest checkout button`
- One logical change per commit; squash exploratory commits before merge
- PRs under 400 lines of real change; larger → split
- PR description: what, why, testing done, screenshots for UI changes

---

## Feature flags

- Every flag has an owner and expiration date
- "Temporary" flags that live past their expiration become technical debt tickets
- Flags are removed after full rollout — no zombie flags

---

## Documentation that must exist

- **API docs**: auto-generated from code where possible; hand-written where not
- **Architecture decision records (ADR)**: one per significant decision (see `adr/` folder)
- **Setup / onboarding**: a new developer can run the project locally in under 30 minutes
- **Runbook**: for production incidents — how to diagnose, rollback, escalate

---

## Anti-patterns (never do this)

- Silent catch blocks
- Magic numbers / strings without named constants
- Copy-paste instead of extract
- God objects / god functions
- `// TODO: fix later` without a ticket
- Committing commented-out code
- Using `any` / `unknown` to escape type checking
- Mocking the thing under test
- Relying on implementation details in tests
- Coupling business logic to framework code (keep domain pure)
