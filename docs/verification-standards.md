# Verification Standards

The central rule: **evidence outranks agreement.** A collaboration unit is verified when an independent party can inspect or reproduce proof that it does what it claims — not when a participant, human or AI, asserts that it does.

## Why agreement is not enough

Agents are fluent and confident; humans are agreeable under time pressure. Consensus is cheap and frequently wrong. "It works on my run," "the agent confirmed it," and "looks good to me" are assertions, not verification. Lithos requires that claims be backed by artifacts a third party can re-examine.

## Forms of acceptable evidence

In rough order of strength:

1. **Automated tests** — new or existing tests that exercise the change and pass, runnable by anyone.
2. **Continuous integration** — a CI run on the proposed change, linked and inspectable, not just a green badge from an unrelated run.
3. **Reproducible steps** — a recorded command (or sequence) and its actual output, such that a reviewer can re-run it and see the same result.
4. **Artifacts** — logs, diffs, screenshots, generated files, or reports attached to the unit.
5. **Generated governance checks** — for governed documentation changes, generated docs indexes and drift reports that can be regenerated from the repository. Where a project declares conformance, the [conformance fixtures](conformance-and-fixtures.md) and their pure-stdlib checker are reproducible evidence in the same sense: anyone can re-run the checker to confirm the declared claim still holds and that the fixtures pass or reject for the documented reasons.
6. **Static safety scans** — machine-runnable checks that reject secret-shaped values, private machine-local paths, and unfinished-work placeholders before review, merge, or release. See [static safety scan](static-safety-scan.md).
7. **Scenario regression suites** — named fixtures for behavior-bearing claims and examples, run as reproducible checks so output changes are visible and reviewed. See [scenario regression governance](scenario-regression-governance.md).
8. **Release provenance records** — evidence that a release was built from a specific revision, passed its gates, and was explicitly approved for publication. See [release and supply-chain governance](release-and-supply-chain-governance.md).
9. **Independent review** — a reviewer, separate from the implementer where practical, who has examined the change against its acceptance criteria.

## What each unit must carry

To be accepted, a collaboration unit **must**:

- State what was claimed and which evidence supports each claim.
- Include at least one form of **reproducible behavior evidence** (test, CI, scenario regression suite, or recorded steps) for any behavioral change; static safety scans are required safety evidence, but never substitute for behavior proof.
- Report results **faithfully**: if tests fail, say so with the output; if a step was skipped, say it was skipped; do not round a partial pass up to "passing."
- Distinguish what was verified from what was merely asserted or assumed.
- For release candidates, cite the exact revision, static safety scan, scenario regression outcome where relevant, generated drift evidence, and owner approval reference separately.

## Reproducibility

Evidence that cannot be reproduced is testimony, not proof. Prefer evidence that another person can regenerate from the repository: committed tests, pinned commands, CI configuration in version control. Where reproduction needs setup, document the setup as part of the evidence.

## Honesty obligations

- Never claim work is complete, fixed, or passing without having observed the verifying output.
- Surface failures and uncertainty rather than smoothing them over; a precise "this part is unverified" is more valuable than a vague "done."
- If verification was not performed, say that plainly instead of implying it was.

## The verifier role

The [verifier](roles.md) owns the production and reporting of this evidence. The verifier **should** be independent of the implementer where project size allows, and **must** report outcomes without optimistic rounding.

## Recording evidence in a run manifest

Where a project keeps per-run records, the [agent run manifest](agent-run-manifest.md) is where this evidence is gathered for a single run, alongside the boundary that held and the approval that was referenced. The manifest keeps **verification evidence** — proof the work is sound — distinct from the **approval reference** — the record that the work was allowed; neither substitutes for the other. The same honesty obligations apply: an explicit "unverified" entry in the manifest is worth more than an implied pass.

## Relationship to approval

Verification evidence is a precondition for [implementation approval](approval-semantics.md), not a substitute for it. Evidence shows the work is sound; the owner's approval decides that it ships. Neither replaces the other.
