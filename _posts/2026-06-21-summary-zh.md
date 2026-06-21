---
layout: default
title: "Horizon Summary: 2026-06-21 (ZH)"
date: 2026-06-21
lang: zh
---

> 从 50 条内容中筛选出 11 条重要资讯。

---

1. [诺贝尔奖得主 John Jumper 离开 DeepMind 加入 Anthropic](#item-1) ⭐️ 9.0/10
2. [《大西洋月刊》发布 AI 音乐训练数据可搜索数据库](#item-2) ⭐️ 8.0/10
3. [MCP 的关键价值：将认证流程隔离在智能体上下文之外](#item-3) ⭐️ 7.0/10
4. [VLC 创建者为机器人构建开源基础设施](#item-4) ⭐️ 7.0/10
5. [网络安全软件出口管制有着失败的历史](#item-5) ⭐️ 7.0/10
6. [美国质疑 ASML 芯片设备在华，ASML 否认](#item-6) ⭐️ 7.0/10
7. [Elastic 拟以最高 8500 万美元收购 Deductive AI](#item-7) ⭐️ 7.0/10
8. [NASA 选择 Relativity Space 执行 2028 年火星任务](#item-8) ⭐️ 7.0/10
9. [在 YouTube 上发布“构建你自己的 LLM”工作坊](#item-9) ⭐️ 7.0/10
10. [ML 博士生没有顶会论文能否毕业？](#item-10) ⭐️ 7.0/10
11. [DVD-JEPA：开源的最小 JEPA 世界模型](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [诺贝尔奖得主 John Jumper 离开 DeepMind 加入 Anthropic](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/) ⭐️ 9.0/10

诺贝尔奖得主、AlphaFold 关键人物 John Jumper 已离开 Google DeepMind，加入竞争对手 AI 公司 Anthropic。 此举标志着 AI 行业的一次重大人才流动，可能加速 Anthropic 的研究进展，同时削弱 DeepMind 在蛋白质折叠和科学 AI 领域的领导地位。 Jumper 并非近期唯一离开 DeepMind 的知名人物，这表明顶尖人才向竞争实验室流动的广泛趋势。

rss · TechCrunch · 6月20日 16:39

**背景**: John Jumper 领导了 AlphaFold 的开发，这是一个高精度预测蛋白质结构的 AI 系统，并因此获得诺贝尔化学奖。DeepMind 作为 Google 子公司一直是 AI 研究的领导者，而 Anthropic 则专注于安全与伦理的 AI 开发。

**标签**: `#AI`, `#DeepMind`, `#Anthropic`, `#talent`, `#industry news`

---

<a id="item-2"></a>
## [《大西洋月刊》发布 AI 音乐训练数据可搜索数据库](https://www.theverge.com/ai-artificial-intelligence/953183/the-atlantic-searchable-database-music-ai-training-data) ⭐️ 8.0/10

《大西洋月刊》记者 Alex Reisner 发现了四个用于训练 AI 模型的音乐数据集，总计约 2120 万首曲目，并将其公开可搜索。最大的数据集包含 1200 万首曲目，第二个包含 900 万首。 这种前所未有的透明度揭示了 AI 训练数据集中受版权保护材料的巨大规模，使得对版权和伦理问题的审查成为可能。它为研究人员、艺术家和公众提供了一个关键工具，以了解哪些音乐驱动了生成式 AI 系统。 其中两个数据集非常庞大（1200 万和 900 万首曲目），另外两个较小但仍有意义，各包含约 10 万首曲目。该数据库完全可搜索，允许用户查找特定歌曲或艺术家。

rss · The Verge · 6月20日 18:46

**背景**: 生成式 AI 音乐模型（如 Suno 和 Google 的模型）通过大量音频集合进行训练，以学习模式并生成新音乐。所使用的数据集通常未经明确许可从互联网抓取，引发了版权担忧。这项调查为不透明的 AI 训练数据世界带来了急需的透明度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/953183/the-atlantic-searchable-database-music-ai-training-data">The Atlantic created a searchable database of the music used to train AI | The Verge</a></li>
<li><a href="https://hypebeast.com/2026/6/ai-music-datasets-exposed-in-suno-copyright-clash">AI Music Datasets and Suno Copyright Clash Explained | Hypebeast</a></li>
<li><a href="https://www.theatlantic.com/technology/2026/06/ai-music-generators-suno-google-udio/687485/">The Millions of Songs Mashed Into AI -Generated Music - The Atlantic</a></li>

</ul>
</details>

**标签**: `#AI`, `#music`, `#training data`, `#copyright`, `#transparency`

---

<a id="item-3"></a>
## [MCP 的关键价值：将认证流程隔离在智能体上下文之外](https://simonwillison.net/2026/Jun/19/sean-lynch/#atom-everything) ⭐️ 7.0/10

Sean Lynch 提出，模型上下文协议（MCP）的主要价值在于将认证流程隔离在智能体的上下文窗口之外，甚至可能完全脱离执行框架。他认为 MCP 的理想形态可能只是一个 API 的认证网关。 这一见解将 MCP 的角色从通用的数据连接协议重新定位为安全聚焦的层，这可以简化智能体架构并减少攻击面。它突出了一个实际好处，可能推动 MCP 在生产级 AI 系统中的更广泛采用。 Lynch 将 MCP 与传统技能/CLI 方法进行对比，认为认证隔离才是真正的差异化优势。他指出，即使 MCP 除了作为认证网关之外什么都不做，它仍然是一个胜利。

rss · Simon Willison · 6月19日 22:45

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月宣布的一个开放标准，用于连接 AI 应用与外部数据源和工具。它提供了读取文件、执行函数和处理上下文提示的标准化接口，已被 OpenAI 和 Google DeepMind 等主要 AI 提供商采用。在智能体系统中，安全管理认证具有挑战性，因为凭证通常位于智能体的上下文窗口内，从而产生安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#model-context-protocol`, `#llms`, `#ai`, `#authentication`, `#agent`

---

<a id="item-4"></a>
## [VLC 创建者为机器人构建开源基础设施](https://techcrunch.com/2026/06/19/he-made-your-free-video-player-run-smoothly-now-hes-doing-that-for-robots/) ⭐️ 7.0/10

VLC 媒体播放器的主要开发者 Jean-Baptiste Kempf 正在构建 Kyber，这是一个用于实时控制机器人、无人机等远程设备的开源基础设施层。 该项目可能使实时远程设备控制大众化，让开发者和公司能够在开源基础上构建可扩展的机器人和物联网应用，类似于 VLC 对媒体播放的变革。 Kyber 旨在提供人类或 AI 代理与远程硬件之间的低延迟、可靠通信，解决全球范围内的网络抖动和同步等挑战。

rss · TechCrunch · 6月20日 00:47

**背景**: Jean-Baptiste Kempf 以领导 VLC 而闻名，这是一款开源媒体播放器，下载量超过 60 亿次。他拥有数十年的开源开发经验，并创立了多家公司。Kyber 代表他进军机器人基础设施领域，利用其在实时系统方面的专业知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://jbkempf.com/">Jean-Baptiste Kempf — VLC, VideoLAN, Kyber & Open Source</a></li>
<li><a href="https://github.com/jbkempf">jbkempf (Jean-Baptiste Kempf) · GitHub Top Stories The VLC Creator Is Now Building Open Source Infrastructure ... VLC Developer Kyber Startup $5 M Lightspeed Robotics Drones VLC Player - Jean-Baptiste Kempf, 20 Years of Open Source ... VLC Player - Jean-Baptiste Kempf, 20 Years of Open Source ...</a></li>
<li><a href="https://europeanpurpose.com/news/the-vlc-creator-is-now-building-open-source-infrastructure-for-robots-and-drones">The VLC Creator Is Now Building Open Source Infrastructure ...</a></li>

</ul>
</details>

**标签**: `#open-source`, `#robotics`, `#real-time`, `#infrastructure`, `#IoT`

---

<a id="item-5"></a>
## [网络安全软件出口管制有着失败的历史](https://techcrunch.com/2026/06/19/encryption-spyware-and-now-mythos-history-shows-why-cyber-export-control-doesnt-work/) ⭐️ 7.0/10

一篇 TechCrunch 文章指出，对网络安全软件的出口管制在历史上一直失败，以 1990 年代的 PGP 为例，并质疑将其应用于 Anthropic 未发布的 AI 模型 Mythos。 这很重要，因为各国政府正在考虑对像 Mythos 这样的先进 AI 模型实施出口管制，但历史表明这些措施无效，可能阻碍创新而无法阻止坚定的对手。 文章强调了美国政府 1990 年代控制 PGP 加密的失败尝试，尽管有管制，PGP 仍传播到全球。文章将其与当前关于监管 Anthropic 强大的网络安全 AI 模型 Mythos 的辩论相类比。

rss · TechCrunch · 6月19日 22:40

**背景**: 出口管制是政府出于国家安全等原因对向其他国家转让某些技术的限制。PGP（Pretty Good Privacy）是一种加密程序，成为 1990 年代加密出口管制斗争的象征。Anthropic 的 Mythos 是一个未发布的 AI 模型，该公司声称其过于危险而不能公开发布，引发了全球关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/19/encryption-spyware-and-now-mythos-history-shows-why-cyber-export-control-doesnt-work/">From PGP to Mythos: a brief history of export controls that didn't stop anyone | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States">Export of cryptography from the United States - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/what-is-mythos-and-why-are-experts-worried-about-anthropics-ai-model/">What is Mythos, Anthropic’s unreleased AI model, and how ...</a></li>

</ul>
</details>

**标签**: `#export controls`, `#cybersecurity`, `#AI regulation`, `#encryption`, `#Anthropic`

---

<a id="item-6"></a>
## [美国质疑 ASML 芯片设备在华，ASML 否认](https://techcrunch.com/2026/06/19/the-us-says-asmls-top-chip-tool-may-be-in-china-asml-says-it-isnt/) ⭐️ 7.0/10

美国政府质疑 ASML 最先进的芯片制造设备可能在中国运行，但 ASML 否认这一说法，称从未向中国客户出售过此类设备。 这一争议凸显了半导体出口管制中的持续紧张局势，美国试图阻止中国获取可能增强其军事和人工智能能力的尖端芯片技术。 ASML 的极紫外（EUV）光刻系统是制造最先进芯片所必需的，但由于美国主导的出口限制，从未出口到中国。TWINSCAN NXE:3400B 就是此类高端系统之一。

rss · TechCrunch · 6月19日 07:59

**背景**: ASML 是一家荷兰公司，主导着用于将芯片设计打印到硅晶圆上的光刻机市场。自 2018 年以来，美国加强了出口管制，限制中国获取包括 EUV 设备在内的先进半导体技术，这些设备使用了美国原产的组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/china-vexed-at-expansion-of-asml-chip-tool-export-controls-reveals-ministry-statement">China vexed at expansion of ASML chip tool export ... | Tom's Hardware</a></li>
<li><a href="https://www.silicon.co.uk/workspace/asml-china-revoke-544240">ASML Chip System Export Licence For China Partially Revoked</a></li>
<li><a href="https://www.congress.gov/crs-product/R48642">U.S. Export Controls and China: Advanced Semiconductors</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#geopolitics`, `#export controls`, `#ASML`, `#chip manufacturing`

---

<a id="item-7"></a>
## [Elastic 拟以最高 8500 万美元收购 Deductive AI](https://techcrunch.com/2026/06/18/source-elastic-agrees-to-buy-crv-backed-deductiveai-for-up-to-85m/) ⭐️ 7.0/10

Elastic 已同意以最高 8500 万美元收购 Deductive AI，这家初创公司利用 AI 自动检测并修复软件缺陷。 此次收购表明，AI 原生运维工具正成为可观测性平台的核心基础设施，并验证了自主故障修复的市场价值。 Deductive AI 成立于三年前，在收购前不到一年从 CRV 获得了 750 万美元的种子轮融资。

rss · TechCrunch · 6月19日 00:51

**背景**: Elastic 是一家上市公司，以其 Elasticsearch 搜索和分析引擎闻名。Deductive AI 的技术利用人工智能自动检测并修复软件缺陷，充当快速迭代团队的 AI 站点可靠性工程师（SRE）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/18/source-elastic-agrees-to-buy-crv-backed-deductiveai-for-up-to-85m/">Source: Elastic agrees to buy CRV-backed Deductive AI for up ...</a></li>
<li><a href="https://startupfortune.com/elastics-85-million-bet-on-deductiveai-is-a-signal-that-ai-native-ops-tooling-is-now-acquisition-currency/">Elastic's $85 million bet on DeductiveAI is a signal that AI ...</a></li>
<li><a href="https://creati.ai/ai-news/2026-06-20/elastic-acquires-deductive-ai-85m/">Elastic Acquires AI Bug-Detection Startup Deductive AI for Up ...</a></li>

</ul>
</details>

**标签**: `#acquisition`, `#AI`, `#software engineering`, `#bug detection`, `#Elastic`

---

<a id="item-8"></a>
## [NASA 选择 Relativity Space 执行 2028 年火星任务](https://www.theverge.com/science/952988/nasa-relativity-space-eric-schmidt-mars) ⭐️ 7.0/10

NASA 已选择由前谷歌 CEO Eric Schmidt 领导的 Relativity Space，在新型公私合作模式下，于 2028 年将 Aeolus 载荷发射至火星。 这标志着 NASA 在深空探索中向利用私营公司的重要转变，可能降低成本并加速火星科学研究，同时也凸显了 Relativity Space 在 NASA 行星任务中日益增长的作用。 Relativity Space 将提供航天器、火箭和巡航操作，而 NASA 提供 Aeolus 仪器套件，用于测量火星上的风、水冰云和温度。该任务计划于 2028 年执行。

rss · The Verge · 6月19日 18:41

**背景**: Relativity Space 是一家美国航空航天公司，以使用 3D 打印制造火箭而闻名，包括正在开发的 Terran R。Aeolus 任务旨在提供首个关于火星风场和气候的全球、季节性和昼夜数据，建立在数十年火星探索的基础上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nasa.gov/news-release/nasa-announces-public-private-partnership-to-advance-mars-science/">NASA Announces Public-Private Partnership to Advance Mars Science - NASA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relativity_Space">Relativity Space</a></li>
<li><a href="https://ntrs.nasa.gov/citations/20200000616">The Aeolus Mission Concept, an Innovative Mission to Study the Winds and Climate of Mars - NASA Technical Reports Server (NTRS)</a></li>

</ul>
</details>

**标签**: `#NASA`, `#Mars mission`, `#public-private partnership`, `#space exploration`, `#Relativity Space`

---

<a id="item-9"></a>
## [在 YouTube 上发布“构建你自己的 LLM”工作坊](https://www.reddit.com/r/MachineLearning/comments/1uazlnd/hi_reddit_i_posted_my_build_your_own_llm_workshop/) ⭐️ 7.0/10

Justin Angel 在 YouTube 上发布了一个免费工作坊视频，从头教授如何构建大型语言模型，涵盖机器学习基础、Transformer 架构和训练，无需数学先修知识。 该资源降低了初学者理解和构建 LLM 的门槛，填补了快速发展的 AI 领域中易于获取、以代码为先的教育内容的空白。 工作坊包含幻灯片、基于 Excel 的数学直觉练习以及 PyTorch 编码示例，涵盖 SwiGLU、Kaiming 初始化、RMSNorm 和指令微调等主题。

reddit · r/MachineLearning · /u/JustinAngel · 6月20日 15:36

**背景**: 构建 LLM 通常需要理解深度学习、Transformer 和训练技术。该工作坊旨在不假设先修数学或 ML 知识的情况下教授这些概念，通过代码和 Excel 建立直觉。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://abdulkaderhelwan.medium.com/swiglu-activation-function-77627e0b2b52">SwiGLU Activation Function . SwiGLU (Swish-Gated Linear... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Weight_initialization">Weight initialization - Wikipedia</a></li>
<li><a href="https://machinelearningmastery.com/layernorm-and-rms-norm-in-transformer-models/">LayerNorm and RMS Norm in Transformer Models ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Machine Learning`, `#Tutorial`, `#Deep Learning`, `#Transformers`

---

<a id="item-10"></a>
## [ML 博士生没有顶会论文能否毕业？](https://www.reddit.com/r/MachineLearning/comments/1uazlhg/would_you_let_an_ml_phd_student_graduate_without/) ⭐️ 7.0/10

Reddit 上的一场讨论提出，一个 ML 博士生虽然工作扎实，但没有在 NeurIPS、ICML、ICLR、CVPR 等顶级会议上发表论文，是否应该允许其毕业，引发了关于发表文化的辩论。 这场辩论凸显了 ML 学术界中发表指标与真实研究质量之间的张力，可能影响毕业政策与学生福祉。 该学生有三篇第一作者的 A 级论文和连贯的论文方向，但缺乏在 NeurIPS、ICML、ICLR 或 CVPR 等 A* ML 会议上的发表记录。

reddit · r/MachineLearning · /u/Hope999991 · 6月20日 15:36

**背景**: 在机器学习领域，顶级会议（如 NeurIPS、ICML、ICLR、CVPR）竞争激烈，通常被视为学术职业发展的关键。许多博士项目明确或隐含地要求此类发表才能毕业。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alexhernandezgarcia.com/resources/publication-venues-ml.html">Publication venues in machine learning and related fields</a></li>
<li><a href="https://algoverseairesearch.org/blog/icml-iclr-aaai-student-guide">Beyond NeurIPS: A Student's Guide to ICML, ICLR, AAAI, and ...</a></li>
<li><a href="https://icml.cc/public/JournalToConference">The NeurIPS/ICLR/ICML Journal-to-Conference Track</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区意见分歧：一些人认为扎实的工作和 A 级论文应足以毕业，而另一些人坚持认为顶级发表对于展示影响力和严谨性至关重要。

**标签**: `#machine learning`, `#PhD`, `#publication culture`, `#academia`, `#graduation standards`

---

<a id="item-11"></a>
## [DVD-JEPA：开源的最小 JEPA 世界模型](https://www.reddit.com/r/MachineLearning/comments/1uatlzx/dvdjepa_an_opensource_fullyreproducible_jepa/) ⭐️ 7.0/10

DVD-JEPA 是一个开源、完全可复现的联合嵌入预测架构（JEPA）实现，它学习预测在 16×16 网格中弹跳的 DVD 标志的表示，并通过线性探针实现了精确的位置恢复。 这项工作提供了 JEPA 概念的最小且诚实的演示，表明预测表示而非像素可以产生有用的世界模型，并且它完全在浏览器中运行，便于教育和实验。 该模型使用上下文编码器、EMA 目标编码器和潜在预测器，无需标签或解码器进行训练；线性探针可将标志的精确(y,x)位置恢复到 0.73 像素以内，预测器可以“梦想”正确的未来帧约 20 步，之后出现潜在漂移。

reddit · r/MachineLearning · /u/NielsRogge · 6月20日 10:52

**背景**: JEPA（联合嵌入预测架构）是 Yann LeCun 在 2022 年提出的一种自监督学习方法，它预测抽象嵌入（潜在表示）而非像素级重建。传统的视频预测模型常常难以处理不可预测的像素级细节，而 JEPA 在编码器中丢弃不可预测的信息。线性探针是一种附加在冻结表示上的简单线性分类器，用于评估其语义内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Joint_Embedding_Predictive_Architecture">Joint Embedding Predictive Architecture</a></li>
<li><a href="https://www.emergentmind.com/topics/linear-probes">Linear Probes: Neural Network Diagnostics</a></li>

</ul>
</details>

**社区讨论**: 输入中未提供社区讨论内容。

**标签**: `#world models`, `#JEPA`, `#representation learning`, `#self-supervised learning`, `#video prediction`

---