# Review a Pull Request Against Lithos

Review a proposed change for whether it keeps the project conformant and whether the agent that produced it stayed inside its authority. This complements ordinary code review; it does not replace it.

## What to check

- **Role and gate drift** — does the change quietly combine roles, collapse the layering of the four [approval gates](../../../docs/approval-semantics.md), or treat a lower gate as clearing a higher one?
- **Manifest truthfulness** — if the change touches conformance, does the **adoption manifest** still match reality and stay schema-valid against the [conformance fixtures](../../../fixtures/conformance/) invariants? See [conformance truthfulness](conformance-truthfulness.md).
- **Artifacts move together** — when a normative claim changes, do the skills, templates, docs, localized READMEs, and verifiers change with it, or has one drifted behind?
- **Static safety** — does the [static safety scan](../../../docs/static-safety-scan.md) pass on the change, with no secret-shaped value, private machine-local path, or unfinished-work placeholder?
- **Scenario and release implications** — does the change alter an advertised behavior without a justified [scenario regression](../../../docs/scenario-regression-governance.md) update, or move a project toward publishing without [release and supply-chain](../../../docs/release-and-supply-chain-governance.md) governance?
- **Safety blockers vs. status churn** — separate a real safety finding (a crossed authority or approval gate, a sandbox or credential-scope escape, a secret or static-safety regression, or missing behavior/safety evidence for risky or runtime work) from status or prose churn (duplicated roadmap/status restatement, routine post-merge bookkeeping, repeated non-approval paragraphs, or stale-text hunts that git history, CI, pull-request metadata, or generated artifacts already settle). Block on the former; for the latter, prefer deriving the truth from metadata or generated artifacts over requesting more status prose. Distinguishing the two does not lower the bar on any safety boundary — see [verification standards](../../../docs/verification-standards.md).

## The line an agent may not cross

A pull request is a proposal. Per the [autonomous PR policy](../../../docs/autonomous-pr-policy.md), confirm the change shows **no self-approval, no self-merge, and no ownerless auto-merge**, and that merging, branch deletion, releasing, and external communication are routed to explicit owner approval. A green check is evidence, not authorization to merge. Report findings; the owner decides. See [agent role boundaries](agent-role-boundaries.md).
