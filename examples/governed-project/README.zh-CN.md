# 示例 — 受治理项目

这是在具有正式评审、多贡献者、分阶段路线图与审计义务的项目中采纳 [Lithos](../../README.zh-CN.md) 的完整示例。

它代表一个假想的支付领域本地库 **Granite**。Granite 面向下游服务维护者，要求任何变更都能被还原为“为何被批准、如何被验证”。

## 这个示例展示什么

- 来自 [`docs/governed-project-structure.md`](../../docs/governed-project-structure.md) 的完整受治理文档脊柱。
- `GOAL.md` 作为稳定产品定位与权威入口。
- `docs/product/prd.md` 中的产品需求与清单。
- `docs/design/architecture.md` 与 `docs/design/technical-solution.md` 中的架构/技术方案分工。
- `docs/roadmap/features.md` 与 `docs/roadmap/current-status.md` 中的功能状态治理。
- `docs/plans/README.md` 中的任务级计划规则。
- `docs/AI_FLOW.md` 中的本地 Lithos 工作流。
- `docs/dev_log/`、`docs/lessons/`、`docs/practices/` 中的知识脊柱。
- `tools/build_docs_index.py` 与 `tools/docs_drift_signal.py` 中的可重复文档生成门禁。
- 与英文 README 保持语义同步的双语入口。

## 文件

- [`README.md`](README.md) — 英文示例入口。
- [`README.zh-CN.md`](README.zh-CN.md) — 中文示例入口。
- [`GOAL.md`](GOAL.md) — 稳定产品目标与权威索引。
- [`docs/AI_FLOW.md`](docs/AI_FLOW.md) — 本地 AI 辅助开发工作流。
- [`AGENTS.md`](AGENTS.md) — agent 面向的协作契约。
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) — PR 证据清单。
- [`docs/INDEX.md`](docs/INDEX.md) — 仅索引 `docs/` 的生成文档索引。
- [`LESSONS.md`](LESSONS.md) — lessons/practices 根入口。
- [`ai-collaborative-development-standards.md`](ai-collaborative-development-standards.md) — 指向 `docs/AI_FLOW.md` 的兼容入口。

## 它如何被采纳

1. 从 [`templates/governed-project/`](../../templates/governed-project/) 开始。
2. 使用 `docs/AI_FLOW.md` 作为操作性本地工作流文件。
3. 加入产品、设计、路线图、计划、开发日志、经验与实践脊柱，使开发任务能从目标追踪到证据。
4. 让 `docs/INDEX.md` 由工具生成，且只索引 `docs/` 目录。
5. 同步 `AGENTS.md`、PR 清单、README 双语入口与验证命令。

对比仅工作流模板 [`templates/governed-ai-flow.md`](../../templates/governed-ai-flow.md) 可以看到为什么更轻的受治理工作流刻意比完整受治理骨架更薄。
