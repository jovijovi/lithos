---
title: "Granite Roadmap Current Status"
status: active
created_at: 2026-06-05
---
# Granite Roadmap Current Status

> Living roadmap, phase tracker, and implementation-stage acceptance register.

```text
last_updated: 2026-06-05
base_branch: main
product_role: local payments-domain rules library with deterministic decision evidence
source_of_truth: GOAL.md, docs/product/prd.md, docs/design/architecture.md, docs/design/technical-solution.md, docs/roadmap/features.md, docs/roadmap/current-status.md, docs/AI_FLOW.md
current_mainline: R0 documentation authority baseline is established in this worked example; product implementation remains planned
```

## 1. How to read this roadmap

The document hierarchy is:

```text
PRD -> design docs -> roadmap/current-status + feature tracker -> approved phase implementation plan in docs/plans/
```

- `GOAL.md` defines stable product positioning and points to source-of-truth docs.
- `docs/product/prd.md` defines product requirements.
- `docs/design/architecture.md` gives the system-level architecture.
- `docs/design/technical-solution.md` defines the module-level technical solution.
- `docs/roadmap/features.md` tracks feature/capability completion.
- This file tracks engineering phases, status, tails, and acceptance criteria.
- Per-phase implementation plans live under `docs/plans/` named `YYYY-MM-DD-<task-slug>.md`.

## 2. Current decision

```text
Granite is currently a governed documentation example. R0 is complete as an example baseline. F-POLICY-001, F-FEE-001, and F-SETTLEMENT-001 remain planned and require separate implementation approval.
```

## 3. Phase roadmap

### R0 — Documentation authority baseline

Goal: establish the governed source-of-truth chain and prevent implementation from drifting away from product intent.

Checklist:

- [x] Create `GOAL.md`.
- [x] Create `docs/product/prd.md`.
- [x] Create `docs/design/architecture.md`.
- [x] Create `docs/design/technical-solution.md`.
- [x] Create `docs/roadmap/features.md`.
- [x] Create this file.
- [x] Create `docs/AI_FLOW.md`.

Acceptance:

- Docs show a complete authority chain.
- Product requirements, design, and roadmap agree on current scope.
- No document implies live settlement, payment-network calls, or release publication.

Status: Complete for the worked example.

## 4. Tail register

| Tail | Class | Owner | Gate | Acceptance method |
|---|---|---|---|---|
| Implement policy-version validation | NEXT_PHASE | Maintainers | Implementation | Tests and feature tracker update |
| Implement fee rule evaluation | NEXT_PHASE | Maintainers | Implementation | Tests and feature tracker update |
| Implement settlement-window classification | NEXT_PHASE | Maintainers | Implementation | Tests and feature tracker update |

## 5. Standing non-approvals

Unless explicitly approved in a later phase, Granite does not authorize:

- live settlement;
- payment-network calls;
- production configuration mutation;
- external delivery;
- destructive repository actions;
- publishing packages or releases.
