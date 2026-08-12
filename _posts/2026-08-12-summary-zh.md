---
layout: default
title: "Horizon Summary: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
---

> 从 83 条内容中筛选出 15 条重要资讯。

---

1. [Qwen3.8-2.4T-A95B：大型 MoE 模型媲美顶尖 AI，通过 1 比特量化可在消费级硬件上运行](#item-1) ⭐️ 9.0/10
2. [研究人员窃取主要 LLM API 的隐藏推理](#item-2) ⭐️ 9.0/10
3. [DeepSeek V4 Pro 0813：低成本编程模型获社区好评](#item-3) ⭐️ 8.0/10
4. [Tailscale 将数据库损坏追溯到 16 年前的 SQLite WAL 重置错误](#item-4) ⭐️ 8.0/10
5. [Meta 发布 Muse Glimmer：开源 30B 参数智能体模型](#item-5) ⭐️ 8.0/10
6. [亚马逊默认使用 Twitch 主播内容训练 AI，需选择退出](#item-6) ⭐️ 8.0/10
7. [AI 先驱在 Ai4 上辩论开放与安全](#item-7) ⭐️ 8.0/10
8. [Form Energy 融资 7.5 亿美元，用于 100 小时铁空气电池](#item-8) ⭐️ 8.0/10
9. [微软威胁诉讼后，研究人员发布 Windows 零日漏洞](#item-9) ⭐️ 8.0/10
10. [Adam 的各向异性破坏旋转不变性与低秩偏好](#item-10) ⭐️ 8.0/10
11. [CPU 去优化项目发现最慢 x86 指令：耗时 1980 亿周期](#item-11) ⭐️ 8.0/10
12. [林纳斯·托瓦兹解释 Linux 的速度与设计原则](#item-12) ⭐️ 8.0/10
13. [你从未听说过的最快双精度转字符串算法](#item-13) ⭐️ 8.0/10
14. [Zed 推出 Delta 多人协作编程环境](#item-14) ⭐️ 7.0/10
15. [企业从 AI 辅助转向智能体执行](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B：大型 MoE 模型媲美顶尖 AI，通过 1 比特量化可在消费级硬件上运行](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个 2.4 万亿参数的混合专家（MoE）模型，活跃参数为 950 亿，已在 Hugging Face 上提供 BF16 和 FP8 格式。模型卡声称性能介于 Opus 4.8 和 Fable 5 之间，社区报告显示 1 比特量化版本约 397GB，可在高端消费级硬件上本地部署。 此次发布大幅降低了本地运行最先进 AI 模型的门槛，因为 1 比特量化版本可以在普通人能购买的机器上运行，可能使前沿性能的获取更加民主化。同时，它加剧了 Qwen、Kimi 和 DeepSeek 等开源权重模型提供商之间的竞争，推动效率和可访问性的边界。 完整的 BF16 模型约 4.9TB，而 1 比特量化版本约 397GB，每个 MoE 活跃参数为 950 亿。开源权重模型默认缺少视觉输入和 1M 上下文长度，这些是官方 Qwen3.8-Max 版本独有的。由于 q4 量化缺乏 QAT，发布时服务该模型具有挑战性，需要外部量化工作。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: 混合专家（MoE）模型每个 token 只激活部分参数，从而在可控计算下实现大规模。量化通过降低数值精度来减小模型大小，1 比特量化是一种极端形式，可以大幅缩小模型以适应消费级硬件。Qwen 是领先的开源权重 AI 模型系列，此次发布延续了越来越大且高效的开源模型的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/ Qwen 3 . 8 - 2 . 4 T - A 95 B · Hugging Face</a></li>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen 3 . 8 - 2 . 4 T - A 95 B , a 2 . 4 T -Parameter Model , with...</a></li>
<li><a href="https://www.remio.ai/post/qwen-3-8-open-weight-model-announcement-promises-2-4t-parameters-but-proof-comes">Qwen 3 . 8 Open-Weight Model Announcement Promises...</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调该模型通过 1 比特量化的可访问性，一位用户指出它将 Opus 4.5 级别的性能带入了普通人能购买的机器。其他人讨论了服务挑战、与 Kimi k3 和 DeepSeek V4-Pro 等竞争对手的比较，以及对开源权重版本缺少视觉和 1M 上下文功能的失望。

**标签**: `#AI/ML`, `#Large Language Models`, `#MoE`, `#Qwen`, `#Open Source`

---

<a id="item-2"></a>
## [研究人员窃取主要 LLM API 的隐藏推理](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/) ⭐️ 9.0/10

研究人员展示了一种方法，通过将加密的推理痕迹重放到较弱的兄弟模型中并对其进行越狱，从而解密并恢复专有 LLM API 的隐藏思维链推理。该攻击影响了 Anthropic、OpenAI 和 Google，但此后已被修复。 这一漏洞暴露了主要 AI API 中的重大隐私缺陷，使得攻击者能够恢复提供商原本打算隐藏的内部推理。这凸显了在 AI 服务中加强加密和访问控制的必要性，并对 AI 安全和用户信任产生影响。 该攻击利用了同一系列模型共享相同加密密钥的事实，使得加密的推理块可以在会话和模型之间重放。最容易攻击的目标是 Claude Haiku 4.5，通过简单的提示和助手回合前缀即可越狱。论文附录中包含了大量提取的推理痕迹。

rss · Simon Willison · 8月11日 22:40

**背景**: 思维链（CoT）推理是一种让 LLM 生成中间推理步骤以提高复杂任务性能的技术。专有 LLM API 通常通过加密来隐藏这些推理痕迹，但这项研究表明加密可以被绕过。攻击涉及将加密的痕迹重放到较弱的模型中并对其进行越狱，以揭示原始推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://www.explainx.ai/blog/stealing-reasoning-traces-encrypted-cot-vulnerability-august-2026">Stealing Reasoning Traces: The Encrypted Chain-of-Thought ...</a></li>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes ...</a></li>

</ul>
</details>

**社区讨论**: 未提供社区讨论，但根据高分和主题，可能涉及对 AI 隐私和安全的担忧，一些人赞扬这项研究，另一些人质疑其严重性。然而，没有具体的评论可用。

**标签**: `#LLM security`, `#chain-of-thought`, `#privacy`, `#AI research`, `#vulnerability`

---

<a id="item-3"></a>
## [DeepSeek V4 Pro 0813：低成本编程模型获社区好评](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek 发布了 V4 Pro 0813 快照版本，这是一个大规模混合专家模型，在 OpenRouter 上以每百万输入 token 0.435 美元、每百万输出 token 0.87 美元的价格提供。它支持 1,048,576 token 的上下文窗口和最多 384,000 个输出 token，并提供思考和非思考两种模式。 此次发布意义重大，因为它以远低于领先闭源模型的成本提供了具有竞争力的编程性能，可能使开发者和初创公司更容易获得先进的 AI 技术。社区的高度参与（692 分，246 条评论）反映了人们对高性价比 AI 替代方案的浓厚兴趣。 来自 Artificial Analysis 和 LM Market Cap 的独立基准测试将 DeepSeek V4 Pro 0813 在编程类别中排名约第 59 位。社区在 Codex CLI 上的测试显示，它用 12 分钟完成了一个功能，花费 0.12 美元，但存在一个 bug；而 Grok 4.6 在 3 分钟内完成，花费 1.41 美元，且没有 bug。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek 是一家中国 AI 公司，以发布成本更低、可与专有系统相媲美的开放权重模型而闻名。V4 Pro 系列基于混合专家架构，每个 token 只激活部分参数，从而提高效率。该模型专为高级推理、编程和长周期智能体工作流设计，并可通过多个提供商使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://lmmarketcap.com/model/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - Pricing & Benchmarks 2026 | LM Market Cap</a></li>
<li><a href="https://models.dev/models/deepseek/deepseek-v4-pro-0813/">DeepSeek V 4 Pro 0813 pricing, providers, and specs | Models .dev</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户称赞该模型的成本效益和处理繁重开发任务的能力。一些用户指出链接到 OpenRouter 缺乏有用信息，建议链接到官方文档或基准测试。直接对比显示，DeepSeek V4 Pro 0813 更便宜但速度较慢且有 bug，而 Grok 4.6 更快且无 bug，但价格更高。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#cost efficiency`

---

<a id="item-4"></a>
## [Tailscale 将数据库损坏追溯到 16 年前的 SQLite WAL 重置错误](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale 公开详细说明了 SQLite WAL 重置逻辑中一个 16 年前的错误，该错误导致其控制平面反复出现数据库损坏。经过大量调试后，该错误已在 SQLite 3.51.3 版本中修复。 这一事件凸显了严格测试和开源调试工具的重要性，因为即使是像 SQLite 这样广泛使用且经过充分测试的数据库，也可能隐藏多年的细微错误。它也展示了公司如何资助开源开发，从而使整个生态系统受益。 该错误是 WAL 重置逻辑中的一个数据竞争，尽管 SQLite 采用单写者设计，但仅在特定并发条件下才会发生。Tailscale 和 SQLite 团队花了数周时间寻找该错误，最初的修复在破坏其他功能后被回滚，最终在 3.51.3 版本中修复。

hackernews · ropbear · 8月12日 14:22 · [社区讨论](https://news.ycombinator.com/item?id=49272832)

**背景**: SQLite 是一种广泛使用的嵌入式数据库，支持预写日志（WAL）以提高性能和并发性。WAL 将新条目临时存储在单独的文件中，然后检查点将其合并到主数据库。该错误涉及 WAL 重置过程中的竞争条件，在特定情况下可能导致数据库损坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://www.theregister.com/databases/2026/08/12/tailscale-says-deeply-buried-16-year-old-sqlite-bug-caused-last-years-outages/5287004">Tailscale says deeply buried 16-year-old SQLite bug caused ...</a></li>
<li><a href="https://antithesis.com/blog/2026/wal-reset-bug/">Breaking the WAL | Antithesis</a></li>

</ul>
</details>

**社区讨论**: 社区赞扬了 Tailscale 的详细描述以及他们对开源开发的资助，特别是帮助隔离该错误的 SQLite VFS 垫片。一些评论者指出，单写者设计仍然存在数据竞争具有讽刺意味，而其他人则欣赏技术深度和公司的透明度。

**标签**: `#SQLite`, `#database`, `#bug`, `#Tailscale`, `#open-source`

---

<a id="item-5"></a>
## [Meta 发布 Muse Glimmer：开源 30B 参数智能体模型](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/) ⭐️ 8.0/10

Meta 推出了 Muse Glimmer，这是一个 30B 参数的开源权重模型，采用 Apache 2.0 许可证发布，针对智能体任务完成、工具使用和多步推理进行了优化。该模型可通过 LM Studio 和 Hugging Face 下载，并提供 18.16 GB 的量化版本。 此次发布意义重大，因为 Meta 以宽松许可证回归开源权重模型，可能加速智能体 AI 在本地和消费级环境中的采用。对智能体能力的关注与行业向自主任务完成和工具集成发展的趋势一致。 Muse Glimmer 是一个视觉模型，带有专用感知编码器，从 Muse Spark 蒸馏而来。它在 DeepSearchQA、MCP-Atlas、τ-Bench 和 SWE-Bench 等基准测试中表现良好，并且可以在 32 GB 或更高内存的机器上运行，为其他应用留出空间。

rss · Simon Willison · 8月10日 23:56

**背景**: 智能体 AI 指的是能够自主执行多步任务、使用工具并进行长程推理的模型。开源权重模型允许开发者在本地运行和微调，提供隐私和定制化优势。Apache 2.0 是一种宽松许可证，允许商业使用且限制极少。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ollama.com/library/muse-glimmer">muse - glimmer</a></li>
<li><a href="https://huggingface.co/meta-models/Muse-Glimmer-30B">meta- models / Muse - Glimmer -30B · Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2601.20975">[2601.20975] DeepSearchQA: Bridging the Comprehensiveness Gap ... DeepSearchQA:Bridgingthe ComprehensivenessGapforDeepResearch ... DeepSearchQA: Bridging the Comprehensiveness Gap for Deep ... DeepSearchQA Leaderboard & Scores — August 2026 | BenchLM.ai DeepSearchQA Leaderboard DeepSearchQA Evaluation for AI-Q Deep Researcher google/deepsearchqa · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#Meta`, `#Agentic AI`, `#Model Release`

---

<a id="item-6"></a>
## [亚马逊默认使用 Twitch 主播内容训练 AI，需选择退出](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/) ⭐️ 8.0/10

亚马逊将默认使用 Twitch 主播的内容进行 AI 训练，用户若不想被使用需主动选择退出。Twitch 首席产品官 Mike Minton 在直播中确认了这一政策，并表示如果采用选择加入模式，参与人数会很少。 这一政策转变引发了内容创作者对隐私和伦理的重大担忧，因为他们的内容在未经明确同意的情况下被使用。这可能为其他平台树立先例，并加剧关于 AI 训练数据同意和创作者权利的辩论。 该政策默认适用于所有 Twitch 主播，并提供选择退出机制。Mike Minton 的评论“如果这是选择加入，没人会加入”凸显了公司的理由，但也因忽视用户偏好而受到批评。

rss · TechCrunch · 8月12日 20:10

**背景**: Twitch 是亚马逊旗下的直播平台，创作者在此直播游戏、音乐等内容。AI 训练通常使用大量公开可用的数据集，但未经明确同意使用创作者内容会引发法律和伦理问题。亚马逊的生成式 AI 披露中表示，其 AI 训练会使用公开可用的数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.windowscentral.com/artificial-intelligence/if-it-was-opt-in-nobody-would-opt-in-cringe-twitch-cpo-admits-everyone-hates-its-ai-training-feature-doesnt-care">"If it was opt in ... nobody would opt-in." Twitch CPO ... | Windows Ce...</a></li>
<li><a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=TmGoGN3UbFaQ1CAph7">Generative AI Development Disclosure - Amazon Customer Service</a></li>
<li><a href="https://aws.amazon.com/bedrock/amazon-models/privacy/">Amazon Model Training & Privacy - AWS</a></li>

</ul>
</details>

**社区讨论**: 社区反应普遍负面，许多人批评 CPO 的言论无视用户关切。一些用户指出，与 YouTube 不同，Twitch 至少提供了选择退出选项，但默认选择加入的做法被视为对创作者信任的背叛。

**标签**: `#AI training`, `#Twitch`, `#Amazon`, `#privacy`, `#content policy`

---

<a id="item-7"></a>
## [AI 先驱在 Ai4 上辩论开放与安全](https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/) ⭐️ 8.0/10

在 Ai4 大会上，杰弗里·辛顿、李飞飞和吴恩达就 AI 监管、开源访问以及面对中国进步时美国的竞争力进行了公开辩论。 这次讨论意义重大，因为它汇集了 AI 领域三位最具影响力的声音，共同探讨一个关键政策问题：如何在安全关切与开放的好处之间取得平衡。他们的观点可能影响全球的监管方法和行业实践，对开发者、研究人员和政策制定者产生影响。 辩论在 Ai4 大会上举行，小组成员讨论了 AI 安全与开源访问之间的紧张关系，以及在中国 AI 进步的情况下美国如何竞争。没有宣布具体的政策建议或技术突破，但交流凸显了专家们不同的观点。

rss · TechCrunch · 8月12日 17:51

**背景**: 随着先进 AI 系统能力的增强，AI 安全问题日益受到关注，导致有人呼吁对开源模型进行监管和限制。然而，开源倡导者认为，透明度和协作对于创新以及确保 AI 利益广泛分配至关重要。这场辩论反映了关于如何负责任地治理 AI 发展的更广泛的行业和政策讨论。

**标签**: `#AI safety`, `#AI regulation`, `#open source`, `#Geoffrey Hinton`, `#Fei-Fei Li`

---

<a id="item-8"></a>
## [Form Energy 融资 7.5 亿美元，用于 100 小时铁空气电池](https://techcrunch.com/2026/08/12/form-energy-raises-750m-to-build-more-100-hour-batteries-for-the-grid/) ⭐️ 8.0/10

Form Energy 已筹集 7.5 亿美元，用于扩大其 100 小时铁空气电池的制造规模，谷歌和 Crusoe 为其客户。这笔资金将支持扩大生产，以满足对长时电网储能日益增长的需求。 这轮重大融资凸显了长时储能对整合可再生能源日益增长的重要性。有了谷歌和 Crusoe 等主要客户，Form Energy 的技术可能有助于稳定电网，减少对化石燃料的依赖。 100 小时铁空气电池采用可逆锈蚀技术，储能成本低于 20 美元/千瓦时，比锂离子电池便宜约 10 倍。Form Energy 位于西弗吉尼亚州的超级工厂已开始出货这些电池，新资金将进一步扩大产能。

rss · TechCrunch · 8月12日 16:18

**背景**: 铁空气电池是一种金属空气电池，以铁为阳极，以环境空气中的氧气为阴极。它专为长时储能设计，可提供长达 100 小时的电力，这对于平衡太阳能和风能等间歇性可再生能源至关重要。该技术被视为解决可再生能源间歇性问题的关键方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Metal–air_electrochemical_cell">Metal–air electrochemical cell - Wikipedia</a></li>
<li><a href="https://energy-solutions.co/articles/sub/aqueous-iron-air-batteries-long-duration-storage">Iron-Air Batteries 2026: 100-Hour Storage at Under $20/kWh ...</a></li>
<li><a href="https://hardware.slashdot.org/story/26/02/28/0446211/worlds-largest-battery-soon-at-google-data-center-100-hour-iron-air-storage">'World's Largest Battery ' Soon At Google Data Center: 100 - Hour ...</a></li>

</ul>
</details>

**标签**: `#energy storage`, `#batteries`, `#renewable energy`, `#grid`, `#funding`

---

<a id="item-9"></a>
## [微软威胁诉讼后，研究人员发布 Windows 零日漏洞](https://techcrunch.com/2026/08/12/after-microsoft-threatened-legal-action-a-security-researcher-publishes-a-new-windows-zero-day-bug/) ⭐️ 8.0/10

安全研究员 Nightmare Eclipse 不顾微软公开威胁采取法律行动，发布了一个新的 Windows 零日漏洞。这是该研究员一系列披露中的最新一次，加剧了独立安全研究员与软件巨头之间的紧张关系。 这一事件凸显了安全研究人员与供应商在漏洞披露问题上的持续冲突，引发了对负责任披露与法律恐吓之间平衡的质疑。它可能影响研究人员未来选择披露漏洞的方式，进而影响全球 Windows 用户的安全。 该零日漏洞是 Nightmare Eclipse 发布的最新一个，此前他已发布过其他 Windows 漏洞。微软的法律威胁似乎并未阻止该研究员，此次发布可能包含可能被恶意行为者利用的技术细节。

rss · TechCrunch · 8月12日 15:18

**背景**: 零日漏洞是指供应商未知的软件缺陷，没有可用的补丁，因此对攻击者极具价值。漏洞披露是一个有争议的问题：研究人员在发布细节时经常面临供应商的法律威胁，即使他们以负责任的方式行事。微软有对研究人员采取法律行动的历史，此案是安全社区更广泛紧张模式的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-target-defense-firms/">Lazarus hackers exploited Windows zero-day to target defense ...</a></li>
<li><a href="https://www.zdnet.com/article/microsoft-august-windows-update-421-bugs-zero-day-exploited/">Microsoft fixes 421 bugs and a Windows zero-day in August ...</a></li>
<li><a href="https://github.com/disclose/research-threats">GitHub - disclose/research-threats: Collection of legal threats against good faith Security Researchers; vulnerability disclosure gone wrong. A continuation of work started by @attritionorg · GitHub</a></li>

</ul>
</details>

**标签**: `#security`, `#zero-day`, `#Microsoft`, `#vulnerability disclosure`, `#legal`

---

<a id="item-10"></a>
## [Adam 的各向异性破坏旋转不变性与低秩偏好](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

一项新研究表明，Adam 的逐坐标自适应性破坏了因子模型中的旋转不变性，导致隐式低秩偏好的丧失，而 Muon 和 Shampoo 等优化器则保留了这一性质。作者在欠定矩阵感知上测试了九种更新规则，发现基于该性质可分为两个明显的聚类。 这一见解将优化器选择与矩阵分解中的隐式偏差联系起来，对于理解过参数化模型的泛化至关重要。它可能指导实践者选择保留低秩结构的优化器，从而在矩阵补全和深度学习等任务上提升性能。 该研究包含一个单参数族，可在逐坐标和共享标量分母之间插值，表明随着各向异性降低，恢复性能单调提升。Muon 在真正低秩目标上表现精确，但随着谱尾增加而退化，并在约 4%尾能量处与 GD 交叉。作者还发现，全局范数裁剪将其自身优化器的恢复误差从 0.347 改善到 0.220。

reddit · r/MachineLearning · /u/EtherealGlyph · 8月12日 16:39

**背景**: 在矩阵分解中，像 W = UV^T 这样的模型对旋转(U,V) → (UQ, VQ)具有不变性，而梯度下降尊重这种对称性。Adam 的逐坐标二阶矩归一化打破了这种不变性，因为它依赖于因子的基。隐式偏差是指优化算法在没有显式正则化的情况下，倾向于收敛到具有某些属性（如低秩）的解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.24218v2">Conda: Column-Normalized Adam for Training Large Language Models Faster</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rotational_invariance">Rotational invariance - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论中包括对 Muon 影响的辩论，一些人报告其具有强烈的谱简单性偏差，而另一些人发现它在深度线性模型中拟合虚假特征。作者指出，他们的扫描在同一轴上显示了这两种行为。还有关于更努力调优 Adam 的评论，作者对此表示欢迎。

**标签**: `#optimization`, `#implicit bias`, `#low-rank`, `#Adam`, `#matrix sensing`

---

<a id="item-11"></a>
## [CPU 去优化项目发现最慢 x86 指令：耗时 1980 亿周期](https://www.reddit.com/r/programming/comments/1vmhj23/hardware_researcher_spins_up_cpu_deoptimization/) ⭐️ 8.0/10

一位硬件研究员发起了“CPU 去优化”项目，旨在找出最慢的单条 x86 指令，结果发现一条指令耗时 1980 亿个周期，相当于执行 62 秒。该项目还编制了一个“耻辱堂”，收录了众所周知的慢速指令。 该项目揭示了 x86 指令令人惊讶的性能特征，可为性能工程和编译器设计提供参考。它挑战了人们对指令效率的假设，并可能为软件开发带来更好的优化策略。 最慢的指令耗时 1980 亿个周期，在典型的 3.2 GHz 时钟频率下相当于约 62 秒。该项目可能使用诸如时间戳计数器（RDTSC）之类的精确计时方法来测量周期数，并将发现汇编成公开的“耻辱堂”列表。

reddit · r/programming · /u/masiroo · 8月12日 15:34

**背景**: x86 指令的执行时间差异很大，受微码、内存访问和流水线停顿等因素影响。通常使用 Agner Fog 的指令表和 TSC 等工具来测量指令延迟。该项目反其道而行之，专注于最慢的指令而非最快的指令，以突出潜在的性能陷阱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Time_Stamp_Counter">Time Stamp Counter - Wikipedia</a></li>
<li><a href="https://www.agner.org/optimize/instruction_tables.pdf">Introduction Page 1 4. Instruction tables By Agner Fog</a></li>
<li><a href="https://stackoverflow.com/questions/692718/how-many-cpu-cycles-are-needed-for-each-assembly-instruction">How many CPU cycles are needed for each assembly instruction? Code sample</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能包含对极端周期数的惊叹，以及对其在实际代码中影响的辩论。一些人可能质疑测量方法，或指出这类慢速指令在实践中很少使用，而另一些人则欣赏该项目的教育价值。

**标签**: `#x86`, `#CPU`, `#performance`, `#hardware`, `#instruction set`

---

<a id="item-12"></a>
## [林纳斯·托瓦兹解释 Linux 的速度与设计原则](https://www.reddit.com/r/programming/comments/1vmoddq/linus_torvalds_explains_what_makes_linux_so_fast/) ⭐️ 8.0/10

林纳斯·托瓦兹在 Reddit 上分享了他对 Linux 快速运行的设计和工程原则的见解。他强调简单性、良好的数据结构和避免不必要的复杂性的重要性。 这次讨论提供了来自 Linux 创始人的罕见直接见解，为开发者和系统设计者提供了宝贵的指导。理解这些原则有助于改进其他软件项目的性能，并加深对 Linux 架构的欣赏。 托瓦兹强调，Linux 的速度源于对常见情况的关注、高效的算法，以及在存在更好替代方案时愿意改变设计的意愿。他还强调了性能分析和测量在指导优化工作中的重要性。

reddit · r/programming · /u/Rechenplaner · 8月12日 19:40

**背景**: Linux 是一个广泛使用的开源操作系统内核，以其性能和可靠性著称。其设计选择，如单内核和对简单性的关注，经过数十年的争论和优化。托瓦兹的评论为这些选择背后的哲学提供了难得的见解。

**社区讨论**: Reddit 上的讨论可能包含开发者的技术评论，许多人同意简单性和性能分析的重要性。有些人可能会争论具体的权衡，但总体情绪似乎是积极的，并对托瓦兹的直接参与表示赞赏。

**标签**: `#Linux`, `#performance`, `#kernel`, `#Linus Torvalds`, `#systems`

---

<a id="item-13"></a>
## [你从未听说过的最快双精度转字符串算法](https://www.reddit.com/r/programming/comments/1vm65dm/the_fastest_doubletostring_algorithm_youve_never/) ⭐️ 8.0/10

Reddit 上的一篇帖子介绍了一种鲜为人知的算法“yy”，用于将双精度浮点数转换为字符串，据报道其性能优于 Schubfach 等现有方法。该算法仅使用一次预计算 10 的幂的乘法，因此比经典方法更快。 双精度转字符串是许多系统（如 JSON 序列化、日志记录和数据库输出）中性能关键的操作。更快的算法可以显著提高处理大量浮点数据的应用程序的吞吐量。 该算法在 vitaut 的博客文章中有详细说明，完全使用固定宽度整数运算，并且仅使用一次预计算 10 的幂的乘法，而经典的 Schubfach 需要两到三次。基准测试结果显示，yy 每次转换耗时 16.61 纳秒，而 Schubfach 为 34.58 纳秒。

reddit · r/programming · /u/mttd · 8月12日 06:25

**背景**: 双精度转字符串是将 64 位 IEEE-754 浮点数转换为其十进制字符串表示的过程。挑战在于生成最短的字符串，使其能够往返转换回原始的二进制值，这对于准确的数据表示至关重要。传统的算法如 Schubfach 和 Errol 被用于各种库中，但“yy”算法通过将舍入区间与十进制网格相交，提供了一种更高效的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vitaut.net/posts/2026/yy-dtoa/">The fastest double-to-string algorithm you’ve never heard of</a></li>
<li><a href="https://lobste.rs/s/vzza5g/fastest_double_string_algorithm_you_ve">The fastest double-to-string algorithm you’ve never heard of | Lobsters</a></li>
<li><a href="https://github.com/miloyip/dtoa-benchmark">GitHub - miloyip/dtoa-benchmark: C++ double-to-string conversion benchmark · GitHub</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论包括专家评论和验证，用户注意到性能改进并讨论算法的实现细节。一些用户质疑某些库从 Schubfach 切换到 yy 的决定，因为速度差异显著。

**标签**: `#algorithms`, `#performance`, `#floating-point`, `#optimization`, `#programming`

---

<a id="item-14"></a>
## [Zed 推出 Delta 多人协作编程环境](https://zed.dev/blog/introducing-delta) ⭐️ 7.0/10

Zed 推出了 Delta，这是一个用于与智能体协作编程并审查其工作的多人环境，并邀请用户参与私人测试。该功能支持实时协作对话，并将对话视为文档，允许在智能体交互中进行内联评论。 Delta 可能通过让团队在编辑器内实时协作，重塑协作开发工作流程，从而减少对独立代码审查工具的需求。它还引发了关于多用户编辑和 AI 生成摘要价值的讨论，反映了 AI 辅助开发的更广泛行业趋势。 Delta 目前处于私人测试阶段，其底层技术 DeltaDB 预计将开源。该功能基于 Zed 现有的 AI 智能体能力，包括 2026 年推出的并行智能体，旨在提供更集成的协作体验。

hackernews · khy · 8月12日 18:19 · [社区讨论](https://news.ycombinator.com/item?id=49276574)

**背景**: Zed 是一款高性能代码编辑器，使用名为 GPUI 的 Rust UI 框架构建，由 Atom 背后的团队开发。它因其速度和内置 AI 功能而受到关注，Delta 代表了将协作和 AI 驱动的工作流程直接集成到编辑器中的重要一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zed.dev/blog/introducing-delta">Introducing Delta — Zed 's Blog</a></li>
<li><a href="https://sesamedisk.com/what-is-zed-deltadb-features/">What Is Zed DeltaDB and Its Key Features - Sesame Disk</a></li>
<li><a href="https://runtimewire.com/article/zed-deltadb-version-control-agent-conversations">Nathan Sobo's Zed takes aim at pull requests with... - RuntimeWire</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些人质疑多用户编辑的实际价值，称编码是“单人游戏”，而另一些人则看到在指导和审查 AI 生成工作方面的潜力。对 AI 摘要的担忧包括冗长和遗漏边缘情况，一些用户还抱怨博客文章的低对比度设计。

**标签**: `#Zed`, `#code editor`, `#collaborative editing`, `#AI`, `#developer tools`

---

<a id="item-15"></a>
## [企业从 AI 辅助转向智能体执行](https://openai.com/index/how-enterprises-put-ai-to-work) ⭐️ 7.0/10

OpenAI 的研究强调，企业正从使用 AI 进行辅助转向部署智能体 AI（agentic AI）来执行任务，并采用 ChatGPT 和 Codex 等工具。据报道，前沿企业正在 AI 采用方面领先，获得竞争优势。 这一转变标志着企业 AI 的一个重要趋势，自主智能体可以处理超出简单聊天的复杂任务，可能改变工作流程并提高生产力。它强调了采用智能体 AI 以保持竞争力的战略重要性，影响 AI 从业者、商业领袖和更广泛的技术生态系统。 该研究特别提到 ChatGPT 和 Codex 是这一转变中的关键工具，其中 Codex 是一个自动化软件工程任务的 AI 编码智能体。研究结果表明，智能体 AI 的早期采用者正在获得可衡量的优势，但摘要中未披露具体指标。

rss · OpenAI Blog · 8月12日 06:00

**背景**: 智能体 AI（agentic AI）指的是能够在有限监督下自主行动以实现目标的 AI 系统，它们使用工具并适应环境以完成任务。与仅响应提示的传统聊天机器人不同，智能体 AI 可以规划并执行多步骤流程。OpenAI 的 Codex 于 2025 年 4 月发布，是此类智能体的一个例子，专为编码任务设计。这项研究反映了更广泛的行业趋势，即企业正从 AI 作为副驾驶转向 AI 作为自主工作者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is agentic AI? - IBM</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#enterprise AI`, `#agentic AI`, `#AI adoption`, `#OpenAI`, `#ChatGPT`

---