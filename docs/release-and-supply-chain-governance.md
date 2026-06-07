# Release and Supply-Chain Governance

Publishing a release is the moment a project's work crosses from its own repository into the world: a package others install, an artifact others run, a version others depend on. It is **destructive and external** in the sense of [approval semantics](approval-semantics.md) — hard to take back once downstream consumers have it. Lithos governs the release boundary so that what ships is owner-approved, provenance-bearing, and never published by an agent on its own authority.

This document defines the release gate, the provenance evidence a release carries, the supply-chain rules a build obeys, and the boundary that keeps publishing distinct from ordinary development approval. It is part of Lithos's one [full-lifecycle governance model](governed-project-structure.md) and applies to any project that publishes releases.

## No agent self-release

The load-bearing rule, consistent with the [autonomous PR policy](autonomous-pr-policy.md):

- An agent **must never** publish a release, push a package, upload an artifact, or cut a tag intended for distribution on its own authority.
- Releasing is **not** implied by [implementation approval](approval-semantics.md). Approval to merge a change is not approval to publish it; publishing requires its own explicit, contemporaneous, per-action owner approval at the destructive/external gate.
- An agent **may** prepare a release as [preparation](approval-semantics.md) — assemble notes, compute the next version, stage build outputs, draft the provenance record — and then **stop and request owner approval** before anything leaves the repository.

Adopting Lithos is **not** authorization to publish. A project that releases **must** keep the act behind a human decision.

## The release gate

A release proceeds only when all of the following hold, and the owner has approved this specific release:

1. The change being released has cleared [implementation approval](approval-semantics.md) and carries its [verification evidence](verification-standards.md).
2. The project's gates pass on the **exact revision being released** — tests, the [static safety scan](static-safety-scan.md), and, for behavior-bearing projects, the [scenario regression suite](scenario-regression-governance.md).
3. The release's **provenance record** (below) is complete.
4. The owner grants explicit, per-action approval to publish.

Clearing the implementation gate never clears this gate; a project that operates at the live/runtime layer governs that separately under its own controls.

## Provenance and release evidence

A release carries a **provenance record** so any published artifact can be traced back to how it was produced and approved. It is part of the governed [evidence](verification-standards.md) chain — retained, not discarded after publish — and states:

- the **source revision** (commit) the release was built from;
- the **version** assigned, consistent with [versioning and governance](versioning-and-governance.md);
- the **checks that passed** on that revision, and where their output is recorded;
- the **approval reference** — who approved the release and when — kept distinct from the verification evidence, exactly as a [run manifest](agent-run-manifest.md) keeps approval distinct from proof;
- what was **published, and to where**, with each external action marked as such.

Provenance is **records, not authorization**: it documents a release that an owner approved; it never substitutes for that approval. Like every portable artifact, it carries no secrets — signing keys, registry tokens, and credentials are referenced by redacted placeholder, never written into the record (see [tooling interoperability](tooling-interoperability.md)).

## Supply-chain policy

The integrity of what ships depends on the integrity of what goes into it:

- **Dependencies are declared and pinned.** A build resolves to known versions; an unpinned or floating dependency is not a reproducible build.
- **No unreviewed external fetch at build or release time.** Pulling and executing arbitrary remote content during a build is an external side effect and is governed as one; build inputs are reviewed, not fetched blindly.
- **No secrets in artifacts or logs.** Published artifacts, build logs, and provenance records are scanned by the [static safety scan](static-safety-scan.md); a credential-shaped or private value blocks the release.
- **Least-privilege publishing.** Credentials used to publish are narrowly scoped and short-lived, held under the [environment and sandbox policy](environment-and-sandbox-policy.md), and never broadened to make a release convenient.

A project **may** add stronger supply-chain controls — artifact signing, attestation, reproducible builds — and **should** when its consumers' risk warrants it. It **must not** drop the rules above and still claim the release was governed.

## The publish boundary

Keep these distinct, because collapsing them is how unapproved releases happen:

| Action | Gate |
|---|---|
| Merging an approved change to the integration branch | Implementation |
| Tagging, packaging, publishing, or uploading for distribution | Destructive / external — explicit per-action owner approval |
| Operating a released system live, or default-on autonomous release | Live / runtime — separate controls beyond Lithos |

A green build is [evidence](verification-standards.md) the artifact is sound; it is not approval to ship it. When it is unclear which gate a release action falls under, treat it as the higher gate and ask.

## Relationship to the rest of Lithos

- Releasing is a destructive/external action under [approval semantics](approval-semantics.md) and a forbidden ownerless action under the [autonomous PR policy](autonomous-pr-policy.md).
- Versioning of a release follows [versioning and governance](versioning-and-governance.md).
- Release evidence is [verification evidence](verification-standards.md), gated by the [static safety scan](static-safety-scan.md) and the [scenario regression suite](scenario-regression-governance.md), and recorded alongside other governed artifacts under [knowledge governance](knowledge-governance.md).
- Provenance and supply-chain records are vendor-neutral, secret-free portable artifacts per [tooling interoperability](tooling-interoperability.md).
