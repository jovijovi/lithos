# Autonomous PR Policy

Agents increasingly open and update pull requests on their own. That is useful and, kept inside the [preparation gate](approval-semantics.md), safe. What is **not** safe — and what adopting Lithos never licenses — is an agent advancing its own work past a human decision. This document defines what an agent may do with pull requests autonomously, what it may never self-approve, and which actions require explicit higher-gate owner approval.

## What an agent may do autonomously

Opening and updating a pull request is **preparation**: it is reversible, contained, and proposes rather than integrates. Within the preparation gate, and on an isolated branch or worktree, an agent **may**:

- open a pull request from its working branch;
- update, rebase, or amend its own pull request in response to review or CI;
- attach evidence — tests, CI links, recorded commands and output, an [agent run manifest](agent-run-manifest.md);
- request review and respond to it;
- close a pull request it opened, without deleting shared branches or history.

A pull request is a **proposal**. Creating one asserts nothing about whether the work is approved or sound.

## What an agent may never self-approve

These are reserved to the human [owner](roles.md) and an agent **must never** perform them on its own authority, even one it operated for the owner:

- **Approve its own pull request**, or record an approving review that stands in for the owner's decision.
- **Self-merge** — merging its own pull request, or merging any pull request without the owner's implementation-gate approval for that specific change.
- **Enable ownerless auto-merge** — configuring a merge that lands automatically when checks pass, without explicit owner approval of the merge.
- **Record the business verdict.** An agent may report execution status; whether the result is *accepted* belongs to the owner (see [agent run manifest](agent-run-manifest.md)).

Approval authority is human and is never delegated to an agent. A green check is evidence, not approval; [verification](verification-standards.md) is a precondition for [implementation approval](approval-semantics.md), not a substitute for it.

## What requires explicit higher-gate owner approval

The following are not preparation. Each requires the owner's explicit, contemporaneous, per-action approval at the [gate](approval-semantics.md) named, and an agent **must** stop and request it rather than proceeding:

| Action | Gate required |
|---|---|
| Merging / landing a pull request | Implementation |
| Deleting a branch (including after merge) | Destructive / external |
| Force-push, history rewrite | Destructive / external |
| Publishing a release or package | Destructive / external |
| Sending external communications, mutating external services | Destructive / external |
| Acting against live or production systems, or operating without a human in the loop | Live / runtime |

When it is unclear which gate an action falls under, the agent treats it as the higher gate and asks.

## Lithos is not authorization

This is the load-bearing statement of this document. **Adopting Lithos does not authorize**, and an agent **must not** treat Lithos adoption as authorization for, any of the following without separate, explicit owner approval:

- self-merge or auto-merge of any pull request;
- deletion of branches;
- releasing or publishing packages, artifacts, or communications;
- live, runtime, default-on, or autonomous behavior against real systems;
- any external or destructive side effect.

Lithos's approval semantics are *organizational*: they describe when a human has sanctioned a class of work, not a grant of machine permission. A project that operates at the live/runtime layer **must** define its own separate controls — explicit human authorization, monitoring, kill switches, and audit — which Lithos neither provides nor implies.

## Recording PR activity

When an agent-executed unit needs auditability, the pull request activity is recorded in an [agent run manifest](agent-run-manifest.md): what was authorized, what actually ran (each action marked local/offline or external/live), the verifying evidence, and the boundary that held. The manifest keeps the **approval reference** distinct from the **verification evidence**, and execution status distinct from the owner's business verdict. A manifest records the run; it does not authorize the merge.

## Relationship to the rest of Lithos

- The gates referenced here are defined in [approval semantics](approval-semantics.md); the owner who holds them is defined in [roles](roles.md).
- A project declares its autonomous PR policy in its [adoption manifest](conformance-and-fixtures.md); the forbidden actions above are exactly the invariants the conformance checker enforces.
- The boundary that an autonomous run stayed within is recorded per the [environment and sandbox policy](environment-and-sandbox-policy.md).
