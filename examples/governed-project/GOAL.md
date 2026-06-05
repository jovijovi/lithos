# Granite Project Goal

## One-sentence product positioning

`Granite` is a small payments-domain rules library that gives downstream services a reviewed, deterministic way to calculate fee and settlement decisions without embedding policy logic in every service.

## Product identity

Granite is a local library. It is not a payment processor, not a wallet, not an operations console, and not a live settlement service.

```text
Downstream service
  -> supplies transaction facts and selects a policy version
Granite
  -> validates inputs, evaluates local rules, returns deterministic decision evidence
External payment networks
  -> remain outside this project
```

## What this project owns

- Fee and settlement rule evaluation.
- Policy-version validation.
- Deterministic local decision evidence.
- Documentation showing how rules are approved, verified, and released.

## What adjacent systems own

- Actual money movement.
- Customer communication.
- Production deployment and monitoring.
- Regulatory reporting outside local rule evidence.

## Source-of-truth index

Read these in order for product, design, roadmap, and implementation work:

1. Product requirements: `docs/product/prd.md`
2. System architecture: `docs/design/architecture.md`
3. Technical design: `docs/design/technical-solution.md`
4. Feature completion tracking: `docs/roadmap/features.md`
5. Roadmap and phase status: `docs/roadmap/current-status.md`
6. Development workflow: `docs/AI_FLOW.md`
7. Documentation index: `docs/INDEX.md`

`GOAL.md` is intentionally stable. It defines product positioning and points to the living documents above; it is not a phase tracker.
