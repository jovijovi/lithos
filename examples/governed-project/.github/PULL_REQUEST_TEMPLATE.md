# Pull Request Checklist

## Summary

- **What changed:**
- **Why:**
- **Scope deliberately excluded:**

## Lithos governance

- [ ] The change maps to `GOAL.md`, PRD, design, and roadmap/current-status.
- [ ] One coherent intent; scope did not widen without owner approval.
- [ ] Work happened on a branch or isolated worktree, not directly on `main`.
- [ ] Feature tracker and current-status updates are included if completion state changed.
- [ ] `docs/INDEX.md`, `docs/lessons/_drift_report.md`, dev log, lessons, and practices are updated or checked when relevant.
- [ ] `README.md` and `README.zh-CN.md` are semantically aligned if user-facing claims changed.
- [ ] No live settlement, payment-network call, release publication, or external delivery occurred without explicit higher-gate approval.

## Verification

- [ ] Tests or recorded commands prove behavior.
- [ ] Documentation verification passed.
- [ ] CI is linked and green where applicable.
- [ ] Failures, skips, and unverified areas are called out honestly.

## Reviewer notes

Focus on product-boundary drift, evidence quality, and whether the source-of-truth chain stayed aligned.
