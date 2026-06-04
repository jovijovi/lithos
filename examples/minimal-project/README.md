# Example — Minimal Project

A worked example of adopting [Lithos](../../README.md) in a small, single-maintainer project.

This stands in for a hypothetical command-line tool, **Pebble**, maintained by one developer who works with AI agents day to day. It shows the *minimal* shape of conformance.

## What this example demonstrates

- A local workflow file written from [`templates/minimal-ai-flow.md`](../../templates/minimal-ai-flow.md), named **`AI_FLOW.md`** (the maintainer's chosen filename).
- Roles deliberately combined — one person is owner, operator, reviewer, and verifier — but the combination is stated, not accidental.
- The four approval gates operationalized for a project that never touches live systems.
- A lightweight, evidence-based definition of done.

## Files

- [`AI_FLOW.md`](AI_FLOW.md) — the local workflow file.

## How it was adopted

1. Read `docs/philosophy.md` and `docs/core-concepts.md`.
2. Chose the filename `AI_FLOW.md`.
3. Copied the minimal template and filled in every bracketed decision.
4. Added the [`AGENTS.md.snippet`](../../templates/AGENTS.md.snippet) contract to the project's `AGENTS.md` and adopted the [PR checklist](../../templates/pr-checklist.md).

Compare with the [governed example](../governed-project/README.md) to see what changes when a project adds formal review and an audit trail.
