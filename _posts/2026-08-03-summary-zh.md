---
layout: default
title: "Horizon Summary: 2026-08-03 (ZH)"
date: 2026-08-03
lang: zh
---

> 从 50 条内容中筛选出 3 条重要资讯。

---

1. [OpenAI 的 Astra 以每个不到 2000 美元解决 10 个十年未解数学难题](#item-1) ⭐️ 8.0/10
2. [Karpathy 指出弹球提示作为新的 LLM 基准](#item-2) ⭐️ 7.0/10
3. [公开信辩论 AI 开放权重监管](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI 的 Astra 以每个不到 2000 美元解决 10 个十年未解数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 8.0/10

OpenAI 宣布其下一代主要模型 Astra 解决了十个至少十年未有进展的数学问题，每个问题在 GPT-5.6 Sol 代币价格下花费不到 2000 美元。结果以 Lean 4 形式化证明和论文形式发布，但未公开所使用的提示词。 这展示了 AI 在纯数学和理论计算机科学领域以极低成本取得重大突破的潜力，可能加速这些领域的研究。同时，继 Anthropic 最近用 Claude Mythos Preview 发现密码学弱点之后，这也加剧了 AI 实验室之间的竞争。 OpenAI 使用了 Astra 的内部版本，并以 GPT-5.6 Sol 代币价格每个问题花费不到 2000 美元。openai/ten-proofs 仓库包含 Lean 4 形式化证明，并提供了描述解决方案的论文和 LLM 生成的 PDF，但未发布提示词。

rss · Simon Willison · 8月1日 20:34

**背景**: Lean 4 是一个交互式定理证明器，可以对数学证明进行形式化验证。OpenAI 的公告延续了 AI 模型用于数学研究的趋势，例如陶哲轩提出的“大数学”概念，涉及人机协作。成本效率显著，因为 GPT-5.6 Sol 的定价为每百万输入代币 5 美元，每百万输出代币 30 美元。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://byteiota.com/openai-astra-multi-agent-model/">OpenAI Astra: Multi-Agent Model Solves 10 Decade-Old Math ...</a></li>
<li><a href="https://www.nextbigfuture.com/2026/08/openai-next-major-model-astra-solves-major-math-problems.html">OpenAI Next Major Model Astra Solves Major Math Problems</a></li>
<li><a href="https://lushbinary.com/blog/gpt-5-6-pricing-cost-optimization-sol-terra-luna/">GPT-5.6 Pricing & Cost Optimization: Sol vs Terra vs Luna</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区讨论可能既有兴奋也有怀疑，一些人质疑未公开的失败案例和提示词透明度。网上的数学家正经历“深蓝时刻”，反映出对 AI 在其领域作用的敬畏和存在主义担忧。

**标签**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#theoretical computer science`

---

<a id="item-2"></a>
## [Karpathy 指出弹球提示作为新的 LLM 基准](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Andrej Karpathy 强调了一个简单的提示——“创建一个弹球游戏”——这个提示难倒了大多数前沿 LLM，引发了关于使用此类任务作为物理世界理解基准的讨论。这一观察在 AI 社区中引起了广泛关注，许多人认为它暴露了当前模型能力的不足。 这很重要，因为它指向了一种新型基准，测试模型对物理交互和空间推理的理解，这对于机器人技术和模拟等现实应用至关重要。同时，它也强调了随着模型改进，需要更多定性和主观的评估方法。 提示“创建一个弹球游戏”通常会导致模型生成所有正确的组件，但无法正确排列它们，例如在发射滑槽中放置墙壁或使挡板以错误方向旋转。据一位评论者称，Opus 5 是第一个在特定环境中“一次性”完成该任务的模型。

hackernews · delichon · 8月2日 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: 前沿 LLM 是在大量文本数据上训练的大型语言模型，擅长语言任务，但往往缺乏对物理世界的直观理解。像这个弹球游戏这样的基准测试了空间推理和物理交互，而这些在传统的基于文本的评估中并未得到很好的体现。这与开发能够模拟和推理现实世界动态的世界模型的更广泛努力相一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/research-outcome/LLM-Game-Benchmark">GitHub - research-outcome/LLM-Game-Benchmark: Evaluating Large Language Models with Grid-Based Game Competitions: An Extensible LLM Benchmark and Leaderboard · GitHub</a></li>
<li><a href="https://www.linkedin.com/posts/joe-glick-11a412_aws-calls-world-models-the-industry-pivot-activity-7467515347596627968-gFMr">World Models: AI's Next-Gen Frontier Beyond Language | LinkedIn</a></li>
<li><a href="https://mbzuai.ac.ae/news/are-frontier-llms-ready-to-be-ai-scientists-a-new-benchmark-says-not-yet/">Are frontier LLMs ready to be AI scientists? A new benchmark says...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍认为弹球提示是一个有用的基准，一些人指出它暴露了模型缺乏物理理解。然而，一些评论者警告说，像 Anthropic 这样的模型可能专门针对 three.js 代码进行了训练，使得此类测试对一般能力的指示性较弱。其他人分享了个人经验，需要大量调整才能让 LLM 生成功能性动画，这表明当前存在局限性。

**标签**: `#AI`, `#LLM`, `#benchmark`, `#physical reasoning`, `#Karpathy`

---

<a id="item-3"></a>
## [公开信辩论 AI 开放权重监管](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

微软于 2026 年 7 月 24 日牵头发布了一封题为“开放权重与美国 AI 领导力”的公开信，已有 235 家 AI 相关公司签署，包括 NVIDIA、亚马逊、Y Combinator、Linux 基金会以及后来的 OpenAI。三天后，Anthropic 发布了自己的回应，7 月 28 日，“Pacing the Frontier”发布，有 1324 名前沿 AI 公司员工签署。 这些信件代表了业界对开放权重 AI 模型监管的重大辩论，主要参与者持相反立场。结果可能影响美国 AI 政策，进而影响 AI 生态系统的创新、竞争和安全。 微软的信明确支持蒸馏技术，即模型利用其他模型的输出进行训练，认为这是一种合法做法。值得注意的是，Anthropic 没有签署微软的信，反而呼吁打击工业规模的蒸馏操作，同时表示从未主张禁止开放权重模型。

rss · Simon Willison · 8月2日 04:16

**背景**: 开放权重模型是指其核心组件（包括最终权重和偏置）公开发布的 AI 模型，任何人都可以下载、检查和修改。争论的焦点在于这类模型是否构成安全风险（如被滥用于网络攻击或生物攻击），还是通过更广泛的访问促进创新和竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/">Open Weights and American AI Leadership - microsoft.com</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open source`, `#open-weight models`, `#industry`, `#regulation`

---