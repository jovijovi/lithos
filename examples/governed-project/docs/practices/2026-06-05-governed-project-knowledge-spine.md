---
title: "Governed project knowledge spine"
status: active
created_at: 2026-06-05
last_validated_at: 2026-06-06T03:29:48Z
description: "A mature governed Lithos project should capture dev logs, lessons, practices, docs-only indexes, drift reports, and bilingual README synchronization."
dev_log: docs/dev_log/2026-06-05-governance-spine-adoption.md
tags: [governance, documentation, lithos]
applies_to:
  - AGENTS.md
  - README.md
  - README.zh-CN.md
  - docs/AI_FLOW.md
  - docs/INDEX.md
  - docs/product/prd.md
  - docs/roadmap/current-status.md
  - docs/roadmap/features.md
  - tools/build_docs_index.py
  - tools/docs_drift_signal.py
---
# Governed project knowledge spine

## When to apply

Apply this practice when a project adopts the full governed Lithos structure rather than only a local workflow file.

## Practice

1. Keep the authority chain explicit: `GOAL.md`, PRD, design docs, roadmap/features, current-status, plans, and code.
2. Add a knowledge spine: `docs/dev_log/`, `docs/lessons/`, `docs/practices/`, and root `LESSONS.md`.
3. Generate `docs/INDEX.md` from docs-directory frontmatter only.
4. Generate `docs/lessons/_drift_report.md` from lesson/practice `applies_to` paths.
5. Keep `README.md` and localized README files semantically aligned.
6. Make local verification and CI check the generated docs artifacts.

## Evidence

This Granite example carries the required files and is checked by the parent Lithos repository verifier.
