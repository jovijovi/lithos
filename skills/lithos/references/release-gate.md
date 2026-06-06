# Run a Release or Acceptance Gate

Decide whether a prepared change may be accepted, and whether a published artifact may ship. Run this as a gate that returns a clear verdict, not an impression. The normative rules are [release and supply-chain governance](../../../docs/release-and-supply-chain-governance.md).

## Separate blockers from notes

Return two distinct lists, and never round one up to the other:

- **Blockers** stop the gate. A failing test or [static safety scan](../../../docs/static-safety-scan.md), a [scenario regression](../../../docs/scenario-regression-governance.md) on an advertised behavior, an incomplete provenance record, an unpinned dependency, or any forbidden ownerless action is a blocker.
- **Notes** are advisory: improvements, follow-ups, and risks that do not by themselves fail the gate.

State explicitly anything that was sampled, time-boxed, or not run, so a partial pass is never reported as full coverage.

## Owner-approved publishing; no agent self-release

The load-bearing boundary: **there is no agent self-release.** An agent may *prepare* a release — compute the version, stage outputs, draft the **provenance record** — and must then **stop and request explicit, per-action owner approval** before anything leaves the repository. Clearing the implementation gate does not clear the release gate. A green build is evidence the artifact is sound; it is not authorization to ship it. Acting against live or production systems is a separate gate Lithos does not grant ([approval semantics](../../../docs/approval-semantics.md), [agent role boundaries](agent-role-boundaries.md)).
