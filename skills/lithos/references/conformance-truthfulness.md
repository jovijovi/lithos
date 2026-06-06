# Conformance Truthfulness

A conformance claim is only worth as much as its honesty. Across every Lithos intent the same rule holds: **what the project says must match what the project does.** The normative basis is [conformance and fixtures](../../../docs/conformance-and-fixtures.md).

## Everything must agree

A claim is truthful only when these are mutually consistent:

- **Prose** — the local workflow file and any conformance statement describe the project as it actually operates, with no requirement quietly dropped.
- **Manifest, schema, and checker** — the adoption manifest is schema-valid and behaves exactly as the [checker](../../../scripts/verify_conformance_fixtures.py) enforces, including that a manifest declaring it does *not* claim conformance is rejected, not accepted as a smaller claim.
- **Fixtures** — the valid [conformance fixtures](../../../fixtures/conformance/) pass for the right reasons, and every `invalid-*` fixture still fails for its documented reason; weakening one into a pass silently removes a guardrail.
- **Worked-example commands** — any command a project's docs tell a reader to run must actually run in that project and produce the stated result. A gate that lists a command which cannot run there is a broken, untruthful gate.

## Evidence, not assertion

The [static safety scan](../../../docs/static-safety-scan.md) is safety evidence, **not behavior proof**; behavior is proven by [scenario regression](../../../docs/scenario-regression-governance.md) fixtures and tests. A behavior-bearing claim with no fixture behind it is an assertion and must be reported as such, never presented as proven. When prose and a checker appear to disagree, the prose governs and the checker is corrected — but neither may be left disagreeing.
