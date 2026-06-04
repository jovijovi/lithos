# AGENTS.md — Contributing to Lithos

This file governs how AI agents (and the humans operating them) contribute to the **Lithos** repository itself. It is also a worked example of the kind of contract Lithos asks adopting projects to write. Lithos is a standard, so changes here are edits to a published document — treat them with corresponding care.

## What this repository is

Lithos publishes the *AI-Collaborative Software Development Standards*: normative documents, templates, skills, and examples. There is no application runtime to build or deploy. Contributions are almost always documentation, templates, skills, examples, or the verification script.

## Authority and approval

- A human owner approves what gets merged. Agents propose; they do not self-merge.
- Approval is scoped. Sanctioning a change to one document does not sanction unrelated edits.
- Distinguish the approval gates defined in [`docs/approval-semantics.md`](docs/approval-semantics.md). In this repository the relevant ones are *preparation* (drafting, local edits) and *implementation* (a reviewed change destined for `main`). There is no live/runtime execution surface here.
- Never perform destructive or external side-effecting actions (force-push, history rewrite, publishing a release, deleting branches you did not create) without explicit, contemporaneous owner approval.

## Working discipline

- Do work on a feature branch or a dedicated worktree, never directly on `main`. See [`docs/core-concepts.md`](docs/core-concepts.md).
- Keep changes scoped to one coherent intent per branch and per pull request.
- Match the surrounding voice: concise, precise, standards-body. Do not embellish.
- Localized READMEs must stay **semantically aligned** with `README.md`. If you change the English landing page, update the translations to match meaning — do not let them drift.
- Do not edit the binary assets in `assets/`.
- Keep all content tool- and vendor-neutral. Refer to roles and capabilities generically; do not name specific products, private profiles, or internal systems.

## Verification before completion

A change is not "done" because it reads well. Before requesting review:

1. Run `python scripts/verify_docs.py` and confirm it passes.
2. Confirm every new internal link resolves.
3. Confirm no forbidden placeholder tokens or private paths were introduced (the script checks this; do not rely on it alone).

State the evidence — the command you ran and its result — when you hand work back. See [`docs/verification-standards.md`](docs/verification-standards.md).

## Pull requests

Use [`templates/pr-checklist.md`](templates/pr-checklist.md). A PR should explain *what changed and why*, list the verification performed, and call out any documents (including translations) that must change together.

## Governance

Substantive changes to the normative documents follow [`docs/versioning-and-governance.md`](docs/versioning-and-governance.md). When in doubt about whether a change is normative, assume it is and flag it for the owner.
