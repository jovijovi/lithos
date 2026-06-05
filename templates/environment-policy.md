<!--
Lithos environment and sandbox policy template.
Copy this into your repository and replace every [bracketed] decision.
A small project may instead keep these decisions as a section of its
local workflow file; a governed project should maintain this as a
first-class, change-controlled document. Delete this comment when done.
Reference: docs/environment-and-sandbox-policy.md.
Lithos: https://github.com/jovijovi/lithos
-->

# Environment and Sandbox Policy — [Project Name]

This policy states *where* a run may execute and *what it may touch*. It describes limits; it does not grant capability. Declaring that a run *may* reach a resource never authorizes a particular action — the approval gates defined by [Lithos](https://github.com/jovijovi/lithos) still apply, and adopting this policy never authorizes live or autonomous execution.

A project may tighten any boundary below; it must not loosen these and still claim conformance.

## Isolation

State which isolation layers apply, and do not conflate them.

- **Git worktree isolation:** [how version-controlled changes are kept separate and revertible — e.g. one isolated worktree/checkout per collaboration unit].
- **OS / process sandbox:** [whether the running process is constrained, and by what — or `none beyond worktree isolation`].

A worktree does not sandbox a process; a sandbox does not version changes.

## Filesystem roots

- **May read:** [paths, relative to the project or by role].
- **May write:** [the unit's working tree and declared scratch locations only].
- **Must not touch:** [reads outside the project — home directory, system configuration, unrelated repositories].

Describe roots relative to the project or by role; do not record absolute machine paths.

## Network

- **Egress (outbound):** [`none` by default for preparation work, or the named destinations/registries genuinely required, with reason].
- **Ingress (inbound):** [`none`, or what may connect and why].

Where egress is needed, name the allowed destinations rather than allowing all.

## Credentials and secrets

- **Accessible credentials:** [`none`, or the least-privilege, narrowly scoped tokens the task requires, and for how long].
- Secrets are never written into the working tree, logs, or a run manifest; use `[REDACTED]` placeholders.

## External side effects and destructive actions

These are not preparation. Each requires the destructive/external gate and explicit, per-action owner approval:

- [publishing a release or package]
- [sending external communications / mutating external services]
- [deleting or rewriting data or history]

## Runtime / live gates

[State plainly whether the project operates at the live/runtime layer.] / [It does not.] / [It does, governed by the separate controls — explicit human authorization, monitoring, kill switch, and audit — described in the local workflow file. Lithos does not provide them and this policy does not grant them.]

## Escalation and abort

When a run meets a boundary, it stops and requests the higher gate rather than working around it. Halt immediately on:

- an unexpected credential or authorization prompt;
- an attempted write outside the declared roots;
- any action that would have an external or live effect;
- any sign that actual scope exceeds claimed scope.

When it is unclear which gate applies, treat it as the higher gate and ask.

## Recording the boundary that held

The boundary actually in force for each run is recorded in its run manifest (see [`agent-run-manifest.json`](agent-run-manifest.json)): whether the run stayed local and offline, any external or live actions taken, and which environment policy applied. The policy sets the limits; the manifest records the reality.
