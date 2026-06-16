<!--
Lithos PR checklist template.
Copy into .github/PULL_REQUEST_TEMPLATE.md or your contributing docs.
Lithos: https://github.com/jovijovi/lithos
-->

# Pull Request Checklist

## Summary

- **What changed:** [one or two sentences]
- **Why:** [the intent this serves]
- **Scope:** [what this PR deliberately does NOT do]

## Collaboration (Lithos)

- [ ] One coherent intent; scope did not widen without owner approval.
- [ ] Worked on a feature branch / isolated worktree, not directly on the integration branch.
- [ ] The applicable approval gate is satisfied (implementation; and per-action approval for any destructive/external effect).
- [ ] No agent self-approval, self-merge, ownerless auto-merge, branch deletion, or publishing occurred without explicit owner approval.
- [ ] No live/runtime execution was performed unless separately authorized.
- [ ] Stayed within the declared environment/sandbox boundaries — filesystem roots, network egress, and credential scope; no out-of-scope reads, network access, or secret use.

## Verification (evidence, not agreement)

- [ ] Tests added/updated and passing for behavioral changes.
- [ ] Static safety scan passed; no secret-shaped values, private machine-local paths, or unfinished-work placeholders were introduced.
- [ ] Scenario regression fixtures were added/updated and run for behavior-bearing claims or examples.
- [ ] Release-facing changes cite the exact revision, provenance evidence, and explicit owner approval before any publish action.
- [ ] CI run linked and green (where applicable).
- [ ] Reproduction steps or recorded command + output included for any behavior change.
- [ ] Results reported faithfully — failures, skips, and unverified areas are called out.
- [ ] An agent run manifest / audit entry is recorded when the run needs auditability — what was authorized, what ran (local/offline vs external/live), and the boundary that held.

## Documents that change together

- [ ] Local workflow file updated if collaboration rules changed.
- [ ] `AGENTS.md` updated if the agent contract changed.
- [ ] Localized docs/READMEs updated to stay semantically aligned (if applicable).
- [ ] `docs/INDEX.md` and `docs/lessons/_drift_report.md` regenerated or checked when docs/knowledge files changed.
- [ ] Scenario-regression and release-governance docs updated when behavior or publishing claims changed.
- [ ] Dev log / lessons / practices updated when the change produced reusable knowledge or phase evidence.
- [ ] No duplicate status churn: roadmap, current-status, and dev-log edits are included only when they change authority, a safety boundary, or current user-visible truth — not routine bookkeeping that git history or generated artifacts already record.

## Notes for the reviewer

[Anything the reviewer should focus on, risks, or open questions.]
