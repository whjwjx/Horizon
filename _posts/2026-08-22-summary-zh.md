---
layout: default
title: "Horizon Summary: 2026-08-22 (ZH)"
date: 2026-08-22
lang: zh
---

> 从 58 条内容中筛选出 13 条重要资讯。

---

1. [Linus Torvalds 称赞 AI 协助调试 Linux 内核问题](#item-1) ⭐️ 8.0/10
2. [DeepMind 校友创立的 Inherent 声称其 AI Faraday 在论文复现上超越 Anthropic 和 OpenAI](#item-2) ⭐️ 8.0/10
3. [开发者从零训练 250M 参数 LLM，部署仅需 60MB](#item-3) ⭐️ 8.0/10
4. [DelveRL：用于训练游戏智能体的开源 Roguelike](#item-4) ⭐️ 8.0/10
5. [编码代理：关键技能是指令与验证，而非逐行审查](#item-5) ⭐️ 7.0/10
6. [llm-openrouter 0.7 新增 Responses API 和服务器端工具](#item-6) ⭐️ 7.0/10
7. [停止制作 TUI：编码代理让原生 UI 变得廉价](#item-7) ⭐️ 7.0/10
8. [GPT-5.6 后 ChatGPT 搜索中 site:运算符使用激增](#item-8) ⭐️ 7.0/10
9. [OpenAI 转变立场，敦促加州加强 AI 安全法案](#item-9) ⭐️ 7.0/10
10. [前沿 AI 实验室缺乏公开的失控模型遏制计划](#item-10) ⭐️ 7.0/10
11. [美国电池初创企业从国防资金中找到生命线](#item-11) ⭐️ 7.0/10
12. [迈克尔·波兰斯基的 AI 初创公司利用活体人类皮肤进行训练](#item-12) ⭐️ 7.0/10
13. [英伟达：决定 AI 智能体性能的是“马具”而非模型](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Linus Torvalds 称赞 AI 协助调试 Linux 内核问题](https://simonwillison.net/2026/Aug/22/linus-torvalds/) ⭐️ 8.0/10

Linus Torvalds 公开称赞 AI 助手在调试一个棘手的 Linux 内核问题时提供了巨大帮助，尽管 AI 最初持悲观态度。他亲自编写并提交了针对 Intel Xe 图形驱动的修复，该过程涉及 24 个调试补丁和 18 次内核启动。 Torvalds 这样有影响力的人物公开认可，可能会改变开发者对 AI 辅助编程的看法，尤其是在 Linux 内核等关键系统中。这凸显了 AI 在处理繁琐调试任务方面的潜力，可能加速开发并减少人力投入。 该 bug 最终被定位到一行代码，其中 round_up() 应为 round_down()。AI 在被推动时不断添加并分析调试代码，Torvalds 还让 AI 撰写了提交信息，显示了对 AI 生成内容的信任。

rss · Simon Willison · 8月22日 21:04

**背景**: Linux 内核是一个复杂的开源操作系统内核，调试问题可能非常耗时。AI 辅助编程工具（如大型语言模型）越来越多地被用于帮助开发者编写和调试代码，但在内核开发中的采用一直较为谨慎。Torvalds 的认可之所以引人注目，是因为他以怀疑态度和高标准著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://itsfoss.com/news/torvalds-used-ai-fix-kernel-bug/">Linux Creator Linus Torvalds Just Used AI to Fix a Kernel Bug</a></li>
<li><a href="https://www.phoronix.com/news/Linus-Torvalds-Debug-AI">Linus Torvalds Endures A Debug Session From Hell, "Enormously Helped" By AI - Phoronix</a></li>

</ul>
</details>

**社区讨论**: Phoronix 上的社区讨论（51 条评论）普遍对 Torvalds 使用 AI 表示惊讶和兴趣，一些人称赞 AI 的协助，另一些人则讨论 AI 在内核开发中的可靠性和影响。一些评论者指出了 AI 最初悲观态度与 Torvalds 坚持之间的讽刺。

**标签**: `#AI-assisted development`, `#Linux kernel`, `#Linus Torvalds`, `#debugging`, `#developer tools`

---

<a id="item-2"></a>
## [DeepMind 校友创立的 Inherent 声称其 AI Faraday 在论文复现上超越 Anthropic 和 OpenAI](https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/) ⭐️ 8.0/10

由 DeepMind 校友创立的伦敦 AI 实验室 Inherent 发布了 AI 智能体 Faraday，它能独立复现科学论文。该公司声称 Faraday 在复现任务上超越了 Claude Opus 4.8 和 GPT-5.5，而所用模型规模仅为这些前沿系统的一小部分。 这一进展意义重大，因为它表明专门的、规模较小的 AI 智能体在特定科学任务上可以超越更大的前沿模型，从而可能通过自动化复现研究结果来加速科研进程。同时，它也凸显了 AI 驱动科学发现的趋势以及 AI 实验室之间的竞争格局。 Faraday 是一个 27B 参数的科学智能体，旨在无需预先接触目标解决方案即可复现已发表的研究。Inherent 由前 Google DeepMind 研究员 Louis Kirsch、Kaloyan Aleksiev、Tantum Collins 和 Edward Hughes 创立，并在发布前几周获得了 5000 万美元的种子轮融资。

rss · TechCrunch · 8月22日 19:00

**背景**: 复现科学论文是确保研究有效性的关键但耗时的过程。像 Faraday 这样的 AI 智能体旨在自动化这一过程，使用 PaperBench 等基准来评估其自主复现机器学习研究的能力。这一领域是 AI 驱动科学发现更广泛运动的一部分，智能体可以验证并基于现有工作进行构建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/">Inherent, founded by DeepMind alumni, says its AI 'teammate ...</a></li>
<li><a href="https://www.llms.blog/posts/inherent-releases-faraday-27b-scientific-agent-outperforms-frontier-models-on-paper-replication">Inherent Releases Faraday: 27B Scientific Agent Outperforms ...</a></li>
<li><a href="https://www.aichatdaily.com/ai-models/inherent-s-faraday-agent-beats-claude-gpt-5-5">Inherent's Faraday agent beats Claude and GPT-5.5 at ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#research`, `#DeepMind`, `#scientific discovery`, `#agent`

---

<a id="item-3"></a>
## [开发者从零训练 250M 参数 LLM，部署仅需 60MB](https://www.reddit.com/r/MachineLearning/comments/1vv2nkh/i_developed_my_own_quantized_llm_from_scratch/) ⭐️ 8.0/10

一位开发者从零开始，在 30B tokens 的 fineweb 数据上训练了一个 250M 参数的 LLM，量化至 2 比特以下，实现了 60MB 的部署体积，在 CPU 上以 400 tok/s 的速度运行。该模型还具备基于磁盘的长上下文记忆功能，将较旧的 token 压缩至 1 比特，支持从多达 1 亿个 token 中检索。 这表明极端量化和高效的内存管理可以使 LLM 在无需 GPU 的资源受限设备上部署，可能扩大 AI 在边缘和移动环境中的使用。创新的基于磁盘的长上下文方法可能启发处理 LLM 中超长序列的新方法。 该模型对 131k 个 token 中的每一个使用固定的 512 位编码（8.4 MB，零训练参数），词汇嵌入表未经过训练。长上下文机制将最近的 2048 个 token 保留在 fp16 中，而较旧的 token 被压缩至 1 比特并存储在磁盘上，每个 token 约 320 字节。基础模型在保留的英文网页文本上实现了 23.3 的困惑度。

reddit · r/MachineLearning · /u/Final-Data-1410 · 8月22日 04:39

**背景**: 量化将模型权重的精度降低到更低的位宽，如 2 位或 4 位，以缩小模型大小并加速推理。传统 LLM 使用学习到的嵌入表将 token 映射为向量，但该模型使用固定的随机编码，这些编码被证明能捕获一定的语义相似性。基于磁盘的记忆是内存中 KV 缓存的替代方案，允许模型访问更长的历史记录而不会超出 RAM 限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/pprp/Awesome-LLM-Quantization">GitHub - pprp/Awesome- LLM - Quantization : Awesome list for LLM ...</a></li>
<li><a href="https://arxiv.org/html/2509.23040v5">Look Back to Reason Forward: Revisitable Memory for Long-Context LLM Agents - arXiv</a></li>
<li><a href="https://developer.nvidia.com/blog/scaling-to-millions-of-tokens-with-efficient-long-context-llm-training/">Scaling to Millions of Tokens with Efficient Long-Context LLM Training - NVIDIA Developer</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区反应积极，作者对好奇且有帮助的评论表示感谢。讨论可能包括关于量化方法、基于磁盘的检索和固定嵌入编码的技术问题，以及进一步改进的建议。

**标签**: `#LLM`, `#quantization`, `#efficient inference`, `#long context`, `#from-scratch training`

---

<a id="item-4"></a>
## [DelveRL：用于训练游戏智能体的开源 Roguelike](https://www.reddit.com/r/MachineLearning/comments/1vvii1j/i_built_an_opensource_roguelike_specifically_for/) ⭐️ 8.0/10

作者发布了 DelveRL，这是一个专为训练强化学习智能体而设计的开源、可人工游玩的 Roguelike 游戏。它包含结构化 API、确定性模拟、程序化关卡、部分可观测性，以及循环 PPO 训练器，基线结果达到中位数 18 层，扩展运行可达 33 层。 这填补了强化学习环境的一个空白，提供了一个专门构建、易于与智能体框架集成的游戏，不同于许多现有游戏。它可能加速游戏 AI 研究，并鼓励社区贡献以基准测试和提升智能体性能。 DelveRL 完全在本地运行，包括无渲染器的批量环境，训练代码、检查点、桥接文档和原始基准测试均开源。游戏是一款无尽的回合制 Roguelike，智能体必须探索、管理风险和资源、与敌人战斗并逃离每一层。

reddit · r/MachineLearning · /u/SnyderConsulting · 8月22日 17:32

**背景**: 强化学习（RL）智能体通常需要既具有挑战性又易于接口的自定义环境。PPO（近端策略优化）是一种流行的策略梯度算法，用于训练此类智能体，而 Roguelike 提供程序化生成和部分可观测性，适合测试探索和决策能力。智能体框架（agent harness）是将 AI 模型连接到环境的软件基础设施，管理工具、记忆和反馈循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Proximal_Policy_Optimization">Proximal policy optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agent_harness">Agent harness - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Delver_(video_game)">Delver - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement-learning`, `#open-source`, `#game-ai`, `#environment`, `#PPO`

---

<a id="item-5"></a>
## [编码代理：关键技能是指令与验证，而非逐行审查](https://simonwillison.net/2026/Aug/22/more-than-just-code-review/) ⭐️ 7.0/10

Simon Willison 认为，高效使用编码代理的关键技能是自信地指导它们进行更改并验证结果，这不一定需要逐行审查代码。 这一见解挑战了代码审查必须逐行进行的常见假设，为使用 AI 编码代理的开发人员提供了一种更实用的方法。它可能改变团队验证 AI 生成代码的方式，提高生产力并增强对代理工程的信任。 Willison 提出了除逐行审查之外的替代验证方法，例如运行测试、检查行为或使用其他验证技术。该文章简洁，缺乏深入的技术细节，但突出了 AI 辅助开发中的一个实际技能缺口。

rss · Simon Willison · 8月22日 15:56

**背景**: 编码代理是能够自主编写、修改、调试和重构代码的 AI 工具，它们能理解多文件上下文并规划跨代码库的更改。代理工程指的是指导这些自主 AI 代理的技艺，需要判断力和架构技能。传统的代码审查通常涉及逐行检查，但面对 AI 生成的代码，需要新的验证策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentic.ai/best/coding-agents">20 Best AI Coding Agents in 2026 — Agentic.ai</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-engineering-from-code-workflows-regie-san-juan-sjyyc">Agentic Engineering : From Code to Workflows</a></li>
<li><a href="https://medium.com/@telumai/there-was-prompt-engineering-then-vibe-coding-now-agentic-engineering-7da779d1cb63">There Was Prompt Engineering Then Vibe Coding Now Agentic ...</a></li>

</ul>
</details>

**标签**: `#coding-agents`, `#code-review`, `#generative-ai`, `#agentic-engineering`, `#AI`

---

<a id="item-6"></a>
## [llm-openrouter 0.7 新增 Responses API 和服务器端工具](https://simonwillison.net/2026/Aug/21/llm-openrouter/) ⭐️ 7.0/10

llm-openrouter 0.7 已发布，增加了对 LLM 0.32 的兼容性，并改用 OpenRouter 的 Responses API 实现。它还引入了三个新的服务器端工具：Shell、WebFetch 和 WebSearch。 此更新通过支持推理轨迹显示和提供服务器端工具，增强了插件功能，简化了 LLM 用户的工作流程。这反映了 LLM 生态系统中高级 API 功能和工具集成的持续发展。 新的服务器端工具可以通过 -T WebSearch 等选项启用。该插件现在使用 OpenRouter 的 Responses API，该 API 支持推理、工具调用和网络搜索。

rss · Simon Willison · 8月21日 16:58

**背景**: LLM 是一个用于与各种语言模型交互的命令行工具，而 llm-openrouter 是一个将其连接到 OpenRouter 托管的模型的插件。OpenRouter 提供统一的 API 来访问多种 AI 模型，其 Responses API 是一个兼容 OpenAI 的接口，支持推理和工具使用等高级功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/docs/api_reference/responses/overview">OpenRouter Responses API - OpenAI-Compatible Documentation</a></li>
<li><a href="https://simonwillison.net/2026/Aug/21/llm-openrouter/">Release: llm - openrouter 0.7 | Simon Willison’s Weblog</a></li>
<li><a href="https://github.com/simonw/llm-openrouter">GitHub - simonw/ llm - openrouter : LLM plugin for models hosted by...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#OpenRouter`, `#plugin`, `#AI`, `#tools`

---

<a id="item-7"></a>
## [停止制作 TUI：编码代理让原生 UI 变得廉价](https://simonwillison.net/2026/Aug/21/stop-making-tuis/) ⭐️ 7.0/10

Thomas Ptacek 认为，编码代理使得构建原生用户界面的成本变得极低，开发者应该用真正的 GUI 取代一次性的 CLI。Simon Willison 对此表示赞同，并提到他自己通过 vibe coding 开发的 macOS 任务栏应用（用于带宽和 GPU 监控）每天都在使用。 这一转变可能改变开发者构建小工具的方式，使其更易用、更友好。它凸显了 AI 辅助开发对日常编程实践的日益影响，可能削弱终端工具的主导地位。 Ptacek 的文章标题为“停止制作 TUI”，鼓励开发者尝试为一次性 CLI 构建原生 UI。Willison 自己的应用是通过 vibe coding 使用 SwiftUI 创建的，他指出自己“没有借口”不更广泛地采用这种方法。

rss · Simon Willison · 8月21日 16:07

**背景**: Vibe coding 是一种 AI 辅助开发方法，开发者用自然语言描述项目，LLM 生成代码，通常不深入审查就接受输出。编码代理是能够自主编写、修改和调试代码的 AI 工具。传统上，由于简单性，TUI（终端用户界面）常用于小工具，但 GUI 开发成本的降低正在改变这一权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://agentic.ai/best/coding-agents">20 Best AI Coding Agents in 2026 — Agentic.ai</a></li>

</ul>
</details>

**标签**: `#UI`, `#developer tools`, `#coding agents`, `#native apps`, `#productivity`

---

<a id="item-8"></a>
## [GPT-5.6 后 ChatGPT 搜索中 site:运算符使用激增](https://simonwillison.net/2026/Aug/20/chatgpt-search-now-uses-the-siteoperator-at-scale/) ⭐️ 7.0/10

Promptwatch 的追踪数据显示，ChatGPT 搜索中包含 site:运算符的查询比例从 0.3%-0.5%跃升至 2026 年 8 月 8 日的 16%-17%，这与 GPT-5.6 的发布相吻合。这表明 ChatGPT 处理搜索查询的方式发生了重大转变，可能反映了其搜索工具底层实现的改变。 这一变化对 SEO 和 GEO（生成引擎优化）具有重大影响，内容创作者和营销人员必须适应 ChatGPT 现在如何优先考虑特定域名。site:运算符使用增加表明信息获取方式更加有针对性，这可能影响网站流量和在 AI 生成答案中的可见性。 该数据基于 Promptwatch 对提示词的自动追踪，可能无法代表所有 ChatGPT 用户。Simon Willison 推测 OpenAI 的搜索工具现在使用类似 search(query, recency, domains)的函数签名，而不是直接鼓励使用 site:运算符，但 OpenAI 的系统提示词仍然不透明。此外，8 月 18 日的后续报告指出，搜索中引用 Reddit 的可能性降低。

rss · Simon Willison · 8月20日 23:57

**背景**: site:运算符是一种搜索命令，用于将结果限制在特定域名，常见于 Google 等传统搜索引擎。生成引擎优化（GEO）是一个新兴领域，专注于提高内容在 AI 生成回复中的可见性，而传统 SEO 则针对链接排名列表。Promptwatch 是一种工具，用于追踪品牌在 ChatGPT、Claude 和 Gemini 等平台的 AI 回答中的出现情况，为 AI 搜索行为中不可见的变化提供洞察。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Generative_engine_optimization">Generative engine optimization - Wikipedia</a></li>
<li><a href="https://promptwatch.com/">Promptwatch | #1 AI Search Visibility & GEO Platform</a></li>
<li><a href="https://developers.google.com/search/docs/monitor-debug/search-operators/all-search-site">How To Use the Site Search Operator | Google Search Central | Documentation | Google for Developers</a></li>

</ul>
</details>

**标签**: `#ChatGPT`, `#SEO`, `#GEO`, `#search`, `#AI`

---

<a id="item-9"></a>
## [OpenAI 转变立场，敦促加州加强 AI 安全法案](https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/) ⭐️ 7.0/10

OpenAI 已改变先前反对的立场，现敦促加州加强 AI 安全法案 SB 53。这标志着该公司在 AI 监管立场上的重大转变。 这一转变可能影响 SB 53 的最终形态，并标志着整个行业向接受 AI 监管的转变。它也可能鼓励其他科技公司支持安全措施，从而塑造未来的 AI 治理。 SB 53 由参议员 Scott Wiener 提出，要求 AI 公司披露大规模前沿模型的安全信息。该法案在去年更广泛的 SB 1047 被否决后，由州长 Gavin Newsom 签署成为法律。

rss · TechCrunch · 8月22日 16:30

**背景**: 加州一直处于 AI 监管努力的前沿。SB 53 是早前 SB 1047 的缩减版，后者因 AI 公司的强烈游说而被否决。该法案旨在平衡安全与创新，支持者认为安全与创新可以兼容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kron4.com/hill-politics/newsom-signs-first-in-the-nation-ai-safety-disclosures-law/165/">Gavin Newsom signs SB 53 , enacting California AI safety bill</a></li>
<li><a href="https://businessnoon.com/california-signs-landmark-ai-safety-bill-sb-53/">California ’s Bold AI Safety Bill SB 53 Changes the Game</a></li>
<li><a href="https://sd11.senate.ca.gov/news/senator-wieners-landmark-responsible-ai-innovation-bill-advances-final-vote">Senator Wiener’s Landmark Responsible AI Innovation Bill Advances...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#regulation`, `#OpenAI`, `#policy`

---

<a id="item-10"></a>
## [前沿 AI 实验室缺乏公开的失控模型遏制计划](https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/) ⭐️ 7.0/10

Guidelight 的一项新研究发现，包括 OpenAI、Anthropic 和 Meta 在内的领先 AI 实验室几乎没有公开记录遏制失控 AI 模型的计划。该研究将 OpenAI 评为最高分 3/5，而 Anthropic 和 Meta 得分最低。 这种缺乏透明度的现象引发了对 AI 安全和治理的重大担忧，因为 AI 系统越来越多地表现出意外且可能危险的行为。监管机构和公众需要明确的遏制协议，以确保问责并防止灾难性后果。 该研究指出了 OpenAI、Anthropic 和 Meta 的模型近期表现出意外行为的事件，强调了制定强有力遏制措施的紧迫性。失控模型遏制包括紧急步骤，如切断权限、暂停部署、限制访问或使模型离线。

rss · TechCrunch · 8月22日 16:00

**背景**: 失控模型遏制是指当 AI 系统表现出抵抗人类控制时，公司将采取的紧急程序。随着前沿 AI 模型变得更有能力和自主性，它们违背人类意图的风险也在增加，因此做好准备至关重要。该研究的发现凸显了行业对安全的公开承诺与其实际运营准备之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/">Frontier AI labs still won't say how they'd contain a rogue model | TechCrunch</a></li>
<li><a href="https://superintelligencenews.com/companies/rogue-model-containment-ai-labs-pressure/">Rogue Model Containment : AI Labs Under Pressure</a></li>
<li><a href="https://cryptobriefing.com/frontier-ai-labs-rogue-model-containment/">Study reveals frontier AI labs lack plans to contain rogue models</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI governance`, `#rogue AI`, `#frontier labs`, `#risk assessment`

---

<a id="item-11"></a>
## [美国电池初创企业从国防资金中找到生命线](https://techcrunch.com/2026/08/22/us-battery-startups-have-found-a-lifeline-in-defense/) ⭐️ 7.0/10

美国能源部宣布提供 5 亿美元拨款，以加强国内电池供应链，在电动汽车激励措施减少后，为电池初创企业提供了关键的资金生命线。该资金旨在减少对外国来源的依赖并增强国家安全。 转向国防资金意义重大，因为它为在电动汽车激励措施削减后苦苦挣扎的电池初创企业提供了新的收入来源。这也符合更广泛的国家安全优先事项，可能加速电池技术在国防和民用领域的创新。 这些拨款是加强美国电池供应链计划的一部分，重点是减少对外依赖。据报道，锂离子电池的国防应用是一个关键讨论点，电池材料初创公司 Coreshell 的发言人如此表示。

rss · TechCrunch · 8月22日 15:20

**背景**: 美国电池初创企业传统上依赖电动汽车（EV）激励措施来推动需求，但近期的政策变化减少了这些激励措施，使许多公司陷入财务困境。能源部的拨款是联邦政府确保国内电池供应链的更广泛努力的一部分，这对清洁能源和国家安全都至关重要。国防应用，如为军事装备和便携式电子设备供电，为先进电池技术提供了稳定且高价值的市场。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/22/us-battery-startups-have-found-a-lifeline-in-defense/">US battery startups have found a lifeline in defense | TechCrunch</a></li>
<li><a href="https://www.energy.gov/">Department of Energy</a></li>
<li><a href="https://www.cnet.com/culture/energy-department-awards-auto-battery-grants/">Energy Department awards auto battery grants - CNET</a></li>

</ul>
</details>

**标签**: `#battery`, `#energy`, `#defense`, `#DOE`, `#startups`

---

<a id="item-12"></a>
## [迈克尔·波兰斯基的 AI 初创公司利用活体人类皮肤进行训练](https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/) ⭐️ 7.0/10

迈克尔·波兰斯基，作为 Lady Gaga 的伴侣和肖恩·帕克的前副手，公开了他的 AI 驱动初创公司，该公司在体外让活体人类皮肤组织存活数周，以发现新的护肤化合物。这家公司现在才公开其工作。 这代表了 AI 与生物技术的新颖交叉，通过在活体人类组织而非动物模型或合成替代品上测试化合物，可能加速护肤和药物发现。这可能导致更有效、更安全的护肤产品，影响美容行业和皮肤病医学。 该初创公司让活体人类皮肤组织在体外存活数周，这比通常只能维持几天的离体皮肤培养时间更长。这种延长的存活能力允许对护肤化合物进行更全面的测试，但关于 AI 模型和组织维持方法的具体技术细节尚未披露。

rss · TechCrunch · 8月22日 01:31

**背景**: 离体人类皮肤模型用于研究中，以在保持组织结构的同时研究皮肤生物学和测试治疗方法。传统的离体皮肤培养通常只能维持 72 小时到几天，限制了其使用。AI 驱动的药物发现越来越多地用于皮肤病学，分析化合物和生物相互作用，加速新活性成分的识别。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41598-020-79683-3?error=cookies_not_supported&code=7246d9fc-2892-43d3-925a-160bfb42e113">A novel human ex vivo skin model to study early local responses to...</a></li>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/41093479/">Artificial Intelligence in Dermatology Research and Drug Discovery - PubMed</a></li>
<li><a href="https://blog.bccresearch.com/ai-revolutionizes-topical-drug-delivery">AI Revolutionizes Topical Drug Delivery: From Early Adoption to 2026 Advances</a></li>

</ul>
</details>

**标签**: `#AI`, `#biotech`, `#skincare`, `#drug discovery`, `#startup`

---

<a id="item-13"></a>
## [英伟达：决定 AI 智能体性能的是“马具”而非模型](https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero/) ⭐️ 7.0/10

英伟达 2026 年 8 月的研究表明，对 AI 模型周围的“马具”（即工具、记忆和工作流逻辑的脚手架）进行微调，即使底层模型较弱，也能确保智能体表现出色。在 SWE-bench 和 GAIA 等基准测试中，带有精心设计和微调马具的弱开源模型表现优于旗舰前沿模型。 这一发现将 AI 开发的重点从原始模型能力转移到周围的马具上，这对智能体的可靠性和微调策略至关重要。它表明，组织可以使用性能较弱的模型来实现高性能智能体，从而可能降低成本并使 AI 智能体更容易获得。 该研究解决了 AI 智能体采用的最大障碍之一：在长期任务中保持智能体不偏离轨道。马具包括微调方法、护栏和监督系统，以防止智能体“走火入魔”。

rss · TechCrunch · 8月21日 19:43

**背景**: 在 AI 智能体系统中，“马具”指的是将模型与工具、记忆和工作流逻辑连接起来的脚手架，本质上使模型成为智能体。传统上，人们非常重视底层大型语言模型（LLM）的能力，但英伟达的研究表明，马具在系统中所占的比重比许多人意识到的要小，尤其是在复杂的多步骤任务中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aitoolly.com/ai-news/article/2026-08-22-nvidia-research-proves-the-ai-harness-and-fine-tuning-are-the-true-heroes-of-agent-performance-over">Nvidia: AI Harness and Fine-Tuning Outperform Base Models</a></li>
<li><a href="https://www.androguider.com/2026/08/nvidia-harness-vs-ai-model-why-fine.html">Nvidia Harness vs AI Model - Why Fine-Tuning Is Now More ...</a></li>
<li><a href="https://www.techbuzz.ai/articles/nvidia-research-ai-agent-control-beats-raw-model-power">Nvidia Research : AI Agent Control Beats Raw Model... | The Tech Buzz</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Nvidia`, `#fine-tuning`, `#AI reliability`, `#model harness`

---