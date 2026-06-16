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
- [ ] No duplicate status churn: roadmap/current-status/dev-log edits are included only when they change authority, a safety boundary, current decisions, open tails, or current user-visible truth — not routine bookkeeping that git history, CI, PR metadata, or generated artifacts already record.
- [ ] `docs/INDEX.md`, `docs/lessons/_drift_report.md`, dev log, lessons, and practices are updated or checked when relevant.
- [ ] `README.md` and `README.zh-CN.md` are semantically aligned if user-facing claims changed.
- [ ] No agent self-approval, self-merge, ownerless auto-merge, branch deletion, or publishing occurred without explicit owner approval.
- [ ] No live settlement, payment-network call, release publication, or external delivery occurred without explicit higher-gate approval.
- [ ] Environment, sandbox, and credential scope stayed within the documented policy (no broadened network/filesystem access or secret exposure).
- [ ] An agent run manifest and audit evidence are attached or linked when the change was agent-executed or touched external/runtime boundaries.
- [ ] Conformance claim (adoption manifest) and portable, vendor-neutral artifacts stay accurate; knowledge records inform but do not override the authority chain.
- [ ] Scenario-regression and release-governance docs updated when behavior or publishing claims changed.

## Verification

- [ ] Tests or recorded commands prove behavior.
- [ ] `tools/static_safety_scan.py` passed.
- [ ] Scenario regression fixtures were added/updated and run for behavior-bearing decision claims.
- [ ] Release-facing changes cite exact revision, provenance evidence, and explicit owner approval before any publish action.
- [ ] Documentation verification passed.
- [ ] CI is linked and green where applicable.
- [ ] Failures, skips, and unverified areas are called out honestly.

## Reviewer notes

Focus on product-boundary drift, evidence quality, and whether the source-of-truth chain stayed aligned.
