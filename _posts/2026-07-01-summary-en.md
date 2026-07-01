---
layout: default
title: "Horizon Summary: 2026-07-01 (EN)"
date: 2026-07-01
lang: en
---

> From 84 items, 15 important content pieces were selected

---

1. [Realta Fusion claims first direct electricity from fusion](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Claude Sonnet 5](#item-2) ⭐️ 8.0/10
3. [Claude Code secretly embeds steganographic markers in requests](#item-3) ⭐️ 8.0/10
4. [Anthropic Launches Claude Science for Researchers](#item-4) ⭐️ 8.0/10
5. [OpenAI Launches GeneBench-Pro for Genomics AI](#item-5) ⭐️ 8.0/10
6. [OpenAI Fixes 18-Year-Old Bug via Core Dump Epidemiology](#item-6) ⭐️ 8.0/10
7. [Ornith-1.0: Open-Source LLM Achieves SOTA in Agentic Coding](#item-7) ⭐️ 8.0/10
8. [AI chip startup Etched hits $5B valuation, $1B in sales](#item-8) ⭐️ 8.0/10
9. [Tesla Tests Cybercab Without Steering Wheel in Austin](#item-9) ⭐️ 8.0/10
10. [Arcturus uses laser-infused nano-copper to halve grid losses](#item-10) ⭐️ 8.0/10
11. [Amazon Launches $1B FDE Org for AI Agent Deployment](#item-11) ⭐️ 8.0/10
12. [Anthropic's Claude Fable 5 Greenlit to Return](#item-12) ⭐️ 8.0/10
13. [Meta's Brain2Qwerty v2 Decodes Sentences from Non-Invasive Brain Signals](#item-13) ⭐️ 8.0/10
14. [Anthropic SDK Python v0.115.0 Adds Managed Agents Streaming](#item-14) ⭐️ 7.0/10
15. [shot-scraper video: Record agent demos with Playwright](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Realta Fusion claims first direct electricity from fusion](https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/) ⭐️ 9.0/10

Realta Fusion announced it has generated electricity directly from a fusion reaction, bypassing the traditional steam turbine process. This appears to be a first in the fusion energy field. Direct electricity generation from fusion could significantly improve reactor economics and efficiency, accelerating the path to commercial fusion power. It represents a major milestone in clean energy technology. The company uses its CoSMo fusion system, which employs innovative plasma confinement and heating methods. CEO Kieran Furlong stated that harvesting electricity directly from the plasma 'really helps with the economics' of reactor design.

rss · TechCrunch · Jun 30, 19:12

**Background**: Traditional fusion power plants would use heat from fusion reactions to produce steam and drive turbines, similar to conventional nuclear or fossil fuel plants. Direct energy conversion, which captures charged particles from the fusion plasma to generate electricity without a thermal cycle, has been theorized for decades but never demonstrated at scale. Realta Fusion's breakthrough brings this concept closer to reality.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/realta-fusion-generates-electricity-directly-from-a-fusion-reaction-an-apparent-first/">Realta Fusion generates electricity directly from a fusion ...</a></li>
<li><a href="https://realtafusion.com/">Realta Fusion | Compact, Scalable, Modular – CoSMo fusion ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Direct_energy_conversion">Direct energy conversion - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#fusion energy`, `#breakthrough`, `#clean energy`, `#nuclear fusion`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 8.0/10

Anthropic has released Claude Sonnet 5, a faster and more agentic model that can plan, use tools, and run autonomously. It offers competitive performance but with nuanced cost-efficiency trade-offs compared to the larger Opus model. This release advances agentic AI capabilities in a smaller, faster package, potentially making autonomous AI assistants more accessible. However, the cost-performance trade-offs mean users must carefully choose between Sonnet 5 and Opus based on their specific use cases. On benchmarks, Sonnet 5 wins Terminal-Bench and ties Opus on knowledge work at 40-60% lower cost, but Opus leads on coding, terminal use, computer use, and reasoning by small margins. Community benchmarks show Sonnet 5 has weak spots in trivia, combined tool-calling tasks, and puzzle solving.

hackernews · marinesebastian · Jun 30, 17:59 · [Discussion](https://news.ycombinator.com/item?id=48736605)

**Background**: Agentic AI refers to systems that can act autonomously, using tools, memory, planning, and feedback loops to accomplish complex tasks. Claude Sonnet 5 is designed to be the most agentic Sonnet model yet, capable of making plans and using browsers and terminals autonomously.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/blog/research/claude-sonnet-5-vs-claude-opus-4-8">Claude Sonnet 5 vs Claude Opus 4.8: The Complete Comparison</a></li>
<li><a href="https://claudefa.st/blog/models/claude-sonnet-5-vs-opus-4-8">Claude Sonnet 5 vs Opus 4.8: Benchmarks & Price</a></li>
<li><a href="https://agentic.ai/what-is-agentic-ai">What Is Agentic AI? Definition, 6 Levels & Examples (2026)</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that Sonnet 5's cost per task often exceeds Opus at higher effort levels, leading some to question when to use it. Others note its speed and agentic capabilities, but express concerns about regressions in certain tasks like vulnerability discovery.

**Tags**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#agentic`

---

<a id="item-3"></a>
## [Claude Code secretly embeds steganographic markers in requests](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

A developer discovered that Anthropic's Claude Code tool embeds steganographic markers in its API requests to identify usage, likely to detect model distillation by Chinese firms, without transparent disclosure to users. This raises significant transparency and trust concerns for a widely-used AI coding tool, as users may unknowingly have their requests tracked in a hidden manner. It also highlights the growing tension between protecting proprietary models and respecting user privacy. The steganographic markers are embedded in the text of requests sent to Anthropic's API, making them difficult to detect without reverse engineering. The technique is reminiscent of 'underhanded code' and appears designed to bypass custom API gateways that might strip explicit telemetry.

hackernews · kirushik · Jun 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=48734373)

**Background**: Steganography is the practice of hiding messages within other data, such as text or images, to avoid detection. Model distillation is a technique where a smaller model is trained to mimic a larger one, often used to replicate proprietary AI capabilities. Companies like Anthropic may use steganographic markers to identify unauthorized distillation attempts by detecting patterns in API traffic.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.03439">[2505.03439] The Steganographic Potentials of Language Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2510.04850">[2510.04850] Detecting Distillation Data from Reasoning Models Knowledge Distillation Detection for Open-weights Models GitHub - liuxiaotong/model-audit: LLM distillation detection ... GitHub - autodistill/autodistill: Images to inference with no ... Knowledge distillation - Wikipedia Knowledge Distillation Tutorial — PyTorch Tutorials 2.12.0 ...</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some downplay the severity, arguing the intent is clearly to detect Chinese model distillation and does not harm normal developers. Others criticize the lack of transparency and worry about what else might be hidden, while some suggest using open-source alternatives like Codex CLI to avoid such practices.

**Tags**: `#steganography`, `#AI ethics`, `#transparency`, `#Claude Code`, `#security`

---

<a id="item-4"></a>
## [Anthropic Launches Claude Science for Researchers](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic has launched Claude Science, an AI workbench designed specifically for scientists and researchers, integrating with local servers, databases, and HPC clusters. This tool addresses the critical need for secure, integrated AI in data-intensive fields like pharma and computational biology, potentially accelerating research workflows. Claude Science runs a local server with a web-based UI, enabling secure connections to institutional data sources without exposing them to the cloud.

hackernews · lebovic · Jun 30, 17:07 · [Discussion](https://news.ycombinator.com/item?id=48735770)

**Background**: Many research environments, especially in pharma, are heavily locked down, preventing direct cloud connections. Claude Science's local-server architecture allows researchers to use AI on sensitive data while maintaining compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://www.statnews.com/2026/06/30/anthropic-release-claude-science-ceo-dario-amodei/">Anthropic releases Claude Science, a product aimed at researchers, the pharma industry</a></li>
<li><a href="https://techcrunch.com/2026/06/30/anthropics-claude-science-bets-on-workflow-not-a-new-model-to-win-over-scientists/">Anthropic’s Claude Science bets on workflow, not a new model, to win over scientists | TechCrunch</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the tool's potential for real-world research, with one user noting successful use in designing RNAi biopesticides, though with caveats about naive approaches. Another commenter raised concerns about LLMs generating fake data, questioning how Claude Science prevents such hallucinations.

**Tags**: `#AI`, `#Data Science`, `#Scientific Computing`, `#Anthropic`, `#HPC`

---

<a id="item-5"></a>
## [OpenAI Launches GeneBench-Pro for Genomics AI](https://openai.com/index/introducing-genebench-pro) ⭐️ 8.0/10

OpenAI introduced GeneBench-Pro, an expanded benchmark for evaluating AI agents on complex, multi-stage scientific analyses in genomics, quantitative biology, and translational biomedicine. This benchmark addresses the need for realistic evaluation of AI in scientific discovery, potentially accelerating research in personalized medicine and genomics by providing a standardized test for multi-step reasoning. GeneBench-Pro includes harder problems across a wider breadth of domains compared to its predecessor GeneBench, and is designed to capture the complexity of real-world problems that computational life scientists face.

rss · OpenAI Blog · Jun 30, 00:00

**Background**: Existing biology benchmarks often focus on knowledge retrieval or single-step tasks, whereas real scientific research requires multi-stage reasoning. GeneBench-Pro aims to fill this gap by testing AI agents on realistic multi-stage analyses.

<details><summary>References</summary>
<ul>
<li><a href="https://www.biorxiv.org/content/10.64898/2026.06.29.735386v1">GeneBench-Pro: Evaluating Multistage Statistical Reasoning ...</a></li>
<li><a href="https://cdn.openai.com/pdf/21938268-21af-442f-af93-3b2249afb241/genebench-pro.pdf">GeneBench-Pro:EvaluatingMultistageStatisticalReasoning ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#benchmark`, `#genomics`, `#biology`, `#OpenAI`

---

<a id="item-6"></a>
## [OpenAI Fixes 18-Year-Old Bug via Core Dump Epidemiology](https://openai.com/index/core-dump-epidemiology-data-infrastructure-bug) ⭐️ 8.0/10

OpenAI engineers published a white paper detailing their 'core dump epidemiology' methodology, which they used to debug rare infrastructure crashes and uncovered both a hardware fault and an 18-year-old software bug. This novel approach to large-scale crash analysis could transform debugging practices for distributed systems, improving reliability across the AI industry and beyond. The methodology leverages large-scale core dump analysis to correlate crash patterns across thousands of machines, enabling the identification of root causes that are invisible in isolated incidents.

rss · OpenAI Blog · Jun 30, 00:00

**Background**: Core dumps are snapshots of a program's memory at the time of a crash, typically analyzed individually using tools like GDB. OpenAI's approach treats them as epidemiological data, aggregating and analyzing patterns across many crashes to find systemic issues.

<details><summary>References</summary>
<ul>
<li><a href="https://www.siliconreport.com/openai-details-core-dump-epidemiology-for-infrastructure-debugging-8b6d27b1">OpenAI Details 'Core Dump Epidemiology' for Infrastructure ...</a></li>
<li><a href="https://stackoverflow.com/questions/8305866/how-do-i-analyze-a-programs-core-dump-file-with-gdb-when-it-has-command-line-pa">linux - How do I analyze a program's core dump file with GDB ... Code sample</a></li>
<li><a href="https://dzone.com/articles/debugging-core-dump-files-on-linux-a-detailed-guid">Debugging Linux Core Dump Files: A Detailed Guide - DZone</a></li>

</ul>
</details>

**Tags**: `#debugging`, `#infrastructure`, `#core dump`, `#systems engineering`, `#OpenAI`

---

<a id="item-7"></a>
## [Ornith-1.0: Open-Source LLM Achieves SOTA in Agentic Coding](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of open-weight LLMs (MIT license) for agentic coding, with sizes from 9B to 397B parameters, built on Gemma 4 and Qwen 3.5 (both Apache 2.0). It achieves state-of-the-art performance among open-source models of comparable size on coding benchmarks. This release provides a powerful, permissively licensed alternative for autonomous coding agents, potentially accelerating AI-assisted software development. Its self-scaffolding training approach—where the model learns to generate its own task-specific harnesses—represents a novel paradigm that could improve agentic capabilities across the field. The model family includes 9B Dense, 31B Dense, 35B MoE, and 397B MoE variants, with the 35B GGUF (20GB) already usable via LM Studio. Early user tests show proficient multi-step tool calling, e.g., navigating a codebase to find specific functions.

rss · Simon Willison · Jun 29, 16:17

**Background**: Agentic coding refers to AI agents that autonomously plan, write, test, and modify code with minimal human intervention. Traditional LLM coding assistants rely on human-designed harnesses to structure tasks; Ornith-1.0's self-scaffolding innovation allows the model to generate its own task-specific harnesses during reinforcement learning, improving solution quality.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://simonwillison.net/2026/Jun/29/ornith/">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding</a></li>
<li><a href="https://www.mindstudio.ai/blog/self-scaffolding-ai-models-ornith-1-0">Self-Scaffolding AI Models: How Ornith 1.0 Writes Its Own Agent Harness | MindStudio</a></li>

</ul>
</details>

**Discussion**: No community comments were provided in the news item.

**Tags**: `#LLM`, `#coding`, `#open-source`, `#AI`, `#agentic`

---

<a id="item-8"></a>
## [AI chip startup Etched hits $5B valuation, $1B in sales](https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/) ⭐️ 8.0/10

Etched, an AI chip startup, announced it has secured over $1 billion in contracts for its inference systems and achieved a $5 billion valuation, emerging from stealth with a working chip. This marks a significant milestone for a challenger to Nvidia's dominance in AI inference hardware, signaling strong market demand for specialized chips that optimize transformer-based models. Etched's chip is designed exclusively for transformer models, which power most modern AI systems like GPT-4, potentially offering higher efficiency and lower cost for inference workloads.

rss · TechCrunch · Jun 30, 18:13

**Background**: AI inference is the process of using a trained model to make predictions on new data, which is computationally intensive for large models. Most AI chips today, like Nvidia's GPUs, are general-purpose and handle both training and inference, but specialized chips like Etched's aim to optimize inference for specific model architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/30/nvidia-competitor-etched-hits-5b-valuation-1b-in-sales-for-ai-chip/">Nvidia competitor Etched hits $5B valuation, $1B in sales for ...</a></li>
<li><a href="https://techcrunch.com/2024/06/25/etched-is-building-an-ai-chip-that-only-runs-transformer-models/">Etched is building an AI chip that only runs one type of model</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#Nvidia competitor`, `#inference hardware`, `#startup funding`, `#AI infrastructure`

---

<a id="item-9"></a>
## [Tesla Tests Cybercab Without Steering Wheel in Austin](https://techcrunch.com/2026/06/30/tesla-starts-testing-cybercab-without-pedals-or-a-steering-wheel-in-austin/) ⭐️ 8.0/10

Tesla has begun testing its Cybercab, a fully autonomous vehicle without pedals or a steering wheel, on public roads in Austin, Texas. This marks a concrete step toward launching a commercial robotaxi network. This testing brings Tesla closer to fulfilling Elon Musk's long-standing promise of a robotaxi network, which could disrupt the ride-hailing industry. Success would position Tesla as a leader in autonomous mobility, competing with Waymo and Zoox. The Cybercab is a two-passenger electric vehicle designed without manual controls, relying entirely on Tesla's Full Self-Driving (FSD) software. EPA documents suggest it has a roughly 50-kWh battery pack and nearly 280 miles of range.

rss · TechCrunch · Jun 30, 15:32

**Background**: Tesla unveiled the Cybercab concept in October 2024 and launched a limited robotaxi service in Austin in June 2025 using existing vehicles. The Cybercab is purpose-built for autonomous ride-hailing, unlike retrofitted cars. Competitors like Waymo and Zoox are also testing purpose-built robotaxis.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Cybercab">Tesla Cybercab - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>
<li><a href="https://www.caranddriver.com/news/a71590701/tesla-cybercab-specs-epa-documents-revealed/">We Have New Tesla Cybercab Specs Before You're Supposed to See Them Thanks to EPA Documents</a></li>

</ul>
</details>

**Tags**: `#autonomous vehicles`, `#Tesla`, `#robotaxi`, `#transportation`

---

<a id="item-10"></a>
## [Arcturus uses laser-infused nano-copper to halve grid losses](https://techcrunch.com/2026/06/30/arcturus-could-halve-the-grids-electrical-losses-using-its-nano-infused-copper/) ⭐️ 8.0/10

Stealthy startup Arcturus has developed a laser-based process to infuse carbon nanomaterials into copper, creating a composite that could reduce electrical grid losses by up to 50%. If scaled, this breakthrough could dramatically improve global energy efficiency, reduce electricity costs, and lower carbon emissions by upgrading existing grid infrastructure without replacing entire systems. The company's website lists applications in motorsports, drones, robotics, electric motors, data centers, and power infrastructure, suggesting the material is versatile beyond grid use.

rss · TechCrunch · Jun 30, 15:01

**Background**: Electrical grid losses occur due to resistance in copper wires, wasting about 5-10% of generated electricity. Carbon nanomaterials like carbon nanotubes have extremely high electrical conductivity, but integrating them into bulk metals has been challenging. Arcturus uses lasers to embed these nanomaterials into copper, enhancing conductivity without compromising mechanical properties.

<details><summary>References</summary>
<ul>
<li><a href="https://arcturus.io/">Arcturus | Metals Infused with Advanced Carbon Nanomaterials</a></li>

</ul>
</details>

**Tags**: `#energy`, `#materials science`, `#nanotechnology`, `#grid efficiency`

---

<a id="item-11"></a>
## [Amazon Launches $1B FDE Org for AI Agent Deployment](https://techcrunch.com/2026/06/30/amazon-launches-new-1-billion-fde-org-following-openai-and-anthropic/) ⭐️ 8.0/10

Amazon Web Services (AWS) announced a new $1 billion Forward-Deployed Engineering (FDE) organization that embeds engineers directly within customer companies to build and deploy purpose-built AI agents, with a focus on fast deployments and enabling customer self-sufficiency. This move signals a major industry trend toward specialized, on-site AI agent deployment, following similar initiatives by OpenAI and Anthropic, and could reshape how enterprise AI services are delivered, emphasizing speed and customer independence. The FDE model, popularized by Palantir, puts primary deployment responsibility with the contractor while transferring engineering capabilities to the customer. AWS's FDE teams are already working with clients including the Allen Institute, Cox Automotive, NBA, NFL, and Ricoh.

rss · TechCrunch · Jun 30, 15:00

**Background**: Purpose-built AI agents are specialized AI systems focused on a single job, such as lead nurturing or customer service deflection, and can take action autonomously. The FDE approach involves embedding engineers on-site to accelerate deployment and ensure long-term customer self-sufficiency, contrasting with traditional consulting models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.moneycontrol.com/artificial-intelligence/aws-joins-openai-anthropic-in-building-fde-teams-with-1-billion-investment-article-13962633.html">AWS joins OpenAI, Anthropic in building FDE teams with $1 ...</a></li>
<li><a href="https://cryptobriefing.com/amazon-1b-fde-ai-agents/">Amazon launches $1B FDE organization to deploy AI agents ...</a></li>
<li><a href="https://ainave.com/tech-news/aws-fde-1b-to-embed-agentic-ai-on-site-in-45-days">AWS FDE: $1B forward-deployed engineering for agentic AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Amazon`, `#enterprise`, `#agents`, `#investment`

---

<a id="item-12"></a>
## [Anthropic's Claude Fable 5 Greenlit to Return](https://www.theverge.com/ai-artificial-intelligence/958964/anthropic-claude-fable-5-is-back) ⭐️ 8.0/10

Anthropic announced that the Department of Commerce has lifted export controls on Claude Fable 5 and Claude Mythos 5, allowing the models to be restored online starting tomorrow after weeks of negotiations with the Trump administration. This marks a major policy shift regarding AI export controls, enabling Anthropic to deploy its advanced AI models for cybersecurity and coding tasks, which could accelerate AI adoption in critical sectors. Claude Fable 5 is the same underlying model as Mythos 5 but with robust safeguards for cybersecurity and biology, and queries in those domains are automatically routed to Opus 4.8.

rss · The Verge · Jul 1, 00:03

**Background**: Claude Fable 5 and Claude Mythos 5 are large language models developed by Anthropic to find and fix vulnerabilities in software. They were previously sidelined due to export controls amid safety and misuse concerns. The lifting of controls follows negotiations with the Trump administration, indicating a shift in regulatory stance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#export controls`, `#Claude`, `#policy`

---

<a id="item-13"></a>
## [Meta's Brain2Qwerty v2 Decodes Sentences from Non-Invasive Brain Signals](https://www.producthunt.com/products/meta) ⭐️ 8.0/10

Meta FAIR released Brain2Qwerty v2, a system that decodes full typed sentences from non-invasive MEG brain recordings with a 39% average word error rate, and 22% for the best participant. This marks a significant advancement in non-invasive brain-computer interfaces, bringing us closer to practical communication aids for patients with severe motor impairments without requiring surgery. Brain2Qwerty v2 decodes sentences asynchronously from a continuous MEG window, without segmenting around individual keystrokes, achieving 61% word accuracy in real-time decoding.

rss · Product Hunt (AI应用) · Jun 30, 04:22

**Background**: Brain-computer interfaces (BCIs) aim to translate brain activity into commands. Non-invasive methods like MEG (magnetoencephalography) measure magnetic fields from neural activity without implants, but decoding language from such signals has been challenging. Previous work required invasive electrodes or segmented recordings.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/facebookresearch/brain2qwerty/blob/main/brain2qwerty_v2/README.md">brain2qwerty/brain2qwerty_v2/README.md at main ... - GitHub</a></li>
<li><a href="https://explainx.ai/blog/meta-brain2qwerty-v2-non-invasive-brain-to-text-decoder-2026">Meta Brain2Qwerty v2: Reading Your Thoughts Without Surgery</a></li>
<li><a href="https://o-mega.ai/articles/brain2qwerty-v2-the-2026-brain-to-text-guide">Brain2Qwerty v2: 2026 Brain-to-Text Guide | Articles | o-mega</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#AI`, `#neuroscience`, `#non-invasive`, `#decoding`

---

<a id="item-14"></a>
## [Anthropic SDK Python v0.115.0 Adds Managed Agents Streaming](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.115.0) ⭐️ 7.0/10

Anthropic released version 0.115.0 of the anthropic-sdk-python on June 30, 2026, adding support for Managed Agents event delta streaming, agent overrides, reverse pagination, vault credential injection scoping, and agent/deployment webhook events. These features enhance real-time monitoring and control of Managed Agents, improve API usability with reverse pagination, and strengthen security through scoped credential injection, benefiting developers building complex agent workflows. The release includes a single commit (8c23f7e) that bundles all new API features. The previous version v0.114.0 added support for claude-sonnet-5 and fixed an agent_toolset bug allowing absolute paths within the workdir.

github · stainless-app[bot] · Jun 30, 19:47

**Background**: Managed Agents are AI agents that can perform tasks autonomously within a session. Event delta streaming allows clients to receive real-time updates as the agent executes, while reverse pagination enables fetching results from the end of a list. Vault credential injection scoping restricts which credentials an agent can access, improving security.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/managed-agents/events-and-streaming">Session event stream - Claude Platform Docs</a></li>
<li><a href="https://apidog.com/blog/pagination-in-rest-apis/">How to Implement Pagination in REST APIs (Step by Step Guide)</a></li>
<li><a href="https://docs.beyondtrust.com/rs/docs/injection">Credential injection | RS</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#SDK`, `#Python`, `#API`, `#Managed Agents`

---

<a id="item-15"></a>
## [shot-scraper video: Record agent demos with Playwright](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 7.0/10

Simon Willison released shot-scraper 1.10 with a new `shot-scraper video` command that accepts a `storyboard.yml` file and uses Playwright to record a video of a web application routine. This tool enables coding agents to produce visual demos of their work, addressing a critical need for verifying and showcasing agent-generated code in AI-assisted development workflows. The `storyboard.yml` file defines server setup, viewport, cursor visibility, JavaScript overrides (e.g., clipboard mocking), and a sequence of scenes with actions like clicks and pauses. The command supports `--auth` for authenticated sessions and outputs video in WebM or MP4 format.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a command-line tool for taking screenshots of web pages using Playwright, an open-source browser automation library by Microsoft. The new video command extends shot-scraper to record full screen recordings, making it easier for developers and AI agents to create reproducible demos of web interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot ...</a></li>
<li><a href="https://letsdatascience.com/news/shot-scraper-launches-video-command-in-110-07962b66">shot-scraper launches video command in 1.10 | Let's Data Science</a></li>
<li><a href="https://digg.com/tech/46k6q4wt">Shot-Scraper Adds Video Recording Support Using YAML ...</a></li>

</ul>
</details>

**Tags**: `#developer-tools`, `#testing`, `#automation`, `#playwright`, `#ai-agents`

---