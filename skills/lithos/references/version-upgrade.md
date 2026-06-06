# Upgrade a Project to a Newer Lithos Version

Move a project from the Lithos version it currently claims to a newer one, changing only what the version delta requires. This is distinct from deepening governance ([governed upgrade](governed-upgrade.md)); here the depth may stay the same while the standard itself has moved.

## Compare claimed against current

1. Read the **claimed Lithos version** from the project's adoption manifest and local workflow file.
2. Read the **current Lithos version** the project intends to adopt, and the [versioning and governance](../../../docs/versioning-and-governance.md) notes for the releases in between. A major release can change or add a requirement; a minor release is additive; a patch changes no meaning.
3. Derive the **missing deltas** — the specific requirements added, redefined, or tightened between the two versions.

## Patch only the missing deltas

Apply each missing delta and nothing more; do not rewrite conformant sections that did not change. For every delta, update the artifacts **together** so they cannot drift apart:

- the **adoption manifest** — the claimed version and any new fields — against its [schema](../../../schemas/lithos-adoption-manifest.schema.json);
- the local workflow file, the `AGENTS.md` contract, and the PR checklist;
- any [templates](../../../templates/) the project vendored, and the project's own docs;
- the project's verifiers, so a new requirement is actually enforced, not merely described.

## Done when

The manifest names the new version, every changed artifact moved with it, and the project's gates are **re-verified fresh** on the result — the local verifier, the [static safety scan](../../../docs/static-safety-scan.md), and any [scenario regression](../../../docs/scenario-regression-governance.md) suite all pass on the upgraded revision. Then run [audit a project](audit-project.md) to confirm no delta was missed.
