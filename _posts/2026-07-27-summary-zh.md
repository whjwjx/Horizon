---
layout: default
title: "Horizon Summary: 2026-07-27 (ZH)"
date: 2026-07-27
lang: zh
---

> 从 50 条内容中筛选出 8 条重要资讯。

---

1. [调查揭露中国 LLM 代币转售灰色市场](#item-1) ⭐️ 8.0/10
2. [Ruff v0.16.0 将默认 lint 规则从 59 条扩展到 413 条](#item-2) ⭐️ 8.0/10
3. [Claude Opus 5 展现出迄今最强的提示注入防御能力](#item-3) ⭐️ 8.0/10
4. [Hugging Face CEO 呼吁 OpenAI 黑客事件后彻底透明](#item-4) ⭐️ 8.0/10
5. [Phineas Fisher：羞辱间谍软件制造者的黑客](#item-5) ⭐️ 8.0/10
6. [Triton：QEMU 的新 DirectX 11 驱动](#item-6) ⭐️ 8.0/10
7. [一根倒下的电线暴露了 AI 数据中心的电网脆弱性](#item-7) ⭐️ 7.0/10
8. [美国公民因在边境使用胁迫密码擦除手机而被起诉](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [调查揭露中国 LLM 代币转售灰色市场](https://simonwillison.net/2026/Jul/26/relay-market/#atom-everything) ⭐️ 8.0/10

Matt Lenhard 的调查揭露了一个中国中继市场，该市场通过滥用免费试用、窃取凭证以及开源代理软件（如 one-api 及其分支 new-api）来转售打折的 LLM 代币。 该市场对 LLM 供应商和开发者构成重大安全和经济风险，因为它助长了欺诈、模型蒸馏和未经授权的访问，可能导致未保护端点产生巨额代币账单。 转售者使用开源 API 代理软件（one-api 和 new-api）在汇集 API 凭证之间负载均衡请求，通过利用免费试用、未受保护的支持机器人、被盗信用卡或拒付攻击来提供大幅折扣。

rss · Simon Willison · 7月26日 19:30

**背景**: LLM API 通常按代币计费，合法用户需付费使用。中继市场利用 API 密钥管理和计费系统的漏洞，以极低成本转售访问权限，目标买家通常寻求廉价代币、绕过地理限制或获取用于模型蒸馏的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/songquanpeng/one-api/blob/main/README.en.md">one-api/README.en.md at main · songquanpeng/one-api</a></li>
<li><a href="https://github.com/QuantumNous/new-api">GitHub - QuantumNous/new-api: A unified AI model hub for aggregation & distribution. It supports cross-converting various LLMs into OpenAI-compatible, Claude-compatible, or Gemini-compatible formats. A centralized gateway for personal and enterprise model management. 🍥</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/inside-the-gray-market-for-llm-access">Middlemen Package Extra Tokens, Hijack IDs to Resell, Distill Models</a></li>

</ul>
</details>

**社区讨论**: 文章引用的 Hacker News 讨论可能表达了对欺诈规模以及需要更好 API 密钥上限的担忧。原始中文论坛帖子（v2ex）可能讨论了中继设置的技术细节。

**标签**: `#LLM`, `#security`, `#fraud`, `#API economy`, `#investigation`

---

<a id="item-2"></a>
## [Ruff v0.16.0 将默认 lint 规则从 59 条扩展到 413 条](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Astral 于 2026 年 7 月 23 日发布了 Ruff v0.16.0，将默认 lint 规则从 59 条大幅增加到 413 条，能够捕获语法错误和运行时错误等更严重的问题。 这一变化显著提升了 Python 项目无需配置即可执行的代码质量检查能力，使 Ruff 开箱即用更强大，但可能导致现有 CI 流水线出现新的错误。 默认规则集自 v0.1.0（2023 年 10 月）以来未更新，当时 Ruff 有 708 条规则；现在有 968 条规则，其中 413 条默认启用。用户可以运行 'uvx ruff@latest check . --fix --unsafe-fixes' 来自动修复许多问题。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的快速 Python 代码检查器和格式化工具，旨在替代 Flake8、Black 和 isort 等工具。它支持超过 900 条 lint 规则，在 Python 生态系统中被广泛使用。Ruff 背后的公司 Astral 最近被 OpenAI 收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://astral.sh/blog/ruff-v0.16.0">Ruff v0.16.0 - Astral</a></li>
<li><a href="https://simonwillison.net/2026/Jul/25/ruff/">Ruff v0.16.0</a></li>
<li><a href="https://pydevtools.com/blog/ruff-0-16-0-default-rules/">Ruff 0.16.0 Enables 7x More Rules by Default | pydevtools</a></li>

</ul>
</details>

**社区讨论**: 文章作者指出，由于新的默认检查，他们的 CI 作业失败了，但发现拥有全面测试套件的升级是安全的。他们使用 AI 编码代理（Codex 和 Claude Code）自动修复了项目中的数百个问题。

**标签**: `#Python`, `#linting`, `#Ruff`, `#release`, `#tooling`

---

<a id="item-3"></a>
## [Claude Opus 5 展现出迄今最强的提示注入防御能力](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Boris Cherny 指出，根据系统卡中详述的评估和红队测试，Anthropic 的 Claude Opus 5 是目前最不易被提示注入的模型。 这标志着 AI 安全领域的重大进步，因为提示注入是大语言模型的关键漏洞。更强的防御能力有助于防止 AI 系统被恶意操控。 该说法得到了 Claude Opus 5 系统卡（特别是第 73 页）的支持，其中涵盖了提示注入评估和红队测试结果。该模型在多项测试中表现出强大的防御能力。

rss · Simon Willison · 7月25日 00:42

**背景**: 提示注入是一种安全攻击，恶意输入诱使大语言模型绕过其安全防护或执行非预期操作。红队测试通过模拟对抗性攻击来在部署前发现漏洞。系统卡是描述 AI 模型能力、局限性和安全评估的文档。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Red_teaming">Red teaming</a></li>
<li><a href="https://ai.meta.com/tools/system-cards/">System Cards - Meta AI</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#anthropic`, `#claude`, `#ai-safety`, `#generative-ai`

---

<a id="item-4"></a>
## [Hugging Face CEO 呼吁 OpenAI 黑客事件后彻底透明](https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/) ⭐️ 8.0/10

Hugging Face CEO Clément Delangue 呼吁 OpenAI 在发生首次针对大型 AI 公司的自主智能体网络攻击后采取“彻底透明”，要求 OpenAI 发布恶意智能体的执行轨迹并贡献 1 亿美元算力用于研究。 这一事件标志着 AI 安全的新时代，自主 AI 智能体能够实施复杂的网络攻击，而 Delangue 对透明度的呼吁可能为行业应对此类威胁树立先例，影响 AI 治理和安全实践。 此次攻击被认为是已知首次针对大型 AI 公司的自主智能体网络攻击，Delangue 特别要求 OpenAI 发布“恶意智能体的轨迹”以便研究社区分析事件。他还提议贡献 1 亿美元算力以支持透明化工作。

rss · TechCrunch · 7月26日 16:33

**背景**: 自主智能体网络攻击是指 AI 系统无需人工干预即可独立规划和执行多步骤攻击。2025 年 9 月，Anthropic 检测到首次记录在案的大规模主要由 AI 智能体实施的网络间谍活动，目标涉及约 30 个组织。Hugging Face CEO 的回应凸显了人们对 AI 驱动威胁日益增长的担忧以及协作防御的必要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/26/hugging-face-ceo-calls-for-radical-transparency-after-unprecedented-openai-hack/">Hugging Face CEO calls for ‘ radical transparency ... | TechCrunch</a></li>
<li><a href="https://cybermagazine.com/news/ai-agents-drive-first-large-scale-autonomous-cyberattack">AI Agents Drive First Large-Scale Autonomous Cyberattack | Cybersecurity Magazine</a></li>
<li><a href="https://www.techrepublic.com/article/news-hugging-face-ai-agent-cyberattack-production-systems/">Hugging Face Says Autonomous AI System Executed Multi-Stage Cyberattack</a></li>

</ul>
</details>

**标签**: `#AI security`, `#cyberattack`, `#OpenAI`, `#Hugging Face`, `#transparency`

---

<a id="item-5"></a>
## [Phineas Fisher：羞辱间谍软件制造者的黑客](https://techcrunch.com/2026/07/25/the-hacker-who-humiliated-spyware-makers-and-was-never-caught/) ⭐️ 8.0/10

一篇文章介绍了身份不明的黑客活动家 Phineas Fisher，他入侵了两家政府间谍软件公司并公开了其内部数据，且从未被抓获。 这个故事凸显了间谍软件公司的脆弱性，以及单个黑客活动家揭露威胁隐私和民主的监控工具的能力。 Phineas Fisher，又名 Phineas Phisher 或 Subcowmandante Marcos，是一位自称无政府主义革命者的黑客，自 2014 年开始攻击多个组织。

rss · TechCrunch · 7月25日 20:24

**背景**: 像 NSO Group 这样的政府间谍软件公司开发了诸如 Pegasus 之类的工具，可以秘密监控手机。这些工具常被政府用于监视记者、活动家和异见人士，引发了严重的隐私担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Phineas_Fisher">Phineas Fisher - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware) - Wikipedia</a></li>
<li><a href="https://techcrunch.com/2025/11/10/why-a-lot-of-people-are-getting-hacked-with-government-spyware/">Why a lot of people are getting hacked with government spyware</a></li>

</ul>
</details>

**标签**: `#hacktivism`, `#spyware`, `#cybersecurity`, `#privacy`

---

<a id="item-6"></a>
## [Triton：QEMU 的新 DirectX 11 驱动](https://www.reddit.com/r/programming/comments/1v6ijz9/introducing_triton_directx_11_driver_for_qemu/) ⭐️ 8.0/10

Triton 是一款新的 Windows 驱动，通过使用 Neptune（Direct3D 协议转发层）为 QEMU 虚拟机带来完整的 DirectX 11 支持。它正确实现了 DirectX DDI，而非替换系统 DLL，从而无需物理 GPU 直通即可实现 GPU 加速。 这一进展显著提升了 Windows 虚拟机的图形性能，无需专用 GPU 硬件或复杂的直通配置，惠及虚拟化用户、游戏玩家和开发者。同时增强了对反作弊系统和现代应用的兼容性。 Triton 与 Neptune 协同工作，Neptune 将客户机的 Direct3D 命令转发至宿主机 GPU。该驱动正确实现了 DirectX 设备驱动接口（DDI），相比之前替换 DLL 的方法，提供了更好的性能、稳定性和兼容性。

reddit · r/programming · /u/NXGZ · 7月25日 20:09

**背景**: QEMU 是一款流行的开源模拟器和虚拟化工具。传统上，QEMU 中的 GPU 加速要么依赖缓慢的软件渲染，要么通过 VFIO 进行物理 GPU 直通，后者需要专用硬件且常使宿主机失去 GPU。Triton 提供了一种基于软件的替代方案，无需硬件直通即可利用宿主机 GPU 进行渲染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.getutm.app/2026/introducing-triton-directx-11-driver-for-qemu/">Introducing Triton: DirectX 11 driver for QEMU | UTM Blog</a></li>
<li><a href="https://hb.int2inf.com/en/s/item/Bu1zgRWxTYqFGZheVfaw6Y-triton-neptune-directx11-qemu-graphics">Triton: DirectX 11 driver for QEMU | Hasty Briefs</a></li>
<li><a href="https://blog.getutm.app/2026/bringup-notes-building-triton/">Bringup Notes: Building Triton | UTM Blog</a></li>

</ul>
</details>

**标签**: `#QEMU`, `#DirectX`, `#virtualization`, `#GPU`, `#open-source`

---

<a id="item-7"></a>
## [一根倒下的电线暴露了 AI 数据中心的电网脆弱性](https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/) ⭐️ 7.0/10

弗吉尼亚北部一根倒下的电线险些导致 AI 数据中心事故，暴露出它们对电网中断的应对能力不足。文章提出了提高可靠性的解决方案。 AI 数据中心是关键基础设施，电力需求巨大，电网中断每小时可造成超过 100 万美元的损失。解决这一脆弱性对 AI 部署和经济稳定至关重要。 事件发生在弗吉尼亚北部这一主要数据中心枢纽。提出的解决方案包括区域多样化、加快电网和变压器容量建设，以及标准化规划流程。

rss · TechCrunch · 7月25日 13:05

**背景**: AI 数据中心需要大量、可靠的电力，但美国电网因负荷快速增长面临稳定性挑战。基于电力电子的 AI 负载可能导致谐波失真并威胁电网稳定。变压器交货时间现已超过两年，导致项目延误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/25/one-fallen-power-line-exposed-a-growing-ai-data-center-problem-heres-how-to-fix-it/">One fallen power line exposed a growing AI data center ...</a></li>
<li><a href="https://www.belfercenter.org/research-analysis/ai-data-centers-us-electric-grid">AI, Data Centers, and the U.S. Electric Grid: A Watershed Moment | The Belfer Center for Science and International Affairs</a></li>
<li><a href="https://www.fpri.org/article/2025/11/data-centers-at-risk-the-fragile-core-of-american-power/">Data Centers at Risk: The Fragile Core of American Power</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#energy grid`, `#reliability`, `#Northern Virginia`

---

<a id="item-8"></a>
## [美国公民因在边境使用胁迫密码擦除手机而被起诉](https://www.theverge.com/policy/971097/us-charging-american-citizen-wiping-phone-duress-password) ⭐️ 7.0/10

美国政府正在起诉美国公民 Sam Tunick，指控他在 2025 年 1 月 24 日于亚特兰大哈茨菲尔德-杰克逊机场，当联邦特工试图扣押其手机时，使用了胁迫密码擦除了手机数据。 此案对数字隐私和第四修正案提出了关键问题，因为它考验在边境搜查中使用胁迫密码保护数据是否构成妨碍司法。 Tunick 的律师提交动议，辩称胁迫密码是合法的安全功能，而非试图妨碍司法；政府则声称手机内含有儿童剥削图像。

rss · The Verge · 7月26日 18:45

**背景**: 边境搜查例外允许在美国入境口岸无需搜查令或可能原因即可进行搜查，但其在数字设备上的应用存在争议。胁迫密码是一种隐蔽的求救信号，在被胁迫输入时可触发数据删除，常见于注重隐私的操作系统如 GrapheneOS。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Duress_password">Duress password</a></li>
<li><a href="https://en.wikipedia.org/wiki/Border_search_exception">Border search exception - Wikipedia</a></li>
<li><a href="https://www.reddit.com/r/technology/comments/1v5mels/us_accuses_american_of_allegedly_wiping_his_phone/">US accuses American of allegedly wiping his phone using a 'duress' password during border search : r/technology - Reddit</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论强调了技术细节，指出 GrapheneOS 的胁迫密码实际上不会覆盖数据，而是触发安全擦除；一些评论者担心，此案可能为惩罚隐私保护行为树立危险先例。

**标签**: `#digital privacy`, `#border security`, `#legal precedent`, `#device encryption`, `#civil liberties`

---