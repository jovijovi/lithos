---
title: "Project Technical Solution"
status: active
created_at: 2026-06-05
---
# [Project Name] Technical Solution

## 1. Architecture summary

The system-level architecture lives in `docs/design/architecture.md`. This file is the module-level companion: per-file responsibilities, data models, artifact layout, and testing strategy.

> **Abstraction level.** State module direction at the design level: responsibilities, data models, invariants, failure policy, and test strategy as intent. Do not embed concrete commands, shell pipelines, regex snippets, or exact tool/verifier parameters — that mechanism lives in code, in `docs/plans/`, or in the verification tooling it configures — unless a command interface is itself the object being designed.

```text
Caller or user
  -> [request or intent]
[Project Name]
  -> [core processing]
Evidence
  -> [tests, artifacts, review material]
```

## 2. Document authority

Durable requirements live in:

- PRD and product requirements: `docs/product/prd.md`
- System architecture: `docs/design/architecture.md`
- Technical solution: this file
- Feature completion matrix: `docs/roadmap/features.md`
- Roadmap, phases, acceptance criteria: `docs/roadmap/current-status.md`

## 3. Core modules

### 3.1 `[module]`

Responsibilities:

- [Responsibility]
- [Responsibility]

Design notes:

- [Constraint]
- [Boundary]

Current status: [Done / Partial / Planned / Parked].

### 3.2 `[module]`

Responsibilities:

- [Responsibility]

Current status: [Done / Partial / Planned / Parked].

## 4. Data model and artifacts

| Data or artifact | Purpose | Owner | Verification |
|---|---|---|---|
| [Name] | [Purpose] | [Module/role] | [Test or check] |

## 5. Error handling and failure policy

- Fail closed when authority, state, or evidence is unclear.
- Report failures without rounding partial evidence up to success.
- Redact sensitive values in logs, fixtures, examples, and artifacts.

## 6. Testing strategy

State the strategy as intent — which behaviors, boundaries, and failure modes must be proven and why — not the exact commands a run executes.

- Unit tests for module behavior.
- Integration or smoke tests for critical boundaries.
- Documentation verification for authority-chain consistency.
- Static or secret-shaped scans for risky surfaces.
