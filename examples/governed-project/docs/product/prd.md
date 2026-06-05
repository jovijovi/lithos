---
title: "Granite PRD"
status: active
created_at: 2026-06-05
---
# Granite PRD

## 1. Product goal

Granite gives downstream services a deterministic local library for fee and settlement rule decisions without embedding policy logic in every service.

## 2. Users and non-users

### Primary users

- Product engineers integrating payment-domain rule decisions.
- Maintainers reviewing policy updates.

### Caller projects

- Services that need local fee and settlement decision evidence.
- Test harnesses validating policy-version behavior.

### Non-users / non-callers

- Payment-network operators.
- Customer-support communication systems.
- Production settlement schedulers.

## 3. Product principles

- **Documentation-first governance**: PRD defines product requirements; design documents define the technical solution; roadmap/status tracks engineering completion; phase plans detail implementation only after goals are fixed.
- **Human approval authority**: AI agents propose, implement, and verify; they do not self-approve.
- **Deterministic local evidence**: every decision can be reproduced from input facts and a policy version.
- **No hidden live expansion**: docs never imply money movement, network calls, production mutation, or external delivery without explicit approval.

## 4. Functional requirements

### FR-1 Policy-version validation

The library must validate the requested policy version before producing a decision.

Checklist:

- [x] Requirement states validation happens before decisions are returned.
- [x] Evidence expectations include valid and invalid policy versions.

Acceptance:

- Invalid policy versions fail before a decision is returned.
- Valid policy versions are recorded in decision evidence.

### FR-2 Fee rule evaluation

The library must calculate fee decisions from local inputs and versioned rules.

Checklist:

- [x] Requirement states decisions come from local inputs and versioned rules.
- [x] Evidence expectations include representative fee classes and decision metadata.

Acceptance:

- Unit tests cover representative fee classes.
- Decision evidence includes input markers, rule version, and outcome.

### FR-3 Settlement-window classification

The library must classify settlement windows from local facts.

Checklist:

- [x] Requirement states settlement windows are classified from local facts.
- [x] Evidence expectations include supported and unsupported windows.

Acceptance:

- Unit tests cover same-day, delayed, and unsupported windows.

### FR-4 Governed knowledge spine

The project must preserve dev logs, lessons, practices, generated docs index, drift report, and bilingual README alignment when governance claims change.

Checklist:

- [x] `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, and `LESSONS.md` exist.
- [x] Generated docs index and drift report are checked by local verification.
- [x] `README.md` and `README.zh-CN.md` describe the same project claims.

Acceptance:

- The parent Lithos verifier checks the governed knowledge spine and README markers.

## 5. Non-goals

- Moving money.
- Calling external payment networks.
- Customer communication.
- Production configuration mutation.
- Live/runtime AI operation.

## 6. Release and acceptance standard

A release or phase is accepted only when feature tracker rows and roadmap status are updated, verification commands in `docs/AI_FLOW.md` pass, and review concerns are resolved or explicitly accepted by the owner.
