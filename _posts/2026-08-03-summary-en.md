---
layout: default
title: "Horizon Summary: 2026-08-03 (EN)"
date: 2026-08-03
lang: en
---

> From 50 items, 3 important content pieces were selected

---

1. [OpenAI's Astra Solves 10 Decade-Old Math Problems for Under $2,000 Each](#item-1) ⭐️ 8.0/10
2. [Karpathy Highlights Pinball Prompt as New LLM Benchmark](#item-2) ⭐️ 7.0/10
3. [Open Letters Debate AI Open-Weight Regulation](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI's Astra Solves 10 Decade-Old Math Problems for Under $2,000 Each](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 8.0/10

OpenAI announced that its next major model, Astra, solved ten mathematical problems that had seen no progress for at least a decade, spending less than $2,000 per problem at GPT-5.6 Sol token prices. The results were published with Lean 4 formalizations and a paper, but the prompts used were not disclosed. This demonstrates AI's potential to make significant breakthroughs in pure mathematics and theoretical computer science at a remarkably low cost, potentially accelerating research in these fields. It also intensifies competition among AI labs, following Anthropic's recent cryptographic discovery with Claude Mythos Preview. OpenAI used an internal version of Astra and spent less than $2,000 per problem at GPT-5.6 Sol token prices. The openai/ten-proofs repository contains Lean 4 formalizations, and a paper and an LLM-generated PDF describing the solutions are available, but the prompts were not released.

rss · Simon Willison · Aug 1, 20:34

**Background**: Lean 4 is an interactive theorem prover that allows formal verification of mathematical proofs. OpenAI's announcement follows a trend of AI models being used for mathematical research, such as Terence Tao's concept of 'big mathematics' involving human-AI collaboration. The cost efficiency is notable, as GPT-5.6 Sol pricing is $5 per million input tokens and $30 per million output tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://byteiota.com/openai-astra-multi-agent-model/">OpenAI Astra: Multi-Agent Model Solves 10 Decade-Old Math ...</a></li>
<li><a href="https://www.nextbigfuture.com/2026/08/openai-next-major-model-astra-solves-major-math-problems.html">OpenAI Next Major Model Astra Solves Major Math Problems</a></li>
<li><a href="https://lushbinary.com/blog/gpt-5-6-pricing-cost-optimization-sol-terra-luna/">GPT-5.6 Pricing & Cost Optimization: Sol vs Terra vs Luna</a></li>

</ul>
</details>

**Discussion**: The Hacker News community discussion likely includes both excitement and skepticism, with some questioning the undisclosed failures and the lack of prompt transparency. Mathematicians online are experiencing a 'Deep Blue moment,' reflecting both awe and existential concern about AI's role in their field.

**Tags**: `#AI`, `#mathematics`, `#OpenAI`, `#research`, `#theoretical computer science`

---

<a id="item-2"></a>
## [Karpathy Highlights Pinball Prompt as New LLM Benchmark](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Andrej Karpathy highlighted a simple prompt—'create a pinball game'—that stumps most frontier LLMs, sparking discussion about using such tasks as benchmarks for physical world understanding. This observation has gained traction in the AI community, with many agreeing that it exposes gaps in current model capabilities. This matters because it points to a new kind of benchmark that tests models' understanding of physical interactions and spatial reasoning, which are crucial for real-world applications like robotics and simulation. It also highlights the need for more qualitative and subjective evaluation methods as models improve. The prompt 'create a pinball game' often results in models producing all the right components but failing to arrange them correctly, such as placing a wall in the launch chute or having flippers pivot the wrong way. Opus 5 is noted as the first model to 'one shot' it in a harness, according to one commenter.

hackernews · delichon · Aug 2, 04:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Background**: Frontier LLMs are large language models trained on vast text data, excelling at language tasks but often lacking intuitive understanding of the physical world. Benchmarks like this pinball game test spatial reasoning and physical interaction, which are not well captured by traditional text-based evaluations. This aligns with broader efforts to develop world models that can simulate and reason about real-world dynamics.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/research-outcome/LLM-Game-Benchmark">GitHub - research-outcome/LLM-Game-Benchmark: Evaluating Large Language Models with Grid-Based Game Competitions: An Extensible LLM Benchmark and Leaderboard · GitHub</a></li>
<li><a href="https://www.linkedin.com/posts/joe-glick-11a412_aws-calls-world-models-the-industry-pivot-activity-7467515347596627968-gFMr">World Models: AI's Next-Gen Frontier Beyond Language | LinkedIn</a></li>
<li><a href="https://mbzuai.ac.ae/news/are-frontier-llms-ready-to-be-ai-scientists-a-new-benchmark-says-not-yet/">Are frontier LLMs ready to be AI scientists? A new benchmark says...</a></li>

</ul>
</details>

**Discussion**: Community comments generally agree that the pinball prompt is a useful benchmark, with some noting that it exposes models' lack of physical understanding. However, some commenters caution that models like Anthropic's may be specifically trained on three.js code, making such tests less indicative of general capability. Others share personal experiences of needing extensive tuning to get LLMs to produce functional animations, suggesting current limitations.

**Tags**: `#AI`, `#LLM`, `#benchmark`, `#physical reasoning`, `#Karpathy`

---

<a id="item-3"></a>
## [Open Letters Debate AI Open-Weight Regulation](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 7.0/10

Microsoft shepherded an open letter titled 'Open Weights and American AI Leadership' dated July 24, 2026, signed by 235 AI-adjacent companies including NVIDIA, Amazon, Y Combinator, The Linux Foundation, and later OpenAI. Three days later, Anthropic published its own response, and on July 28, 'Pacing the Frontier' was released with signatures from 1,324 employees of frontier AI companies. These letters represent a significant industry-wide debate over the regulation of open-weight AI models, with major players taking opposing stances. The outcome could shape US AI policy, affecting innovation, competition, and safety in the AI ecosystem. The Microsoft letter explicitly supports distillation, a technique where models train on other models' outputs, arguing it is a legitimate practice. Notably, Anthropic did not sign the Microsoft letter and instead called for a crackdown on industrial-scale distillation operations, while also stating it has never advocated for a ban on open-weights models.

rss · Simon Willison · Aug 2, 04:16

**Background**: Open-weight models are AI models whose core components, including final weights and biases, are publicly released, allowing anyone to download, inspect, and modify them. The debate centers on whether such models pose safety risks, such as misuse for cyberattacks or biological attacks, or whether they promote innovation and competition by allowing broader access.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/">Open Weights and American AI Leadership - microsoft.com</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open source`, `#open-weight models`, `#industry`, `#regulation`

---