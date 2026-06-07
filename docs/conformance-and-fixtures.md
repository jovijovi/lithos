# Conformance and Fixtures

A project that says "we follow Lithos" makes a claim others rely on. This document defines **what a project may claim**, **how it declares the claim in a machine-readable way**, and **how evidence and fixtures prove the claim** without turning informative aids into normative requirements.

## What a project may claim

Conformance means a project meets the requirements in the [standard documents](versioning-and-governance.md): assigned [roles](roles.md), the four layered [approval gates](approval-semantics.md), worktree/branch discipline, and evidence-based [verification](verification-standards.md). A project states the version it conforms to (for example, "conforms to Lithos 1.x").

Lithos defines **exactly one governance model: the full lifecycle.** There are no adoption tiers or profiles. A small project keeps the model's anchors concise — terse files, short docs, lessons and practices anchors that are empty but present — yet it never omits governance structure. The full lifecycle covers the local workflow, the assigned roles, the four approval gates, worktree/branch discipline, verification evidence, environment and sandbox boundaries, the adoption manifest, the [knowledge spine](knowledge-governance.md), the static safety scan, and — as applicable — scenario regression and release/supply-chain governance.

A project **may** be stricter than the standard and still conform. It **must not** drop a requirement and claim conformance: a claim that omits roles, collapses the gate layering, abandons isolation, or accepts work without evidence is not a smaller adoption of Lithos — it is not Lithos.

## The adoption manifest

A project declares its conformance in a **machine-readable adoption manifest**: which version it claims, who holds each role, how the gates are operated, the autonomous PR policy in force, and the knowledge governance fields the full-lifecycle model maintains. The manifest is a **declaration, not an authorization**: writing one grants no permission and clears no gate.

- Schema: [`schemas/lithos-adoption-manifest.schema.json`](../schemas/lithos-adoption-manifest.schema.json).
- Fillable template: [`templates/lithos-adoption-manifest.json`](../templates/lithos-adoption-manifest.json).

The manifest is deliberately small, vendor-neutral, and free of secret-shaped or private values; see [tooling interoperability](tooling-interoperability.md) for why these artifacts are portable across agents and tools.

## Evidence and fixtures

A claim is only as good as the evidence behind it. Lithos ships **conformance fixtures** — example adoption manifests that demonstrate what passes and what must fail:

- [`fixtures/conformance/valid-concise-adoption.json`](../fixtures/conformance/valid-concise-adoption.json) — a small project under the one governance model, with every required anchor present but kept terse.
- [`fixtures/conformance/valid-full-lifecycle-governance.json`](../fixtures/conformance/valid-full-lifecycle-governance.json) — the same governance model shown in full detail, with every optional field and the knowledge governance fields populated.
- [`fixtures/conformance/invalid-autonomous-self-merge.json`](../fixtures/conformance/invalid-autonomous-self-merge.json) — a manifest that must be rejected because it claims an agent may self-merge.
- [`fixtures/conformance/invalid-autonomous-self-approval.json`](../fixtures/conformance/invalid-autonomous-self-approval.json) — a manifest that must be rejected because it claims an agent may approve its own pull request.
- [`fixtures/conformance/invalid-live-runtime-without-controls.json`](../fixtures/conformance/invalid-live-runtime-without-controls.json) — a manifest that must be rejected because it declares live/runtime in scope while waiving owner approval and the separate controls real systems require.
- [`fixtures/conformance/invalid-live-runtime-non-object.json`](../fixtures/conformance/invalid-live-runtime-non-object.json) — a manifest that must be rejected because its live/runtime gate is present but is not an object (here `null`), which cannot carry the owner-approval and separate-controls flags the gate requires.
- [`fixtures/conformance/invalid-workflow-path-traversal.json`](../fixtures/conformance/invalid-workflow-path-traversal.json) — a manifest that must be rejected because its local workflow path uses traversal (`..`) to point outside the repository, so it is not a portable repo-relative path. The offending value is non-secret and non-private, so it is safe to commit as a fixture.
- [`fixtures/conformance/invalid-conformance-claim-false.json`](../fixtures/conformance/invalid-conformance-claim-false.json) — a manifest that must be rejected because it sets `conformance_claim.claims_conformance` to `false`: a manifest that declares it does not claim conformance is a non-claim, not a smaller claim, so the checker must not accept it as conforming.

