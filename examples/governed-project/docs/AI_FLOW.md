---
title: "AI-assisted development flow"
status: active
created_at: 2026-06-05
---
# AI-assisted development flow

## Purpose

Granite is developed with humans and AI agents working together. This document defines how to move from product documents to implementation while keeping work auditable, reversible, and aligned with the product goal.

Documentation development and management come before code development: code implements the documents, not the other way around.

## Document hierarchy

The authority chain is:

```text
GOAL.md -> docs/product/prd.md -> docs/design/architecture.md + docs/design/technical-solution.md -> docs/roadmap/features.md + docs/roadmap/current-status.md -> approved phase implementation plan in docs/plans/ -> code and knowledge artifacts
```

Required preflight for roadmap, phase-gate, implementation, PR, CI, review, merge, or next-phase-readiness work:

1. `GOAL.md`
2. `docs/product/prd.md`
3. `docs/design/architecture.md`
4. `docs/design/technical-solution.md`
5. `docs/roadmap/features.md`
6. `docs/roadmap/current-status.md`
7. this file
8. `LESSONS.md` and `docs/lessons/_drift_report.md` when knowledge artifacts or README-visible claims change

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

## Autonomous PR policy

Opening and updating a pull request is preparation: an agent may open its own PR, push updates in response to review or CI, attach evidence, and request review. An agent must never self-approve, self-merge, enable ownerless auto-merge, delete branches, publish a release, connect to payment networks, or perform other live/external/destructive actions without explicit per-action owner approval. A pull request is a proposal; adopting Lithos is not authorization to land it.

## Environment and sandbox boundaries

These state where a run may execute and what it may touch. They describe limits; they do not grant capability, and they never authorize live settlement or autonomous operation.

- **Isolation:** one git worktree per task keeps version-controlled changes separate and revertible; Granite adds no OS/process sandbox beyond that worktree isolation. A worktree does not sandbox a process; a sandbox does not version changes.
- **Filesystem roots:** writes stay within the task's working tree; reads outside the project — home directory, system configuration, unrelated repositories — are out of scope.
- **Network:** as a local library example, Granite runs with no network egress or ingress, and makes no payment-network or external-service calls.
- **Credentials:** Granite needs no credentials or secrets to build or test. Use `[REDACTED]` placeholders for any sensitive example value, and never write secrets into the working tree, logs, or a run manifest.
- **Escalation:** on meeting a boundary — an unexpected credential prompt, a write outside the working tree, or any action with an external or live effect — stop and request the higher gate instead of working around it.

## Per-task lifecycle

1. **Preflight** — read the document hierarchy and state whether the requested work matches current roadmap/status.
2. **Scope** — confirm whether the task is documentation, design, implementation, review, cleanup, or release work.
3. **Plan** — for non-trivial implementation, derive a phase implementation plan from PRD/design/roadmap.
4. **Implement** — use narrow commits and tests for behavior changes.
5. **Update authority docs** — update PRD/design/feature tracker/roadmap when product scope, design, completion state, or acceptance evidence changes.
6. **Update knowledge docs** — add dev logs, lessons, or practices when the work produces reusable knowledge or phase evidence; keep localized READMEs aligned when visible claims change.
7. **Verify** — run local gates and safety scans.
8. **Review** — reviewer findings must be resolved or explicitly accepted by the owner.
9. **PR and merge** — push branch, open PR, wait for CI, merge only when green, then verify `main` from a clean checkout/worktree.

## Implementation plan rule

A phase implementation plan lives under `docs/plans/` and is named `docs/plans/YYYY-MM-DD-<task-slug>.md`. It must include context, checklist, acceptance criteria, likely changed files, verification gates, risks, and rollback strategy.

A plan must not redefine product goals, expand product scope, or imply new live/runtime approvals.

## Verification gates

Run these before PR or merge unless the task explains why a gate is irrelevant:

```bash
python scripts/verify_project.py
python tools/build_docs_index.py --check
python tools/docs_drift_signal.py --check
python tools/static_safety_scan.py
git diff --check
```

`scripts/verify_project.py` is the bundled local verifier: it checks the governed document spine, the README/AGENTS/AI_FLOW gate vocabulary, and the docs-index boundary, then runs the docs index check, the drift self-test and check, and the static safety scan. Running it alone clears the documentation gates; the individual commands are listed so a single failing gate can be re-run in isolation.

Granite is at R0, a documentation authority baseline, so it has no product test suite yet. Behavior tests and scenario fixtures (see `docs/evaluation/scenario-regression.md`) become required once product implementation starts, and publishing remains governed by `docs/release/release-governance.md`; a verification block must not claim a behavior or release gate that does not yet exist.

Secret/static safety gates:

- Run a secret-shaped scan over added or changed text before commit.
- Run static dangerous-pattern scans for new subprocess, network, config-write, or external-delivery surfaces when relevant.
- Use `[REDACTED]` placeholders for sensitive examples.

## Run manifest and audit trail

When a collaboration unit is executed by an agent and needs to be auditable, retain an agent run manifest for the run, keeping these distinct:

- the approval reference (which gate, who granted it, the scope) versus the verification evidence;
- the claimed scope versus the actual commands and artifacts, each marked local/offline or external/live/runtime;
- execution status versus the maintainer's business verdict;
- what was redacted, where the manifest is retained, and what was left unverified or skipped.

A manifest records a run; it does not authorize one and never licenses live settlement or autonomous operation. Retain manifests alongside dev-log and verification evidence under `docs/dev_log/`.

## Conformance and portable artifacts

Granite declares its Lithos conformance — version, single `full-lifecycle-governance` model, role holders, gate operation, verification stance, and autonomous PR policy above — in a machine-readable adoption manifest. The manifest is a declaration, not an authorization: writing one grants no permission and clears no gate. Keep it and every committed collaboration artifact vendor-neutral, plain-text, and portable across tools, with no vendor or product names and no secret values. Knowledge artifacts (dev logs, lessons, practices) are part of this portable set: they record and inform, but never override the authority chain or grant approval.

## PR requirements

Every non-trivial PR should include summary, source-of-truth docs touched, feature tracker/current-status impact, test plan with command results, review evidence, secret-safety statement, an environment/sandbox boundary statement (with an agent run manifest or audit entry when the unit was agent-executed and needs auditability), and a boundary statement for explicit non-approvals.

Target `main` unless the roadmap introduces another integration trunk.

## Anti-patterns

- Starting code work before PRD/design/roadmap alignment.
- Treating historical plans, chat logs, or dev notes as authority.
- Putting task-level implementation plans in `docs/roadmap/` instead of `docs/plans/`.
- Letting engineering sequence shrink PRD or design scope.
- Letting local evidence imply live settlement, payment-network calls, release publication, or external delivery.
- Broad `git add -A` without inspecting the diff.
- Committing runtime outputs, prompt material, raw stderr with secrets, `.env`, or token files.
