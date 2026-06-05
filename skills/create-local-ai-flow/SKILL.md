---
name: create-local-ai-flow
description: Use when a project is adopting Lithos and needs its local workflow file written from scratch — produces a conformant local AI-collaboration document from the right template, with roles, approval gates, environment boundaries, discipline, verification, and a machine-readable conformance claim filled in.
---

# Create a Local AI Flow

Produce a conformant **local workflow file** for a repository adopting Lithos, plus the companion artifacts that make its conformance claim inspectable. Output is documents the project commits; you do not change runtime behavior or grant any execution authority.

## When to use

- A repository has decided to adopt Lithos and has no local workflow file yet.
- An existing collaboration document needs to be replaced with a conformant one.

## Inputs to gather first

- Project size and contributor model (solo, small team, formal review).
- Whether the project ever operates at the live/runtime layer, and under what existing controls.
- Whether the project bears **behavior** (advertised input/output claims, shipped examples) or **publishes artifacts** others install.
- The environment a run touches: filesystem roots, network need, and which credentials, if any, a task requires.
- Existing conventions: branch naming, CI, review process, where docs live.
- The filename the project wants for the local workflow file (it chooses — do not impose one).

## Steps

1. **Pick the depth and template.** Lithos defines two governed adoption depths and no minimal profile. A **lighter governed workflow** (local workflow file + agent contract + PR checklist) → `templates/governed-ai-flow.md`. A **full governed project** (the lighter surface plus the full authority chain and knowledge spine) → copy `templates/governed-project/` and use `docs/governed-project-structure.md` as the authority map.
2. **Choose the filename with the owner.** Any discoverable name is valid (e.g. `AI_FLOW.md`, `docs/AI_FLOW.md`, `ai-collaborative-development-standards.md`). For full governed adoption, prefer `docs/AI_FLOW.md` and keep `GOAL.md` as the stable source-of-truth index.
3. **Assign roles.** Fill in who holds each role from `docs/roles.md`; state any combined roles. Approval authority is human-only.
4. **Operationalize the four gates.** For each gate in `docs/approval-semantics.md`, write how it is signaled. State plainly whether the project operates at the live/runtime layer; if not, say so.
5. **Declare the environment and sandbox boundary.** From `templates/environment-policy.md` and `docs/environment-and-sandbox-policy.md`, state filesystem roots, network egress/ingress, the **credential scope** bound to least privilege, the external/destructive side effects that leave the workspace, and escalation/abort conditions. Distinguish git worktree isolation (a source-control boundary) from an OS/process sandbox (a runtime boundary).
6. **State discipline.** Branch naming, isolation expectations, and what the integration branch may contain (`docs/core-concepts.md`).
7. **Set the autonomous PR policy.** Per `docs/autonomous-pr-policy.md`, an agent may open, update, and close its own pull request as preparation; it must never perform **self-approval**, **self-merge**, or enable **ownerless auto-merge**. Merging, branch deletion, force-push, releasing, and external communication require explicit higher-gate owner approval.
8. **Define "done."** The reproducible evidence each unit must carry (`docs/verification-standards.md`), the **static safety scan** gate that rejects secret-shaped tokens, private machine-local paths, and unfinished-work placeholders locally and in CI (`docs/static-safety-scan.md`), and — for behavior-bearing projects — a **scenario regression** suite pinning each advertised behavior to a named fixture (`docs/scenario-regression-governance.md`). The static safety scan is safety evidence, **not behavior proof**; behavior is proven by scenario fixtures and tests.
9. **Make the conformance claim machine-readable.** Fill the **adoption manifest** from `templates/lithos-adoption-manifest.json` against its `schemas/lithos-adoption-manifest.schema.json` schema: the version and depth claimed, role holders, gate operation, and the autonomous PR policy. The manifest is a declaration, **not authorization**. The **conformance fixtures** in `fixtures/conformance/` cover valid claims and the **invalid** ones that must be rejected — such as agent self-approval, self-merge, and live/runtime without controls — while ownerless auto-merge stays enforced by the adoption manifest, schema, and checker policy invariants, so the claim stays honest.
10. **Provide for run records.** State where an **agent run manifest** (run record) is retained as audit evidence for an agent-executed unit, keeping the approval reference distinct from the verification evidence and execution status distinct from the owner's verdict (`docs/agent-run-manifest.md`). A manifest records a run; it is **not authorization** for it.
11. **For full governed projects, stand up the knowledge spine and release governance.** Establish the **knowledge spine** — `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, generated `docs/INDEX.md`, and `docs/lessons/_drift_report.md` (`docs/knowledge-governance.md`). For published artifacts, add **release and supply-chain** governance: no agent self-release, a provenance record, pinned dependencies, and owner-approved publishing (`docs/release-and-supply-chain-governance.md`).
12. **Wire companions and resolve every blank.** Add the `templates/AGENTS.md.snippet` contract (or `templates/governed-project/AGENTS.md`) to `AGENTS.md`, adopt `templates/pr-checklist.md`, and reference the local workflow file from `README`, `GOAL.md` where present, and `AGENTS.md`. Leave no bracketed placeholder behind; an unfilled blank is a conformance gap.

## Done when

- The local workflow file exists under the chosen name and is referenced from the project's entry points.
- All four gates are operationalized, the environment and sandbox boundary and credential scope are declared, and the live/runtime stance is explicit.
- The autonomous PR policy forbids self-approval, self-merge, and ownerless auto-merge, and the static safety scan gate is part of "done."
- A schema-valid adoption manifest states the version and depth; behavior-bearing and publishing projects carry scenario regression and release and supply-chain governance.
- Running `audit-local-ai-flow` against it reports no gaps.

## Guardrails

- Never assign approval authority to an agent; an agent run manifest is evidence, **not authorization**.
- You may make a rule stricter locally; do not loosen a Lithos requirement and still call the result conformant.
- Adopting this file does not authorize live, autonomous, or release execution — say so in the file when relevant.
