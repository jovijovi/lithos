# Approval Semantics

Most AI-collaboration incidents come from treating approval as a single yes. Lithos requires that approval be **layered**: four distinct gates, each granting a strictly narrower license than the name might suggest. Clearing one gate **never** implies clearing a higher one.

Approval is always an act a **human owner** takes (see [roles](roles.md)). An agent may request approval; it may not grant it to itself.

## The four gates

### 1. Preparation / preflight

**Licenses:** reading, analysis, drafting, planning, and changes confined to an isolated working tree that touch nothing shared and have no external effect.

- This is the default working state for an implementation agent.
- It includes writing code, editing docs, and running read-only or sandboxed commands locally.
- It does **not** license merging, publishing, or anything observable outside the isolated workspace.

Preparation may often proceed under a standing, general authorization, because it is reversible and contained.

### 2. Implementation approval

**Licenses:** integrating a prepared change into shared project state — merging to the integration branch, landing a pull request, committing to a branch others build on.

- Scoped to the specific change reviewed. Approval of one unit is not approval of adjacent edits.
- Requires that [verification](verification-standards.md) evidence exists and that review concerns are resolved.
- Does **not** license destructive or external side effects beyond the integration itself.

### 3. Destructive / external side-effect approval

**Licenses:** actions that are hard to reverse or that reach outside the repository — history rewrites, force-pushes, deleting branches or data, publishing a release or package, sending communications, mutating external services.

- Requires **explicit, contemporaneous** owner approval for the specific action. A standing authorization does not cover this gate.
- The actor **must** describe the action and its blast radius before acting, and confirm the target matches expectations.
- Approval is per-action, not per-session.

### 4. Live / runtime execution approval

**Licenses:** an AI acting against live or production systems, or operating autonomously without a human in the immediate loop.

- This gate is outside the scope of what adopting Lithos grants. Lithos is a development-collaboration standard, **not** an execution product, and adopting it does **not** authorize live or autonomous AI execution.
- A project that chooses to operate at this layer **must** define its own additional controls — explicit human authorization, monitoring, kill switches, and audit — separately and deliberately. Lithos neither provides nor implies them.

## Rules that bind all gates

- **No implicit escalation.** Being cleared for a lower gate never auto-clears a higher one.
- **Scope is explicit.** An approval covers the work described and nothing more.
- **Approval is human.** Agents propose and request; owners grant.
- **Default to asking.** When it is unclear which gate an action falls under, treat it as the higher gate and request approval.
- **Record it.** The approval, its scope, and who gave it **should** be recoverable after the fact.

## Mapping to a local project

An adopting project records, in its [local workflow file](local-adoption.md), how each gate is signaled in practice (e.g. how implementation approval is given, which actions count as destructive, and — if applicable — whether the project operates at the live/runtime layer at all and under what separate controls).
