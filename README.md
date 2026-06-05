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
- **Worktree & branch discipline** — isolation of in-progress work so human and agent changes stay reviewable. See [`docs/core-concepts.md`](docs/core-concepts.md).
- **Verification standards** — evidence over agreement: tests, CI, reviews, artifacts, reproducibility. See [`docs/verification-standards.md`](docs/verification-standards.md).
- **Templates** — ready-to-copy local workflow files in [`templates/`](templates/), minimal and governed.
- **Governed project structure** — a fuller document authority chain for mature repos: `GOAL.md`, PRD, design, roadmap/status, feature tracker, phase plans, and `docs/AI_FLOW.md`. See [`docs/governed-project-structure.md`](docs/governed-project-structure.md).
- **Skills** — reusable operational procedures in [`skills/`](skills/) for creating, auditing, and adapting a local AI flow.
- **Examples** — worked adoptions in [`examples/`](examples/), from a single contributor to a governed project.

## Scope — what Lithos is not

Lithos is a **software-development collaboration standard and toolkit**. It is **not** a runtime, an agent framework, or an execution product.

Adopting Lithos does **not** authorize autonomous or live AI execution. Its approval semantics are *organizational* — they describe when a human has sanctioned a class of work, not a grant of machine permission. Any live, destructive, or externally visible action still requires the explicit, contemporaneous approval defined by the adopting project. See [`docs/approval-semantics.md`](docs/approval-semantics.md).

## Quick adoption

1. Read [`docs/philosophy.md`](docs/philosophy.md) and [`docs/core-concepts.md`](docs/core-concepts.md).
2. Choose where your collaboration rules will live — pick your own local workflow filename (e.g. `AI_FLOW.md`, `ai-collaborative-development-standards.md`, or a name that fits your repo). See [`docs/local-adoption.md`](docs/local-adoption.md).
3. Copy a starting point: [`templates/minimal-ai-flow.md`](templates/minimal-ai-flow.md) for a small project, [`templates/governed-ai-flow.md`](templates/governed-ai-flow.md) for workflow-only formal review, or the full [`templates/governed-project/`](templates/governed-project/) spine for a mature governed repo.
4. Add the [`templates/AGENTS.md.snippet`](templates/AGENTS.md.snippet) contract to your `AGENTS.md`.
5. Adopt [`templates/pr-checklist.md`](templates/pr-checklist.md) and the [verification standards](docs/verification-standards.md).

A worked walkthrough lives in [`examples/minimal-project/`](examples/minimal-project/) and [`examples/governed-project/`](examples/governed-project/).

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
│   ├── local-adoption.md
│   ├── governed-project-structure.md
│   ├── verification-standards.md
│   └── versioning-and-governance.md
├── skills/                    Reusable operational procedures
│   ├── create-local-ai-flow/
│   ├── audit-local-ai-flow/
│   └── adapt-ai-flow-for-governed-project/
├── templates/                 Copy-ready local adoption files and governed project spine
├── examples/                  Worked adoptions
└── scripts/                   Repository verification (stdlib Python)
```

## Governance & versioning

Lithos is versioned and governed as a standard, not as a moving codebase. See [`docs/versioning-and-governance.md`](docs/versioning-and-governance.md) and [`AGENTS.md`](AGENTS.md).

## License

Released under the [MIT License](LICENSE).

Copyright (c) 2026 jovijovi and Lithos Contributors.
