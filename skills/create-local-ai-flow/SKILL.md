---
name: create-local-ai-flow
description: Use when a project is adopting Lithos and needs its local workflow file written from scratch — produces a conformant local AI-collaboration document from the right template, with roles, approval gates, discipline, and verification filled in.
---

# Create a Local AI Flow

Produce a conformant **local workflow file** for a repository adopting Lithos. Output is one document the project commits; you do not change runtime behavior or grant any execution authority.

## When to use

- A repository has decided to adopt Lithos and has no local workflow file yet.
- An existing collaboration document needs to be replaced with a conformant one.

## Inputs to gather first

- Project size and contributor model (solo, small team, formal review).
- Whether the project ever operates at the live/runtime layer, and under what existing controls.
- Existing conventions: branch naming, CI, review process, where docs live.
- The filename the project wants for the local workflow file (it chooses — do not impose one).

## Steps

1. **Pick the template.** Small/early-stage → `templates/minimal-ai-flow.md`. Formal review with only workflow governance → `templates/governed-ai-flow.md`. Mature projects with roadmap/status/design authority, multiple agents, staged phases, release gates, runtime boundaries, or compliance needs → copy the full `templates/governed-project/` spine and use `docs/governed-project-structure.md` as the authority map.
2. **Choose the filename with the owner.** Any discoverable name is valid (e.g. `AI_FLOW.md`, `docs/AI_FLOW.md`, `ai-collaborative-development-standards.md`). Place it where the project keeps such docs. For governed-project adoption, prefer `docs/AI_FLOW.md` and keep `GOAL.md` as the stable source-of-truth index.
3. **Assign roles.** Fill in who holds each role from `docs/roles.md`. Note explicitly any roles that are combined.
4. **Operationalize the four gates.** For each gate in `docs/approval-semantics.md`, write how it is signaled here. State plainly whether the project operates at the live/runtime layer at all; if not, say so.
5. **State discipline.** Branch naming, isolation expectations, and what the integration branch may contain.
6. **Define "done."** The verification evidence each unit must carry, per `docs/verification-standards.md`.
7. **Wire companions.** Add the `templates/AGENTS.md.snippet` contract or `templates/governed-project/AGENTS.md` to `AGENTS.md` and adopt `templates/pr-checklist.md`. Reference the local workflow file from `README`, `GOAL.md` where present, and `AGENTS.md`.
8. **Resolve every bracketed decision.** Leave no placeholder behind; an unfilled blank is a conformance gap.

## Done when

- The file exists under the chosen name and is referenced from the project's entry points.
- All four gates are operationalized and the live/runtime stance is explicit.
- Roles are assigned, discipline stated, and "done" defined with reproducible evidence.
- Running `audit-local-ai-flow` against it reports no gaps.

## Guardrails

- Never assign approval authority to an agent.
- You may make a rule stricter locally; do not loosen a Lithos requirement and still call the result conformant.
- Adopting this file does not authorize live or autonomous AI execution — say so in the file when relevant.
