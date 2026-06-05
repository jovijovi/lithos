---
title: "Feature and Capability Tracker"
status: active
---
# Feature and Capability Tracker

This table is the unified feature/capability completion register for Granite. It tracks product features, implementation status, evidence, and next acceptance gates.

Status legend:

- **Done** — implemented and covered by tests/docs evidence.
- **Partial** — meaningful implementation exists, but acceptance is incomplete.
- **Planned** — product requirement accepted, implementation not started or not merged.
- **Parked** — intentionally outside current engineering sequence.
- **Non-goal** — explicitly not owned by this product.

| ID | Feature / capability | Product status | Implementation status | Evidence | Remaining acceptance |
|---|---|---|---|---|---|
| F-GOV-001 | Documentation-first authority chain | Required | Done | `GOAL.md`, `docs/product/prd.md`, `docs/design/architecture.md`, this file, `docs/roadmap/current-status.md`, `docs/AI_FLOW.md` | Maintain this chain as features/phases change |
| F-POLICY-001 | Policy-version validation | Required | Planned | PRD FR-1 | Add implementation and tests |
| F-FEE-001 | Fee rule evaluation | Required | Planned | PRD FR-2 | Add implementation and tests |
| F-SETTLEMENT-001 | Settlement-window classification | Required | Planned | PRD FR-3 | Add implementation and tests |
| F-NONGOAL-001 | Live settlement, payment-network calls, external delivery | Non-goal | Non-goal | PRD non-goals and `docs/AI_FLOW.md` gate 4 | Requires separate product approval |

## Completion roll-up

| Area | Done | Partial | Planned/Parked | Note |
|---|---:|---:|---:|---|
| Governance/docs | 1 | 0 | 0 | Authority chain established. |
| Core product | 0 | 0 | 3 | Product capabilities are planned. |

## Maintenance rule

Update this file whenever a feature's product requirement, implementation state, or acceptance evidence changes. Do not bury feature completion inside PR bodies, chat logs, or historical notes.
