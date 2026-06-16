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
5. **Declare the environment and sandbox boundaries.** State where a run may execute and what it may touch — filesystem roots, network egress, credentials, and external side effects — following the [environment and sandbox policy](environment-and-sandbox-policy.md). A small project may keep these decisions as a section of this file; as the project grows they should be promoted to a first-class, change-controlled document.

It **should** also list the project's destructive/external actions explicitly, point to its PR checklist, and — when agent-executed collaboration units need auditability — retain an [agent run manifest](agent-run-manifest.md) for each run so a reviewer can reconstruct what was authorized and what actually happened.

## Recommended companion files

- An `AGENTS.md` (or equivalent) carrying the agent-facing contract — start from [`templates/AGENTS.md.snippet`](../templates/AGENTS.md.snippet).
- A PR checklist — start from [`templates/pr-checklist.md`](../templates/pr-checklist.md).
- An environment and sandbox policy declaring run boundaries — start from [`templates/environment-policy.md`](../templates/environment-policy.md). A small project may instead fold these decisions into the local workflow file, as long as they are present.
- An agent run manifest for runs that need auditability — start from [`templates/agent-run-manifest.json`](../templates/agent-run-manifest.json).
- An adoption manifest declaring the Lithos version, the single `full-lifecycle-governance` model, the role holders, how the gates operate, the verification stance, and the [autonomous PR policy](autonomous-pr-policy.md) in force — start from [`templates/lithos-adoption-manifest.json`](../templates/lithos-adoption-manifest.json) against [`schemas/lithos-adoption-manifest.schema.json`](../schemas/lithos-adoption-manifest.schema.json). It is a declaration, not an authorization; see [conformance and fixtures](conformance-and-fixtures.md). These artifacts stay vendor-neutral and portable — see [tooling interoperability](tooling-interoperability.md).
- A root `LESSONS.md`, `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, generated `docs/INDEX.md`, and generated `docs/lessons/_drift_report.md` keep reusable knowledge out of chat history, governed as durable artifacts per [knowledge governance](knowledge-governance.md). A small project keeps these anchors present but concise.
- Roadmap, current-status, and dev-log records stay lean: add them when they change phase authority, current decisions, open tails, user-visible truth, or a safety boundary. They are status evidence, not behavior or safety proof, and should not duplicate git history, CI, PR metadata, generated indexes, or drift reports.
- A static safety scanner, usually under `tools/static_safety_scan.py`, enforces the [static safety scan](static-safety-scan.md) gate with the other local checks.
- Behavior-bearing projects should add scenario fixtures and a local scenario-regression note following [scenario regression governance](scenario-regression-governance.md).
- Projects that publish packages, tags, or distributed artifacts should add a release-governance note following [release and supply-chain governance](release-and-supply-chain-governance.md).
- If localized README files exist, keep them semantically aligned with `README.md` whenever visible project claims change.

## Choosing a starting point

Lithos defines **one governance model: the full lifecycle.** It does **not** define a minimal or lite tier. Lithos can be lightweight — a small project keeps its files terse and its lessons and practices anchors empty but present — yet it is never minimalized: roles, approval gates, working discipline, and evidence are present at any size. Dropping any of those is not a smaller adoption of Lithos — it is no longer Lithos.

The templates are components of that one model, not separate paths:

| Start from | What it gives you |
| --- | --- |
| [`templates/governed-ai-flow.md`](../templates/governed-ai-flow.md) | The local workflow file on its own — the component a small or early-stage project writes first, kept concise while the rest of the structure stays present. |
| [`templates/governed-project/`](../templates/governed-project/) plus [`governed-project-structure.md`](governed-project-structure.md) | The full lifecycle structure laid out end to end — document authority chain, knowledge spine, and verification tooling — for formal roadmap governance, multiple agents, staged phases, release gates, runtime boundaries, or compliance needs. |

Copy what you start from into your repository under the filename you chose, then fill in the bracketed decisions. The [`examples/`](../examples/) directory shows the model filled in end to end.

If an installed agent is doing the adoption work, start from the [`lithos`](../skills/lithos/SKILL.md) umbrella skill. It is the operational entry point that routes the agent to the focused create, audit, governed-upgrade, version-upgrade, PR-review, and release-gate procedures while keeping this document and the rest of `docs/` authoritative.

## Adapting, not just copying

Lithos is portable because it is generic. Adapt freely:

- Rename roles to match your team, as long as the responsibilities remain owned.
- Add gates or sub-gates if your domain needs them; you **must not** remove the layering of the four defined gates.
- Tighten any rule. You **may** make the standard stricter locally; you **should not** loosen a requirement and still claim conformance.

As a project grows, the [`lithos`](../skills/lithos/SKILL.md) skill's [governed-upgrade](../skills/lithos/references/governed-upgrade.md) procedure walks through filling the model's concise anchors in with full detail — the document authority chain, knowledge spine, scenario regression, and release governance — without ever loosening a requirement.

## Keeping it honest

A local workflow file that no longer matches how the project actually works is worse than none, because it misleads. Review it when the team, tooling, or risk profile changes, and verify it with the [`lithos`](../skills/lithos/SKILL.md) skill's [audit-project](../skills/lithos/references/audit-project.md) procedure. Keep the adoption manifest honest the same way: its path and retention location are local choices, but a project claiming Lithos conformance must keep the manifest describing how the project actually operates, and a claim that drops a requirement is not a smaller Lithos adoption — see [conformance and fixtures](conformance-and-fixtures.md).
