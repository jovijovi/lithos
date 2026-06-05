---
name: adapt-ai-flow-for-governed-project
description: Use when a project with formal review, multiple contributors, or compliance obligations needs to upgrade a minimal Lithos local workflow file into a governed one — adds the stricter roles, approval records, and audit trail governance requires without loosening any requirement.
---

# Adapt an AI Flow for a Governed Project

Upgrade an existing local workflow file (often a minimal one) into a **governed** shape suited to formal review, multiple contributors, or compliance obligations. You add and tighten; you never loosen a Lithos requirement.

## When to use

- A project has outgrown a solo/minimal flow and now has formal review or compliance needs.
- An audit (`audit-local-ai-flow`) recommended governance additions.

## What governance adds

Start from the project's current file, `templates/governed-ai-flow.md`, and — when the project needs a full authority chain — `docs/governed-project-structure.md` plus `templates/governed-project/`. Then layer in:

1. **Independent roles.** Separate reviewer and verifier from the implementation role; state who may approve and that approval authority is human-only. Remove role combinations that governance disallows.
2. **Recorded approvals.** For each gate in `docs/approval-semantics.md`, define how the approval is *recorded* (who, what scope, when), not just signaled — especially gate 3 (destructive/external) approvals, which must be explicit and per-action.
3. **Explicit destructive/external inventory.** Enumerate the project's hard-to-reverse and outward-facing actions and the required approval for each.
4. **Stronger verification.** Require reproducible evidence (tests/CI) for behavioral changes, link CI runs, and require faithful reporting of failures and skips per `docs/verification-standards.md`.
5. **Audit trail.** State where approvals, reviews, and verification evidence are retained so a unit can be reconstructed after the fact.
6. **Change control for the standard itself.** Point to `docs/versioning-and-governance.md` and require that normative changes to the local workflow file are reviewed and that translations/companion docs change together.
7. **Live/runtime stance.** If the project operates at the live/runtime layer, document the separate controls (human authorization, monitoring, kill switch, audit) it relies on — Lithos does not provide these.
8. **Document authority chain.** For mature governed repos, establish `GOAL.md`, `docs/product/prd.md`, `docs/design/architecture.md`, `docs/design/technical-solution.md`, `docs/roadmap/features.md`, `docs/roadmap/current-status.md`, `docs/plans/README.md`, and `docs/AI_FLOW.md`. Keep product requirements, design, roadmap/status, and task plans separate.
9. **Knowledge spine.** Add `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, generated `docs/INDEX.md`, and `docs/lessons/_drift_report.md` so lessons and practices do not live only in chat history.
10. **README localization discipline.** If the project has localized README files, update them with `README.md` whenever user-facing project claims change.

## Steps

1. Read the current file and run `audit-local-ai-flow` to find gaps.
2. Apply the additions above, preserving any rules already stricter than the template.
3. Resolve every bracketed decision; leave no placeholder.
4. If the existing local workflow file lives at the repo root but governance docs live under `docs/`, move it to `docs/AI_FLOW.md` or add a clear pointer so there is one operational source of truth.
5. Update `AGENTS.md`, README/GOAL pointers, localized README files, and the PR checklist to match the stricter flow.
6. Generate or check docs index and drift artifacts when the governed project uses them.
7. Re-run the audit to confirm no gaps remain.

## Guardrails

- Tighten only. Do not drop or weaken a Lithos requirement in the name of "process fit."
- Keep approval authority human and per-scope.
- Adapting for governance does not grant live/autonomous execution; document, don't imply, any runtime controls.

## Done when

- The file reflects independent review/verification, recorded per-action approvals, an audit trail, and an explicit live/runtime stance.
- Mature governed projects have the full source-of-truth chain and knowledge spine from `docs/governed-project-structure.md`.
- `audit-local-ai-flow` reports conformance with no open gaps.
