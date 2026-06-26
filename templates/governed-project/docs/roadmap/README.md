---
title: "Roadmap directory"
status: active
created_at: 2026-06-05
---
# Roadmap Directory

`docs/roadmap/` owns roadmap, phase status, and feature tracking. Keep status records lean: this directory records phase authority, current decisions, open tails, acceptance criteria, and safety boundaries, not duplicate bookkeeping already proven by git history, CI, PR metadata, or generated artifacts.

`current-status.md` is the current-decision entrypoint, not a status database. If it starts carrying long phase history, full tail tables, evidence-path indexes, generated metadata, or repeated non-approval prose, split those details into named companion files such as `phase-ledger.md`, `tail-register.md`, `evidence-index.md`, `boundary-register.md`, or `reference-index.md`, and leave short pointers in `current-status.md`.

| Concern | Home |
|---|---|
| Product requirements | `../product/prd.md` |
| System architecture | `../design/architecture.md` |
| Technical design | `../design/technical-solution.md` |
| Feature completion tracking | `features.md` |
| Roadmap/current decision entrypoint | `current-status.md` |
| Long history, evidence, boundary, or reference detail | Companion files under `docs/roadmap/` when needed |
| Concrete task/phase implementation plans | `../plans/` |

Do not place step-by-step implementation plans in this directory. Use `docs/plans/YYYY-MM-DD-<task-slug>.md` for approved execution plans.
