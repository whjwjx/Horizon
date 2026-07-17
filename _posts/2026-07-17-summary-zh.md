---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> 从 87 条内容中筛选出 15 条重要资讯。

---

1. [Firefox 编译为 WebAssembly 在 Chrome 中运行](#item-1) ⭐️ 9.0/10
2. [xAI 因隐私争议开源 Grok Build](#item-2) ⭐️ 9.0/10
3. [Moonshot AI 发布 Kimi K3 开放权重前沿模型](#item-3) ⭐️ 8.0/10
4. [OpenAI 的 GPT-Red：通过自对弈提升 AI 安全性](#item-4) ⭐️ 8.0/10
5. [GPT-5.6 Codex 漏洞删除用户文件](#item-5) ⭐️ 8.0/10
6. [Thinking Machines Lab 发布 975B 开放权重模型 Inkling](#item-6) ⭐️ 8.0/10
7. [Linus Torvalds 为 Linux 内核使用 AI 辩护](#item-7) ⭐️ 8.0/10
8. [研究人员诱骗 Claude 泄露私人记忆](#item-8) ⭐️ 8.0/10
9. [Cursor 零日漏洞被公开披露以保护用户](#item-9) ⭐️ 8.0/10
10. [数百万鲨鱼机器人吸尘器存在远程代码执行漏洞](#item-10) ⭐️ 8.0/10
11. [微软 Comic Chat 开源，时隔 30 年](#item-11) ⭐️ 7.0/10
12. [诱饵字体：用光学幻觉字体迷惑 AI 视觉模型](#item-12) ⭐️ 7.0/10
13. [OpenAI 提出 AI 安全的逆向联邦制方案](#item-13) ⭐️ 7.0/10
14. [旧金山市长在 Waymo 交通堵塞后寻求更严格的机器人出租车规定](#item-14) ⭐️ 7.0/10
15. [Uber 以 148 亿美元收购 Delivery Hero](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Firefox 编译为 WebAssembly 在 Chrome 中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 已将完整的 Firefox 浏览器编译为 WebAssembly，使其能够在 Chrome 等其他浏览器中完全运行。演示在 Chrome 中的 Firefox-in-WASM 里加载了一个博客，所有网络流量通过 Wisp 协议代理。 这是一项突破性的技术成就，展示了 WebAssembly 的极致能力，可能开启新的用例，如浏览器内沙盒浏览、遗留应用兼容性和高级 Web 平台实验。该项目还凸显了 AI 辅助编程的力量，估计使用了价值 25,000 美元的 AI 代币。 该项目选择 Firefox/Gecko 是因为其强大的单进程支持，构建过程估计使用了价值 25,000 美元的 Claude Opus 和 Fable 代币。所有网络流量通过 Wisp 协议经 WebSocket 经由 Puter 的服务器转发，该服务器不得不扩容以应对 Hacker News 带来的流量。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly (WASM) 是一种低级二进制指令格式，允许用 C、C++ 和 Rust 等语言编写的代码以接近原生的速度在 Web 浏览器中运行。将 Firefox 这样的完整浏览器编译为 WASM 是一项巨大的工程挑战，因为浏览器是复杂的多进程应用程序，依赖于通常不在浏览器沙箱中可用的系统级 API。Wisp 协议是一种低开销协议，用于通过单个 WebSocket 连接代理多个 TCP 和 UDP 套接字，这是必要的，因为浏览器中的 WASM 代码无法直接打开任意网络连接。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low ...</a></li>
<li><a href="https://github.com/HeyPuter/puter">GitHub - HeyPuter/puter: 🌐 The Internet Computer! Free, Open-Source, and Self-Hostable.</a></li>
<li><a href="https://github.com/fable-compiler/fable">GitHub - fable-compiler/Fable: F# to JavaScript, TypeScript, Python, Rust, Erlang and Dart Compiler · GitHub</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常积极，许多人对这一技术壮举表示惊叹。一些评论者对所有流量通过 Puter 服务器代理的成本和可扩展性表示担忧，而其他人则讨论了类似项目（如 WebKitWASM）的潜力。

**标签**: `#WebAssembly`, `#Firefox`, `#browser engineering`, `#WASM`, `#Puter`

---

<a id="item-2"></a>
## [xAI 因隐私争议开源 Grok Build](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI 在 GitHub 上以 Apache 2.0 许可证发布了整个 Grok Build 代码库，此前用户发现该 CLI 工具会将整个目录上传到 Google Cloud 存储桶。该公司还删除了所有保留的用户数据，并禁用了默认数据保留。 这一事件凸显了 AI 编码工具中的严重隐私风险，并迫使 xAI 采取前所未有的透明度措施，包括开源一个主要产品。此举可能为 AI 辅助开发工具的隐私保护树立新标准。 该代码库包含 844,530 行 Rust 代码（仅约 3% 为第三方依赖），只有一个提交，因此无法看到开发历史。上传代码的残留部分仍在仓库中，但已被禁用。

rss · Simon Willison · 7月15日 23:59

**背景**: Grok Build 是 xAI 的 AI 辅助编码 CLI 工具，由 Grok 模型驱动。隐私问题曝光于用户发现该工具在未经明确同意的情况下将整个目录（包括 SSH 密钥和密码数据库）上传到 xAI 的 Google Cloud 存储桶。xAI 最初禁用了该功能，随后开源代码以重建信任。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/15/grok-build/">xai-org/grok-build, now open source</a></li>
<li><a href="https://www.internationalcyberdigest.com/xais-grok-build-cli-uploads-entire-git-repositories-to-a-google-cloud-bucket/">xAI's Grok Build CLI Uploads Entire Git repositories to a Google Cloud Bucket</a></li>
<li><a href="https://glitchwire.com/news/xais-grok-build-cli-was-uploading-entire-repositories-to-google-cloud-the-compan/">xAI's Grok Build CLI Was Uploading Entire Repositories to Google Cloud. The Company Has Said Nothing. — Glitchwire</a></li>

</ul>
</details>

**社区讨论**: 社区反应极为负面，用户对隐私侵犯表示愤怒并要求透明度。一些人称赞开源是积极的一步，但其他人对 xAI 处理事件的方式仍持怀疑态度。

**标签**: `#privacy`, `#open source`, `#AI`, `#security`, `#xAI`

---

<a id="item-3"></a>
## [Moonshot AI 发布 Kimi K3 开放权重前沿模型](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI 发布了 Kimi K3，这是一个开放权重的前沿 AI 模型，据内部评估其性能仅次于 Claude Fable 5 和 GPT-5.6 Sol，完整模型权重将在未来几天内发布。 Kimi K3 的开放权重发布可能加速 AI 智能的商品化，挑战美国前沿实验室的主导地位，并为开发者和企业提供高性价比的替代方案。 该模型可通过 OpenRouter API 以有竞争力的价格使用（例如，一个长推理查询仅需 0.25 美元），且 Moonshot AI 会使用 API 使用数据进行训练，除非另有企业协议。

hackernews · vincent_s · 7月16日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=48935342)

**背景**: 开放权重模型是指其核心参数公开发布的 AI 模型，任何人都可以下载和使用。前沿模型是最先进的通用 AI 模型，通常需要数亿美元的训练成本。以 Moonshot 为代表的中国 AI 实验室正越来越多地发布具有竞争力的开放权重模型，延续了 DeepSeek 开创的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 Moonshot 使用 API 数据进行训练的政策表示担忧，有用户注意到长推理查询的高昂成本。另一位评论者指出，中国实验室正推动智能商品化，可能是一种销售硬件和基础设施的策略。

**标签**: `#AI`, `#open-source`, `#LLM`, `#benchmarks`, `#Moonshot`

---

<a id="item-4"></a>
## [OpenAI 的 GPT-Red：通过自对弈提升 AI 安全性](https://openai.com/index/unlocking-self-improvement-gpt-red) ⭐️ 8.0/10

OpenAI 推出了 GPT-Red，这是一个利用自对弈来自动化红队测试的系统，旨在提升 AI 的安全性、对齐能力以及对提示注入攻击的鲁棒性。 这种方法自动化了关键的安全评估流程，可能减少对大量人工红队测试的需求，并实现模型鲁棒性的持续改进。它直接应对了日益增长的提示注入威胁，这是已部署 AI 代理面临的主要安全挑战。 GPT-Red 是一个基于 LLM 的红队测试器，在自对弈框架中扮演对抗角色，生成多样化的提示注入攻击。OpenAI 报告称，使用 GPT-Red 训练的 GPT-5.6 Sol 在直接提示注入基准测试中的失败次数比 GPT-5.5 减少了六倍。

rss · OpenAI Blog · 7月15日 10:00

**背景**: 红队测试是一种安全实践，测试者模拟攻击以发现漏洞。在 AI 安全领域，人类红队测试者手动构造提示来破解模型。自对弈是一种 AI 系统通过与自身对抗来改进的技术，常用于游戏 AI。提示注入攻击利用 LLM 无法区分系统指令和用户提供内容的弱点，对处理外部数据的 AI 代理构成风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/unlocking-self-improvement-gpt-red/">GPT-Red: Unlocking Self-Improvement for Robustness | OpenAI</a></li>
<li><a href="https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html">OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden ...</a></li>
<li><a href="https://www.technologyreview.com/2026/07/15/1140514/meet-gpt-red-an-llm-super-hacker-openai-built-to-make-its-models-safer/">Meet GPT-Red: an LLM super-hacker OpenAI built to make its ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#red teaming`, `#self-play`, `#alignment`, `#prompt injection`

---

<a id="item-5"></a>
## [GPT-5.6 Codex 漏洞删除用户文件](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

GPT-5.6 Codex 的一个漏洞在启用完全访问模式且未使用沙箱时，会因模型错误地删除 $HOME 而非临时目录，导致用户文件被删除。 该漏洞对 AI 编码代理构成严重安全风险，可能导致在未使用适当沙箱或审查的情况下运行 Codex 的用户遭受不可逆的数据丢失。这凸显了自主 AI 系统中强健安全措施的必要性。 该漏洞发生在启用完全访问模式、禁用沙箱且关闭自动审查的情况下。模型试图覆盖 $HOME 以定义临时目录，但错误地删除了 $HOME。

rss · Simon Willison · 7月16日 17:45

**背景**: GPT-5.6 Codex 是一个 AI 编码代理，可以自主读取、编写和执行用户机器上的代码。完全访问模式授予代理广泛的权限，而沙箱则将其隔离以防止有害操作。没有沙箱，错误的命令会直接影响用户的文件系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/openai-codex-gpt-5-6-home-deletion-full-access-july-2026">Codex GPT-5.6 $HOME Deletion — Full Access | explainx.ai Blog</a></li>
<li><a href="https://github.com/openai/codex/issues/4407">Change the hardcoded $HOME/.codex path #4407 - GitHub</a></li>
<li><a href="https://amux.io/guides/ai-agent-sandboxing/">AI Agent Sandboxing in 2026: Docker, E2B, Firecracker... — amux</a></li>

</ul>
</details>

**标签**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`

---

<a id="item-6"></a>
## [Thinking Machines Lab 发布 975B 开放权重模型 Inkling](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

由 Mira Murati 领导的 Thinking Machines Lab 发布了 Inkling，这是一个 975B 参数、开放权重的多模态混合专家模型，采用 Apache-2.0 许可证。该模型有 41B 活跃参数，并在 45 万亿个文本、图像、音频和视频 token 上进行了训练。 此次发布增强了美国开放权重生态系统，为中国开放模型和 NVIDIA Nemotron 提供了有竞争力的替代方案。其 Apache-2.0 许可证和多模态能力使其成为微调和定制的强大基础。 Inkling 并非前沿模型，而是设计为通过 Tinker 平台进行微调的强大基础。模型卡和训练数据文档内容简略，对数据来源的描述模糊。较小的变体 Inkling-Small（276B 总参数，12B 活跃参数）仍在测试中。

rss · Simon Willison · 7月16日 15:35

**背景**: 开放权重模型意味着训练好的参数可公开下载，允许用户运行、研究和修改模型。混合专家（MoE）架构使用多个专门的子网络和门控机制，每次输入只激活部分参数，从而提高效率。Apache-2.0 许可证是一种宽松的开源许可证，允许自由使用、修改和分发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>
<li><a href="https://www.emergentmind.com/topics/mixture-of-experts-transformer">Mixture - of - Experts Transformer</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#Thinking Machines Lab`

---

<a id="item-7"></a>
## [Linus Torvalds 为 Linux 内核使用 AI 辩护](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linux 创始人 Linus Torvalds 在 Linux Media 邮件列表中公开表示，Linux 不是一个反 AI 的项目，AI 是内核开发中一个明显有用的工具，并邀请不同意的人分叉或离开。 来自 Linux 最高维护者的权威背书，标志着开源社区中强烈的支持 AI 立场，可能影响 AI 工具在内核开发及其他开源项目中的整合方式。 Torvalds 强调 AI 的实用性已毋庸置疑，尽管他承认关于 AI 的其他问题（如其经济影响）仍有待解答。该声明是对社区反对在内核开发中使用 AI 的回应。

rss · Simon Willison · 7月16日 13:26

**背景**: Linux 是全球最大的开源操作系统内核，由 Linus Torvalds 领导的全球社区维护。生成式 AI 和大语言模型的最新进展引发了开源社区内部关于其在软件开发中的角色和伦理的辩论。

**标签**: `#Linux`, `#AI`, `#open source`, `#kernel development`, `#Linus Torvalds`

---

<a id="item-8"></a>
## [研究人员诱骗 Claude 泄露私人记忆](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

研究员 Ayush Paul 发现了一种提示注入攻击，绕过了 Claude 的 web_fetch 工具保护，通过诱骗模型跟随蜜罐网站上的嵌套链接，从而窃取用户的私人记忆。 这次攻击展示了 AI 代理安全中的关键漏洞，表明即使是精心设计的保护措施也可能被绕过，并凸显了在具有工具访问权限的 LLM 中防止数据窃取的持续挑战。 该攻击利用了一个漏洞，即 web_fetch 可以跟随先前获取页面中嵌入的链接，并且仅针对用户代理中包含'Claude-User'的客户端以避免检测。Anthropic 已在内部发现该问题，并通过移除该功能封堵了漏洞。

rss · Simon Willison · 7月15日 14:21

**背景**: 提示注入是一种安全漏洞，恶意输入会导致 LLM 产生意外行为。'致命三重奏'描述了同时拥有私人数据、访问不受信任内容以及能够与外部通信的 AI 代理——这种组合使得数据窃取成为可能。Claude 的 web_fetch 工具设计为仅访问用户提供或来自其 web_search 工具的 URL，但此次攻击找到了绕过该限制的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对绕过保护的简易性表示担忧，并讨论了 Anthropic 的漏洞赏金决定是否公平。一些人指出该攻击需要蜜罐网站，限制了其实际可利用性，而另一些人则强调需要更强大的防御措施来应对提示注入。

**标签**: `#AI security`, `#prompt injection`, `#data exfiltration`, `#Claude`, `#vulnerability`

---

<a id="item-9"></a>
## [Cursor 零日漏洞被公开披露以保护用户](https://www.reddit.com/r/programming/comments/1uxjm12/cursor_0day_when_full_disclosure_becomes_the_only/) ⭐️ 8.0/10

安全公司 Mindgard 公开披露了 AI 编程助手 Cursor 中的一个零日漏洞，此前该软件供应商未能及时修复。 此次披露凸显了 AI 编程工具中存在的严重安全风险——这类工具正被开发者广泛使用——并强调了负责任披露与用户保护之间的张力。 Mindgard 在其博客上发布了漏洞细节，使组织能够评估自身风险并实施补偿性控制措施。

reddit · r/programming · /u/alexeyr · 7月15日 21:52

**背景**: 零日漏洞是指软件供应商未知的安全缺陷，用户在补丁发布前一直处于风险之中。Cursor 是一款以 AI 为先的代码编辑器，提供结对编程辅助，作为 GitHub Copilot 的替代方案而日益流行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left">Cursor 0day: When Full Disclosure Becomes the Only Protection ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>
<li><a href="https://cursor.com/">Cursor : AI coding agent</a></li>

</ul>
</details>

**社区讨论**: Reddit 上 r/programming 的讨论反应不一：有人称赞完全披露对用户安全是必要的，也有人批评未与供应商进行负责任的披露协调。

**标签**: `#security`, `#vulnerability`, `#AI coding tools`, `#full disclosure`, `#Cursor`

---

<a id="item-10"></a>
## [数百万鲨鱼机器人吸尘器存在远程代码执行漏洞](https://www.reddit.com/r/programming/comments/1uyhqyt/no_shark_is_safe_millions_of_shark_vacuums_are/) ⭐️ 8.0/10

研究人员在数百万台鲨鱼（Shark）品牌机器人吸尘器中发现了严重的远程代码执行漏洞，攻击者可通过暴露的 UART 引脚获取 root shell 访问权限。 该漏洞使数百万家庭中的物联网设备面临被远程控制的风险，包括摄像头访问和网络渗透，对隐私和安全构成重大威胁。 该漏洞由研究员 Tokay0 在 RV2320EDUS 主板上发现，通过按 Ctrl-C 中断 U-Boot 启动序列即可绕过密码认证，获得 root 权限。

reddit · r/programming · /u/ScottContini · 7月16日 22:37

**背景**: 远程代码执行漏洞允许攻击者在设备上远程运行任意代码。机器人吸尘器等物联网设备通常缺乏强大的安全防护，成为攻击者的目标。暴露的 UART 引脚是一种硬件调试接口，在生产设备中应被禁用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/shark-vacuum-rce-flaw/">Shark Vacuum RCE Flaw Lets Attackers Remotely Control Cameras...</a></li>

</ul>
</details>

**标签**: `#security`, `#IoT`, `#vulnerability`, `#RCE`, `#embedded systems`

---

<a id="item-11"></a>
## [微软 Comic Chat 开源，时隔 30 年](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/) ⭐️ 7.0/10

2026 年 7 月 16 日，微软在 GitHub 上以开源许可证发布了 Comic Chat（也称 Microsoft Chat）的源代码，使这款 1996 年的 IRC 客户端得以保存和修改。 此次发布保存了一段独特的互联网历史——一款将文本对话自动转化为漫画条目的图形化 IRC 客户端——并允许开发者研究、移植或重新构想其创新的视觉聊天概念。 Comic Chat 由微软研究员 David Kurlander 开发，于 1996 年随 Internet Explorer 3.0 首次发布；它还让世界认识了 Comic Sans 字体。此次开源发布包含原始的 C++ 源代码，托管在 github.com/microsoft/comic-chat。

hackernews · jervant · 7月16日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48936426)

**背景**: Internet Relay Chat (IRC) 是 1990 年代流行的基于文本的聊天协议。Comic Chat 是一款图形化客户端，使用自定义 IRC 扩展将对话渲染为包含头像、对话气泡和表情的漫画面板。它随 Windows 98 捆绑发布，并被本地化为 24 种语言，但最终随着其他聊天平台的出现而逐渐消失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Comic_Chat">Microsoft Comic Chat - Wikipedia</a></li>
<li><a href="https://github.com/microsoft/comic-chat">GitHub - microsoft/comic-chat: Source code for the Microsoft ...</a></li>
<li><a href="https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/">Microsoft Comic Chat is now open source</a></li>

</ul>
</details>

**社区讨论**: 社区反应充满怀旧和积极情绪，原始贡献者 Robert Standefer 分享了促成此次发布的六年历程。一些评论者回忆说，Comic Chat 曾因其非标准协议扩展而在 IRC 上受到诟病，而另一些人则称赞其创意精神，并指出它启发了像 Chogger 这样的项目。

**标签**: `#open source`, `#microsoft`, `#irc`, `#nostalgia`, `#history`

---

<a id="item-12"></a>
## [诱饵字体：用光学幻觉字体迷惑 AI 视觉模型](https://www.mixfont.com/experiments/decoy-font) ⭐️ 7.0/10

MixFont 发布了诱饵字体（Decoy Font），这是一种 TTF 字体，能在不同分辨率下嵌入两个不同的信息，形成光学幻觉，从而迷惑 GPT-4、Claude 和 Gemini 等 AI 视觉模型。 这种字体凸显了当前 AI 视觉系统的一个根本局限：无法感知双层文本，这对 AI 安全、验证码设计以及理解计算机视觉中的对抗样本具有重要意义。 该字体的原理是将高频的清晰信息（如“SORRY ROBOT”）与低频的模糊信息（如“HAPPY HUMAN”）结合，因此在正常分辨率下可见清晰文本，而在缩小或模糊时隐藏文本会显现。

hackernews · ray__ · 7月16日 16:18 · [社区讨论](https://news.ycombinator.com/item?id=48936584)

**背景**: AI 视觉模型以固定分辨率处理图像，并经常对输入进行降采样，这可能导致细节丢失。该字体利用这一点，将信息编码在降采样后仍保留的低频分量中，而诱饵信息则占据会丢失的高频细节。这种技术类似于利用人类与机器感知差异的对抗性攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.mixfont.com/experiments/decoy-font">Decoy Font: A TTF font that hides what you type - mixfont.com</a></li>
<li><a href="https://www.creativebloq.com/design/fonts-typography/this-optical-illusion-font-was-created-to-baffle-ai-and-it-actually-works-for-now">This optical illusion font was created to baffle AI, and it ...</a></li>
<li><a href="https://www.popsci.com/technology/font-optical-illusion-hide-ai/">This font uses an optical illusion to hide from AI</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：有人认为它很酷但质疑其实用性，也有人报告在让 AI 模型读取隐藏文本方面取得了不同程度的成功。用户指出，GPT-4 有时能通过提示解码隐藏信息，但 Claude 和 Gemini 则更困难。

**标签**: `#AI`, `#typography`, `#computer vision`, `#security`, `#optical illusion`

---

<a id="item-13"></a>
## [OpenAI 提出 AI 安全的逆向联邦制方案](https://openai.com/index/advancing-ai-safety-through-state-and-federal-action) ⭐️ 7.0/10

OpenAI 提出了一种“逆向联邦制”的 AI 治理方法，即由州级 AI 法律和实验来推动国家框架的制定，而非仅依赖自上而下的联邦监管。 该提案可能影响美国如何监管 AI，在创新与安全之间取得平衡，同时利用州级实验来构建更民主、更灵活的国家政策。 根据 OpenAI 的计划，NIST 下属的 AI 标准与创新中心将主导联邦工作，该方法旨在通过建立统一的国家基线，避免各州法律相互冲突的碎片化局面。

rss · OpenAI Blog · 7月15日 12:00

**背景**: 随着前沿 AI 模型日益强大，AI 治理日益受到关注。传统上，联邦监管是自上而下的，而“逆向联邦制”允许各州作为政策实验室，在政策推广至全国前先行测试。OpenAI 于 2026 年 6 月发布的《前沿 AI 民主治理蓝图》阐述了这一愿景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibyteslearning.com/news/openai-reverse-federalism-ai-safety-governance-202607160801460">OpenAI's 'Reverse Federalism' Bet on AI Safety Law</a></li>
<li><a href="https://cctest.ai/en/articles/openai-s-reverse-federalism-vision-for-u-s-ai-safety">OpenAI’s Reverse Federalism Approach to AI Safety - CCTest</a></li>
<li><a href="https://www.machinebrief.com/news/openais-reverse-federalism-could-reshape-ai-governance-he6h">OpenAI's 'Reverse Federalism' Could Reshape AI Governance</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI governance`, `#policy`, `#OpenAI`

---

<a id="item-14"></a>
## [旧金山市长在 Waymo 交通堵塞后寻求更严格的机器人出租车规定](https://techcrunch.com/2026/07/16/san-francisco-mayor-pushes-for-tougher-rules-after-the-waymo-traffic-fiasco/) ⭐️ 7.0/10

旧金山市长丹尼尔·卢里呼吁州监管机构对 Waymo 等机器人出租车运营商实施更严格的要求，此前 Waymo 车辆在停电期间造成了长达数小时的严重交通堵塞。 这一监管举措可能为城市如何监督自动驾驶汽车运营树立先例，可能会减缓部署速度，但能提高安全性和公众信任。 交通堵塞发生在旧金山大面积停电期间，多辆 Waymo 机器人出租车在十字路口瘫痪，需要拖车。卢里市长特别敦促加州公用事业委员会更新其规则。

rss · TechCrunch · 7月16日 23:25

**背景**: Waymo 是一家领先的自动驾驶汽车公司，在旧金山运营机器人出租车服务。该事件凸显了 L4 级自动驾驶汽车在停电等意外场景中的脆弱性，它们可能无法安全导航。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://insideevs.com/news/782523/waymo-robotaxi-san-francisco-outage-power/">When The Power Went Out In San Francisco, So Did Waymo’s ...</a></li>
<li><a href="https://www.firstpost.com/auto/waymo-robotaxis-run-out-of-charge-require-towing-during-san-franciscos-july-4-gridlock-14029301.html">Waymo Robotaxis Run Out of charge, require towing during San ...</a></li>
<li><a href="https://www.msn.com/en-us/news/technology/waymo-halts-san-francisco-robotaxis-after-massive-power-outage/ar-AA1SMlFC">Waymo halts San Francisco robotaxis after massive power outage</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#regulation`, `#Waymo`, `#San Francisco`, `#robotaxi`

---

<a id="item-15"></a>
## [Uber 以 148 亿美元收购 Delivery Hero](https://techcrunch.com/2026/07/16/ubers-14-8b-delivery-hero-deal-would-nearly-double-its-global-footprint/) ⭐️ 7.0/10

Uber 已同意以 148 亿美元的全股票交易收购 Delivery Hero，这将使 Uber 的全球业务版图几乎翻倍，并打造出中国以外全球最大的食品配送平台之一。 此次收购显著增强了 Uber 在全球食品配送市场的地位，使其能够更有效地与 DoorDash 等竞争对手抗衡，并拓展至 60 多个新国家。 该交易为全股票交易，尚未最终完成；Delivery Hero 还同意将其在 Uber Eats 已运营的 14 个市场的业务以 16 亿美元出售给 SSW Partners。

rss · TechCrunch · 7月16日 17:12

**背景**: Delivery Hero 是一家德国跨国在线食品订购和配送公司，业务覆盖 60 多个国家。Uber Eats 是 Uber 的食品配送部门，此前已通过收购 Postmates（2020 年）等方式扩张。该交易反映了食品配送行业持续的整合趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/16/ubers-14-8b-delivery-hero-deal-would-nearly-double-its-global-footprint/">Uber 's $14.8B Delivery Hero deal would nearly double... | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Delivery_Hero">Delivery Hero</a></li>

</ul>
</details>

**标签**: `#acquisition`, `#food delivery`, `#Uber`, `#business`

---