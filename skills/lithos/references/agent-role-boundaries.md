# Agent Role Boundaries

Every Lithos intent preserves the same boundary: humans approve, agents propose. This reference states what that means operationally so an agent does not quietly cross it.

## Owner-held approval

Approval is an act a human [owner](../../../docs/roles.md) takes. **Approval authority is human-only** and is never delegated to an agent. Across the four [approval gates](../../../docs/approval-semantics.md), an agent may *request* approval and *report* execution status; it may not *grant* approval or record the business verdict of whether the result is accepted. Clearing a lower gate never auto-clears a higher one.

## Independent review and verification

Where the project's size allows, the reviewer and verifier are **independent of the implementation** role ([`docs/roles.md`](../../../docs/roles.md)). Review is for substance, not politeness; verification is by reproducible evidence, not agreement. When roles are combined in a small project, the local workflow file says so, so the combination is a deliberate choice rather than an accident.

## What an agent may never self-grant

Per the [autonomous PR policy](../../../docs/autonomous-pr-policy.md), an agent must never perform **self-approval**, **self-merge**, or **ownerless auto-merge**, and must never release, delete shared branches, rewrite history, or act on live systems without explicit, contemporaneous owner approval. An [agent run manifest](../../../docs/agent-run-manifest.md) records what was authorized and what ran; it is evidence, **not authorization**.

When multiple agents collaborate, these boundaries hold per agent: no agent approves another's work in the owner's place, and the controller surfaces decisions to the owner rather than originating them.
