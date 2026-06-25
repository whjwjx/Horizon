---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 68 条内容中筛选出 15 条重要资讯。

---

1. [OpenAI 携手博通推出首款自研 AI 芯片 'Jalapeno'](#item-1) ⭐️ 9.0/10
2. [GPT-5 Pro 解决三年免疫学谜题](#item-2) ⭐️ 8.0/10
3. [《自然》评论质疑微软量子芯片主张](#item-3) ⭐️ 8.0/10
4. [谷歌 Play 商店将允许替代计费，遵循 Epic 和解协议](#item-4) ⭐️ 8.0/10
5. [Papers with Code 重建 OCR 中心，汇集顶级模型](#item-5) ⭐️ 8.0/10
6. [HDD-RoPE：一种超越 xPos 的新型位置编码](#item-6) ⭐️ 8.0/10
7. [RubyLLM：面向主流 AI 提供商的统一 Ruby 框架](#item-7) ⭐️ 7.0/10
8. [Bunny DNS 免费：最多支持 500 个域名](#item-8) ⭐️ 7.0/10
9. [OpenAI 通过 Appia 基金会支持先进 AI 共享标准](#item-9) ⭐️ 7.0/10
10. [MDN 浏览器兼容数据转为 SQLite 数据库](#item-10) ⭐️ 7.0/10
11. [LLM 生成的求职申请抹去候选人身份](#item-11) ⭐️ 7.0/10
12. [Datasette 1.0a35 新增创建/修改表界面](#item-12) ⭐️ 7.0/10
13. [欧洲反击美国芯片战限制](#item-13) ⭐️ 7.0/10
14. [工程师岗位在 AI 冲击下最具韧性](#item-14) ⭐️ 7.0/10
15. [谷歌再失两名顶尖 AI 研究员，转投 Anthropic](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 携手博通推出首款自研 AI 芯片 'Jalapeno'](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 与博通联合发布了名为 'Jalapeno' 的自研 AI 推理芯片，专为大语言模型设计，由台积电制造，并在 OpenAI 自身模型的辅助下仅用九个月完成开发。 这标志着 OpenAI 首次涉足自研芯片领域，减少对外部硬件（如 Nvidia GPU）的依赖，有望大幅降低推理成本，可能重塑 AI 硬件格局。 该芯片针对推理任务而非训练进行了优化，其开发过程中使用了 OpenAI 的模型来辅助设计和优化，从而加速了进程。芯片由台积电制造，而非英特尔。

hackernews · TechCrunch · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理是运行已训练模型以生成预测的过程，与需要大量算力的训练不同。目前大多数 AI 公司依赖 Nvidia 的 GPU 来完成这两项任务，但像 Google TPU 这样的自研芯片已在推理方面展现出显著的效率提升。OpenAI 此举顺应了 AI 硬件垂直整合的行业趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/openai-broadcom-jalapeno-inference-chip/">OpenAI and Broadcom unveil LLM-optimized inference chip | OpenAI</a></li>
<li><a href="https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html">OpenAI and Broadcom reveal Jalapeno, first AI chip in partnership</a></li>
<li><a href="https://interestingengineering.com/ai-robotics/openai-jalapeno-ai-inference-chip-broadcom">OpenAI unveils Jalapeño chip for large-scale inference workloads</a></li>

</ul>
</details>

**社区讨论**: 评论者对 OpenAI 模型如何加速芯片设计表示好奇，也有人怀疑这可能是营销噱头。其他人指出芯片由台积电制造，并讨论了将模型权重固化到硅片中以实现极致效率的潜力，提及了 Taalas 等公司。

**标签**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#inference`, `#Broadcom`

---

<a id="item-2"></a>
## [GPT-5 Pro 解决三年免疫学谜题](https://openai.com/index/gpt-5-immunology-mystery) ⭐️ 8.0/10

免疫学家 Derya Unutmaz 使用 GPT-5 Pro 解决了一个关于 T 细胞行为的三年未解之谜，揭示了传统方法未能发现的见解。 这一突破展示了 GPT-5 加速生物医学研究的能力，可能推动癌症免疫疗法和自身免疫疾病治疗的进展。 GPT-5 Pro 是 OpenAI 的推理模型，被用于分析复杂的免疫学数据，识别出解释该谜题的模式。解决方案涉及理解 T 细胞受体信号传导和激活机制。

rss · OpenAI Blog · 6月23日 17:00

**背景**: T 细胞是一种对适应性免疫至关重要的白细胞。它们通过 T 细胞受体（TCR）识别抗原并被激活以对抗感染或癌症。该谜题涉及 T 细胞行为的特定方面，已困扰研究人员三年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-5/">Introducing GPT-5 | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/T_cell">T cell - Wikipedia</a></li>

</ul>
</details>

**标签**: `#GPT-5`, `#immunology`, `#AI in science`, `#biomedical research`, `#breakthrough`

---

<a id="item-3"></a>
## [《自然》评论质疑微软量子芯片主张](https://www.theverge.com/tech/956450/nature-microsoft-quantum-computing-majorana-1-claims) ⭐️ 8.0/10

《自然》周三发表的一篇评论质疑微软为其 Majorana 1 量子芯片所声称的拓扑量子比特的有效性，该芯片于 2025 年 2 月发布。 来自顶级科学期刊的同行评审评论对微软声称的重大量子计算突破提出质疑，可能影响拓扑量子比特研究的可信度以及该公司的量子路线图。 该评论特别质疑 Majorana 1 芯片背后的基础技术，微软称该芯片采用拓扑量子比特作为未来量子计算机的构建模块。

rss · The Verge · 6月24日 20:54

**背景**: 拓扑量子比特是一种利用任意子和编织来实现固有错误保护的量子比特，比传统量子比特更稳定。微软多年来一直追求这种方法，但实验实现已被证明极其困难，许多物理学家仍对该公司的说法持怀疑态度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Majorana_1">Majorana 1 - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Topological_qubit">Topological qubit</a></li>
<li><a href="https://www.sciencenews.org/article/microsoft-topological-quantum-majorana">Physicists are mostly unconvinced by Microsoft’s new topological quantum chip</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#Microsoft`, `#topological qubits`, `#Nature`, `#controversy`

---

<a id="item-4"></a>
## [谷歌 Play 商店将允许替代计费，遵循 Epic 和解协议](https://www.theverge.com/policy/956296/google-play-app-store-alternative-billing-fee-antitrust) ⭐️ 8.0/10

谷歌宣布将开始推出允许全球开发者在 Play 商店中使用替代计费方式的变更，这是其与 Epic Games 反垄断和解的一部分。 此举可能重塑数字市场竞争，减少谷歌对应用内支付的控制，并可能降低开发者和消费者的成本。 这些变更包括将 30%的固定佣金降低，并对替代计费方式收取最高 9%或 20%的服务费，尽管法院尚未批准该和解协议。

rss · The Verge · 6月24日 17:36

**背景**: Epic Games 的诉讼指控谷歌在 Android 应用分发和应用内支付方面维持非法垄断。该和解是在 2023 年陪审团裁定谷歌行为反竞争之后达成的。替代计费允许开发者使用第三方支付处理器，绕过谷歌的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://solidgate.com/blog/external-billing-google-play/">Google Play external billing: Maximize revenue from your app</a></li>
<li><a href="https://overcentral.com/en/google-settles-epic-games-antitrust-lawsuit-with-20-play-store-fee-reduction/">Google Settles Epic Games Antitrust Lawsuit With 20... | Overcentral</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#Google Play`, `#app store`, `#billing`, `#policy`

---

<a id="item-5"></a>
## [Papers with Code 重建 OCR 中心，汇集顶级模型](https://www.reddit.com/r/MachineLearning/comments/1ueiam6/find_the_best_opensource_ocr_models_in_one_place/) ⭐️ 8.0/10

Niels Rogge 重建了 Papers with Code 网站，新增了专门的 OCR 任务页面，精选了顶级开源 OCR 模型和基准，包括百度最新发布的 Unlimited OCR（3B 参数，500M 激活）——采用参考滑动窗口注意力机制——以及 Mistral 的 OCR 4 API。 这个中心化平台帮助开发者和研究人员快速找到最适合文档数字化的 OCR 模型，这对于实现基于代理的 RAG 和依赖将杂乱 PDF 转换为干净 Markdown 的 AI 代理至关重要。 该页面列出了主要基准，如 OlmOCRBench（由 Ai2 创建）和 OmniDocBench（由上海人工智能实验室创建），推荐模型包括 Chandra OCR 2（开源，可自托管）和 Mistral OCR v4（API）。百度 Unlimited OCR 在 OmniDocBench v1.5 和 v1.6 上取得了最先进的结果。

reddit · r/MachineLearning · /u/NielsRogge · 6月24日 16:26

**背景**: 光学字符识别（OCR）将扫描文档和 PDF 转换为机器可读文本。近期大语言模型和注意力机制（如滑动窗口注意力）的进步显著提升了长文档 OCR 的准确性。基于代理的 RAG（检索增强生成）利用 OCR 将公司数据输入 AI 代理，使其能够回答问题并自动化工作流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/BaiduAI_News/status/2069322806748410291">Baidu AI on X: "We’re open-sourcing Unlimited OCR — built to read long documents in one pass. With 3B total parameters and only 500M activated, Unlimited OCR sets new end-to-end SOTA results on OmniDocBench v1.5 and v1.6. The key innovation is Reference Sliding Window Attention (R-SWA), https://t.co/cBRqmyRUKN" / X</a></li>
<li><a href="https://klu.ai/glossary/sliding-window-attention">What is Sliding Window Attention? — Klu</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSeek-OCR">GitHub - deepseek-ai/DeepSeek-OCR: Contexts Optical Compression · GitHub</a></li>

</ul>
</details>

**标签**: `#OCR`, `#open-source`, `#benchmarks`, `#RAG`, `#AI agents`

---

<a id="item-6"></a>
## [HDD-RoPE：一种超越 xPos 的新型位置编码](https://www.reddit.com/r/MachineLearning/comments/1uelcm9/high_dimensional_dynamic_rotary_positional/) ⭐️ 8.0/10

作者提出了高维动态旋转位置编码（HDD-RoPE），这是一种新颖的位置编码方法，在 TinyStories 数据集上比 xPos 收敛更快。 这项工作挑战了标准 RoPE 中位置是一维的假设，可能使 Transformer 学习更复杂的位置关系，并提高语言建模的效率。 HDD-RoPE 使用数据依赖的旋转速率，并可将查询/键块分解为任意大小（例如 4），对应多个旋转轴。开源代码和详细数学推导已在 GitHub 上发布。

reddit · r/MachineLearning · /u/mikayahlevi · 6月24日 18:16

**背景**: 旋转位置编码（RoPE）通过以固定速率旋转查询和键的元素对来编码位置。xPos 是 RoPE 的改进变体，引入了指数衰减。TinyStories 是一个由短故事组成的合成数据集，词汇量有限，常用于测试小型语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zeta.apac.ai/en/latest/zeta/nn/biases/xpos/">Xpos - zeta</a></li>
<li><a href="https://huggingface.co/datasets/roneneldan/TinyStories/tree/main">roneneldan/ TinyStories at main</a></li>
<li><a href="https://github.com/ggml-org/ggml/issues/441">Support for xPos positional embedding · Issue #441 · ggml-org/ggml</a></li>

</ul>
</details>

**标签**: `#positional encoding`, `#transformer`, `#machine learning`, `#NLP`, `#RoPE`

---

<a id="item-7"></a>
## [RubyLLM：面向主流 AI 提供商的统一 Ruby 框架](https://rubyllm.com/) ⭐️ 7.0/10

RubyLLM 是一个新的开源 Ruby 框架，为多个 AI 提供商（包括 OpenAI、Anthropic 以及通过 Ollama 运行的本地模型）提供统一接口。 RubyLLM 简化了 Ruby 开发者的 AI 集成，减少了样板代码并支持快速原型开发，类似于 Rails 简化 Web 开发的方式。 该框架支持聊天补全、流式传输和工具使用，但用户报告了某些提供商的缓存问题以及实现完整可观测性的困难。

hackernews · doener · 6月24日 14:41 · [社区讨论](https://news.ycombinator.com/item?id=48660711)

**背景**: Ruby 开发者之前需要为每个 AI 提供商使用单独的 SDK，导致代码重复和维护开销。RubyLLM 旨在通过跨提供商提供一致的 API 来解决这个问题，类似于 Python 的 aisuite 或 Vercel 的 AI SDK。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rubyllm.com/">RubyLLM | One beautiful Ruby framework for all major AI providers.</a></li>
<li><a href="https://github.com/crmne/ruby_llm">GitHub - crmne/ ruby _ llm : One delightful Ruby framework for every...</a></li>
<li><a href="https://medium.com/airtribe/rubyllm-and-the-return-of-rails-superpower-notes-from-euruko-2025-b72eeeb6b185">RubyLLM and the Return of Rails’ Superpower — Notes... | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区称赞 RubyLLM 易于使用且灵活，有人将其与 Vercel 的 AI 框架相提并论。但也有人担心缓存可靠性、缺乏对原生 responses API 的支持（尽管最近已添加），以及难以追踪 API 调用以实现可观测性。

**标签**: `#Ruby`, `#AI`, `#framework`, `#LLM`, `#open-source`

---

<a id="item-8"></a>
## [Bunny DNS 免费：最多支持 500 个域名](https://bunny.net/blog/were-making-bunny-dns-free/) ⭐️ 7.0/10

Bunny DNS 已取消所有 DNS 查询费用，现在为每个账户提供最多 500 个域名的免费 DNS 托管服务，包括智能记录和健康监控等功能。 此举使 Bunny DNS 成为 Cloudflare 的强大欧洲替代方案，在地缘政治变化的背景下满足了日益增长的欧洲云服务需求。 免费套餐包括无查询限制、无按请求计费，且关键功能不隐藏在企业计划之后。Bunny DNS 是 Bunny.net 的一部分，这是一家私营公司，仅在 2022 年进行过一轮 600 万美元的融资。

hackernews · dabinat · 6月24日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48657030)

**背景**: DNS（域名系统）托管将域名转换为 IP 地址。许多提供商按查询收费或提供有限的免费套餐。Cloudflare 是主导者，但总部位于美国，这引发了人们对 Bunny DNS 等欧洲替代方案的兴趣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bunny.net/dns/">Bunny DNS | The #1 Scriptable DNS Platform | bunny .net</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎此举，称赞 Bunny 是 Cloudflare 的竞争性欧洲替代方案。一些人担心流量激增可能导致意外收费，指出 Bunny 的计费保护仅适用于 CDN，而不适用于其他产品。

**标签**: `#DNS`, `#cloud`, `#EU tech`, `#free tier`, `#competition`

---

<a id="item-9"></a>
## [OpenAI 通过 Appia 基金会支持先进 AI 共享标准](https://openai.com/index/helping-build-shared-standards-for-advanced-ai) ⭐️ 7.0/10

OpenAI 宣布支持 Appia 基金会，该基金会是 Linux 基金会旗下联合开发基金会的一项倡议，旨在为先进 AI 建立共享标准，重点关注评估框架、安全实践和全球合作。 此举意义重大，因为它促进了 AI 开发中的全球合作与安全，有助于确保 AI 系统在整个供应链中满足一致的义务和期望，这对负责任的 AI 治理至关重要。 Appia 基金会旨在为 AI 价值链中的合规评估构建模块化开源规范，OpenAI 的参与将其在先进 AI 方面的专业知识用于帮助制定这些标准。

rss · OpenAI Blog · 6月23日 13:00

**背景**: Appia 基金会由 Linux 基金会旗下联合开发基金会发起，旨在为 AI 建立标准化合规规范。它专注于创建实用手段来评估 AI 系统是否满足消费者期望和义务。OpenAI 的支持增强了该倡议的分量，这是通过共享标准确保 AI 安全性和可靠性的更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://appiafoundation.org/">Appia Foundation</a></li>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-launches-appia-foundation-to-establish-standardized-conformity-specifications-across-the-ai-value-chain">Linux Foundation Launches Appia Foundation to Establish...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#AI governance`, `#OpenAI`, `#standards`, `#global cooperation`

---

<a id="item-10"></a>
## [MDN 浏览器兼容数据转为 SQLite 数据库](https://simonwillison.net/2026/Jun/24/browser-compat-db/#atom-everything) ⭐️ 7.0/10

Simon Willison 使用 Claude Code 和 Codex Desktop 生成的 AI 脚本，将 Mozilla 的 mdn/browser-compat-data 仓库转换为约 66MB 的 SQLite 数据库，并通过开放 CORS 头托管在 GitHub 上。 这使得 MDN 全面的浏览器兼容性数据易于查询和集成到 Web 应用中，降低了开发者检查跨浏览器功能支持的障碍。 该数据库通过 GitHub Actions 工作流构建，并强制推送到一个孤立分支，从而启用开放 CORS 头以便直接访问。可以使用 Datasette Lite 进行交互式探索。

rss · Simon Willison · 6月24日 23:59

**背景**: MDN 的 browser-compat-data 是一个大型 JSON 数据集，记录哪些 Web 功能在哪些浏览器版本中得到支持。SQLite 是一个轻量级的基于文件的数据库引擎。CORS 头控制 Web 浏览器中的跨域资源共享。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/">sqlite - utils</a></li>
<li><a href="https://bunny.net/academy/http/what-are-cross-origin-resource-sharing-cors-headers/">How do Cross Origin Resource Sharing ( CORS ) Headers work?</a></li>

</ul>
</details>

**标签**: `#browser compatibility`, `#SQLite`, `#developer tools`, `#MDN`, `#data engineering`

---

<a id="item-11"></a>
## [LLM 生成的求职申请抹去候选人身份](https://simonwillison.net/2026/Jun/24/tom-macwright/#atom-everything) ⭐️ 7.0/10

Tom MacWright 观察到，越来越多的求职申请和作品集由 LLM 共同撰写，使候选人变得千篇一律、缺乏个性，掩盖了他们的真实技能和身份。 这一趋势削弱了招聘流程，使雇主更难评估真实人才和匹配度，并迫使候选人迎合 AI 生成的规范，而非展示真实的自我。 MacWright 指出，LLM 生成的作品集链接到 LLM 生成的 GitHub 项目，提交信息也完全由 LLM 生成，没有留下候选人实际工作或个性的痕迹。

rss · Simon Willison · 6月24日 18:13

**背景**: 大型语言模型（LLM）如 GPT-4 可以生成文本、代码甚至整个项目。求职者开始使用这些工具自动化申请材料，但过度依赖可能产生缺乏个人风格和真实经验的内容，MacWright 将此现象称为“意外匿名”。

**标签**: `#AI`, `#careers`, `#LLM`, `#authenticity`, `#hiring`

---

<a id="item-12"></a>
## [Datasette 1.0a35 新增创建/修改表界面](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a35 引入了新的创建和修改表界面及 JSON API，用户可通过界面或 API 定义列、主键、约束等。同时新增了稳定的模板上下文文档，用于自定义模板。 此版本是 Datasette 1.0 的重要里程碑，大幅增强了数据库管理能力，使非技术用户更易使用。稳定的模板上下文文档确保自定义模板在未来版本中保持兼容。 创建表 API 支持列类型、NOT NULL、字面量/表达式默认值和单列外键。修改表 API 支持添加、重命名、重新排序和删除列，以及更改类型、默认值、约束、主键、外键和表名。

rss · Simon Willison · 6月23日 21:34

**背景**: Datasette 是一个用于探索和发布数据的开源工具，为 SQLite 数据库提供 Web 界面和 JSON API。在此版本之前，创建或修改表需要直接使用 SQL 命令或外部工具，限制了非开发者的可用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/stable/json_api.html">JSON API - Datasette documentation</a></li>
<li><a href="https://simonwillison.net/2026/jun/23/datasette/">Release: datasette 1.0a35 | Simon Willison’s Weblog</a></li>

</ul>
</details>

**标签**: `#datasette`, `#open-source`, `#data-exploration`, `#release`, `#JSON API`

---

<a id="item-13"></a>
## [欧洲反击美国芯片战限制](https://techcrunch.com/2026/06/24/europe-is-pushing-back-on-washingtons-chip-war/) ⭐️ 7.0/10

欧洲正在反击华盛顿的芯片战，ASML 首席执行官 Christophe Fouquet 表示，拟议的 MATCH 法案将限制已经出售给中国的上一代深紫外（DUV）光刻工具。 这很重要，因为它可能加剧贸易紧张局势，扰乱全球半导体供应链，不仅影响 ASML，也影响依赖芯片制造设备的整个科技行业。 MATCH 法案将在现有禁止极紫外（EUV）工具的基础上，将限制扩大到 ASML 的 DUV 浸没式机器，并禁止设备维护和零部件供应，从而堵住中国利用旧工具取得进展的漏洞。

rss · TechCrunch · 6月25日 00:08

**背景**: 美国一直在收紧对华先进半导体设备的出口管制，以遏制中国的技术进步。ASML 是一家关键的荷兰公司，主导着光刻市场，其较旧的 DUV 工具对于制造许多芯片仍然至关重要。MATCH 法案代表了芯片战的进一步升级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/24/europe-is-pushing-back-on-washingtons-chip-war/">Europe is pushing back on Washington's chip war | TechCrunch</a></li>
<li><a href="https://www.businesskorea.co.kr/news/articleView.html?idxno=271952">[Special Report] U.S. Pushes DUV Blockade to Widen Chip War with...</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/us-secures-netherlands-for-pax-silica-alliance-in-key-win-for-strategic-chip-alliance-tension-remains-over-match-act-restrictions">US Secures Netherlands for Pax Silica Alliance in... | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#geopolitics`, `#ASML`, `#chip war`, `#trade policy`

---

<a id="item-14"></a>
## [工程师岗位在 AI 冲击下最具韧性](https://techcrunch.com/2026/06/24/ai-was-supposed-to-kill-engineering-jobs-but-new-data-suggests-theyre-the-most-resilient/) ⭐️ 7.0/10

SignalFire 的新数据显示，在追踪超过 8000 万家公司的数百万员工后，发现工程是 2025 年最具韧性的岗位职能，尽管 AI 驱动的裁员广泛存在，工程师在新员工中的占比仍在增长。 这一发现挑战了 AI 将消灭工程岗位的普遍说法，反而表明对工程师的需求依然强劲。这对软件工程师、AI/ML 专业人士以及更广泛的科技行业具有重大意义，表明在 AI 驱动的经济中，工程技能正变得更加宝贵。 SignalFire 的分析追踪了超过 8000 万家公司的数百万员工的职业轨迹，提供了招聘趋势的全面视角。数据特别显示，即使在 AI 相关裁员成为头条新闻的情况下，工程仍是 2025 年最具韧性的岗位职能。

rss · TechCrunch · 6月24日 21:56

**背景**: 自 ChatGPT 等生成式 AI 工具兴起以来，人们普遍担心 AI 会取代软件工程师等技术岗位。然而，许多科技领袖仍在持续招聘工程师，OpenAI 和 Anthropic 等公司也宣布了大规模的 AI 开发工程招聘。SignalFire 的这一数据提供了实证，表明工程岗位并未消失，而是在演变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/24/ai-was-supposed-to-kill-engineering-jobs-but-new-data-suggests-theyre-the-most-resilient/">AI was supposed to kill engineering jobs , but new data ... | TechCrunch</a></li>
<li><a href="https://dropthe.org/tech/ai-impact-on-tech-hiring-2026-boom-pause-ax/">AI Impact on Tech Hiring 2026: Boom Pause Ax - DropThe</a></li>

</ul>
</details>

**标签**: `#AI`, `#software engineering`, `#job market`, `#data analysis`

---

<a id="item-15"></a>
## [谷歌再失两名顶尖 AI 研究员，转投 Anthropic](https://techcrunch.com/2026/06/24/ai-researchers-continue-to-leave-google-for-its-rivals/) ⭐️ 7.0/10

谷歌 DeepMind 的两名顶尖 AI 研究员 Jonas Adler 和 Alexander Pritzel 将离职加入竞争对手 Anthropic，此前已有 Noam Shazeer 和 John Jumper 等高知名度科学家离开。 人才流失标志着 AI 行业竞争格局的变化，可能削弱谷歌的地位，同时增强 Anthropic 作为主要 AI 参与者的实力。 Adler 和 Pritzel 分别对逆问题和 AlphaFold 做出贡献；他们的离职加剧了人才外流，可能影响谷歌 AI 研究的势头。

rss · TechCrunch · 6月24日 21:42

**背景**: 谷歌长期以来一直是 AI 研究的主导力量，但近几个月来，顶尖研究人员不断流向 Anthropic 等初创公司，后者专注于安全 AI。Anthropic 由前 OpenAI 员工创立，吸引了大量投资和人才，加剧了对 AI 专业人才的竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zerohedge.com/technology/google-loses-another-two-high-profile-ai-researchers-anthropic">Google Loses Another Two High Profile AI Researchers ... | ZeroHedge</a></li>
<li><a href="https://www.techmeme.com/260624/p35">Sources: Google AI researchers Jonas Adler and Alexander Pritzel ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#talent migration`, `#Google`, `#Anthropic`, `#industry trends`

---