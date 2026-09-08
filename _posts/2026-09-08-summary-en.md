---
layout: default
title: "Horizon Summary: 2026-09-08 (EN)"
date: 2026-09-08
lang: en
---

> From 50 items, 11 important content pieces were selected

---

1. [OpenAI Reveals How Coding Agents Accelerate AI Research](#item-1) ⭐️ 8.0/10
2. [Europe's First Commercial Orbital Rocket Reaches Orbit](#item-2) ⭐️ 8.0/10
3. [LLM-Guided Evolution Breaks 10 Circle-Packing Records for $28](#item-3) ⭐️ 8.0/10
4. [OpenAI Chief Scientist Calls for Stronger AI Alignment and Global Coordination](#item-4) ⭐️ 7.0/10
5. [Linux Kernel Git Server Overwhelmed by Abusive Scrapers](#item-5) ⭐️ 7.0/10
6. [OpenAI Chief Scientist Advocates for Defensive AI Development](#item-6) ⭐️ 7.0/10
7. [DNS Abuse: Up to 20% of New gTLDs Are Scams](#item-7) ⭐️ 7.0/10
8. [Why Rewriting Software from Scratch Usually Fails](#item-8) ⭐️ 7.0/10
9. [Seattle Times and Newsday Sue OpenAI and Microsoft for Copyright Infringement](#item-9) ⭐️ 7.0/10
10. [Tiny Recurrent System Autonomously Generates Bad Apple Video from Single State](#item-10) ⭐️ 7.0/10
11. [Rustuna: High-Performance Rust Implementation of Optuna Released](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Reveals How Coding Agents Accelerate AI Research](https://openai.com/index/research-acceleration-view-inside-openai) ⭐️ 8.0/10

OpenAI published a blog post sharing early data on how coding agents are reshaping its internal AI research, showing a dramatic increase in daily AI spend per researcher from near zero in February 2026 to roughly $600 by late August 2026. The post also discusses the concept of Recursive Self-Improvement (RSI), which OpenAI appears to consider its new AGI milestone. This is significant because it provides an authoritative, insider look at how AI labs themselves are leveraging coding agents to accelerate research, potentially leading to faster AI development and the realization of RSI. The data suggests a major shift in research workflows, which could have broad implications for the AI industry and the pace of innovation. The post includes a chart showing that daily AI spend per researcher remained near zero until around April 2026, then rose steadily to about $150 by June, plateaued, and then surged to roughly $600 by late August. The author speculates that the late-July acceleration may correspond to internal access to the model later released as GPT-6 Astra.

rss · OpenAI Blog · Sep 6, 08:00

**Background**: Recursive Self-Improvement (RSI) is a hypothesized process where an AGI system can rewrite its own code to become more intelligent, potentially leading to an intelligence explosion. Coding agents are AI tools that can autonomously write, debug, and refactor code, and they are increasingly used in software development and research. OpenAI's post suggests that these agents are becoming integral to its research process, enabling higher experiment velocity and task complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2607.07663">[2607.07663] Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops</a></li>
<li><a href="https://sakana.ai/rsi-lab/">Introducing Sakana AI’s Recursive Self-Improvement (RSI) Lab</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI research`, `#coding agents`, `#research acceleration`, `#ML`

---

<a id="item-2"></a>
## [Europe's First Commercial Orbital Rocket Reaches Orbit](https://www.theverge.com/science/990906/isar-aerospace-europe-orbital-rocket-launch) ⭐️ 8.0/10

Germany's Isar Aerospace successfully launched its two-stage Spectrum rocket into low Earth orbit from a Norwegian spaceport, marking Europe's first fully commercial orbital launch. This follows a failed attempt in March when the vehicle crashed into the sea after 30 seconds. This milestone demonstrates that private European companies can independently achieve orbital launches, reducing reliance on government agencies and foreign providers. It could spur competition and innovation in the European space industry, benefiting satellite operators and the broader aerospace ecosystem. The Spectrum rocket is a relatively compact, two-stage, liquid-fueled vehicle designed to carry up to 1,000 kg to low Earth orbit. It uses liquid oxygen and propane for propulsion, and most of its development and manufacturing, including its Aquila engines, is done in-house.

rss · The Verge · Sep 6, 19:04

**Background**: Low Earth orbit (LEO) is an orbit around Earth with an altitude typically below 2,000 km, where most artificial satellites reside. Historically, European orbital launches have been conducted by government-backed entities like Arianespace, so a fully commercial launch by a startup like Isar Aerospace represents a significant shift toward privatization in the region's space sector.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Spectrum_(rocket)">Spectrum (rocket) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Isar_Aerospace">Isar Aerospace - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Low_Earth_orbit">Low Earth orbit - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space`, `#aerospace`, `#rocket launch`, `#commercial space`, `#Europe`

---

<a id="item-3"></a>
## [LLM-Guided Evolution Breaks 10 Circle-Packing Records for $28](https://www.reddit.com/r/MachineLearning/comments/1w9xlyi/llmguided_program_evolution_improves_10_bestknown/) ⭐️ 8.0/10

A researcher used an LLM to iteratively evolve an optimization algorithm, improving the best-known sum-of-radii for 10 circle-packing instances (N=101-114) on the Packomania csqv benchmark by 2.4% to 5.4% in 15 iterations, at a total LLM cost of $27.72. The results were independently accepted by Packomania. This demonstrates a novel application of LLMs to evolve optimization algorithms rather than directly solve problems, achieving measurable improvements on a recognized benchmark with independent verification. The low cost and open-source nature could inspire broader adoption of LLM-guided program evolution in other optimization domains. The approach starts from a simple seed solver, with the LLM proposing algorithmic changes guided by a scoreboard and history, and each candidate is scored by an independent verifier. The paper is available on arXiv (2609.05093), with code and solutions on GitHub (ucsandman/discovery-loop), and the author invites critique on the plateau-detection stopping rule.

reddit · r/MachineLearning · /u/SIGH_I_CALL · Sep 7, 16:54

**Background**: Circle packing is a classic optimization problem where non-overlapping circles are placed in a container to maximize the sum of radii or packing density. Packomania is a well-known benchmark repository for such problems, and the csqv variant focuses on specific instances. LLM-guided program evolution is an emerging technique where large language models propose code modifications iteratively, guided by feedback, to improve algorithms.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.05093">[2609.05093] LLM-Guided Program Evolution for Circle Packing: Breaking 10 Packomania Records for $28</a></li>
<li><a href="https://packomania.com/">Packomania (52C17)</a></li>
<li><a href="https://github.com/clint-kristopher-morris/llm-guided-evolution">GitHub - clint-kristopher-morris/llm-guided-evolution: LLM Guided Evolution - The Automation of Models Advancing Models · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#program evolution`, `#optimization`, `#circle packing`, `#AI research`

---

<a id="item-4"></a>
## [OpenAI Chief Scientist Calls for Stronger AI Alignment and Global Coordination](https://openai.com/index/an-alien-mind) ⭐️ 7.0/10

OpenAI's Chief Scientist Jakub Pachocki published a reflective piece titled 'An Alien Mind' discussing the challenges of aligning increasingly capable AI systems. He explicitly calls for stronger safeguards and international coordination to address these risks. This piece signals that leading AI researchers are prioritizing alignment and governance as AI capabilities advance, potentially influencing industry practices and policy discussions. It underscores the urgency of global cooperation to mitigate existential risks from misaligned AI. The article is a reflective commentary rather than a technical breakthrough, focusing on the philosophical and practical challenges of aligning superintelligent systems. Pachocki's position as Chief Scientist at OpenAI lends weight to his call for stronger safeguards and international coordination.

rss · OpenAI Blog · Sep 6, 09:00

**Background**: AI alignment is a subfield of AI safety that aims to steer AI systems toward intended goals and values, but it is challenging because proxy goals can lead to reward hacking or unintended behaviors. Advanced AI systems may develop emergent behaviors like power-seeking or deception, which could be harmful if not properly aligned. Many prominent AI researchers and leaders have warned that misaligned superintelligent AI could endanger civilization, prompting calls for robust governance and international cooperation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_governance">AI governance</a></li>

</ul>
</details>

**Tags**: `#AI alignment`, `#AI safety`, `#OpenAI`, `#AI governance`

---

<a id="item-5"></a>
## [Linux Kernel Git Server Overwhelmed by Abusive Scrapers](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev reported that git.kernel.org, the official Git repository for the Linux kernel, now spends more CPU cycles rendering commits for scrapers than on all legitimate access, including git clones. Across five geo-distributed nodes, 14 CPU cores are constantly dedicated to rendering git commits as HTML for scrapers. This highlights the growing operational burden of abusive web scrapers on critical open-source infrastructure, which can degrade performance for legitimate users and increase costs. It underscores the need for better scraping etiquette, bot detection, and resource management strategies across the web ecosystem. The report indicates that at any one time, 14 CPU cores across the five nodes are solely occupied with rendering commits as HTML for scrapers. This 'background radiation' of abusive crawlers is a significant issue for sites like Datasette, which serves many crawlable pages.

rss · Simon Willison · Sep 7, 23:08

**Background**: git.kernel.org is the official Git repository for the Linux kernel, operated by the Linux Kernel Organization. Web scrapers are automated programs that systematically fetch web pages, and when they ignore robots.txt or make excessive requests, they can consume significant server resources. Rendering git commits as HTML is a feature that allows users to view commits in a browser, but it is computationally expensive when done for scrapers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kernel.org/">The Linux Kernel Archives</a></li>
<li><a href="https://github.com/torvalds/linux">GitHub - torvalds/linux: Linux kernel source tree · GitHub</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion likely includes diverse perspectives on mitigation strategies, such as blocking scrapers, using CAPTCHAs, or implementing rate limiting. Some may argue that scrapers are a sign of AI training bots, while others might suggest better server-side caching or serving static pages to reduce load.

**Tags**: `#web scraping`, `#Linux kernel`, `#git`, `#server operations`, `#resource management`

---

<a id="item-6"></a>
## [OpenAI Chief Scientist Advocates for Defensive AI Development](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 7.0/10

Jakub Pachocki, OpenAI's Chief Scientist, argued in a recent post that rapid AI development is necessary to build defensive systems against AI dangers, while cautioning against recklessness. He emphasized that powerful, aligned AI is needed for defense and that this will be a primary focus of OpenAI's deployment efforts. This statement from a key OpenAI figure signals a strategic direction for the company, potentially influencing AI policy and development priorities. It highlights the tension between advancing AI capabilities and ensuring safety, a central debate in the AI community. Pachocki's comments come from an OpenAI blog post titled 'An Alien Mind,' specifically the section on 'Scalable Defense.' He stresses that defensive systems must secure infrastructure, protect against rogue agents in real time, and invent new protective measures, but warns that the urgency must not excuse recklessness.

rss · Simon Willison · Sep 7, 22:26

**Background**: AI alignment refers to ensuring AI systems act in accordance with human intentions and values. Rogue AI agents are AI systems that act unexpectedly or maliciously, potentially causing harm. OpenAI has been investing in defensive measures, such as secure architecture and cyber defense initiatives, to address these risks.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/the-defenders-window/">The Defender’s Window | OpenAI</a></li>
<li><a href="https://openai.com/collective-cyberdefense/">A call for collective action on cyber defense | OpenAI</a></li>
<li><a href="https://www.lesswrong.com/posts/QWRXnTAfnGigwZhDy/turing-test-passing-ai-implies-aligned-ai">Turing-Test-Passing AI implies Aligned AI — LessWrong</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#AI policy`, `#artificial intelligence`

---

<a id="item-7"></a>
## [DNS Abuse: Up to 20% of New gTLDs Are Scams](https://simonwillison.net/2026/Sep/6/the-purpose-of-dns-is-to-spread-scams/) ⭐️ 7.0/10

A blog post by Terence Eden, cited by Simon Willison, highlights an Interisle report showing that of 85 million new gTLD registrations in 2025, 8.5 million were blocklisted by May 2025, with a likely abuse rate of 10-20%. This statistic underscores a systemic security crisis where DNS, a foundational internet infrastructure, is being exploited at an alarming rate for scams, affecting users, businesses, and trust in online services. It calls for urgent attention from ICANN and policymakers to implement stronger abuse prevention measures. The Interisle report suggests that a 10% abuse rate is the likely floor, with the real figure possibly closer to 20%, meaning one in five newly registered gTLD domains could be scams. ICANN has reportedly discussed this issue for years without effective resolution.

rss · Simon Willison · Sep 6, 14:40

**Background**: The Domain Name System (DNS) translates human-readable domain names into IP addresses, and generic top-level domains (gTLDs) are categories like .com, .org, and newer ones. ICANN oversees the DNS root zone and coordinates domain name assignments, but its contractual requirements for abuse prevention are minimal, allowing cybercriminals to easily register domains for phishing and other scams. Blocklists are used to identify and mitigate abusive domains, but they only capture a fraction of the problem.

<details><summary>References</summary>
<ul>
<li><a href="https://www.einnews.com/pr_news/916015197/interisle-study-finds-malicious-actors-accounted-for-10-20-of-new-domain-name-registrations-in-2025">Interisle Study Finds Malicious Actors Accounted for 10-20% of New...</a></li>
<li><a href="https://gac.icann.org/presentations/public/Interisle+GAC+Presentation+June+2025.pdf">Phishing and Domain Abuse</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, but the discussion likely revolves around the severity of DNS abuse and criticism of ICANN's slow response. Commenters may debate the accuracy of the statistics and propose solutions such as mandatory identity verification for domain registrants.

**Tags**: `#DNS`, `#cybersecurity`, `#scams`, `#ICANN`, `#internet governance`

---

<a id="item-8"></a>
## [Why Rewriting Software from Scratch Usually Fails](https://simonwillison.net/2026/Sep/6/theres-no-limit-to-how-bad-code-can-get/) ⭐️ 7.0/10

Simon Willison shared his experience-based argument on Lobste.rs that rewriting legacy software from scratch rarely succeeds, explaining the 'moving target' problem and lack of developer incentives. He recommends shoring up the old system with automated tests and targeted refactors instead. This commentary addresses a common dilemma in software engineering: whether to rewrite or incrementally improve legacy systems. Willison's pragmatic perspective can help teams avoid costly failed rewrites and manage technical debt more effectively, impacting project success and resource allocation. Willison notes that during a rewrite, the old system continues to evolve, and its developers lack incentive to improve it, leading to mounting tech debt. The new system often ships incomplete, resulting in two production systems, and he cites Will Larson's article 'Migrations: the sole scalable fix to tech debt' as a responsible approach.

rss · Simon Willison · Sep 6, 09:08

**Background**: Technical debt refers to the implied cost of additional rework caused by choosing an easy solution now instead of a better approach that would take longer. Rewriting from scratch is often tempting when code becomes unmanageable, but it carries risks such as losing business logic and underestimating complexity. Will Larson's article advocates for incremental migrations as a more scalable fix.

**Tags**: `#software engineering`, `#technical debt`, `#rewrite`, `#legacy systems`, `#project management`

---

<a id="item-9"></a>
## [Seattle Times and Newsday Sue OpenAI and Microsoft for Copyright Infringement](https://www.theverge.com/ai-artificial-intelligence/990932/seattle-times-newsday-lawsuit-openai-microsoft) ⭐️ 7.0/10

The Seattle Times and Newsday have filed a copyright infringement lawsuit against OpenAI and Microsoft, alleging unauthorized use of their journalism in AI training data and reproduction of passages in AI responses. This lawsuit adds to the growing legal pressure on AI companies over training data practices, potentially shaping future copyright law and licensing agreements between news organizations and AI developers. The outlets claim OpenAI's AI models reproduce passages from their reporting in response to user queries, similar to other lawsuits filed by media entities. The case targets both OpenAI and its major investor Microsoft.

rss · The Verge · Sep 6, 23:36

**Background**: AI models like OpenAI's GPT are trained on vast amounts of text data, often scraped from the internet without explicit permission from content creators. News organizations have increasingly sued AI companies, arguing that such use infringes copyright and undermines their business models.

**Tags**: `#AI`, `#copyright`, `#legal`, `#OpenAI`, `#Microsoft`

---

<a id="item-10"></a>
## [Tiny Recurrent System Autonomously Generates Bad Apple Video from Single State](https://www.reddit.com/r/MachineLearning/comments/1wa8rub/generating_bad_apple_autonomously_from_a_single/) ⭐️ 7.0/10

A researcher trained a compact recurrent dynamical system with only 417,129 parameters to autonomously generate the entire ~6,500-frame Bad Apple video from a single initial state (h_0, c_0), without any timestamp inputs during inference. The system runs at over 200 FPS on an RTX 4080 and the code, weights, and analysis tools are publicly available on GitHub. This work demonstrates that a very small recurrent system can learn to generate a long, complex sequence autonomously, which could inspire more efficient approaches to video generation and sequence modeling. It also highlights the potential of dynamical systems and curriculum learning for training stable long-horizon generators, which may benefit fields like procedural content generation and neural animation. The architecture uses a 64-dimensional latent state, a 4-gate LSTM-style recurrent transition (CTF) with orthogonal initialization, and a frame decoder with bilinear upsampling and depthwise-separable convolutions. Training employed learned latent teacher tables, a rollout horizon curriculum (K doubling from 2 to 512), state perturbation noise, second-difference acceleration regularization, and chunked decoding to manage memory.

reddit · r/MachineLearning · /u/SEBADA321 · Sep 8, 00:05

**Background**: The work builds on prior research using SIREN (a neural network with periodic activation functions) to implicitly represent videos as coordinate functions mapping (t, y, x) to pixel values. In contrast, this project replaces the explicit time input with a recurrent dynamical system that learns the temporal flow in latent space, enabling autonomous generation from a single initial condition. The Bad Apple video is a famous black-and-white shadow art music video originally created in 2009, often used as a benchmark for video processing tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.vincentsitzmann.com/siren/">Implicit Neural Representations with Periodic Activation Functions</a></li>
<li><a href="https://arxiv.org/pdf/1810.02363">Recurrent Transition Networks for Character Locomotion</a></li>
<li><a href="https://grokipedia.com/page/Bad_Apple_shadow_art_music_video">Bad Apple!! (shadow art music video)</a></li>

</ul>
</details>

**Tags**: `#recurrent neural networks`, `#video generation`, `#dynamical systems`, `#machine learning`, `#autonomous generation`

---

<a id="item-11"></a>
## [Rustuna: High-Performance Rust Implementation of Optuna Released](https://www.reddit.com/r/MachineLearning/comments/1w9nyhz/rustuna_a_highperformance_rust_implementation_of/) ⭐️ 7.0/10

The Optuna team has released Rustuna, a high-performance Rust implementation of Optuna that maintains API compatibility while eliminating Python dependencies and reducing memory footprint. It is available on GitHub and detailed in a Medium blog post. Rustuna addresses critical concerns in the ML ecosystem, such as supply chain attacks and memory efficiency, by leveraging Rust's safety and performance. This could enable broader adoption of Optuna in production environments where Python dependencies are a liability, and it signals a trend toward more robust, language-agnostic ML tooling. Rustuna retains the familiar Optuna API and concept, ensuring a smooth transition for existing users. It is built natively in Rust, which contributes to its lower memory footprint and zero Python dependencies, mitigating supply chain risks.

reddit · r/MachineLearning · /u/c-bata · Sep 7, 10:01

**Background**: Optuna is a popular automatic hyperparameter optimization framework designed for machine learning, known for its define-by-run API and integration with various ML libraries. Rust is a systems programming language that emphasizes performance, type safety, concurrency, and memory safety, making it an attractive choice for building high-performance, secure tools. Rustuna leverages these Rust features to provide a more efficient and secure alternative to the original Python-based Optuna.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Optuna">Optuna - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language) - Wikipedia</a></li>
<li><a href="https://github.com/optuna/optuna">GitHub - optuna/optuna: A hyperparameter optimization framework · GitHub</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Optuna`, `#Hyperparameter Optimization`, `#Machine Learning`, `#Performance`

---