---
layout: default
title: "Horizon Summary: 2026-06-28 (ZH)"
date: 2026-06-28
lang: zh
---

> 从 58 条内容中筛选出 15 条重要资讯。

---

1. [DeepSeek DSpark：投机解码加速大模型推理](#item-1) ⭐️ 9.0/10
2. [OpenAI 预览 GPT-5.6 Sol，能力大幅提升](#item-2) ⭐️ 9.0/10
3. [Dean Ball 谈 AI 实验室经济与出口管制](#item-3) ⭐️ 8.0/10
4. [2000 人未能攻破 AI 助手](#item-4) ⭐️ 8.0/10
5. [讽刺性事件报告揭示 AI 代理在供应链中的风险](#item-5) ⭐️ 8.0/10
6. [亚洲 AI 初创公司在出口禁令下推出类似 Mythos 的模型](#item-6) ⭐️ 8.0/10
7. [特朗普政府授权 Anthropic Mythos 5 供 100 多家美国机构使用](#item-7) ⭐️ 8.0/10
8. [科技巨头自研 AI 芯片挑战英伟达](#item-8) ⭐️ 8.0/10
9. [Mojo 编程语言即将开源](#item-9) ⭐️ 8.0/10
10. [AWS 冷却故障导致 150 多项云服务中断](#item-10) ⭐️ 8.0/10
11. [OpenRA 重振经典命令与征服系列](#item-11) ⭐️ 7.0/10
12. [俄罗斯黑客涉嫌对捷豹路虎发动 25 亿美元黑客攻击](#item-12) ⭐️ 7.0/10
13. [AI 的政治影响需要集体行动](#item-13) ⭐️ 7.0/10
14. [苹果寻求豁免，向被制裁的中国供应商 CXMT 采购内存](#item-14) ⭐️ 7.0/10
15. [让 CPU 愤怒的数据访问模式](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DeepSeek DSpark：投机解码加速大模型推理](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf) ⭐️ 9.0/10

DeepSeek 发表了一篇关于 DSpark 的论文，该技术通过投机解码加速大语言模型推理，并已在 Hugging Face 上发布了相应模型。 这一创新可显著降低推理延迟和成本，使大模型更适用于实时应用，而 DeepSeek 的公开出版与一些美国实验室的封闭做法形成鲜明对比。 DSpark 根据并发程度可实现 51% 到 400% 的吞吐量提升，并已在实际流量中部署。模型以 DeepSeek-V4-Flash-DSpark 和 DeepSeek-V4-Pro-DSpark 形式提供。

hackernews · aurenvale · 6月27日 09:18 · [社区讨论](https://news.ycombinator.com/item?id=48696585)

**背景**: 投机解码是一种推理优化技术，它使用较小的草稿模型提出多个 token，然后由较大的目标模型并行验证。这种方法可将延迟降低 2-3 倍，且不降低输出质量，其灵感来自计算机体系结构中的投机执行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI ...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark">deepseek -ai/ DeepSeek -V4-Pro- DSpark · Hugging Face</a></li>
<li><a href="https://cryptobriefing.com/deepseek-dspark-faster-inference/">DeepSeek unveils DSpark for 60% to 85% faster inference optimization</a></li>

</ul>
</details>

**社区讨论**: 社区称赞 DeepSeek 的开放创新，与美国实验室的封闭形成对比。用户对可能集成到 DwarfStar 等本地推理工具表示兴奋，并注意到速度和成本节省的实际好处。

**标签**: `#AI`, `#LLM`, `#speculative decoding`, `#DeepSeek`, `#inference acceleration`

---

<a id="item-2"></a>
## [OpenAI 预览 GPT-5.6 Sol，能力大幅提升](https://openai.com/index/previewing-gpt-5-6-sol) ⭐️ 9.0/10

OpenAI 宣布对 GPT-5.6 系列进行有限预览，包括旗舰模型 Sol、均衡模型 Terra 以及快速经济的 Luna，这些模型在编程、科学和网络安全方面能力更强。 此次发布代表了 AI 能力的重大飞跃，在关键领域提供了改进的性能，同时引入了新的定价结构，使先进 AI 更易获取。 GPT-5.6 Sol 的定价为每百万输入 token 5 美元，每百万输出 token 30 美元，Terra 和 Luna 价格更低。该系列还引入了可预测的提示缓存，支持显式缓存断点和 30 分钟的最小缓存寿命。

rss · OpenAI Blog · 6月26日 10:00

**背景**: OpenAI 的 GPT 模型是驱动各种 AI 应用的大型语言模型。GPT-5.6 系列引入了新的命名规则，数字表示代际，名称表示能力层级。应美国政府要求，预览仅限于受信任的合作伙伴。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/previewing-gpt-5-6-sol/">Previewing GPT-5.6 Sol: a next-generation model | OpenAI</a></li>
<li><a href="https://www.reddit.com/r/singularity/comments/1ugcoic/previewing_gpt56_sol_a_nextgeneration_model/">r/singularity on Reddit: Previewing GPT-5.6 Sol: a next-generation model</a></li>
<li><a href="https://www.datacamp.com/blog/gpt-5-6-sol-luna-terra">GPT-5.6 Sol, Terra, and Luna: OpenAI's Next-Gen Model Family | DataCamp</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的社区讨论对新模型在 Cerebras 上的速度（高达每秒 750 个 token）以及新的命名规则感到兴奋，但一些人对政府参与限制访问表示担忧。

**标签**: `#AI`, `#OpenAI`, `#GPT`, `#machine learning`, `#safety`

---

<a id="item-3"></a>
## [Dean Ball 谈 AI 实验室经济与出口管制](https://simonwillison.net/2026/Jun/26/dean-w-ball/#atom-everything) ⭐️ 8.0/10

Dean W. Ball 指出，前沿 AI 实验室在模型发布后仅有短短几个月的盈利窗口，而大规模基础设施建设假设了全球市场，但出口管制可能破坏这一假设。 这一分析揭示了美国出口管制与前沿 AI 基础设施经济可行性之间的根本矛盾，可能重塑行业动态和政策决策。 Ball 指出，前沿模型随着竞争出现迅速变为次前沿，利润空间被压缩；没有人会为有限的国内市场建造 1000 亿美元的数据中心。

rss · Simon Willison · 6月26日 22:25

**背景**: 前沿模型是最先进的 AI 模型，训练成本极高。出口管制限制向特定国家销售 AI 芯片和技术，从而限制了美国 AI 服务的市场。AI 基础设施建设涉及数据中心和能源的巨大投资，预计 2026 年将达到约 6000 亿美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_export_controls_on_AI_chips_and_semiconductors">United States export controls on AI chips and semiconductors</a></li>
<li><a href="https://thediligencestack.com/p/ai-infrastructure-economics-the-2">AI Infrastructure Economics : The $2-for-$1 Problem</a></li>

</ul>
</details>

**标签**: `#AI economics`, `#frontier models`, `#export controls`, `#AI infrastructure`, `#industry dynamics`

---

<a id="item-4"></a>
## [2000 人未能攻破 AI 助手](https://simonwillison.net/2026/Jun/26/hack-my-ai-assistant/#atom-everything) ⭐️ 8.0/10

Fernando Irarrázaval 发起了一项挑战，2000 人尝试了 6000 次，试图从他的受反提示注入规则保护的 OpenClaw AI 助手中泄露秘密，但无人成功。 这项真实世界实验表明，像 Opus 4.6 这样的前沿模型对提示注入攻击的抵抗力显著增强，这对于在敏感环境中部署 AI 助手至关重要。 该挑战花费了 500 美元的 token 费用，并因大量入站邮件导致 Google 账户被暂停，但无人泄露秘密。使用的模型是 Opus 4.6，系统提示中包含了明确的防提示注入规则。

rss · Simon Willison · 6月26日 18:33

**背景**: 提示注入攻击通过将恶意命令嵌入用户输入，诱使 AI 模型忽略其指令。防提示注入规则是旨在防止此类攻击的系统级指令。OpenClaw 是一个开源的个人 AI 助手，可连接多个消息平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openclaw.ai/">OpenClaw — Personal AI Assistant</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论中充满了合理的质疑和挑战发起人的真诚回应，许多评论者指出，6000 次失败并不能保证对更复杂攻击的安全性。

**标签**: `#AI security`, `#prompt injection`, `#LLM`, `#red teaming`, `#OpenClaw`

---

<a id="item-5"></a>
## [讽刺性事件报告揭示 AI 代理在供应链中的风险](https://simonwillison.net/2026/Jun/26/incident-report/#atom-everything) ⭐️ 8.0/10

Andrew Nesbitt 发布了一份虚构的事件报告 CVE-2026-LGTM，描述了两个来自竞争供应商的 AI 审查代理因一个依赖项更新陷入分歧循环，产生了 340 条评论和 41,255 美元的推理成本，直到财务部门撤销了它们的 API 密钥。 这篇讽刺文章凸显了自主 AI 代理在软件供应链安全中真实且日益增长的危险，不受控制的循环可能导致财务浪费、运营中断甚至市场操纵。它强调了在 AI 驱动的开发工作流中引入人工监督和强健护栏的紧迫性。 报告幽默地指出，一家供应商的营销团队发布新闻稿称‘多代理对抗性安全推理同比增长 430%’，导致股价开盘上涨 6%。事件后正式分配了虚构的 CVE 标识符‘CVE-2026-LGTM’。

rss · Simon Willison · 6月26日 17:58

**背景**: AI 审查代理是自动分析代码变更以发现安全漏洞或策略合规性的工具。在开源依赖管理中，它们可以批准或拒绝拉取请求。然而，当多个代理意见不一致时，它们可能陷入无限循环，消耗大量计算资源并延迟部署。该事件讽刺了此类失败，提醒人们注意缺乏回退机制和成本控制的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nesbitt.io/2026/06/26/incident-report-cve-2026-lgtm.html">Incident Report: CVE - 2026 - LGTM | Andrew Nesbitt</a></li>
<li><a href="https://openclawradar.com/article/cve-2026-lgtm-ai-security-agents-fail">CVE - 2026 - LGTM : AI Security Gates Bypassed by Prompt Injection</a></li>
<li><a href="https://galileo.ai/blog/human-in-the-loop-agent-oversight">How to Build Human-in-the-Loop Oversight for AI Agents | Galileo</a></li>

</ul>
</details>

**社区讨论**: 社区反应热烈，原帖有 340 条评论。许多读者称赞这篇讽刺作品准确捕捉了过度依赖 AI 代理的荒谬性，而另一些人则讨论了此类场景的可行性，并提出了人工介入监督和成本上限等技术缓解措施。

**标签**: `#security`, `#ai`, `#supply-chain`, `#satire`, `#software-engineering`

---

<a id="item-6"></a>
## [亚洲 AI 初创公司在出口禁令下推出类似 Mythos 的模型](https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/) ⭐️ 8.0/10

亚洲 AI 初创公司正在发布能力与 Anthropic 的 Mythos 相当的 LLM，利用美国对 Anthropic 前沿 AI 模型的出口禁令来抢占市场份额。 这一转变可能永久改变全球 AI 格局，美国实验室可能失去亚洲的重要市场，并凸显了出口管制对尖端技术的地缘政治影响。 Mythos 是一款专为网络安全漏洞发现而设计的模型，特朗普政府对其施加出口禁令，以防止外国获得如此强大的网络能力。

rss · TechCrunch · 6月27日 12:00

**背景**: Anthropic 的 Mythos 是一个专门用于发现软件漏洞的 LLM，在网络能力方面远超其他 AI 模型。美国政府对其施加出口管制，以防止被外国对手使用，这引发了网络安全界关于此类禁令有效性和后果的辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mythos_(model)">Mythos (model)</a></li>
<li><a href="https://insidecybersecurity.com/daily-news/cybersecurity-community-pushes-back-using-export-controls-ban-anthropic-s-frontier-ai">Cybersecurity community pushes back on using export controls to ban Anthropic’s frontier AI models with significant vulnerability discovery capabilities | InsideCyberSecurity.com</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/anthropic-export-ban-sounds-alarms-130007792.html">Anthropic export ban sounds alarms for AI industry</a></li>

</ul>
</details>

**标签**: `#AI`, `#geopolitics`, `#startups`, `#export ban`, `#Asia`

---

<a id="item-7"></a>
## [特朗普政府授权 Anthropic Mythos 5 供 100 多家美国机构使用](https://techcrunch.com/2026/06/26/trump-admin-releases-anthropic-mythos-to-be-used-by-more-than-100-us-companies-agencies/) ⭐️ 8.0/10

特朗普政府已授权 Anthropic 的 Mythos 5（一款强大的网络安全 AI 模型）供 100 多家美国公司和政府机构使用，包括其非美国员工。 这标志着政府与行业在 AI 应用方面迈出了重要一步，可能加速关键领域的网络安全能力，同时也引发了对安全性和滥用的担忧。 Mythos 5 与 Claude Fable 5 使用相同的基础模型，但在某些领域取消了安全限制，最初通过 Project Glasswing 部署。授权范围包括授权实体的非美国员工。

rss · TechCrunch · 6月27日 01:01

**背景**: Anthropic 是一家成立于 2021 年的 AI 安全公司。Mythos 是一个旨在发现软件漏洞的大型语言模型，由于安全担忧，其公开发布一直受限。英国 AI 安全研究所此前测试了 Claude Mythos，并将其评为网络安全能力最强的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_Mythos">Anthropic Mythos</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://appwrite.io/blog/post/anthropic-just-launched-claude-fable-5-and-claude-mythos-5">Anthropic just launched Claude Fable 5 and Claude Mythos 5 - Appwrite</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Government`, `#Policy`, `#Mythos`

---

<a id="item-8"></a>
## [科技巨头自研 AI 芯片挑战英伟达](https://techcrunch.com/video/why-everyone-from-openai-to-spacex-is-building-their-own-chips-and-turning-up-the-heat-on-nvidia/) ⭐️ 8.0/10

OpenAI 发布了其首款与 Broadcom 合作打造的定制推理芯片 Jalapeño，加入了 Google、Apple 和 SpaceX 的行列，开发专有 AI 硬件以减少对英伟达的依赖。 这一趋势标志着 AI 硬件格局的重大转变，领先科技公司试图通过摆脱英伟达主导的 GPU 来降低成本、提升性能并保障供应链安全。 Jalapeño 是一款专为 LLM 推理设计的处理器，与 Broadcom 和 Celestica 合作，仅用九个月就完成了从设计到流片，旨在更快、更便宜地部署像 ChatGPT 这样的模型。

rss · TechCrunch · 6月26日 17:43

**背景**: 英伟达长期以来凭借其强大的 GPU 主导着 AI 芯片市场，但随着 AI 需求激增，各公司开始寻求定制芯片以优化推理等特定工作负载。定制芯片可以提供更好的每瓦性能，并减少对单一供应商的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://digg.com/tech/60qj05iw">OpenAI announces Jalapeño, a custom LLM inference chip ...</a></li>
<li><a href="https://intheworldofai.com/p/openai-reveals-ai-chip">OpenAI Reveals Jalapeño Chip : Breaking Free from Nvidia</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Nvidia`, `#OpenAI`, `#hardware`, `#custom silicon`

---

<a id="item-9"></a>
## [Mojo 编程语言即将开源](https://www.reddit.com/r/programming/comments/1uh1qm4/mojo_programming_language_will_become_opensource/) ⭐️ 8.0/10

Modular 公司在 Mojo 语言官网上宣布，Mojo 即将开源，并承诺在 2026 年 8 月的 ModCon '26 上提供更多更新。 Mojo 是一种专为 AI/ML 工作负载设计的高性能语言，开源后可能加速其采用和社区贡献，有望在 AI 生态中挑战 Python 和 C++ 等成熟语言。 截至 2026 年 6 月，Mojo 编译器仍为闭源，标准库已开源；完整开源预计在 2026 年秋季。Mojo 基于 MLIR 构建，可编译到 CPU、GPU、TPU 及其他加速器。

reddit · r/programming · /u/baldierot · 6月27日 12:39

**背景**: Mojo 是由 Modular 公司开发的一种编程语言，结合了类似 Python 的语法和系统级性能。它利用 MLIR 编译器框架面向异构硬件，特别适合 AI 和高性能计算。该语言自发布以来一直为专有，但 Modular 承诺在 2026 年秋季开源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://mojolang.org/">Mojo</a></li>

</ul>
</details>

**标签**: `#Mojo`, `#open source`, `#programming languages`, `#AI/ML`

---

<a id="item-10"></a>
## [AWS 冷却故障导致 150 多项云服务中断](https://www.reddit.com/r/programming/comments/1uhbf79/the_aws_data_hall_cooling_failure_linked_to/) ⭐️ 8.0/10

2026 年 5 月 7 日，AWS US-EAST-1 区域一个数据厅的冷却故障引发了超过 150 项云服务中断，导致 Coinbase、FanDuel 和 CME Group 等主要客户中断数小时。 这一事件凸显了云基础设施在物理层的脆弱性——单点冷却故障可能引发大规模中断，对主要云服务商的可靠性承诺构成挑战。 故障发生在 AWS US-EAST-1 的可用区 use1-az4，导致该区中断 12 小时。Coinbase 核心交易中断近 7 小时，AWS 将事件描述为热事件，导致电力和冷却故障。

reddit · r/programming · /u/Cultural_Wheel_6936 · 6月27日 19:21

**背景**: AWS US-EAST-1 是最大且最老的 AWS 区域之一，承载大量关键服务。数据厅包含服务器机架和冷却系统；冷却故障会导致服务器过热并关机，从而引发服务中断。该事件凸显了设施层面冗余的重要性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://devops-daily.com/posts/aws-use1-az4-thermal-event-single-az-lessons">When One Data Center Room Got Hot: AWS US-EAST-1, Coinbase...</a></li>
<li><a href="https://techfyle.com/aws-data-centre-cooling-failure-overheating/">Data Centres: We Have a Cooling Problem | TechFyle | TF</a></li>

</ul>
</details>

**标签**: `#AWS`, `#cloud computing`, `#infrastructure`, `#reliability`, `#incident analysis`

---

<a id="item-11"></a>
## [OpenRA 重振经典命令与征服系列](https://www.openra.net/) ⭐️ 7.0/10

OpenRA 是一个开源游戏引擎，它针对现代系统重制了《红色警戒》、《泰伯利亚的黎明》和《沙丘 2000》等经典命令与征服系列游戏，并改进了平衡性和新增功能。 该项目保存并现代化了定义该类型的标志性即时战略游戏，使其能在当前硬件上运行，同时培育了活跃的社区。它还展示了像 EA 这样的发行商如何通过开源旧游戏来支持开源项目。 OpenRA 包含一个灵活的引擎，支持多种游戏模组，社区还增加了改进的单位平衡、现代用户界面和在线多人游戏等功能。该项目是免费开源的，源代码可在 GitHub 上获取。

hackernews · tosh · 6月27日 12:10 · [社区讨论](https://news.ycombinator.com/item?id=48697560)

**背景**: 命令与征服是一个传奇的即时战略游戏系列，最初由 Westwood Studios 开发，现在由 Electronic Arts 拥有。第一款游戏于 1995 年发布，被认为普及了即时战略类型。OpenRA 是一个独立项目，使用自定义引擎重新创建游戏机制，玩家需要拥有原始游戏资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openra.net/about/">About | OpenRA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Command_&_Conquer">Command & Conquer - Wikipedia</a></li>
<li><a href="https://openra.itch.io/openra">OpenRA by OpenRA developers</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 OpenRA 的平衡性改进和现代功能，有人指出在玩过 OpenRA 后再玩原版，会发现新版本的平衡性有多好。另一位评论者赞赏 EA 开源旧游戏的决定，并建议更多发行商效仿。社区反应非常积极，多年来多个讨论串显示出持续的兴趣。

**标签**: `#open-source`, `#gaming`, `#RTS`, `#game-development`

---

<a id="item-12"></a>
## [俄罗斯黑客涉嫌对捷豹路虎发动 25 亿美元黑客攻击](https://techcrunch.com/2026/06/26/russian-hackers-were-behind-2-5-billion-hack-of-jaguar-land-rover-report/) ⭐️ 7.0/10

一份报告称，俄罗斯国家支持的黑客对捷豹路虎发动了价值 25 亿美元的网络攻击，使其成为近年来损失最惨重、破坏性最大的黑客事件之一。 这一事件凸显了国家支持的网络攻击对关键基础设施和大型企业日益增长的威胁，可能对国家安全和全球汽车行业产生影响。 据报道，此次攻击给捷豹路虎造成了 25 亿美元的损失和破坏，攻击来源指向俄罗斯黑客，但具体技术手段尚未披露。

rss · TechCrunch · 6月26日 17:29

**背景**: 国家支持的黑客组织通常以大型企业为目标，进行间谍活动、牟利或破坏。由于汽车行业依赖互联技术和供应链，已成为主要攻击目标。

**标签**: `#cybersecurity`, `#hacking`, `#automotive`, `#state-sponsored`, `#data breach`

---

<a id="item-13"></a>
## [AI 的政治影响需要集体行动](https://techcrunch.com/2026/06/26/its-not-about-anthropic-vs-openai-anymore/) ⭐️ 7.0/10

TechCrunch 的一篇文章指出，AI 能力已发展到具有真实政治后果的程度，应对这些后果需要集体行动，而非聚焦于 Anthropic 和 OpenAI 等公司之间的竞争。 从模型竞争转向集体行动至关重要，因为 AI 的政治影响广泛影响社会，没有任何单一公司或实体能独自管理这些风险。 文章强调范式已改变：不再关乎哪家公司构建最佳模型，而是关乎行业和政策制定者如何协作处理 AI 的政治后果。

rss · TechCrunch · 6月26日 16:24

**背景**: 来自 Anthropic 和 OpenAI 等公司的 AI 模型能力迅速提升，引发了对其在虚假信息、监控和政治操纵中使用的担忧。历史上，AI 领域一直专注于竞争性模型开发，但日益增长的政治影响需要协调应对。

**标签**: `#AI policy`, `#collective action`, `#AI safety`, `#political impact`

---

<a id="item-14"></a>
## [苹果寻求豁免，向被制裁的中国供应商 CXMT 采购内存](https://www.theverge.com/tech/958707/apple-ram-buy-memory-blacklisted-china-cxmt) ⭐️ 7.0/10

苹果正在游说特朗普政府，寻求豁免以从长鑫存储（CXMT）采购 DRAM 芯片。CXMT 是一家中国内存制造商，因与中国人民解放军有关联而被美国国防部列入黑名单。 此举凸显了苹果在内存价格上涨时确保低成本供应的需求与美国对中国科技公司的国家安全限制之间的紧张关系。如果获批，可能为其他寻求类似豁免的公司开创先例，从而重塑供应链格局。 CXMT 并未被列入美国实体清单，但根据第 889 条被美国国防部列入黑名单，该条款限制与有中国军方背景的公司交易。从法律上讲，苹果可以向 CXMT 采购，但这样做存在声誉风险。

rss · The Verge · 6月27日 17:28

**背景**: CXMT 是一家总部位于合肥的中国 DRAM 制造商，生产 LPDDR4、DDR4 和 DDR5 内存。由于与中国人民解放军有关联，被美国国防部列入黑名单。苹果正面临内存和存储价格飙升的压力，这推高了其产品的成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/958707/apple-ram-buy-memory-blacklisted-china-cxmt">Apple wants permission to buy memory from a blacklisted Chinese ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/CXMT">CXMT</a></li>
<li><a href="https://appleinsider.com/articles/26/06/27/apple-asks-trump-to-let-it-buy-memory-from-a-blacklisted-supplier">Apple asks Trump to allow RAM imports from banned supplier</a></li>

</ul>
</details>

**标签**: `#Apple`, `#supply chain`, `#geopolitics`, `#memory chips`, `#CXMT`

---

<a id="item-15"></a>
## [让 CPU 愤怒的数据访问模式](https://www.reddit.com/r/programming/comments/1uh3z4m/data_access_patterns_that_makes_your_cpu_really/) ⭐️ 7.0/10

一篇 Reddit 帖子讨论了导致 CPU 性能问题的数据访问模式，如缓存未命中（cache miss）和分支预测错误（branch misprediction），以及内存布局如何影响性能。 理解这些模式对于编写性能关键型代码的开发者至关重要，因为糟糕的数据访问会显著降低 CPU 效率。这些知识有助于为现代处理器优化软件。 该帖子可能涵盖缓存行利用率、顺序访问与随机访问、以及分支预测惩罚。还可能讨论数据结构填充和布局重组等技术。

reddit · r/programming · /u/Double_Ad641 · 6月27日 14:19

**背景**: 现代 CPU 使用缓存来加速数据访问，但当数据不在缓存中（缓存未命中）时，CPU 会停顿。分支预测器猜测条件跳转的结果；预测错误会导致流水线刷新。内存布局（例如结构体顺序）影响缓存行为，从而影响性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cache_(computing)">Cache (computing) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Branch_misprediction">Branch misprediction</a></li>
<li><a href="https://johnnysswlab.com/performance-through-memory-layout/">Performance Through Memory Layout - Johnny's Software Lab</a></li>

</ul>
</details>

**标签**: `#performance`, `#CPU`, `#data access patterns`, `#optimization`, `#systems programming`

---