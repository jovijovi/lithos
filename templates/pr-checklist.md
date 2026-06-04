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
- [ ] No live/runtime execution was performed unless separately authorized.

## Verification (evidence, not agreement)

- [ ] Tests added/updated and passing for behavioral changes.
- [ ] CI run linked and green (where applicable).
- [ ] Reproduction steps or recorded command + output included for any behavior change.
- [ ] Results reported faithfully — failures, skips, and unverified areas are called out.

## Documents that change together

- [ ] Local workflow file updated if collaboration rules changed.
- [ ] `AGENTS.md` updated if the agent contract changed.
- [ ] Localized docs/READMEs updated to stay semantically aligned (if applicable).

## Notes for the reviewer

[Anything the reviewer should focus on, risks, or open questions.]
