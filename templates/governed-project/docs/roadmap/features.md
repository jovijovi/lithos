---
title: "Feature and Capability Tracker"
status: active
created_at: 2026-06-05
---
# Feature and Capability Tracker

This table is the unified feature/capability completion register for `[Project Name]`. It tracks product features, implementation status, evidence, and next acceptance gates.

Status legend:

- **Done** — implemented and covered by tests/docs evidence.
- **Partial** — meaningful implementation exists, but acceptance is incomplete.
- **Planned** — product requirement accepted, implementation not started or not merged.
- **Parked** — intentionally outside current engineering sequence.
- **Non-goal** — explicitly not owned by this product.

| ID | Feature / capability | Product status | Implementation status | Evidence | Remaining acceptance |
|---|---|---|---|---|---|
| F-GOV-001 | Documentation-first authority chain: GOAL -> PRD -> design -> feature tracker -> roadmap/status -> phase plans | Required | Planned | `GOAL.md`, `docs/product/prd.md`, `docs/design/architecture.md`, this file, `docs/roadmap/current-status.md` | Maintain this chain as features/phases change |
| F-CORE-001 | [Core capability] | Required | Planned | [Evidence path] | [Remaining acceptance] |
| F-NONGOAL-001 | Live/default-on behavior not approved by this project | Non-goal | Non-goal | PRD non-goals and `docs/AI_FLOW.md` gate 4 | Requires separate owner approval and product docs change |

## Completion roll-up

| Area | Done | Partial | Planned/Parked | Note |
|---|---:|---:|---:|---|
| Governance/docs | 0 | 0 | 1 | Authority chain is being established. |
| Core product | 0 | 0 | 1 | Replace with project-specific rows. |

## Maintenance rule

Update this file whenever a feature's product requirement, implementation state, or acceptance evidence changes. Do not bury feature completion inside PR bodies, chat logs, or historical notes.
