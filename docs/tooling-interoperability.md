# Tooling Interoperability

Lithos is adopted by teams using different agents, editors, CI systems, and review tools. For the standard to be portable, the **artifacts that carry collaboration state must be vendor-neutral** — so one tool can produce a record another tool can read, and a project can change tools without losing its governance. This document defines those portable artifact boundaries and the neutrality rules they obey.

## Why portable artifacts

Collaboration state — who holds which role, which gate was cleared, where a run could execute, what evidence proved the work, what conformance is claimed — must outlive any single tool. If that state lives only inside a vendor's product, it cannot be reviewed by an independent party, handed to a different agent, or audited after the tool is gone. Lithos keeps the state in **plain, self-describing files** instead.

## The portable artifact set

Each artifact has one boundary. Together they let agents and tools exchange roles, approvals, environment boundaries, run manifests, reviews, verification evidence, and conformance claims.

| Artifact | Carries | Owns | Must not own |
|---|---|---|---|
| [Local workflow file](local-adoption.md) | How this project operates the standard. | Role assignments, gate signalling, isolation and verification rules. | Per-run state or product authority. |
| [Adoption manifest](conformance-and-fixtures.md) | The conformance claim. | Version, depth, roles, gate operation, autonomous PR policy, knowledge fields. | Approval grants; secret values. |
| [Environment policy](environment-and-sandbox-policy.md) | Where a run may execute and what it may touch. | Filesystem, network, credential, and side-effect limits. | Capability grants or live/runtime authorization. |
| [Agent run manifest](agent-run-manifest.md) | What one run was authorized to do and did. | Approval reference, claimed vs actual, evidence, boundary, redaction, retention. | Approval itself; product authority. |
| [PR checklist](local-adoption.md) | The per-unit review and evidence gate. | Review items, evidence capture, documents that change together. | Long-form design or roadmap content. |
| [Knowledge artifacts](knowledge-governance.md) | Durable reasoning and reusable insight. | Development logs, lessons, practices, generated index and drift report. | Product authority or approval. |

## Neutrality rules

These rules are normative for any artifact a project commits as part of its Lithos adoption:

- **No vendor, product, or private-system names.** Refer to roles and capabilities generically — "the implementation agent," "the CI system," "the reviewer" — not by the brand of the tool that fills the role. A committed artifact **must not** name a specific vendor, product, private profile, or internal system.
- **Self-describing values.** Where a field has a closed set of allowed values, the artifact **should** carry that set with the data (for example, an `allowed_*` list beside the chosen value), so a different tool can validate the record without the originating tool's documentation.
- **Plain, parseable formats.** Portable artifacts are plain text — JSON or Markdown — parseable with a standard library and no third-party dependency. A consuming tool **must not** need a vendor SDK to read them.
- **No secrets in artifacts.** Secrets, tokens, credentials, and private identifiers are never written into a portable artifact; they are redacted with placeholders. Interoperability **must not** become a channel for leaking sensitive values.
- **Records, not authorizations.** A portable artifact records or declares; it never grants. Exchanging an artifact between tools transfers information, not permission: it clears no [gate](approval-semantics.md) and authorizes no live, destructive, or external action.

## Exchanging roles across tools

Because role assignment lives in the local workflow file and the adoption manifest rather than in a tool, one agent can hand a role to another by reference. What may **not** be handed across tools is approval authority: it remains with the human [owner](roles.md) regardless of which tool an agent runs in. A tool that "accepts" an approval on the owner's behalf has not cleared the gate.

## Relationship to the rest of Lithos

- The artifact boundaries refine [governed project structure](governed-project-structure.md), which lists where each file lives.
- The neutrality rules mirror the repository's own contribution rules in [`AGENTS.md`](../AGENTS.md): keep all content tool- and vendor-neutral.
- Conformance can be declared and checked across tools using the [adoption manifest and fixtures](conformance-and-fixtures.md).
