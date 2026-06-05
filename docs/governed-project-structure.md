# Governed Project Structure

Lithos can be adopted at two depths:

1. **Workflow-only adoption** — a local workflow file, an agent contract, and a PR checklist.
2. **Governed project adoption** — a full documentation authority chain that keeps product intent, design, roadmap, implementation plans, verification, and agent behavior aligned.

Small projects may start with workflow-only adoption. Projects with formal review, multi-agent work, staged roadmaps, release gates, compliance needs, or product/runtime boundaries should use the governed project structure.

## Authority chain

Governed projects should keep this chain explicit:

```text
GOAL.md -> docs/product/prd.md -> docs/design/architecture.md + docs/design/technical-solution.md -> docs/roadmap/features.md + docs/roadmap/current-status.md -> docs/plans/YYYY-MM-DD-<task-slug>.md -> code and artifacts
```

Each link has one job:

| File | Owns | Must not own |
|---|---|---|
| `GOAL.md` | Stable product positioning and source-of-truth index. | Phase status, task instructions, temporary evidence. |
| `docs/product/prd.md` | Product requirements, users, non-users, principles, non-goals. | Module design, implementation sequencing. |
| `docs/design/architecture.md` | System-level architecture, diagrams, trust boundaries, responsibility split. | Product scope changes or phase closure claims. |
| `docs/design/technical-solution.md` | Module-level design, data models, file responsibilities, test strategy. | Product requirement changes. |
| `docs/roadmap/features.md` | Capability tracker: status, evidence, remaining acceptance. | Step-by-step execution plans. |
| `docs/roadmap/current-status.md` | Living phase tracker, current decision, open tails, acceptance gates. | Product requirement redefinition. |
| `docs/plans/` | Approved task or phase implementation plans. | Roadmap ownership or product authority. |
| `docs/AI_FLOW.md` | Local human-AI development workflow and gate semantics. | Runtime authorization beyond what the project separately approves. |
| `AGENTS.md` | Short agent-facing contract and preflight order. | Full product truth; it points to the authority chain. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Per-unit review checklist and evidence capture. | Long-form design or roadmap content. |

## Recommended directory map

```text
.
├── GOAL.md
├── README.md
├── AGENTS.md
├── .github/PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── AI_FLOW.md
│   ├── INDEX.md
│   ├── product/prd.md
│   ├── design/architecture.md
│   ├── design/technical-solution.md
│   ├── roadmap/README.md
│   ├── roadmap/features.md
│   ├── roadmap/current-status.md
│   └── plans/README.md
├── src/ or package code
├── tests/
├── scripts/ or tools/
└── fixtures/ or examples/ when contract evidence matters
```

The exact code layout is local choice. The governed document spine above is the portable part.

## Preflight rule for governed work

Before roadmap, design, implementation, PR, review, merge, or next-phase-readiness work, agents should read in order:

1. `GOAL.md`
2. `docs/product/prd.md`
3. `docs/design/architecture.md`
4. `docs/design/technical-solution.md`
5. `docs/roadmap/features.md`
6. `docs/roadmap/current-status.md`
7. `docs/AI_FLOW.md`

Then state:

- current product position;
- requested feature or phase target;
- open tails and explicit non-approvals;
- whether the requested task is allowed by the roadmap;
- which verification gates will prove the work.

## Plan placement rule

Task-level implementation plans live in `docs/plans/` and are named:

```text
docs/plans/YYYY-MM-DD-<task-slug>.md
```

A plan derives from PRD, design, roadmap, and current status. It must include context, checklist, acceptance criteria, likely changed files, verification gates, risks, and rollback. It must not redefine product goals or imply new live/runtime approval.

## When to choose this structure

Use the governed structure when any of these are true:

- work proceeds through phases or release gates;
- multiple agents or contributors may act in parallel;
- the project has external side effects, publishing, runtime, private data, or destructive operations;
- a reviewer needs to reconstruct why a change was allowed;
- roadmap status and implementation evidence must stay separate;
- old plans or chat history have already caused drift.

## Templates

Copy the governed starter set from [`templates/governed-project/`](../templates/governed-project/):

- [`GOAL.md`](../templates/governed-project/GOAL.md)
- [`AGENTS.md`](../templates/governed-project/AGENTS.md)
- [`PR checklist`](../templates/pr-checklist.md)
- [`docs/AI_FLOW.md`](../templates/governed-project/docs/AI_FLOW.md)
- [`docs/product/prd.md`](../templates/governed-project/docs/product/prd.md)
- [`docs/design/architecture.md`](../templates/governed-project/docs/design/architecture.md)
- [`docs/design/technical-solution.md`](../templates/governed-project/docs/design/technical-solution.md)
- [`docs/roadmap/features.md`](../templates/governed-project/docs/roadmap/features.md)
- [`docs/roadmap/current-status.md`](../templates/governed-project/docs/roadmap/current-status.md)
- [`docs/plans/README.md`](../templates/governed-project/docs/plans/README.md)

A local project may add stricter rules. It must not weaken Lithos's approval gates, human approval authority, isolation discipline, or evidence-before-completion rule.
