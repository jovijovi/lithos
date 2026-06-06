# Scenario Regression Governance

Some projects bear **behavior**: they make claims about what an input produces, ship examples that are supposed to work, and promise that a release does not quietly change those outcomes. For such projects, prose and tests are not enough on their own — the behavior a project advertises must be pinned to **named, committed scenario fixtures** so a regression is caught mechanically rather than discovered by a downstream consumer.

This document defines how a behavior-bearing project governs scenario fixtures and prevents regressions in its claims, its examples, and its releases. It is part of Lithos's one [full-lifecycle governance model](governed-project-structure.md) and applies to any project that bears behavior; a project with no behavioral surface does not need it.

## What a scenario fixture is

A **scenario fixture** is a committed, self-describing record of one expected behavior:

- a **name** that identifies the scenario and the claim it backs;
- an **input** — the conditions, arguments, or state the scenario exercises;
- an **expected outcome** — the result the project asserts for that input;
- enough context for an independent party to **reproduce** the check.

Fixtures are plain, parseable text (see [tooling interoperability](tooling-interoperability.md)) and carry **no secrets or private values**; sensitive inputs are redacted with placeholders. A fixture is [evidence](verification-standards.md): its value is that anyone can re-run it and see the same result.

The [conformance fixtures](conformance-and-fixtures.md) that prove a project's adoption manifest are themselves a worked instance of this pattern — named inputs with expected pass/reject outcomes, checked by a reproducible script.

## The claim-to-fixture rule

The governing rule is simple: **a behavior-bearing claim must be backed by a scenario fixture.**

- When a project documents that an input yields an outcome, that outcome **should** be pinned by a fixture, so the documentation cannot silently drift from the behavior.
- When a project ships an example that is meant to work, the example **should** be exercised as a fixture, so a broken example fails a check instead of a user.
- A new behavioral capability **must** add the fixtures that cover its accepted cases and its important edge and failure cases, not only its happy path.

A claim with no fixture behind it is an assertion, not verified behavior, and **must** be reported as such rather than presented as proven.

## Preventing regressions

Scenario fixtures form a **regression suite** that runs with the project's other [verification](verification-standards.md) gates, locally and in continuous integration. From this follow the regression rules:

- A change that alters a fixture's expected outcome is a **behavior change**. It **must** be called out as such, justified, and approved — not folded silently into an unrelated change by editing the expected value to match new output.
- Removing or weakening a fixture removes a guardrail. It is reviewed as a guardrail removal: a deletion or relaxation **must** be deliberate and justified, never a quiet way to make a failing suite pass. Silently dropping coverage and reporting green is the failure this gate exists to prevent.
- When a regression is found, the fixture that caught it **stays**; the fix restores the expected outcome rather than discarding the fixture.

If the suite is sampled, time-boxed, or otherwise bounded, the project **must** state what was not run, so a partial pass is never rounded up to full coverage.

## Relationship to releases

Scenario regressions are a **release gate**. A release that would change advertised behavior, or that cannot show its scenario suite passing on the exact revision being released, **must not** proceed without explicit owner approval of that behavior change. The passing scenario suite is part of the release's provenance evidence; see [release and supply-chain governance](release-and-supply-chain-governance.md).

## Authority boundary

Scenario fixtures **record and verify behavior; they do not govern it.** A fixture cannot redefine product scope, override the [authority chain](governed-project-structure.md), or grant approval. Where a fixture and the product requirements disagree, the requirements govern and the fixture is corrected through the normal change process. Passing the regression suite is a precondition for [implementation approval](approval-semantics.md), not a substitute for it.

## Relationship to the rest of Lithos

- Fixtures are [verification evidence](verification-standards.md): reproducible, inspectable, and reported faithfully.
- They are vendor-neutral, secret-free portable artifacts under [tooling interoperability](tooling-interoperability.md).
- The [adoption manifest](conformance-and-fixtures.md) and its fixtures are the canonical worked example of scenario-style governance.
- Scenario regressions gate releases under [release and supply-chain governance](release-and-supply-chain-governance.md).
