---
title: "Adopt governed knowledge spine"
status: archived
created_at: 2026-06-05
archived_at: 2026-06-05
---
# Adopt governed knowledge spine

## Task background

The governed Granite example originally demonstrated the product/design/roadmap authority chain, but it did not demonstrate the newer knowledge spine proven by `lithos-example-project`: development logs, lessons, practices, generated docs-only indexes, drift reports, and bilingual README synchronization.

## Changes demonstrated

- Added a root `LESSONS.md` entry point.
- Added `docs/dev_log/`, `docs/lessons/`, and `docs/practices/`.
- Added generated `docs/INDEX.md` and `docs/lessons/_drift_report.md` artifacts.
- Added `tools/build_docs_index.py` and `tools/docs_drift_signal.py`.
- Added `README.zh-CN.md` and kept it aligned with `README.md`.
- Updated PRD, AI flow, AGENTS, roadmap, and PR checklist to mention knowledge-spine expectations.

## Verification

The parent Lithos repository verifies this example through `python scripts/verify_docs.py`, which checks required files, local links, generated docs index freshness, drift report freshness, and multi-language README markers.

## Boundary

This example remains local/offline documentation and template evidence. It does not approve live payment behavior, network calls, release publication, external delivery, or autonomous operation.
