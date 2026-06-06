# Audit Whether a Project Conforms

Assess an existing adoption against Lithos and against how the project actually works. The checklist mechanics are the [`audit-local-ai-flow`](../../audit-local-ai-flow/SKILL.md) skill; this reference frames what a project-level audit must conclude.

## Check the claim against the standard

Walk the [`audit-local-ai-flow`](../../audit-local-ai-flow/SKILL.md) checklist: roles, the four [approval gates](../../../docs/approval-semantics.md) and their layering, the environment and credential-scope boundary, working discipline, verification, and the [autonomous PR policy](../../../docs/autonomous-pr-policy.md). Confirm the depth claimed matches the surface present — a lighter governed workflow and a full governed project carry different obligations ([`docs/conformance-and-fixtures.md`](../../../docs/conformance-and-fixtures.md)) — and remember there is **no minimal profile** to fall back on.

## Check truth, not just presence

- The **adoption manifest** must be schema-valid and pass the same invariants the [conformance checker](../../../scripts/verify_conformance_fixtures.py) enforces. Named [conformance fixtures](../../../fixtures/conformance/) pin invalid shapes that must be rejected — self-approval, self-merge, and live/runtime without controls — while other autonomous-PR-policy invariants the schema and checker enforce have no separate named fixture, including that **ownerless auto-merge** is rejected.
- The [static safety scan](../../../docs/static-safety-scan.md) must actually run locally and in CI; treat it as safety evidence, **not behavior proof**.
- Behavior-bearing claims must be backed by a [scenario regression](../../../docs/scenario-regression-governance.md) fixture; a claim with no fixture is an assertion, not proven behavior.

## Report drift

A document that no longer matches practice is worse than none, because it misleads. Compare recent merged work to what the file requires: do merged pull requests show agent self-approval, self-merge, or ownerless auto-merge in practice? Do releases carry owner approval and a provenance record? Flag every gap with a pointer to the standard and a prioritized, tightening-only remediation. Propose; let the owner approve. See [conformance truthfulness](conformance-truthfulness.md).
