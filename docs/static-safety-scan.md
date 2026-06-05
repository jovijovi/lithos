# Static Safety Scan

A static safety scan is a **deterministic, machine-runnable check over committed text** that rejects values which must never enter a governed repository: secret-shaped tokens, private machine-local paths, and unfinished-work placeholders. Lithos treats it as a **first-class governance gate**, not an optional lint: it runs locally and in continuous integration, and a change is not done until it passes.

The scan exists because the most damaging governance failures are not subtle design errors — they are a leaked credential, a hard-coded home directory, or a placeholder that shipped as if it were real. These are mechanically detectable, so Lithos requires that they be detected mechanically rather than left to reviewer attention.

## What it is, and is not

A static safety scan is **static** (it reads text; it never executes the project), **deterministic** (the same input yields the same verdict), and **reproducible** (anyone can re-run it and see the same result). It is therefore [verification evidence](verification-standards.md): a green run is proof a third party can regenerate, not testimony.

It is **not** a substitute for review, testing, or approval. It catches a fixed, well-understood class of mistakes; it does not judge whether the change is correct, in scope, or approved. Passing the scan clears no [approval gate](approval-semantics.md).

## What the scan must reject

A conforming static safety scan **must** reject, at minimum:

- **Secret-shaped tokens.** Credential, API-key, access-token, and private-key material — recognized by shape, not by knowing the specific secret. Detection is heuristic and errs toward flagging; a real value is redacted with a placeholder such as `[REDACTED]`, never committed.
- **Private machine-local paths.** Absolute paths rooted in a per-user home directory or another contributor's environment, which leak where a run happened and break portability. Committed text uses repository-relative paths.
- **Unfinished-work placeholders.** Markers that text is not yet real — leftover task markers and filler placeholder prose. Their presence means the change was not finished before it was offered as done.

A project **may** extend the scan with stricter project-specific rules — additional token shapes, banned internal identifiers, or dangerous-call patterns — but **must not** drop the three classes above and still claim the gate is satisfied.

## How the scanner itself must behave

Because the scanner's own source is committed text that the scan reads, two rules keep it honest:

- **No self-match.** The scanner **must** assemble every sensitive needle from split fragments (for example, by concatenation) so its own pattern definitions do not match themselves. A scanner that flags its own source is either broken or forces contributors to disable it — both defeat the gate.
- **Self-test on dynamic probes.** The scanner **should** verify its own engine before scanning: construct known-bad values *at runtime* — never as stored literals — confirm the engine flags them, and confirm it clears a known-clean value. This turns a passing scan into evidence the engine works, rather than evidence it matched nothing because it was misconfigured. Probes are built dynamically precisely so the repository text never contains a raw credential-shaped value.

The scanner is **pure-standard-library and dependency-free**, so any contributor or tool can run it without installing anything, consistent with the portability rules in [tooling interoperability](tooling-interoperability.md).

## Where it runs

The static safety scan is part of the project's definition of done, alongside the other [verification](verification-standards.md) gates:

- **Locally**, before a change is offered for review — a contributor runs it and reports the result.
- **In continuous integration**, as a required check on the proposed change, so the gate cannot be skipped by forgetting to run it.

A run that is reported but not actually executed is not evidence; the [honesty obligations](verification-standards.md) apply to this gate as to any other.

## Relationship to the rest of Lithos

- The scan produces [verification evidence](verification-standards.md) and is one of the reproducible checks a unit carries.
- It enforces, mechanically, the no-secrets rule that [knowledge governance](knowledge-governance.md) and [tooling interoperability](tooling-interoperability.md) state for every committed artifact.
- It protects the [environment and sandbox policy](environment-and-sandbox-policy.md): a leaked credential or machine-local path is a boundary violation made visible in the diff.
- Like every other gate, it records and proves; it grants nothing. Passing the scan does not authorize a merge, a release, or any live or external action — those remain with the human [owner](roles.md) under the [autonomous PR policy](autonomous-pr-policy.md).
