---
title: "Scenario regression governance"
status: active
created_at: 2026-06-05
---
# Scenario regression governance

> Pin behavior-bearing claims to named, committed scenario fixtures so a regression is caught mechanically, not by a downstream consumer.

This document defines how this project governs scenario fixtures. If the project bears behavior — it claims an input yields an outcome, or ships examples meant to work — those claims are pinned to fixtures and run as a regression suite with the other gates in [`docs/AI_FLOW.md`](../AI_FLOW.md). A project with no behavioral surface records that here and keeps this gate dormant.

## What a scenario fixture is

A committed, self-describing record of one expected behavior:

- a **name** identifying the scenario and the claim it backs;
- an **input** — the conditions, arguments, or state it exercises;
- an **expected outcome** — the result this project asserts for that input;
- enough context for an independent party to reproduce the check.

Fixtures are plain, parseable text and carry no secrets; sensitive inputs are redacted with `[REDACTED]` placeholders. A fixture is evidence: its value is that anyone can re-run it and see the same result.

## Claim-to-fixture rule

- A documented input-to-outcome claim should be pinned by a fixture so documentation cannot silently drift from behavior.
- An example meant to work should be exercised as a fixture, so a broken example fails a check instead of a user.
- A new behavioral capability must add fixtures for its accepted cases and its important edge and failure cases, not only the happy path.

A claim with no fixture behind it is an assertion, not verified behavior, and is reported as such rather than presented as proven.

## Preventing regressions

- A change that alters a fixture's expected outcome is a behavior change: it is called out, justified, and approved — never folded silently into an unrelated change by editing the expected value to match new output.
- Removing or weakening a fixture removes a guardrail; it is reviewed as a guardrail removal, never a quiet way to make a failing suite pass.
- When a regression is found, the fixture that caught it stays; the fix restores the expected outcome.
- If the suite is sampled or time-boxed, state what was not run so a partial pass is never rounded up to full coverage.

## This project's scenario suite

```text
behavioral surface: [yes / no — what kind of behavior this project bears]
fixtures:           [path to committed scenario fixtures, or "none yet"]
command:            [project scenario-regression command, run with the other verification gates]
```

## Authority boundary

Fixtures record and verify behavior; they do not govern it. Where a fixture and the product requirements disagree, the requirements in `docs/product/prd.md` govern and the fixture is corrected through the normal change process. Passing the suite is a precondition for implementation approval, not a substitute for it.

## Release gate

A scenario regression is a release gate. A release that would change advertised behavior, or that cannot show its scenario suite passing on the exact revision being released, does not proceed without explicit owner approval. See [`docs/release/release-governance.md`](../release/release-governance.md).
