# Governed Project Structure

Lithos defines exactly one governance model: the full lifecycle. This document describes the structure that model uses — a documentation authority chain plus a knowledge spine that keeps product intent, design, roadmap, implementation plans, verification, lessons, practices, and agent behavior aligned. There are no adoption tiers; a small project keeps these anchors concise, but the structure is present either way.

The local workflow file, an agent contract, and a PR checklist are components of this structure, not a separate adoption mode. A small, single-maintainer, or early-stage project may keep most files terse and its lessons and practices anchors empty but present; a project with formal review, multi-agent work, staged roadmaps, release gates, compliance needs, or product/runtime boundaries fills the same structure in with full detail.

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
| `docs/roadmap/current-status.md` | Lean current-decision entrypoint: active phase, high-signal tails, acceptance gates, and safety boundaries. | Product requirement redefinition, full history ledgers, generated metadata, PR/CI indexes, or bulky evidence catalogs. |
| `docs/plans/` | Approved task or phase implementation plans. | Roadmap ownership or product authority. |
| `docs/dev_log/` | Task evidence logs, decisions, review outcomes, verification summaries. | Product requirements or roadmap ownership. |
| `docs/lessons/` | Reusable lessons learned from concrete work, with drift tracking when useful. | Raw task logs or temporary status. |
| `docs/practices/` | Reusable practices future contributors should apply. | One-off status updates. |
| `docs/evaluation/scenario-regression.md` | Scenario fixture policy for behavior-bearing claims and examples. | Product requirements or implementation approval. |
| `docs/release/release-governance.md` | Release gate, provenance, and supply-chain evidence. | Publishing approval or secret material. |
| `LESSONS.md` | Root entry point for lessons and practices. | Detailed evidence or generated reports. |
| `docs/AI_FLOW.md` | Local human-AI development workflow and gate semantics. | Runtime authorization beyond what the project separately approves. |
| `AGENTS.md` | Short agent-facing contract and preflight order. | Full product truth; it points to the authority chain. |
| `.github/PULL_REQUEST_TEMPLATE.md` | Per-unit review checklist and evidence capture. | Long-form design or roadmap content. |
| `docs/environment-policy.md` (or a section of `docs/AI_FLOW.md`) | Declared environment/sandbox boundaries: filesystem roots, network egress, credential scope, and external side effects a run may touch. | Product authority, gate approval, or any live/runtime authorization. |
| Agent run manifests / audit log (retained with run evidence, e.g. under `docs/dev_log/`) | Per-run record of what was authorized, what actually ran (local/offline vs external/live), and the boundary that held. | Product authority, granting approval, or licensing live/runtime execution. |

The environment policy and run manifests are boundary and evidence records: one describes limits, the other documents runs. Neither carries product authority, clears a [gate](approval-semantics.md), or authorizes live/runtime execution. See [environment and sandbox policy](environment-and-sandbox-policy.md) and [agent run manifest](agent-run-manifest.md).

Agent pull-request activity follows the [autonomous PR policy](autonomous-pr-policy.md): an agent may open and update its own pull requests, but must never self-approve, self-merge, or land work without the owner's implementation-gate approval.

## Recommended directory map

```text
.
├── GOAL.md
├── README.md
├── README.zh-CN.md              # optional but recommended for bilingual projects
├── LESSONS.md
├── AGENTS.md
├── lithos-adoption-manifest.json # machine-readable conformance declaration
├── .github/PULL_REQUEST_TEMPLATE.md
├── .github/workflows/verify.yml
├── docs/
│   ├── AI_FLOW.md
│   ├── environment-policy.md     # declared run boundaries (optional; may live inside AI_FLOW.md)
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
│   ├── practices/README.md
│   ├── evaluation/scenario-regression.md
│   └── release/release-governance.md
├── tools/
│   ├── build_docs_index.py
│   ├── docs_drift_signal.py
│   └── static_safety_scan.py
├── src/ or package code
├── tests/
└── fixtures/ or examples/ when contract evidence matters
```

