# Accessibility Checklist (WCAG 2.1 AA)

Minimum bar for every project. Used by Design agent during `audit_accessibility` and by Tech agent before any merge.

---

## Color & contrast

- [ ] Text contrast ≥ 4.5:1 (body text)
- [ ] Large text contrast ≥ 3:1 (18px+ regular or 14px+ bold)
- [ ] UI component contrast ≥ 3:1 (borders, icons, form controls)
- [ ] Information never conveyed by color alone (use icon + text)
- [ ] Focus indicator contrast ≥ 3:1 against adjacent colors

---

## Typography

- [ ] Body text minimum 16px
- [ ] Line height ≥ 1.5 for body text
- [ ] Paragraph spacing ≥ 2x line height
- [ ] Line length ≤ 80 characters for long-form reading
- [ ] Text resizable to 200% without loss of content or function

---

## Touch & click targets

- [ ] Interactive targets ≥ 44×44px (mobile)
- [ ] Targets ≥ 24×24px with 8px+ spacing (desktop)
- [ ] No overlapping interactive regions

---

## Keyboard navigation

- [ ] Every interactive element reachable by Tab
- [ ] Tab order is logical (matches visual order)
- [ ] Focus always visible (never `outline: none` without replacement)
- [ ] No keyboard traps (Esc or similar always exits modals/dropdowns)
- [ ] Skip-to-content link at top of page
- [ ] Keyboard shortcuts (if any) documented and non-conflicting

---

## Screen reader support

- [ ] Every image has `alt` text (or `alt=""` if decorative)
- [ ] Icons with meaning have `aria-label`; purely decorative icons have `aria-hidden="true"`
- [ ] Form inputs have associated `<label>` (not just placeholder)
- [ ] Buttons describe action: "Delete account" not "Submit"
- [ ] Dynamic content changes announced (`aria-live` for updates)
- [ ] Headings are hierarchical (h1 → h2 → h3, no skipping)
- [ ] Landmarks used: `<header>`, `<nav>`, `<main>`, `<footer>`

---

## Forms

- [ ] Every input has a visible label
- [ ] Required fields marked with text (not just *)
- [ ] Error messages specific and helpful ("Email must contain @" not "Invalid")
- [ ] Errors announced to screen readers (`aria-invalid`, `aria-describedby`)
- [ ] Autocomplete attributes on common fields (`autocomplete="email"`, etc.)
- [ ] No auto-submit on input change without explicit user action

---

## Motion & animation

- [ ] `prefers-reduced-motion` honored for all non-essential animation
- [ ] No animation that flashes > 3 times per second (seizure risk)
- [ ] Auto-playing video/animation can be paused
- [ ] Parallax / large movement has a reduced-motion alternative

---

## Media

- [ ] Videos have captions
- [ ] Audio-only content has transcript
- [ ] No auto-playing audio with sound
- [ ] Media controls keyboard-accessible

---

## Content structure

- [ ] Page has a unique, descriptive `<title>`
- [ ] Language declared (`<html lang="en">`)
- [ ] Reading order matches DOM order (no tab-index tricks)
- [ ] ARIA used only when HTML semantics insufficient (HTML first)

---

## Responsive & zoom

- [ ] Content usable at 320px wide (mobile)
- [ ] No horizontal scroll at standard viewport sizes
- [ ] Content usable at 400% zoom without loss
- [ ] Orientation (portrait/landscape) not required

---

## Testing

- [ ] Automated check: axe DevTools / Lighthouse (0 critical issues)
- [ ] Keyboard-only test: complete the primary user task
- [ ] Screen reader test: primary flow with NVDA (Windows) or VoiceOver (Mac)
- [ ] Zoom test: 400% zoom, content still usable
- [ ] Reduced motion test: toggle OS setting, verify

---

## When AA isn't enough

Some contexts require AAA or additional standards:
- **Government / public sector**: check local law (EN 301 549 in EU, Section 508 in US)
- **Healthcare**: HIPAA interactions with accessibility
- **Financial**: often legally required to meet AA minimum

If project falls in these categories, document in `projects/[name]/context.md` under Constraints.
