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

## Files

- [`GOAL.md`](GOAL.md) — stable product goal and source-of-truth index.
- [`docs/AI_FLOW.md`](docs/AI_FLOW.md) — local AI-assisted development workflow.
- [`AGENTS.md`](AGENTS.md) — agent-facing contract.
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) — PR evidence checklist.
- [`docs/INDEX.md`](docs/INDEX.md) — documentation map.
- [`ai-collaborative-development-standards.md`](ai-collaborative-development-standards.md) — compatibility pointer to `docs/AI_FLOW.md`.

## How it was adopted

1. Started from [`templates/governed-project/`](../../templates/governed-project/).
2. Kept `docs/AI_FLOW.md` as the operational local workflow file.
3. Added the product/design/roadmap/plans spine so development tasks trace from goal to evidence.
4. Updated `AGENTS.md` and the PR checklist to match the stricter flow.

Compare with the [minimal example](../minimal-project/README.md) to see why workflow-only adoption is intentionally lighter.
