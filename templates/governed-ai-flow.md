<!--
Lithos local workflow file — GOVERNED template.
For projects with formal review, multiple contributors, or compliance needs.
Copy this into your repository under a filename you choose
(e.g. ai-collaborative-development-standards.md), then replace every
[bracketed] decision. Delete this comment when done.
Lithos: https://github.com/jovijovi/lithos
-->

# AI-Collaborative Development Standards — [Project Name]

This project conforms to [Lithos](https://github.com/jovijovi/lithos) [version 1.x]. This document is the single source of truth for how humans and AI collaborate here, and it is itself change-controlled.

> Adopting this workflow does not authorize live or autonomous AI execution. Approvals here are organizational. Any runtime authority is governed separately, below.

## Roles

Review and verification are independent of implementation.

| Role | Held by | Notes |
| --- | --- | --- |
| Owner / approver | [name/group] | Sole approval authority; human only. |
| Controller / operator | [name/group] | Drives sessions; surfaces decisions, does not approve. |
| Architect | [name/group] | Owns design and acceptance criteria. |
| Implementation agent | [agents + names] | Implements within approved scope. |
| Reviewer | [name/group] | Independent of implementation. |
| Verifier | [name/group] | Independent; produces evidence. |

Approval authority is never held by an implementation agent.

## Approval gates and how they are recorded

1. **Preparation / preflight** — isolated, reversible work; standing authorization. No shared/external effect.
2. **Implementation** — merge to `[main]` requires [N approving reviews + owner sign-off], recorded in [the PR]. Scoped to the reviewed change only. An agent may open and update its own pull request, but must never self-approve, self-merge, or enable ownerless auto-merge; merging is the owner's decision.
3. **Destructive / external** — explicit, per-action owner approval, recorded in [location]. Inventory of such actions:
   - [force-push / history rewrite]
   - [publishing a release or package]
   - [deleting branches or data]
   - [sending external communications / mutating external services]
4. **Live / runtime execution** — [out of scope: this project does not operate at this layer]. / [In scope: governed by the separate controls in "Runtime controls" below.]

## Working discipline

- One collaboration unit per branch; branch from `[main]` as `[type/short-description]`.
- Parallel work uses isolated worktrees/checkouts so uncommitted changes never cross units.
- `[main]` contains only reviewed, verified work; protected by [branch protection].

## Environment and sandbox boundaries

This states *where* a run may execute and *what it may touch*. It describes limits; it does not grant capability, and it never authorizes live or autonomous execution.

- **Isolation:** [git worktree isolation per unit; OS/process sandbox, or `none beyond worktree isolation`]. A worktree does not sandbox a process; a sandbox does not version changes.
- **Filesystem roots:** writes confined to [the unit's working tree and declared scratch only]; reads outside the project ([home directory, system configuration, unrelated repositories]) are [denied].
- **Network:** egress [`none` by default for preparation work, or the named destinations/registries genuinely required]; ingress [`none`].
- **Credentials:** [`none`, or the least-privilege, narrowly scoped tokens the task needs, for only as long as it runs]. Secrets are never written into the working tree, logs, or a run manifest; use `[REDACTED]` placeholders.
- **Escalation:** on meeting a boundary — an unexpected credential prompt, a write outside the declared roots, or any action with an external or live effect — stop and request the higher gate rather than working around it.

Keep these decisions here or in a separate change-controlled environment policy.

## Verification — definition of done

A unit is accepted only with reproducible evidence:

- [ ] Tests added/updated and passing; linked [CI] run is green.
- [ ] Reproduction steps recorded for any behavioral change.
- [ ] Independent reviewer's concerns resolved or explicitly accepted by the owner.
- [ ] Failures, skips, and unverified areas reported faithfully.
- [ ] Evidence retained in [location] for audit.

## Audit trail

Approvals, reviews, and verification evidence are retained in [location] so any merged unit can be reconstructed after the fact.

When a unit is agent-executed and needs auditability, retain an agent run manifest per run: what was authorized, what actually ran (each action marked local/offline or external/live), the verifying evidence, and the boundary that held. A manifest records a run; it does not authorize one and never licenses live/runtime execution.

## Runtime controls (only if operating at the live/runtime layer)

[Describe explicit human authorization, monitoring, kill switch, and audit. Lithos does not provide these — they are this project's responsibility.]

## Change control for this document

Normative changes to this file follow [Lithos governance](https://github.com/jovijovi/lithos). Such changes are reviewed like code, and any companion docs (`AGENTS.md`, PR checklist, translations) change together.

## Companions

- Agent contract: `AGENTS.md`.
- PR checklist: `[path/to/pr-checklist.md]`.
- Environment and sandbox policy: this file's boundaries section, or `[path/to/environment-policy.md]`.
- Agent run manifest (per run, when auditability is needed): `[path/to/agent-run-manifest.json]`.
- Adoption manifest declaring the conformance claim: `[path/to/lithos-adoption-manifest.json]`. It is a declaration, not an authorization, and is kept vendor-neutral and portable.
