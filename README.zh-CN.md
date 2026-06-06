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
- **环境与沙箱策略**——运行可以在何处执行、可以触及什么（文件系统、网络、凭据、副作用），并与审批保持区分。见 [`docs/environment-and-sandbox-policy.md`](docs/environment-and-sandbox-policy.md)。
- **工作树与分支纪律**——隔离进行中的工作，使人类与智能体的改动始终可审阅。见 [`docs/core-concepts.md`](docs/core-concepts.md)。
- **验证标准**——证据高于附和：测试、CI、评审、产物、可复现性。见 [`docs/verification-standards.md`](docs/verification-standards.md)。
- **智能体运行清单**——逐次运行的审计记录：被授权做什么、实际运行了什么，以及涉及的证据与边界；它是记录，而非授权。见 [`docs/agent-run-manifest.md`](docs/agent-run-manifest.md)。
- **模板**——[`templates/`](templates/) 中可直接复制的本地工作流文件，分为仅工作流采纳版与完整受治理版。
- **受治理项目结构**——面向成熟仓库的完整文档权威链：`GOAL.md`、PRD、设计、路线图/状态、功能追踪、阶段计划与 `docs/AI_FLOW.md`。见 [`docs/governed-project-structure.md`](docs/governed-project-structure.md)。
- **知识脊柱**——受治理仓库中的开发日志、经验、实践、仅索引 `docs/` 的生成索引与漂移报告：`docs/dev_log/`、`docs/lessons/`、`docs/practices/` 与 `tools/`。这些知识如何存续、按使用过期，并始终从属于权威链，定义于 [`docs/knowledge-governance.md`](docs/knowledge-governance.md)。
- **一致性与采纳清单**——项目可以声明什么，以机器可读的采纳清单声明（[`schemas/lithos-adoption-manifest.schema.json`](schemas/lithos-adoption-manifest.schema.json)，从 [`templates/lithos-adoption-manifest.json`](templates/lithos-adoption-manifest.json) 填写），并以[一致性夹具](fixtures/conformance/)展示什么应通过、什么必须失败。见 [`docs/conformance-and-fixtures.md`](docs/conformance-and-fixtures.md)。
- **自主 PR 策略**——智能体可以自行对 PR 做什么，以及绝不可自我批准或自我合并的边界。见 [`docs/autonomous-pr-policy.md`](docs/autonomous-pr-policy.md)。
- **静态安全扫描**——在评审或发布前，用确定性关卡拒绝形似密钥的值、私有本机路径与未完成占位文本。见 [`docs/static-safety-scan.md`](docs/static-safety-scan.md)。
- **场景回归治理**——用命名夹具固定有行为含义的声明与示例，使回归被机器捕获。见 [`docs/scenario-regression-governance.md`](docs/scenario-regression-governance.md)。
- **发布与供应链治理**——为发布产物设立所有者审批、来源记录与供应链边界。见 [`docs/release-and-supply-chain-governance.md`](docs/release-and-supply-chain-governance.md)。
- **工具互操作性**——承载协作状态的产物保持厂商中立且可移植，使项目可以更换工具而不丢失治理。见 [`docs/tooling-interoperability.md`](docs/tooling-interoperability.md)。
- **双语 README 治理**——当面向用户的声明变化时，源 README 与本地化 README 必须保持语义一致。
- **技能**——[`skills/`](skills/) 中可复用的操作流程：唯一的 [`lithos`](skills/lithos/SKILL.md) 伞式技能将智能体路由到对项目的采纳、审计、升级、评审或发布门禁，并在 [`skills/lithos/references/`](skills/lithos/references/) 下为每个意图提供一份流程。
- **示例**——[`examples/`](examples/) 中的受治理项目落地范例。

## 范围——Lithos 不是什么

Lithos 是一套**软件开发协作标准与工具集**，**不是**运行时、智能体框架或执行产品。

采纳 Lithos **并不**授权自主或实时的 AI 执行。其审批语义是*组织层面*的——它们描述人类何时认可了某一类工作，而非授予机器权限。任何实时、破坏性或对外可见的动作，仍需采纳方所定义的明确且即时的审批。见 [`docs/approval-semantics.md`](docs/approval-semantics.md)。

## 快速采纳

1. 阅读 [`docs/philosophy.md`](docs/philosophy.md) 与 [`docs/core-concepts.md`](docs/core-concepts.md)。
2. 决定协作规则的存放位置——自行选择本地工作流文件名（例如 `AI_FLOW.md`、`ai-collaborative-development-standards.md`，或适合你仓库的名称）。见 [`docs/local-adoption.md`](docs/local-adoption.md)。
3. 选择起点：只需要正式评审工作流的项目用 [`templates/governed-ai-flow.md`](templates/governed-ai-flow.md)，成熟受治理仓库用完整 [`templates/governed-project/`](templates/governed-project/) 文档骨架，其中包含开发日志、经验、实践、生成索引、漂移报告与双语 README 规则。
4. 将 [`templates/AGENTS.md.snippet`](templates/AGENTS.md.snippet) 契约加入你的 `AGENTS.md`。
5. 采纳 [`templates/pr-checklist.md`](templates/pr-checklist.md) 与[验证标准](docs/verification-standards.md)，并在[采纳清单](templates/lithos-adoption-manifest.json)中声明你所遵循的内容。

完整演练见 [`examples/governed-project/`](examples/governed-project/)。

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
│   ├── environment-and-sandbox-policy.md
│   ├── local-adoption.md
│   ├── governed-project-structure.md
│   ├── verification-standards.md
│   ├── agent-run-manifest.md
│   ├── knowledge-governance.md
│   ├── conformance-and-fixtures.md
│   ├── tooling-interoperability.md
│   ├── autonomous-pr-policy.md
│   ├── static-safety-scan.md
│   ├── scenario-regression-governance.md
│   ├── release-and-supply-chain-governance.md
│   └── versioning-and-governance.md
├── schemas/                   机器可读的采纳清单模式
├── skills/                    可复用的操作流程
│   └── lithos/                唯一伞式技能：路由 采纳/审计/升级/评审/发布
│       └── references/        每个意图一份流程：采纳、审计、治理升级、版本升级、PR 评审、发布门禁
├── templates/                 可直接复制的本地采纳文件与受治理项目骨架
├── fixtures/                  一致性夹具（通过与拒绝）
├── examples/                  落地范例
└── scripts/                   仓库验证（仅用 Python 标准库）
```

## 治理与版本

Lithos 作为标准而非持续变动的代码库进行版本化与治理。见 [`docs/versioning-and-governance.md`](docs/versioning-and-governance.md) 与 [`AGENTS.md`](AGENTS.md)。

## 许可证

依据 [MIT License](LICENSE) 发布。

Copyright (c) 2026 jovijovi and Lithos Contributors.
