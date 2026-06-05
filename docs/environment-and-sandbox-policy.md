# Environment and Sandbox Policy

[Approval](approval-semantics.md) decides *whether* work may proceed. An **environment policy** decides *where* it may run and *what it may touch* — filesystem, network, credentials, and side effects. Lithos asks every adopting project to state those boundaries, so that "preparation" is a contained reality rather than an assumption.

This policy is **descriptive of limits, not a grant of capability.** Declaring that a run *may* reach the network does not authorize any particular external action; the higher gates still apply, and adopting this policy never authorizes live or autonomous execution.

## Why a separate policy

Isolation is what makes the preparation gate safe to grant under standing authorization. If the boundary is implicit, an agent's "local" change can quietly read a secret, reach the network, or mutate an external system. A written environment policy turns that boundary into something a reviewer can inspect and a project can enforce.

## Boundaries a policy must address

### Isolation: worktree vs sandbox

These are different layers, and a project should not conflate them:

- **Git worktree isolation** keeps a unit's *version-controlled changes* separate so they stay reviewable and revertible (see [core concepts](core-concepts.md)). It is a source-control boundary.
- **OS / process sandbox** constrains what the running process can *do* — which files it may read or write, and which network, devices, or system calls it may use. It is a runtime boundary.

A worktree does not sandbox a process, and a sandbox does not version changes. State which of each applies.

### Filesystem roots

State the paths a run may read and the paths it may write. Writes should be confined to the unit's working tree and declared scratch locations; reads outside the project — home directory, system configuration, unrelated repositories — should be called out or denied. Describe roots relative to the project or by role; do not record absolute machine paths.

### Network egress and ingress

State whether the run may open outbound connections (egress) and whether anything may connect to it (ingress). Default to no network for preparation-gate work. Where egress is genuinely needed — installing declared dependencies, fetching declared inputs — name the allowed destinations or registries rather than allowing all.

### Credential and secret scope

State which credentials, if any, a run may access, and bind them to least privilege: only the secrets the task needs, only for as long as it runs. Secrets are never written into the working tree, logs, or a run manifest; use redaction placeholders. Read-only and narrowly scoped tokens are preferred over broad ones.

### External side effects and destructive actions

Enumerate the actions that reach outside the workspace or are hard to reverse — publishing, sending communications, mutating external services, deleting or rewriting data or history. None of these is preparation; each requires the destructive/external gate and explicit, per-action owner approval.

### Runtime / live gates

State plainly whether the project operates at the live/runtime layer at all. If it does not, say so. If it does, that layer is governed by separate, deliberate controls — explicit human authorization, monitoring, a kill switch, and audit — which Lithos does not provide. This policy neither implies nor grants them.

### Escalation and abort conditions

State what a run must do when it meets a boundary: stop and request the higher gate rather than work around it. Name the conditions that require an immediate halt — an unexpected credential or authorization prompt, an attempted write outside the declared roots, an action that would have an external or live effect, or any sign that the actual scope exceeds the claimed scope. When it is unclear which gate applies, treat it as the higher gate and ask.

## Recording the boundary that held

The boundary actually in force for a run is recorded in its [agent run manifest](agent-run-manifest.md): whether the run stayed local and offline, any external or live actions taken, and which environment policy applied. The policy sets the limits; the manifest records the reality.

## Template and adoption

Start from [`templates/environment-policy.md`](../templates/environment-policy.md) and fill in the bracketed decisions. A small project may keep this as a section of its [local workflow file](local-adoption.md); a governed project should maintain it as a first-class, change-controlled document. A project may tighten any boundary; it must not loosen these and still claim conformance.
