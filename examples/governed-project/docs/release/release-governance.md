---
title: "Granite Release and Supply-Chain Governance"
status: active
created_at: 2026-06-05
---
# Granite Release and Supply-Chain Governance

> Granite ships to downstream consumers, so publishing is governed as a destructive, external action: owner-approved, provenance-bearing, never cut by an agent.

A published Granite version is hard to take back once consumers depend on it. Releasing — packaging, tagging for distribution, or pushing an artifact — is a destructive/external action under the approval gates in [`docs/AI_FLOW.md`](../AI_FLOW.md). Granite currently authorizes no releases; this document defines the gate a future release must clear.

## No agent self-release

- An agent must never publish a Granite release, push a package, upload an artifact, or cut a distribution tag on its own authority.
- Releasing is not implied by implementation approval; publishing needs its own explicit, per-action owner approval.
- An agent may prepare a release — draft notes, compute the next version, stage build outputs, draft the provenance record — then stop and request owner approval before anything leaves the repository.

## Release gate

A Granite release proceeds only when all of the following hold and the owner has approved this specific release:

1. The change cleared implementation approval and carries its verification evidence.
2. Granite's gates pass on the **exact revision being released** — tests, the static safety scan (`tools/static_safety_scan.py`), and the [scenario regression suite](../evaluation/scenario-regression.md).
3. The provenance record below is complete.
4. The owner grants explicit, per-action approval to publish.

## Provenance record

Each Granite release carries a provenance record, retained with the project's other evidence, stating:

- the **source revision** the release was built from;
- the **version** assigned, consistent with Granite's versioning rules;
- the **checks that passed** on that revision, and where their output is recorded;
- the **approval reference** — who approved the release and when — kept distinct from the verification evidence;
- what was **published, and to where**, with each external action marked as such.

Provenance is records, not authorization, and carries no secrets: signing keys and registry tokens appear only as `[REDACTED]` placeholders.

## Supply-chain policy

- **Dependencies are declared and pinned** so a Granite build resolves to known versions.
- **No unreviewed external fetch at build or release time**; build inputs are reviewed, not fetched blindly.
- **No secrets in artifacts or logs**; release artifacts, build logs, and provenance records are scanned by `tools/static_safety_scan.py`.
- **Least-privilege publishing**; publish credentials are narrowly scoped and short-lived, held under the environment policy and never broadened for convenience.

## Publish boundary

| Action | Gate |
|---|---|
| Merging an approved change to `main` | Implementation |
| Tagging, packaging, or publishing a Granite distribution | Destructive / external — explicit per-action owner approval |
| Operating a released system live or default-on | Live / runtime — separate controls beyond Lithos |

## Current release posture

```text
publishes:       intended for downstream consumers; no releases authorized yet
distribution:    to be decided at the first release phase
provenance:      retained alongside dev-log and verification evidence
current status:  standing non-approval — see docs/roadmap/current-status.md
```

A green build is evidence the artifact is sound; it is not approval to ship it.
