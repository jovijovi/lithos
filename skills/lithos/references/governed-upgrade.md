# Upgrade to a Full Governed Project

Strengthen a project that outgrew a **lighter governed workflow** into a **full governed project** — for formal review, multiple agents, staged phases, runtime boundaries, or compliance needs. This is a governance-depth upgrade, distinct from moving to a newer Lithos version ([version upgrade](version-upgrade.md)).

## Tighten only

The rule that governs the whole upgrade: you add and tighten; you **never loosen** a Lithos requirement. There is no minimal profile to drop toward — a lighter governed workflow and a full governed project differ in surface, not in whether roles, gates, isolation, and evidence hold. Start from the project's current file and [`templates/governed-ai-flow.md`](../../../templates/governed-ai-flow.md), and — for a full authority chain — [`docs/governed-project-structure.md`](../../../docs/governed-project-structure.md) plus [`templates/governed-project/`](../../../templates/governed-project/). Run [audit a project](audit-project.md) first to find the gaps, preserve any rules already stricter than the template, and resolve every bracketed decision as you go.

## What the upgrade adds

- **Independent roles** — reviewer and verifier separated from the implementation role; approval authority human-only, and role combinations governance disallows removed ([`docs/roles.md`](../../../docs/roles.md)).
- **Recorded approvals** — per-action owner approval for the destructive/external gate, recorded (who, what scope, when) not merely signaled ([`docs/approval-semantics.md`](../../../docs/approval-semantics.md)).
- **A first-class environment and sandbox policy** — filesystem roots, network egress/ingress, the **credential scope** bound to least privilege, the external/destructive side-effect inventory, and escalation/abort conditions, promoted to a change-controlled document ([`docs/environment-and-sandbox-policy.md`](../../../docs/environment-and-sandbox-policy.md)).
- **Stronger verification** — reproducible evidence (tests/CI) for behavioral changes with failures and skips reported faithfully, plus the static safety scan gate treated as safety evidence, **not behavior proof** ([`docs/verification-standards.md`](../../../docs/verification-standards.md), [`docs/static-safety-scan.md`](../../../docs/static-safety-scan.md)).
- **A machine-readable conformance claim** — an adoption manifest that matches its [schema](../../../schemas/lithos-adoption-manifest.schema.json) and exercises the conformance fixtures, including the invalid cases ([`docs/conformance-and-fixtures.md`](../../../docs/conformance-and-fixtures.md)). The manifest is a record, **not authorization**.
- **The document authority chain** — `GOAL.md` → PRD → design → roadmap/status → plans → code, kept separate from task plans ([`docs/governed-project-structure.md`](../../../docs/governed-project-structure.md)).
- **The knowledge spine** — `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, a generated `docs/INDEX.md`, and a drift report ([`docs/knowledge-governance.md`](../../../docs/knowledge-governance.md)).
- **Scenario regression** for behavior-bearing surfaces, and **release and supply-chain** governance — no agent self-release, a provenance record, pinned dependencies, owner-approved publishing — for published artifacts ([scenario regression](../../../docs/scenario-regression-governance.md), [release and supply-chain](../../../docs/release-and-supply-chain-governance.md)).
- **Change control and localization** — normative changes to the local workflow file are reviewed and translations/companion docs change together ([`docs/versioning-and-governance.md`](../../../docs/versioning-and-governance.md)); if localized README files exist, keep them aligned when visible claims change.

## Done when

The manifest now claims `full-governed-project` and stays schema-valid, the knowledge spine exists, the full source-of-truth chain is in place, and [audit a project](audit-project.md) reports no open gaps. Tightening governance grants no new execution authority; see [agent role boundaries](agent-role-boundaries.md).
