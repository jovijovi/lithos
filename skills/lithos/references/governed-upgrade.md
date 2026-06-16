# Fill In a Concise Adoption

As a project grows — formal review, multiple agents, staged phases, runtime boundaries, or compliance needs — fill the concise anchors of Lithos's one full-lifecycle governance model in with full detail. Lithos has no tiers, so this is not moving between governance modes; it is elaborating the same model, distinct from moving to a newer Lithos version ([version upgrade](version-upgrade.md)).

## Tighten only

The rule that governs the whole change: you add and tighten; you **never loosen** a Lithos requirement. There is no smaller tier to drop toward — a concise adoption and a fully elaborated one differ in how much content the anchors carry, not in whether roles, gates, isolation, and evidence hold. Start from the project's current file and [`templates/governed-ai-flow.md`](../../../templates/governed-ai-flow.md), and — for the full authority chain — [`docs/governed-project-structure.md`](../../../docs/governed-project-structure.md) plus [`templates/governed-project/`](../../../templates/governed-project/). Run [audit a project](audit-project.md) first to find the gaps, preserve any rules already stricter than the template, and resolve every bracketed decision as you go.

## What the upgrade adds

- **Independent roles** — reviewer and verifier separated from the implementation role; approval authority human-only, and role combinations governance disallows removed ([`docs/roles.md`](../../../docs/roles.md)).
- **Recorded approvals** — per-action owner approval for the destructive/external gate, recorded (who, what scope, when) not merely signaled ([`docs/approval-semantics.md`](../../../docs/approval-semantics.md)).
- **A first-class environment and sandbox policy** — filesystem roots, network egress/ingress, the **credential scope** bound to least privilege, the external/destructive side-effect inventory, and escalation/abort conditions, promoted to a change-controlled document ([`docs/environment-and-sandbox-policy.md`](../../../docs/environment-and-sandbox-policy.md)).
- **Stronger verification** — reproducible evidence (tests/CI) for behavioral changes with failures and skips reported faithfully, plus the static safety scan gate treated as safety evidence, **not behavior proof** ([`docs/verification-standards.md`](../../../docs/verification-standards.md), [`docs/static-safety-scan.md`](../../../docs/static-safety-scan.md)).
- **A machine-readable conformance claim** — an adoption manifest that matches its [schema](../../../schemas/lithos-adoption-manifest.schema.json) and exercises the conformance fixtures, including the invalid cases ([`docs/conformance-and-fixtures.md`](../../../docs/conformance-and-fixtures.md)). The manifest is a record, **not authorization**.
- **The document authority chain** — `GOAL.md` → PRD → design → roadmap/status → plans → code, kept separate from task plans ([`docs/governed-project-structure.md`](../../../docs/governed-project-structure.md)).
- **Lean status records** — roadmap, current-status, and dev-log entries record phase authority, current decisions, open tails, user-visible truth, and safety boundaries; they do not replace behavior/safety evidence or repeat bookkeeping already proven by git history, CI, PR metadata, generated indexes, or drift reports ([`docs/verification-standards.md`](../../../docs/verification-standards.md)).
- **The knowledge spine** — `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, a generated `docs/INDEX.md`, and a drift report ([`docs/knowledge-governance.md`](../../../docs/knowledge-governance.md)).
- **Scenario regression** for behavior-bearing surfaces, and **release and supply-chain** governance — no agent self-release, a provenance record, pinned dependencies, owner-approved publishing — for published artifacts ([scenario regression](../../../docs/scenario-regression-governance.md), [release and supply-chain](../../../docs/release-and-supply-chain-governance.md)).
- **Change control and localization** — normative changes to the local workflow file are reviewed and translations/companion docs change together ([`docs/versioning-and-governance.md`](../../../docs/versioning-and-governance.md)); if localized README files exist, keep them aligned when visible claims change.

## Done when

The manifest claims Lithos's single `full-lifecycle-governance` model and stays schema-valid, the knowledge spine is fully elaborated, the full source-of-truth chain is in place, and [audit a project](audit-project.md) reports no open gaps. Tightening governance grants no new execution authority; see [agent role boundaries](agent-role-boundaries.md).
