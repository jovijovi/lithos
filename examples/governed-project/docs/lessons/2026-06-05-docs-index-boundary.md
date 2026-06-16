---
title: "Keep the generated docs index inside docs"
status: active
created_at: 2026-06-05
last_validated_at: 2026-06-16T06:55:25Z
description: "A governed project should keep root entry points and generated docs-directory indexes separate."
dev_log: docs/dev_log/2026-06-05-governance-spine-adoption.md
tags: [governance, documentation, lithos]
applies_to:
  - GOAL.md
  - README.md
  - README.zh-CN.md
  - LESSONS.md
  - docs/INDEX.md
  - tools/build_docs_index.py
---
# Keep the generated docs index inside docs

## Lesson

A generated documentation index should not become a second project homepage. Root entry points such as `README.md`, `README.zh-CN.md`, `GOAL.md`, and `LESSONS.md` should stay outside `docs/INDEX.md`.

## What to do

- Generate `docs/INDEX.md` only from `docs/**/*.md` files with frontmatter.
- Exclude generated reports such as `docs/lessons/_drift_report.md`.
- Keep root entry points linked from README/GOAL instead of listing them in the generated docs corpus.
- Make verification fail if `docs/INDEX.md` links root files.

## See also

- Dev log: [Adopt governed knowledge spine](../dev_log/2026-06-05-governance-spine-adoption.md)
- Practice: [Governed project knowledge spine](../practices/2026-06-05-governed-project-knowledge-spine.md)