The fixtures are validated by a pure-stdlib checker, [`scripts/verify_conformance_fixtures.py`](../scripts/verify_conformance_fixtures.py), which parses the schema, the template, and the fixtures and enforces the core invariants below. The valid fixtures and the template pass; each invalid fixture fails, and for its intended reason.

### Core invariants

The checker enforces, at minimum, that a conforming manifest:

- is itself a well-formed conformance declaration: it carries the manifest format version this checker validates, names the Lithos version it claims, and **actually claims conformance** — `conformance_claim` is an object whose `claims_conformance` is `true` and whose `statement` is a non-empty string. These fields are checked semantically, not by presence alone, so a manifest with a wrong-typed version, a missing or non-object claim, or `claims_conformance` set to `false` is rejected rather than silently accepted;
- assigns every required [role](roles.md);
- declares the four [approval gates](approval-semantics.md), and keeps owner approval distinct from verification evidence and from run records;
- keeps the live/runtime gate behind owner approval and separate controls even when it is declared out of scope, so the gate can never be silently weakened;
- names a **single, portable repo-relative** local workflow path, rejecting absolute, home or other private machine-local, URL-like, path-traversal, and empty-segment values. A standalone checker cannot know an adopting repository's root, so it verifies the path's **shape**, not the file's physical presence; actual file presence is checked by the adopting project's local verifier and its root workflow file, not by this checker;
- has an [autonomous PR policy](autonomous-pr-policy.md) that does **not** permit agent self-approval, agent self-merge, ownerless auto-merge, ownerless branch deletion, ownerless release or publishing, or live/runtime behavior by default;
- carries the [knowledge governance](knowledge-governance.md) fields, which the full-lifecycle model always maintains — terse anchor values are allowed, but the fields are not optional;
- contains **no** secret-shaped or private machine-local values in any string field — the checker scans the whole manifest recursively and rejects them. (This proves an arbitrary adoption manifest is clean; it is distinct from the repository [static safety scan](static-safety-scan.md), which proves only the committed repository text is clean.)

## Informative versus normative

The line matters, because it decides what a conformance change costs (see [versioning and governance](versioning-and-governance.md)):

- **Normative** — the requirement language (**must** / **should** / **may**) in the [`docs/`](.) standard documents. These define conformance.
- **Informative** — the schema, template, fixtures, the checker, and every example. They *help* a project adopt and *demonstrate* the requirements, but they do not themselves define conformance. A project conforms by meeting the requirements, not by matching a fixture byte for byte.

When the checker and the prose appear to disagree, the prose governs and the checker is corrected.

## How fixture changes are reviewed

Fixtures are evidence, so they are reviewed as evidence:

- A change to a **valid** fixture **must** keep it passing for the right reasons, not merely keep the checker green.
- A change to an **invalid** fixture **must** keep it failing, and failing for the documented reason; weakening it into a pass silently removes a guardrail.
- Adding an invariant to the checker is an additive, informative change unless it also tightens a requirement in the prose, in which case it is normative and follows the [governance](versioning-and-governance.md) process.
- A fixture or schema change that introduces a secret-shaped or private value, a vendor or product name, or a private system reference is rejected.

## Relationship to the rest of Lithos

- The claim is bounded by [versioning and governance](versioning-and-governance.md): conformance is to a stated version.
- The manifest sits beside the other portable artifacts described in [tooling interoperability](tooling-interoperability.md).
- The fixtures are themselves [verification evidence](verification-standards.md): regenerable, inspectable, and reported faithfully.
