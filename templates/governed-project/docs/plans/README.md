---
title: "Implementation plans directory"
status: active
---
# Implementation plans directory

`docs/plans/` holds concrete, task- or phase-level implementation plans. A plan here is an execution artifact: it says how an already-approved phase will be built, tested, and verified. It is not a place to define or change product scope.

## What lives here vs. in `docs/roadmap/`

| Concern | Home |
|---|---|
| Product requirements | `../product/prd.md` |
| Technical design | `../design/technical-solution.md` |
| Feature/capability completion tracking | `../roadmap/features.md` |
| Roadmap, phase status, phase acceptance criteria | `../roadmap/current-status.md` |
| Concrete task/phase implementation plans | `docs/plans/` |

`docs/roadmap/` owns roadmap, status, and feature tracking. It does not own task-level execution plans.

## Naming convention

Every plan file is named:

```text
docs/plans/YYYY-MM-DD-<task-slug>.md
```

## Rules for new plans

- A plan must derive from `docs/product/prd.md`, `docs/design/technical-solution.md`, and `docs/roadmap/current-status.md`.
- A plan must trace back to an approved roadmap phase.
- A plan must not redefine product goals, expand product scope, or weaken the PRD/design.
- A plan must not imply new live/runtime approvals.
- Per `docs/AI_FLOW.md`, a plan must include context, implementation checklist, acceptance criteria, likely files, verification gates, risks, and rollback strategy.

## Historical artifacts are non-authoritative

Old plans, chat summaries, and dev notes may be useful context, but they are not source-of-truth unless promoted into the current authority chain.
