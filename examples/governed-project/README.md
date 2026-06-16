# Example — Governed Project

A worked example of adopting [Lithos](../../README.md) in a project with formal review, multiple contributors, staged roadmap work, and audit obligations.

This stands in for a hypothetical payments library, **Granite**, maintained by a team that ships to downstream consumers and must be able to reconstruct how any change was approved and verified.

## What this example demonstrates

- The complete lifecycle document spine from [`docs/governed-project-structure.md`](../../docs/governed-project-structure.md).
- `GOAL.md` as a stable product-positioning and source-of-truth index.
- Product requirements in `docs/product/prd.md`.
- System architecture and module detail split across `docs/design/architecture.md` and `docs/design/technical-solution.md`.
- Feature/status governance split across `docs/roadmap/features.md` and `docs/roadmap/current-status.md`, with status records kept lean so they capture phase authority, current decisions, open tails, and safety boundaries rather than duplicating git history, CI, PR metadata, or generated artifacts.
- Task-level implementation plan rules in `docs/plans/README.md`.
- The local Lithos workflow at `docs/AI_FLOW.md`.
- Knowledge capture through `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, root `LESSONS.md`, and generated drift reports — records that inform future work but never override the authority chain or clear an approval gate.
- A Lithos conformance claim suitable for a machine-readable adoption manifest: version, single full-lifecycle governance model, roles, gates, verification, and autonomous PR policy, kept vendor-neutral and portable across tools.
- An autonomous PR policy: agents may open and update pull requests, but never self-approve, self-merge, enable ownerless auto-merge, delete branches, publish, or perform live/external actions without explicit owner approval.
- Reproducible verification gates that actually run in this directory: a bundled local verifier (`scripts/verify_project.py`), a docs index check (`tools/build_docs_index.py`), an activity-aware drift signal (`tools/docs_drift_signal.py`), and a first-class static safety scan (`tools/static_safety_scan.py`).
- Static safety as a first-class gate: `tools/static_safety_scan.py` rejects secret-shaped tokens, private machine-local paths, and unfinished-work placeholders, and runs inside `scripts/verify_project.py`.
- Scenario-regression and release governance: `docs/evaluation/scenario-regression.md` pins behavior-bearing claims to named fixtures, and `docs/release/release-governance.md` keeps publishing owner-approved and provenance-bearing — never cut by an agent on its own authority.
- Generated knowledge drift evidence in `docs/lessons/_drift_report.md`, produced by `tools/docs_drift_signal.py`.
- Bilingual README governance through `README.md` and `README.zh-CN.md`.

## Verification gates

These gates are runnable from this example directory and are what an agent or contributor runs before opening a PR:

```bash
python scripts/verify_project.py
python tools/build_docs_index.py --check
python tools/docs_drift_signal.py --check
python tools/static_safety_scan.py
git diff --check
```

`scripts/verify_project.py` is the single local verifier entry point; it checks the governed spine and gate vocabulary, then runs the docs index check, the drift self-test and check, and the static safety scan. The repository's root verification (`scripts/verify_docs.py`) also invokes it, so the example's self-declared gates stay truthful.

Granite is at R0, a documentation authority baseline, so it ships no product test suite yet. Behavior tests and scenario fixtures from `docs/evaluation/scenario-regression.md` become required once product implementation starts; the verification block never claims a behavior gate that does not yet exist.

## Files

- [`README.md`](README.md) — English example entry point.
- [`README.zh-CN.md`](README.zh-CN.md) — Chinese example entry point.
- [`GOAL.md`](GOAL.md) — stable product goal and source-of-truth index.
- [`docs/AI_FLOW.md`](docs/AI_FLOW.md) — local AI-assisted development workflow.
- [`AGENTS.md`](AGENTS.md) — agent-facing contract.
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) — PR evidence checklist.
- [`docs/INDEX.md`](docs/INDEX.md) — generated docs-directory index.
- [`scripts/verify_project.py`](scripts/verify_project.py) — bundled local verifier gate.
- [`LESSONS.md`](LESSONS.md) — root entry point for lessons and practices.
- [`ai-collaborative-development-standards.md`](ai-collaborative-development-standards.md) — compatibility pointer to `docs/AI_FLOW.md`.

## How it was adopted

1. Started from [`templates/governed-project/`](../../templates/governed-project/).
2. Kept `docs/AI_FLOW.md` as the operational local workflow file.
3. Added the product/design/roadmap/plans spine so development tasks trace from goal to evidence.
4. Added the dev-log/lesson/practice knowledge spine and generated docs index/drift tooling.
5. Updated `AGENTS.md`, bilingual READMEs, and the PR checklist to match the stricter flow.

The local workflow template [`templates/governed-ai-flow.md`](../../templates/governed-ai-flow.md) remains a useful component reference, but this example demonstrates the complete lifecycle structure Lithos expects even when a real project keeps some content concise.
