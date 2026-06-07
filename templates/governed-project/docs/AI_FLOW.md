---
title: "AI-assisted development flow"
status: active
created_at: 2026-06-05
---
# AI-assisted development flow

## Purpose

This repository is developed with humans and AI agents working together. This document defines how to move from product documents to implementation while keeping work auditable, reversible, and aligned with the product goal.

Documentation development and management come before code development: code implements the documents, not the other way around.

## Document hierarchy

The authority chain is:

```text
GOAL.md -> docs/product/prd.md -> docs/design/architecture.md + docs/design/technical-solution.md -> docs/roadmap/features.md + docs/roadmap/current-status.md -> approved phase implementation plan in docs/plans/ -> code and knowledge artifacts
```

Concrete task or phase implementation plans live under `docs/plans/`; `docs/roadmap/` owns roadmap, status, and feature tracking, not task-level execution plans. See `docs/plans/README.md`.

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
main                          # integration trunk
feat/<topic>                  # feature branch
fix/<topic>                   # bugfix branch
docs/<topic>                  # documentation/governance branch
chore/<topic>                 # maintenance branch
```

Rules:

- `main` is the integration trunk and should stay releasable.
- One task branch = one task = one PR.
- Do not commit directly to `main` except explicitly approved trivial metadata changes.
- Start from a clean `origin/main` worktree.

## Roles

| Role | Held by | Notes |
|---|---|---|
| Owner / approver | [human owner or group] | Sole approval authority; human only. |
| Controller / operator | [person or orchestrating agent] | Sequences sessions; surfaces decisions, does not approve. |
| Architect | [person or role] | Owns design and acceptance criteria. |
| Implementation agent | [agents or contributors] | Implements within approved scope. |
| Reviewer | [independent reviewer] | Reviews correctness, scope, and workflow conformance. |
| Verifier | [independent verifier] | Produces and reports evidence. |

Approval authority is never held by an implementation agent.

## Approval gates

1. **Preparation / preflight** — reading, planning, drafting, and isolated local changes may proceed under standing authorization. No shared, destructive, external, or live effect.
2. **Implementation** — merging to `main`, landing a PR, or treating work as accepted requires owner approval for that specific change after verification evidence exists.
3. **Destructive / external** — force-pushes, history rewrites, deleting branches or data, publishing packages or releases, sending communications, or mutating external services require explicit per-action owner approval.
4. **Live / runtime execution** — this project [does not operate at this layer / operates only under the separate controls listed here]. Lithos adoption alone never authorizes live or autonomous execution.

Clearing one gate never clears a higher gate.

## Autonomous PR policy

Opening and updating a pull request is preparation: an agent may open its own PR, push updates in response to review or CI, attach evidence, and request review. An agent must never self-approve, self-merge, enable ownerless auto-merge, delete branches, publish, or perform live/external/destructive actions without explicit per-action owner approval. A pull request is a proposal; adopting Lithos is not authorization to land it.

## Environment and sandbox boundaries

These state *where* a run may execute and *what it may touch*. They describe limits; they do not grant capability, and they never authorize live or autonomous execution.

- **Isolation:** [git worktree isolation per task; OS/process sandbox, or `none beyond worktree isolation`]. A worktree does not sandbox a process; a sandbox does not version changes.
- **Filesystem roots:** writes confined to [the task's working tree and declared scratch only]; reads outside the project ([home directory, system configuration, unrelated repositories]) are [denied or explicitly called out].
- **Network:** egress is [`none` by default for preparation work, or the named destinations/registries genuinely required]; ingress is [`none`].
- **Credentials:** [`none`, or the least-privilege, narrowly scoped tokens a task needs, for only as long as it runs]. Secrets are never written into the working tree, logs, or a run manifest; use `[REDACTED]` placeholders.
- **Escalation:** on meeting a boundary — an unexpected credential prompt, an attempted write outside the declared roots, or any action with an external or live effect — stop and request the higher gate instead of working around it.

Keep these decisions here or in a separate change-controlled environment policy.

## Per-task lifecycle

1. **Preflight** — read the document hierarchy and state whether the requested work matches current roadmap/status.
2. **Scope** — confirm whether the task is documentation, design, implementation, review, cleanup, or release work.
3. **Plan** — for non-trivial implementation, derive a phase implementation plan from PRD/design/roadmap. The plan must not redefine product goals.
4. **Implement** — use narrow commits and tests for behavior changes.
5. **Update authority docs** — update PRD/design/feature tracker/roadmap when product scope, design, completion state, or acceptance evidence changes.
6. **Update knowledge docs** — add dev logs, lessons, or practices when the work produces reusable knowledge or phase evidence; keep localized READMEs aligned when visible claims change.
7. **Verify** — run local gates and safety scans.
8. **Review** — reviewer findings must be resolved or explicitly accepted by the owner.
9. **PR and merge** — push branch, open PR, wait for CI, merge only when green, then verify `main` from a clean checkout/worktree.

## Implementation plan rule

A phase implementation plan is an execution artifact created only after PRD/design/roadmap target is clear. It lives under `docs/plans/` and is named `docs/plans/YYYY-MM-DD-<task-slug>.md`. It must include:

- context and exact target from PRD/design/roadmap;
- checklist of implementation goals;
- acceptance criteria;
- files likely to change;
- verification gates;
- risks and open questions;
- rollback strategy.

A plan must not redefine product goals, expand product scope, or imply new live/runtime approvals.

## Verification gates

Run these before PR or merge unless the task clearly explains why a gate is irrelevant:

```bash
[project test command]
[project syntax or build command]
python tools/build_docs_index.py --check
python tools/docs_drift_signal.py --check
python tools/static_safety_scan.py
[project documentation verification command]
git diff --check
```

Secret/static safety gates:

- Run `python tools/static_safety_scan.py` — a first-class gate that rejects secret-shaped tokens, private machine-local paths, and unfinished-work placeholders. See `docs/release/release-governance.md` for how it gates a release.
- Run static dangerous-pattern scans for new subprocess, network, config-write, or external-delivery surfaces when relevant.
- For behavior-bearing work, run the scenario regression suite defined in `docs/evaluation/scenario-regression.md`; a changed expected outcome is a behavior change that needs approval.
- Use `[REDACTED]` placeholders for sensitive examples.

## Run manifest and audit trail

When a collaboration unit is executed by an agent and needs to be auditable, retain an agent run manifest for the run. It records, kept distinct:

- the approval reference (which gate, who granted it, the scope) versus the verification evidence;
- the claimed scope versus the actual commands and artifacts, each action marked local/offline or external/live/runtime;
- execution status versus the owner's business verdict;
- what was redacted, where the manifest is retained, and what was left unverified or skipped.

A manifest records a run; it does not authorize one and never licenses live/runtime execution. Retain manifests alongside dev-log and verification evidence.

## Conformance and portable artifacts

This project declares its Lithos conformance — version, single `full-lifecycle-governance` model, role holders, gate operation, verification stance, and the autonomous PR policy above — in a machine-readable adoption manifest. The manifest is a declaration, not an authorization: writing one grants no permission and clears no gate. Keep it and every committed collaboration artifact vendor-neutral, plain-text, and portable across tools, with no vendor or product names and no secret values. Knowledge artifacts (dev logs, lessons, practices) are part of this portable set: they record and inform, but never override the authority chain or grant approval.

## PR requirements

Every non-trivial PR should include:

- summary of changes;
- source-of-truth docs touched;
- feature tracker and roadmap status impact;
- test plan with commands and results;
- review evidence;
- secret-safety statement;
- environment/sandbox boundary statement, and an agent run manifest or audit entry when the unit was agent-executed and needs auditability;
- boundary statement for explicit non-approvals.

Target `main` unless a roadmap explicitly introduces another integration trunk.

## Anti-patterns

- Starting code work before PRD/design/roadmap alignment.
- Treating historical plans, chat logs, or dev notes as authority.
- Putting task-level implementation plans in `docs/roadmap/` instead of `docs/plans/`.
- Letting engineering sequence shrink PRD or design scope.
- Letting dry-run, preview, or local evidence imply live/default-on behavior.
- Broad `git add -A` without inspecting the diff.
- Committing runtime outputs, prompt material, raw stderr with secrets, `.env`, or token files.
