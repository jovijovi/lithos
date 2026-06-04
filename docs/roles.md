# Roles

Lithos defines roles by **responsibility and authority**, not by job title or by whether the actor is human or AI. One person may hold several roles; one role may be shared; an agent may hold a role a human would otherwise hold. What matters is that every responsibility below has a named owner for each collaboration unit.

The roles are generic on purpose. Map them onto your team and tools as you see fit.

## Owner (user / owner)

The human who is ultimately accountable for the work and who holds approval authority.

- Sets intent and priorities.
- Grants approvals at each [gate](approval-semantics.md). Approval authority **must not** be delegated to an agent.
- Accepts or rejects completed work.

## Controller / Operator

The actor who drives the collaboration session and operates the tools and agents — the orchestrating hand. May be the owner directly, or a human (or agent) acting on the owner's behalf.

- Sequences the work, dispatches agents, and relays context.
- Enforces that the right gate is cleared before the next step.
- Does **not** originate approvals; surfaces decisions to the owner.

## Architect

The actor responsible for design and approach before implementation.

- Decomposes intent into a plan and identifies risks and trade-offs.
- Defines the shape of the change and its acceptance criteria.
- Hands a clear, bounded brief to the implementation role.

## Implementation agent

The actor that produces the change — typically an AI agent, but the role is the same for a human.

- Implements within the approved plan and scope.
- Works on an isolated branch/worktree per [core concepts](core-concepts.md).
- Proposes; does not self-approve and does not widen scope without going back to the architect or owner.

## Reviewer

The actor who critically reads the proposed change for correctness, clarity, scope, and adherence to the local workflow file.

- Reviews for substance, not politeness — disagreement is the job.
- Independent of the implementation role wherever practical.
- Blocks merge until concerns are resolved or explicitly accepted by the owner.

## Verifier

The actor who confirms the change with **evidence** rather than opinion.

- Runs tests, CI, and reproduction steps; collects artifacts.
- Confirms claims are backed by inspectable evidence per [verification standards](verification-standards.md).
- Reports results faithfully, including failures and skipped steps.

## Separation of concerns

- Approval authority (owner) is never held by an implementation agent.
- Review and verification **should** be independent of implementation where the project's size allows.
- When roles are combined (common in small projects), the local workflow file **should** say so explicitly, so the combination is a choice rather than an accident.
