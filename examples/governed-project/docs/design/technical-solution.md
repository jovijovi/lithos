---
title: "Granite Technical Solution"
status: active
created_at: 2026-06-05
---
# Granite Technical Solution

## 1. Architecture summary

The system-level architecture lives in `docs/design/architecture.md`. This file is the module-level companion: per-file responsibilities, data models, artifact layout, and testing strategy.

```text
Caller
  -> transaction facts + policy version
Granite
  -> local validation + rule evaluation
Evidence
  -> deterministic decision payload
```

## 2. Document authority

Durable requirements live in PRD, architecture, technical solution, feature tracker, and roadmap/current-status. Implementation plans under `docs/plans/` derive from those documents.

## 3. Core modules

### 3.1 `policy_version`

Responsibilities:

- Validate requested policy version.
- Refuse unknown versions before evaluation.

Current status: Planned.

### 3.2 `fee_rules`

Responsibilities:

- Evaluate fee classes from local transaction facts.
- Return deterministic fee evidence.

Current status: Planned.

### 3.3 `settlement_window`

Responsibilities:

- Classify local settlement windows.
- Report unsupported windows explicitly.

Current status: Planned.

## 4. Data model and artifacts

| Data or artifact | Purpose | Owner | Verification |
|---|---|---|---|
| Transaction facts | Input to local rules. | Caller | Validation tests. |
| Decision evidence | Reproducible rule output. | Granite | Unit tests and structured-output checks. |

## 5. Error handling and failure policy

- Fail closed when policy version or required input facts are unclear.
- Report failures without rounding partial evidence up to success.
- Redact sensitive values in logs, fixtures, examples, and artifacts.

## 6. Testing strategy

- Unit tests for policy validation, fee rules, and settlement-window classification.
- Documentation verification for authority-chain consistency.
- Static or secret-shaped scans for risky surfaces.
