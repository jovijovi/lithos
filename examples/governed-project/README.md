# Example — Governed Project

A worked example of adopting [Lithos](../../README.md) in a project with formal review, multiple contributors, staged roadmap work, and audit obligations.

This stands in for a hypothetical payments library, **Granite**, maintained by a team that ships to downstream consumers and must be able to reconstruct how any change was approved and verified.

## What this example demonstrates

- The full governed document spine from [`docs/governed-project-structure.md`](../../docs/governed-project-structure.md).
- `GOAL.md` as a stable product-positioning and source-of-truth index.
- Product requirements in `docs/product/prd.md`.
- System architecture and module detail split across `docs/design/architecture.md` and `docs/design/technical-solution.md`.
- Feature/status governance split across `docs/roadmap/features.md` and `docs/roadmap/current-status.md`.
- Task-level implementation plan rules in `docs/plans/README.md`.
- The local Lithos workflow at `docs/AI_FLOW.md`.
- Knowledge capture through `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, and generated drift reports — records that inform future work but never override the authority chain or clear an approval gate.
- A Lithos conformance claim (version and depth) suitable for a machine-readable adoption manifest, kept vendor-neutral and portable across tools.
- An autonomous PR policy: agents may open and update pull requests, but never self-approve, self-merge, enable ownerless auto-merge, delete branches, publish, or perform live/external actions without explicit owner approval.
- Bilingual README governance through `README.md` and `README.zh-CN.md`.

## Files

- [`README.md`](README.md) — English example entry point.
- [`README.zh-CN.md`](README.zh-CN.md) — Chinese example entry point.
- [`GOAL.md`](GOAL.md) — stable product goal and source-of-truth index.
- [`docs/AI_FLOW.md`](docs/AI_FLOW.md) — local AI-assisted development workflow.
- [`AGENTS.md`](AGENTS.md) — agent-facing contract.
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) — PR evidence checklist.
- [`docs/INDEX.md`](docs/INDEX.md) — generated docs-directory index.
- [`LESSONS.md`](LESSONS.md) — root entry point for lessons and practices.
- [`ai-collaborative-development-standards.md`](ai-collaborative-development-standards.md) — compatibility pointer to `docs/AI_FLOW.md`.

## How it was adopted

1. Started from [`templates/governed-project/`](../../templates/governed-project/).
2. Kept `docs/AI_FLOW.md` as the operational local workflow file.
3. Added the product/design/roadmap/plans spine so development tasks trace from goal to evidence.
4. Added the dev-log/lesson/practice knowledge spine and generated docs index/drift tooling.
5. Updated `AGENTS.md`, bilingual READMEs, and the PR checklist to match the stricter flow.

Compare with the workflow-only [`templates/governed-ai-flow.md`](../../templates/governed-ai-flow.md) template to see why a lighter governed workflow is intentionally thinner than the full governed spine.
