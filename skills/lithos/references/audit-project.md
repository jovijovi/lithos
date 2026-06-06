# Audit Whether a Project Conforms

Assess an existing adoption against Lithos and against how the project actually works. The output is a findings report; you do not silently rewrite the project's documents.

## Walk the conformance checklist

Record each item present / partial / missing with a pointer to the relevant Lithos doc:

1. **Roles** — every role in [`docs/roles.md`](../../../docs/roles.md) has an owner, combined roles are stated, and approval authority is not held by an agent.
2. **Approval gates** — all four gates in [`docs/approval-semantics.md`](../../../docs/approval-semantics.md) are operationalized, their layering is intact (no gate implies a higher one), and the live/runtime stance is explicit.
3. **Environment and sandbox boundary** — filesystem roots, network egress/ingress, the **credential scope** bound to least privilege, external/destructive side effects, and escalation/abort conditions are stated ([`docs/environment-and-sandbox-policy.md`](../../../docs/environment-and-sandbox-policy.md)); git worktree isolation and an OS/process sandbox are not conflated.
4. **Discipline** — branch naming, worktree isolation, and the integration branch's allowed contents are defined ([`docs/core-concepts.md`](../../../docs/core-concepts.md)).
5. **Verification and static safety scan** — "done" requires reproducible evidence, not agreement, and a [static safety scan](../../../docs/static-safety-scan.md) gate rejects secret-shaped tokens, private machine-local paths, and unfinished-work placeholders locally and in CI; confirm it is treated as safety evidence, **not behavior proof**.
6. **Autonomous PR policy** — the file lets an agent open/update/close its own pull request as preparation but forbids **self-approval**, **self-merge**, and **ownerless auto-merge**, routing merging, branch deletion, releasing, and external communication to higher-gate owner approval ([`docs/autonomous-pr-policy.md`](../../../docs/autonomous-pr-policy.md)).
7. **Conformance claim and depth** — the depth claimed matches the surface present; a lighter governed workflow and a full governed project carry different obligations, and there is **no minimal profile** to fall back on ([`docs/conformance-and-fixtures.md`](../../../docs/conformance-and-fixtures.md)).
8. **Knowledge spine and discoverability** — for full governed projects the knowledge spine exists or is explicitly out of scope ([`docs/knowledge-governance.md`](../../../docs/knowledge-governance.md)), and the local workflow file is a single source of truth referenced from `README`/`AGENTS.md`.

## Check truth, not just presence

- The **adoption manifest** must be schema-valid and pass the same invariants the [conformance checker](../../../scripts/verify_conformance_fixtures.py) enforces. Named [conformance fixtures](../../../fixtures/conformance/) pin invalid shapes that must be rejected — self-approval, self-merge, and live/runtime without controls — while other autonomous-PR-policy invariants the schema and checker enforce have no separate named fixture, including that **ownerless auto-merge** is rejected.
- The [static safety scan](../../../docs/static-safety-scan.md) must actually run locally and in CI; treat it as safety evidence, **not behavior proof**.
- Behavior-bearing claims must be backed by a [scenario regression](../../../docs/scenario-regression-governance.md) fixture; a claim with no fixture is an assertion, not proven behavior. Released artifacts must carry owner approval and a provenance record ([release and supply-chain](../../../docs/release-and-supply-chain-governance.md)).

## Report drift

A document that no longer matches practice is worse than none, because it misleads. Compare recent merged work to what the file requires: do merged pull requests show agent self-approval, self-merge, or ownerless auto-merge in practice? Does the static safety scan really run, or is it only described? Do releases carry owner approval and a provenance record? Flag every gap with a pointer to the standard and a prioritized, tightening-only remediation. Propose; let the owner approve. See [conformance truthfulness](conformance-truthfulness.md).
