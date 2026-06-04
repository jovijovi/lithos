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
2. **Implementation** — merge to `[main]` requires [N approving reviews + owner sign-off], recorded in [the PR]. Scoped to the reviewed change only.
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

## Verification — definition of done

A unit is accepted only with reproducible evidence:

- [ ] Tests added/updated and passing; linked [CI] run is green.
- [ ] Reproduction steps recorded for any behavioral change.
- [ ] Independent reviewer's concerns resolved or explicitly accepted by the owner.
- [ ] Failures, skips, and unverified areas reported faithfully.
- [ ] Evidence retained in [location] for audit.

## Audit trail

Approvals, reviews, and verification evidence are retained in [location] so any merged unit can be reconstructed after the fact.

## Runtime controls (only if operating at the live/runtime layer)

[Describe explicit human authorization, monitoring, kill switch, and audit. Lithos does not provide these — they are this project's responsibility.]

## Change control for this document

Normative changes to this file follow [Lithos governance](https://github.com/jovijovi/lithos). Such changes are reviewed like code, and any companion docs (`AGENTS.md`, PR checklist, translations) change together.

## Companions

- Agent contract: `AGENTS.md`.
- PR checklist: `[path/to/pr-checklist.md]`.
