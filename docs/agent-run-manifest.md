# Agent Run Manifest and Audit Log

When a human or an AI agent executes a collaboration unit, Lithos expects a record that makes the run reconstructable after the fact: an **agent run manifest** (equivalently, a run record or audit-log entry). It captures what a run was authorized to do, what it actually did, and the evidence and boundaries involved.

A manifest is a **record, not an authorization.** Writing or storing one grants no permission and clears no [gate](approval-semantics.md). It documents a run; it never sanctions one. Adopting Lithos does not authorize live or autonomous execution, and a manifest that describes a live action does not retroactively license it.

## What a manifest is for

- Reconstruct a run from durable evidence rather than from chat history or memory.
- Let an independent reviewer or verifier see, side by side, what was claimed and what happened.
- Preserve the boundary that actually held — what stayed local and offline, and what reached outside.

## Distinctions a manifest must keep separate

A manifest is only useful if it refuses to blur these:

1. **Approval reference vs verification evidence.** The *approval reference* points to the human sanction that allowed the work — which [gate](approval-semantics.md), who granted it, and the scope it covers. The *verification evidence* is the inspectable proof that the work does what it claims. One says "this was allowed"; the other says "this is sound." A manifest records both and never lets one stand in for the other. See [verification standards](verification-standards.md).
2. **Execution status vs business verdict.** *Execution status* is how the run ended — completed, partial, failed, or aborted. The *business verdict* is whether the result is accepted — pending, accepted, or rejected — and it belongs to the owner. A run can complete cleanly and still be rejected; a run can fail and still produce something worth keeping. Recording one as the other is a common and costly error.
3. **Claimed scope vs actual commands and artifacts.** The *claimed scope* is what the unit was asked to do and what it deliberately excludes. The *actual* record is the commands or actions that ran and the artifacts they produced. A reviewer compares the two; silent scope-widening shows up precisely here.
4. **Local/offline vs external/live/runtime boundary.** Each recorded action is marked as contained — local, offline, reversible, no external effect — or as crossing outward to an external, live, or runtime system. The manifest must make plain which actions, if any, left the isolated workspace, and under which higher-gate approval. See [environment and sandbox policy](environment-and-sandbox-policy.md).
5. **Redaction and retention.** Secrets, tokens, credentials, and private identifiers are redacted before a manifest is stored; the manifest records that redaction happened and how. It also records where it is retained and for how long, so an audit is possible without re-exposing sensitive material.
6. **Unverified or skipped evidence.** A manifest states plainly what was *not* verified and what was skipped, and why. An honest gap is more valuable than an implied pass: absence of a claim is not evidence, and the manifest names the absence.

## Required content

At minimum, a run manifest should carry:

- **Identity** — the collaboration unit, branch, and repository it belongs to.
- **Roles** — who held owner, controller, implementation, review, and verification for this run (see [roles](roles.md)).
- **Approval reference** — the gate cleared, who granted it, the scope it covers, and where that approval is recorded. This is a pointer, not the evidence.
- **Claimed scope** — intent, in-scope items, and explicit non-goals or non-approvals.
- **Actual execution** — status, time bounds, the commands or actions run (each marked local/offline or external/live/runtime), and the artifacts produced.
- **Verification evidence** — reproducible evidence (tests, CI, recorded steps) with results, the independent-review outcome, and an explicit list of unverified or skipped items.
- **Verdict** — execution status kept distinct from the owner's business verdict.
- **Boundary** — whether the run stayed local and offline, any external or live actions taken, and a reference to the environment policy in force.
- **Redaction and retention** — confirmation that secrets were redacted, the method used, and where and how long the manifest is kept.

A copy-ready schema is in [`templates/agent-run-manifest.json`](../templates/agent-run-manifest.json); fill in the bracketed values for each run.

## Relationship to the rest of Lithos

- It is **evidence**, governed by [verification standards](verification-standards.md): the manifest is itself something a third party can inspect, and it must report results faithfully.
- It references, but does not replace, [approval](approval-semantics.md): the approval reference points to a human decision recorded elsewhere.
- It is bounded by the [environment and sandbox policy](environment-and-sandbox-policy.md): the manifest records which boundary actually held.
- For governed projects, manifests are retained alongside dev-log and verification evidence; see [governed project structure](governed-project-structure.md).

## Honesty obligations

The honesty rules that bind verification bind the manifest. Never record a run as passing without having observed the verifying output, never round a partial result up to "done," and surface failures and unverified areas rather than smoothing them over. A manifest that flatters the run is worse than none, because it will be trusted in an audit.
