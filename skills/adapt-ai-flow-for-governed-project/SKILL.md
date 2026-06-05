---
name: adapt-ai-flow-for-governed-project
description: Use when a project with formal review, multiple contributors, or compliance obligations needs to upgrade a workflow-only Lithos local workflow file into a full governed-project one — adds the stricter roles, environment policy, autonomous PR policy, approval records, conformance claim, and audit trail governance requires without loosening any requirement.
---

# Adapt an AI Flow for a Governed Project

Upgrade an existing local workflow file (often a workflow-only one) into a **governed** shape suited to formal review, multiple contributors, or compliance obligations. You add and tighten; you never loosen a Lithos requirement.

## When to use

- A project has outgrown a lighter workflow-only flow and now has formal review or compliance needs.
- An audit (`audit-local-ai-flow`) recommended governance additions.

## What governance adds

Start from the project's current file, `templates/governed-ai-flow.md`, and — when the project needs a full authority chain — `docs/governed-project-structure.md` plus `templates/governed-project/`. Then layer in:

1. **Independent roles.** Separate reviewer and verifier from the implementation role; state who may approve and that approval authority is human-only. Remove role combinations that governance disallows.
2. **Recorded approvals.** For each gate in `docs/approval-semantics.md`, define how the approval is *recorded* (who, what scope, when), not just signaled — especially gate 3 (destructive/external) approvals, which must be explicit and per-action.
3. **Environment and sandbox policy.** Promote the environment policy to a first-class, change-controlled document (`docs/environment-and-sandbox-policy.md`): filesystem roots, network egress/ingress, the **credential scope** bound to least privilege, the external/destructive side-effect inventory, and escalation/abort conditions. Keep git worktree isolation and OS/process sandbox distinct.
4. **Autonomous PR policy.** Make explicit that an agent may open/update/close its own pull request as preparation but must never perform **self-approval**, **self-merge**, or **ownerless auto-merge**; merging, branch deletion, releasing, and external communication require explicit higher-gate owner approval (`docs/autonomous-pr-policy.md`).
5. **Stronger verification and a static safety scan.** Require reproducible evidence (tests/CI) for behavioral changes, link CI runs, and report failures and skips faithfully (`docs/verification-standards.md`). Add the **static safety scan** gate — secret-shaped tokens, private machine-local paths, and unfinished-work placeholders, locally and in CI (`docs/static-safety-scan.md`); treat it as safety evidence, **not behavior proof**.
6. **Machine-readable conformance claim.** Declare conformance in an **adoption manifest** that matches `schemas/lithos-adoption-manifest.schema.json` (version, depth, roles, gates, autonomous PR policy), and exercise the **conformance fixtures** in `fixtures/conformance/`, including the **invalid** cases, so the claim stays honest (`docs/conformance-and-fixtures.md`).
7. **Agent run records and audit trail.** State where approvals, reviews, verification evidence, and an **agent run manifest** are retained so a unit can be reconstructed after the fact; keep the approval reference distinct from the evidence. A manifest is a record, **not authorization** (`docs/agent-run-manifest.md`).
8. **Change control for the standard itself.** Point to `docs/versioning-and-governance.md` and require that normative changes to the local workflow file are reviewed and that translations/companion docs change together.
9. **Live/runtime stance.** If the project operates at the live/runtime layer, document the separate controls (human authorization, monitoring, kill switch, audit) it relies on — Lithos does not provide these.
10. **Document authority chain.** For mature governed repos, establish `GOAL.md`, `docs/product/prd.md`, `docs/design/architecture.md`, `docs/design/technical-solution.md`, `docs/roadmap/features.md`, `docs/roadmap/current-status.md`, `docs/plans/README.md`, and `docs/AI_FLOW.md`. Keep product requirements, design, roadmap/status, and task plans separate.
11. **Knowledge spine.** Add the **knowledge spine** — `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, generated `docs/INDEX.md`, and `docs/lessons/_drift_report.md` — so lessons and practices do not live only in chat history (`docs/knowledge-governance.md`).
12. **Scenario regression governance.** For behavior-bearing projects, pin advertised behaviors and shipped examples to named fixtures so a **scenario regression** is caught mechanically, and call out, justify, and approve any change to an expected outcome (`docs/scenario-regression-governance.md`).
13. **Release and supply-chain governance.** For published artifacts, require owner-approved publishing with no agent self-release, a provenance record, pinned dependencies, and least-privilege publishing credentials (`docs/release-and-supply-chain-governance.md`).
14. **README localization discipline.** If the project has localized README files, update them with `README.md` whenever user-facing project claims change.

## Steps

1. Read the current file and run `audit-local-ai-flow` to find gaps.
2. Apply the additions above, preserving any rules already stricter than the template.
3. Resolve every bracketed decision; leave no placeholder.
4. If the existing local workflow file lives at the repo root but governance docs live under `docs/`, move it to `docs/AI_FLOW.md` or add a clear pointer so there is one operational source of truth.
5. Update `AGENTS.md`, README/GOAL pointers, localized README files, the adoption manifest, and the PR checklist to match the stricter flow.
6. Generate or check docs index and drift artifacts when the governed project uses them.
7. Re-run the audit to confirm no gaps remain.

## Guardrails

- Tighten only. Do not drop or weaken a Lithos requirement in the name of "process fit."
- Keep approval authority human and per-scope; an agent run manifest is evidence, **not authorization**.
- Adapting for governance does not grant live/autonomous or release execution; document, don't imply, any runtime controls.

## Done when

- The file reflects independent review/verification, recorded per-action approvals, a declared environment and sandbox boundary, an explicit autonomous PR policy, an audit trail, and an explicit live/runtime stance.
- A schema-valid adoption manifest backs the conformance claim, and behavior-bearing and publishing projects carry scenario regression and release and supply-chain governance.
- Mature governed projects have the full source-of-truth chain and knowledge spine from `docs/governed-project-structure.md`.
- `audit-local-ai-flow` reports conformance with no open gaps.