The exact code layout is local choice. The governed document spine and knowledge spine above are the portable parts; their artifact boundaries and vendor-neutrality rules are defined in [tooling interoperability](tooling-interoperability.md). `docs/INDEX.md` should index only files under `docs/`; root entry points such as `README.md`, `GOAL.md`, and `LESSONS.md` stay outside that generated corpus. A project claiming Lithos conformance keeps a machine-readable [adoption manifest](conformance-and-fixtures.md) (for example `lithos-adoption-manifest.json`) declaring the version, the single governance model, roles, gates, verification, and autonomous PR policy; the manifest is a declaration, not part of the authority chain, and clears no gate.

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

Generate `docs/INDEX.md` from docs-directory frontmatter and keep it docs-only. Generate `docs/lessons/_drift_report.md` from lesson/practice `applies_to` paths, then commit both generated artifacts when they change. Run `tools/static_safety_scan.py` with the same verification gate set so secret-shaped values, private machine-local paths, and unfinished-work placeholders cannot enter the evidence chain.

The full lifecycle — born-state, use-driven validation, the immutability of frozen records, evidence retention, and the authority boundary that knowledge records but never governs — is defined in [knowledge governance](knowledge-governance.md).

If a project has localized README files, update them together with `README.md` whenever user-facing claims change. Semantic alignment matters more than literal translation.

## Status records, kept lean

`docs/roadmap/features.md`, `docs/roadmap/current-status.md`, and `docs/dev_log/` must keep what governs the work: phase authority, the current decision, open tails, and any safety boundary a reader needs in order to act safely. They **should not** carry duplicated status prose that git history, CI, pull-request metadata, or the generated `docs/INDEX.md` and drift report already make true. Add or change a status record when it moves user-visible truth, phase authority, the current decision or tail state, or a safety boundary; skip routine post-merge bookkeeping entries, repeated non-approval paragraphs, and stale-text hunts that derive no new truth.

Treat `docs/roadmap/current-status.md` as a dashboard entrypoint, not as the whole status database. When long phase history, full tail tables, evidence paths, generated machine metadata, reference lists, or boundary prose become too large for fast preflight reading, split them into named companion files under `docs/roadmap/` and leave concise pointers in `current-status.md`. Do not solve status bloat by deleting safety information; move bulky detail to the right owner and keep the entrypoint's current decision, high-signal tails, and explicit non-approvals intact. Keeping these anchors lean preserves the spine's authority and safety signal instead of burying it in churn — it does not relax the [verification](verification-standards.md) or [approval](approval-semantics.md) requirements those records sit beside.

Task and status rows in these records are implementer progress check-ins: a `Done` or equivalent mark is the implementer's claim that the current task state is complete, which [verification](verification-standards.md), independent review, and CI confirm or send back for repair — it is not by itself quality, behavior, safety, or merge proof. Word each row for the current task state only (for example `Design task complete` or `Implementation task complete`), and keep future-process predictions — `waiting for review`, `pending the next gate`, `implementation will follow`, `after merge` — out of the row. Record future work, blockers, and explicit non-approvals in the tail and non-approval sections that own them.

## Plan placement rule

Task-level implementation plans live in `docs/plans/` and are named:

```text
docs/plans/YYYY-MM-DD-<task-slug>.md
```

A plan derives from PRD, design, roadmap, and current status. It must include context, checklist, acceptance criteria, likely changed files, verification gates, risks, and rollback. It must not redefine product goals or imply new live/runtime approval.

## Where the structure becomes load-bearing

The full lifecycle structure is always present; these conditions are where its heavier parts stop being terse anchors and must be filled in:

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
- [`docs/evaluation/scenario-regression.md`](../templates/governed-project/docs/evaluation/scenario-regression.md)
- [`docs/release/release-governance.md`](../templates/governed-project/docs/release/release-governance.md)
- [`tools/build_docs_index.py`](../templates/governed-project/tools/build_docs_index.py), [`tools/docs_drift_signal.py`](../templates/governed-project/tools/docs_drift_signal.py), and [`tools/static_safety_scan.py`](../templates/governed-project/tools/static_safety_scan.py)

A local project may add stricter rules. It must not weaken Lithos's approval gates, human approval authority, isolation discipline, or evidence-before-completion rule.
