# Core Concepts

This document defines the vocabulary Lithos uses. The terms are deliberately generic so they map onto any team, tool, or agent.

## Collaboration unit

A **collaboration unit** is one coherent piece of work — a feature, a fix, a document change — carried from intent to merged result. Every unit has an owning human, a stated intent, and a record of how it was verified. Lithos is organized around making each unit legible.

## Local workflow file

The **local workflow file** is the single document in an adopting repository that records how humans and AI collaborate there. Lithos does not mandate its name — a project chooses one that fits (for example `AI_FLOW.md` or `ai-collaborative-development-standards.md`). See [local adoption](local-adoption.md). It is the place where Lithos's generic rules become concrete commitments.

## Roles

Lithos separates *who does the work* from *who is accountable*. The generic cast — owner, controller/operator, architect, implementation agent, reviewer, verifier — is defined in [roles](roles.md). A single person or agent may hold several roles; the point is that each responsibility has an owner.

## Approval gates

An **approval gate** is a point where work may not proceed without a human sanction of the appropriate kind. Lithos defines four distinct gates — preparation/preflight, implementation, destructive/external side effect, and live/runtime execution — in [approval semantics](approval-semantics.md). Gates are layered: clearing one never implies clearing a higher one.

## Worktree and branch discipline

In-progress work **must** be isolated from the integration branch so that changes stay reviewable and revertible.

- **Branch discipline.** Each collaboration unit lives on its own branch, scoped to a single intent, named so its purpose is obvious. The integration branch (commonly `main`) reflects only reviewed, verified work.
- **Worktree discipline.** When humans and agents — or several units — proceed in parallel, each **should** operate in an isolated working tree (e.g. a separate checkout or a git worktree) so uncommitted changes never bleed across units.

The purpose of both is the same: at any moment, a reviewer can see exactly what a unit changed, in isolation, before it counts.

## Verification

**Verification** is the production of evidence that a unit does what it claims: tests, CI runs, reviews, artifacts, reproducible steps. Verification is distinct from assertion. An agent stating that something works is not verification; a passing test that a human can re-run is. See [verification standards](verification-standards.md).

## Evidence

**Evidence** is any artifact a third party can inspect or reproduce to confirm a claim — a test log, a CI link, a diff, a screenshot, a recorded command and its output. Lithos privileges evidence over agreement: consensus among collaborators, human or AI, does not substitute for it.

## Conformance

A project **conforms** to Lithos when it has a local workflow file that assigns the roles, honors the four approval gates, enforces worktree/branch discipline, and requires evidence-based verification before a unit is considered done. Everything else is local choice.
