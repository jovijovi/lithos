# Upgrade to a Full Governed Project

Strengthen a project that outgrew a lighter governed workflow into a full governed project — for formal review, multiple agents, staged phases, runtime boundaries, or compliance needs. The mechanics are the [`adapt-ai-flow-for-governed-project`](../../adapt-ai-flow-for-governed-project/SKILL.md) skill. This is a governance-depth upgrade, distinct from moving to a newer Lithos version ([version upgrade](version-upgrade.md)).

## Tighten only

The rule that governs the whole upgrade: you add and tighten; you **never loosen** a Lithos requirement. There is no minimal profile to drop toward — a lighter governed workflow and a full governed project differ in surface, not in whether roles, gates, isolation, and evidence hold.

## What the upgrade adds

Run [`adapt-ai-flow-for-governed-project`](../../adapt-ai-flow-for-governed-project/SKILL.md) and layer in:

- **Independent roles** — reviewer and verifier separated from implementation; approval authority human-only ([`docs/roles.md`](../../../docs/roles.md)).
- **Recorded approvals** — per-action owner approval for the destructive/external gate, recorded not merely signaled ([`docs/approval-semantics.md`](../../../docs/approval-semantics.md)).
- **The document authority chain** — `GOAL.md` → PRD → design → roadmap/status → plans → code ([`docs/governed-project-structure.md`](../../../docs/governed-project-structure.md)).
- **The knowledge spine** — `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, a generated index, and a drift report ([`docs/knowledge-governance.md`](../../../docs/knowledge-governance.md)).
- **Scenario regression** for behavior-bearing surfaces and **release and supply-chain** governance for published artifacts ([scenario regression](../../../docs/scenario-regression-governance.md), [release and supply-chain](../../../docs/release-and-supply-chain-governance.md)).

## Done when

The manifest now claims `full-governed-project` and stays schema-valid, the knowledge spine exists, and [audit a project](audit-project.md) reports no open gaps. Tightening governance grants no new execution authority; see [agent role boundaries](agent-role-boundaries.md).
