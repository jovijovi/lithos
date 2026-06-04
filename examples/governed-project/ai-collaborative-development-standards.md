# AI-Collaborative Development Standards — Granite

This project conforms to [Lithos](https://github.com/jovijovi/lithos) version 1.x. This document is the single source of truth for how humans and AI collaborate here, and it is itself change-controlled.

> Adopting this workflow does not authorize live or autonomous AI execution. Approvals here are organizational. Any runtime authority is governed separately, below.

## Roles

Review and verification are independent of implementation.

| Role | Held by | Notes |
| --- | --- | --- |
| Owner / approver | Maintainers group (2 leads) | Sole approval authority; human only. |
| Controller / operator | Contributing engineer running the session | Drives the session; surfaces decisions, does not approve. |
| Architect | Assigned design owner per change | Owns design and acceptance criteria. |
| Implementation agent | AI agents + the contributing engineer | Implement within approved scope. |
| Reviewer | A maintainer not involved in implementation | Independent review. |
| Verifier | CI plus a maintainer confirming evidence | Independent of implementation. |

Approval authority is never held by an implementation agent.

## Approval gates and how they are recorded

1. **Preparation / preflight** — isolated, reversible work; standing authorization. No shared or external effect.
2. **Implementation** — merge to `main` requires one approving review from an independent maintainer plus owner sign-off, recorded in the pull request. Scoped to the reviewed change only.
3. **Destructive / external** — explicit, per-action owner approval, recorded as a comment on the relevant issue or PR. Inventory of such actions:
   - Force-push or history rewrite on any shared branch.
   - Publishing a release or package to the registry.
   - Deleting branches, tags, or data.
   - Sending external communications or mutating external services.
4. **Live / runtime execution** — Granite is a library; agents do **not** execute against production. The project does not operate at the live/runtime layer, so the runtime controls section below is intentionally marked not applicable.

## Working discipline

- One collaboration unit per branch; branch from `main` as `feat/...`, `fix/...`, or `chore/...`.
- Parallel work uses isolated git worktrees so uncommitted changes never cross units.
- `main` contains only reviewed, verified work; protected by branch protection requiring review and green CI.

## Verification — definition of done

A unit is accepted only with reproducible evidence:

- [ ] Tests added/updated and passing; the linked CI run is green.
- [ ] Reproduction steps recorded for any behavioral change.
- [ ] The independent reviewer's concerns are resolved or explicitly accepted by the owner.
- [ ] Failures, skips, and unverified areas are reported faithfully.
- [ ] Evidence retained on the PR and in CI history for audit.

## Audit trail

Approvals, reviews, and verification evidence are retained on the pull request and in CI run history, so any merged unit can be reconstructed after the fact.

## Runtime controls

Not applicable — this project does not operate at the live/runtime layer (see gate 4).

## Change control for this document

Normative changes to this file follow [Lithos governance](https://github.com/jovijovi/lithos). Such changes are reviewed like code, and any companion documents (`AGENTS.md`, the PR checklist, translations) change together.

## Companions

- Agent contract: `AGENTS.md`.
- PR checklist: `.github/PULL_REQUEST_TEMPLATE.md`.
