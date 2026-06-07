---
name: lithos
description: Use when an agent must apply the Lithos AI-collaboration standard to a real software project — adopting a project into Lithos, auditing whether it conforms, filling concise full-lifecycle governance anchors with more detail, upgrading its Lithos version, reviewing a pull request against Lithos, or running a release or acceptance gate — and whenever owner approval and multi-agent role boundaries must be preserved.
---

# Lithos

Lithos is an agent-neutral standard for how humans and AI collaborate on software. This skill is the **operational entry point** for an installed agent: it routes an intent to the right Lithos procedure. The repository's normative docs, schemas, templates, and verifiers **are the authority**; this skill points to them and never restates the standard in their place.

Installing this skill **does not make a project conformant**, and it is **not authorization** to merge, release, or act on live systems. Conformance is earned by meeting the requirements in [`docs/`](../../docs/); approval stays with the human owner (see [agent role boundaries](references/agent-role-boundaries.md)).

## Route the intent

| The owner wants to… | Use |
|---|---|
| Adopt a project into Lithos for the first time | [adopt a project](references/adopt-project.md) |
| Check whether a project actually conforms | [audit a project](references/audit-project.md) |
| Fill a concise adoption's anchors in with full detail as it grows | [governed upgrade](references/governed-upgrade.md) |
| Move a project from one Lithos version to a newer one | [version upgrade](references/version-upgrade.md) |
| Review a pull request against Lithos | [PR review](references/pr-review.md) |
| Run a release or acceptance gate | [release gate](references/release-gate.md) |

Two concerns cut across every intent and are read alongside the procedure above:

- [agent role boundaries](references/agent-role-boundaries.md) — owner-held approval, independent review and verification, and what an agent may never self-grant.
- [conformance truthfulness](references/conformance-truthfulness.md) — prose, manifest, schema, checker, fixtures, and worked-example commands must all match reality.

## What this skill does not do

- It does not install itself into a project or modify a project's tooling; community skill tooling handles installation.
- It does not clear an [approval gate](../../docs/approval-semantics.md), grant a release, or sanction live/runtime execution.
- It does not loosen any Lithos requirement. An agent may make a rule stricter locally; it may never drop one and still call the result Lithos.

Start from [`docs/local-adoption.md`](../../docs/local-adoption.md) when an intent is unclear, and from [`docs/conformance-and-fixtures.md`](../../docs/conformance-and-fixtures.md) for what a project may claim.
