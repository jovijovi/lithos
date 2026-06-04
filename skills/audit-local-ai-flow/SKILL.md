---
name: audit-local-ai-flow
description: Use when checking whether a project's local workflow file actually conforms to Lithos and matches how the project really works — produces a gap report covering roles, the four approval gates, discipline, verification, and drift from reality.
---

# Audit a Local AI Flow

Assess an existing **local workflow file** against Lithos and against the project's real practice. Output is a findings report; you do not silently rewrite the document.

## When to use

- Before relying on a local workflow file you did not write.
- Periodically, or after the team, tooling, or risk profile changes.
- When the document and observed behavior seem to disagree.

## Inputs to gather first

- The local workflow file (whatever it is named).
- The project's `AGENTS.md`, PR checklist, branch/CI configuration, and recent merged units as evidence of real practice.

## Conformance checklist

Check each item; record present / partial / missing with a pointer to the relevant Lithos doc.

1. **Roles** — every role in `docs/roles.md` has an owner; combined roles are stated explicitly; approval authority is not held by an agent.
2. **Approval gates** — all four gates from `docs/approval-semantics.md` are operationalized; layering is intact (no gate implies a higher one); the live/runtime stance is explicit.
3. **Discipline** — branch naming and worktree isolation are stated; the integration branch's allowed contents are defined (`docs/core-concepts.md`).
4. **Verification** — "done" requires reproducible evidence, not agreement; honesty obligations are present (`docs/verification-standards.md`).
5. **Discoverability** — the file is referenced from `README`/`AGENTS.md` and is a single source of truth.
6. **No placeholders** — no unresolved bracketed decisions remain.

## Drift checks (document vs. reality)

- Do recent merged units actually carry the evidence the file requires?
- Does observed branch/review practice match what the file states?
- Are destructive/external actions in practice covered by the file's gate-3 rules?

Flag any place the document describes a process the project does not follow — drift makes the file misleading, which is worse than silence.

## Output

A concise report: each checklist item with status and evidence, each drift finding, and a prioritized list of fixes. Recommend tightening (never loosening) where a requirement is weak. Propose changes; let the owner approve them.

## Done when

- Every checklist item and drift check has a verdict backed by a pointer.
- Gaps are listed with concrete, prioritized remediation.
- No finding is asserted without evidence from the file or the project's real practice.
