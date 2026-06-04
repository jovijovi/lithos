<!--
Lithos local workflow file — MINIMAL template.
Copy this into your repository under a filename you choose (e.g. AI_FLOW.md),
then replace every [bracketed] decision. Delete this comment when done.
Lithos: https://github.com/jovijovi/lithos
-->

# AI Collaboration Workflow — [Project Name]

This project follows [Lithos](https://github.com/jovijovi/lithos). This file is our single source of truth for how humans and AI collaborate here.

> Adopting this workflow does not authorize live or autonomous AI execution. Approvals here are organizational, not a grant of machine permission.

## Roles

Small project — roles are combined as noted.

- **Owner / approver:** [name] — holds all approval authority.
- **Controller / operator:** [name or "owner"] — drives sessions and agents.
- **Implementation:** AI agents under the operator, plus [names].
- **Review & verification:** [name] — may be the owner; states findings with evidence.

Approval authority is never delegated to an agent.

## Approval gates

1. **Preparation / preflight** — reading, drafting, and isolated local changes proceed under standing authorization. No shared or external effect.
2. **Implementation** — merging to `[main]` requires [the owner's explicit OK on the PR].
3. **Destructive / external** — actions like [force-push, history rewrite, publishing, deleting data] require explicit per-action owner approval.
4. **Live / runtime execution** — [this project does NOT operate at this layer]. / [If it does, describe the separate controls here.]

## Working discipline

- Branch per change off `[main]`, named `[type/short-description]`.
- Keep one intent per branch and PR.
- `[main]` contains only reviewed, verified work.

## Definition of done

A change is done when:

- [ ] Behavioral changes have a passing, re-runnable test or recorded command + output.
- [ ] [CI] is green on the change (where applicable).
- [ ] Results are reported faithfully, including any failures or skipped steps.

## Companions

- Agent contract: see `AGENTS.md`.
- PR checklist: see `[path/to/pr-checklist.md]`.
