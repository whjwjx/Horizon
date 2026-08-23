---
layout: default
title: "Horizon Summary: 2026-08-23 (ZH)"
date: 2026-08-23
lang: zh
---

> 从 43 条内容中筛选出 12 条重要资讯。

---

1. [Linus Torvalds 称赞 AI 帮助调试 Linux 内核错误](#item-1) ⭐️ 8.0/10
2. [Uber 因自动暂停司机账户面临近 10 亿美元 GDPR 罚款](#item-2) ⭐️ 8.0/10
3. [前沿 AI 实验室缺乏公开的失控模型遏制计划](#item-3) ⭐️ 8.0/10
4. [Anthropic 顶级 AI 模型遇冷，更便宜替代品受青睐](#item-4) ⭐️ 7.0/10
5. [Fable 模型高成本促使 AI 任务分配策略调整](#item-5) ⭐️ 7.0/10
6. [编码代理：指导与验证，而非仅仅审查](#item-6) ⭐️ 7.0/10
7. [Waymo 定制芯片驱动自动驾驶出租车雄心](#item-7) ⭐️ 7.0/10
8. [AI 训练使用受版权保护的书籍：法律灰色地带](#item-8) ⭐️ 7.0/10
9. [DeepMind 校友创立的 Inherent 公司称其 AI 代理 Faraday 在研究复现上超越 Anthropic 和 OpenAI](#item-9) ⭐️ 7.0/10
10. [OpenAI 转变立场，敦促加州加强 AI 安全法案 SB 53](#item-10) ⭐️ 7.0/10
11. [美国电池初创公司通过 5 亿美元能源部拨款找到国防生命线](#item-11) ⭐️ 7.0/10
12. [迈克尔·波兰斯基用活体人类皮肤训练 AI 以发现护肤成分](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Linus Torvalds 称赞 AI 帮助调试 Linux 内核错误](https://simonwillison.net/2026/Aug/22/linus-torvalds/) ⭐️ 8.0/10

Linus Torvalds 公开承认，在调试 Intel Xe 图形驱动（特别是 Battlemage G21 显卡）中一个棘手的 Linux 内核问题时，AI 提供了巨大帮助。AI 承担了大量基础工作，添加调试代码并分析结果，尽管它最初宣称该问题无法解决。 Torvalds 这样备受尊敬的人物的认可，凸显了 AI 在复杂软件开发中日益增长的作用，可能鼓励在内核和系统编程中更广泛地采用 AI。这也强调了 AI 工具的协作潜力，即使它们表现出悲观情绪，只要人类坚持，仍能发挥作用。 调试过程涉及 24 个调试补丁和 18 次内核启动，以隔离导致 GDM 无限重启的错误。Torvalds 指出，AI 多次表示问题无法解决，但在他的推动下，AI 忠实地添加调试代码并分析结果，他甚至让 AI 撰写了提交信息。

rss · Simon Willison · 8月22日 21:04

**背景**: 该错误位于 drm/xe 驱动中，该驱动负责 Linux 内核中的 Intel 图形处理。修复提交 818bebeb63dd 阻止了将扁平 CCS 存储作为可用 VRAM 分配，解决了内存损坏问题。Torvalds 的评论是在提交信息中做出的，这是对 AI 在内核开发中作用的罕见且显著的认可。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linus-Torvalds-Debug-AI">Linus Torvalds Endures A Debug Session From Hell, "Enormously Helped" By AI - Phoronix</a></li>
<li><a href="https://it.slashdot.org/story/26/08/21/1742239/linus-torvalds-endures-a-debug-session-from-hell-enormously-helped-by-ai">Linus Torvalds Endures A Debug Session From Hell, 'Enormously Helped' By AI - Slashdot</a></li>
<li><a href="https://itsfoss.com/news/torvalds-used-ai-fix-kernel-bug/">Linux Creator Linus Torvalds Just Used AI to Fix a Kernel Bug</a></li>

</ul>
</details>

**社区讨论**: 社区讨论（如 Phoronix 和 Slashdot 上的）总体持积极态度，许多人称赞 Torvalds 对使用 AI 的开放态度，并指出其实际好处。一些评论者调侃 AI 的悲观情绪，而其他人则讨论 AI 在内核开发中的影响，少数人对 AI 在关键系统中的可靠性表示怀疑。

**标签**: `#AI-assisted development`, `#Linux kernel`, `#debugging`, `#Linus Torvalds`

---

<a id="item-2"></a>
## [Uber 因自动暂停司机账户面临近 10 亿美元 GDPR 罚款](https://techcrunch.com/2026/08/23/uber-faces-fine-of-nearly-1b-over-automated-driver-suspensions/) ⭐️ 8.0/10

荷兰数据保护局对 Uber 处以 8.25 亿欧元（约合 9.66 亿美元）的罚款，原因是 Uber 在 2020 年至 2022 年间未经人工审查自动暂停司机账户。这是 GDPR 历史上第二高的罚款，仅次于 2023 年 Meta 的 12 亿欧元罚款。 这一裁决强调了 GDPR 对完全自动化决策的严格限制，此类决策对个人有重大影响，为企业在自动化决策中必须加入人工监督和申诉机制树立了先例。它标志着监管机构对各行各业 AI 驱动系统的审查加强，不仅影响网约车行业，也影响任何使用自动化决策的企业。 该罚款源于 170 名法国司机的投诉，他们被自动化系统暂停账户而未经人工审查。Uber 计划对裁决提出上诉，此次罚款是 GDPR 历史上第二高的罚款，仅次于 2023 年 Meta 的 12 亿欧元罚款。

rss · TechCrunch · 8月23日 19:30

**背景**: 《通用数据保护条例》（GDPR）是欧盟的一项全面数据保护法律，限制对个人有重大影响的完全自动化决策，要求有意义的人工监督和申诉权。Uber 在 2020 年至 2022 年间使用的自动暂停司机账户系统据称缺乏这些保障，导致荷兰数据保护局采取行动。荷兰监管机构此前曾因数据保留问题对 Uber 罚款 1000 万欧元，显示出监管执法的连续性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hokanews.com/2026/08/uber-hit-with-963-million-gdpr-fine.html">Uber Hit With $963 Million GDPR Fine Over Automated Driver Account Suspensions | Hokanews</a></li>
<li><a href="https://www.omegatechnologysolutionsgroupinc.com/blog/uber-faces-966m-gdpr-fine-for-automated-driver-suspensions-54af76">Uber faces $966M GDPR fine for automated driver suspensions · Omega</a></li>
<li><a href="https://startupfortune.com/dutch-regulator-fines-uber-nearly-1-billion-over-automated-driver-suspensions/">Dutch Regulator Fines Uber Nearly $1 Billion Over Automated Driver Suspensions - Startup Fortune</a></li>

</ul>
</details>

**标签**: `#GDPR`, `#Uber`, `#regulatory`, `#automated systems`, `#data protection`

---

<a id="item-3"></a>
## [前沿 AI 实验室缺乏公开的失控模型遏制计划](https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/) ⭐️ 8.0/10

Guidelight AI Standards 的一项新研究显示，包括 OpenAI、Anthropic、Google、Meta 和 xAI 在内的领先 AI 实验室，很少有公开记录的遏制失控 AI 模型的计划。该研究对这些实验室的准备情况进行了评分，其中 OpenAI 得分最高，而 Anthropic 和 Meta 得分最低。 这之所以重要，是因为随着 AI 系统能力增强并偶尔表现出意外或危险行为，缺乏公开的遏制计划引发了对准备情况和问责制的严重担忧。它凸显了 AI 安全和治理方面的关键缺口，可能对公众信任和监管监督产生重大影响。 Guidelight 将遏制计划定义为“当检测到 AI 试图颠覆控制时触发的预先指定计划”，涵盖要撤销的权限、谁可以继续操作、约束条件以及何时将模型完全离线。该研究对五家实验室进行了评分，OpenAI 得分最高，Anthropic 和 Meta 得分最低，但未披露具体分数。

rss · TechCrunch · 8月22日 16:00

**背景**: 失控 AI 模型是指行为违背其预期目的、可能试图颠覆人类控制的 AI 系统。遏制计划对于减轻此类模型的风险至关重要，因为它们概述了限制伤害的具体行动。Guidelight AI Standards 是一家致力于促进安全前沿 AI 发展的组织，其研究强调了该行业目前在这一领域缺乏透明度的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/">Frontier AI labs still won't say how they'd contain a rogue model | TechCrunch</a></li>
<li><a href="https://cryptobriefing.com/frontier-ai-labs-rogue-model-containment/">Study reveals frontier AI labs lack plans to contain rogue models</a></li>
<li><a href="https://cryptorank.io/news/feed/218e2-frontier-ai-labs-containment-plans">Frontier AI labs still won’t say how they’d contain a rogue model | AI News ai safety | CryptoRank.io</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#frontier AI`, `#rogue AI`, `#AI governance`, `#AI labs`

---

<a id="item-4"></a>
## [Anthropic 顶级 AI 模型遇冷，更便宜替代品受青睐](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 7.0/10

据英国《金融时报》报道，Anthropic 在 2026 年 7 月的年化收入达到 650 亿美元，高于 5 月的 470 亿美元；而 OpenAI 的年化收入在季度内增长 35%，超过 400 亿美元。尽管 Anthropic 于 7 月 24 日发布了旗舰模型 Opus 5，但模型采用数据显示其落后于更旧、更便宜的模型。 这凸显了 AI 行业的一个关键竞争动态：如果定价过高，仅靠尖端性能可能无法推动采用。这表明对价格敏感的客户更青睐更便宜的模型，这可能会影响 AI 公司如何定价和定位其产品。 Ramp AI 指数 2026 年 7 月数据显示，Opus 4.8 以 28.0% 的支出占比领先，而新发布的 Opus 5 仅占 3.5%。Anthropic 预计第三季度将实现盈利，并拥有 6000 个年消费 10 万美元以上的客户。

rss · Simon Willison · 8月23日 20:24

**背景**: 年化收入是一种将当前月收入推算至全年的指标，用于反映公司的增长轨迹。Ramp AI 指数通过分析使用 Ramp 公司卡的 7 万多家企业的账单数据，衡量 AI 的采用和支出情况，从而洞察企业实际使用哪些 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/a/annualized-income.asp">Annualized Income: Definition, Formula, and Example</a></li>
<li><a href="https://ramp.com/data/ai-index">Ramp AI Index</a></li>

</ul>
</details>

**标签**: `#AI industry`, `#Anthropic`, `#OpenAI`, `#revenue`, `#market trends`

---

<a id="item-5"></a>
## [Fable 模型高成本促使 AI 任务分配策略调整](https://simonwillison.net/2026/Aug/23/drew-breunig/) ⭐️ 7.0/10

Drew Breunig 指出，Anthropic 的 Fable 模型成本高昂，正促使开发者更谨慎地在昂贵与较便宜的 AI 模型（如 Opus、5.6、K3 和 GLM）之间分配任务。 这一转变标志着 AI 行业日趋成熟，成本优化变得与能力同等重要，影响开发者如何构建 AI 驱动的工作流程并管理预算。它反映了在 AI 采用中平衡性能与经济效率的更广泛趋势。 Breunig 指出，在 Fable 之前，过度投入编码工具或上下文策略显得愚蠢，因为新模型会以相同或更低价格出现并解决大部分问题。然而，Fable 的卓越质量但高昂成本使得 Opus 和其他模型对大多数编码需求“足够好”，从而促使更审慎的工作分配。

rss · Simon Willison · 8月23日 19:55

**背景**: Anthropic 于 2026 年 6 月发布了 Claude Fable 5 和 Claude Mythos 5，其中 Fable 5 在几乎所有基准测试中达到最先进水平，但定价为每百万输入 token 10 美元、每百万输出 token 50 美元。Opus 是 Anthropic 最智能的模型，适用于代理式编码和复杂推理，而 GLM 是中国公司 Z.ai 开发的开源权重模型系列。这段引言反映了面对前沿 AI 模型经济现实时的实际应对。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#cost optimization`, `#Anthropic`, `#Claude`

---

<a id="item-6"></a>
## [编码代理：指导与验证，而非仅仅审查](https://simonwillison.net/2026/Aug/22/more-than-just-code-review/) ⭐️ 7.0/10

西蒙·威利森认为，高效使用编码代理的关键技能是自信地指导它们并进行更改验证，这不一定需要逐行审查代码。 这一观点将焦点从逐行代码审查转向更高层次的验证策略，随着 AI 辅助开发的普及，这一点至关重要。它可能改变开发者在 AI 驱动工作流中处理质量保证的方式。 威利森指出，逐行检查代码从来不是验证更改的最有效方式。他建议采用替代验证方法，如运行测试或检查行为，作为更高效的途径。

rss · Simon Willison · 8月22日 15:56

**背景**: 编码代理是根据指令自主编写或修改代码的 AI 工具。代理工程是一个新兴学科，它编排此类代理，同时由人类提供监督。传统的代码审查涉及人工检查，但随着 AI 代理的出现，需要新的验证范式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-engineering-from-code-workflows-regie-san-juan-sjyyc">Agentic Engineering : From Code to Workflows</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#code-review`, `#AI`, `#software-engineering`, `#LLMs`

---

<a id="item-7"></a>
## [Waymo 定制芯片驱动自动驾驶出租车雄心](https://techcrunch.com/2026/08/23/techcrunch-mobility-the-custom-chip-driving-waymos-robotaxi-ambitions/) ⭐️ 7.0/10

Waymo 首次透露，其为自动驾驶出租车设计了定制的 5nm AI 芯片，用于处理来自摄像头、激光雷达和雷达的传感器数据，取代了之前的 Intel FPGA。该芯片提供超过 1000 TOPS 的 AI 处理能力，用于实时传感器处理。 这标志着自动驾驶汽车硬件领域的重大转变，Waymo 与 Tesla 一起开发定制芯片以提升性能和可扩展性。定制芯片可以降低成本并提高效率，可能加速自动驾驶出租车车队的部署，并塑造自动驾驶领域的竞争格局。 该芯片采用 5nm 工艺制造，设计用于实时处理来自多种传感器类型的原始数据。Waymo 与外部芯片制造商合作生产该芯片，它是公司下一代自动驾驶系统的一部分。

rss · TechCrunch · 8月23日 16:03

**背景**: 自动驾驶汽车依赖快速处理传感器数据来做出驾驶决策。此前，Waymo 使用 Intel FPGA 来完成这项任务，但定制芯片提供了更好的性能和能效。这一趋势与 Tesla 采用自家 AI 芯片的做法相似，凸显了硬件专业化在自动驾驶技术商业化竞赛中的重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://autos.yahoo.com/ev-and-future-tech/articles/waymo-builds-custom-chip-robotaxi-173117486.html">Waymo builds custom chip for robotaxi fleet</a></li>
<li><a href="https://www.benzinga.com/markets/tech/26/08/61350963/waymo-unveils-first-custom-robotaxi-chip-with-more-than-1000-tops-of-ai-processing-power">Waymo Unveils First Custom Robotaxi Chip With More... - Benzinga</a></li>
<li><a href="https://www.techrepublic.com/article/news-waymo-custom-ai-chips-robotaxis/">Alphabet's Waymo Unveils Custom Silicon to Power Its Next-Gen...</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#Waymo`, `#custom silicon`, `#robotaxi`, `#AI hardware`

---

<a id="item-8"></a>
## [AI 训练使用受版权保护的书籍：法律灰色地带](https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/) ⭐️ 7.0/10

文章讨论了在未经作者同意的情况下，使用受版权保护的书籍训练 AI 模型是否合法的持续法律和伦理争论，强调了问题的复杂性和缺乏明确法律先例的现状。 这一问题影响作者、AI 公司以及整个创意产业，因为此类法律斗争的结果可能为 AI 模型的训练方式以及创作者是否获得补偿树立先例。同时，它也影响公众对 AI 发展的信任和监管态度。 文章指出，合理使用是核心法律概念，但其在 AI 训练中的应用仍不确定。最近的案例，如 Bartz 诉 Anthropic 案，区分了训练中的合理使用与保留盗版副本的侵权，表明合法性可能取决于具体情况。

rss · TechCrunch · 8月23日 15:00

**背景**: AI 模型，尤其是大型语言模型（LLM），需要大量文本数据进行训练，这些数据通常来自互联网或数字化书籍。版权法，特别是美国的合理使用原则，允许在未经许可的情况下有限使用受版权保护的材料，但 AI 训练是否属于变革性合理使用仍是一个有争议的问题。缺乏针对文本和数据挖掘的具体立法增加了不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://distillation.technology/learn/is-ai-training-fair-use">Is AI Training Fair Use? What Bartz v. Anthropic Actually</a></li>
<li><a href="https://www.linkedin.com/pulse/legal-uncertainty-over-ai-training-copyrighted-content-savneet-singh-fj2me">Legal Uncertainty Over AI Training on Copyrighted Content and its...</a></li>
<li><a href="https://www.linkedin.com/pulse/judge-alsup-gets-right-ai-training-fair-use-sound-legal-tredennick-rt1fc">Judge Alsup Gets It Right: AI Training as Fair Use Represents Sound...</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#copyright`, `#legal`, `#machine learning`, `#publishing`

---

<a id="item-9"></a>
## [DeepMind 校友创立的 Inherent 公司称其 AI 代理 Faraday 在研究复现上超越 Anthropic 和 OpenAI](https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/) ⭐️ 7.0/10

总部位于伦敦、由 DeepMind 校友创立的 AI 实验室 Inherent 发布了 AI 代理 Faraday，据称其在复现科学论文方面超越了 Anthropic 的 Claude Opus 4.8 和 OpenAI 的模型。该公司声称 Faraday 以远小于大型模型的规模实现了这一成绩。 这一进展可能通过自动化研究复现（验证发现的关键步骤）加速科学发现。同时，它也凸显了小型、专业化 AI 代理与行业巨头竞争的潜力，可能重塑 AI 研究的竞争格局。 Faraday 的性能部分归功于其使用强化学习，这是一种不同于大型模型的训练方法。Inherent 的长期目标是开发一个能够跨科学领域运作的 AI 科学家代理，而非局限于单一基准或学科。

rss · TechCrunch · 8月22日 19:00

**背景**: 复现科学论文涉及重现现有研究的实验、数据和发现，这对于验证声明和在前人工作基础上继续研究至关重要。像 Faraday 这样的 AI 代理旨在自动化这一过程，可能减少手动复现所需的时间和精力。这一声明之所以引人注目，是因为它来自一家小型初创公司，挑战了像 Anthropic 和 OpenAI 这样规模更大、资金更充足的实验室。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vmtech.rs/en/instagram-insights/inherent-faraday-research-agent">Inherent Faraday AI research replication — VMTech</a></li>
<li><a href="https://chang.aevumnews.com/en/inherent-deepmind-alumni-s-ai-teammate-outperforms-giants-in-research-replication">Inherent : DeepMind Alumni 's AI 'Teammate' Outperforms Giants in.....</a></li>
<li><a href="https://creati.ai/ai-news/2026-08-22/inherent-says-its-faraday-ai-agent-beat-anthropic-and-openai-at-replicating-research/">Inherent says its Faraday AI agent beat Anthropic and OpenAI at...</a></li>

</ul>
</details>

**标签**: `#AI`, `#research`, `#DeepMind`, `#scientific discovery`, `#agent`

---

<a id="item-10"></a>
## [OpenAI 转变立场，敦促加州加强 AI 安全法案 SB 53](https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/) ⭐️ 7.0/10

OpenAI 已逆转其先前反对立场，现呼吁加州立法者加强 AI 安全法案 SB 53。该公司特别敦促进行修正，要求在 AI 模型训练期间实施持续监控并加强网络安全。 这一转变标志着 OpenAI 在 AI 监管态度上的重大调整，承认某种形式的约束性监管可能是不可避免的。这可能影响 SB 53 的通过，并为美国 AI 治理树立先例，尤其是考虑到加州作为硅谷所在地的角色。 SB 53 由参议员 Scott Wiener 提出，并由 Encode AI、Economic Security Action California 和 Secure AI Project 共同发起。州长 Gavin Newsom 已签署该法案成为法律，要求 AI 公司披露大规模前沿模型的安全信息。OpenAI 提出的修正案侧重于训练期间的持续监控和加强网络安全。

rss · TechCrunch · 8月22日 16:30

**背景**: 加州一直处于 AI 监管努力的前沿。去年，州长 Newsom 在 AI 公司的强烈游说下否决了更广泛的 AI 安全法案 SB 1047。SB 53 代表了一种更有针对性的方法，侧重于前沿模型的披露要求。OpenAI 的转变反映了对高级 AI 风险日益增长的担忧以及对监管清晰度的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sd11.senate.ca.gov/news/senator-wieners-landmark-responsible-ai-innovation-bill-advances-final-vote">Senator Wiener’s Landmark Responsible AI Innovation Bill Advances...</a></li>
<li><a href="https://businessnoon.com/california-signs-landmark-ai-safety-bill-sb-53/">California ’s Bold AI Safety Bill SB 53 Changes the Game</a></li>
<li><a href="https://www.kron4.com/hill-politics/newsom-signs-first-in-the-nation-ai-safety-disclosures-law/433/">Gavin Newsom signs SB 53 , enacting California AI safety bill</a></li>
<li><a href="https://semasocial.com/blog/openai-is-calling-for-california-to-strengthen-sb-53-an-ai-safety-bill-that-the-company-previously-opposed">OpenAI Now Supports California AI Safety Bill SB 53 - semasocial.com</a></li>
<li><a href="https://azat.tv/en/openai-california-sb53-ai-safety-law-amendments/">OpenAI Urges California to Strengthen Frontier Model Safety Rules...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#regulation`, `#California`, `#policy`

---

<a id="item-11"></a>
## [美国电池初创公司通过 5 亿美元能源部拨款找到国防生命线](https://techcrunch.com/2026/08/22/us-battery-startups-have-found-a-lifeline-in-defense/) ⭐️ 7.0/10

美国电池初创公司从能源部获得了 5 亿美元的拨款，在电动汽车激励措施被削减后提供了财务生命线。这笔资金是向无人机、基地和下一代车辆的国防合同战略转向的一部分。 这一发展意义重大，因为它有助于在汽车需求崩溃的情况下维持美国电池产业，可能将该行业的重点转向国家安全应用。这也凸显了政府资金被重新导向国防相关技术的更广泛趋势。 这些拨款支持从事固态电池和用于弹药及高超音速系统的热电池的初创公司，这些领域是传统锂离子电池的短板。此外，一些初创公司正在吸引与国防供应商 ADS 有关联的 ADS Ventures 等投资者，表明电池与国防领域之间的联系日益紧密。

rss · TechCrunch · 8月22日 15:20

**背景**: 2026 年初，国会削减了电动汽车税收抵免和消费者激励措施，导致汽车电池需求崩溃。这迫使美国电池初创公司寻求替代市场，国防合同成为稳定的收入来源。能源部的拨款是加强国内电池制造和国家安全的更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androguider.com/2026/08/defense-lifeline-how-500m-in-doe-grants.html">Defense Lifeline: How $500M in DOE Grants Are Saving US Battery ...</a></li>
<li><a href="https://www.techbuzz.ai/articles/us-battery-startups-score-500m-defense-lifeline-after-ev-cuts">US Battery Startups Score $500M Defense Lifeline... | The Tech Buzz</a></li>
<li><a href="https://mezha.net/eng/bukvy/b820c632_us_battery_startups/">US Battery Startups Turn to Defense After EV Incentives... - #Mezha</a></li>

</ul>
</details>

**标签**: `#batteries`, `#energy storage`, `#defense`, `#government funding`, `#startups`

---

<a id="item-12"></a>
## [迈克尔·波兰斯基用活体人类皮肤训练 AI 以发现护肤成分](https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/) ⭐️ 7.0/10

迈克尔·波兰斯基的 AI 驱动初创公司一直在悄悄开发一项技术，能在体外让活体人类皮肤组织存活数周，现在才公开这一信息。该公司利用这种活体组织训练 AI 模型，以发现新的护肤化合物。 这代表了 AI 与生物技术的新颖结合，可能通过提供比传统方法更符合生理学的测试平台，加速护肤和药物发现。它可能影响化妆品和制药行业，减少对动物试验的依赖，并提高新化合物的功效。 该技术涉及人类皮肤组织的离体培养，这是一种在体外长时间维持组织活力的技术。该初创公司的方法可能使用气液界面培养或类似方法来保持组织存活，然后应用 AI 分析对潜在化合物的反应。

rss · TechCrunch · 8月22日 01:31

**背景**: 离体人类皮肤培养是生物医学研究中一项成熟的技术，在实验室中保持皮肤样本存活以研究皮肤生物学和测试治疗方法。AI 驱动的药物发现是一个不断发展的领域，利用机器学习识别有前景的化合物，但将其与活体人类组织结合是一种相对较新的方法。这可能更准确地预测化合物在人体内的行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.academia.edu/92848865/Dynamic_Physiological_Culture_of_Ex_Vivo_Human_Tissue_A_Systematic_Review">(PDF) Dynamic Physiological Culture of Ex Vivo Human Tissue ...</a></li>
<li><a href="https://www.researchgate.net/figure/Ex-Vivo-Culture-Platforms-for-healthy-and-HS-skin-Schematics-of-three-ex-vivo-culture_fig2_355224937">Ex Vivo Culture Platforms for healthy and HS skin . Schematics of...</a></li>

</ul>
</details>

**标签**: `#AI`, `#biotech`, `#skincare`, `#startup`, `#drug discovery`

---