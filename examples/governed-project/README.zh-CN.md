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
- `docs/dev_log/`、`docs/lessons/`、`docs/practices/` 中的知识脊柱——记录并启发后续工作，但绝不凌驾于权威链之上，也不清除审批门禁。
- `tools/build_docs_index.py` 与 `tools/docs_drift_signal.py` 中的可重复文档生成门禁。
- 适合写入机器可读采纳清单的 Lithos 一致性声明（版本与深度），保持厂商中立、跨工具可移植。
- 自主 PR 策略：agent 可以开启并更新 Pull Request，但未经 owner 明确批准，绝不自我批准、自我合并、启用无人把关的自动合并、删除分支、发布或执行实时/外部动作。
- 真正可在本目录运行的可复现验证门禁：内置本地验证器 `scripts/verify_project.py`、文档索引检查 `tools/build_docs_index.py`、活动感知的漂移信号 `tools/docs_drift_signal.py`，以及一等静态安全扫描 `tools/static_safety_scan.py`。
- 静态安全作为一等门禁：`tools/static_safety_scan.py` 拒绝形如密钥的令牌、私有的本机绝对路径以及未完成工作的占位符，并在 `scripts/verify_project.py` 内部运行。
- 场景回归与发布治理：`docs/evaluation/scenario-regression.md` 将承载行为的声明固定到具名夹具，`docs/release/release-governance.md` 让发布须经 owner 批准、携带溯源记录，绝不由 agent 自行执行。
- 由 `tools/docs_drift_signal.py` 生成的知识漂移证据，记录在 `docs/lessons/_drift_report.md`。
- 与英文 README 保持语义同步的双语入口。

## 验证门禁

以下门禁可在本示例目录直接运行，也是 agent 或贡献者在开启 PR 前所运行的命令：

```bash
python scripts/verify_project.py
python tools/build_docs_index.py --check
python tools/docs_drift_signal.py --check
python tools/static_safety_scan.py
git diff --check
```

`scripts/verify_project.py` 是唯一的本地验证器入口：它先检查受治理文档脊柱与门禁词汇，再运行文档索引检查、漂移自检与检查，以及静态安全扫描。仓库根验证（`scripts/verify_docs.py`）也会调用它，使示例自声明的门禁保持真实可信。

Granite 处于 R0 文档权威基线阶段，因此尚未附带产品测试套件。一旦开始产品实现，`docs/evaluation/scenario-regression.md` 中的行为测试与场景夹具即成为必需门禁；验证块绝不声明尚不存在的行为门禁。

## 文件

- [`README.md`](README.md) — 英文示例入口。
- [`README.zh-CN.md`](README.zh-CN.md) — 中文示例入口。
- [`GOAL.md`](GOAL.md) — 稳定产品目标与权威索引。
- [`docs/AI_FLOW.md`](docs/AI_FLOW.md) — 本地 AI 辅助开发工作流。
- [`AGENTS.md`](AGENTS.md) — agent 面向的协作契约。
- [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md) — PR 证据清单。
- [`docs/INDEX.md`](docs/INDEX.md) — 仅索引 `docs/` 的生成文档索引。
- [`scripts/verify_project.py`](scripts/verify_project.py) — 内置本地验证器门禁。
- [`LESSONS.md`](LESSONS.md) — lessons/practices 根入口。
- [`ai-collaborative-development-standards.md`](ai-collaborative-development-standards.md) — 指向 `docs/AI_FLOW.md` 的兼容入口。

## 它如何被采纳

1. 从 [`templates/governed-project/`](../../templates/governed-project/) 开始。
2. 使用 `docs/AI_FLOW.md` 作为操作性本地工作流文件。
3. 加入产品、设计、路线图、计划、开发日志、经验与实践脊柱，使开发任务能从目标追踪到证据。
4. 让 `docs/INDEX.md` 由工具生成，且只索引 `docs/` 目录。
5. 同步 `AGENTS.md`、PR 清单、README 双语入口与验证命令。

对比仅工作流模板 [`templates/governed-ai-flow.md`](../../templates/governed-ai-flow.md) 可以看到为什么更轻的受治理工作流刻意比完整受治理骨架更薄。
