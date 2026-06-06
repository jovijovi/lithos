<div align="center">

<img src="assets/lithos-logo-horizontal.png" alt="Lithos" width="420" />

### AI-Collaborative Software Development Standards

*Inscribe how humans and AI build software together.*

[English](README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Español](README.es.md)

</div>

---

## What Lithos is

Lithos is an open standard for **how humans and AI collaborate on software**. It defines the roles, the approval boundaries, the working discipline, and the evidence a project should expect when people and agents build software together — without prescribing any particular tool, vendor, or runtime.

It exists because AI-assisted development is now routine, but the *rules of engagement* are usually improvised. Lithos makes those rules explicit, reviewable, and portable across teams.

Read Lithos at three layers:

1. **Brand — Lithos.** A stable name and identity for the standard, so a project can say "we follow Lithos" and mean something precise.
2. **Formal standard — *AI-Collaborative Software Development Standards*.** The normative documents in [`docs/`](docs/): roles, approval semantics, verification, governance. These are written to be cited.
3. **Local adoption shape.** How a single repository actually adopts the standard: a local workflow file (whose name the project chooses), an `AGENTS.md` contract, a PR checklist, and the templates and skills that make the standard operational day to day.

## What Lithos defines

- **Roles** — a generic cast (owner, controller/operator, architect, implementation agent, reviewer, verifier) with clear authority boundaries. See [`docs/roles.md`](docs/roles.md).
- **Approval semantics** — distinct gates for preflight/preparation, implementation, destructive or external side effects, and live/runtime execution. See [`docs/approval-semantics.md`](docs/approval-semantics.md).
- **Environment & sandbox policy** — where a run may execute and what it may touch (filesystem, network, credentials, side effects), kept distinct from approval. See [`docs/environment-and-sandbox-policy.md`](docs/environment-and-sandbox-policy.md).
- **Worktree & branch discipline** — isolation of in-progress work so human and agent changes stay reviewable. See [`docs/core-concepts.md`](docs/core-concepts.md).
- **Verification standards** — evidence over agreement: tests, CI, reviews, artifacts, reproducibility. See [`docs/verification-standards.md`](docs/verification-standards.md).
- **Agent run manifest** — a per-run audit record of what was authorized, what actually ran, and the evidence and boundary involved; a record, not an authorization. See [`docs/agent-run-manifest.md`](docs/agent-run-manifest.md).
- **Templates** — ready-to-copy starting points in [`templates/`](templates/): the local workflow file on its own and the full project starter set, both components of the one full-lifecycle governance model.
- **Governed project structure** — a fuller document authority chain for mature repos: `GOAL.md`, PRD, design, roadmap/status, feature tracker, phase plans, and `docs/AI_FLOW.md`. See [`docs/governed-project-structure.md`](docs/governed-project-structure.md).
- **Knowledge spine** — development logs, lessons, practices, generated docs-only indexes, and drift reports for governed repos: `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, and `tools/`. How this knowledge lives, expires by use, and stays subordinate to the authority chain is defined in [`docs/knowledge-governance.md`](docs/knowledge-governance.md).
- **Conformance & adoption manifest** — what a project may claim, declared in a machine-readable adoption manifest ([`schemas/lithos-adoption-manifest.schema.json`](schemas/lithos-adoption-manifest.schema.json), filled from [`templates/lithos-adoption-manifest.json`](templates/lithos-adoption-manifest.json)), with [conformance fixtures](fixtures/conformance/) showing what passes and what must fail. See [`docs/conformance-and-fixtures.md`](docs/conformance-and-fixtures.md).
- **Autonomous PR policy** — what an agent may do with pull requests on its own, and what it must never self-approve or self-merge. See [`docs/autonomous-pr-policy.md`](docs/autonomous-pr-policy.md).
- **Static safety scan** — a deterministic gate that rejects secret-shaped values, private machine-local paths, and unfinished-work placeholders before review or release. See [`docs/static-safety-scan.md`](docs/static-safety-scan.md).
- **Scenario regression governance** — named fixtures that pin behavior-bearing claims and examples so regressions are caught mechanically. See [`docs/scenario-regression-governance.md`](docs/scenario-regression-governance.md).
- **Release & supply-chain governance** — owner-approved release gates, provenance records, and supply-chain boundaries for published artifacts. See [`docs/release-and-supply-chain-governance.md`](docs/release-and-supply-chain-governance.md).
- **Tooling interoperability** — the artifacts that carry collaboration state are vendor-neutral and portable, so a project can change tools without losing its governance. See [`docs/tooling-interoperability.md`](docs/tooling-interoperability.md).
- **Bilingual README governance** — source and localized README files stay semantically aligned when user-facing claims change.
- **Skills** — reusable operational procedures in [`skills/`](skills/): the single [`lithos`](skills/lithos/SKILL.md) umbrella skill routes an agent to adopt, audit, upgrade, review, or release-gate a project, with one procedure per intent under [`skills/lithos/references/`](skills/lithos/references/).
- **Examples** — a worked adoption of the full-lifecycle model in [`examples/`](examples/).

## Scope — what Lithos is not

Lithos is a **software-development collaboration standard and toolkit**. It is **not** a runtime, an agent framework, or an execution product.

Adopting Lithos does **not** authorize autonomous or live AI execution. Its approval semantics are *organizational* — they describe when a human has sanctioned a class of work, not a grant of machine permission. Any live, destructive, or externally visible action still requires the explicit, contemporaneous approval defined by the adopting project. See [`docs/approval-semantics.md`](docs/approval-semantics.md).

## Quick adoption

1. Read [`docs/philosophy.md`](docs/philosophy.md) and [`docs/core-concepts.md`](docs/core-concepts.md).
2. Choose where your collaboration rules will live — pick your own local workflow filename (e.g. `AI_FLOW.md`, `ai-collaborative-development-standards.md`, or a name that fits your repo). See [`docs/local-adoption.md`](docs/local-adoption.md).
3. Copy a starting point — both are components of the one full-lifecycle model: [`templates/governed-ai-flow.md`](templates/governed-ai-flow.md) is the local workflow file on its own, kept concise; the full [`templates/governed-project/`](templates/governed-project/) spine lays the same model out end to end with dev logs, lessons, practices, generated docs index, drift report, and bilingual README rules.
4. Add the [`templates/AGENTS.md.snippet`](templates/AGENTS.md.snippet) contract to your `AGENTS.md`.
5. Adopt [`templates/pr-checklist.md`](templates/pr-checklist.md) and the [verification standards](docs/verification-standards.md), and declare what you conform to in an [adoption manifest](templates/lithos-adoption-manifest.json).

A worked walkthrough lives in [`examples/governed-project/`](examples/governed-project/).

## Repository map

```
.
├── README.md                  Canonical landing page (this file)
├── README.<lang>.md           Localized landing pages
├── LICENSE                    MIT
├── AGENTS.md                  How agents contribute to this repository
├── docs/                      The formal standard (normative)
│   ├── philosophy.md
│   ├── core-concepts.md
│   ├── roles.md
│   ├── approval-semantics.md
│   ├── environment-and-sandbox-policy.md
│   ├── local-adoption.md
│   ├── governed-project-structure.md
│   ├── verification-standards.md
│   ├── agent-run-manifest.md
│   ├── knowledge-governance.md
│   ├── conformance-and-fixtures.md
│   ├── tooling-interoperability.md
│   ├── autonomous-pr-policy.md
│   ├── static-safety-scan.md
│   ├── scenario-regression-governance.md
│   ├── release-and-supply-chain-governance.md
│   └── versioning-and-governance.md
├── schemas/                   Machine-readable adoption manifest schema
├── skills/                    Reusable operational procedures
│   └── lithos/                Single umbrella skill: routes adopt / audit / upgrade / review / release
│       └── references/        One procedure per intent: adopt, audit, governed-upgrade, version-upgrade, pr-review, release-gate
├── templates/                 Copy-ready local adoption files and governed project spine
├── fixtures/                  Conformance fixtures (passing and rejecting)
├── examples/                  Worked adoptions
└── scripts/                   Repository verification (stdlib Python)
```

## Governance & versioning

Lithos is versioned and governed as a standard, not as a moving codebase. See [`docs/versioning-and-governance.md`](docs/versioning-and-governance.md) and [`AGENTS.md`](AGENTS.md).

## License

Released under the [MIT License](LICENSE).

Copyright (c) 2026 jovijovi and Lithos Contributors.
