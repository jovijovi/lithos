---
title: "Granite Scenario Regression Governance"
status: active
created_at: 2026-06-05
---
# Granite Scenario Regression Governance

> Granite is a behavior-bearing library: every decision rule it ships is pinned to a named scenario fixture so a regression is caught mechanically, not by a downstream consumer.

Granite computes payments-domain decisions and reports deterministic evidence for them. Because consumers depend on those decisions not changing silently, each documented decision is backed by a scenario fixture, and the fixtures run as a regression suite with the other gates in [`docs/AI_FLOW.md`](../AI_FLOW.md).

## What a Granite scenario fixture is

A committed, self-describing record of one expected decision:

- a **name** identifying the scenario and the rule it backs (for example, `fee/round-half-even-minor-units`);
- an **input** — the policy version, amount, currency, and context the rule evaluates;
- an **expected outcome** — the decision and evidence Granite asserts for that input;
- enough context for an independent party to reproduce the check.

Fixtures are plain text, carry no real account or credential values, and redact any sensitive field with `[REDACTED]`.

## Claim-to-fixture rule

- Each rule documented in `docs/product/prd.md` and `docs/design/technical-solution.md` is pinned by at least one fixture.
- Each accepted edge case — minor-unit rounding, unknown policy version, settlement-window boundaries — has its own fixture, not only the happy path.
- A rule with no fixture behind it is an unverified assertion and is reported as such in `docs/roadmap/features.md`.

## Planned scenario coverage

Granite is at R0 (documentation baseline); the rules below are planned and gated by implementation approval, so the committed suite is currently empty. When each feature lands it must add these fixtures:

| Feature | Example scenarios |
|---|---|
| F-POLICY-001 policy-version validation | known version accepted; unknown version rejected with evidence |
| F-FEE-001 fee rule evaluation | percentage fee; flat fee; minor-unit rounding at the half boundary |
| F-SETTLEMENT-001 settlement-window classification | in-window, edge-of-window, and after-cutoff inputs |

Until those features are implemented, this document records the rule, not a passing suite; see [`docs/roadmap/current-status.md`](../roadmap/current-status.md).

## Preventing regressions

- Changing a fixture's expected decision is a behavior change: it is called out, justified, and approved, never edited to match new output.
- Removing or weakening a fixture is reviewed as a guardrail removal.
- A regression keeps the fixture that caught it; the fix restores the expected decision.
- A sampled or time-boxed run states what was not exercised.

## Authority boundary

Fixtures record and verify behavior; they do not govern it. Where a fixture disagrees with `docs/product/prd.md`, the PRD governs and the fixture is corrected through the normal change process. Passing the suite is a precondition for implementation approval, not a substitute for it.

## Release gate

Granite's scenario suite is a release gate: a release that would change an advertised decision, or that cannot show the suite passing on the exact revision being released, does not proceed without explicit owner approval. See [`docs/release/release-governance.md`](../release/release-governance.md).
