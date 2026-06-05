---
title: "Project PRD"
status: active
created_at: 2026-06-05
---
# [Project Name] PRD

## 1. Product goal

[Project Name] gives [primary user] a way to [durable outcome] without [problem it removes from callers or users].

## 2. Users and non-users

### Primary users

- [User 1]
- [User 2]

### Caller or integration projects

- [Caller type 1]
- [Caller type 2]

### Non-users / non-callers

- [Explicitly out-of-scope user or system]

## 3. Product principles

- **Documentation-first governance**: PRD defines product requirements; design documents define the technical solution; roadmap/status tracks engineering completion; phase plans detail implementation only after goals are fixed.
- **Human approval authority**: AI agents propose, implement, and verify; they do not self-approve.
- **Auditable by default**: accepted work has reproducible evidence.
- **Fail closed on uncertainty**: unclear authority, unsafe input, missing evidence, and stale state block acceptance.
- **No hidden live expansion**: docs never imply live/default-on behavior, production mutation, external delivery, or destructive action without explicit approval.

## 4. Functional requirements

### FR-1 [Capability name]

The product must [requirement].

Checklist:

- [ ] [Acceptance item]
- [ ] [Acceptance item]

Acceptance:

- [Evidence required to accept this requirement]

### FR-2 [Capability name]

The product must [requirement].

Checklist:

- [ ] [Acceptance item]

Acceptance:

- [Evidence required to accept this requirement]

## 5. Non-goals

- [Non-goal 1]
- [Non-goal 2]
- Live/runtime or externally visible behavior is not approved by this PRD unless this project separately defines those controls.

## 6. Release and acceptance standard

A release or phase is accepted only when:

- requirements touched by the change have evidence in `docs/roadmap/features.md`;
- phase status and tails are updated in `docs/roadmap/current-status.md`;
- local verification commands in `docs/AI_FLOW.md` pass or skipped gates are named honestly;
- review concerns are resolved or explicitly accepted by the owner;
- docs index, drift report, dev log, lessons, practices, and localized READMEs are updated or explicitly not affected.
