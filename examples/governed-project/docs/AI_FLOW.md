---
title: "AI-assisted development flow"
status: active
---
# AI-assisted development flow

## Purpose

Granite is developed with humans and AI agents working together. This document defines how to move from product documents to implementation while keeping work auditable, reversible, and aligned with the product goal.

Documentation development and management come before code development: code implements the documents, not the other way around.

## Document hierarchy

The authority chain is:

```text
GOAL.md -> docs/product/prd.md -> docs/design/architecture.md + docs/design/technical-solution.md -> docs/roadmap/features.md + docs/roadmap/current-status.md -> approved phase implementation plan in docs/plans/ -> code
```

Required preflight for roadmap, phase-gate, implementation, PR, CI, review, merge, or next-phase-readiness work:

1. `GOAL.md`
2. `docs/product/prd.md`
3. `docs/design/architecture.md`
4. `docs/design/technical-solution.md`
5. `docs/roadmap/features.md`
6. `docs/roadmap/current-status.md`
7. this file

## Branch model

Use trunk-based development with short-lived per-task branches.

```text
main                 # integration trunk
feat/<topic>         # feature branch
fix/<topic>          # bugfix branch
docs/<topic>         # documentation/governance branch
chore/<topic>        # maintenance branch
```

Rules:

- `main` is the integration trunk and should stay releasable.
- One task branch = one task = one PR.
- Do not commit directly to `main` except explicitly approved trivial metadata changes.
- Start from a clean `origin/main` worktree.

## Roles

| Role | Held by | Notes |
|---|---|---|
| Owner / approver | Granite maintainers | Sole approval authority; human only. |
| Controller / operator | Contributing engineer or orchestrating agent under maintainer instruction | Sequences sessions; surfaces decisions, does not approve. |
| Architect | Assigned maintainer for the change | Owns design and acceptance criteria. |
| Implementation agent | Human contributor or AI agent | Implements within approved scope. |
| Reviewer | Maintainer not involved in implementation | Reviews correctness, scope, and workflow conformance. |
| Verifier | CI plus assigned maintainer | Produces and reports evidence. |

Approval authority is never held by an implementation agent.

## Approval gates

1. **Preparation / preflight** — reading, planning, drafting, and isolated local changes may proceed under standing authorization. No shared, destructive, external, or live effect.
2. **Implementation** — merging to `main`, landing a PR, or treating work as accepted requires maintainer approval for that specific change after verification evidence exists.
3. **Destructive / external** — force-pushes, history rewrites, deleting branches or data, publishing packages or releases, sending external communications, mutating external services, or connecting to payment networks require explicit per-action owner approval.
4. **Live / runtime execution** — Granite is a local library example and does not operate at the live/runtime layer. Lithos adoption does not authorize live settlement or autonomous operation.

Clearing one gate never clears a higher gate.

## Per-task lifecycle

1. **Preflight** — read the document hierarchy and state whether the requested work matches current roadmap/status.
2. **Scope** — confirm whether the task is documentation, design, implementation, review, cleanup, or release work.
3. **Plan** — for non-trivial implementation, derive a phase implementation plan from PRD/design/roadmap.
4. **Implement** — use narrow commits and tests for behavior changes.
5. **Update authority docs** — update PRD/design/feature tracker/roadmap when product scope, design, completion state, or acceptance evidence changes.
6. **Verify** — run local gates and safety scans.
7. **Review** — reviewer findings must be resolved or explicitly accepted by the owner.
8. **PR and merge** — push branch, open PR, wait for CI, merge only when green, then verify `main` from a clean checkout/worktree.

## Implementation plan rule

A phase implementation plan lives under `docs/plans/` and is named `docs/plans/YYYY-MM-DD-<task-slug>.md`. It must include context, checklist, acceptance criteria, likely changed files, verification gates, risks, and rollback strategy.

A plan must not redefine product goals, expand product scope, or imply new live/runtime approvals.

## Verification gates

Run these before PR or merge unless the task explains why a gate is irrelevant:

```bash
python -m unittest discover -s tests
python scripts/verify_docs.py
git diff --check
```

Secret/static safety gates:

- Run a secret-shaped scan over added or changed text before commit.
- Run static dangerous-pattern scans for new subprocess, network, config-write, or external-delivery surfaces when relevant.
- Use `[REDACTED]` placeholders for sensitive examples.

## PR requirements

Every non-trivial PR should include summary, source-of-truth docs touched, feature tracker/current-status impact, test plan with command results, review evidence, secret-safety statement, and boundary statement for explicit non-approvals.

Target `main` unless the roadmap introduces another integration trunk.

## Anti-patterns

- Starting code work before PRD/design/roadmap alignment.
- Treating historical plans, chat logs, or dev notes as authority.
- Putting task-level implementation plans in `docs/roadmap/` instead of `docs/plans/`.
- Letting engineering sequence shrink PRD or design scope.
- Letting local evidence imply live settlement, payment-network calls, release publication, or external delivery.
- Broad `git add -A` without inspecting the diff.
- Committing runtime outputs, prompt material, raw stderr with secrets, `.env`, or token files.
