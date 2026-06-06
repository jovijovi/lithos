# AGENTS.md

Project-local instructions for AI agents working in the Granite example.

## Project identity

- Project: `Granite`
- Visibility: example repository content
- Integration branch: `main`

## Product and documentation preflight

Documentation precedes implementation. For roadmap, design, implementation, PR, CI, review, merge, or next-phase-readiness work, read in order:

1. `GOAL.md`
2. `docs/product/prd.md`
3. `docs/design/architecture.md`
4. `docs/design/technical-solution.md`
5. `docs/roadmap/features.md`
6. `docs/roadmap/current-status.md`
7. `docs/AI_FLOW.md`

Before changing files, state the current product position, target feature or phase, open tails, explicit non-approvals, and whether the requested task is allowed by the roadmap.

## Development workflow

Use short-lived task branches and isolated worktrees for AI-assisted work. Derive implementation plans from PRD, design, roadmap, and current status. A plan must not redefine product goals.

## Product boundaries

Do not infer live settlement, payment-network calls, release publication, destructive branch actions, or external delivery from ordinary implementation approval. These require explicit higher-gate approval in `docs/AI_FLOW.md`.

Agents may open and update their own pull requests as preparation, but must never self-approve, self-merge, enable ownerless auto-merge, delete branches, publish, or perform live/external/destructive actions without explicit owner approval. Adopting Lithos is not authorization for any of these.

## Secrets and credentials

Never commit secrets, API keys, tokens, cookies, raw environment values, private platform identifiers, or signed URLs. Use `[REDACTED]` in docs and examples when referring to sensitive values.

## Tooling expectations

- Run `python scripts/verify_project.py` (the bundled local verifier) before claiming completion; it checks the document spine and gate vocabulary, then runs the docs index check, the drift self-test and check, and the static safety scan. Re-run any individual gate from `docs/AI_FLOW.md` in isolation when one fails, and finish with `git diff --check`.
- Update `docs/roadmap/features.md` and `docs/roadmap/current-status.md` when feature status, acceptance evidence, or open tails change.
- Keep `docs/INDEX.md` aligned with documentation changes.
- Record task evidence in `docs/dev_log/` when work is non-trivial.
- Update `docs/lessons/`, `docs/practices/`, and root `LESSONS.md` when the work produces reusable knowledge.
- Update `README.md` and `README.zh-CN.md` together when user-facing claims change.
- Run `python tools/build_docs_index.py --check` and `python tools/docs_drift_signal.py --check` before claiming documentation governance is current.
- Run `python tools/static_safety_scan.py` before claiming a change is safe to commit; it rejects secret-shaped tokens, private machine-local paths, and unfinished-work placeholders as a first-class gate, and also runs inside `scripts/verify_project.py`.
- Treat publishing as a destructive/external action under `docs/release/release-governance.md`: never publish, tag, or release on your own authority, and back behavior-bearing claims with the fixtures required by `docs/evaluation/scenario-regression.md`. Granite is at R0 and has no product test suite yet; that gate becomes required once product implementation starts.
- Treat knowledge records (`docs/dev_log/`, `docs/lessons/`, `docs/practices/`) as informative: they inform future work but never override the authority chain or clear an approval gate.
- Keep collaboration artifacts vendor-neutral, plain-text, and portable across tools; never embed vendor or product names or secret values.
- Declare Granite's Lithos conformance — version, single `full-lifecycle-governance` model, role holders, gate operation, verification stance, and autonomous PR policy — in an adoption manifest; the manifest is a declaration, not an authorization.
