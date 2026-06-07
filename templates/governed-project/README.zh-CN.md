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

这些知识作为持久的、可作证据的产物受治理：它记录并启发后续工作，但绝不授予批准，也不凌驾于权威链之上。

## 一致性

`[project-name]` 按单一全生命周期治理模型符合 Lithos `[1.x]`。该声明记录在机器可读采纳清单（`[lithos-adoption-manifest.json]`）中——所声明的版本、治理模型、角色担任者、门禁运作方式、验证证据以及自主 PR 策略。清单是声明而非授权，并保持厂商中立、可移植。

## 发布安全与场景治理

- [`docs/evaluation/scenario-regression.md`](docs/evaluation/scenario-regression.md) 将承载行为的声明固定到具名场景夹具，使回归被机器捕获，而不是被下游消费者发现。
- [`docs/release/release-governance.md`](docs/release/release-governance.md) 治理发布边界：发布须经 owner 批准、携带溯源记录，绝不由 agent 自行执行。
- `tools/static_safety_scan.py` 是一等门禁，拒绝形如密钥的令牌、私有的本机绝对路径以及未完成工作的占位符；它在 `scripts/verify_project.py` 与 CI 中运行。
- [`docs/lessons/_drift_report.md`](docs/lessons/_drift_report.md) 承载知识产物的生成式漂移证据。

## 本地验证

```bash
python tools/build_docs_index.py --check
python tools/docs_drift_signal.py --check
python tools/static_safety_scan.py
python scripts/verify_project.py
git diff --check
```

## 边界

普通开发批准不等于批准实时/默认开启行为、外部交付、发布、生产配置变更、破坏性动作或自主运行。仍需遵守 [`docs/AI_FLOW.md`](docs/AI_FLOW.md) 中的更高审批门禁。Agent 可以开启并更新自己的 Pull Request，但未经 owner 明确批准，绝不自我批准、自我合并、启用无人把关的自动合并或删除分支。
