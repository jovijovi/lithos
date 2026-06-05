# [项目名称]

[一句话说明产品定位。]

语言：[English](README.md) · [中文](README.zh-CN.md)

## 这个项目是什么

`[project-name]` 是一个受 Lithos 治理的项目。产品真相属于文档权威链，而不是聊天记录或孤立计划。

## 权威链

按顺序阅读：

1. [`GOAL.md`](GOAL.md)
2. [`docs/product/prd.md`](docs/product/prd.md)
3. [`docs/design/architecture.md`](docs/design/architecture.md)
4. [`docs/design/technical-solution.md`](docs/design/technical-solution.md)
5. [`docs/roadmap/features.md`](docs/roadmap/features.md)
6. [`docs/roadmap/current-status.md`](docs/roadmap/current-status.md)
7. [`docs/AI_FLOW.md`](docs/AI_FLOW.md)
8. [`docs/INDEX.md`](docs/INDEX.md)

## 知识脊柱

- [`docs/dev_log/`](docs/dev_log/README.md) 记录任务证据与决策。
- [`docs/lessons/`](docs/lessons/README.md) 记录可复用经验。
- [`docs/practices/`](docs/practices/README.md) 记录可复用实践。
- [`LESSONS.md`](LESSONS.md) 是 lessons 与 practices 的根入口。
- [`docs/lessons/_drift_report.md`](docs/lessons/_drift_report.md) 由 `tools/docs_drift_signal.py` 生成。

## 本地验证

```bash
python tools/build_docs_index.py --check
python tools/docs_drift_signal.py --check
python scripts/verify_project.py
git diff --check
```

## 边界

普通开发批准不等于批准实时/默认开启行为、外部交付、发布、生产配置变更、破坏性动作或自主运行。仍需遵守 [`docs/AI_FLOW.md`](docs/AI_FLOW.md) 中的更高审批门禁。
