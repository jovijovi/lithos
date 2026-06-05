# Versioning and Governance

Lithos is a **standard**, so it is versioned and governed as a published document set, not as a continuously shifting codebase. Adopters need to cite a specific version and trust that its meaning is stable.

## Versioning

Lithos uses semantic versioning adapted to a standard:

- **Major (`X`.0.0)** — a change that can break conformance: a new or removed requirement, a redefined gate, a tightened obligation. Adopters may need to change their local workflow file to remain conformant.
- **Minor (x.`Y`.0)** — additive, backward-compatible change: new guidance, new templates, new skills, new examples, clarifications that do not alter existing requirements.
- **Patch (x.y.`Z`)** — corrections that do not change meaning: typos, formatting, broken links, translation fixes.

Each release **should** carry notes describing what changed and, for major releases, what adopters must do to stay conformant. A published release also carries the provenance and gate evidence defined in [release and supply-chain governance](release-and-supply-chain-governance.md), including the exact source revision and the verification checks that passed.

## What is normative

The **normative** content is the requirement language (**must** / **should** / **may**) in the [`docs/`](.) standard documents. Templates, skills, examples, and the conformance aids — the [adoption manifest schema, fixtures, and checker](conformance-and-fixtures.md) — are **informative**: they help adoption and demonstrate the requirements but do not themselves define conformance. A change to informative material is at most a minor release; a change to a requirement is major. Adding or tightening a fixture or checker invariant stays informative unless it also changes a prose requirement, in which case it is normative and follows this process.

## Conformance and claims

A project may state the Lithos version it conforms to (e.g. "conforms to Lithos 1.x"). Conformance means the project meets the requirements defined in [core concepts](core-concepts.md): assigned roles, the four layered approval gates, worktree/branch discipline, and evidence-based verification. A project **may** be stricter than the standard and still conform; it **must not** drop a requirement and claim conformance.

## Changing the standard

- Substantive changes are proposed as pull requests and approved by the human owner, following [`AGENTS.md`](../AGENTS.md).
- A change that adds, removes, or redefines a requirement **must** be identified as normative and flagged for a major release.
- Localized READMEs and any affected documents **must** be updated in the same change so the standard stays internally consistent across languages.
- A release-facing change **must** state whether the [static safety scan](static-safety-scan.md), [scenario regression](scenario-regression-governance.md), and generated drift checks are affected.
- When in doubt whether a change is normative, treat it as normative.

## Translations

The English `README.md` and the `docs/` documents are canonical. Localized READMEs are maintained for accessibility and **must** stay semantically aligned with the canonical text; where a translation and the canonical text appear to conflict, the canonical English governs.

## Deprecation

A requirement that is being removed or replaced **should** first be marked deprecated in a minor release, with guidance, before being changed or removed in a subsequent major release, so adopters have a migration path.
