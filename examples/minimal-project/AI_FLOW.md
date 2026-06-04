# AI Collaboration Workflow — Pebble

This project follows [Lithos](https://github.com/jovijovi/lithos). This file is our single source of truth for how humans and AI collaborate here.

> Adopting this workflow does not authorize live or autonomous AI execution. Approvals here are organizational, not a grant of machine permission.

## Roles

Single-maintainer project — roles are combined as noted.

- **Owner / approver:** Robin (maintainer) — holds all approval authority.
- **Controller / operator:** Robin — drives sessions and agents.
- **Implementation:** AI agents under Robin's direction.
- **Review & verification:** Robin — reviews each change and records evidence before merging.

Approval authority is never delegated to an agent. Because review and implementation are combined here, Robin reads each agent change critically as a separate step rather than merging on sight.

## Approval gates

1. **Preparation / preflight** — reading, drafting, and isolated local edits proceed under standing authorization. No shared or external effect.
2. **Implementation** — merging to `main` requires Robin's explicit approval on the pull request after review.
3. **Destructive / external** — force-push, history rewrite, publishing a release to the package registry, or deleting branches require an explicit, per-action decision by Robin at the time of the action.
4. **Live / runtime execution** — Pebble is a local CLI; this project does **not** operate at the live/runtime layer. Agents never run against production or external systems.

## Working discipline

- Branch per change off `main`, named `feat/...`, `fix/...`, or `docs/...`.
- One intent per branch and per PR.
- `main` contains only reviewed, verified work.

## Definition of done

A change is done when:

- [ ] Behavioral changes have a passing `pytest` test or a recorded command and its output.
- [ ] CI (GitHub Actions) is green on the change.
- [ ] Results are reported faithfully, including any failures or skipped steps.

## Companions

- Agent contract: see `AGENTS.md`.
- PR checklist: see `.github/PULL_REQUEST_TEMPLATE.md`.
