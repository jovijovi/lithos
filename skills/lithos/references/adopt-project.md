# Adopt a Project into Lithos

Bring a repository that has decided to follow Lithos to its first conformant state: write its **local workflow file** and the companion artifacts that make its conformance claim inspectable. The output is documents the project commits — adoption changes no runtime behavior and grants no execution authority.

## Pick a starting point

Lithos defines **exactly one governance model: the full lifecycle**, with **no adoption tiers** or profiles. A small project keeps the model's anchors concise, never weaker. Pick where to begin within that one model:

- **The local workflow file on its own** — start from [`templates/governed-ai-flow.md`](../../../templates/governed-ai-flow.md), paired with an `AGENTS.md` contract and a PR checklist. This is the component a small or early-stage project writes first; the rest of the structure stays present even when terse.
- **The full structure laid out** — copy [`templates/governed-project/`](../../../templates/governed-project/) and follow [`docs/governed-project-structure.md`](../../../docs/governed-project-structure.md) for the document authority chain and the knowledge spine.

Starting concise is not dropping a requirement: roles, the four approval gates, isolation discipline, and evidence are present either way ([`docs/conformance-and-fixtures.md`](../../../docs/conformance-and-fixtures.md)).

## Write the local workflow file

The owner chooses the filename — any discoverable name is valid (`AI_FLOW.md`, `docs/AI_FLOW.md`, `ai-collaborative-development-standards.md`); when laying out the full structure prefer `docs/AI_FLOW.md` with `GOAL.md` as the stable source-of-truth index. Resolve every bracketed blank — an unfilled blank is a conformance gap. The file must:

1. **Assign [roles](../../../docs/roles.md)**, stating any combined roles; approval authority is human-only.
2. **Operationalize the four [approval gates](../../../docs/approval-semantics.md)** — say how each is signaled — and state plainly whether the project operates at the live/runtime layer.
3. **Declare the environment and sandbox boundary** ([`docs/environment-and-sandbox-policy.md`](../../../docs/environment-and-sandbox-policy.md), [`templates/environment-policy.md`](../../../templates/environment-policy.md)): filesystem roots, network egress/ingress, the **credential scope** bound to least privilege, external/destructive side effects, and escalation/abort conditions. Keep git worktree isolation (a source-control boundary) distinct from an OS/process sandbox (a runtime boundary).
4. **State working discipline** — branch naming, isolation, and what the integration branch may contain ([`docs/core-concepts.md`](../../../docs/core-concepts.md)).
5. **Set the [autonomous PR policy](../../../docs/autonomous-pr-policy.md)** — an agent may open, update, and close its own pull request as preparation but never **self-approval**, **self-merge**, or **ownerless auto-merge**; merging, branch deletion, releasing, and external communication need explicit higher-gate owner approval.
6. **Define "done"** — the reproducible [verification](../../../docs/verification-standards.md) evidence each unit carries, and the [static safety scan](../../../docs/static-safety-scan.md) gate that rejects secret-shaped tokens, private machine-local paths, and unfinished-work placeholders locally and in CI. That scan is safety evidence, **not behavior proof**; behavior is proven by scenario fixtures and tests.

## Make the claim inspectable

1. Fill the **adoption manifest** from [`templates/lithos-adoption-manifest.json`](../../../templates/lithos-adoption-manifest.json) against its [schema](../../../schemas/lithos-adoption-manifest.schema.json) — version, governance model, role holders, gate operation, and the autonomous PR policy — and confirm it the way the [conformance fixtures](../../../fixtures/conformance/) do, including the **invalid** cases that must be rejected. The manifest is a declaration, **not authorization**.
2. For a behavior-bearing project, pin advertised behaviors with a [scenario regression](../../../docs/scenario-regression-governance.md) suite. For a project that publishes artifacts, add [release and supply-chain](../../../docs/release-and-supply-chain-governance.md) governance.
3. Where agent-executed units need auditability, retain an [agent run manifest](../../../docs/agent-run-manifest.md) for each run as a record — **not authorization** — keeping the approval reference distinct from the verification evidence.

## Done when

Every gate is operationalized, the environment and credential-scope boundary is declared, the manifest is schema-valid, the static safety scan runs locally and in CI, the file is referenced from the project's entry points, and [audit a project](audit-project.md) reports no gaps. Adoption authorizes nothing on its own; see [agent role boundaries](agent-role-boundaries.md).
