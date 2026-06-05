---
title: "Release and supply-chain governance"
status: active
created_at: 2026-06-05
---
# Release and supply-chain governance

> Publishing is a destructive, external action: owner-approved, provenance-bearing, never cut by an agent on its own authority.

This document defines how this project governs the release boundary so that what ships is owner-approved and traceable. Publishing — packaging, tagging for distribution, or pushing an artifact — is a destructive/external action under the approval gates in [`docs/AI_FLOW.md`](../AI_FLOW.md). A project that does not publish records that here and keeps this gate dormant.

## No agent self-release

- An agent must never publish a release, push a package, upload an artifact, or cut a distribution tag on its own authority.
- Releasing is not implied by implementation approval. Approval to merge a change is not approval to publish it; publishing requires its own explicit, per-action owner approval.
- An agent may prepare a release — assemble notes, compute the next version, stage build outputs, draft the provenance record — then stop and request owner approval before anything leaves the repository.

## Release gate

A release proceeds only when all of the following hold and the owner has approved this specific release:

1. The change cleared implementation approval and carries its verification evidence.
2. The project's gates pass on the **exact revision being released** — tests, the static safety scan (`tools/static_safety_scan.py`), and, for behavior-bearing work, the [scenario regression suite](../evaluation/scenario-regression.md).
3. The provenance record below is complete.
4. The owner grants explicit, per-action approval to publish.

Clearing the implementation gate never clears this gate.

## Provenance record

A release carries a provenance record, retained with the project's other evidence, stating:

- the **source revision** the release was built from;
- the **version** assigned, consistent with the project's versioning rules;
- the **checks that passed** on that revision, and where their output is recorded;
- the **approval reference** — who approved the release and when — kept distinct from the verification evidence;
- what was **published, and to where**, with each external action marked as such.

Provenance is records, not authorization. It carries no secrets — signing keys and registry tokens are referenced by `[REDACTED]` placeholder, never written into the record.

## Supply-chain policy

- **Dependencies are declared and pinned**; an unpinned or floating dependency is not a reproducible build.
- **No unreviewed external fetch at build or release time**; build inputs are reviewed, not fetched blindly.
- **No secrets in artifacts or logs**; published artifacts, build logs, and provenance records are scanned by `tools/static_safety_scan.py`.
- **Least-privilege publishing**; publish credentials are narrowly scoped and short-lived, held under the environment policy, and never broadened for convenience.

A project may add stronger controls — artifact signing, attestation, reproducible builds — and should when consumer risk warrants it. It must not drop the rules above and still claim the release was governed.

## Publish boundary

| Action | Gate |
|---|---|
| Merging an approved change to `main` | Implementation |
| Tagging, packaging, publishing, or uploading for distribution | Destructive / external — explicit per-action owner approval |
| Operating a released system live, or default-on autonomous release | Live / runtime — separate controls beyond Lithos |

A green build is evidence the artifact is sound; it is not approval to ship it. When it is unclear which gate a release action falls under, treat it as the higher gate and ask.

## This project's release posture

```text
publishes:       [yes / no]
distribution:    [package registry, artifact store, or "none"]
provenance:      [where release provenance records are retained]
current status:  [e.g. "no releases authorized; standing non-approval in docs/roadmap/current-status.md"]
```
