# Philosophy

Lithos exists to make the collaboration between humans and AI in software development **explicit, reviewable, and durable**. The name evokes stone: something you inscribe deliberately, that outlasts the moment.

## The problem

AI now writes, refactors, and reviews production code. The capability arrived faster than the conventions. In most projects the *rules of engagement* — who decides, what an agent may do unsupervised, what counts as "done" — live in someone's head or in a chat scrollback. They are inconsistent between repositories, invisible to new contributors, and impossible to audit after the fact.

That gap is not a tooling problem. It is a **standards** problem.

## What Lithos asserts

1. **Collaboration needs written rules, not vibes.** A project should be able to point to a document that says how humans and agents work together, and that document should be precise enough to settle a disagreement.
2. **Authority is human and explicit.** AI can propose, draft, and verify. It does not grant itself permission. Approval is an act a person takes, scoped to a class of work.
3. **Approval is layered, not binary.** Permission to prepare a change is not permission to ship it; permission to ship is not permission to take destructive or external action; none of those is permission to run autonomously against live systems. Conflating these layers is the root of most AI-collaboration incidents. See [approval semantics](approval-semantics.md).
4. **Evidence outranks agreement.** "The agent said it works" is not verification. Tests, CI results, reviews, artifacts, and reproducible steps are. See [verification standards](verification-standards.md).
5. **Discipline protects reviewability.** Isolated worktrees and scoped branches keep in-progress work legible, so a human can see exactly what changed before it counts. See [core concepts](core-concepts.md).
6. **Portability beats prescription.** Lithos describes the *shape* of good collaboration without dictating tools, vendors, or even filenames. A project adapts it locally. See [local adoption](local-adoption.md).
7. **Govern safety strictly; govern status leanly.** Governance weight belongs on what can cause harm — authority, approval gates, environment boundaries, and evidence — not on restating status that the project's own history already records. A status record earns its place when it changes user-visible truth, phase authority, the current decision or tail state, or a safety boundary; routine bookkeeping that metadata or generated artifacts can derive does not. See [verification standards](verification-standards.md).

## What Lithos is not

Lithos is a standard and a toolkit for *organizing development*. It is not a runtime, not an agent framework, and not a grant of autonomy. Adopting Lithos changes how a team agrees to work; it does not, by itself, authorize any machine to act.

## How to read the rest

The remaining documents are normative but lightweight. They use **must**, **should**, and **may** in the usual sense: *must* is a requirement for conformance, *should* is a strong recommendation, *may* is permitted. Where a document leaves a choice open, that openness is deliberate — fill it in locally.
