# Local Adoption

Lithos describes the *shape* of human–AI collaboration. Adoption is the act of making that shape concrete in one repository. This document defines what an adopting project must produce and the choices it is free to make.

## The local workflow file

Every adopting project **must** have a single document that records how humans and AI collaborate there. Lithos calls this the **local workflow file**.

**The project chooses its own filename.** Lithos does not mandate one. Pick a name that fits your repository's conventions, for example:

- `AI_FLOW.md`
- `ai-collaborative-development-standards.md`
- `COLLABORATION.md`
- `docs/ai-workflow.md`

What matters is that the file is discoverable, singular (one source of truth, not scattered rules), and referenced from the project's entry points (`README`, `AGENTS.md`).

## What the local workflow file must cover

To conform to Lithos, the local workflow file **must**:

1. **Assign the roles.** State who holds each role in [roles](roles.md), and explicitly note any roles that are combined.
2. **Operationalize the four approval gates.** For each gate in [approval semantics](approval-semantics.md), say how it is signaled in this project — and state plainly whether the project operates at the live/runtime layer at all.
3. **State the worktree/branch discipline.** Branch naming, isolation expectations, and what the integration branch is allowed to contain (see [core concepts](core-concepts.md)).
4. **Define "done."** The [verification](verification-standards.md) evidence a unit must carry before it is accepted.

It **should** also list the project's destructive/external actions explicitly, and point to its PR checklist.

## Recommended companion files

- An `AGENTS.md` (or equivalent) carrying the agent-facing contract — start from [`templates/AGENTS.md.snippet`](../templates/AGENTS.md.snippet).
- A PR checklist — start from [`templates/pr-checklist.md`](../templates/pr-checklist.md).
- For governed projects, a root `LESSONS.md`, `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, generated `docs/INDEX.md`, and generated `docs/lessons/_drift_report.md` keep reusable knowledge out of chat history.
- If localized README files exist, keep them semantically aligned with `README.md` whenever visible project claims change.

## Choosing a starting template

| If your project… | Start from |
| --- | --- |
| is small, single-maintainer, or early-stage | [`templates/minimal-ai-flow.md`](../templates/minimal-ai-flow.md) |
| needs a stricter local workflow file, but not a full document spine | [`templates/governed-ai-flow.md`](../templates/governed-ai-flow.md) |
| has formal roadmap governance, multiple agents, staged phases, release gates, runtime boundaries, or compliance needs | [`templates/governed-project/`](../templates/governed-project/) plus [`governed-project-structure.md`](governed-project-structure.md) |

Copy the template into your repository under the filename you chose, then fill in the bracketed decisions. The [`examples/`](../examples/) directory shows both filled in.

## Adapting, not just copying

Lithos is portable because it is generic. Adapt freely:

- Rename roles to match your team, as long as the responsibilities remain owned.
- Add gates or sub-gates if your domain needs them; you **must not** remove the layering of the four defined gates.
- Tighten any rule. You **may** make the standard stricter locally; you **should not** loosen a requirement and still claim conformance.

When you have adapted a template for a project with formal governance, the [`adapt-ai-flow-for-governed-project`](../skills/adapt-ai-flow-for-governed-project/SKILL.md) skill walks through the additions that governance typically requires, including the full source-of-truth chain when workflow-only adoption is too thin.

## Keeping it honest

A local workflow file that no longer matches how the project actually works is worse than none, because it misleads. Review it when the team, tooling, or risk profile changes, and verify it with the [`audit-local-ai-flow`](../skills/audit-local-ai-flow/SKILL.md) skill.
