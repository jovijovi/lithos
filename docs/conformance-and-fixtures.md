# Conformance and Fixtures

A project that says "we follow Lithos" makes a claim others rely on. This document defines **what a project may claim**, **how it declares the claim in a machine-readable way**, and **how evidence and fixtures prove the claim** without turning informative aids into normative requirements.

## What a project may claim

Conformance means a project meets the requirements in the [standard documents](versioning-and-governance.md): assigned [roles](roles.md), the four layered [approval gates](approval-semantics.md), worktree/branch discipline, and evidence-based [verification](verification-standards.md). A project states the version it conforms to (for example, "conforms to Lithos 1.x").

Lithos defines **two governed adoption depths** and **no minimal profile**:

- **Lighter governed workflow** — a local workflow file, an agent contract, and a PR checklist. Thinner than a full spine, but it still preserves roles, gates, isolation, and evidence.
- **Full governed project** — the lighter surface plus the full documentation authority chain and the [knowledge spine](knowledge-governance.md).

A project **may** be stricter than the standard and still conform. It **must not** drop a requirement and claim conformance: a claim that omits roles, collapses the gate layering, abandons isolation, or accepts work without evidence is not a smaller adoption of Lithos — it is not Lithos.

## The adoption manifest

A project declares its conformance in a **machine-readable adoption manifest**: which version and depth it claims, who holds each role, how the gates are operated, the autonomous PR policy in force, and — for full governed projects — the knowledge governance fields. The manifest is a **declaration, not an authorization**: writing one grants no permission and clears no gate.

- Schema: [`schemas/lithos-adoption-manifest.schema.json`](../schemas/lithos-adoption-manifest.schema.json).
- Fillable template: [`templates/lithos-adoption-manifest.json`](../templates/lithos-adoption-manifest.json).

The manifest is deliberately small, vendor-neutral, and free of secret-shaped or private values; see [tooling interoperability](tooling-interoperability.md) for why these artifacts are portable across agents and tools.

## Evidence and fixtures

A claim is only as good as the evidence behind it. Lithos ships **conformance fixtures** — example adoption manifests that demonstrate what passes and what must fail:

- [`fixtures/conformance/valid-lighter-governed-workflow.json`](../fixtures/conformance/valid-lighter-governed-workflow.json) — a conforming lighter governed workflow.
- [`fixtures/conformance/valid-full-governed-project.json`](../fixtures/conformance/valid-full-governed-project.json) — a conforming full governed project, with the knowledge governance fields populated.
- [`fixtures/conformance/invalid-autonomous-self-merge.json`](../fixtures/conformance/invalid-autonomous-self-merge.json) — a manifest that must be rejected because it claims an agent may self-merge.
- [`fixtures/conformance/invalid-autonomous-self-approval.json`](../fixtures/conformance/invalid-autonomous-self-approval.json) — a manifest that must be rejected because it claims an agent may approve its own pull request.
- [`fixtures/conformance/invalid-live-runtime-without-controls.json`](../fixtures/conformance/invalid-live-runtime-without-controls.json) — a manifest that must be rejected because it declares live/runtime in scope while waiving owner approval and the separate controls real systems require.
- [`fixtures/conformance/invalid-live-runtime-non-object.json`](../fixtures/conformance/invalid-live-runtime-non-object.json) — a manifest that must be rejected because its live/runtime gate is present but is not an object (here `null`), which cannot carry the owner-approval and separate-controls flags the gate requires.

The fixtures are validated by a pure-stdlib checker, [`scripts/verify_conformance_fixtures.py`](../scripts/verify_conformance_fixtures.py), which parses the schema, the template, and the fixtures and enforces the core invariants below. The valid fixtures and the template pass; each invalid fixture fails, and for its intended reason.

### Core invariants

The checker enforces, at minimum, that a conforming manifest:

- assigns every required [role](roles.md);
- declares the four [approval gates](approval-semantics.md), and keeps owner approval distinct from verification evidence and from run records;
- keeps the live/runtime gate behind owner approval and separate controls even when it is declared out of scope, so the gate can never be silently weakened;
- names a **single, present** local workflow file;
- has an [autonomous PR policy](autonomous-pr-policy.md) that does **not** permit agent self-approval, agent self-merge, ownerless auto-merge, ownerless branch deletion, ownerless release or publishing, or live/runtime behavior by default;
- carries the [knowledge governance](knowledge-governance.md) fields when it claims full governed project adoption;
- requires **no** secret-shaped or private values.

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
