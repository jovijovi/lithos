# Adopt a Project into Lithos

Bring a repository that has decided to follow Lithos to its first conformant state. The mechanics of writing the local workflow file are the [`create-local-ai-flow`](../../create-local-ai-flow/SKILL.md) skill; this reference frames the adoption decisions around it.

## Decide the depth

Lithos defines two governed adoption depths and **no minimal profile**. A small project adopts a lighter shape, never a weaker one.

- **Lighter governed workflow** — a local workflow file, an `AGENTS.md` contract, and a PR checklist. Start from [`templates/governed-ai-flow.md`](../../../templates/governed-ai-flow.md).
- **Full governed project** — the lighter surface plus the document authority chain and the knowledge spine. Copy [`templates/governed-project/`](../../../templates/governed-project/) and follow [`docs/governed-project-structure.md`](../../../docs/governed-project-structure.md).

Choosing the lighter governed workflow is not dropping a requirement: roles, the four approval gates, isolation discipline, and evidence are preserved either way ([`docs/conformance-and-fixtures.md`](../../../docs/conformance-and-fixtures.md)).

## Produce the artifacts

1. Run [`create-local-ai-flow`](../../create-local-ai-flow/SKILL.md) to write the local workflow file, assign [roles](../../../docs/roles.md), operationalize the four [approval gates](../../../docs/approval-semantics.md), and declare the environment and credential-scope boundary.
2. Fill the **adoption manifest** from [`templates/lithos-adoption-manifest.json`](../../../templates/lithos-adoption-manifest.json) against its [schema](../../../schemas/lithos-adoption-manifest.schema.json), and confirm it the way the [conformance fixtures](../../../fixtures/conformance/) do. The manifest is a declaration, **not authorization**.
3. Wire the [static safety scan](../../../docs/static-safety-scan.md) into the project's definition of done — it is safety evidence, **not behavior proof**.
4. For a behavior-bearing project, pin advertised behaviors with a [scenario regression](../../../docs/scenario-regression-governance.md) suite. For a project that publishes artifacts, add [release and supply-chain](../../../docs/release-and-supply-chain-governance.md) governance.

## Done when

Every gate is operationalized, the manifest is schema-valid, the static safety scan runs locally and in CI, and [audit a project](audit-project.md) reports no gaps. Adoption authorizes nothing on its own; see [agent role boundaries](agent-role-boundaries.md).
