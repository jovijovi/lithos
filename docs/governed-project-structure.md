# Governed Project Structure

Lithos can be adopted at two governed depths:

1. **Lighter governed workflow adoption** — a local workflow file, an agent contract, and a PR checklist. This is thinner than a full project spine, but it still preserves roles, approval gates, isolation discipline, and evidence.
2. **Full governed project adoption** — a full documentation authority chain plus a knowledge spine that keeps product intent, design, roadmap, implementation plans, verification, lessons, practices, and agent behavior aligned.

Small projects may start with the lighter governed workflow. Projects with formal review, multi-agent work, staged roadmaps, release gates, compliance needs, or product/runtime boundaries should use the full governed project structure.

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
| `docs/dev_log/` | Task evidence logs, decisions, review outcomes, verification summaries. | Product requirements or roadmap ownership. |
| `docs/lessons/` | Reusable lessons learned from concrete work, with drift tracking when useful. | Raw task logs or temporary status. |
| `docs/practices/` | Reusable practices future contributors should apply. | One-off status updates. |
| `LESSONS.md` | Root entry point for lessons and practices. | Detailed evidence or generated reports. |
| `docs/AI_FLOW.md` | Local human-AI development workflow and gate semantics. | Runtime authorization beyond what the project separately approves. |
| `AGENTS.md` | Short agent-facing contract and preflight order. | Full product truth; it points to the authority chain. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Per-unit review checklist and evidence capture. | Long-form design or roadmap content. |

## Recommended directory map

```text
.
├── GOAL.md
├── README.md
├── README.zh-CN.md              # optional but recommended for bilingual projects
├── LESSONS.md
├── AGENTS.md
├── .github/PULL_REQUEST_TEMPLATE.md
├── .github/workflows/verify.yml
├── docs/
│   ├── AI_FLOW.md
│   ├── INDEX.md                 # generated docs-directory index
│   ├── product/prd.md
│   ├── design/architecture.md
│   ├── design/technical-solution.md
│   ├── roadmap/README.md
│   ├── roadmap/features.md
│   ├── roadmap/current-status.md
│   ├── plans/README.md
│   ├── dev_log/README.md
│   ├── lessons/README.md
│   ├── lessons/_drift_report.md # generated drift report
│   └── practices/README.md
├── tools/
│   ├── build_docs_index.py
│   └── docs_drift_signal.py
├── src/ or package code
├── tests/
└── fixtures/ or examples/ when contract evidence matters
```

The exact code layout is local choice. The governed document spine and knowledge spine above are the portable parts. `docs/INDEX.md` should index only files under `docs/`; root entry points such as `README.md`, `GOAL.md`, and `LESSONS.md` stay outside that generated corpus.

## Preflight rule for governed work

Before roadmap, design, implementation, PR, review, merge, or next-phase-readiness work, agents should read in order:

1. `GOAL.md`
2. `docs/product/prd.md`
3. `docs/design/architecture.md`
4. `docs/design/technical-solution.md`
5. `docs/roadmap/features.md`
6. `docs/roadmap/current-status.md`
7. `docs/AI_FLOW.md`
8. `LESSONS.md` and `docs/lessons/_drift_report.md` when the task touches lessons/practices or README-visible governance claims

Then state:

- current product position;
- requested feature or phase target;
- open tails and explicit non-approvals;
- whether the requested task is allowed by the roadmap;
- which verification gates will prove the work.

## Knowledge spine rule

Use `docs/dev_log/` for task evidence and decision logs. Use `docs/lessons/` for reusable lessons and `docs/practices/` for reusable practices. Use root `LESSONS.md` as the discoverable entry point.

Generate `docs/INDEX.md` from docs-directory frontmatter and keep it docs-only. Generate `docs/lessons/_drift_report.md` from lesson/practice `applies_to` paths, then commit both generated artifacts when they change.

If a project has localized README files, update them together with `README.md` whenever user-facing claims change. Semantic alignment matters more than literal translation.

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
- lessons and practices should accumulate outside chat history;
- user-facing README files exist in more than one language and must stay aligned;
- old plans or chat history have already caused drift.

## Templates

Copy the governed starter set from [`templates/governed-project/`](../templates/governed-project/):

- [`README.md`](../templates/governed-project/README.md) and [`README.zh-CN.md`](../templates/governed-project/README.zh-CN.md)
- [`GOAL.md`](../templates/governed-project/GOAL.md)
- [`LESSONS.md`](../templates/governed-project/LESSONS.md)
- [`AGENTS.md`](../templates/governed-project/AGENTS.md)
- [`PR checklist`](../templates/pr-checklist.md)
- [`docs/AI_FLOW.md`](../templates/governed-project/docs/AI_FLOW.md)
- [`docs/product/prd.md`](../templates/governed-project/docs/product/prd.md)
- [`docs/design/architecture.md`](../templates/governed-project/docs/design/architecture.md)
- [`docs/design/technical-solution.md`](../templates/governed-project/docs/design/technical-solution.md)
- [`docs/roadmap/features.md`](../templates/governed-project/docs/roadmap/features.md)
- [`docs/roadmap/current-status.md`](../templates/governed-project/docs/roadmap/current-status.md)
- [`docs/plans/README.md`](../templates/governed-project/docs/plans/README.md)
- [`docs/dev_log/README.md`](../templates/governed-project/docs/dev_log/README.md)
- [`docs/lessons/README.md`](../templates/governed-project/docs/lessons/README.md)
- [`docs/practices/README.md`](../templates/governed-project/docs/practices/README.md)
- [`tools/build_docs_index.py`](../templates/governed-project/tools/build_docs_index.py) and [`tools/docs_drift_signal.py`](../templates/governed-project/tools/docs_drift_signal.py)

A local project may add stricter rules. It must not weaken Lithos's approval gates, human approval authority, isolation discipline, or evidence-before-completion rule.
