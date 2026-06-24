---
layout: default
title: "Horizon Summary: 2026-06-24 (ZH)"
date: 2026-06-24
lang: zh
---

> 从 76 条内容中筛选出 15 条重要资讯。

---

1. [GPT-5 助力解决三年免疫学谜题](#item-1) ⭐️ 8.0/10
2. [OpenAI 推出 Daybreak 安全工具](#item-2) ⭐️ 8.0/10
3. [LLM 在角色混淆中优先考虑风格而非内容](#item-3) ⭐️ 8.0/10
4. [Moebius 0.2B 图像修复模型通过 WebGPU 移植到浏览器](#item-4) ⭐️ 8.0/10
5. [2026 年科技裁员：AI 被列为主要原因](#item-5) ⭐️ 8.0/10
6. [微软与雪佛龙计划建设大型燃气数据中心](#item-6) ⭐️ 8.0/10
7. [TikZ 编辑器：所见即所得与源码同步的 LaTeX 绘图工具](#item-7) ⭐️ 7.0/10
8. [OpenAI 加入 Appia 基金会推动 AI 标准建设](#item-8) ⭐️ 7.0/10
9. [Datasette 1.0a35 新增创建/修改表界面](#item-9) ⭐️ 7.0/10
10. [Superhuman 收购 AI 检测初创公司 GPTZero](#item-10) ⭐️ 7.0/10
11. [Anthropic 推出 Claude Tag，在 Slack 中学习公司知识](#item-11) ⭐️ 7.0/10
12. [LastPass 因 Klue 漏洞泄露客户支持数据](#item-12) ⭐️ 7.0/10
13. [AI 世界因持续运行的智能体群而变得“循环”](#item-13) ⭐️ 7.0/10
14. [Groq 在英伟达交易后融资 6.5 亿美元，转向新云业务](#item-14) ⭐️ 7.0/10
15. [ML 团队在生产中跳过对抗性测试](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GPT-5 助力解决三年免疫学谜题](https://openai.com/index/gpt-5-immunology-mystery) ⭐️ 8.0/10

OpenAI 于 2025 年 8 月 7 日发布的多模态大语言模型 GPT-5 Pro，帮助免疫学家 Derya Unutmaz 解决了一个关于 T 细胞行为的三年未解之谜，为免疫调控提供了新见解。 这一突破展示了先进 AI 在加速生物医学发现方面的具体潜力，对癌症免疫疗法和自身免疫疾病研究具有重要意义。 GPT-5 Pro 可通过 ChatGPT 和 Microsoft Copilot 公开访问，开发者也可通过 OpenAI API 使用。具体的 T 细胞谜题涉及理解 T 细胞如何调控自身行为，这可能带来新的治疗靶点。

rss · OpenAI Blog · 6月23日 17:00

**背景**: T 细胞是一种对适应性免疫至关重要的白细胞。它们通过 T 细胞受体（TCR）识别抗原并被激活以对抗感染或癌症。T 细胞行为失调可能导致自身免疫疾病或免疫反应受损。GPT-5 是 OpenAI 生成式预训练 Transformer 模型的最新版本，具备多模态推理和复杂分析能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5_Pro">GPT-5 Pro</a></li>
<li><a href="https://www.immunology.org/public-information/bitesized-immunology/systems-processes/t-cell-activation">T-cell activation | British Society for Immunology</a></li>

</ul>
</details>

**标签**: `#GPT-5`, `#immunology`, `#AI in science`, `#biomedical research`, `#T cells`

---

<a id="item-2"></a>
## [OpenAI 推出 Daybreak 安全工具](https://openai.com/index/daybreak-securing-the-world) ⭐️ 8.0/10

OpenAI 推出了 Daybreak 工具，包括 Codex Security 和 GPT-5.5-Cyber，用于大规模自动化漏洞发现、验证和修复。 这标志着 AI 驱动的网络安全领域取得重大进展，使组织能够以前所未有的速度和规模主动保护其系统。 Codex Security 逐个提交扫描 GitHub 仓库并在隔离环境中验证问题，而 GPT-5.5-Cyber 专为高级防御性网络工作流设计，已通过多步骤攻击模拟测试。

rss · OpenAI Blog · 6月22日 10:00

**背景**: OpenAI 的 Daybreak 计划旨在帮助防御者跟上不断加速的威胁形势。Codex Security 是一个 AI 驱动的应用安全代理，可构建项目特定的上下文和威胁模型。GPT-5.5-Cyber 是专为授权防御性网络安全任务设计的专用模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/daybreak-securing-the-world/">Daybreak: Tools for securing every organization in the world</a></li>
<li><a href="https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/">Scaling Trusted Access for Cyber with GPT-5.5 and GPT-5.5-Cyber | OpenAI</a></li>
<li><a href="https://developers.openai.com/codex/security">Security – Codex | OpenAI Developers</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Vulnerability Management`, `#OpenAI`, `#Codex`, `#Cybersecurity`

---

<a id="item-3"></a>
## [LLM 在角色混淆中优先考虑风格而非内容](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything) ⭐️ 8.0/10

Charles Ye、Jasmine Cui 和 Dylan Hadfield-Menell 的研究表明，LLM 无法可靠地区分系统/助手文本与用户输入，实际上更优先考虑文本的风格而非内容，从而实现了严重的越狱攻击。 这证实了 LLM 在区分特权文本与不可信文本方面的根本局限性，表明除非模型实现真正的角色感知，否则提示注入防御将永远是一场打地鼠游戏。 研究人员发现，“去风格化”——以略微不同的方式重写文本——将攻击成功率从 61% 降至 10%，尽管对人类读者来说含义保持不变。像 gpt-oss-20b 这样的模型会被模仿内部思考块风格的文本所欺骗。

rss · Simon Willison · 6月22日 23:59

**背景**: 提示注入是一种网络安全攻击，攻击者通过精心构造输入来操纵 LLM 的行为，通常绕过系统提示。LLM 将系统提示和用户输入都视为自然语言字符串，因此很难强制执行边界。角色混淆指的是模型无法正确感知自身角色与用户角色。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://role-confusion.github.io/">Prompt Injection as Role Confusion</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论可能强调了这项研究的重要性，一些评论者指出这些发现与提示注入的实际经验相符。其他人可能讨论架构变更或更好的训练是否能解决这个问题。

**标签**: `#prompt injection`, `#LLM security`, `#jailbreak`, `#AI safety`

---

<a id="item-4"></a>
## [Moebius 0.2B 图像修复模型通过 WebGPU 移植到浏览器](https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything) ⭐️ 8.0/10

Simon Willison 成功将 Moebius 0.2B 图像修复模型移植到浏览器中，完全通过 WebGPU 运行，演示地址为 simonw.github.io/moebius-web/。此次移植使用了 Claude Code 和基于 WebGPU 后端的 ONNX Runtime Web。 这使得任何拥有现代浏览器的用户都能使用先进的图像修复功能，无需 NVIDIA CUDA 或专用 GPU 硬件。这证明了轻量级模型可以在消费级设备上实现高性能，有望推动 AI 图像编辑的普及。 Moebius 模型仅有 0.2B 参数，但声称性能可与 FLUX.1-Fill-Dev 等 10B 级模型媲美。浏览器版本使用 ONNX Runtime Web 和 WebGPU 加速，整个移植过程是使用 Claude Code 作为并行副项目交互完成的。

rss · Simon Willison · 6月22日 23:43

**背景**: 图像修复是一种由 AI 模型合理填充图像中缺失或不需要部分的技术。传统上，这类模型需要强大的 GPU 和 PyTorch 等框架配合 CUDA 运行。WebGPU 是一种现代浏览器 API，允许直接访问 GPU 进行计算和图形处理，从而无需服务器端处理即可在浏览器中执行机器学习推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/22/porting-moebius/">Porting the Moebius 0.2B image inpainting model to run in the ...</a></li>
<li><a href="https://huggingface.co/papers/2606.19195">Paper page - Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance</a></li>
<li><a href="https://hustvl.github.io/Moebius/">Moebius Project Page</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（item?id=48630171）赞扬了基于浏览器的 AI 的实用演示以及巧妙使用 Claude Code 进行快速原型开发。一些评论者指出本地运行模型的潜在隐私优势，而另一些人则质疑其输出质量与服务器端替代方案的对比。

**标签**: `#image inpainting`, `#WebGPU`, `#browser AI`, `#model porting`, `#machine learning`

---

<a id="item-5"></a>
## [2026 年科技裁员：AI 被列为主要原因](https://techcrunch.com/2026/06/22/the-running-list-major-tech-layoffs-in-2026-where-employers-cited-ai/) ⭐️ 8.0/10

TechCrunch 发布了一份 2026 年主要科技公司裁员的持续更新清单，这些公司在裁员时明确将人工智能列为一个因素，记录了 AI 驱动裁员日益增长的趋势。 这份清单凸显了科技行业的一个重大转变：AI 正越来越多地取代人类岗位，影响就业策略，并引发对岗位流失的担忧。 该清单按时间倒序排列，仅包含那些在宣布大规模裁员时明确将 AI 列为因素的大型科技公司，但摘要中未提供具体公司名称和裁员数字。

rss · TechCrunch · 6月23日 01:27

**背景**: 科技行业裁员屡见不鲜，但明确将 AI 列为裁员原因标志着一个新阶段。AI 自动化日益能够完成以前由人类完成的任务，促使公司重组其劳动力。

**标签**: `#tech layoffs`, `#AI`, `#employment`, `#industry trends`

---

<a id="item-6"></a>
## [微软与雪佛龙计划建设大型燃气数据中心](https://techcrunch.com/2026/06/22/microsoft-and-chevron-plan-one-of-the-largest-gas-powered-data-center-projects-in-us/) ⭐️ 8.0/10

微软与雪佛龙签署了一份为期 20 年的购电协议，用于新建的天然气发电数据中心项目，这将锁定数十年的碳排放。 该协议凸显了人工智能日益增长的能源需求与气候目标之间的紧张关系，大型科技公司转向化石燃料以满足即时电力需求。 该项目是美国最大的燃气数据中心项目之一，20 年的购电协议确保了固定电价，但也承诺长期使用天然气。

rss · TechCrunch · 6月22日 20:37

**背景**: 购电协议（PPA）是发电方与客户之间的长期合同，常用于为能源项目融资。天然气发电厂排放大量温室气体，但低于燃煤电厂。数据中心需要大量电力，而人工智能工作负载正推动能源消耗快速增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Power_purchase_agreement">Power purchase agreement</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gas-fired_power_plant">Gas-fired power plant - Wikipedia</a></li>
<li><a href="https://www.c2es.org/content/natural-gas/">Natural Gas - Center for Climate and Energy SolutionsCenter for Climate and Energy Solutions</a></li>

</ul>
</details>

**标签**: `#data centers`, `#energy`, `#carbon emissions`, `#Microsoft`, `#Chevron`

---

<a id="item-7"></a>
## [TikZ 编辑器：所见即所得与源码同步的 LaTeX 绘图工具](https://tikz.dev/editor/) ⭐️ 7.0/10

一款开源的所见即所得 TikZ 编辑器发布，用户可通过拖拽和调整元素大小来可视化编辑 TikZ 图形，同时保持源代码与渲染图形同步。该编辑器几乎完全由 Codex 编码代理构建。 该工具解决了学术界和 LaTeX 用户长期以来的痛点——传统上需要手动调整坐标并重新编译来创建图形。通过将所见即所得编辑与源码同步相结合，它大大降低了创建高质量 TikZ 图形的门槛。 该编辑器解析 TikZ 代码并跟踪每个对象的精确源码位置，使得修改坐标时不会改变其他代码格式。它还包含从 SVG、PPTX 和 IPE 到 TikZ 的转换器，并重新实现了 LaTeX 的连字和换行算法以支持多行节点。

hackernews · DominikPeters · 6月23日 14:24 · [社区讨论](https://news.ycombinator.com/item?id=48645437)

**背景**: TikZ 是一个强大的 LaTeX 宏包，用于以编程方式创建矢量图形，广泛应用于学术论文中的图表和图形。传统上，用户需要编写如\draw (0,0) -- (1,2);这样的命令，并重新编译才能看到效果，使得迭代设计变得繁琐。所见即所得（WYSIWYG）编辑器允许以接近最终输出的形式进行可视化编辑，但此前很少有适用于 TikZ 的此类工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tikz.dev/">PGF/TikZ Manual - Complete Online Documentation</a></li>
<li><a href="https://www.overleaf.com/learn/latex/TikZ_package">TikZ package - Overleaf, Online LaTeX Editor</a></li>
<li><a href="https://en.wikipedia.org/wiki/WYSIWYG_editor">WYSIWYG editor</a></li>

</ul>
</details>

**社区讨论**: 社区称赞了该编辑器的概念和用户界面，有用户指出它解决了一个长期存在的需求。然而，一个关键的批评是生成的 TikZ 代码全部使用绝对坐标，这不符合 TikZ 的惯用写法，可能导致代码可维护性较差。一些用户还提到了像 q.uiver.app 这样的替代工具用于特定场景。

**标签**: `#LaTeX`, `#TikZ`, `#editor`, `#academic`, `#open-source`

---

<a id="item-8"></a>
## [OpenAI 加入 Appia 基金会推动 AI 标准建设](https://openai.com/index/helping-build-shared-standards-for-advanced-ai) ⭐️ 7.0/10

OpenAI 宣布通过 Appia 基金会为先进 AI 建立共享标准做出贡献，重点关注评估框架、安全实践和全球合作。 这一举措对于确保 AI 安全和促进全球合作至关重要，因为标准化的评估和安全实践有助于在整个行业验证和审计 AI 系统。 由 Linux 基金会发起的 Appia 基金会提供了一个开放的连接层，提供测试标准、评估指南和组件类型，以验证和审计安全可信的 AI 模型。

rss · OpenAI Blog · 6月23日 13:00

**背景**: 随着 AI 系统变得越来越先进，对共享标准以确保安全性和可信度的需求日益增长。Appia 基金会是一个国际性的、开放治理的合作组织，制定规范帮助组织证明其 AI 系统符合相关义务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://appiafoundation.org/">Appia Foundation</a></li>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-launches-appia-foundation-to-establish-standardized-conformity-specifications-across-the-ai-value-chain">Linux Foundation Launches Appia Foundation to Establish ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#standards`, `#OpenAI`, `#global cooperation`, `#evaluation frameworks`

---

<a id="item-9"></a>
## [Datasette 1.0a35 新增创建/修改表界面](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a35 引入了新的“创建表”和“修改表”界面及对应的 JSON API，用户可通过 UI 或 API 修改数据库模式。 此版本通过允许无需直接 SQL 访问即可进行模式更改，显著提升了 Datasette 的易用性，使其对非技术用户更友好，并支持编程式数据库管理。 “创建表”API 支持定义列、主键、自定义类型、NOT NULL 约束、默认值和单列外键。“修改表”API 支持添加、重命名、重新排序和删除列，以及更改类型、默认值、约束、主键、外键和表名。

rss · Simon Willison · 6月23日 21:34

**背景**: Datasette 是一个用于探索和发布数据的开源工具，主要与 SQLite 数据库配合使用。它提供 Web 界面和 JSON API 用于查询和可视化数据。此前，模式更改需要直接 SQL 命令或插件；此 alpha 版本带来了原生的模式编辑功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/stable/json_api.html">JSON API - Datasette documentation</a></li>
<li><a href="https://datasette.io/">Datasette: An open source multi-tool for exploring and publishing data</a></li>

</ul>
</details>

**标签**: `#datasette`, `#data tools`, `#release`, `#JSON API`, `#database`

---

<a id="item-10"></a>
## [Superhuman 收购 AI 检测初创公司 GPTZero](https://techcrunch.com/2026/06/23/superhuman-acquires-ai-detection-startup-gptzero/) ⭐️ 7.0/10

拥有 Grammarly 的办公效率公司 Superhuman 收购了 AI 检测初创公司 GPTZero，该公司由 Edward Tian 和 Alex Cui 于 2023 年创立。 此次收购标志着 AI 检测市场的整合，并增强了 Superhuman 识别 AI 生成内容的能力，这对学术诚信和企业信任至关重要。 GPTZero 最初由普林斯顿毕业生 Edward Tian 作为毕业设计项目开发，已被超过 3500 所大学和数百家机构使用。收购金额未披露。

rss · TechCrunch · 6月23日 21:48

**背景**: GPTZero 是一个 AI 检测平台，用于识别由大型语言模型（如 ChatGPT、Claude 和 Gemini）生成的文本。它因帮助教育工作者检测 AI 撰写的论文而广受欢迎，但也因误报率受到批评。Superhuman 成立于 2009 年，提供包括 Grammarly 在内的办公效率工具，Grammarly 已具备 AI 检测功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/23/superhuman-acquires-ai-detection-startup-gptzero/">Superhuman acquires AI detection startup GPTZero | TechCrunch</a></li>
<li><a href="https://www.businessinsider.com/superhuman-acquires-gptzero-ai-authenticity-tools-2026-6">A Princeton grad built a $30 million AI detection business. Now he's selling it to Superhuman.</a></li>
<li><a href="https://blog.superhuman.com/superhuman-to-acquire-gptzero/">Superhuman to Acquire GPTZero, AI Authenticity Platform</a></li>

</ul>
</details>

**标签**: `#AI`, `#acquisition`, `#AI detection`, `#Grammarly`, `#startup`

---

<a id="item-11"></a>
## [Anthropic 推出 Claude Tag，在 Slack 中学习公司知识](https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/) ⭐️ 7.0/10

Anthropic 发布了 Claude Tag，这是一个常驻 Slack 的 AI 队友，可以像人类同事一样被 @提及。它会从频道对话中持续学习，建立持久的上下文和机构记忆。 这标志着 AI 从工具向团队成员的转变，深度嵌入企业工作流。它可能显著提升生产力，并帮助组织保留员工离职时常丢失的机构知识。 Claude Tag 目前面向 Claude Enterprise 和 Team 客户提供测试版，取代了原有的 Slack 版 Claude 应用。它可以作为团队成员加入组织的 Slack 实例，主动提供洞察、标记问题，并完成编码和数据分析等任务。

rss · TechCrunch · 6月23日 17:00

**背景**: Anthropic 是一家 AI 安全公司，开发了 Claude 系列大语言模型。Slack 是一个流行的企业消息平台，团队在此协作。Claude Tag 基于 AI 代理的概念，这些代理可以在特定环境中自主运行，并从持续交互中学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/introducing-claude-tag">Introducing Claude Tag \ Anthropic</a></li>
<li><a href="https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/">Anthropic’s Claude Tag is learning your company, one Slack ...</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/06/23/anthropic-reimagines-claude-in-slack-as-nosy-always-on-agentic-ai-coworker/5260422">Anthropic reimagines Claude in Slack as nosy, always-on ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#Enterprise`, `#Slack`, `#Anthropic`, `#Productivity`

---

<a id="item-12"></a>
## [LastPass 因 Klue 漏洞泄露客户支持数据](https://techcrunch.com/2026/06/23/password-manager-maker-lastpass-says-hackers-stole-customer-support-case-data-during-klue-breach/) ⭐️ 7.0/10

LastPass 披露，黑客通过其技术合作伙伴 Klue 的漏洞窃取了客户支持案例数据，这是该密码管理器近年来第二次数据泄露。 此事件凸显了密码管理器等关键服务中第三方集成的持续安全风险，可能削弱用户信任，并凸显了加强供应商安全评估的必要性。 此次攻击针对竞争情报平台 Klue，影响了 LastPass 的客户支持案例数据；被盗数据的具体范围和类型尚未完全披露。

rss · TechCrunch · 6月23日 15:12

**背景**: LastPass 此前在 2022 年遭遇重大泄露，攻击者获取了客户密码库备份和个人信息，导致多年的加密货币被盗。此后该公司一直面临对其安全实践的审查。Klue 是一个将竞争情报数据与 Salesforce 同步的平台，其集成被滥用，从多个客户处窃取了 CRM 数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/hackers-breach-klue-integration/">Hackers Breach Klue Integration to Steal Salesforce CRM Data</a></li>
<li><a href="https://reliaquest.com/blog/threat-spotlight-integration-abused-in-crm-data-theft/">Klue Integration Abused in Salesforce Data Theft | ReliaQuest ...</a></li>
<li><a href="https://www.huntress.com/blog/klue-breach-investigation">Cybercrime Breaches Klue: Salesforce Data Impacted for Many ...</a></li>

</ul>
</details>

**标签**: `#security`, `#data breach`, `#password manager`, `#LastPass`

---

<a id="item-13"></a>
## [AI 世界因持续运行的智能体群而变得“循环”](https://techcrunch.com/2026/06/22/the-ai-world-is-getting-loopy/) ⭐️ 7.0/10

一种名为“循环”AI 的新概念提出部署持续在后台运行的 AI 智能体群，而非响应单个提示。这标志着从反应式 AI 向持久、自主的后台处理的转变。 这种方法可以支持更复杂、长期运行的任务和主动协助，改变 AI 融入工作流程的方式。它代表了智能体 AI 的重大演进，迈向能够随时间独立行动的系统。 TechCrunch 的文章描述了这一概念，但提供的技术细节有限。“循环”方法授权一群智能体无休止地工作，意味着无需人工干预的持续运行。

rss · TechCrunch · 6月22日 20:53

**背景**: 智能体 AI 是指能够追求目标、使用工具并以不同程度的自主性采取行动的 AI 系统。群体智能是去中心化、自组织系统的集体行为，通常受蚁群等自然群体的启发。“循环”概念结合了这些思想，创建了持续在后台运行的智能体群。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swarm_intelligence">Swarm intelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#agentic AI`, `#swarm intelligence`, `#background processing`

---

<a id="item-14"></a>
## [Groq 在英伟达交易后融资 6.5 亿美元，转向新云业务](https://techcrunch.com/2026/06/22/ai-chipmaker-groq-confirms-650m-raise-re-staffs-after-nvidias-20b-not-acqui-hire-deal/) ⭐️ 7.0/10

AI 芯片初创公司 Groq 确认完成 6.5 亿美元融资，并在英伟达以 200 亿美元收购其技术及 CEO 的“非收购式雇佣”交易后，重组业务，专注于其新云服务。 此次融资和业务转型展示了 Groq 的韧性及其从芯片设计向云服务的战略转变，可能重塑 AI 基础设施市场与英伟达及超大规模云服务商的竞争格局。 这轮 6.5 亿美元融资由 Disruptive 领投，Groq 还从 xAI 和 Meta 聘请了新高管来领导其新云业务，该业务为 AI 工作负载提供 GPU 即服务。

rss · TechCrunch · 6月22日 20:13

**背景**: Groq 最初开发了 LPU（语言处理单元），这是一种专为 AI 推理设计的 ASIC。新云是一种专门的云服务提供商，通过债务购买 GPU 服务器并按小时出租算力，专注于 AI 和高性能计算工作负载。英伟达的“非收购式雇佣”交易以 200 亿美元收购了 Groq 的知识产权并挖走了其 CEO，迫使这家初创公司重新定位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/22/ai-chipmaker-groq-confirms-650m-raise-re-staffs-after-nvidias-20b-not-acqui-hire-deal/">AI chipmaker Groq confirms $650M raise, re-staffs after ...</a></li>
<li><a href="https://fourweekmba.com/groq-650m-raise-nvidia-20b-acqui-hire-neocloud/">Groq Raises $650M After Nvidia's $20B Not-Acqui-Hire Gutted ...</a></li>
<li><a href="https://groq.com/lpu-architecture">LPU | Groq is fast, low cost inference.</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#funding`, `#Groq`, `#Nvidia`, `#cloud computing`

---

<a id="item-15"></a>
## [ML 团队在生产中跳过对抗性测试](https://www.reddit.com/r/MachineLearning/comments/1uddtws/are_model_security_risks_extraction_poisoning/) ⭐️ 7.0/10

一篇 Reddit 帖子指出，许多 ML 团队在部署模型时未进行针对模型窃取和数据投毒等安全风险的对抗性测试，表明模型的安全审查落后于传统软件。 这一差距使已部署的模型面临攻击风险，攻击者可能窃取知识产权或破坏模型行为，削弱对 ML 系统的信任，并可能导致重大的经济和声誉损失。 该帖子特别提到模型窃取和数据投注是未经测试的风险，并指出模型的安全审查实践不如常规软件成熟。

reddit · r/MachineLearning · /u/Xorphian · 6月23日 10:52

**背景**: 模型窃取攻击允许对手通过查询模型并构建替代模型来窃取模型，而数据投毒攻击则通过破坏训练数据来操纵模型输出。对抗性测试系统地评估模型对此类恶意输入的鲁棒性，但许多生产团队缺乏正式的流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.16065v1">A Survey of Model Extraction Attacks and Defenses in ...</a></li>
<li><a href="https://www.ibm.com/think/topics/data-poisoning">What is data poisoning? - IBM</a></li>
<li><a href="https://developers.google.com/machine-learning/guides/adv-testing">Adversarial Testing for Generative AI | Machine Learning ...</a></li>

</ul>
</details>

**标签**: `#ML Security`, `#Adversarial Testing`, `#Model Extraction`, `#Data Poisoning`, `#Production ML`

---