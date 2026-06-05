---
title: "[Project Name] Roadmap Current Status"
status: active
---
# [Project Name] Roadmap Current Status

> Living roadmap, phase tracker, and implementation-stage acceptance register.

```text
last_updated: [YYYY-MM-DD]
base_branch: main
product_role: [stable product role]
source_of_truth: GOAL.md, docs/product/prd.md, docs/design/architecture.md, docs/design/technical-solution.md, docs/roadmap/features.md, docs/roadmap/current-status.md, docs/AI_FLOW.md
current_mainline: [current phase or decision]
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
[State the current approved direction, active phase, open tails, and explicit non-approvals.]
```

## 3. Phase roadmap

### R0 — Documentation authority baseline

Goal: establish the governed source-of-truth chain and prevent implementation from drifting away from product intent.

Checklist:

- [ ] Create or update `GOAL.md`.
- [ ] Create or update `docs/product/prd.md`.
- [ ] Create or update `docs/design/architecture.md`.
- [ ] Create or update `docs/design/technical-solution.md`.
- [ ] Create or update `docs/roadmap/features.md`.
- [ ] Create or update this file.
- [ ] Create or update `docs/AI_FLOW.md`.
- [ ] Verify docs and tests.

Acceptance:

- Docs index and verification gates pass.
- No active document names stale plans, chat logs, or old notes as source-of-truth.
- Product requirements, design, and roadmap agree on current scope.

Status: Planned.

## 4. Tail register

| Tail | Class | Owner | Gate | Acceptance method |
|---|---|---|---|---|
| [Tail name] | [BLOCKER / NEXT_PHASE / WATCH / PARKED] | [Owner] | [Gate] | [Evidence needed] |

## 5. Standing non-approvals

Unless explicitly approved in a later phase, this project does not authorize:

- live/default-on AI operation;
- production configuration mutation;
- external delivery or public ingress;
- destructive repository actions;
- publishing packages or releases.
