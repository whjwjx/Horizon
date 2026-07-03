---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> 从 73 条内容中筛选出 15 条重要资讯。

---

1. [弗吉尼亚州禁止出售地理位置数据](#item-1) ⭐️ 8.0/10
2. [Podman v6.0.0 发布，网络功能重大升级](#item-2) ⭐️ 8.0/10
3. [理解才能参与：避免与 AI 代理协作中的认知债务](#item-3) ⭐️ 8.0/10
4. [AI 的高能耗威胁净零目标](#item-4) ⭐️ 8.0/10
5. [Anthropic 与三星洽谈定制 AI 芯片](#item-5) ⭐️ 8.0/10
6. [OpenAI 提议将 5%股权捐赠给美国主权财富基金](#item-6) ⭐️ 8.0/10
7. [微软斥资 25 亿美元成立 AI 部署公司](#item-7) ⭐️ 8.0/10
8. [Anthropic Python SDK v0.116.0 新增智能体记忆测试版标头](#item-8) ⭐️ 7.0/10
9. [Linux 6.9 回归：LUKS 挂起不再从内存中擦除密钥](#item-9) ⭐️ 7.0/10
10. [PeerTube：去中心化视频平台引发关注](#item-10) ⭐️ 7.0/10
11. [使用 DSPy 优化 Datasette Agent 的 SQL 提示](#item-11) ⭐️ 7.0/10
12. [私人航天员为美国太空部队执行轨道任务](#item-12) ⭐️ 7.0/10
13. [Wisk Aero 因解雇提出安全问题的经理被起诉](#item-13) ⭐️ 7.0/10
14. [美国国土安全部网络遭黑客入侵，参议员发出警告](#item-14) ⭐️ 7.0/10
15. [好的 API 优雅地老去](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [弗吉尼亚州禁止出售地理位置数据](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data) ⭐️ 8.0/10

弗吉尼亚州通过了一项法律，禁止出售地理位置数据，成为美国首批专门禁止此类做法的州之一。该法律针对数据经纪人，并对位置信息的商业转移施加了严格限制。 这项法律标志着隐私保护的重要一步，可能遏制诸如追踪堕胎诊所访问或保险公司使用驾驶数据等滥用行为。它为其他州和联邦隐私立法树立了先例。 该法律明确禁止“出售”地理位置数据，但执法挑战依然存在，特别是对于在弗吉尼亚州收集数据的州外公司。地理位置数据的定义包括识别设备或个人物理位置的信息。

hackernews · toomuchtodo · 7月2日 21:03 · [社区讨论](https://news.ycombinator.com/item?id=48767347)

**背景**: 地理位置数据是指识别设备或个人地理位置的信息，通常通过智能手机、应用程序或车辆收集。数据经纪人汇总并出售此类数据，用于广告、保险风险评估和政治竞选等各种目的。目前，美国没有针对数据经纪人的全面联邦法规，导致各州法律零散不一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://termly.io/legal-dictionary/geolocation-data/">Geolocation Date Definition | Termly's Legal Dictionary</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_broker">Data broker</a></li>
<li><a href="https://epic.org/issues/consumer-privacy/data-brokers/">Data Brokers – EPIC – Electronic Privacy Information Center</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持该法律，但对执法表示担忧，特别是针对州外公司和“出售”的定义。一些人强调了具体滥用案例，如追踪 Planned Parenthood 访问和保险公司使用驾驶数据，凸显了严格监管的必要性。

**标签**: `#privacy`, `#geolocation data`, `#regulation`, `#data brokers`, `#Virginia`

---

<a id="item-2"></a>
## [Podman v6.0.0 发布，网络功能重大升级](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) ⭐️ 8.0/10

Podman v6.0.0 已发布，带来了重大的网络改进，并移除了对 CNI、cgroups v1、iptables、slirp4netns、Windows 10 和 Intel Mac 的支持。该更新还新增了机器和 Quadlet 功能，以及 AMD GPU 支持。 Podman v6.0.0 是一个包含破坏性变更的版本，移除了多个遗留组件，要求用户迁移到更新的网络栈。该更新还增强了 Quadlet（通过 systemd 单元管理容器）的功能，并增加了对 AMD GPU 的支持以加速工作负载。

hackernews · soheilpro · 7月2日 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48762098)

**背景**: Podman 是由 Red Hat 开发的无守护进程、无根容器引擎，旨在作为 Docker 的直接替代品。与 Docker 不同，Podman 不需要中央守护进程，从而增强了安全性并减少了资源占用。Quadlet 是一个允许用户将容器作为 systemd 服务运行的工具，简化了部署和管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lxer.com/module/newswire/view/365824/index.html">LXer: Podman 6 . 0 Lands with Breaking Changes, AMD GPUs Support</a></li>
<li><a href="https://www.redhat.com/en/topics/containers/what-is-podman">What is Podman?</a></li>
<li><a href="https://www.xurrent.com/blog/podman-vs-docker-complete-2025-comparison-guide-for-devops-teams">Podman vs Docker: Complete 2026 Comparison Guide for DevOps Teams | Xurrent</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体积极，用户称赞 Podman 从 Docker 迁移的简便性及其无守护进程设计。然而，一些用户指出与 Docker 存在细微不兼容之处，可能导致问题，并提醒 Podman 的 Docker 兼容性并非完美无缺。

**标签**: `#Podman`, `#containers`, `#Docker alternative`, `#devops`, `#open source`

---

<a id="item-3"></a>
## [理解才能参与：避免与 AI 代理协作中的认知债务](https://simonwillison.net/2026/Jul/2/understand-to-participate/#atom-everything) ⭐️ 8.0/10

Geoffrey Litt 在 AIE 大会上提出了“理解才能参与”的概念，认为开发者必须深入理解 AI 生成的代码变更，才能保持主动协作，避免积累认知债务。 随着 AI 编码代理生成越来越复杂的变更，这一概念凸显了人机协作中的关键挑战：保持共同理解以防止认知债务，否则会损害长期软件健康和团队效能。 Litt 强调，如果没有丰富的代码心智模型，开发者就会失去创造性思考和有效参与所需的流畅性。该演讲是 AIE 大会的一部分，相关录像预计将在随后三周内发布。

rss · Simon Willison · 7月2日 17:07

**背景**: 认知债务指的是当 AI 生成代码的速度超过人类理解能力时，团队内部共同理解的侵蚀。与技术债务表现为错误或构建失败不同，认知债务悄无声息地削弱团队推理和修改软件的能力。随着生成式和代理式 AI 加速开发，这一概念受到关注，引发了关于在速度指标之外维护软件健康的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/2/understand-to-participate/">Understand to participate | Simon Willison’s Weblog</a></li>
<li><a href="https://margaretstorey.com/blog/2026/02/09/cognitive-debt/">How Generative and Agentic AI Shift Concern from Technical Debt to Cognitive Debt</a></li>
<li><a href="https://getdx.com/blog/cognitive-debt-the-hidden-risk-in-ai-driven-software-development/">Cognitive debt: The hidden risk in AI-driven software development</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#cognitive debt`, `#software engineering`, `#human-AI collaboration`

---

<a id="item-4"></a>
## [AI 的高能耗威胁净零目标](https://techcrunch.com/2026/07/02/a-warning-sign-about-ais-real-cost-courtesy-of-google-and-amazon/) ⭐️ 8.0/10

TechCrunch 的一篇文章警告称，AI 日益增长的能耗正使谷歌和亚马逊等科技巨头越来越难以兑现其净零承诺。 这凸显了 AI 发展与环境可持续性之间的关键矛盾，可能迫使企业在创新与气候承诺之间做出选择。 AI 能耗发生在三个阶段：训练、推理和基础设施冷却，每个阶段都有巨大的电力需求。净零承诺通常缺乏标准化方法，允许公司自行定义核算规则。

rss · TechCrunch · 7月2日 19:14

**背景**: 净零承诺是公司平衡其温室气体排放与清除的承诺，但没有强制要求的方法。AI 模型，尤其是大型模型，需要巨大的计算资源，导致高耗电量和相关的碳排放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@charlez_victor/why-does-artificial-intelligence-consume-so-much-energy-417cfd49c2ad">Why Does Artificial Intelligence Consume So Much Energy ? | Medium</a></li>
<li><a href="https://news.climate.columbia.edu/2021/12/16/net-zero-pledges-can-they-get-us-where-we-need-to-go/">Net Zero Pledges : Can They Get Us Where We Need to Go?</a></li>

</ul>
</details>

**标签**: `#AI`, `#environment`, `#sustainability`, `#tech industry`, `#energy consumption`

---

<a id="item-5"></a>
## [Anthropic 与三星洽谈定制 AI 芯片](https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/) ⭐️ 8.0/10

据报道，Anthropic 正在与三星商讨开发定制 AI 芯片，此前 OpenAI 刚与博通合作推出了自己的定制 AI 芯片。 这标志着领先 AI 公司正转向定制硬件以减少对英伟达的依赖，并针对自身工作负载优化性能，是行业重要趋势。 此类先进 AI 芯片的预估开发成本约为 5 亿美元，Anthropic 目前运行模型的硬件栈包括英伟达 GPU、谷歌 TPU、亚马逊 Trainium 芯片以及博通定制芯片。

rss · TechCrunch · 7月2日 18:31

**背景**: 定制 AI 芯片专为 AI 工作负载设计，比通用芯片性能更优、能效更高。许多 AI 公司寻求定制芯片以摆脱对英伟达的依赖，后者主导着 AI 芯片市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/02/anthropic-is-discussing-a-new-custom-chip-with-samsung/">Anthropic is discussing a new custom chip with... | TechCrunch</a></li>
<li><a href="https://cryptobriefing.com/anthropic-custom-ai-server-chip-asic/">Anthropic explores custom AI server chip as revenue triples past $30...</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-06-24/openai-and-broadcom-unveil-ai-chip-to-run-models-faster-cheaper">OpenAI , Broadcom Unveil Jalapeno AI Chip Promising... - Bloomberg</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Anthropic`, `#custom chip`, `#Samsung`, `#industry trends`

---

<a id="item-6"></a>
## [OpenAI 提议将 5%股权捐赠给美国主权财富基金](https://techcrunch.com/2026/07/02/openai-proposed-donating-5-of-its-equity-to-a-us-sovereign-wealth-fund/) ⭐️ 8.0/10

OpenAI CEO Sam Altman 提议将公司 5%的股权捐赠给美国主权财富基金，旨在让公众分享 AI 繁荣带来的财务收益。 这一提议可能重塑公众从 AI 进步中获益的方式，有可能为其他 AI 公司树立先例，并影响关于 AI 财富公平分配的政策讨论。 该提议涉及捐赠股权而非现金，意味着主权财富基金将成为 OpenAI 的股东。具体的估值和时间表尚未明确。

rss · TechCrunch · 7月2日 15:20

**背景**: 主权财富基金是一种国家所有的投资基金，投资于股票、债券和房地产等资产。美国目前没有联邦层面的主权财富基金，但一些州有类似基金。OpenAI 的提议重新引发了关于公众参与 AI 利润分配的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_wealth_fund">Sovereign wealth fund</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#AI policy`, `#sovereign wealth fund`, `#equity`, `#public benefit`

---

<a id="item-7"></a>
## [微软斥资 25 亿美元成立 AI 部署公司](https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/) ⭐️ 8.0/10

微软宣布成立新的 AI 部署公司 Microsoft Frontier Co.，承诺投入 25 亿美元，并安排 6000 名员工嵌入客户团队。 此举标志着微软的重大战略转变，效仿亚马逊、OpenAI 和 Anthropic 成立专门的 AI 部署部门，可能加速企业 AI 应用并重塑竞争格局。 新部门名为 Microsoft Frontier Co.，将安排 6000 名行业和工程专家嵌入客户组织，支持企业 AI 部署，这种做法被称为前向部署工程。

rss · TechCrunch · 7月2日 13:53

**背景**: AI 部署公司帮助企业集成和运营 AI 解决方案。亚马逊、OpenAI 和 Anthropic 等主要科技公司已建立类似部门，协助客户从 AI 实验转向生产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/02/microsoft-launches-its-own-ai-deployment-company-with-2-5-billion-commitment/">Microsoft launches its own AI deployment company with $2.5 billion commitment | TechCrunch</a></li>
<li><a href="https://www.cnbc.com/2026/07/02/microsoft-commits-2point5-billion-6000-employees-ai-implementation-unit.html">Microsoft commits $2.5 billion and 6,000 employees to new AI implementation unit</a></li>
<li><a href="https://en.cryptonomist.ch/2026/07/02/microsoft-ai-deployment-enterprise/">Microsoft AI Deployment Boosted by $2.5B Enterprise Venture</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#AI deployment`, `#investment`, `#industry news`

---

<a id="item-8"></a>
## [Anthropic Python SDK v0.116.0 新增智能体记忆测试版标头](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.116.0) ⭐️ 7.0/10

Anthropic 发布了其 Python SDK 的 0.116.0 版本，新增了 'agent-memory-2026-07-22' 测试版标头，用于启用 AI 智能体的记忆功能。 此更新使开发者能够构建可记住过去交互并在会话间共享知识的 AI 智能体，显著提升了智能体的连续性和个性化能力。 该测试版标头名为 'agent-memory-2026-07-22'，需在 API 请求中包含以激活记忆工具。开发者还需实现客户端处理器来控制存储。

github · stainless-app[bot] · 7月2日 19:07

**背景**: AI 智能体记忆允许智能体在多次交互中保留上下文，使其能够从过去的会话中学习并与其他智能体共享信息。Anthropic 此前在 2026 年 4 月通过不同的测试版标头为 Claude Managed Agents 引入了记忆功能。本次 SDK 更新将类似能力扩展到了使用 Python SDK 构建的自定义智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.leoniemonigatti.com/blog/claude-memory-tool.html">Exploring Anthropic’s Memory Tool – Leonie Monigatti</a></li>
<li><a href="https://bibigpt.co/en/features/claude-managed-agents-memory-explained">Claude Managed Agents Memory Explained: Anthropic's 2026-04-23 Persistent-Context Beta</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#SDK`, `#agent-memory`, `#AI`, `#Python`

---

<a id="item-9"></a>
## [Linux 6.9 回归：LUKS 挂起不再从内存中擦除密钥](https://mathstodon.xyz/@iblech/116769502749142438) ⭐️ 7.0/10

自 Linux 内核 6.9 版本起，LUKS 挂起功能在系统挂起期间不再从内存中擦除磁盘加密密钥，可能使密钥暴露在 RAM 中。 这一回归破坏了挂起期间全盘加密的安全保障，拥有物理访问权限的攻击者可能从内存中提取主密钥，从而危及所有加密数据。 此变化影响 cryptsetup luksSuspend 命令，该命令并非内核官方部分，但常用于基于 Debian 的发行版。内核现在在挂起期间将加密密钥保留在内存中，而之前会将其擦除。

hackernews · IngoBlechschmid · 7月2日 15:25 · [社区讨论](https://news.ycombinator.com/item?id=48763035)

**背景**: LUKS（Linux 统一密钥设置）是一种保护静态数据的磁盘加密规范。当系统挂起到 RAM 时，加密密钥必须保留在内存中以实现快速恢复。luksSuspend 命令旨在擦除该密钥并阻止 I/O，直到重新输入密码，从而提供针对冷启动攻击的额外安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vpshostingdiscount.com/security-compliance/since-linux-6-9-luks-suspend-stopped-wiping-disk-encryption-keys-from-memory/">Since Linux 6.9, LUKS Suspend Stopped Wiping Disk- encryption ...</a></li>
<li><a href="https://hacknjill.com/cybersecurity/since-linux-6-9-luks-suspend-stopped-wiping-disk-encryption-keys-from-memory/">Since Linux 6.9, LUKS Suspend Stopped Wiping Disk- encryption ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：有人认为这一回归影响不大，因为 luksSuspend 并非官方支持；另一些人则强调此类安全漏洞容易被忽视，因为一切看起来仍然正常。一位用户指出，睡眠后无需重新输入启动密码，证实密钥仍保留在内存中。

**标签**: `#Linux`, `#security`, `#encryption`, `#kernel`, `#LUKS`

---

<a id="item-10"></a>
## [PeerTube：去中心化视频平台引发关注](https://github.com/Chocobozzz/PeerTube) ⭐️ 7.0/10

PeerTube 是一个免费开源、使用 ActivityPub 联邦协议的去中心化视频平台，正作为 YouTube 等中心化服务的替代方案获得关注，但仍面临盈利和内容可用性方面的挑战。 PeerTube 的重要性在于它提供了一种抗审查、由社区控制的替代方案，可能重塑在线视频内容的托管和分发方式。 PeerTube 使用点对点技术来减轻热门视频的服务器负载，并支持直播。然而，其联邦特性意味着内容发现和受众覆盖范围仍不如中心化平台。

hackernews · doener · 7月2日 11:17 · [社区讨论](https://news.ycombinator.com/item?id=48759634)

**背景**: PeerTube 是一个免费开源的去中心化视频平台，使用 ActivityPub 协议实现实例间的联邦，允许用户托管自己的服务器同时与其他实例交互。它旨在作为 YouTube 等中心化平台的替代品，赋予内容创作者更多控制权并降低审查风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PeerTube">PeerTube - Wikipedia</a></li>
<li><a href="https://joinpeertube.org/faq">FAQ | JoinPeerTube</a></li>
<li><a href="https://dailycoin.com/decentralized-video-streaming-platforms-best-alternatives-to-youtube/">Decentralized YouTube Alternatives: Video Streaming... - DailyCoin</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调盈利是专业创作者的主要障碍，一位 YouTuber 指出制作成本高昂。其他人指出 PeerTube 上缺乏主流话题的内容和观众，尽管有些人认为它适合小众开源项目。

**标签**: `#decentralization`, `#video platform`, `#open source`, `#federation`, `#PeerTube`

---

<a id="item-11"></a>
## [使用 DSPy 优化 Datasette Agent 的 SQL 提示](https://simonwillison.net/2026/Jul/2/dspy-datasette-agent-prompts/#atom-everything) ⭐️ 7.0/10

Simon Willison 使用 DSPy 框架评估并改进了 Datasette Agent 的 SQL 系统提示，发现了列名猜测和错误重试循环等问题，并提出了在模式列表中包含列名等修复方案。 这展示了一种实用的、自动化的提示优化方法，可显著提高 AI 辅助数据查询工具（如 Datasette Agent）的可靠性和准确性。 实验通过 Claude Fable 5 使用了 GPT-4.1 mini 和 nano 模型，发现模式列表中缺少列名会导致错误猜测和错误循环；包含列名或软化相关建议可解决该问题。

rss · Simon Willison · 7月2日 18:25

**背景**: DSPy 是一个通过算法优化提示和权重来编程语言模型的框架，而非手动编写提示。Datasette Agent 是一个 AI 助手，可生成 SQL 查询来回答用户关于 Datasette 中数据的问题。提示优化对于确保 AI 代理生成正确且高效的 SQL 查询至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/stanfordnlp/dspy">GitHub - stanfordnlp/dspy: DSPy: The framework for programming—not prompting—language models</a></li>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>
<li><a href="https://github.com/datasette/datasette-agent">GitHub - datasette / datasette - agent : An LLM-powered agent for...</a></li>

</ul>
</details>

**标签**: `#DSPy`, `#prompt engineering`, `#Datasette`, `#AI agents`, `#SQL`

---

<a id="item-12"></a>
## [私人航天员为美国太空部队执行轨道任务](https://techcrunch.com/2026/07/02/private-space-pilots-are-flying-orbital-missions-for-the-us-space-force/) ⭐️ 7.0/10

私营公司 True Anomaly 和 Rocket Lab 正在为美国太空部队执行轨道卫星机动，进行类似于空中缠斗的近距离操作。 这标志着太空物流和防御领域的范式转变，私营公司承担了传统上由政府资产执行的军事轨道操作，可能加速天基防御能力的发展。 True Anomaly 由前太空部队成员创立，专注于太空防御，其 Jackal 航天器用于执行任务；Rocket Lab 则提供 Electron 火箭和 Photon 卫星平台等发射和卫星平台。

rss · TechCrunch · 7月2日 23:01

**背景**: 美国太空部队越来越多地利用商业伙伴进行太空操作。True Anomaly 是一家专注于太空优势的国防科技公司，Rocket Lab 是领先的小型卫星发射服务商。这些任务涉及卫星近距离机动，测试潜在太空冲突的战术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.trueanomaly.space/?ref=whatocome.xyz">True Anomaly - Delivering Decisive Capabilities for Space Superiority.</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_Lab">Rocket Lab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_Lab_Electron">Rocket Lab Electron - Wikipedia</a></li>

</ul>
</details>

**标签**: `#space`, `#defense`, `#private aerospace`, `#satellites`, `#military`

---

<a id="item-13"></a>
## [Wisk Aero 因解雇提出安全问题的经理被起诉](https://techcrunch.com/2026/07/02/boeing-owned-wisk-aero-accused-of-firing-manager-who-raised-safety-concerns/) ⭐️ 7.0/10

波音旗下的 Wisk Aero 前软件经理提起诉讼，声称他在提出公司为赶在 2025 年关键飞行测试前匆忙进行软件测试的担忧后被解雇。 此案凸显了波音及其子公司持续存在的安全文化问题，并可能影响 Wisk 自主空中出租车的认证，该认证需要 FAA 对其软件安全性的信任。 自 2020 年以来，Wisk 已收到 32 起向 OSHA 提出的举报投诉，参议院小组委员会就波音“破碎的安全文化”举行了听证会。该公司正在寻求 FAA 对美国首款全自动载客飞机的认证。

rss · TechCrunch · 7月2日 17:30

**背景**: Wisk Aero 是波音子公司，开发用于城市空中交通的自主 eVTOL（电动垂直起降）飞机。该公司已进行超过 1,750 次试飞，旨在推出自动飞行出租车服务。自主飞行认证是一项重大挑战，需要严格的软件测试以确保安全。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenextweb.com/news/wisk-aero-boeing-whistleblower-safety-software-testing">Boeing's autonomous air taxi subsidiary faces a whistleblower lawsuit over rushed software testing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wisk_Aero">Wisk Aero</a></li>
<li><a href="https://www.flyingmag.com/breaking-new-ground-the-challenge-of-certifying-autonomous-aircraft/">Breaking New Ground: The Challenge of Certifying Autonomous Aircraft</a></li>

</ul>
</details>

**标签**: `#software safety`, `#aviation`, `#whistleblower`, `#autonomous vehicles`, `#Boeing`

---

<a id="item-14"></a>
## [美国国土安全部网络遭黑客入侵，参议员发出警告](https://techcrunch.com/2026/07/02/us-government-says-it-got-hacked-again/) ⭐️ 7.0/10

参议院情报委员会的一位民主党高层警告称，美国国土安全部的情报共享网络遭到黑客入侵，可能危及国家安全。 此次政府情报共享网络遭入侵，可能泄露联邦、州及私营部门合作伙伴之间共享的敏感信息，从而损害国家安全及对关键基础设施的信任。 国土安全信息网络（HSIN）用于与政府、国际及私营部门合作伙伴共享敏感但非机密的信息。此次入侵的具体细节及被访问数据的范围尚未披露。

rss · TechCrunch · 7月2日 14:22

**背景**: 国土安全信息网络（HSIN）是一个基于网络的安全平台，使国土安全部能够与合作伙伴共享威胁情报和态势感知，旨在促进国土安全任务的协作。此前政府网络遭入侵的事件已暴露出联邦网络安全中持续存在的漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nextgov.com/cybersecurity/2026/06/hackers-breached-dhs-information-sharing-network-people-familiar-say/414534/">Hackers breached DHS information- sharing network ... - Nextgov/FCW</a></li>
<li><a href="https://www.govinfo.gov/content/pkg/CHRG-108hhrg98599/html/CHRG-108hhrg98599.htm">improvements to department of homeland security information...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#government`, `#national security`, `#hacking`

---

<a id="item-15"></a>
## [好的 API 优雅地老去](https://www.reddit.com/r/programming/comments/1ulbz41/good_apis_age_slowly/) ⭐️ 7.0/10

一篇文章讨论了使 API 经久耐用且易于维护的设计原则，强调简洁性、一致性和向后兼容性。 这些原则帮助开发者创建多年后仍有用且易于集成的 API，从而减少整个软件生态系统中的技术债务和迁移成本。 该文章可能涵盖避免过度规范、使用稳定的抽象以及从一开始就为演进而非完美而设计等主题。

reddit · r/programming · /u/fagnerbrack · 7月2日 08:04

**背景**: API（应用程序编程接口）定义了不同软件组件之间的通信方式。设计良好的 API 对于构建可靠且可扩展的系统至关重要，但许多 API 会随着需求变化而变得脆弱或过时。

**标签**: `#API Design`, `#Software Engineering`, `#Best Practices`

---