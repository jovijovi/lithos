<div align="center">

<img src="assets/lithos-logo-horizontal.png" alt="Lithos" width="420" />

### 人机协作软件开发标准

*铭刻人类与 AI 共同构建软件的方式。*

[English](README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Русский](README.ru.md) · [Español](README.es.md)

</div>

---

## Lithos 是什么

Lithos 是一套关于**人类与 AI 如何协作开发软件**的开放标准。它定义了角色、审批边界、工作纪律，以及当人与智能体共同构建软件时一个项目应当期望获得的证据——而不绑定任何特定工具、厂商或运行时。

它之所以存在，是因为 AI 辅助开发已成常态，而其"协作规则"往往仍是临时拼凑的。Lithos 让这些规则变得明确、可审阅、可在团队间迁移。

可以从三个层面理解 Lithos：

1. **品牌——Lithos。** 为该标准提供稳定的名称与身份，使项目能够声明"我们遵循 Lithos"并具有确切含义。
2. **正式标准——《人机协作软件开发标准》。** 即 [`docs/`](docs/) 中的规范文档：角色、审批语义、验证、治理。它们以可被引用的方式撰写。
3. **本地落地形态。** 单个仓库实际采纳标准的方式：一个本地工作流文件（文件名由项目自行选择）、一份 `AGENTS.md` 契约、一份 PR 检查清单，以及让标准在日常中可操作的模板与技能。

## Lithos 定义了什么

- **角色**——一组通用角色（所有者、控制者/操作者、架构师、实现智能体、评审者、验证者），并明确各自的权限边界。见 [`docs/roles.md`](docs/roles.md)。
- **审批语义**——为预检/准备、实现、破坏性或外部副作用、以及实时/运行时执行设立各自独立的关卡。见 [`docs/approval-semantics.md`](docs/approval-semantics.md)。
- **工作树与分支纪律**——隔离进行中的工作，使人类与智能体的改动始终可审阅。见 [`docs/core-concepts.md`](docs/core-concepts.md)。
- **验证标准**——证据高于附和：测试、CI、评审、产物、可复现性。见 [`docs/verification-standards.md`](docs/verification-standards.md)。
- **模板**——[`templates/`](templates/) 中可直接复制的本地工作流文件，分为精简版与受治理版。
- **受治理项目结构**——面向成熟仓库的完整文档权威链：`GOAL.md`、PRD、设计、路线图/状态、功能追踪、阶段计划与 `docs/AI_FLOW.md`。见 [`docs/governed-project-structure.md`](docs/governed-project-structure.md)。
- **知识脊柱**——受治理仓库中的开发日志、经验、实践、仅索引 `docs/` 的生成索引与漂移报告：`docs/dev_log/`、`docs/lessons/`、`docs/practices/` 与 `tools/`。
- **双语 README 治理**——当面向用户的声明变化时，源 README 与本地化 README 必须保持语义一致。
- **技能**——[`skills/`](skills/) 中可复用的操作流程，用于创建、审计与适配本地 AI 工作流。
- **示例**——[`examples/`](examples/) 中的落地范例，从单人贡献者到受治理项目。

## 范围——Lithos 不是什么

Lithos 是一套**软件开发协作标准与工具集**，**不是**运行时、智能体框架或执行产品。

采纳 Lithos **并不**授权自主或实时的 AI 执行。其审批语义是*组织层面*的——它们描述人类何时认可了某一类工作，而非授予机器权限。任何实时、破坏性或对外可见的动作，仍需采纳方所定义的明确且即时的审批。见 [`docs/approval-semantics.md`](docs/approval-semantics.md)。

## 快速采纳

1. 阅读 [`docs/philosophy.md`](docs/philosophy.md) 与 [`docs/core-concepts.md`](docs/core-concepts.md)。
2. 决定协作规则的存放位置——自行选择本地工作流文件名（例如 `AI_FLOW.md`、`ai-collaborative-development-standards.md`，或适合你仓库的名称）。见 [`docs/local-adoption.md`](docs/local-adoption.md)。
3. 选择起点：小型项目用 [`templates/minimal-ai-flow.md`](templates/minimal-ai-flow.md)，只需要正式评审工作流的项目用 [`templates/governed-ai-flow.md`](templates/governed-ai-flow.md)，成熟受治理仓库用完整 [`templates/governed-project/`](templates/governed-project/) 文档骨架，其中包含开发日志、经验、实践、生成索引、漂移报告与双语 README 规则。
4. 将 [`templates/AGENTS.md.snippet`](templates/AGENTS.md.snippet) 契约加入你的 `AGENTS.md`。
5. 采纳 [`templates/pr-checklist.md`](templates/pr-checklist.md) 与[验证标准](docs/verification-standards.md)。

完整演练见 [`examples/minimal-project/`](examples/minimal-project/) 与 [`examples/governed-project/`](examples/governed-project/)。

## 仓库结构

```
.
├── README.md                  规范英文首页
├── README.<lang>.md           本地化首页
├── LICENSE                    MIT
├── AGENTS.md                  智能体如何为本仓库做贡献
├── docs/                      正式标准（规范性）
│   ├── philosophy.md
│   ├── core-concepts.md
│   ├── roles.md
│   ├── approval-semantics.md
│   ├── local-adoption.md
│   ├── governed-project-structure.md
│   ├── verification-standards.md
│   └── versioning-and-governance.md
├── skills/                    可复用的操作流程
│   ├── create-local-ai-flow/
│   ├── audit-local-ai-flow/
│   └── adapt-ai-flow-for-governed-project/
├── templates/                 可直接复制的本地采纳文件与受治理项目骨架
├── examples/                  落地范例
└── scripts/                   仓库验证（仅用 Python 标准库）
```

## 治理与版本

Lithos 作为标准而非持续变动的代码库进行版本化与治理。见 [`docs/versioning-and-governance.md`](docs/versioning-and-governance.md) 与 [`AGENTS.md`](AGENTS.md)。

## 许可证

依据 [MIT License](LICENSE) 发布。

Copyright (c) 2026 jovijovi and Lithos Contributors.
