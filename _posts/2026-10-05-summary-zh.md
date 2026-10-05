---
layout: default
title: "Horizon Summary: 2026-10-05 (ZH)"
date: 2026-10-05
lang: zh
---

> 从 49 条内容中筛选出 9 条重要资讯。

---

1. [Strata 在 RTX 4090 上以每秒 100 tokens 运行 125B Qwen 3.8 Flash Next](#item-1) ⭐️ 8.0/10
2. [ARC-AGI-3 在 Kaggle 上的最高分 30 天内从 7% 跃升至 56%](#item-2) ⭐️ 8.0/10
3. [GitHub 工具可从 macOS 27 移除 Apple Intelligence 并回收磁盘空间](#item-3) ⭐️ 7.0/10
4. [Simon Willison 呼吁按用量付费服务默认设置硬性预算上限](#item-4) ⭐️ 7.0/10
5. [谷歌因 AI 提交激增暂停开源漏洞赏金计划](#item-5) ⭐️ 7.0/10
6. [特朗普宣布成立新的“超级智能部队”AI 特别工作组](#item-6) ⭐️ 7.0/10
7. [联邦法官称 Flock 为“无差别大规模监控”](#item-7) ⭐️ 7.0/10
8. [OpenAI 安全员工 David Robinson 辞职，称公司文化已崩坏](#item-8) ⭐️ 7.0/10
9. [杰克·多西的 Bitchat 因政府命令从印度应用商店下架](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Strata 在 RTX 4090 上以每秒 100 tokens 运行 125B Qwen 3.8 Flash Next](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

一个名为 Strata 的 GitHub 项目能够在消费级 RTX 4090 显卡上以约每秒 100 个 token 的速度运行 125B 参数的 Qwen 3.8 Flash Next 模型，有用户报告在配备 128GB DDR5 和 Ryzen 7950x3d 的 4090 上达到每秒 124 个 token。该项目引发了关于量化质量的争论，因为一项社区基准测试发现，在相同 GGUF 权重下，Strata 的视觉准确率相比 llama.cpp 明显下降。 这表明 125B 级别的大型模型如今可以在消费级硬件上以交互速度运行，有可能让前沿规模的人工智能无需昂贵的云端 GPU 即可普及。它也凸显了为追求速度而进行激进量化与由此导致的质量下降之间日益紧张的关系，这对任何为精度敏感任务部署本地 LLM 的人都至关重要。 Qwen 3.8 Flash Next 总参数量为 125B，但每个 token 仅激活 6B，外加 51B 的 n-gram 嵌入和 4B 的 MTP，这解释了它为何能在消费级硬件上运行。一项社区基准测试显示，在 50 张图像的视觉坐标任务中，Strata 的中位误差为 154.8 像素，而相同权重下 llama.cpp 仅为 46.5 像素；持怀疑态度者警告，低于 4-bit 的量化可能导致显著的质量下降。

hackernews · snehesht · 10月4日 12:51 · [社区讨论](https://news.ycombinator.com/item?id=49953495)

**背景**: Qwen 3.8 Flash Next 是阿里巴巴 Qwen 系列的大型语言模型，采用类似混合专家的架构，每个 token 仅激活其 125B 参数中的一小部分，以保持推理效率。量化会降低模型权重的数值精度（例如从 16 位浮点数降至 4 位整数），以缩小内存占用并加速推理，但可能损害输出质量。Strata 是专为该模型构建的专用推理运行时，而 llama.cpp 是广泛使用的通用 LLM 推理引擎，常被用作性能和质量基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/qwenlm/qwen3.8-flash-next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>
<li><a href="https://www.youtube.com/watch?v=m0VHx73SAG0">The New Way to Run 125 B Models 6× Faster Than... - YouTube</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一：一些用户报告了令人惊喜的良好结果（4090 上每秒 124 个 token，RTX 6000 Pro 上解码每秒 255 个 token），而另一些人则对低于 4-bit 的量化持怀疑态度，并给出基准测试显示在相同权重下 Strata 的视觉准确率远逊于 llama.cpp。一位评论者指出 Strata 链接正在各大 LLM 论坛被刷屏，并质疑这种热度在蜜月期过后还能剩下多少。

**标签**: `#LLM inference`, `#quantization`, `#consumer hardware`, `#Qwen`, `#performance benchmarking`

---

<a id="item-2"></a>
## [ARC-AGI-3 在 Kaggle 上的最高分 30 天内从 7% 跃升至 56%](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

在过去 30 天里，Kaggle 上 ARC-AGI-3 基准测试的最高分从约 7% 跃升至 56%，这一成绩由运行在智能体框架（harness）中的小型本地模型取得。这一涨幅超过了平均人类水平，而该基准测试原本正是为了凸显人类在抽象与推理方面的优势而设计的。 这一快速进展挑战了“当前 AI 距离 ARC-AGI-3 还很遥远”的假设，并表明在交互式推理任务中，智能体框架的设计可能比单纯的模型规模更重要。它可能改变研究者、竞赛组织者以及公众对“人类水平抽象能力”和 AGI 时间线的解读方式。 Kaggle 的规则限制参赛者只能使用小型本地模型，因此 56% 这一数字反映的是框架工程带来的提升，而非借助前沿云端大规模系统。该基准测试本身是交互式的，要求智能体探索新环境、即时获取目标并构建可适应的世界模型；帖子中引用的排行榜图片也被指出略有滞后。

reddit · r/MachineLearning · /u/we_are_mammals · 10月4日 10:24 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**背景**: ARC-AGI-3 是 ARC Prize 推出的“抽象与推理语料库”基准测试的第三代版本，属于交互式推理基准，要求 AI 智能体探索新环境、即时推断目标并持续学习，而不是解决静态谜题。早期的 ARC-AGI 版本使用静态网格任务，而前沿模型在交互式版本上的历史得分一直停留在个位数。Kaggle 承办 ARC Prize 竞赛，参赛者只能使用小型本地模型，因此框架设计成为挑战的核心部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://benchlm.ai/benchmarks/arcAgi3">ARC - AGI - 3 Leaderboard & Scores — July 2026 | BenchLM.ai</a></li>
<li><a href="https://www.vietanh.dev/blog/2026-06-15-plan-once-then-act-small-model-agents">Plan Once, Then Act: When the ReAct Loop Is the Wrong Harness for...</a></li>

</ul>
</details>

**社区讨论**: 该 Reddit 帖子询问社区如何看待这一跃升，并将其描述为小型本地模型在框架加持下，在一个本应展示人类优越性的基准上击败了平均人类。评论者很可能会争论这一结果究竟反映了真正的抽象能力进步，还是针对该基准的框架调优，以及它对 AGI 主张意味着什么。

**标签**: `#ARC-AGI`, `#AGI`, `#benchmark`, `#machine learning`, `#Kaggle`

---

<a id="item-3"></a>
## [GitHub 工具可从 macOS 27 移除 Apple Intelligence 并回收磁盘空间](https://github.com/omlahore/RemoveMacAI) ⭐️ 7.0/10

一个名为 RemoveMacAI 的 GitHub 项目提供了脚本，用于从 macOS 27 Golden Gate 中移除 Apple Intelligence；在该系统中，AI 功能不再是可选项，据称占用约 27 GB 磁盘空间。该工具引发了大量关注，获得 361 分和 222 条评论，讨论涉及系统臃肿、隐私和用户控制权。 这反映出用户对 AI 功能被强制塞入操作系统、且缺乏简单关闭开关的做法日益不满，与长期以来 Windows 上的“去臃肿”文化相呼应。它表明，即便是曾以干净默认设置著称的苹果，如今也面临用户要求控制本地 AI 模型和存储空间的压力。 根据社区报告，macOS 27 中的 Apple Intelligence 无法通过常规设置禁用，其磁盘占用约为 27 GB，但该工具的具体移除方式及潜在副作用在现有内容中未详细说明。项目托管于 github.com/omlahore/RemoveMacAI。

hackernews · privacyisntdead · 10月4日 19:42 · [社区讨论](https://news.ycombinator.com/item?id=49957116)

**背景**: Apple Intelligence 是苹果在其操作系统中推出的一套端侧与云端协同的 AI 功能，包括升级版 Siri。在 Sequoia 和 Tahoe 等较早的 macOS 版本中，用户可以将其关闭，但 macOS 27 Golden Gate 将其变为强制功能，并随系统捆绑本地推理模型。这引发了与 Windows 臃肿软件以及 O&O ShutUp10 等移除组件的工具的类比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://me.pcmag.com/en/macos/38213/is-apple-intelligence-stealing-your-macs-storage-heres-how-to-turn-it-off">Is Apple Intelligence Stealing Your Mac's Storage? Here's How to...</a></li>
<li><a href="https://upstract.com/x/58b113ecdf1fea32">Apple's macOS 27 installs a lot of AI bloatware</a></li>

</ul>
</details>

**社区讨论**: 评论者将这一情况与 Windows 的去臃肿相提并论，有人对 iOS 不再提供简单的 AI 开关感到沮丧，而微软和 Firefox 等竞争对手却提供了全局开关。也有人为捆绑的本地模型辩护，认为它们体积小、不依赖云端，足以完成基本任务；还有人质疑苹果如何权衡磁盘占用成本与用户反弹。

**标签**: `#macOS`, `#Apple Intelligence`, `#privacy`, `#system optimization`, `#bloatware`

---

<a id="item-4"></a>
## [Simon Willison 呼吁按用量付费服务默认设置硬性预算上限](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) ⭐️ 7.0/10

Simon Willison 发表博文，主张按用量付费的服务和 API 应默认提供硬性预算上限，一旦达到消费限额就切断服务并返回错误，而不是仅仅发送警告邮件。他指出 AWS 已于 2026 年 9 月推出月度支出限额，Google Cloud 也在 7 月推出了 Spend Caps，表明行业正开始朝这个方向发展。 随着 AI 编程代理和个人代理让启动消耗付费 API、存储和计算资源的服务变得极其容易，失控成本已成为真实风险——一个被广泛报道的案例中，两个 AI 代理循环运行 11 天，账单高达 4.7 万美元。默认硬性上限可以保护个人和企业免遭灾难性的意外账单，并可能改变开发者选择云服务商的方式。 Willison 坚持上限必须是硬性的而非软性的，并提出一个需主动勾选的复选框，明确取消上限并由用户自行承担后续费用。他指出 AWS 的新支出限额在达到后会暂停项目一个月，但该功能目前仍只向有限数量的客户开放，尚未全面可用。

rss · Simon Willison · 10月3日 23:34

**背景**: 按用量付费的云服务和 API 根据消费量向客户计费，这意味着配置错误或失控的程序可能产生无限费用。传统上，服务商只提供软性上限——预算提醒和警告邮件——而实际支出并未受到限制。相比之下，硬性上限会在达到设定金额时自动停止或暂停工作负载，起到真正的天花板作用，而不仅仅是通知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/">We’re going to need default hard budget caps on pretty much...</a></li>
<li><a href="https://academy.codearia.com/en/articles/hard-spend-limits-aws-google-cloud-openai-anthropic">Hard spend limits: AWS, Google Cloud, OpenAI, Vercel</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#API design`, `#cost management`, `#cloud billing`, `#developer tools`

---

<a id="item-5"></a>
## [谷歌因 AI 提交激增暂停开源漏洞赏金计划](https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/) ⭐️ 7.0/10

谷歌已将其开源软件漏洞奖励计划（OSS VRP）暂停至明年，理由是 AI 生成的提交数量“大幅上升”，导致审核流程不堪重负。该计划原本向发现谷歌开源项目漏洞的研究人员支付报酬，但因大量低质量 AI 生成报告涌入，审核工作已难以为继。 这是一个值得关注的行业动态，表明 AI 垃圾内容正成为安全研究和开源维护的系统性问题。它释放出一个信号：随着生成式 AI 让批量生产看似合理但无用的报告变得廉价，作为发现漏洞关键机制的漏洞赏金计划，可能需要从根本上重新思考其提交与审核流程。 此次冻结是临时性的，谷歌计划明年恢复该计划，但尚未公布具体日期或修订后的流程。OSS VRP 的设立初衷是奖励发现谷歌开源项目漏洞的研究人员，而类似的 AI 提交洪流已迫使苹果等其他漏洞赏金计划限制或收紧报告提交。

rss · TechCrunch · 10月4日 20:31

**背景**: 漏洞赏金计划是指组织向报告安全漏洞（尤其是软件漏洞）的个人支付报酬的安排。谷歌的 OSS VRP 专门针对其开源项目中的缺陷，这些项目被广泛使用，但往往由小团队维护。AI 垃圾内容（AI slop）指由 AI 生成的大量低质量内容，在此语境下指那些看似是合法漏洞发现、但缺乏真实安全影响的自动化报告。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/">AI slop seems to be overwhelming bug bounty programs .</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bug_bounty_program">Bug bounty program - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 网络安全专家去年就已警告 AI 垃圾内容对漏洞赏金计划构成严重风险，cURL 项目此前也因同样原因关闭了自己的漏洞赏金计划。总体看法是，这对安全审核团队而言是一场日益严重且可预见的危机，各方对成因几乎没有分歧。

**标签**: `#bug-bounty`, `#open-source`, `#AI`, `#security`, `#Google`

---

<a id="item-6"></a>
## [特朗普宣布成立新的“超级智能部队”AI 特别工作组](https://techcrunch.com/2026/10/04/trump-unveils-his-new-super-intelligence-force/) ⭐️ 7.0/10

美国总统唐纳德·特朗普在 Truth Social 上宣布成立新的“超级智能部队”（SIF），由国家情报总监杰伊·克莱顿领导，联邦贸易委员会主席安德鲁·弗格森等官员担任高级职务。该特别工作组被要求在 120 天内就人工智能的风险与机遇提交报告。 这是一项重大政治进展，将直接影响美国联邦政府与 AI 企业、消费者及利益团体互动的方式，并处于当前 AI 安全辩论的核心。该工作组的结论可能影响未来的 AI 监管和政策方向，从而波及整个 AI/ML 生态系统。 根据特朗普在 Truth Social 上的帖子，SIF 将协调联邦政府与消费者、公共利益团体、宗教组织、关键基础设施提供商以及“超级智能公司”的接触。该工作组包括杰伊·克莱顿、安德鲁·弗格森等官员，并须在 120 天内提交风险与机遇报告。

rss · TechCrunch · 10月4日 15:15

**背景**: “超级智能部队”是特朗普政府对日益激烈的 AI 安全辩论——即是否以及如何监管先进 AI——的最新回应。AI 安全辩论涉及多个派别，对风险的看法各不相同，从近期危害到推测性的 AGI 担忧均有涉及。通过让情报和贸易官员牵头，该工作组释放出同时关注 AI 的国家安全与商业影响的信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/news/story/white-house-announces-new-ai-super-intelligence-force-9444010/">White House announces new AI ' Super Intelligence Force ' | LinkedIn</a></li>
<li><a href="https://sputnikglobe.com/20261004/trump-announces-formation-of-super-intelligence-force-1124833877.html">Trump Announces Formation of Super Intelligence Force</a></li>
<li><a href="https://www.nbcnews.com/politics/trump-administration/trump-announces-members-ai-task-force-rcna601494">Trump announces members of ‘ Super Intelligence Force ’ to...</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#AI safety`, `#government`, `#regulation`, `#Trump administration`

---

<a id="item-7"></a>
## [联邦法官称 Flock 为“无差别大规模监控”](https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/) ⭐️ 7.0/10

一名联邦法官裁定，一名治安官副手在未取得搜查令的情况下使用 Flock Safety 的车牌识别系统搜索一名女子的车牌，侵犯了她的第四修正案权利，并将这种做法称为“无差别大规模监控”。 这一裁决可能为限制执法部门无证使用自动车牌识别系统树立先例，影响全国警察部门部署监控技术的方式，并引发关于隐私和公民自由的更广泛问题。 该裁决专门针对 Flock Safety，这是美国最大的自动车牌识别供应商之一，安装了约 12 万台摄像头，并认定在没有搜查令的情况下搜索其数据库构成第四修正案下的不合理搜查。

rss · TechCrunch · 10月3日 19:33

**背景**: Flock Safety 是一家在美国部署人工智能驱动的自动车牌识别（ALPR）摄像头的公司，自动扫描车牌并记录车辆的时间、位置和详细信息。美国宪法第四修正案保护人们免受不合理搜查和扣押，通常要求执法部门基于合理根据取得搜查令。本案检验的是无证查询聚合的 ALPR 数据是否违反这一保护。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.governing.com/management-and-administration/americas-surveillance-problem-is-much-bigger-than-flock">America’s Surveillance Problem Is Much Bigger than Flock</a></li>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers...</a></li>
<li><a href="https://www.findlaw.com/criminal/criminal-rights/the-fourth-amendment-warrant-requirement.html">The Fourth Amendment Warrant Requirement - FindLaw</a></li>

</ul>
</details>

**标签**: `#surveillance`, `#privacy`, `#fourth-amendment`, `#license-plate-recognition`, `#law-enforcement`

---

<a id="item-8"></a>
## [OpenAI 安全员工 David Robinson 辞职，称公司文化已崩坏](https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/) ⭐️ 7.0/10

在 OpenAI 工作三年半、负责主导撰写重大产品发布配套安全报告的 David Robinson 已辞职，并于 2026 年 10 月 3 日在《大西洋月刊》发表题为《我因 OpenAI 文化崩坏而辞职》的文章。他警告称，AI 安全领域试错的时代已经结束，问题比具体规则或新法律更为深层。 此次辞职为关于领先 AI 实验室是否将速度置于安全之上的争论增添了一个重要的内部声音，并可能在各国监管机构制定 AI 监督框架之际加剧对 OpenAI 治理的审视。此前已有多位安全领域知名人士离职以及 OpenAI 专门安全团队被解散，这表明此事更像一种模式而非孤立事件。 Robinson 负责主导撰写 OpenAI 重大产品发布配套的安全报告，这使他能直接了解安全关切是如何被记录和传达的。他在文章中主张，解决方案需要比具体规则或新法律更深入的审视，将问题定性为文化问题而非仅仅是监管问题。

rss · TechCrunch · 10月3日 16:30

**背景**: OpenAI 是 ChatGPT 的开发者，也是领先的 AI 实验室之一，其在安全问题上屡次遭遇内部动荡，包括 2024 年由 Ilya Sutskever 和 Jan Leike 领导的高调安全团队被解散。AI 安全治理指的是指导和监督 AI 系统的政策、法律及内部实践，涵盖谁负责、治理什么以及如何实施监督等问题。欧盟于 2024 年通过了《人工智能法案》，而关于企业是否在能力上推进过快、牺牲安全的争论已成为行业核心议题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken">OpenAI safety leader quits, warning AI... | The Guardian</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/technology/openai-dissolves-high-profile-safety-team-after-chief-scientist-ilya-sutskevers-exit/articleshow/110223018.cms?from=mdr">OpenAI safety team dissolved: OpenAI dissolves high-profile safety ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety_governance">AI safety governance</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#AI governance`, `#tech industry`, `#company culture`

---

<a id="item-9"></a>
## [杰克·多西的 Bitchat 因政府命令从印度应用商店下架](https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/) ⭐️ 7.0/10

杰克·多西的去中心化通讯应用 Bitchat 在印度政府下达命令后已从该国应用商店下架，使其在印度基本无法使用。TechCrunch 于 2026 年 10 月 3 日报道了这一消息，但官方尚未公开详细原因。 这凸显了政府与注重隐私、抗审查的通讯工具之间日益紧张的关系，并可能为印度监管去中心化应用树立先例。此举将影响软件工程师、隐私倡导者以及在受限环境中依赖此类工具的用户。 Bitchat 通过蓝牙低功耗网状网络运行，具备端到端加密，允许在没有互联网基础设施的情况下进行离线点对点通讯。其去中心化设计使当局难以封锁或监控，这很可能引发了印度政府的行动。

rss · TechCrunch · 10月3日 15:02

**背景**: Bitchat 由 Twitter 和 Block 联合创始人杰克·多西于 2025 年 7 月发布，是一款点对点加密通讯应用，使用蓝牙网状网络而非互联网。它旨在抵抗审查，使在互联网受限或断网地区的人们也能通讯。该应用作为去中心化、隐私优先通讯的原型而受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BitChat">BitChat - Wikipedia</a></li>
<li><a href="https://www.theverge.com/news/701272/jack-dorsey-bitchat-bluetooth-messaging-app">Jack Dorsey made an encrypted Bluetooth messaging app | The Verge</a></li>
<li><a href="https://techcrunch.com/2025/07/07/jack-dorsey-working-on-bluetooth-messaging-app-bitchat/">Jack Dorsey working on Bluetooth messaging app, Bitchat</a></li>

</ul>
</details>

**标签**: `#censorship`, `#india`, `#decentralized-messaging`, `#app-store-policy`, `#tech-regulation`

---