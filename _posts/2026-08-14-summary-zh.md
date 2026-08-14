---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 83 条内容中筛选出 15 条重要资讯。

---

1. [开源模型 Qwen 3.8 27B 推理能力强，引发 AI 商品化讨论](#item-1) ⭐️ 8.0/10
2. [为什么 Opus 5 用起来感觉更差：一位开发者的批评](#item-2) ⭐️ 8.0/10
3. [OpenAI 的 GPT-5.6 构建者指南：更快、更便宜的 AI 代理](#item-3) ⭐️ 8.0/10
4. [OpenAI 预览 GPT-5.6 Sol 的 Ultrafast API 服务层](#item-4) ⭐️ 8.0/10
5. [DeepSeek V4 Pro 0813 发布，开放权重](#item-5) ⭐️ 8.0/10
6. [加州批准自动驾驶卡车在高速公路上测试](#item-6) ⭐️ 8.0/10
7. [谷歌发布 Gemini 3.7 Flash，面向编程与智能体](#item-7) ⭐️ 8.0/10
8. [2004 年 RuneScape 如何在 56k 拨号网络中运行多人 RPG](#item-8) ⭐️ 8.0/10
9. [不要分类，要幻觉：一种新的标签技术](#item-9) ⭐️ 7.0/10
10. [PayPal 与 Stripe 和 Advent 的出售谈判升温](#item-10) ⭐️ 7.0/10
11. [伊朗黑客攻击美国水务设施：已知情况](#item-11) ⭐️ 7.0/10
12. [Meta 的 Glimmer 与 Muse Spark：AI 真的为所有人服务吗？](#item-12) ⭐️ 7.0/10
13. [苹果提议对 iOS 应用外部购买收取 15%佣金](#item-13) ⭐️ 7.0/10
14. [美国法院将公开报告政府间谍软件使用情况](#item-14) ⭐️ 7.0/10
15. [Uber 与 Pony.ai 扩大合作，将在欧洲部署 2000 辆机器人出租车](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [开源模型 Qwen 3.8 27B 推理能力强，引发 AI 商品化讨论](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 8.0/10

Qwen 3.8 27B，一款新的开源稠密 27B 模型，带有视觉编码器和 262K 原生上下文，已在 Hugging Face 上发布。它展示了强大的推理能力，通过了此前只有 Gemma 4 才能通过的私有基准测试。 此次发布凸显了前沿 AI 的快速商品化，像 Qwen 3.8 27B 这样的开源模型实现了曾经专属于大型专有实验室的能力。这可能迫使 OpenAI 和 Anthropic 等公司在原始智能之外进行差异化竞争，并为开发者提供高性能的本地模型。 该模型可在笔记本电脑上本地运行，有用户指出在启用 MTP 的情况下，解决一个私有基准测试需要 5 倍的 token 和 12 分 30 秒，且 VRAM 使用效率似乎不如 Gemma 4 或 Glimmer。社区成员还注意到其独特的“穴居人”式思考轨迹风格可能影响 MTP 预测，以及 Jinja 模板问题需要变通解决。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**背景**: Qwen 是阿里巴巴开发的一系列开放权重大型语言模型。3.8 代基于 Qwen 3.5 架构，提供稠密 27B 参数模型，带有视觉编码器，支持高达 262K token 的上下文，可通过 RoPE 缩放扩展到 1M。像这样的开源模型正日益与专有模型竞争，推动了关于 AI 商品化的讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen / Qwen 3 . 8 - 27 B · Hugging Face</a></li>
<li><a href="https://lmstudio.ai/models/qwen3.8">Qwen 3 . 8</a></li>
<li><a href="https://benchlm.ai/models/qwen3-8-27b">Qwen 3 . 8 - 27 B Benchmarks & Context (August 2026) | BenchLM.ai</a></li>

</ul>
</details>

**社区讨论**: 社区情绪非常积极，用户称赞模型的推理能力和本地性能，但也有人指出效率上的权衡。关于 AI 商品化的讨论很多，有用户质疑当前沿智能变得广泛可用时，OpenAI 和 Anthropic 将如何生存。其他人则分享了关于思考轨迹和模板问题的技术观察。

**标签**: `#AI`, `#Open Source`, `#LLM`, `#Qwen`, `#Local Models`

---

<a id="item-2"></a>
## [为什么 Opus 5 用起来感觉更差：一位开发者的批评](https://mun-logadan.github.io/why-does-opus-5-feel-worse/) ⭐️ 8.0/10

一位开发者发表了一篇题为“为什么 Opus 5 用起来感觉更差”的博客文章，批评该模型的省略式写作风格以及向面向智能体通信的转变。这篇文章在 Hacker News 上引发了大量讨论，获得了 733 分和 668 条评论。 这一批评凸显了为智能体间通信优化的 AI 模型与人类用户需求之间日益增长的矛盾，人类用户觉得这种新风格令人疲惫且不太愉快。随着模型能力增强，与它们交互的用户体验成为关键瓶颈，影响开发者与从业者的采用率和满意度。 作者和评论者指出，Opus 5 写作风格省略，使用抽象措辞和无生命主语，可能感觉像“揭示的洞见”，但常常令人疲惫。一些人推测，后训练已将重点从人类可读性转向“智能体语言”，优先考虑子智能体和推理链的效率，而非人类友好的表达。

hackernews · numeri · 8月14日 10:12 · [社区讨论](https://news.ycombinator.com/item?id=49296740)

**背景**: Claude Opus 5 是 Anthropic 最新的旗舰 AI 模型，以其先进的推理和编码能力著称。该模型的沟通风格一直是讨论的话题，一些用户发现它比之前的版本更冗长或更省略。向面向智能体通信的转变反映了 AI 开发的更广泛趋势，即模型越来越多地用于多智能体系统中相互通信，有时以牺牲人类可读性为代价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coderabbit.ai/blog/opus-5-model-review">Claude Opus 5 Benchmarks for AI Code Review | CodeRabbit</a></li>
<li><a href="https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5">Prompting Claude Opus 5 - Claude Platform Docs</a></li>
<li><a href="https://arxiv.org/html/2502.14321v2">Beyond Self-Talk: A Communication-Centric Survey of LLM-Based Multi-Agent Systems</a></li>

</ul>
</details>

**社区讨论**: 社区讨论大体上同意作者的批评，许多用户分享了类似的体验，认为 Opus 5 的沟通风格令人疲惫且不太愉快。一些用户推测该模型是为智能体间通信优化的，而另一些用户则建议需要人类协作基准来解决这个问题。少数用户报告称在项目中更喜欢其他模型，如 OpenAI 的 Sol。

**标签**: `#AI`, `#LLM`, `#user experience`, `#model behavior`, `#agent design`

---

<a id="item-3"></a>
## [OpenAI 的 GPT-5.6 构建者指南：更快、更便宜的 AI 代理](https://openai.com/index/builders-guide-to-gpt-5-6) ⭐️ 8.0/10

OpenAI 发布了一份构建者指南，展示了初创公司如何利用 GPT-5.6 构建更快、更具成本效益的 AI 代理，重点介绍了更智能的模型选择和新的 Responses API 功能。 该指南标志着 GPT-5.6 已成熟可用于生产环境，为开发者提供了优化成本和性能的实用策略。它可能加速初创公司对 AI 代理的采用，并影响开发者如何在模型变体之间进行选择。 GPT-5.6 包含 Sol、Terra 和 Luna 等模型变体，各自适用于不同任务；Responses API 现在支持零数据保留（ZDR）和重用推理项，以减少 token 使用和延迟。该指南强调避免为简单任务使用过强的模型以节省 token。

rss · OpenAI Blog · 8月13日 11:00

**背景**: GPT-5.6 是 OpenAI 最新的模型系列，提供多种变体以满足不同的成本和性能需求。Responses API 是 OpenAI 用于构建有状态 AI 代理的高级接口，支持文本和图像输入。模型选择对于在 AI 应用中平衡质量和成本至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eesel.ai/blog/gpt-5-6-vs-claude">GPT - 5 . 6 vs Claude: which AI model wins in 2026? | eesel AI</a></li>
<li><a href="https://www.digitalapplied.com/blog/gemini-3-7-flash-vs-sonnet-5-gpt-5-6-terra-benchmarks">Gemini 3.7 Flash vs Sonnet 5 vs GPT - 5 . 6 Terra: Real Wins</a></li>
<li><a href="https://shortcut.innov8academy.in/p/how-to-prompt-gpt-5-6-without-wasting-tokens">Model selection and prompting explained! | ShortCu8</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://openai.com/index/new-tools-and-features-in-the-responses-api/">New tools and features in the Responses API | OpenAI</a></li>

</ul>
</details>

**标签**: `#GPT-5.6`, `#OpenAI`, `#AI agents`, `#API`, `#startups`

---

<a id="item-4"></a>
## [OpenAI 预览 GPT-5.6 Sol 的 Ultrafast API 服务层](https://openai.com/index/previewing-ultrafast) ⭐️ 8.0/10

OpenAI 宣布预览 Ultrafast，这是一个针对其 GPT-5.6 Sol 模型的新 API 服务层，可提供高达 14 倍的推理速度和每秒最多 750 个输出令牌。该服务层由 Cerebras 硬件提供支持。 这一显著的性能提升可能会吸引需要低延迟、高吞吐量 AI 推理的企业用户，可能改变云 AI 市场的竞争格局。这也凸显了 Cerebras 等专用硬件在 AI 基础设施中日益重要的作用。 Ultrafast 服务层目前处于预览阶段，由 Cerebras 提供支持，其采用晶圆级集成技术，与传统 GPU 集群相比可降低延迟。该服务层是 OpenAI 更广泛的 API 服务产品的一部分，其中包括规模层级和优先处理选项。

rss · OpenAI Blog · 8月13日 10:00

**背景**: GPT-5.6 是 OpenAI 于 2026 年 7 月发布的大型语言模型系列，其中 Sol 是最强大的变体。Cerebras Systems 以其晶圆级处理器而闻名，这是有史以来最大的 AI 半导体，并于 2026 年与 OpenAI 签署了合作协议。Ultrafast 服务层利用 Cerebras 硬件实现了速度提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6_Sol">GPT-5.6 Sol</a></li>
<li><a href="https://openai.com/api-scale-tier/">Scale Tier for API Customers | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#API`, `#GPT-5.6`, `#performance`, `#Cerebras`

---

<a id="item-5"></a>
## [DeepSeek V4 Pro 0813 发布，开放权重](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek V4 Pro 0813 现已通过 OpenRouter 的 API 提供，并且开放权重已在 Hugging Face 上发布，拥有 1.7 万亿参数，文件大小为 893 GB。该模型支持 100 万 token 的上下文窗口，最大输出 384K token。 此次发布意义重大，因为 DeepSeek 继续提供具有竞争力的开放权重模型，挑战主要 AI 实验室的专有模型。拥有 1.7 万亿参数的开放权重模型，可能会加速 AI 社区的研究和开发，尤其是对于偏好自托管或微调模型的用户。 该模型采用混合专家（MoE）架构，在 OpenRouter 上的定价为每百万输入 token 0.435 美元，每百万输出 token 0.87 美元。它支持思考和非思考模式、工具调用以及 Responses API，适用于智能体工作流。

rss · Simon Willison · 8月12日 23:59

**背景**: DeepSeek 是一家以发布开放权重大型语言模型而闻名的中国 AI 公司。V4 系列包括早期的模型，如 DeepSeek-V4-Pro（4 月）和 DeepSeek-V4-Flash-0731（7 月），这些模型也开放了权重。OpenRouter 是一个提供统一 API 访问多种 AI 模型的平台，使开发者更容易比较和集成不同的模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/deepseek-v4-pro">DeepSeek V4 Pro 0813 (max) - Intelligence, Performance & Price Analysis</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek-ai/DeepSeek-V4-Flash-0731 · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 提供的内容中没有社区评论，但文章提到基准测试结果曾在 Reddit 和 Hacker News 上分享，不过 Reddit 上的帖子被版主删除。文章还指出 DeepSeek 没有官方公告页面是一个小问题。

**标签**: `#AI`, `#DeepSeek`, `#model release`, `#open weights`, `#LLM`

---

<a id="item-6"></a>
## [加州批准自动驾驶卡车在高速公路上测试](https://techcrunch.com/2026/08/14/self-driving-trucks-are-officially-testing-on-california-highways/) ⭐️ 8.0/10

Aurora Innovation 和 Kodiak AI 已获得加州车管局的许可，可以在加州高速公路上测试其自动驾驶卡车，这标志着自动驾驶卡车领域的一个重要监管里程碑。 这一批准是自动驾驶卡车在加州这样的关键市场实现商业部署的重要一步，可能加速行业采用，并对货运、物流和全国监管框架产生影响。 这些许可允许 Aurora 和 Kodiak 在加州高速公路上运营其自动驾驶卡车，但初期可能仍需安全驾驶员。两家公司已在德克萨斯州开展无人驾驶运营，此次加州批准扩大了它们的测试范围。

rss · TechCrunch · 8月14日 20:37

**背景**: 自动驾驶卡车利用先进的传感器、人工智能和控制系统，在无需人工干预的情况下在高速公路上行驶。加州在批准自动驾驶汽车测试方面一直持谨慎态度，因此这次批准是一个值得注意的监管里程碑。Aurora 和 Kodiak 是自动驾驶卡车领域的领先开发商，分别拥有 Aurora Driver 和 Kodiak Driver 等技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aurora.tech/">aurora . tech</a></li>
<li><a href="https://kodiak.ai/?gad=1">Kodiak AI | Autonomous Trucking & AI -Powered Ground Autonomy ...</a></li>
<li><a href="https://tanktransport.com/2026/06/autonomous-trucking-expansion/">Autonomous Trucking Expansion: 7 Powerful but... | Tank Transport</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#self-driving trucks`, `#regulation`, `#California`, `#transportation`

---

<a id="item-7"></a>
## [谷歌发布 Gemini 3.7 Flash，面向编程与智能体](https://www.producthunt.com/products/gemini-3-7-flash) ⭐️ 8.0/10

谷歌发布了 Gemini 3.7 Flash，这是一款专为编程和智能体任务设计的新模型，定位为其最智能的“工作马”模型。该模型基于 Gemini 3.6 Flash，现已为 160 多个国家的 AI Pro 和 Ultra 订阅用户提供 Gemini Spark 服务。 此次发布巩固了谷歌在竞争激烈的 AI 模型市场中的地位，尤其是对依赖编程辅助和自主智能体的开发者与企业而言。这标志着模型正朝着兼顾性能与效率、面向实际任务应用的专业化方向发展。 Gemini 3.7 Flash 基于 Gemini 3.6 Flash 构建，并已在涵盖推理、编程、智能体工具使用、多模态能力、多语言性能和长上下文理解等基准上进行了评估。该模型现已集成到 Gemini Spark 中，面向 160 多个国家的 Google AI Pro 和 Ultra 订阅用户提供。

rss · Product Hunt (AI应用) · 8月13日 18:16

**背景**: Gemini 是 Google DeepMind 开发的多模态大语言模型系列，是 LaMDA 和 PaLM 2 的继任者，包含 Pro、Flash 和 Flash Lite 等变体，并为 Gemini 聊天机器人提供支持。智能体 AI 指能够自主追求目标、使用工具并采取行动的 AI 系统，与仅回答问题的传统聊天机器人形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-7-flash/">Gemini 3 . 7 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3 . 7 Flash : our most intelligent workhorse model</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Google`, `#coding`, `#agents`, `#model release`

---

<a id="item-8"></a>
## [2004 年 RuneScape 如何在 56k 拨号网络中运行多人 RPG](https://www.reddit.com/r/programming/comments/1vo44t4/how_2004_runescape_fit_a_multiplayer_rpg_into_56k/) ⭐️ 8.0/10

发布了一篇详细的技术分析，解释了 2004 年的 RuneScape 如何在 56k 拨号连接上运行多人 RPG，仅用每秒 5 千字节的带宽就实现了可玩的性能。文章剖析了用于最小化网络流量的巧妙协议设计和数据压缩技术。 这一分析强调了在极端带宽限制下优化网络协议的永恒工程原理，这些原理对现代游戏开发、物联网和低带宽环境仍然具有现实意义。它展示了创造性解决问题如何克服硬件限制，为今天面临类似挑战的开发人员提供了宝贵的经验。 文章可能涵盖了特定的技术，如增量压缩、客户端预测和高效的数据包批处理，这些对于在拨号网络上保持游戏响应至关重要。文章还提到该游戏每个服务器可支持多达数千名玩家，同时在浏览器中显示数十名玩家。

reddit · r/programming · /u/fagnerbrack · 8月14日 11:01

**背景**: RuneScape 是一款大型多人在线角色扮演游戏（MMORPG），于 2001 年首次发布。2004 年，它是一款基于 Java 的浏览器游戏，必须适应使用 56k 拨号调制解调器的玩家，这种调制解调器的最大下载速度约为每秒 56 千比特（约每秒 7 千字节）。游戏开发者必须设计一种网络协议，在最小化数据使用的同时，仍能提供流畅的多人游戏体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jkm.dev/posts/how-2004-runescape-fit-a-multiplayer-rpg-into-56k-dialup/">How 2004 RuneScape fit a multiplayer RPG into 56k dial-up · jkm.dev</a></li>
<li><a href="https://2004.lostcity.rs/">Non-Affiliation Disclaimer | 2004 Scape</a></li>
<li><a href="https://www.youtube.com/watch?v=0CEwxx4iODA">Runescape 2004 - Lost City | 2004 scape - YouTube</a></li>

</ul>
</details>

**社区讨论**: Reddit 上的讨论可能包括开发者和爱好者的评论，他们分享自己使用拨号上网游戏的经验，并称赞 RuneScape 原始开发者的巧妙设计。有些人可能会对提到的具体技术进行辩论，或将其与现代网络实践进行比较。

**标签**: `#network programming`, `#game development`, `#optimization`, `#history`, `#systems design`

---

<a id="item-9"></a>
## [不要分类，要幻觉：一种新的标签技术](https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/) ⭐️ 7.0/10

Simon Willison 强调了 Doug Turnbull 的方法，即使用 LLM 在不知道现有词汇的情况下幻觉出标签，然后通过向量嵌入将它们与真实标签匹配。该方法被展示为一种为未标记内容打标签的实用解决方案。 该技术提供了一种可扩展的方式来为大型内容库打标签，尤其是在标签词汇量过大而无法放入 LLM 提示的情况下。它利用嵌入的语义理解来弥合生成标签与现有标签之间的差距，可能改善内容管理和搜索。 示例提示包含标签形状的样例，以引导模型的幻觉，例如“家具 / 客厅家具 / 咖啡桌和茶几 / 咖啡桌”。匹配步骤使用向量嵌入来找到与幻觉标签最接近的现有标签。

rss · Simon Willison · 8月14日 21:54

**背景**: 向量嵌入是文本的数值表示，能够捕捉语义，使得相似的词或短语在向量空间中距离较近。LLM 可以生成看似合理的标签，但它们可能无法匹配现有的受控词汇表。该方法结合了 LLM 的生成能力和嵌入的检索能力，以大规模自动化打标签。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vector_embedding">Vector embedding</a></li>
<li><a href="https://www.geeksforgeeks.org/nlp/what-are-vector-embeddings/">What are Vector Embeddings? - GeeksforGeeks</a></li>

</ul>
</details>

**标签**: `#LLM`, `#embeddings`, `#tagging`, `#search`, `#content management`

---

<a id="item-10"></a>
## [PayPal 与 Stripe 和 Advent 的出售谈判升温](https://techcrunch.com/2026/08/14/talks-to-sell-paypal-to-stripe-and-advent-are-heating-up/) ⭐️ 7.0/10

据报道，PayPal 正在与 Stripe 和私募股权公司 Advent International 进行深入谈判，拟被收购，同时其新任 CEO 正在制定扭亏为盈的战略。 这一潜在收购可能重塑金融科技格局，整合主要支付参与者，并可能影响数百万用户和商家。这也标志着私募股权对支付领域的重大进军。 据报道，谈判仍在进行中，细节仍属推测。Stripe 和 Advent 的参与表明交易结构可能复杂，可能涉及财团或联合收购。

rss · TechCrunch · 8月14日 22:43

**背景**: PayPal 是一家主要的在线支付公司，近年来面临增长放缓和竞争加剧。Stripe 是领先的支付处理平台，而 Advent International 是一家全球私募股权公司。出售可能有助于 PayPal 在新领导下加速转型。

**标签**: `#fintech`, `#M&A`, `#PayPal`, `#Stripe`, `#private equity`

---

<a id="item-11"></a>
## [伊朗黑客攻击美国水务设施：已知情况](https://techcrunch.com/2026/08/14/what-we-know-about-the-alleged-iranian-hacks-on-u-s-water-utilities/) ⭐️ 7.0/10

2026 年 7 月底至 8 月初，据称由伊朗支持的黑客攻击并侵入了美国多家水务公司的系统，影响了包括明尼苏达州和密歇根州在内的至少七个州。联邦调查局（FBI）和环境保护署（EPA）已发出警报，调查仍在进行中。 这些攻击凸显了关键基础设施（尤其是水务系统）面对国家支持的网络威胁时的脆弱性。成功的入侵可能扰乱水处理过程，对公众健康和安全构成风险，并凸显了整个行业加强网络安全措施的紧迫性。 攻击涉及对系统的未经授权调整，可能影响水处理过程。当局正在调查是否由伊朗行为者负责，EPA 和 CISA 已提供建议，以保护人机界面（HMI）并限制漏洞。

rss · TechCrunch · 8月14日 19:04

**背景**: 水务公司属于关键基础设施，其操作技术（OT）系统（如人机界面 HMI）通常容易受到网络攻击。EPA 和 CISA 长期以来一直强调水务系统网络安全的重要性，提供风险评估和工具包以帮助公用事业加强防御。包括与伊朗有关联的国家支持的黑客组织，越来越多地将此类基础设施作为目标，以施加压力或造成破坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/14/what-we-know-about-the-alleged-iranian-hacks-on-u-s-water-utilities/">What we know about the alleged Iranian hacks on US water ...</a></li>
<li><a href="https://www.cbsnews.com/news/us-investigating-iran-cyberattack-minnesota-water-systems/">U.S. investigating if Iran was behind cyberattack on water ...</a></li>
<li><a href="https://www.thetechedvocate.org/unprecedented-iran-cyberattacks-target-us-water-heres-what-you-need-to-know-now/">Iran Cyberattacks Hit US Water Systems in 2026: What You Need ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#critical infrastructure`, `#Iran`, `#water utilities`, `#hacking`

---

<a id="item-12"></a>
## [Meta 的 Glimmer 与 Muse Spark：AI 真的为所有人服务吗？](https://techcrunch.com/video/does-mark-zuckerberg-really-believe-ai-is-for-everyone/) ⭐️ 7.0/10

Meta 于 2026 年 8 月 10 日发布了开放权重 AI 模型 Glimmer，任何人都可以下载并在自己的硬件上运行。这与其更强大的 Muse Spark 模型形成对比，后者仍为专有，仅通过 Meta 的 API 访问。 此举凸显了开放与封闭 AI 发展之间的持续张力，因为扎克伯格倡导 AI“为所有人服务”，却将最先进的模型保持专有。这可能影响关于 AI 可及性和监管的行业辩论，影响开发者、研究人员和政策制定者。 Glimmer 是一个 300 亿参数的 LLM，从更大的 Muse Spark 模型中蒸馏而来，后者可处理百万 token 的上下文。扎克伯格表示 Meta 将发布 Muse Spark 1.2 作为开放权重模型，但时间表尚不明确。

rss · TechCrunch · 8月14日 15:43

**背景**: 开放权重模型发布训练后 AI 模型的学习参数，允许他人下载和使用，但修改和再分发取决于许可证。Meta 发布 Glimmer 延续了其开源 Llama 模型的历史，而 Muse Spark 是其 Meta Superintelligence Labs 开发的新 Muse 系列的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Muse_Spark">Muse Spark</a></li>
<li><a href="https://www.theregister.com/ai-and-ml/2026/08/10/zuck-rekindles-open-weights-llama-drama-with-muse-glimmer/5285666">Zuck rekindles open weights Llama drama with Muse Glimmer</a></li>

</ul>
</details>

**标签**: `#AI`, `#Meta`, `#open-source`, `#AI models`, `#tech policy`

---

<a id="item-13"></a>
## [苹果提议对 iOS 应用外部购买收取 15%佣金](https://techcrunch.com/2026/08/14/apple-proposes-to-take-a-15-cut-of-purchases-made-outside-the-app-store/) ⭐️ 7.0/10

苹果已向联邦法官提议，允许其对 iOS 应用中通过外部链接完成的购买收取最高 15%的佣金，这与其传统的 30% App Store 佣金相比是一个重大转变。该提议是在 Epic 诉苹果案中 2025 年 4 月的法院命令要求苹果允许外部购买链接之后提出的。 该提议可能重塑应用商店的经济模式和开发者收入，可能为苹果如何从外部购买中获利开创先例。它直接影响软件行业，尤其是依赖 iOS 应用的开发者，并且是正在进行的 Epic 诉苹果法律战中的关键进展。 拟议的费用结构对美国境内通过苹果应用内购买系统之外完成的购买收取 5%至 15%的费用。然而，该提议并未确立新的 App Store 政策，苹果不能仅因提交计划就开始收取佣金；这需要法院批准。

rss · TechCrunch · 8月14日 14:54

**背景**: Epic 诉苹果案始于 2020 年 8 月，挑战了苹果 App Store 的做法，包括 30%的佣金和反引导规则。2021 年，法院大体上判苹果胜诉，但命令其放宽反引导条款。2025 年 4 月的命令要求苹果允许外部购买链接，从而促成了这一提议。该案现已提交至最高法院，最高法院于 2026 年 6 月同意审理苹果的上诉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dribba.com/en/blog/compras-dentro-de-la-app-apple-comision-2026">In- app purchase : what changed in Apple 's rules and... | Blog Dribba</a></li>
<li><a href="https://applemagazine.com/apple-app-store-fees-external-purchases/">Apple Proposes 15% App Store Fees for External Purchases</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epic_Games_v._Apple">Epic Games v. Apple - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Apple`, `#App Store`, `#antitrust`, `#developer economics`, `#legal`

---

<a id="item-14"></a>
## [美国法院将公开报告政府间谍软件使用情况](https://techcrunch.com/2026/08/14/us-courts-will-start-publishing-how-often-the-government-uses-spyware/) ⭐️ 7.0/10

美国法院行政办公室宣布，将开始公开披露法官授权使用间谍软件对犯罪嫌疑人进行窃听的次数，报告将于 2029 年开始。 这标志着向监控透明度迈出的重要一步，让公众更清楚地了解政府使用黑客工具进行实时通信拦截的频率。它可能为公民自由和间谍软件法律监督的辩论提供信息。 报告将涵盖联邦政府使用间谍软件和黑客工具进行实时通信监控的情况，从 2029 年开始。该公告由美国法院行政办公室向 TechCrunch 发布。

rss · TechCrunch · 8月14日 13:29

**背景**: 在美国，执法机构必须获得法院授权才能进行窃听，包括使用间谍软件或黑客工具的窃听。历史上，此类授权的频率并未公开披露，引发了对监控过度的担忧。这一新的报告要求旨在提高问责制和公众意识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/14/us-courts-will-start-publishing-how-often-the-government-uses-spyware/">US courts will start publishing how often the government uses ...</a></li>
<li><a href="https://www.digitaltrends.com/computing/u-s-courts-will-now-make-government-use-of-spyware-tools-public/">U.S. courts will now make government use of spyware tools ...</a></li>
<li><a href="https://techresearchonline.com/news/us-courts-government-spyware-reporting-2029/">US Courts to Reveal Government Spyware Use Starting in 2029</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#government`, `#legal`, `#spyware`

---

<a id="item-15"></a>
## [Uber 与 Pony.ai 扩大合作，将在欧洲部署 2000 辆机器人出租车](https://techcrunch.com/2026/08/14/uber-and-pony-ai-plan-to-bring-2000-robotaxis-to-europe/) ⭐️ 7.0/10

Uber 与 Pony.ai 宣布将其机器人出租车合作伙伴关系扩展到欧洲另外四个城市，新增 2000 辆车辆。这继他们在克罗地亚萨格勒布的首次推出之后，标志着将自动驾驶网约车引入欧洲的重要一步。 此次扩张标志着 Uber 将自动驾驶汽车整合到其欧洲业务中的重大举措，可能重塑网约车市场。同时，这也增强了 Pony.ai 的全球影响力，使其与 Waymo 和 Momenta 等竞争对手一起成为自动驾驶行业的关键参与者。 根据扩大的合作伙伴关系，Pony.ai 将提供其 L4 级自动驾驶技术、乘客体验和运营专业知识，而 Uber 将负责客户接入、预订、支付和客户服务。Pony.ai 已通过其 Gen-7 机器人出租车实现全市范围内的单位经济盈亏平衡，并计划在明年年底前将车队扩展到 3000 多辆。

rss · TechCrunch · 8月14日 10:44

**背景**: 机器人出租车是无需人类驾驶员即可提供网约车服务的自动驾驶车辆。Uber 一直与包括 Pony.ai 和 Momenta 在内的多家自动驾驶公司合作，在不同地区部署机器人出租车。Pony.ai 是一家领先的自动驾驶公司，运营机器人出租车、机器人卡车和私人拥有车辆业务部门，并一直在全球扩展其业务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://investor.uber.com/news-events/news/press-release-details/2026/Pony-ai-and-Uber-Expand-Partnership-to-Deploy-Over-2000-Robotaxis-in-Europe/default.aspx">Uber Technologies, Inc. - Pony.ai and Uber Expand Partnership ...</a></li>
<li><a href="https://www.pony.ai/">Pony.ai</a></li>
<li><a href="https://ir.pony.ai/news-releases/news-release-details/pony-ai-inc-realized-gen-7-robotaxi-city-wide-ue-breakeven-set">PONY AI Inc. Realized Gen-7 Robotaxi city-wide UE Breakeven ...</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#robotaxi`, `#Uber`, `#Pony.ai`, `#Europe`

---