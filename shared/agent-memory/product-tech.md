# Agent Memory — Product Tech

Cross-project code patterns, recurring bugs, tooling preferences, and technical heuristics accumulated over time.
Append-only. Latest entries at top.

---

## 2026-04-17 — Atelier — Séparer I/O et calcul dans les fonctions de métriques go/no-go

**Context**: scaffolding du harness SPIKE-001 — la fonction `compute_metrics()` conduit la décision pass/fail du spike
**Pattern**: les fonctions qui produisent une décision go/no-go doivent être pures (aucun I/O, aucun accès fichier) — elles reçoivent des données, retournent un dict. Les helpers internes (`_safe_rate`, `_percentile`) sont testés séparément pour atteindre 100% de coverage sans mocker le filesystem.
**Evidence**: `metrics.py` entièrement pur → 32 tests passants sans aucun mock I/O ; `run_eval.py` séparé gère tout le filesystem
**Applies to**: tout projet avec une fonction de scoring ou de validation qui doit être testable à 100% et auditée facilement

<!-- Entries added by the agent after each session where a reusable pattern is identified -->
