---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 83 items, 15 important content pieces were selected

---

1. [Qwen3.8-2.4T-A95B: Massive MoE Model Rivals Top AI, Runs on Consumer Hardware via 1-bit Quantization](#item-1) ⭐️ 9.0/10
2. [Researchers Steal Hidden Reasoning from Major LLM APIs](#item-2) ⭐️ 9.0/10
3. [DeepSeek V4 Pro 0813: Low-Cost Coding Model Draws Community Praise](#item-3) ⭐️ 8.0/10
4. [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](#item-4) ⭐️ 8.0/10
5. [Meta Releases Muse Glimmer: Open-Weight 30B Agentic Model](#item-5) ⭐️ 8.0/10
6. [Amazon to Train AI on Twitch Streamers' Content by Default, Opt-Out Required](#item-6) ⭐️ 8.0/10
7. [AI Pioneers Debate Openness vs. Safety at Ai4](#item-7) ⭐️ 8.0/10
8. [Form Energy Raises $750M for 100-Hour Iron-Air Batteries](#item-8) ⭐️ 8.0/10
9. [Researcher Publishes Windows Zero-Day After Microsoft Legal Threat](#item-9) ⭐️ 8.0/10
10. [Adam's Anisotropy Breaks Rotation Invariance and Low-Rank Bias](#item-10) ⭐️ 8.0/10
11. [CPU Deoptimization Project Finds Slowest x86 Instruction: 198 Billion Cycles](#item-11) ⭐️ 8.0/10
12. [Linus Torvalds Explains Linux's Speed and Design Principles](#item-12) ⭐️ 8.0/10
13. [The Fastest Double-to-String Algorithm You've Never Heard Of](#item-13) ⭐️ 8.0/10
14. [Zed Introduces Delta Multiplayer Coding Environment](#item-14) ⭐️ 7.0/10
15. [Enterprises Shift from AI Assistance to Agentic Execution](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B: Massive MoE Model Rivals Top AI, Runs on Consumer Hardware via 1-bit Quantization](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen has released Qwen3.8-2.4T-A95B, a 2.4-trillion-parameter Mixture-of-Experts (MoE) model with 95 billion active parameters, available in BF16 and FP8 formats on Hugging Face. The model card claims performance between Opus 4.8 and Fable 5, and community reports indicate a 1-bit quantized version fits in about 397GB, enabling local deployment on high-end consumer hardware. This release significantly lowers the barrier to running state-of-the-art AI models locally, as the 1-bit quantized version can run on a machine a normal person could buy, potentially democratizing access to frontier-level performance. It also intensifies competition among open-weight model providers like Qwen, Kimi, and DeepSeek, pushing the boundaries of efficiency and accessibility. The full BF16 model is about 4.9TB, while the 1-bit quantized version is approximately 397GB with 95B active parameters per MoE. The open-weight model lacks vision input and 1M context length by default, which are exclusive to the official Qwen3.8-Max version. Serving the model at launch is challenging due to the lack of QAT on q4 quantization, requiring external quantization efforts.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, enabling massive scale with manageable compute. Quantization reduces model size by lowering numerical precision, with 1-bit quantization being an extreme form that can drastically shrink models for consumer hardware. Qwen is a leading open-weight AI model series, and this release follows a trend of increasingly large and efficient open models.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/ Qwen 3 . 8 - 2 . 4 T - A 95 B · Hugging Face</a></li>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen 3 . 8 - 2 . 4 T - A 95 B , a 2 . 4 T -Parameter Model , with...</a></li>
<li><a href="https://www.remio.ai/post/qwen-3-8-open-weight-model-announcement-promises-2-4t-parameters-but-proof-comes">Qwen 3 . 8 Open-Weight Model Announcement Promises...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's accessibility via 1-bit quantization, with one user noting it puts Opus 4.5-level performance into a machine a normal person could buy. Others discuss serving challenges, comparisons to rivals like Kimi k3 and DeepSeek V4-Pro, and disappointment that the open-weight version lacks vision and 1M context features.

**Tags**: `#AI/ML`, `#Large Language Models`, `#MoE`, `#Qwen`, `#Open Source`

---

<a id="item-2"></a>
## [Researchers Steal Hidden Reasoning from Major LLM APIs](https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/) ⭐️ 9.0/10

Researchers demonstrated a method to decrypt and recover hidden chain-of-thought reasoning from proprietary LLM APIs by replaying encrypted traces into weaker sibling models and jailbreaking them. The attack affected Anthropic, OpenAI, and Google, but has since been fixed. This vulnerability exposed a significant privacy flaw in major AI APIs, allowing recovery of internal reasoning that providers intended to keep hidden. It highlights the need for stronger encryption and access controls in AI services, and has implications for AI security and user trust. The attack exploited the fact that models within the same family shared the same encryption key, allowing encrypted reasoning blocks to be replayed across sessions and models. The easiest target was Claude Haiku 4.5, which was jailbroken with a simple prompt and an assistant turn prefix. The paper includes extensive extracted reasoning traces in its appendix.

rss · Simon Willison · Aug 11, 22:40

**Background**: Chain-of-thought (CoT) reasoning is a technique where LLMs generate intermediate reasoning steps to improve performance on complex tasks. Proprietary LLM APIs often hide these reasoning traces from users by encrypting them, but this research shows that the encryption can be bypassed. The attack involves replaying encrypted traces into weaker models and jailbreaking them to reveal the original reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/11/stealing-reasoning-traces/">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://www.explainx.ai/blog/stealing-reasoning-traces-encrypted-cot-vulnerability-august-2026">Stealing Reasoning Traces: The Encrypted Chain-of-Thought ...</a></li>
<li><a href="https://cybersecuritynews.com/top-ai-models-apis-flaw-exposes-hidden-reasoning/">OpenAI, Anthropic, and Google LLM APIs vulnerability Exposes ...</a></li>

</ul>
</details>

**Discussion**: The community discussion is not provided, but based on the high score and topic, it likely involves concerns about AI privacy and security, with some praising the research and others questioning the severity. However, no specific comments are available.

**Tags**: `#LLM security`, `#chain-of-thought`, `#privacy`, `#AI research`, `#vulnerability`

---

<a id="item-3"></a>
## [DeepSeek V4 Pro 0813: Low-Cost Coding Model Draws Community Praise](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek released the V4 Pro 0813 snapshot, a large-scale mixture-of-experts model available on OpenRouter at $0.435 per million input tokens and $0.87 per million output tokens. It supports a 1,048,576-token context window and up to 384,000 output tokens, with both thinking and non-thinking modes. This release is significant because it offers competitive coding performance at a fraction of the cost of leading closed-source models, potentially democratizing access to advanced AI for developers and startups. The high community engagement (692 points, 246 comments) reflects strong interest in cost-effective AI alternatives. Independent benchmarks from Artificial Analysis and LM Market Cap rank DeepSeek V4 Pro 0813 around #59 in coding among tracked models. A community test on Codex CLI showed it completed a feature in 12 minutes at $0.12 but with a bug, while Grok 4.6 finished in 3 minutes at $1.41 without bugs.

hackernews · explosion-s · Aug 12, 16:04 · [Discussion](https://news.ycombinator.com/item?id=49274600)

**Background**: DeepSeek is a Chinese AI company known for releasing open-weight models that rival proprietary systems at lower costs. The V4 Pro series is built on a mixture-of-experts architecture, which activates only a subset of parameters per token, improving efficiency. This model is designed for advanced reasoning, coding, and long-horizon agent workflows, and is available through multiple providers.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://lmmarketcap.com/model/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - Pricing & Benchmarks 2026 | LM Market Cap</a></li>
<li><a href="https://models.dev/models/deepseek/deepseek-v4-pro-0813/">DeepSeek V 4 Pro 0813 pricing, providers, and specs | Models .dev</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive, with users praising the model's cost-effectiveness and capability for heavy development tasks. Some users noted the link to OpenRouter lacks useful information and suggested linking to official docs or benchmarks. A direct comparison showed DeepSeek V4 Pro 0813 was cheaper but slower and had a bug, while Grok 4.6 was faster and bug-free but more expensive.

**Tags**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#cost efficiency`

---

<a id="item-4"></a>
## [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale has publicly detailed a 16-year-old bug in SQLite's WAL reset logic that caused repeated database corruption in their control plane. The bug was fixed in SQLite version 3.51.3 after extensive debugging. This incident highlights the critical importance of rigorous testing and open-source debugging tools, as even a widely-used and well-tested database like SQLite can harbor subtle bugs for years. It also demonstrates how companies can fund open-source development to benefit the entire ecosystem. The bug was a data race in the WAL reset logic that could only occur under specific concurrency conditions, despite SQLite's single-writer design. Tailscale and the SQLite team spent weeks hunting the bug, and an initial fix was rolled back after breaking something else before the final fix in 3.51.3.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**Background**: SQLite is a widely-used embedded database that supports Write-Ahead Logging (WAL) for improved performance and concurrency. WAL temporarily stores new entries in a separate file before checkpointing them into the main database. The bug involved a race condition in the WAL reset process, which could corrupt the database under specific circumstances.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://www.theregister.com/databases/2026/08/12/tailscale-says-deeply-buried-16-year-old-sqlite-bug-caused-last-years-outages/5287004">Tailscale says deeply buried 16-year-old SQLite bug caused ...</a></li>
<li><a href="https://antithesis.com/blog/2026/wal-reset-bug/">Breaking the WAL | Antithesis</a></li>

</ul>
</details>

**Discussion**: The community praised Tailscale for the detailed write-up and for funding open-source development, specifically the SQLite VFS shim that helped isolate the bug. Some commenters noted the irony of a single-writer design still having a data race, while others appreciated the technical depth and the company's transparency.

**Tags**: `#SQLite`, `#database`, `#bug`, `#Tailscale`, `#open-source`

---

<a id="item-5"></a>
## [Meta Releases Muse Glimmer: Open-Weight 30B Agentic Model](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/) ⭐️ 8.0/10

Meta has introduced Muse Glimmer, a 30-billion-parameter open-weights model released under the Apache 2.0 license, optimized for agentic task completion, tool use, and multi-step reasoning. The model is available for download via LM Studio and Hugging Face, with an 18.16 GB quantized version. This release is significant because it marks Meta's return to open-weight models with a permissive license, potentially accelerating adoption of agentic AI in local and consumer environments. The focus on agentic capabilities aligns with industry trends toward autonomous task completion and tool integration. Muse Glimmer is a vision model with a dedicated perception encoder, distilled from Muse Spark. It performs well on benchmarks like DeepSearchQA, MCP-Atlas, τ-Bench, and SWE-Bench, and can run on machines with 32 GB RAM or more, leaving room for other applications.

rss · Simon Willison · Aug 10, 23:56

**Background**: Agentic AI refers to models capable of autonomously performing multi-step tasks, using tools, and reasoning over long horizons. Open-weights models allow developers to run and fine-tune them locally, offering privacy and customization benefits. Apache 2.0 is a permissive license that permits commercial use with minimal restrictions.

<details><summary>References</summary>
<ul>
<li><a href="https://ollama.com/library/muse-glimmer">muse - glimmer</a></li>
<li><a href="https://huggingface.co/meta-models/Muse-Glimmer-30B">meta- models / Muse - Glimmer -30B · Hugging Face</a></li>
<li><a href="https://arxiv.org/abs/2601.20975">[2601.20975] DeepSearchQA: Bridging the Comprehensiveness Gap ... DeepSearchQA:Bridgingthe ComprehensivenessGapforDeepResearch ... DeepSearchQA: Bridging the Comprehensiveness Gap for Deep ... DeepSearchQA Leaderboard & Scores — August 2026 | BenchLM.ai DeepSearchQA Leaderboard DeepSearchQA Evaluation for AI-Q Deep Researcher google/deepsearchqa · Datasets at Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#Meta`, `#Agentic AI`, `#Model Release`

---

<a id="item-6"></a>
## [Amazon to Train AI on Twitch Streamers' Content by Default, Opt-Out Required](https://techcrunch.com/2026/08/12/amazon-will-train-on-twitch-streamers-content-by-default-unless-they-opt-out/) ⭐️ 8.0/10

Amazon will use Twitch streamers' content for AI training by default, requiring users to opt out if they do not want their content used. Twitch CPO Mike Minton confirmed this policy in a livestream, stating that an opt-in model would result in few participants. This policy shift raises significant privacy and ethical concerns for content creators, as their content is used without explicit consent. It could set a precedent for other platforms and intensify debates about AI training data consent and creator rights. The policy applies to all Twitch streamers by default, with an opt-out mechanism available. Mike Minton's comment, 'If this was opt-in, nobody would opt in,' highlights the company's rationale, but has drawn criticism for disregarding user preferences.

rss · TechCrunch · Aug 12, 20:10

**Background**: Twitch is a live streaming platform owned by Amazon, where creators broadcast gameplay, music, and other content. AI training often uses large datasets of publicly available content, but using creator content without explicit consent raises legal and ethical questions. Amazon's broader AI training practices include using publicly available data, as stated in their generative AI disclosure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.windowscentral.com/artificial-intelligence/if-it-was-opt-in-nobody-would-opt-in-cringe-twitch-cpo-admits-everyone-hates-its-ai-training-feature-doesnt-care">"If it was opt in ... nobody would opt-in." Twitch CPO ... | Windows Ce...</a></li>
<li><a href="https://www.amazon.com/gp/help/customer/display.html?nodeId=TmGoGN3UbFaQ1CAph7">Generative AI Development Disclosure - Amazon Customer Service</a></li>
<li><a href="https://aws.amazon.com/bedrock/amazon-models/privacy/">Amazon Model Training & Privacy - AWS</a></li>

</ul>
</details>

**Discussion**: The community response has been largely negative, with many criticizing the CPO's admission as dismissive of user concerns. Some users point out that unlike YouTube, Twitch at least offers an opt-out option, but the default opt-in approach is seen as a betrayal of creator trust.

**Tags**: `#AI training`, `#Twitch`, `#Amazon`, `#privacy`, `#content policy`

---

<a id="item-7"></a>
## [AI Pioneers Debate Openness vs. Safety at Ai4](https://techcrunch.com/2026/08/12/as-ai-safety-concerns-mount-three-pioneers-make-the-case-for-staying-open/) ⭐️ 8.0/10

At the Ai4 conference, Geoffrey Hinton, Fei-Fei Li, and Andrew Ng engaged in a public debate about AI regulation, open source access, and US competitiveness in light of China's advances. This discussion is significant because it brings together three of the most influential voices in AI to address a critical policy question: how to balance safety concerns with the benefits of openness. Their perspectives could shape regulatory approaches and industry practices globally, affecting developers, researchers, and policymakers. The debate took place at the Ai4 conference, and the panelists discussed the tension between AI safety and open source access, as well as how the US can compete as China advances in AI. No specific policy proposals or technical breakthroughs were announced, but the exchange highlighted differing viewpoints among the experts.

rss · TechCrunch · Aug 12, 17:51

**Background**: AI safety concerns have grown as advanced AI systems become more capable, leading to calls for regulation and restrictions on open source models. However, open source advocates argue that transparency and collaboration are essential for innovation and for ensuring that AI benefits are widely distributed. The debate reflects a broader industry and policy discussion about how to govern AI development responsibly.

**Tags**: `#AI safety`, `#AI regulation`, `#open source`, `#Geoffrey Hinton`, `#Fei-Fei Li`

---

<a id="item-8"></a>
## [Form Energy Raises $750M for 100-Hour Iron-Air Batteries](https://techcrunch.com/2026/08/12/form-energy-raises-750m-to-build-more-100-hour-batteries-for-the-grid/) ⭐️ 8.0/10

Form Energy has raised $750 million to expand manufacturing of its 100-hour iron-air batteries, with Google and Crusoe as customers. The funding will support scaling production to meet growing demand for long-duration grid storage. This significant funding round highlights the growing importance of long-duration energy storage for integrating renewable energy. With major customers like Google and Crusoe, Form Energy's technology could help stabilize the grid and reduce reliance on fossil fuels. The 100-hour iron-air batteries use reversible rusting technology, offering storage at under $20/kWh, which is about 10 times cheaper than lithium-ion. Form Energy's West Virginia gigafactory is already shipping these batteries, and the new funding will further expand production capacity.

rss · TechCrunch · Aug 12, 16:18

**Background**: Iron-air batteries are a type of metal-air battery that uses iron as the anode and oxygen from ambient air as the cathode. They are designed for long-duration storage, providing power for up to 100 hours, which is crucial for balancing intermittent renewable sources like solar and wind. This technology is seen as a key solution to the intermittency problem of renewables.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Metal–air_electrochemical_cell">Metal–air electrochemical cell - Wikipedia</a></li>
<li><a href="https://energy-solutions.co/articles/sub/aqueous-iron-air-batteries-long-duration-storage">Iron-Air Batteries 2026: 100-Hour Storage at Under $20/kWh ...</a></li>
<li><a href="https://hardware.slashdot.org/story/26/02/28/0446211/worlds-largest-battery-soon-at-google-data-center-100-hour-iron-air-storage">'World's Largest Battery ' Soon At Google Data Center: 100 - Hour ...</a></li>

</ul>
</details>

**Tags**: `#energy storage`, `#batteries`, `#renewable energy`, `#grid`, `#funding`

---

<a id="item-9"></a>
## [Researcher Publishes Windows Zero-Day After Microsoft Legal Threat](https://techcrunch.com/2026/08/12/after-microsoft-threatened-legal-action-a-security-researcher-publishes-a-new-windows-zero-day-bug/) ⭐️ 8.0/10

Security researcher Nightmare Eclipse has published a new Windows zero-day vulnerability despite Microsoft publicly threatening legal action against them. This marks the latest in a series of disclosures by the researcher, escalating tensions between independent security researchers and the software giant. This incident highlights the ongoing conflict between security researchers and vendors over vulnerability disclosure, raising questions about the balance between responsible disclosure and legal intimidation. It could impact how researchers choose to disclose vulnerabilities in the future, potentially affecting the security of Windows users worldwide. The zero-day is the latest from Nightmare Eclipse, who has previously released other Windows vulnerabilities. Microsoft's legal threat appears to have not deterred the researcher, and the publication may include technical details that could be exploited by malicious actors.

rss · TechCrunch · Aug 12, 15:18

**Background**: Zero-day vulnerabilities are software flaws unknown to the vendor, leaving no patch available, making them highly valuable to attackers. Vulnerability disclosure is a contentious issue: researchers often face legal threats from vendors when they publish details, even if done responsibly. Microsoft has a history of taking legal action against researchers, and this case is part of a broader pattern of tension in the security community.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/lazarus-hackers-exploited-windows-zero-day-to-target-defense-firms/">Lazarus hackers exploited Windows zero-day to target defense ...</a></li>
<li><a href="https://www.zdnet.com/article/microsoft-august-windows-update-421-bugs-zero-day-exploited/">Microsoft fixes 421 bugs and a Windows zero-day in August ...</a></li>
<li><a href="https://github.com/disclose/research-threats">GitHub - disclose/research-threats: Collection of legal threats against good faith Security Researchers; vulnerability disclosure gone wrong. A continuation of work started by @attritionorg · GitHub</a></li>

</ul>
</details>

**Tags**: `#security`, `#zero-day`, `#Microsoft`, `#vulnerability disclosure`, `#legal`

---

<a id="item-10"></a>
## [Adam's Anisotropy Breaks Rotation Invariance and Low-Rank Bias](https://www.reddit.com/r/MachineLearning/comments/1vmjb3p/the_loss_does_not_see_the_basis_but_adam_does_r/) ⭐️ 8.0/10

A new study shows that Adam's per-coordinate adaptivity breaks rotation invariance in factored models, causing loss of implicit low-rank bias, while optimizers like Muon and Shampoo preserve it. The author tested nine update rules on underdetermined matrix sensing and found two distinct clusters based on this property. This insight connects optimizer choice to implicit bias in matrix factorization, which is crucial for understanding generalization in overparameterized models. It could guide practitioners in selecting optimizers that preserve low-rank structure, improving performance on tasks like matrix completion and deep learning. The study includes a one-parameter family that interpolates between per-coordinate and shared-scalar denominators, showing recovery improves monotonically as anisotropy decreases. Muon shows exact recovery on truly low-rank targets but degrades with spectral tail, crossing over with GD near 4% tail energy. The author also found that global norm clipping improved their own optimizer's recovery error from 0.347 to 0.220.

reddit · r/MachineLearning · /u/EtherealGlyph · Aug 12, 16:39

**Background**: In matrix factorization, models like W = UV^T are invariant to rotations (U,V) → (UQ, VQ), and gradient descent respects this symmetry. Adam's per-coordinate second moment normalization breaks this invariance because it depends on the basis of the factors. Implicit bias refers to the tendency of optimization algorithms to converge to solutions with certain properties, such as low rank, without explicit regularization.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2509.24218v2">Conda: Column-Normalized Adam for Training Large Language Models Faster</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rotational_invariance">Rotational invariance - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The discussion includes debates on the implications for Muon, with some reporting strong spectral simplicity bias and others finding it fits spurious features in deep-linear models. The author notes that their sweep shows both behaviors on the same axis. There are also comments about tuning Adam harder, which the author welcomes.

**Tags**: `#optimization`, `#implicit bias`, `#low-rank`, `#Adam`, `#matrix sensing`

---

<a id="item-11"></a>
## [CPU Deoptimization Project Finds Slowest x86 Instruction: 198 Billion Cycles](https://www.reddit.com/r/programming/comments/1vmhj23/hardware_researcher_spins_up_cpu_deoptimization/) ⭐️ 8.0/10

A hardware researcher launched a 'CPU deoptimization' project to identify the slowest single x86 instruction, discovering one that takes 198 billion cycles, equivalent to 62 seconds to execute. The project compiles a 'hall of shame' of notoriously slow instructions. This project highlights surprising performance characteristics of x86 instructions, which can inform performance engineering and compiler design. It challenges assumptions about instruction efficiency and may lead to better optimization strategies in software development. The slowest instruction takes 198 billion cycles, which at a typical 3.2 GHz clock speed translates to about 62 seconds. The project likely uses precise timing methods such as the Time Stamp Counter (RDTSC) to measure cycle counts, and the findings are compiled into a public 'hall of shame' list.

reddit · r/programming · /u/masiroo · Aug 12, 15:34

**Background**: x86 instructions vary greatly in execution time, influenced by factors like microcode, memory access, and pipeline stalls. Tools like Agner Fog's instruction tables and the Time Stamp Counter (TSC) are commonly used to measure instruction latencies. This project takes a reverse approach, focusing on the slowest instructions rather than the fastest, to highlight potential performance pitfalls.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Time_Stamp_Counter">Time Stamp Counter - Wikipedia</a></li>
<li><a href="https://www.agner.org/optimize/instruction_tables.pdf">Introduction Page 1 4. Instruction tables By Agner Fog</a></li>
<li><a href="https://stackoverflow.com/questions/692718/how-many-cpu-cycles-are-needed-for-each-assembly-instruction">How many CPU cycles are needed for each assembly instruction? Code sample</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion likely includes comments expressing fascination with the extreme cycle counts and debating the practical implications for real-world code. Some may question the methodology or suggest that such slow instructions are rarely used in practice, while others appreciate the educational value of the project.

**Tags**: `#x86`, `#CPU`, `#performance`, `#hardware`, `#instruction set`

---

<a id="item-12"></a>
## [Linus Torvalds Explains Linux's Speed and Design Principles](https://www.reddit.com/r/programming/comments/1vmoddq/linus_torvalds_explains_what_makes_linux_so_fast/) ⭐️ 8.0/10

Linus Torvalds shared his insights on the design and engineering principles that make Linux fast, in a discussion on Reddit. He emphasized the importance of simplicity, good data structures, and avoiding unnecessary complexity. This discussion provides rare direct insight from the creator of Linux, offering valuable guidance for developers and system designers. Understanding these principles can help improve performance in other software projects and deepen appreciation for Linux's architecture. Torvalds highlighted that Linux's speed comes from a focus on the common case, efficient algorithms, and a willingness to change designs when better alternatives exist. He also stressed the importance of profiling and measuring to guide optimization efforts.

reddit · r/programming · /u/Rechenplaner · Aug 12, 19:40

**Background**: Linux is a widely used open-source operating system kernel known for its performance and reliability. Its design choices, such as a monolithic kernel and a focus on simplicity, have been debated and refined over decades. Torvalds' comments offer a rare glimpse into the philosophy behind these choices.

**Discussion**: The Reddit discussion likely includes technical commentary from developers, with many agreeing on the importance of simplicity and profiling. Some may debate specific trade-offs, but overall sentiment appears positive and appreciative of Torvalds' direct input.

**Tags**: `#Linux`, `#performance`, `#kernel`, `#Linus Torvalds`, `#systems`

---

<a id="item-13"></a>
## [The Fastest Double-to-String Algorithm You've Never Heard Of](https://www.reddit.com/r/programming/comments/1vm65dm/the_fastest_doubletostring_algorithm_youve_never/) ⭐️ 8.0/10

A Reddit post highlights a little-known algorithm called 'yy' for converting double-precision floating-point numbers to strings, which reportedly outperforms existing methods like Schubfach. The algorithm uses only one multiplication by a precomputed power of 10, making it faster than classic approaches. Double-to-string conversion is a performance-critical operation in many systems, such as JSON serialization, logging, and database output. A faster algorithm can significantly improve throughput in applications that handle large volumes of floating-point data. The algorithm, detailed in a blog post by vitaut, runs entirely on fixed-width integer arithmetic and uses only one multiplication by a precomputed power of 10, whereas classic Schubfach requires two or three. Benchmark results show yy achieving 16.61 ns per conversion compared to Schubfach's 34.58 ns.

reddit · r/programming · /u/mttd · Aug 12, 06:25

**Background**: Double-to-string conversion is the process of converting a 64-bit IEEE-754 floating-point number into its decimal string representation. The challenge is to produce the shortest string that round-trips back to the original binary value, which is essential for accurate data representation. Traditional algorithms like Schubfach and Errol are used in various libraries, but the 'yy' algorithm offers a more efficient approach by intersecting rounding intervals with decimal grids.

<details><summary>References</summary>
<ul>
<li><a href="https://vitaut.net/posts/2026/yy-dtoa/">The fastest double-to-string algorithm you’ve never heard of</a></li>
<li><a href="https://lobste.rs/s/vzza5g/fastest_double_string_algorithm_you_ve">The fastest double-to-string algorithm you’ve never heard of | Lobsters</a></li>
<li><a href="https://github.com/miloyip/dtoa-benchmark">GitHub - miloyip/dtoa-benchmark: C++ double-to-string conversion benchmark · GitHub</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion includes expert commentary and validation, with users noting the performance improvements and discussing the algorithm's implementation details. Some users question the switch from Schubfach to yy in certain libraries, given the significant speed difference.

**Tags**: `#algorithms`, `#performance`, `#floating-point`, `#optimization`, `#programming`

---

<a id="item-14"></a>
## [Zed Introduces Delta Multiplayer Coding Environment](https://zed.dev/blog/introducing-delta) ⭐️ 7.0/10

Zed has introduced Delta, a multiplayer environment for coding with agents and reviewing their work, and is inviting users to a private beta. This feature enables real-time collaborative conversations and treats conversations as documents, allowing inline comments in agent interactions. Delta could reshape collaborative development workflows by enabling teams to work together in real time within the editor, potentially reducing the need for separate code review tools. It also sparks debate about the value of multi-user editing and AI-generated summaries, reflecting broader industry trends toward AI-assisted development. Delta is currently in private beta, and the underlying technology, DeltaDB, is expected to be open-sourced. The feature builds on Zed's existing AI agent capabilities, including parallel agents introduced in 2026, and aims to provide a more integrated collaborative experience.

hackernews · khy · Aug 12, 18:19 · [Discussion](https://news.ycombinator.com/item?id=49276574)

**Background**: Zed is a high-performance code editor built with a Rust UI framework called GPUI, created by the team behind Atom. It has gained attention for its speed and built-in AI features, and Delta represents a significant step toward integrating collaborative and AI-driven workflows directly into the editor.

<details><summary>References</summary>
<ul>
<li><a href="https://zed.dev/blog/introducing-delta">Introducing Delta — Zed 's Blog</a></li>
<li><a href="https://sesamedisk.com/what-is-zed-deltadb-features/">What Is Zed DeltaDB and Its Key Features - Sesame Disk</a></li>
<li><a href="https://runtimewire.com/article/zed-deltadb-version-control-agent-conversations">Nathan Sobo's Zed takes aim at pull requests with... - RuntimeWire</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some question the practical value of multi-user editing, calling coding a 'single-player game,' while others see potential in mentoring and reviewing AI-generated work. Concerns about AI summaries include verbosity and missing edge cases, and some users also complain about the blog post's low-contrast design.

**Tags**: `#Zed`, `#code editor`, `#collaborative editing`, `#AI`, `#developer tools`

---

<a id="item-15"></a>
## [Enterprises Shift from AI Assistance to Agentic Execution](https://openai.com/index/how-enterprises-put-ai-to-work) ⭐️ 7.0/10

OpenAI's research highlights how enterprises are moving from using AI for assistance to deploying agentic AI for execution, with tools like ChatGPT and Codex. Frontier firms are reportedly pulling ahead in AI adoption, gaining a competitive edge. This shift signals a major trend in enterprise AI, where autonomous agents can handle complex tasks beyond simple chat, potentially transforming workflows and productivity. It underscores the strategic importance of adopting agentic AI to stay competitive, affecting AI practitioners, business leaders, and the broader tech ecosystem. The research specifically mentions ChatGPT and Codex as key tools in this transition, with Codex being an AI coding agent that automates software engineering tasks. The findings suggest that early adopters of agentic AI are gaining measurable advantages, though specific metrics were not disclosed in the summary.

rss · OpenAI Blog · Aug 12, 06:00

**Background**: Agentic AI refers to AI systems that can act autonomously to achieve goals with limited supervision, using tools and adapting to complete tasks. Unlike traditional chatbots that only respond to prompts, agentic AI can plan and execute multi-step processes. OpenAI's Codex, released in April 2025, is an example of such an agent, designed for coding tasks. This research reflects a broader industry trend where enterprises are moving from AI as a copilot to AI as an autonomous worker.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is agentic AI? - IBM</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#enterprise AI`, `#agentic AI`, `#AI adoption`, `#OpenAI`, `#ChatGPT`

---