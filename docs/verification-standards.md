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
5. **Independent review** — a reviewer, separate from the implementer where practical, who has examined the change against its acceptance criteria.

## What each unit must carry

To be accepted, a collaboration unit **must**:

- State what was claimed and which evidence supports each claim.
- Include at least one form of **reproducible** evidence (test, CI, or recorded steps) for any behavioral change.
- Report results **faithfully**: if tests fail, say so with the output; if a step was skipped, say it was skipped; do not round a partial pass up to "passing."
- Distinguish what was verified from what was merely asserted or assumed.

## Reproducibility

Evidence that cannot be reproduced is testimony, not proof. Prefer evidence that another person can regenerate from the repository: committed tests, pinned commands, CI configuration in version control. Where reproduction needs setup, document the setup as part of the evidence.

## Honesty obligations

- Never claim work is complete, fixed, or passing without having observed the verifying output.
- Surface failures and uncertainty rather than smoothing them over; a precise "this part is unverified" is more valuable than a vague "done."
- If verification was not performed, say that plainly instead of implying it was.

## The verifier role

The [verifier](roles.md) owns the production and reporting of this evidence. The verifier **should** be independent of the implementer where project size allows, and **must** report outcomes without optimistic rounding.

## Relationship to approval

Verification evidence is a precondition for [implementation approval](approval-semantics.md), not a substitute for it. Evidence shows the work is sound; the owner's approval decides that it ships. Neither replaces the other.
