# Knowledge Governance

A governed project accumulates knowledge: why a change was made, what broke, what pattern is worth repeating. Lithos treats that knowledge as a **governed artifact set**, not as chat history. This document defines the knowledge spine, how its artifacts live and expire, the evidence they retain, and — critically — the authority they do **not** hold.

Knowledge governance is a capability of [full governed project adoption](governed-project-structure.md). A [lighter governed workflow](local-adoption.md) keeps reusable knowledge out of chat history but is not required to maintain the full spine below.

## The knowledge spine

A governed project maintains exactly three long-lived knowledge artifact types under `docs/`, plus two generated artifacts. Do not invent new types; force every artifact into one of these.

| Artifact | Holds | Location | Lifecycle |
|---|---|---|---|
| **Development log** | Per-task narrative — what was done, why, what broke, how it was resolved. | `docs/dev_log/` | Born archived; immutable after creation. |
| **Lesson** | A pitfall worth never repeating. | `docs/lessons/` | Born active; lifecycle by use-driven validation. |
| **Practice** | A reusable pattern future work should adopt. | `docs/practices/` | Born active; lifecycle by use-driven validation. |
| **Generated index** | A docs-directory-only catalogue of the above. | `docs/INDEX.md` | Generated; regenerated when docs change. |
| **Drift report** | Knowledge whose covered paths moved since last validation. | `docs/lessons/_drift_report.md` | Generated; regenerated when knowledge or code moves. |

A root `LESSONS.md` is the discoverable entry point for lessons and practices. It stays outside the generated docs corpus.

Every non-trivial task **must** produce a development log. A task **should** produce a lesson when a future change made without the knowledge would repeat the same mistake, and a practice when it surfaces a pattern future work should adopt.

## Generated, docs-only index

`docs/INDEX.md` is **generated**, not hand-edited, from the frontmatter of files under `docs/`. It indexes only the documentation corpus: root entry points such as `README.md`, `GOAL.md`, and `LESSONS.md` stay outside it. The index is regenerated and committed whenever the documents it catalogues change, so a reviewer can trust it as a current map rather than a stale one.

## Drift report

`docs/lessons/_drift_report.md` is **generated** from the `applies_to` paths declared in each lesson and practice. It signals knowledge whose covered code or documents have moved since the artifact was last validated. The drift report is an *activity-aware backstop*, not an expiry clock: it surfaces candidates for re-validation; it does not itself deprecate anything. A full governed project runs the drift check with its other verification gates and commits the regenerated report whenever the underlying docs or covered paths change, so drift evidence cannot become an optional stale artifact.

## Stale-knowledge handling

Lithos governs staleness by **use, not by calendar**. There is no periodic sweep and no automatic expiry.

- **Use-driven validation.** When a development log, commit, or pull request cites a specific lesson or practice, the citing change **must** re-validate the cited artifact: confirm it still applies (and record that it was validated), refine it with the new edge case, or mark it deprecated with a reason. Citation is the trigger; an uncited artifact is left untouched rather than churned.
- **Immutability of frozen records.** An artifact marked archived, superseded, or deprecated is a **frozen historical record**. Its body **must not** be rewritten, by human or agent. A factual error in a frozen record is corrected by a new development log plus an update to the living documents — never by editing the frozen text. Frontmatter-only transitions (for example marking one lesson as superseded by another) are permitted and **should** be justified in the change.
- **Supersession over mutation.** When new knowledge replaces old, write a new artifact that points back to what it supersedes, rather than overwriting the original.

## Evidence retention

Knowledge artifacts are **evidence** and are governed by [verification standards](verification-standards.md). A governed project **should** state where development logs, verification results, and [agent run manifests](agent-run-manifest.md) are retained and for how long, so any merged unit can be reconstructed after the fact. Retention records secrets as redacted: sensitive values are never written into a log, lesson, practice, or manifest; use redaction placeholders. The retention horizon is a project decision; the requirement is that it is **stated and recoverable**, not implicit.

## Authority boundaries

Knowledge artifacts record and inform; they do **not** govern. This boundary is normative and must be preserved:

- A development log, lesson, or practice **must not** override the authority chain — `GOAL.md`, the PRD, design documents, the roadmap and current status, or the [local workflow file](local-adoption.md). Where a knowledge artifact and an authority document disagree, the authority document governs and the knowledge artifact is corrected.
- Knowledge artifacts **must not** grant approval, clear an [approval gate](approval-semantics.md), or authorize live, destructive, or external action. They are records and reusable insight, never a sanction.
- Knowledge artifacts **must not** redefine product scope. A lesson may inform how the next change is made; it cannot change what the product is for.

Treating historical logs, lessons, or chat notes as authority is an anti-pattern: it lets superseded thinking quietly outrank the current product truth.

## Relationship to the rest of Lithos

- The spine is part of [governed project structure](governed-project-structure.md); the directory map and preflight order live there.
- Knowledge artifacts are [evidence](verification-standards.md) and may be referenced from an [agent run manifest](agent-run-manifest.md).
- Generated indexes and drift reports are governed verification inputs for [scenario regression](scenario-regression-governance.md) and [release governance](release-and-supply-chain-governance.md); they record what knowledge was current, not what is approved.
- A project declares that it maintains this spine in its [adoption manifest](conformance-and-fixtures.md); the fields are checked for full governed project adoption.
- The artifacts are vendor-neutral and portable across tools; see [tooling interoperability](tooling-interoperability.md).
