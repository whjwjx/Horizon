---
layout: default
title: "Horizon Summary: 2026-07-18 (ZH)"
date: 2026-07-18
lang: zh
---

> 从 76 条内容中筛选出 15 条重要资讯。

---

1. [AWS 计费错误显示 17 亿美元预估账单](#item-1) ⭐️ 9.0/10
2. [Firefox 被编译为 WebAssembly 在另一浏览器中运行](#item-2) ⭐️ 9.0/10
3. [Thinking Machines Lab 发布 975B 参数开源权重模型 Inkling](#item-3) ⭐️ 9.0/10
4. [xAI 在隐私争议后开源 Grok Build](#item-4) ⭐️ 9.0/10
5. [Anthropic Python SDK v0.117.0 新增 Dreaming 和 MCP Tunnels](#item-5) ⭐️ 8.0/10
6. [首次在宜居带岩质系外行星上发现大气层](#item-6) ⭐️ 8.0/10
7. [月之暗面发布 Kimi K3，2.8 万亿参数开源权重模型](#item-7) ⭐️ 8.0/10
8. [GPT-5.6 Codex 漏洞可删除 $HOME 目录](#item-8) ⭐️ 8.0/10
9. [Linus Torvalds：Linux 不反 AI，不同意就分叉](#item-9) ⭐️ 8.0/10
10. [CMOV 指令：因假依赖而意外昂贵](#item-10) ⭐️ 8.0/10
11. [1193 个后端服务被追加操作阻塞](#item-11) ⭐️ 8.0/10
12. [旧金山要求苹果和谷歌下架“脱衣”应用](#item-12) ⭐️ 7.0/10
13. [苹果诉讼可能扰乱 OpenAI 的 IPO 计划](#item-13) ⭐️ 7.0/10
14. [Patreon 联合 Cloudflare 主动拦截 AI 爬虫，不再依赖 robots.txt](#item-14) ⭐️ 7.0/10
15. [Zoox 因烟雾混淆召回自动驾驶出租车](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AWS 计费错误显示 17 亿美元预估账单](https://news.ycombinator.com/item?id=48945241) ⭐️ 9.0/10

AWS 计费系统的一个错误导致许多用户看到高达 17 亿美元的预估账单，原因是单位转换错误，将字节误用为千兆字节。 此事件凸显了云服务中准确计费的极端重要性，因为此类错误可能引发恐慌并削弱客户的信任，尤其是小型企业和个人开发者。 该错误发生在计费系统将数据传输费用默认以字节而非千兆字节计算时，导致成本被放大了约 10 亿倍。AWS 已确认该问题并迅速修复。

hackernews · nprateem · 7月17日 09:42

**背景**: AWS 计费系统汇总来自各项服务的使用数据，并应用定价计划生成预估账单。定价计划定义中的单位转换错误可能导致预估金额严重虚高，正如本次事件所示。

**社区讨论**: 社区反应既幽默又担忧，许多用户分享了自己看到巨额预估账单的经历。一些评论者指出，AWS 之前也发生过类似的单位错误，表明这是一个反复出现的问题。

**标签**: `#AWS`, `#billing`, `#bug`, `#cloud`, `#incident`

---

<a id="item-2"></a>
## [Firefox 被编译为 WebAssembly 在另一浏览器中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 成功将完整的 Firefox 浏览器编译为 WebAssembly，使其能够在 Chrome 等另一浏览器中运行。该项目使用了价值约 25,000 美元的 AI 代币（Claude Opus 和 Fable），但由于订阅计划，实际成本低得多。 这展示了一项突破性的技术成就，可能实现新的浏览器隔离、安全性和基于 Web 的计算水平。它也展示了 WebAssembly 在浏览器中运行复杂、全功能应用的潜力。 该演示使用 Wisp 协议将所有网络流量通过 Puter 的服务器转发，因为浏览器中的代码无法打开任意网络连接。该项目选择 Firefox/Gecko 是因为其强大的单进程支持，并声称支持端到端加密。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly (Wasm) 是一种低级二进制指令格式，在现代浏览器中以接近原生的性能运行，允许 C/C++ 和 Rust 等语言编译到 Web。将像 Firefox 这样的完整浏览器编译为 Wasm 是一项极其复杂的任务，因为浏览器的体积和依赖关系。Wisp 协议是一种低开销协议，用于通过单个 WebSocket 连接代理多个 TCP/UDP 套接字。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly">WebAssembly - MDN Web Docs - Mozilla</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常积极，许多人对这一技术壮举印象深刻。一些评论提到了由于流量激增带来的服务器扩展挑战，并且人们对这种设置的实际应用和局限性感到好奇。

**标签**: `#WebAssembly`, `#Firefox`, `#browser engineering`, `#compilation`, `#demo`

---

<a id="item-3"></a>
## [Thinking Machines Lab 发布 975B 参数开源权重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

由 Mira Murati 创立的 Thinking Machines Lab 发布了 Inkling，这是一个总参数 975B（激活参数 41B）的混合专家多模态模型，采用 Apache-2.0 许可证，基于 45 万亿 token 的文本、图像、音频和视频数据训练。 此次发布增强了美国开源权重 AI 生态系统，为中国开源模型提供了有竞争力的替代方案，并通过 Tinker 平台为微调提供了强大的基础。 模型卡片内容简略，训练数据文档极少，该模型并非前沿模型，而是旨在作为定制化的基础。一个更小的 276B（激活参数 12B）变体 Inkling-Small 仍在测试中。

rss · Simon Willison · 7月16日 15:35

**背景**: 混合专家（MoE）模型使用多个专门的子网络（专家）和门控机制，每个输入仅激活部分参数，从而在较低计算成本下实现更大的总参数量。开源权重模型在 Apache-2.0 等宽松许可证下发布训练好的参数，允许自由使用、修改和分发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you've been told</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#Mira Murati`

---

<a id="item-4"></a>
## [xAI 在隐私争议后开源 Grok Build](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI 已将其 Grok Build 整个代码库以 Apache 2.0 许可证开源，此前其 CLI 工具被发现会上传整个目录到云端，包括用户敏感文件。该公司还禁用了上传功能，并删除了所有之前保留的用户数据。 此事件凸显了 AI 驱动开发工具中的严重隐私风险，并通过开源整个代码库为透明度树立了先例。此举可能恢复用户信任，并影响其他 AI 公司处理数据隐私的方式。 Grok Build 仓库包含 844,530 行 Rust 代码，其中仅约 3% 为第三方依赖，并包含一个自包含的 Mermaid 图表终端渲染器。代码库以单个提交发布，因此看不到开发历史。

rss · Simon Willison · 7月15日 23:59

**背景**: Grok Build 是 xAI 基于终端的 AI 编程代理，以全屏 TUI 运行，能够编辑文件、执行 shell 命令和管理任务。Apache 2.0 许可证是一种宽松的开源许可证，允许用户自由使用、修改和分发软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xai-org/grok-build">xai-org/grok-build - GitHub</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>

</ul>
</details>

**社区讨论**: 社区对隐私侵犯表示愤怒，一名用户报告称在其主目录中运行该工具会上传 SSH 密钥和密码数据库。Elon Musk 回应承诺删除所有上传的数据，开源举措被视为重获信任的积极一步。

**标签**: `#AI`, `#privacy`, `#open source`, `#xAI`, `#CLI`

---

<a id="item-5"></a>
## [Anthropic Python SDK v0.117.0 新增 Dreaming 和 MCP Tunnels](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0) ⭐️ 8.0/10

Anthropic 发布了 Python SDK 的 v0.117.0 版本，新增了对 dreaming 和 MCP Tunnels 的 API 支持，并通过使用 SecretStr 修复了凭据安全问题，防止凭据出现在回溯帧中。 这些功能使开发者能够构建具有持久记忆的自我改进型 AI 代理（dreaming），并安全地连接到私有 MCP 服务器（MCP Tunnels），显著扩展了 Anthropic 平台的企业级能力和安全性。 Dreaming 处于研究预览阶段，仅限 Managed Agents 使用，允许代理回顾过去的会话并存储精选记忆。MCP Tunnels 同样处于研究预览阶段，通过仅出站连接访问私有 MCP 服务器，无需开放入站端口。

github · stainless-app[bot] · 7月16日 19:36

**背景**: Anthropic 的 Claude 平台提供 Managed Agents，这是一种用于多步骤任务的预构建代理框架。Dreaming 允许代理从过去的会话中创建精选记忆存储，从而提升未来性能。MCP Tunnels 通过 Model Context Protocol 提供了一种安全方式，将 Claude 连接到内部系统，而无需将其暴露在公共互联网上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/">Anthropic's Claude Managed Agents can now "dream," sort of - Ars Technica</a></li>
<li><a href="https://www.infoq.com/news/2026/05/claude-mcp-tunnels/">Anthropic Introduces MCP Tunnels for Private Agent Access to Internal Systems - InfoQ</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview">MCP tunnels - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#SDK`, `#Python`, `#API`, `#AI`

---

<a id="item-6"></a>
## [首次在宜居带岩质系外行星上发现大气层](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

天文学家利用詹姆斯·韦伯太空望远镜在距离地球 48 光年的红矮星宜居带内的岩质系外行星 LHS 1140 b 上探测到了大气层。这是首次在宜居带类地行星上确认存在大气层。 这一发现是系外行星科学的重要里程碑，表明宜居带岩质行星能够保留大气层，这是潜在宜居性的关键条件。同时，它也展示了韦伯望远镜表征温和类地世界的能力，使我们更接近发现地球以外的生命迹象。 LHS 1140 b 的质量约为地球的 5.6 倍，半径约为 1.7 倍，属于超级地球类别，很可能是一个海洋世界，水质量占比 9-19%。该行星接收到的恒星辐射通量仅为地球的 43%，其大气层是通过韦伯望远镜在其掩星时进行的发射光谱分析确认的。

hackernews · neversaydie · 7月17日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=48947560)

**背景**: LHS 1140 b 于 2017 年由 MEarth 项目发现，最初被认为是一颗致密岩质行星，但后续测量显示其密度较低，符合富水世界的特征。宜居带是指恒星周围液态水可能存在于行星表面的区域。像 LHS 1140 这样的红矮星比太阳更冷更小，其宜居带非常靠近恒星，这曾引发对恒星活动导致大气层剥离的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LHS_1140_b">LHS 1140 b</a></li>
<li><a href="https://www.bbc.com/news/articles/cy4kdd1e0ejo">First atmosphere found around Earth-like planet LHS 1140 b</a></li>
<li><a href="https://lweb.cfa.harvard.edu/MEarth/lhs1140b.pdf">LHS 1140 b _arXiv</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了兴奋与怀疑的混合情绪。有人质疑红矮星周围的岩质行星能否保留大气层，但其他人指出韦伯数据排除了迷你海王星的可能性。讨论还涉及费米悖论和技术文明短暂的时间窗口，以及建议建造太阳透镜望远镜用于未来观测。

**标签**: `#exoplanets`, `#astronomy`, `#JWST`, `#habitability`, `#atmosphere`

---

<a id="item-7"></a>
## [月之暗面发布 Kimi K3，2.8 万亿参数开源权重模型](https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything) ⭐️ 8.0/10

月之暗面发布了 Kimi K3，这是一个拥有 2.8 万亿参数的开源权重模型，在多项基准测试中超越了 GPT-5.5 和 Claude Opus 4.8，并承诺在 2026 年 7 月 27 日前开放权重。 Kimi K3 是迄今为止最大的开源权重模型，标志着开放 AI 研究规模的新前沿，并可能使尖端能力更加普及。 该模型每百万输入令牌收费 3 美元，每百万输出令牌收费 15 美元，是中国 AI 实验室发布的最贵模型；在 Artificial Analysis Intelligence Index 上，其输出令牌使用量比前代 K2.6 减少了 21%。

rss · Simon Willison · 7月16日 20:19

**背景**: 开源权重模型发布训练好的参数但不包含完整训练流程，允许研究人员微调和部署。月之暗面是中国“AI 六虎”之一，与 OpenAI 和 Anthropic 等前沿实验室竞争。“鹈鹕基准测试”是一个非正式测试，要求模型生成骑自行车的鹈鹕的 SVG 图像，用于定性比较模型能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/16/kimi-k3/">Kimi K3, and what we can still learn from the pelican benchmark</a></li>
<li><a href="https://huggingface.co/spaces/victor/pelican-benchmark">Pelican Benchmark - a Hugging Face Space by victor</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI</a></li>

</ul>
</details>

**社区讨论**: 输入中未提供社区讨论内容，因此该字段留空。

**标签**: `#AI`, `#large language models`, `#open-weight`, `#benchmarks`, `#Moonshot AI`

---

<a id="item-8"></a>
## [GPT-5.6 Codex 漏洞可删除 $HOME 目录](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

GPT-5.6 的 Codex 代理存在一个漏洞：在启用完全访问模式且未使用沙箱保护时，它可能错误地删除用户的 $HOME 目录而非临时目录。 该漏洞凸显了 AI 编码代理中的关键安全风险——如果未正确沙箱化，可能造成破坏性后果，尤其是在这些代理变得越来越自主的情况下。 该漏洞发生在 Codex 尝试覆盖 $HOME 环境变量以定义临时目录时，却错误地删除了 $HOME。触发条件包括启用完全访问模式、未使用沙箱保护以及未开启自动审查。

rss · Simon Willison · 7月16日 17:45

**背景**: Codex 是 OpenAI 推出的 AI 编码代理，可在本地或云端运行，用于自动化软件工程任务。沙箱化技术将代理的执行环境隔离，防止其影响宿主系统。$HOME 环境变量指向用户的主目录，其中包含个人文件和配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in your terminal · GitHub</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor... — Northflank</a></li>
<li><a href="https://www.hostinger.com/tutorials/linux-environment-variables">How to Manage Linux Environment Variables in 2026 + Tips</a></li>

</ul>
</details>

**标签**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-9"></a>
## [Linus Torvalds：Linux 不反 AI，不同意就分叉](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds 在 Linux Media 邮件列表中明确表示 Linux 不是一个反 AI 的项目，并称 AI 是明显有用的工具，邀请持不同意见者分叉内核或离开。 来自 Linux 创始人的强力背书标志着重大政策立场，可能影响开源社区对在内核开发及其他领域使用 AI 工具的接受度。 Torvalds 强调 AI 的实用性已毋庸置疑，尽管他承认关于 AI 经济影响的其他问题仍然存在。该声明是在内核开发讨论的背景下作出的。

rss · Simon Willison · 7月16日 13:26

**背景**: Linus Torvalds 是 Linux 内核的创建者和长期维护者，Linux 内核是最大的开源项目之一。AI 工具，尤其是大型语言模型，越来越多地被用于软件开发，但一些社区成员提出了伦理和实际方面的担忧。

**标签**: `#Linux`, `#AI`, `#Open Source`, `#Kernel Development`

---

<a id="item-10"></a>
## [CMOV 指令：因假依赖而意外昂贵](https://www.reddit.com/r/programming/comments/1uyt0tf/the_most_expensive_instruction_might_be_cmov/) ⭐️ 8.0/10

一项技术分析揭示，x86 上的 CMOV（条件移动）指令由于假依赖和寄存器压力增加，可能意外地昂贵，挑战了它总是优于分支的普遍看法。 这一见解对底层优化和系统编程至关重要，因为开发者常使用 CMOV 来避免分支预测错误惩罚，但在某些场景下可能无意中降低性能。 CMOV 指令对目标寄存器产生假依赖，将其与之前的计算绑定，限制了乱序执行。此外，使用 CMOV 会增加寄存器压力，可能导致溢出和进一步的性能下降。

reddit · r/programming · /u/_shadowbannedagain · 7月17日 07:44

**背景**: CMOV 是 x86 指令，根据标志条件移动数据，避免分支预测错误。然而，在乱序 CPU 上，它引入了数据依赖，可能导致流水线停顿。CMOV 与条件分支之间的权衡取决于分支可预测性和代码大小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rcollins.org/p6/opcodes/CMOV.html">New P6 OpCodes: CMOV - Conditional Move - rcollins.org</a></li>
<li><a href="https://www.reddit.com/r/programming/comments/8fqgy/cmov_instruction_a_bad_idea_on_outoforder_cpus/">r/programming on Reddit: CMOV instruction a bad idea on out-of-order CPUs - a.k.a. why to compile for i586 not i686</a></li>

</ul>
</details>

**社区讨论**: Reddit 讨论指出，CMOV 在较新核心上的性能有所改善，但三重输入依赖问题仍然存在。一些评论者指出编译器经常过度使用 CMOV，手动调优仍是获得最佳性能所必需的。

**标签**: `#x86`, `#assembly`, `#performance`, `#optimization`, `#low-level`

---

<a id="item-11"></a>
## [1193 个后端服务被追加操作阻塞](https://www.reddit.com/r/programming/comments/1uzdl0h/1193_backends_waiting_on_an_append/) ⭐️ 8.0/10

一项深入分析揭示，1193 个后端服务因等待一个追加操作而被阻塞，暴露了分布式系统中的严重性能瓶颈。 这种瓶颈可能导致级联故障并降低系统吞吐量，凸显了在分布式数据库或日志系统中谨慎设计追加密集型工作负载的迫切需求。 该分析可能涉及复制日志（如 Raft），其中所有写入都通过单个领导者，使得追加操作成为序列化点。数字 1193 表明这是一个大规模部署，许多追随者等待领导者的追加操作完成。

reddit · r/programming · /u/andreiross · 7月17日 22:01

**背景**: 在 Raft 等分布式共识算法中，所有写操作必须先追加到领导者的日志，然后才能复制到追随者。在高写入负载下，领导者成为瓶颈，因为每次追加必须完成后才能进行下一次。这种设计确保了一致性，但当许多后端依赖同一个领导者时，可能导致性能问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@Omkar-Wagholikar/distributed-systems-deep-dive-single-leader-replication-0a96fb303036">Distributed Systems Deep Dive: Single Leader Replication | by Omkar Wagholikar | Medium</a></li>
<li><a href="https://medium.com/@vishalgoel2668/solving-performance-bottlenecks-in-complex-distributed-systems-a-practical-guide-7015f2fba76f">Solving Performance Bottlenecks in Complex Distributed Systems: A Practical Guide | by Vishalgoel | Medium</a></li>

</ul>
</details>

**标签**: `#distributed systems`, `#performance`, `#backend`, `#database`, `#concurrency`

---

<a id="item-12"></a>
## [旧金山要求苹果和谷歌下架“脱衣”应用](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/) ⭐️ 7.0/10

旧金山市检察官 David Chiu 致函苹果和谷歌，要求它们从应用商店中移除“脱衣”应用，理由是这些应用违反了州法律。 这一监管行动针对大型科技平台上的有害深度伪造应用，可能为应用商店政策和用户安全执法树立先例。 信件称苹果和谷歌长期知道它们托管了违反州法律的应用。“脱衣”应用使用 AI 生成未经同意的深度伪造裸体图像，这在许多司法管辖区是非法的。

rss · TechCrunch · 7月17日 19:49

**背景**: 深度伪造色情内容利用 AI 修改照片或视频，未经同意描绘个人裸体，常被用于报复色情。这类技术已存在多年，但通过应用和在线工具变得更加易得，引发了法律和监管审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nudify_apps">Nudify apps</a></li>
<li><a href="https://www.theguardian.com/news/ng-interactive/2026/jan/11/how-grok-nudification-tool-went-viral-x-elon-musk">‘Add blood, forced smile’: how Grok’s nudification tool... | The Guardian</a></li>

</ul>
</details>

**标签**: `#app stores`, `#regulation`, `#privacy`, `#safety`, `#tech policy`

---

<a id="item-13"></a>
## [苹果诉讼可能扰乱 OpenAI 的 IPO 计划](https://techcrunch.com/video/how-apples-big-lawsuit-could-disrupt-openais-ipo-plans/) ⭐️ 7.0/10

苹果上周五对 OpenAI 提起商业秘密诉讼，指控其存在不当行为模式，并声称超过 400 名前苹果员工现在在 OpenAI 工作。该诉讼可能扰乱 OpenAI 传闻中的 IPO 计划。 该诉讼可能延迟或破坏 OpenAI 的 IPO，影响其估值和融资能力。这也凸显了主要科技公司之间在 AI 人才和知识产权方面的激烈竞争。 诉状指控不当行为涉及 OpenAI 的首席硬件官。OpenAI 的回应谨慎，而时机至关重要，因为该公司据称正在考虑 IPO。

rss · TechCrunch · 7月17日 17:45

**背景**: 商业秘密诉讼是保护机密商业信息的法律行动。苹果和 OpenAI 是 AI 领域的主要参与者，苹果专注于设备端 AI，而 OpenAI 专注于大型语言模型。该诉讼指控 OpenAI 雇佣了前苹果员工，这些员工带来了商业秘密。

**标签**: `#Apple`, `#OpenAI`, `#lawsuit`, `#IPO`, `#AI`

---

<a id="item-14"></a>
## [Patreon 联合 Cloudflare 主动拦截 AI 爬虫，不再依赖 robots.txt](https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/) ⭐️ 7.0/10

Patreon 与 Cloudflare 合作，主动拦截 AI 爬虫抓取创作者内容，不再仅依赖自愿遵守的 robots.txt 协议。 这一转变标志着在对抗未经授权的 AI 训练数据收集方面的重要升级，为其他平台采取主动拦截措施、更好地保护创作者权益树立了先例。 Patreon 使用 Cloudflare 的 Bot Management 服务，该服务在网络边缘实时检测和缓解机器人流量，且不会为合法用户增加延迟。此举正值 2023 年至 2024 年 AI 爬虫流量增长 340% 之际。

rss · TechCrunch · 7月17日 15:21

**背景**: Robots.txt 是 1994 年制定的标准，用于告知网络爬虫可以访问网站的哪些部分，但遵守是自愿的，且常被 AI 公司忽视。Cloudflare 的 Bot Management 提供细粒度控制、每次请求的机器人评分以及自动拦截恶意机器人，比被动的文本文件更有效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/bots/get-started/bot-management/">Bot Management · Cloudflare bot solutions docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Robots.txt">robots . txt - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI scraping`, `#Patreon`, `#Cloudflare`, `#creator rights`, `#web scraping`

---

<a id="item-15"></a>
## [Zoox 因烟雾混淆召回自动驾驶出租车](https://techcrunch.com/2026/07/17/zoox-issues-software-recall-after-a-robotaxi-got-confused-by-heavy-smoke/) ⭐️ 7.0/10

Zoox 在 2026 年 6 月一辆自动驾驶出租车未能应对火灾现场的浓烟后，对 105 辆自动驾驶出租车发布了软件召回。该公司已部署软件更新以解决该问题。 这一事件凸显了自动驾驶汽车的一个关键失效模式——浓烟，并且正值 NHTSA 加强监管审查之际，该机构警告称，干扰急救人员的自动驾驶汽车对公众构成危险。 此次召回涉及 105 辆 Zoox 自动驾驶出租车，软件更新旨在改善烟雾环境下的检测和导航能力。此前，Zoox 在 2025 年 12 月因涉及车道穿越的单独软件错误召回了 332 辆车。

rss · TechCrunch · 7月17日 14:12

**背景**: 自动驾驶汽车依赖摄像头、激光雷达和雷达等传感器来感知环境。浓烟会降低传感器性能，导致混淆。NHTSA 最近警告自动驾驶汽车开发者，车辆必须安全地与急救人员互动，并引用了多起干扰事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/17/amazon-zoox-recalls-robotaxi-smoke.html">Amazon's Zoox issues software recall after robotaxi drove into heavy smoke</a></li>
<li><a href="https://techcrunch.com/2026/07/17/zoox-issues-software-recall-after-a-robotaxi-got-confused-by-heavy-smoke/">Zoox issues software recall after a robotaxi got confused by heavy smoke | TechCrunch</a></li>
<li><a href="https://www.nhtsa.gov/press-releases/av-developers-automated-vehicle-that-cannot-safely-interact-first-responders-danger">Trump’s Transportation Department to AV Developers: ‘An Automated Vehicle That Cannot Safely Interact With First Responders is a Danger to the General Public’ | NHTSA</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#software recall`, `#safety`, `#regulation`, `#Zoox`

---