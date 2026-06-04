# Example — Governed Project

A worked example of adopting [Lithos](../../README.md) in a project with formal review, multiple contributors, and compliance obligations.

This stands in for a hypothetical payments library, **Granite**, maintained by a team that ships to many downstream consumers and must be able to reconstruct how any change was approved and verified.

## What this example demonstrates

- A local workflow file written from [`templates/governed-ai-flow.md`](../../templates/governed-ai-flow.md), named **`ai-collaborative-development-standards.md`** (the team's chosen filename).
- Independent reviewer and verifier roles, separate from implementation.
- Recorded, per-action approvals — especially for destructive and external effects.
- An explicit audit trail and a stated live/runtime stance.
- Change control over the workflow document itself.

## Files

- [`ai-collaborative-development-standards.md`](ai-collaborative-development-standards.md) — the local workflow file.

## How it was adopted

1. Started from the [minimal shape](../minimal-project/README.md), then applied the [`adapt-ai-flow-for-governed-project`](../../skills/adapt-ai-flow-for-governed-project/SKILL.md) skill.
2. Chose the filename `ai-collaborative-development-standards.md`.
3. Separated reviewer and verifier from implementation, enumerated destructive/external actions, and defined where approvals and evidence are retained.
4. Updated `AGENTS.md` and the [PR checklist](../../templates/pr-checklist.md) to match the stricter flow.

Compare with the [minimal example](../minimal-project/README.md) to see what governance adds.
