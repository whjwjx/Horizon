---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 35 条内容中筛选出 4 条重要资讯。

---

1. [Zer0Fit：为谷歌 TabFM 和 TimesFM 打造的 MCP 服务器](#item-1) ⭐️ 8.0/10
2. [Claude Code 与 OpenCode 的 Token 开销对比](#item-2) ⭐️ 7.0/10
3. [CISA 在真实事件中临时构建事件响应手册](#item-3) ⭐️ 7.0/10
4. [苹果失败的汽车项目催生了强大的 AI 芯片](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Zer0Fit：为谷歌 TabFM 和 TimesFM 打造的 MCP 服务器](https://www.reddit.com/r/MachineLearning/comments/1uue8cc/zer0fit_i_took_googles_new_tabfm_timesfm_ml/) ⭐️ 8.0/10

一名研究生创建了 Zer0Fit，这是一个 MCP 服务器，封装了谷歌新发布的 TabFM 和 TimesFM 基础模型，支持从聊天界面进行零样本预测、分类和回归。该服务器在 Docker 容器中本地运行，需要 16GB 显存。 该项目通过简单的聊天界面让非专家也能使用前沿的零样本机器学习模型，降低了在表格和时间序列任务中使用基础模型的门槛。它展示了 MCP 如何连接大语言模型和传统机器学习模型。 Zer0Fit 在鸢尾花数据集上达到 94.7%的准确率，在加州房价回归任务上 R²为 0.91，且无需任何微调。它支持 CSV 输入（即将支持 XLS、XLSX、JSON、JSONL），并采用 5 分钟 TTL 动态加载/卸载模型以释放显存。

reddit · r/MachineLearning · /u/Porespellar · 7月12日 12:32

**背景**: TabFM 和 TimesFM 是谷歌研究团队分别针对表格数据和时间序列预测推出的基础模型。它们支持零样本推理，即无需针对特定任务进行训练即可对新数据集进行预测。MCP（模型上下文协议）是一种将 AI 模型连接到工具和数据源的标准，常与 Open WebUI 或 Claude Code 中的大语言模型配合使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/">Introducing TabFM : A zero-shot foundation model for tabular data</a></li>
<li><a href="https://github.com/google-research/timesfm">google-research/ timesfm : TimesFM ( Time Series Foundation Model )...</a></li>
<li><a href="https://machinelearningmastery.com/building-a-simple-mcp-server-in-python/">Building a Simple MCP Server in Python - Machine Learning Mastery</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#foundation models`, `#MCP server`, `#zero-shot`, `#time series`

---

<a id="item-2"></a>
## [Claude Code 与 OpenCode 的 Token 开销对比](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 7.0/10

一项实证研究发现，Claude Code 在读取用户提示前会发送约 33,000 个 token，而 OpenCode 仅发送约 7,000 个 token，揭示了 Claude Code 在缓存策略和框架开销上存在显著的 token 低效问题。 这种 token 浪费直接增加了 Claude Code 用户的成本，尤其是在处理大型或复杂任务时，并引发了关于 AI 编程代理提供商经济激励的质疑。 该研究记录了编码工具与 Anthropic 端点之间的所有请求，捕获了使用块以进行比较。作者指出，子代理和工具调用开销进一步放大了 token 消耗。

hackernews · systima · 7月12日 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**背景**: 像 Claude Code 和 OpenCode 这样的 AI 编程代理使用大型语言模型来辅助软件开发任务。它们每次请求都会发送系统提示、工具定义和对话历史，这导致了 token 开销。在生产环境中，高效的 token 使用对于成本管理至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/drona23/claude-token-efficient">GitHub - drona23/claude-token-efficient: One CLAUDE.md file. Keeps Claude responses terse. Reduces output verbosity on heavy workflows. Drop-in, no code changes. · GitHub</a></li>
<li><a href="https://buildtolaunch.substack.com/p/claude-code-token-optimization">Claude Code Token Optimization: 19 Changes to Cut Costs (2026)</a></li>
<li><a href="https://www.firecrawl.dev/blog/claude-code-token-efficiency">12 Ways to Cut Token Consumption in Claude Code</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，子代理是 token 消耗的主要来源，有用户报告单个任务启动了 7 个子代理。其他人怀疑 Anthropic 的商业模式激励了更高的 token 使用量，并指出提示简洁性并非唯一因素——工具质量和往返次数也很重要。

**标签**: `#AI coding agents`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#software engineering`

---

<a id="item-3"></a>
## [CISA 在真实事件中临时构建事件响应手册](https://techcrunch.com/2026/07/10/us-cyber-agency-cisa-had-to-build-its-incident-playbook-during-the-incident-agency-reveals/) ⭐️ 7.0/10

CISA 透露，在应对一起涉及承包商 GitHub 仓库中密码泄露的真实事件时，它不得不临时构建事件响应手册，该事件由网络安全记者 Brian Krebs 报道。 这凸显了领先网络安全机构在准备方面的重大缺口，引发了对政府网络安全实践以及联邦机构事件响应有效性的担忧。 该事件由 GitGuardian 的安全研究员发现，他提醒 Krebs 注意 CISA 承包商的一个公开 GitHub 仓库中存在泄露的密码。CISA 承认缺乏现成的手册，不得不在响应过程中创建一份。

rss · TechCrunch · 7月11日 01:01

**背景**: CISA 是美国负责网络安全和基础设施安全的联邦机构。事件响应手册是指导组织检测、响应和恢复网络安全事件的标准化程序。第 14028 号行政令指示 CISA 为联邦民事机构制定此类手册，但此次事件表明内部仍存在缺口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks">Federal Government Cybersecurity Incident and Vulnerability Response Playbooks | CISA</a></li>
<li><a href="https://www.cisa.gov/sites/default/files/2024-08/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf">TLP:CLEAR Cybersecurity Incident & Vulnerability Response Playbooks</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#CISA`, `#incident response`, `#government`, `#data breach`

---

<a id="item-4"></a>
## [苹果失败的汽车项目催生了强大的 AI 芯片](https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra) ⭐️ 7.0/10

苹果放弃的自动驾驶汽车项目间接推动了强大 AI 芯片（如 M7 和 M8）的开发，这些芯片现在用于其设备。汽车项目对设备端 AI 处理的需求推动了芯片创新，后来惠及了苹果更广泛的产品线。 这揭示了苹果失败的汽车项目对其芯片开发产生的重大、此前未被充分认识的影响，对 AI 硬件具有启示意义。它表明，即使主要目标被放弃，雄心勃勃的项目也能产生有价值的衍生技术。 汽车处理器从未完成，但为自动驾驶设计的神经处理单元（NPU）被重新用于苹果的 M 系列芯片。报道指出，未来的 M7 和 M8 芯片将更加注重 AI 支持，而非原始速度或能效。

rss · The Verge · 7月12日 16:27

**背景**: 苹果的自动驾驶汽车项目（代号 Project Titan）在 2024 年 2 月被取消，此前已开发多年。在项目期间，苹果意识到需要强大的设备端 AI 处理能力来应对自动驾驶任务，这推动了先进神经引擎的开发。这些神经引擎后来成为苹果 M 系列芯片的关键组件，实现了 Apple Intelligence 等设备端 AI 功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_car_project">Apple car project - Wikipedia</a></li>
<li><a href="https://www.macrumors.com/roundup/apple-car/">Apple Car: Apple Car: Now Canceled, What we know</a></li>
<li><a href="https://appleinsider.com/articles/26/07/12/power-of-apples-m7-m8-chips-was-born-from-apple-car-research">Power of Apple's M7 & M8 chips was born from Apple Car research</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI chips`, `#self-driving cars`, `#hardware`

---