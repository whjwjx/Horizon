---
layout: default
title: "Horizon Summary: 2026-06-18 (ZH)"
date: 2026-06-18
lang: zh
---

> 从 90 条内容中筛选出 15 条重要资讯。

---

1. [GLM-5.2：最强开源权重 LLM 发布](#item-1) ⭐️ 9.0/10
2. [Lore：面向游戏开发的开源版本控制系统](#item-2) ⭐️ 8.0/10
3. [美国推迟将 DeepSeek 列入黑名单，标记超 100 家中国企业](#item-3) ⭐️ 8.0/10
4. [使用 GPT-5.4 的 AI 化学家改进关键药物反应](#item-4) ⭐️ 8.0/10
5. [OpenAI 推出生命科学 AI 基准测试 LifeSciBench](#item-5) ⭐️ 8.0/10
6. [Charity Majors：AI 让代码变廉价，需要更多工程纪律](#item-6) ⭐️ 8.0/10
7. [AI 模型出口管制削弱美国网络防御](#item-7) ⭐️ 8.0/10
8. [全球领导人担忧美国切断 AI 服务](#item-8) ⭐️ 8.0/10
9. [俄语黑客组织入侵数万台 Fortinet 防火墙](#item-9) ⭐️ 8.0/10
10. [Pramaana Labs 获 2700 万美元种子轮融资，用于 AI 形式化验证](#item-10) ⭐️ 8.0/10
11. [RFC 10008 提出新的 HTTP QUERY 方法](#item-11) ⭐️ 8.0/10
12. [Datasette 1.0a34 在网页界面中增加行编辑功能](#item-12) ⭐️ 7.0/10
13. [Georgi Gerganov 推荐 Qwen3.6-27B 用于本地编程](#item-13) ⭐️ 7.0/10
14. [FTC 诉讼揭露订阅诈骗网络规避应用商店执法的策略](#item-14) ⭐️ 7.0/10
15. [Odyssey 获亚马逊支持，估值达 14.5 亿美元](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GLM-5.2：最强开源权重 LLM 发布](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Z.ai 于 2026 年 6 月 16 日发布了 GLM-5.2，这是一个 753B 参数、拥有 100 万 token 上下文窗口的开源权重 LLM，采用 MIT 许可证。 GLM-5.2 被广泛认为是最强大的开源权重纯文本模型，在 Artificial Analysis Intelligence Index 上超越了 MiniMax-M3 和 DeepSeek V4 Pro 等竞争对手，并以极低的成本提供了接近前沿的性能。 该模型采用混合专家（MoE）架构，总参数 753B 中激活 40B，且每个任务消耗的输出 token（43k）多于同类模型。它在 Code Arena WebDev 排行榜上排名第二，仅次于 Claude Fable 5，尽管缺乏图像输入。

rss · Simon Willison · 6月17日 23:58

**背景**: 开源权重 LLM 将其训练好的参数公开，允许任何人使用和修改。混合专家（MoE）架构每次只激活部分参数，提高了效率。100 万 token 的上下文窗口可以一次性处理非常长的文档或对话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical...</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 GLM-5.2 的性能和低成本感到兴奋，有人称其为对专有 AI 公司的'巨大打击'。但也有用户对推理效率表示担忧，报告称该模型在一个简单的编程任务上花费了 15 分钟和 45k token。

**标签**: `#LLM`, `#open-weights`, `#AI`, `#GLM-5.2`, `#Z.ai`

---

<a id="item-2"></a>
## [Lore：面向游戏开发的开源版本控制系统](https://lore.org/) ⭐️ 8.0/10

Epic Games 已将 Lore 开源，这是一个专为可扩展性设计的下一代版本控制系统，旨在与 Perforce 竞争，服务于游戏开发领域。 Lore 解决了游戏开发中版本控制的关键缺口，它比 Git 更好地处理大型二进制文件和独占锁，为专有的 Perforce 提供了一个现代开源替代方案。 Lore 已经是 UEFN（Unreal Editor for Fortnite）的内置版本控制系统，但由于 UEFN 构建使用了专有压缩格式，当前开源工具尚无法与之通信。

hackernews · regnerba · 6月17日 14:30 · [社区讨论](https://news.ycombinator.com/item?id=48571081)

**背景**: 像 Git 这样的版本控制系统针对基于文本的文件（代码）进行了优化，但在处理游戏开发中常见的大型二进制文件（纹理、3D 模型、音频）时表现不佳。Perforce 是游戏开发行业的标配，因为它支持大文件和独占文件锁定，但它是专有的且管理复杂。Lore 旨在将 Perforce 的可扩展性和锁定功能与 Git 的开放性结合起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epicgames.github.io/lore/explanation/system-design/">The Lore Version Control System - Lore Developer Documentation</a></li>
<li><a href="https://github.com/EpicGames/lore">GitHub - EpicGames/ lore : Lore is a next-generation, open source...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perforce">Perforce - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区普遍认为 Lore 满足了真实需求，许多人指出 Perforce 在游戏开发中的主导地位及其复杂性。一些评论者希望 Lore 能简化工作流程，而另一些人则提醒说它仍处于早期阶段，开源工具尚不完善。

**标签**: `#version control`, `#game development`, `#open source`, `#scalability`, `#Perforce`

---

<a id="item-3"></a>
## [美国推迟将 DeepSeek 列入黑名单，标记超 100 家中国企业](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 8.0/10

美国决定推迟将中国 AI 初创公司 DeepSeek 及其他 100 多家中国企业列入黑名单，尽管跨部门已批准将其认定为国家安全风险，此举旨在避免与北京方面的紧张局势升级。 这一决定凸显了美国在遏制中国技术进步与维持外交关系之间必须把握的微妙平衡，对全球 AI 竞赛和技术脱钩具有重大影响。 黑名单将限制美国公司向这些企业出售商品和服务，但像 DeepSeek 这样的中国 AI 公司已面临英伟达 GPU 的出口管制，且对美国输入的依赖很小。

hackernews · giuliomagnifico · 6月17日 03:55 · [社区讨论](https://news.ycombinator.com/item?id=48565498)

**背景**: DeepSeek 是一家中国 AI 公司，开发了开源权重的 DeepSeek-R1 模型，其性能可与 OpenAI 的 GPT-4 媲美，但训练成本仅为后者的一小部分。其成功被视为美国 AI 领导地位的“斯普特尼克时刻”。美国一直通过关税和出口管制限制中国的技术崛起，而中国则控制着对国防和电子产品至关重要的稀土矿物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://finance.yahoo.com/news/exclusive-us-holds-off-blacklisting-000212827.html">Exclusive- US holds off blacklisting China 's DeepSeek, more than 100...</a></li>
<li><a href="https://economictimes.indiatimes.com/news/international/business/u-s-held-back-blacklisting-deepseek-over-100-chinese-firms-despite-security-concerns-sources-say/articleshow/131792688.cms">U . S . held back blacklisting DeepSeek, over 100 Chinese firms ...</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不同观点：有人称赞 DeepSeek 的性价比和实用性，也有人批评美国政策虚伪或难以执行，并将其与中国自身的限制措施相提并论。少数人指出，由于中国企业已面临 GPU 出口禁令，黑名单的实际影响有限。

**标签**: `#AI`, `#geopolitics`, `#regulation`, `#DeepSeek`, `#US-China`

---

<a id="item-4"></a>
## [使用 GPT-5.4 的 AI 化学家改进关键药物反应](https://openai.com/index/ai-chemist-improves-reaction) ⭐️ 8.0/10

OpenAI 与 Molecule.one 展示了一种由 GPT-5.4 驱动的近乎自主的 AI 化学家，成功改进了药物化学中一项具有挑战性的反应。 这一进展可通过自动化复杂化学合成来加速药物发现，降低新药开发的时间和成本。 该系统利用 GPT-5.4 的推理和计算机使用能力，以最少的人为干预规划和执行实验，实现了关键反应产率的提升。

rss · OpenAI Blog · 6月17日 10:00

**背景**: 药物化学通常需要优化候选药物的合成路线，这一过程耗时且依赖专家直觉。像 GPT-5.4 这样的 AI 模型可以分析大量化学数据并提出新颖的反应条件，而自主系统可以并行运行实验。这种集成标志着向全自动化化学研究迈出了一步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.4">GPT-5.4</a></li>
<li><a href="https://molecule.one/">molecule . one - Making Molecules . Discovering Chemistry</a></li>

</ul>
</details>

**标签**: `#AI`, `#Chemistry`, `#Drug Discovery`, `#Autonomous Systems`, `#GPT-5.4`

---

<a id="item-5"></a>
## [OpenAI 推出生命科学 AI 基准测试 LifeSciBench](https://openai.com/index/introducing-life-sci-bench) ⭐️ 8.0/10

OpenAI 推出了 LifeSciBench，这是一个由领域专家编写和审查的新基准，用于评估 AI 系统在真实世界生命科学研究任务和决策中的表现。 该基准提供了一个严格的、由专家驱动的评估框架，有助于确保 AI 系统在科学研究中的安全性和有效性，可能加速药物发现、基因组学等生命科学领域的进展。 LifeSciBench 侧重于端到端的科学任务而非孤立能力，并通过使用专家编写的私有问题来避免公共数据集的污染。

rss · OpenAI Blog · 6月17日 00:00

**背景**: 基准测试是用于衡量和比较 AI 模型性能的标准化测试。LifeSciBench 是朝着专家编写评估方向发展的更广泛趋势的一部分，这种评估能更好地反映真实世界的专业任务，例如 Humanity's Last Exam 和 Scale 的专家驱动排行榜。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-life-sci-bench/">Introducing LifeSciBench | OpenAI</a></li>
<li><a href="https://theplanettools.ai/blog/openai-gpt-rosalind-life-sciences-codex-plugins-lifescibench-june-2026">GPT-Rosalind Gets GPT-5.5: Codex Plugins + LifeSciBench</a></li>
<li><a href="https://www.techtimes.com/articles/317754/20260604/gpt-rosalind-drug-discovery-update-openai-cuts-genomics-compute-expands-global-access.htm">GPT-Rosalind Drug Discovery Update: OpenAI Cuts Genomics...</a></li>

</ul>
</details>

**标签**: `#AI`, `#benchmark`, `#life sciences`, `#OpenAI`, `#evaluation`

---

<a id="item-6"></a>
## [Charity Majors：AI 让代码变廉价，需要更多工程纪律](https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything) ⭐️ 8.0/10

Charity Majors 认为，AI 颠覆了代码生产的经济学，使代码生成变得几乎免费且即时，这要求更多的工程纪律，而非更少。 这一见解挑战了“AI 降低对熟练工程师需求”的常见说法，强调廉价、可丢弃的代码反而需要更强的工程实践来管理复杂性和维持质量。 Majors 指出，到 2025 年，代码行几乎在一夜之间从被珍视和精心策划变为可丢弃和可重新生成。她警告说，非确定性 AI 系统将需要更多纪律，而非更少。

rss · Simon Willison · 6月17日 17:12

**背景**: 历史上，编写代码缓慢且昂贵，作为一种自然刹车迫使人们在编写前仔细思考。随着生成式 AI 的出现，代码可以以近乎零成本即时生成，瓶颈从生产转移到了维护和系统设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/17/charity-majors/">A quote from Charity Majors | Simon Willison’s Weblog</a></li>
<li><a href="https://charity.wtf/2026/06/15/ai-demands-more-engineering-discipline-not-less-xpost/">AI demands more engineering discipline . Not less (xpost) – charity .wtf</a></li>
<li><a href="https://ghost.madewithlove.dev/blog/ai-didnt-change-the-economics-of-software-engineering/">AI didn't change the economics of software engineering</a></li>

</ul>
</details>

**社区讨论**: 在 Simon Willison 博客和原帖上的社区讨论显示，许多人赞同 Majors 的观点，许多工程师分享经验称 AI 生成的代码引入了细微错误，需要更严格的审查。一些人争论这种转变是否真的增加了纪律，还是仅仅改变了其性质。

**标签**: `#ai-assisted-programming`, `#software-engineering`, `#generative-ai`, `#economics-of-code`

---

<a id="item-7"></a>
## [AI 模型出口管制削弱美国网络防御](https://simonwillison.net/2026/Jun/16/fable-5-export-controls/#atom-everything) ⭐️ 8.0/10

特朗普政府对 Anthropic 的 Claude Fable 5 和 Mythos 5 实施出口管制，理由是该模型能够修复代码漏洞的“越狱”行为。网络安全专家 Kate Moussouris 澄清，所谓的越狱实际上是修补安全漏洞的合法防御请求。 该政策通过限制 AI 模型修复关键安全漏洞，损害了美国网络防御能力，而这正是防御者所需要的。同时，它为监管对网络安全至关重要的 AI 能力树立了危险先例。 出口管制迫使 Anthropic 阻止所有外国国民（包括美国境内用户和自身员工）访问 Fable 5 和 Mythos 5。这些模型被禁是因为它们可以被提示“修复此代码”并生成补丁，而政府将其归类为网络攻击能力。

rss · Simon Willison · 6月16日 05:20

**背景**: Claude Fable 5 是 Anthropic 开发的大型语言模型，设计用于通用场景并具有强大的安全对齐。出口管制是限制敏感技术向外国实体转移的法规，通常用于防止对手获得军事或战略优势。在此案例中，出口管制首次应用于 AI 模型，基于其代码修复能力构成安全威胁的错误认知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519">Inside the whirlwind 24 hours that led the White House to slap export ...</a></li>

</ul>
</details>

**社区讨论**: 讨论中普遍认为出口管制适得其反，Kate Moussouris 等专家强调修复漏洞是 AI 最具价值的防御用途。评论者指出，非技术决策者将防御性代码修复与攻击性网络攻击混为一谈，导致政策误导。

**标签**: `#AI policy`, `#export controls`, `#cybersecurity`, `#AI safety`, `#open source`

---

<a id="item-8"></a>
## [全球领导人担忧美国切断 AI 服务](https://techcrunch.com/2026/06/17/world-leaders-want-american-ai-they-just-dont-want-america-to-be-able-to-turn-it-off/) ⭐️ 8.0/10

在 G7 峰会上，法国总统马克龙和印度总理莫迪提出担忧，认为美国可能切断对美国 AI 系统的访问，而最近的 Anthropic 断供事件使这一担忧变得具体。 这凸显了围绕 AI 主权的日益加剧的地缘政治紧张局势，各国担心依赖美国控制的 AI 基础设施可能被用作政治杠杆，威胁国家安全和经济自主。 Anthropic 断供事件（Claude 访问突然受限）成为美国公司可能切断 AI 服务的具体例证，验证了长期存在的技术胁迫担忧。

rss · TechCrunch · 6月17日 19:01

**背景**: AI 主权指国家自主开发、控制和治理 AI 系统而不依赖外部的能力。美国目前拥有 OpenAI 和 Anthropic 等领先 AI 公司，使其在全球 AI 访问方面拥有显著影响力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/why-ai-sovereignty-matters-more-than-you-think-arpit-tandon-ncfmc">Why AI Sovereignty Matters More Than You Think</a></li>

</ul>
</details>

**标签**: `#AI`, `#geopolitics`, `#AI sovereignty`, `#regulation`, `#Anthropic`

---

<a id="item-9"></a>
## [俄语黑客组织入侵数万台 Fortinet 防火墙](https://techcrunch.com/2026/06/17/cybercriminals-allegedly-hacked-tens-of-thousands-of-fortinet-firewalls-used-by-major-companies-all-over-the-world/) ⭐️ 8.0/10

据报道，一个疑似俄语网络犯罪组织利用已知密码入侵了全球各大公司使用的数万台 Fortinet 防火墙。 此次针对企业防火墙的大规模攻击可能导致广泛的数据泄露和网络入侵，影响众多知名组织，并凸显了密码重复使用的危险。 据报道，攻击者使用的是已知密码而非新漏洞来获取访问权限。被入侵的防火墙包括用于 VPN 和网络安全的 FortiGate 设备。

rss · TechCrunch · 6月17日 18:20

**背景**: Fortinet 防火墙被企业广泛用于网络安全和 VPN 接入。网络犯罪分子经常以这些设备为目标，因为它们提供了进入内部网络的通道。此前的事件表明，许多组织未能更改默认或弱密码，使其容易受到凭证填充攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/passwords-exposed-for-almost-50-000-vulnerable-fortinet-vpns/">Passwords exposed for almost 50,000 vulnerable Fortinet VPNs</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/5278/fortibleed-fortinet-vpn-credentials-stolen">FortiBleed: 75,000 Fortinet VPN Credentials Stolen Across 194...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#Fortinet`, `#firewall`, `#vulnerability`, `#cyberattack`

---

<a id="item-10"></a>
## [Pramaana Labs 获 2700 万美元种子轮融资，用于 AI 形式化验证](https://techcrunch.com/2026/06/17/pramaana-labs-raises-27-million-seed-round-from-khosla-ventures-to-bring-formal-verification-to-ai/) ⭐️ 8.0/10

Pramaana Labs 完成了由 Khosla Ventures 领投的 2700 万美元种子轮融资，旨在将形式化验证技术应用于 AI 系统，专注于法律、药物发现和税务准备等高可靠性领域。 这笔融资表明投资者对形式化验证作为 AI 可靠性解决方案的信心，可能推动 AI 在错误代价高昂的关键领域的应用。 Pramaana 的系统为 AI 答案提供机器可验证的证明，确保准确性并识别违规行为。该公司专注于基于规则的高风险领域，形式化验证可保证正确性。

rss · TechCrunch · 6月17日 14:15

**背景**: 形式化验证使用数学方法证明或证伪系统相对于形式规范的正确性。它广泛应用于硬件和关键软件（如 CompCert 编译器、seL4 内核），但由于神经网络的复杂性和非确定性，一直难以应用于 AI。Pramaana 旨在为高可靠性应用弥合这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://www.rediff.com/business/report/pramaana-labs-raises-27-million-led-by-khosla-ventures/20260617.htm">Pramaana Labs Raises $27M To Develop... - Rediff.com Business</a></li>

</ul>
</details>

**标签**: `#AI`, `#formal verification`, `#funding`, `#reliability`

---

<a id="item-11"></a>
## [RFC 10008 提出新的 HTTP QUERY 方法](https://www.reddit.com/r/programming/comments/1u84m2g/rfc_10008_the_http_query_method/) ⭐️ 8.0/10

RFC 10008 定义了一种新的 HTTP QUERY 方法，允许客户端以安全且幂等的方式发送请求体，将此前由 GET 或 POST 处理的模式标准化。 这为带请求体的查询提供了标准化方式，提升了 API 设计的清晰度和互操作性，并减少了现有实践中的歧义。 QUERY 方法是安全且幂等的，即不会改变服务器状态，且多个相同请求的效果与单个请求相同。它还定义了 Accept-Query 头字段用于内容协商。

reddit · r/programming · /u/Nimelrian · 6月17日 08:43

**背景**: HTTP 方法如 GET 是安全且幂等的，但不支持请求体；而 POST 支持请求体，但既不安全也不幂等。QUERY 方法填补了这一空白，允许携带请求体同时保持安全性和幂等性，适用于 GraphQL 或 SPARQL 等 API 中的复杂查询。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc10008/">RFC 10008 : The HTTP QUERY Method | RFC Editor</a></li>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-httpbis-safe-method-w-body/12/">draft-ietf-httpbis-safe- method -w-body-12 - The HTTP QUERY Method</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Idempotent">Idempotent - Glossary | MDN</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论很活跃，许多评论者就新方法的实用性展开辩论。一些人认为它形式化了一种常见模式，而另一些人则担心潜在的误用和复杂性。总体情绪谨慎乐观，大家对其如何被采纳感兴趣。

**标签**: `#HTTP`, `#RFC`, `#Web Standards`, `#API Design`

---

<a id="item-12"></a>
## [Datasette 1.0a34 在网页界面中增加行编辑功能](https://simonwillison.net/2026/Jun/16/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a34 在网页界面中直接引入了插入、编辑和删除行的功能，可在表格页面和行页面上使用。该功能受 Datasette Agent 启发，后者已支持 SQL 写入操作。 此更新填补了 Datasette 在可用性方面长期存在的空白，使其成为更完整的数据探索和管理工具。它减少了对基本 CRUD 操作的外部工具或插件的需求，惠及所有 Datasette 用户。 插入、编辑和删除功能在表格页面上可用，而编辑和删除也作为操作项出现在行页面上。此版本为 alpha 版本（1.0a34），表明可能仍存在错误或不完整的功能。

rss · Simon Willison · 6月16日 21:31

**背景**: Datasette 是一个用于探索和发布数据的开源工具，主要与 SQLite 数据库配合使用。此前，用户必须依赖插件或外部工具才能通过网页界面修改数据。Datasette Agent 是一个能够编写和执行 SQL 查询（包括写入操作）的 AI 助手，这凸显了原生数据操作界面的缺失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>
<li><a href="https://simonwillison.net/2026/May/21/datasette-agent/">Datasette Agent | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#datasette`, `#release`, `#database`, `#web-ui`, `#alpha`

---

<a id="item-13"></a>
## [Georgi Gerganov 推荐 Qwen3.6-27B 用于本地编程](https://simonwillison.net/2026/Jun/16/georgi-gerganov/#atom-everything) ⭐️ 7.0/10

llama.cpp 的创建者 Georgi Gerganov 公开推荐 Qwen3.6-27B 模型，称其是一款非常强大的本地编程助手，并分享了他每天在 M2 Ultra 和 RTX 5090 机器上使用该模型的经验。 来自本地 LLM 生态关键人物的认可，验证了 Qwen3.6-27B 作为开发者实用工具的价值，可能推动本地编程助手的更广泛采用，并减少对云端 AI 服务的依赖。 Gerganov 使用一个名为 pi agent 的轻量级工具，配合 '-nc --offline' 参数和一个简短的系统提示词来调整模型以适应他的编程风格。他指出，如果不是因为花大量时间审查 PR，他会更频繁地使用该模型。

rss · Simon Willison · 6月16日 16:04

**背景**: Qwen3.6-27B 是阿里巴巴 Qwen 团队于 2026 年 4 月发布的一个稠密 270 亿参数语言模型。llama.cpp 由 Georgi Gerganov 创建，是一个开源库，能够在消费级硬件上高效运行本地 LLM 推理，是 Ollama 和 LM Studio 等工具的基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-27B">Qwen/ Qwen 3 . 6 - 27 B · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://pi.dev/">Pi Coding Agent</a></li>

</ul>
</details>

**标签**: `#local LLM`, `#coding assistant`, `#llama.cpp`, `#Qwen`

---

<a id="item-14"></a>
## [FTC 诉讼揭露订阅诈骗网络规避应用商店执法的策略](https://techcrunch.com/2026/06/17/ftc-lawsuit-reveals-how-subscription-scam-networks-evade-app-store-enforcement/) ⭐️ 7.0/10

美国联邦贸易委员会（FTC）提起诉讼，揭露订阅诈骗网络如何利用空壳公司和支付基础设施，规避苹果 App Store 和 Google Play 等主要应用商店的执法。 此案凸显了应用商店执法的系统性漏洞，表明诈骗者即使在消费者投诉不断的情况下仍能活跃，这削弱了消费者信任和平台责任。 诉讼指控运营者利用空壳公司在被禁止后重新上架应用，并借助 Paddle 等支付处理商处理订阅费用，同时隐藏其身份。

rss · TechCrunch · 6月17日 19:46

**背景**: 订阅诈骗涉及通过欺骗性界面诱使用户支付高昂定期费用的应用。应用商店有禁止此类行为的政策，但执法依赖于检测和封禁违规应用。诈骗者通过创建新的空壳公司并使用充当商户记录的第三方支付平台来规避追踪和封禁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/17/ftc-lawsuit-reveals-how-subscription-scam-networks-evade-app-store-enforcement/">FTC lawsuit reveals how subscription scam networks evade app store ...</a></li>
<li><a href="https://www.subscriptioninsider.com/article-type/news/ftc-fines-paddle-5-million-for-facilitating-tech-support-scams-through-its-payment-platform">FTC Fines Paddle $5 Million for Facilitating... - Subscription Insider</a></li>

</ul>
</details>

**标签**: `#app stores`, `#subscription scams`, `#FTC`, `#consumer protection`, `#platform enforcement`

---

<a id="item-15"></a>
## [Odyssey 获亚马逊支持，估值达 14.5 亿美元](https://techcrunch.com/2026/06/17/world-model-maker-odyssey-nabs-1-45b-valuation-backed-by-amazon-and-other-big-names/) ⭐️ 7.0/10

世界模型初创公司 Odyssey 以 14.5 亿美元估值完成融资，亚马逊是投资者之一。 这表明世界模型正成为大语言模型之外 AI 领域的重要方向，吸引了大型科技公司的投资。 Odyssey 由自动驾驶先驱 Oliver Cameron 和 Jeff Hawke 创立，此前曾发布可流式传输交互式 3D 世界的模型。

rss · TechCrunch · 6月17日 17:43

**背景**: 世界模型是能够学习预测并随时间与环境交互的 AI 系统，可实现模拟和规划。它们被认为是超越大语言模型的下一个前沿，用于具身 AI 和机器人技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://odyssey.ml/">Odyssey</a></li>
<li><a href="https://techcrunch.com/2025/05/28/odysseys-new-ai-model-streams-3d-interactive-worlds/">Odyssey 's new AI model streams 3D interactive worlds | TechCrunch</a></li>

</ul>
</details>

**标签**: `#AI`, `#world models`, `#funding`, `#startup`, `#Amazon`

---