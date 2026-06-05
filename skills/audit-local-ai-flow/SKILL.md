---
name: audit-local-ai-flow
description: Use when checking whether a project's local workflow file actually conforms to Lithos and matches how the project really works — produces a gap report covering roles, the four approval gates, environment boundaries, the autonomous PR policy, verification, the conformance claim, and drift from reality.
---

# Audit a Local AI Flow

Assess an existing **local workflow file** against Lithos and against the project's real practice. Output is a findings report; you do not silently rewrite the document.

## When to use

- Before relying on a local workflow file you did not write.
- Periodically, or after the team, tooling, or risk profile changes.
- When the document and observed behavior seem to disagree.

## Inputs to gather first

- The local workflow file (whatever it is named).
- The project's `AGENTS.md`, PR checklist, branch/CI configuration, adoption manifest, and recent merged units as evidence of real practice.

## Conformance checklist

Check each item; record present / partial / missing with a pointer to the relevant Lithos doc.

1. **Roles** — every role in `docs/roles.md` has an owner; combined roles are stated explicitly; approval authority is not held by an agent.
2. **Approval gates** — all four gates from `docs/approval-semantics.md` are operationalized; layering is intact (no gate implies a higher one); the live/runtime stance is explicit.
3. **Environment and sandbox boundary** — filesystem roots, network egress/ingress, the **credential scope** bound to least privilege, external/destructive side effects, and escalation/abort conditions are stated (`docs/environment-and-sandbox-policy.md`); git worktree isolation and OS/process sandbox are not conflated.
4. **Discipline** — branch naming and worktree isolation are stated; the integration branch's allowed contents are defined (`docs/core-concepts.md`).
5. **Verification and static safety scan** — "done" requires reproducible evidence, not agreement, and honesty obligations are present (`docs/verification-standards.md`); a **static safety scan** gate rejects secret-shaped tokens, private machine-local paths, and unfinished-work placeholders locally and in CI (`docs/static-safety-scan.md`). Confirm the file treats that scan as safety evidence, **not behavior proof**.
6. **Autonomous PR policy** — the file lets an agent open/update/close its own pull request as preparation but forbids **self-approval**, **self-merge**, and **ownerless auto-merge**, and routes merging, branch deletion, releasing, and external communication to explicit higher-gate owner approval (`docs/autonomous-pr-policy.md`).
7. **Conformance claim** — a machine-readable **adoption manifest** declares the version and depth and matches `schemas/lithos-adoption-manifest.schema.json`; the **conformance fixtures** in `fixtures/conformance/`, including the **invalid** cases, are exercised so the claim stays honest (`docs/conformance-and-fixtures.md`).
8. **Agent run records** — for agent-executed units, an **agent run manifest** is retained as audit evidence with the approval reference kept distinct from verification evidence; confirm the file treats it as a record, **not authorization** (`docs/agent-run-manifest.md`).
9. **Discoverability** — the file is referenced from `README`/`AGENTS.md` and is a single source of truth.
10. **No placeholders** — no unresolved bracketed decisions remain.
11. **Governed document spine** — if the project claims formal governance, roadmap phases, release gates, runtime boundaries, or multi-agent development, verify the `GOAL.md -> PRD -> design -> roadmap/features + current-status -> docs/plans -> code` chain from `docs/governed-project-structure.md`, and confirm task-level plans do not live in `docs/roadmap/`.
12. **Knowledge spine** — for full governed projects, verify the **knowledge spine** — `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, generated `docs/INDEX.md`, and `docs/lessons/_drift_report.md` — exists or is explicitly out of scope (`docs/knowledge-governance.md`).
13. **Scenario regression and release governance** — for behavior-bearing projects, advertised behaviors are pinned by a **scenario regression** suite (`docs/scenario-regression-governance.md`); for projects that publish artifacts, **release and supply-chain** governance requires owner-approved publishing, a provenance record, and pinned dependencies with no agent self-release (`docs/release-and-supply-chain-governance.md`).
14. **Localized README sync** — if localized README files exist, verify they stay semantically aligned with `README.md` when visible claims change.

## Drift checks (document vs. reality)

- Do recent merged units actually carry the evidence the file requires, including an **agent run manifest** where one is expected?
- Does the **static safety scan** actually run locally and in CI, or is it only described?
- Do any merged pull requests show agent **self-approval**, **self-merge**, or **ownerless auto-merge** in practice — a violation, not merely a gap?
- Are advertised behaviors backed by **scenario regression** fixtures, and do releases carry owner approval and a provenance record?
- Does observed branch/review practice match what the file states?
- Are destructive/external actions in practice covered by the file's gate-3 rules and the declared **credential scope**?
- Do PRs and plans update the feature tracker/current-status files when they change completion state or evidence?

Flag any place the document describes a process the project does not follow — drift makes the file misleading, which is worse than silence.

## Output

A concise report: each checklist item with status and evidence, each drift finding, and a prioritized list of fixes. Recommend tightening (never loosening) where a requirement is weak. Propose changes; let the owner approve them.

## Done when

- Every checklist item and drift check has a verdict backed by a pointer.
- Gaps are listed with concrete, prioritized remediation.
- No finding is asserted without evidence from the file or the project's real practice.
