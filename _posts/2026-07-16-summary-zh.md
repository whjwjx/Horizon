---
layout: default
title: "Horizon Summary: 2026-07-16 (ZH)"
date: 2026-07-16
lang: zh
---

> 从 77 条内容中筛选出 15 条重要资讯。

---

1. [Stripe 与 Advent 联合出价超 530 亿美元收购 PayPal](#item-1) ⭐️ 9.0/10
2. [xAI 在隐私争议后开源 Grok Build](#item-2) ⭐️ 9.0/10
3. [Inkling：支持音频的开源权重多模态模型](#item-3) ⭐️ 8.0/10
4. [GPT-Red：通过自对弈红队测试提升 AI 安全性](#item-4) ⭐️ 8.0/10
5. [Claude web_fetch 工具被诱骗泄露用户记忆](#item-5) ⭐️ 8.0/10
6. [Lobste.rs 从 MariaDB 迁移到 SQLite](#item-6) ⭐️ 8.0/10
7. [摩擦即特性：Armin Ronacher 谈 AI 代理](#item-7) ⭐️ 8.0/10
8. [黑客揭露 Suno AI 从 YouTube 抓取训练数据](#item-8) ⭐️ 8.0/10
9. [苹果智能通过阿里通义千问获准在华推出](#item-9) ⭐️ 8.0/10
10. [GitHub Dependabot 默认增加 3 天冷却期](#item-10) ⭐️ 7.0/10
11. [微软培训销售团队贬低 OpenAI 和 Anthropic](#item-11) ⭐️ 7.0/10
12. [微软修复创纪录的 570 个漏洞，归功于 AI](#item-12) ⭐️ 7.0/10
13. [印度斥巨资打破中国智能手机制造垄断](#item-13) ⭐️ 7.0/10
14. [美国起诉俄罗斯‘防弹’主机服务商，涉 6200 万美元网络犯罪](#item-14) ⭐️ 7.0/10
15. [Anthropic 与黑石押注 AI 实施初创公司 Ode](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Stripe 与 Advent 联合出价超 530 亿美元收购 PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

据消息人士透露，Stripe 与私募股权公司 Advent International 联合出价超过 530 亿美元收购 PayPal。若交易完成，将合并数字支付领域的两大巨头。 此次收购将把 Stripe、PayPal、Venmo、Braintree 和 Xoom 等主要支付平台整合到同一旗下，引发重大反垄断担忧。这可能重塑在线支付格局，影响竞争、费率及商户选择。 报价对 PayPal 估值超过 530 亿美元，该交易可能因市场集中度面临严格监管审查。社区评论指出，Stripe 对某些行业（如大麻、成人内容）的限制性政策可能对目前由 PayPal 服务的商家产生负面影响。

hackernews · rvz · 7月15日 03:32 · [社区讨论](https://news.ycombinator.com/item?id=48915953)

**背景**: Stripe 是一家私营金融服务平台，为电商和移动应用提供支付处理。PayPal 是一家上市数字支付公司，旗下还拥有 Venmo、Braintree 和 Xoom。Advent International 是一家全球私募股权公司，管理资产约 1000 亿美元。反垄断担忧源于合并后的实体将控制在线非面对面交易（CNP）结账市场的很大份额。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stripe,_Inc.">Stripe, Inc. - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advent_International">Advent International</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，用户担心竞争减少、费率上升以及 Stripe 对某些行业的限制性政策。一些评论者质疑该交易能否通过反垄断审查，并提及可能被迫剥离 Venmo 或 Braintree。

**标签**: `#acquisition`, `#payments`, `#fintech`, `#antitrust`, `#stripe`

---

<a id="item-2"></a>
## [xAI 在隐私争议后开源 Grok Build](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI 在 grok CLI 工具被发现将整个目录上传到云存储、引发隐私争议后，以 Apache 2.0 许可证发布了整个 Grok Build 代码库。该公司还删除了所有保留的用户数据，并禁用了默认数据保留。 这一事件凸显了 AI 编码工具中的关键隐私风险，并为以透明和开源方式应对安全故障树立了先例。在宽松许可证下开源一个主要 AI 代码库，可以促进社区信任并实现独立安全审计。 Grok Build 仓库包含 844,530 行 Rust 代码，其中仅约 3% 为 vendored 代码，并包含一个自包含的 Mermaid 图表渲染器以及受 Codex 和 OpenCode 启发的工具实现。代码库以单个提交发布，没有提供开发历史。

rss · Simon Willison · 7月15日 23:59

**背景**: grok CLI 工具是一个由 xAI 的 Grok API 驱动的终端对话式 AI 助手。用户发现，在目录中运行该命令会将整个目录上传到 xAI 的云存储，包括 SSH 密钥和密码数据库等敏感文件。这引发了广泛批评，并导致对 xAI 隐私实践的信任丧失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>
<li><a href="https://grokcli.io/">Grok CLI - Conversational AI CLI Tool</a></li>

</ul>
</details>

**社区讨论**: 社区对隐私侵犯表达了强烈愤怒，一位用户报告说他们的整个主目录被上传。许多人欢迎开源作为积极的一步，但对 xAI 未来的数据处理做法仍持谨慎态度。

**标签**: `#security`, `#open source`, `#AI`, `#privacy`, `#xAI`

---

<a id="item-3"></a>
## [Inkling：支持音频的开源权重多模态模型](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

Thinking Machines Lab 发布了 Inkling，一个支持音频、文本和视觉的开源权重多模态模型，并可在其 Tinker 平台上进行微调。 Inkling 是支持音频的最大开源权重模型，使企业能够以比使用封闭 API 更低的成本，为特定任务定制多模态模型。 Inkling 并非整体最强的模型，但它结合了多模态能力、高效推理以及可在 Tinker 上微调的特点，使其成为定制的良好基础。

hackernews · vimarsh6739 · 7月15日 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48924912)

**背景**: 开源权重模型公开发布训练好的参数，允许任何人下载、运行和微调。多模态模型同时处理文本、图像和音频等多种数据类型，实现更丰富的理解。Inkling 被定位为定制的基础，而非性能顶尖的通用模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://allthings.how/what-is-an-open-weight-ai-model-and-how-to-use-one/">What is an Open Weight AI Model and How to Use One</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_model">Multimodal model</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Inkling 的音频支持和本地部署潜力，一些人认为它是有望替代封闭模型的开源选择。其他人则强调提供可微调基础模型的商业模式是一种经济高效的企业解决方案。

**标签**: `#open-weights`, `#multimodal`, `#AI`, `#machine learning`, `#audio`

---

<a id="item-4"></a>
## [GPT-Red：通过自对弈红队测试提升 AI 安全性](https://openai.com/index/unlocking-self-improvement-gpt-red) ⭐️ 8.0/10

OpenAI 推出了 GPT-Red，这是一个利用自对弈强化学习的自动化红队测试系统，能够持续发现并缓解提示注入等漏洞，在 GPT-5.6 上将攻击成功率降低了六倍。 这将红队测试从发布前的检查点转变为持续的安全循环，可能为整个行业的 AI 鲁棒性和对齐设定新标准。 GPT-Red 通过自对弈同时训练红队模型和多种防御者 LLM，将对抗性测试直接嵌入 OpenAI 的生产流程。

rss · OpenAI Blog · 7月15日 10:00

**背景**: 红队测试是指探测 AI 系统的漏洞，传统上由人工或静态测试完成。提示注入攻击诱使模型忽略指令，是一个持续存在的安全挑战。自对弈（模型与自身对抗）此前用于游戏 AI，但用于安全训练是新颖的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.startuphub.ai/ai-news/artificial-intelligence/2026/openai-s-gpt-red-ai-learns-to-police-itself">OpenAI's GPT-Red: AI Learns to Police Itself | StartupHub.ai</a></li>
<li><a href="https://aiweekly.co/alerts/openais-gpt-red-slashes-prompt-injection-success-on-gpt-56">OpenAI's GPT-Red Slashes Prompt-Injection Success on GPT-5.6 | AI Weekly</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#red teaming`, `#self-play`, `#prompt injection`, `#OpenAI`

---

<a id="item-5"></a>
## [Claude web_fetch 工具被诱骗泄露用户记忆](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

安全研究员 Ayush Paul 发现了一种方法，利用 Claude 的 web_fetch 工具中的漏洞——允许导航到已获取页面中嵌入的 URL——从而诱骗该工具泄露用户的私人记忆。该攻击成功提取了用户的姓名、所在城市和雇主信息。 该漏洞展示了一种针对广泛使用的 AI 助手的实际数据窃取攻击，绕过了 Anthropic 设计的保护措施。它凸显了在结合私有数据访问和外部内容获取能力的 AI 代理中，保障安全所面临的持续挑战。 该攻击仅针对 User-Agent 中包含 'Claude-User' 的客户端，以避免被检测。Anthropic 拒绝支付漏洞赏金，声称已内部发现该问题，随后通过阻止 web_fetch 跟随获取内容中的链接来堵住漏洞。

rss · Simon Willison · 7月15日 14:21

**背景**: “致命三重奏”指的是一种危险组合：AI 代理处理不可信输入、拥有敏感数据访问权限，并能通过外部工具窃取信息。Claude 的 web_fetch 工具原本设计为仅获取用户明确提供或 web_search 返回的 URL，但漏洞允许跟随已获取页面中的链接，从而使得攻击成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Docs</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted content, and external communication</a></li>

</ul>
</details>

**社区讨论**: 文章链接的 Hacker News 讨论可能包含对攻击巧妙性的评论、对 Anthropic 未支付赏金的失望，以及关于修复是否充分的争论。但输入中未提供具体评论。

**标签**: `#AI safety`, `#prompt injection`, `#data exfiltration`, `#Claude`, `#security`

---

<a id="item-6"></a>
## [Lobste.rs 从 MariaDB 迁移到 SQLite](https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything) ⭐️ 8.0/10

热门社区新闻网站 Lobste.rs 已完成从 MariaDB 到 SQLite 的迁移，报告称 CPU 和内存使用率降低、网站响应速度提升，并通过整合到单个 VPS 降低了托管成本。 此次迁移提供了一个真实案例，证明 SQLite 在中型生产级 Web 应用中的可行性，挑战了 SQLite 仅适用于小型或嵌入式场景的固有观念。 该 Rails 应用现在运行在单个 VPS 上，主 SQLite 数据库文件约 3.8GB，另有独立的缓存（1.1GB）、队列（218MB）和 Rack::Attack（555MB）数据库。迁移 PR 在 30 次提交中增加了 735 行代码并删除了 593 行。

rss · Simon Willison · 7月14日 19:44

**背景**: SQLite 是一个自包含、无服务器的数据库引擎，将数据存储在单个文件中，部署和管理简单。它常用于嵌入式系统和移动应用，但由于并发写入问题，较少用于 Web 应用。Rails 8 改进了对 SQLite 的支持，使此类迁移更加可行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codecurious.dev/articles/optimizing-sqlite-for-rails-8-production-a-complete-guide">Optimizing SQLite For Rails 8 Production: A Complete Guide</a></li>
<li><a href="https://github.com/coleifer/sqlite-web">GitHub - coleifer/sqlite-web: Web-based SQLite database ...</a></li>

</ul>
</details>

**社区讨论**: Lobsters 社区讨论（文章中有链接）包含迁移的技术细节和积极反馈，网站管理员提到显著节省资源并提升性能。一些评论者可能讨论了权衡和可扩展性限制。

**标签**: `#SQLite`, `#database migration`, `#web architecture`, `#Rails`, `#performance`

---

<a id="item-7"></a>
## [摩擦即特性：Armin Ronacher 谈 AI 代理](https://simonwillison.net/2026/Jul/14/armin-ronacher/#atom-everything) ⭐️ 8.0/10

Armin Ronacher 认为，软件项目的共同语言是通过摩擦——代码审查、对话和协调等缓慢的人工过程——来维持的，而 AI 编程代理可能会绕过这些摩擦，从而面临失去关键共同理解的风险。 这一见解挑战了当前认为 AI 代理应消除软件开发中所有摩擦的主流叙事，表明某些摩擦对于知识传递和团队协调至关重要。这对团队如何在采用 AI 工具的同时不损害集体理解具有重要影响。 Ronacher 将项目的共同语言定义为对概念、边界、不变量、所有权和系统原理的共同理解，这些存在于文档、代码、代码审查、对话和争论中。他指出，在 AI 代理出现之前，摩擦迫使开发者阅读代码、提问和协调，从而同步了人们的理解。

rss · Simon Willison · 7月14日 18:04

**背景**: 在软件工程中，共同理解对于维护大型代码库和协调团队至关重要。AI 编程代理可以快速生成和修改代码，可能绕过传统上建立这种理解的人际互动。Ronacher 的文章《The Tower Keeps Rising》探讨了这一矛盾。

**标签**: `#software engineering`, `#AI agents`, `#knowledge management`, `#collaboration`

---

<a id="item-8"></a>
## [黑客揭露 Suno AI 从 YouTube 抓取训练数据](https://techcrunch.com/2026/07/15/hack-suggests-ai-music-generator-suno-scraped-youtube-for-training-data/) ⭐️ 8.0/10

一名黑客利用员工凭证访问了 Suno 的源代码，揭露了这款 AI 音乐生成器从 YouTube 抓取了数十年的音频作为训练数据。 这一事件引发了关于 AI 训练数据实践的严重伦理和法律问题，可能影响版权法以及整个 AI 行业对数据抓取的态度。 黑客使用一名员工的凭证访问了源代码，其中包含从 YouTube 抓取数十年音频的证据。Suno 尚未对此泄露事件公开发表评论。

rss · TechCrunch · 7月15日 17:00

**背景**: Suno 是一个生成式 AI 平台，可根据文本提示创作原创音乐。AI 模型需要大量训练数据，从网络抓取内容是一种常见但有争议的做法，尤其是涉及 YouTube 等平台上的受版权保护的音乐时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://suno.com/home?ref=ai-good.cn">Suno | AI Music Generator</a></li>

</ul>
</details>

**标签**: `#AI`, `#music generation`, `#data scraping`, `#ethics`, `#copyright`

---

<a id="item-9"></a>
## [苹果智能通过阿里通义千问获准在华推出](https://techcrunch.com/2026/07/15/apple-intelligence-approved-for-launch-in-china-with-alibabas-qwen-ai/) ⭐️ 8.0/10

苹果的 AI 平台 Apple Intelligence 通过与阿里巴巴的通义千问（Qwen AI）合作，获得了在中国推出的监管批准。这项去年就有传闻的交易现已确认，标志着苹果在中国市场的 AI 雄心迈出了关键一步。 这一合作使苹果能够在中国这一关键市场提供 AI 功能，同时遵守当地法规。它也巩固了阿里巴巴在 AI 领域的地位，并加剧了与百度、腾讯等其他 AI 提供商的竞争。 Apple Intelligence 是一个个人智能系统，为 iPhone、iPad、Mac 等设备上的功能提供支持，使用设备端和基于云的 Apple Foundation Models。与阿里巴巴通义千问（一系列大语言模型）的合作，可能涉及将通义千问适配到苹果注重隐私的云基础设施上。

rss · TechCrunch · 7月15日 15:29

**背景**: Apple Intelligence 是苹果于 2024 年发布的生成式 AI 平台，将 AI 集成到照片、信息和 Siri 等应用中。要在中国运营，外国 AI 服务必须与本地公司合作并获得政府批准。阿里巴巴的通义千问（Qwen）是中国领先的大语言模型系列，既有开源版本，也通过云服务提供。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_Intelligence">Apple Intelligence - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen_(Alibaba_Cloud)">Qwen (Alibaba Cloud)</a></li>
<li><a href="https://developer.apple.com/apple-intelligence/">Apple Intelligence - Apple Developer</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#China`, `#Alibaba`, `#Qwen`

---

<a id="item-10"></a>
## [GitHub Dependabot 默认增加 3 天冷却期](https://simonwillison.net/2026/Jul/14/github-changeling/#atom-everything) ⭐️ 7.0/10

GitHub Dependabot 现在默认在打开版本更新拉取请求前等待三天，无需任何配置。 这一变化减少了过早更新带来的噪音，并通过留出时间检测恶意发布来提高供应链安全性。 冷却期适用于所有新的版本更新 PR；用户仍可通过配置自定义或禁用此功能。

rss · Simon Willison · 7月14日 22:43

**背景**: Dependabot 是 GitHub 的自动化依赖更新工具，在新版本发布时会创建拉取请求。如果没有冷却期，更新可能在发布后立即打开，从而可能引入恶意或不稳定的包。三天的延迟符合依赖冷却的行业最佳实践。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/">Dependabot version updates introduce default package cooldown</a></li>
<li><a href="https://christian-schneider.net/blog/dependency-cooldowns-supply-chain-defense/">Dependency cooldowns: a simple supply chain fix</a></li>
<li><a href="https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns">We should all be using dependency cooldowns</a></li>

</ul>
</details>

**标签**: `#dependabot`, `#github`, `#dependency-management`, `#security`, `#packaging`

---

<a id="item-11"></a>
## [微软培训销售团队贬低 OpenAI 和 Anthropic](https://techcrunch.com/2026/07/15/microsoft-is-reportedly-training-salespeople-to-talk-down-openai-and-anthropic/) ⭐️ 7.0/10

据报道，微软正在培训其销售人员，宣传其内部 AI 模型比 OpenAI 和 Anthropic 的模型更高效、更具成本效益。 这揭示了微软优先推广自家 AI 模型而非合作伙伴的战略转变，可能重塑企业 AI 竞争格局和客户选择。 培训侧重于强调微软内部模型的效率和成本优势，但未披露具体的技术基准或价格比较。

rss · TechCrunch · 7月15日 23:59

**背景**: 微软对 OpenAI 进行了大量投资，并将其模型集成到 Azure 和 Copilot 等产品中。然而，微软也在开发自己的 AI 模型（如 Phi 系列），以减少依赖并提供替代方案。此举表明其对主要 AI 合作伙伴采取了更具竞争性的姿态。

**标签**: `#Microsoft`, `#AI competition`, `#enterprise AI`, `#sales strategy`

---

<a id="item-12"></a>
## [微软修复创纪录的 570 个漏洞，归功于 AI](https://techcrunch.com/2026/07/15/microsoft-patches-record-number-of-security-vulnerabilities-citing-its-use-of-ai/) ⭐️ 7.0/10

微软 2026 年 7 月的补丁星期二修复了其产品线中创纪录的 570 个安全漏洞，并将这一增长归因于 AI 辅助发现。 这一创纪录的补丁数量表明漏洞检测能力显著提升，可能使微软产品更加安全，同时也凸显了 AI 在网络安全中日益重要的作用。 这 570 个漏洞在一次补丁星期二发布中修复，该发布发生在每月的第二个星期二。微软将发现更多漏洞归功于 AI 工具。

rss · TechCrunch · 7月15日 16:20

**背景**: 补丁星期二是微软每月发布安全更新的周期，于 2003 年正式确立。AI 辅助漏洞发现利用机器学习识别软件中的潜在安全缺陷，如果被滥用，可能同时有利于防御者和攻击者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Patch_Tuesday">Patch Tuesday</a></li>
<li><a href="https://coesecurity.com/ai-assisted-vulnerability-discovery/">AI - Assisted Vulnerability Discovery - Cybersecurity | COE Security</a></li>

</ul>
</details>

**标签**: `#security`, `#Microsoft`, `#AI`, `#vulnerability management`, `#Patch Tuesday`

---

<a id="item-13"></a>
## [印度斥巨资打破中国智能手机制造垄断](https://techcrunch.com/2026/07/15/india-bets-billions-on-breaking-chinas-grip-on-smartphone-manufacturing/) ⭐️ 7.0/10

印度宣布了一项 65 亿美元的智能手机制造计划和 133 亿美元的半导体推动计划，以深化其电子供应链。 这项巨额投资可能显著减少印度在智能手机和半导体生产上对中国的依赖，有可能重塑全球供应链并提升印度在科技行业的地位。 65 亿美元的智能手机计划旨在扩大生产规模并深化附加值，而 133 亿美元的半导体推动是更广泛的 Semicon India 计划的一部分，其中包括设计关联激励（DLI）计划。

rss · TechCrunch · 7月15日 14:39

**背景**: 印度一直试图提振国内电子制造业以减少对进口的依赖，尤其是来自中国的进口。2022 年启动的 Semicon India 计划为半导体设计和制造提供激励。随着苹果和三星等公司将生产转移到印度，印度的智能手机制造业已经增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/15/india-bets-billions-on-breaking-chinas-grip-on-smartphone-manufacturing/">India bets billions on breaking China's grip on smartphone ...</a></li>
<li><a href="https://www.india-briefing.com/news/semicon-india-program-investment-incentives-manufacturing-design-semiconductors-industry-23860.html/">What is the Semicon India Program and How Does it Work?</a></li>
<li><a href="https://www.gadgets360.com/mobiles/news/mobile-phone-manufacturing-scheme-cabinet-approval-production-supply-chain-india-11775385">Cabinet Approves Mobile Phone Manufacturing Scheme With Rs ...</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#smartphone manufacturing`, `#India`, `#supply chain`, `#geopolitics`

---

<a id="item-14"></a>
## [美国起诉俄罗斯‘防弹’主机服务商，涉 6200 万美元网络犯罪](https://techcrunch.com/2026/07/15/us-charges-russian-bulletproof-web-hosts-over-cyberattacks-that-netted-62m-from-cybercrime-victims/) ⭐️ 7.0/10

美国司法部解封了一份 2024 年的起诉书，指控三名俄罗斯公民和两家网络主机服务商运营‘防弹’托管服务，为网络攻击提供便利，导致 6200 万美元损失。 此次行动针对支撑网络犯罪的关键基础设施，可能扰乱重大勒索软件和钓鱼攻击活动。同时凸显了国际执法机构对俄罗斯网络犯罪网络的打击合作。 起诉书最初于 2024 年提交，近期才解封。被告涉嫌提供‘防弹’托管服务，无视滥用投诉和关停请求，允许犯罪分子托管恶意软件、命令与控制服务器及钓鱼网站。

rss · TechCrunch · 7月15日 14:21

**背景**: 防弹托管（BPH）是指故意无视投诉和法律关停请求的网络托管服务，为网络犯罪分子提供避风港。这些服务通常运营在法律宽松的司法管辖区，是勒索软件、僵尸网络及其他网络攻击的关键支撑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bulletproof_hosting">Bulletproof hosting</a></li>
<li><a href="https://www.intel471.com/blog/bulletproof-hosting-a-critical-cybercriminal-service">Bulletproof Hosting: A Critical Cybercriminal Service</a></li>

</ul>
</details>

**标签**: `#cybercrime`, `#law enforcement`, `#security`, `#Russia`, `#indictment`

---

<a id="item-15"></a>
## [Anthropic 与黑石押注 AI 实施初创公司 Ode](https://techcrunch.com/2026/07/15/anthropic-blackstone-bet-the-next-trillion-dollar-ai-business-is-implementation-not-models/) ⭐️ 7.0/10

Anthropic 与黑石投资了 Ode，这家初创公司将前部署工程师派驻到企业内部，以加速 AI 采用，标志着 AI 业务从以模型为中心转向以实施为中心。 此举凸显了业界日益认识到，下一个万亿美元的 AI 机遇在于企业实施，而不仅仅是构建模型，有望在各行业释放巨大的生产力提升。 Ode 的方法采用前部署工程师——这一角色由 Palantir 首创——他们在客户现场工作，定制 AI 系统并将其集成到现有工作流程中，解决 AI 采用的最后一公里挑战。

rss · TechCrunch · 7月15日 13:10

**背景**: 前部署工程师（FDE）是面向客户的软件工程师，他们在客户的运营环境中开发和部署软件，将软件开发与直接协作相结合。这一模式由 Palantir 等公司推广，现在被应用于 AI 领域，许多企业难以从试点项目过渡到全面部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Forward_Deployed_Engineer">Forward Deployed Engineer</a></li>
<li><a href="https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers">What are Forward Deployed Engineers, and why are they so in ...</a></li>
<li><a href="https://www.geeksforgeeks.org/blogs/forward-deployed-engineer-role-skills-salary-roadmap/">Forward Deployed Engineer (FDE): Role, Skills, Salary ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#enterprise`, `#implementation`, `#Anthropic`, `#startup`

---