---
layout: default
title: "Horizon Summary: 2026-06-19 (EN)"
date: 2026-06-19
lang: en
---

> From 85 items, 15 important content pieces were selected

---

1. [10,000 GitHub Repos Found Distributing Trojan Malware](#item-1) ⭐️ 9.0/10
2. [GLM-5.2: Most Powerful Open-Weight Text LLM Released](#item-2) ⭐️ 9.0/10
3. [TypeScript 7.0 RC Released with New Features](#item-3) ⭐️ 9.0/10
4. [OpenAI AI Helps Diagnose 18 Rare Genetic Diseases in Children](#item-4) ⭐️ 8.0/10
5. [AI Chemist Using GPT-5.4 Improves Drug-Making Reaction](#item-5) ⭐️ 8.0/10
6. [AI Demands More Engineering Discipline, Says Charity Majors](#item-6) ⭐️ 8.0/10
7. [OpenAI Hires Transformer Co-Inventor and Ex-Trump AI Policy Aide](#item-7) ⭐️ 8.0/10
8. [Amazon AWS to sell AI chips, challenging Nvidia directly](#item-8) ⭐️ 8.0/10
9. [FERC mandates fast-track grid interconnections for AI data centers](#item-9) ⭐️ 8.0/10
10. [Texas Data Breach Exposes 3M Driver's Licenses, Passports](#item-10) ⭐️ 8.0/10
11. [General Intuition seeks $300M at $2B valuation for embodied AI](#item-11) ⭐️ 8.0/10
12. [Amazon Employees Face Termination for Supporting Data Center Limits](#item-12) ⭐️ 8.0/10
13. [Merkle Tree Certificates: Faster, Safer Internet](#item-13) ⭐️ 8.0/10
14. [Anthropic SDK Python v0.110.0 Adds Code Execution Tool](#item-14) ⭐️ 7.0/10
15. [Cornell CS 6120 Advanced Compilers Now Self-Guided Online](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [10,000 GitHub Repos Found Distributing Trojan Malware](https://orchidfiles.com/github-repositories-distributing-malware/) ⭐️ 9.0/10

A researcher discovered over 10,000 GitHub repositories distributing Trojan malware, exploiting automated agents and search rankings to infect users. The repositories have been active for months, and GitHub has not automatically detected them. This widespread security threat highlights the vulnerability of open-source platforms to supply chain attacks, potentially affecting millions of developers and organizations. The scale of the campaign underscores the need for better automated detection and community vigilance. Each repository contains a zip archive with a Trojan, and the attacker deletes and re-pushes commits every few hours to stay at the top of search results. The researcher published a complete list of these repositories on GitHub.

hackernews · theorchid · Jun 18, 11:45 · [Discussion](https://news.ycombinator.com/item?id=48583928)

**Background**: GitHub is a popular platform for hosting open-source code, but its automated agents and search rankings can be exploited by attackers to distribute malware. Supply chain attacks on open-source platforms have more than doubled in 2025, with over 70% of organizations reporting incidents. This campaign targets automated agents that clone repositories for dependency management, rather than human users.

<details><summary>References</summary>
<ul>
<li><a href="https://orchidfiles.com/github-repositories-distributing-malware/">How I found 10,000 GitHub repositories distributing Trojan malware</a></li>
<li><a href="https://thehackernews.com/2025/06/67-trojanized-github-repositories-found.html">200+ Trojanized GitHub Repositories Found in Campaign Targeting Gamers and Developers</a></li>
<li><a href="https://www.mcafee.com/blogs/other-blogs/mcafee-labs/astaroth-banking-trojan-abusing-github-for-resilience/">Astaroth: Banking Trojan Abusing GitHub for Resilience | McAfee Blog</a></li>

</ul>
</details>

**Discussion**: Community members shared personal experiences of their names being attached to malicious repositories, and noted that the attack targets automated agents rather than humans. Some discussed the tactic of frequently updating commits to appear in 'Last Updated' searches, and referenced a real-world case where a Disney engineer was infected via a GitHub tool.

**Tags**: `#security`, `#malware`, `#GitHub`, `#supply chain attack`, `#open source`

---

<a id="item-2"></a>
## [GLM-5.2: Most Powerful Open-Weight Text LLM Released](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Z.ai released GLM-5.2, a 753B-parameter open-weights LLM with a 1M token context window and MIT license, on June 16, 2026. It uses a Mixture of Experts architecture with 40B active parameters and is currently the top-ranked open-weights model on the Artificial Analysis Intelligence Index. GLM-5.2 sets a new benchmark for open-weights LLMs, outperforming previous leaders like MiniMax-M3 and DeepSeek V4 Pro on independent benchmarks. Its MIT license and strong performance make it a significant alternative to proprietary models, potentially accelerating AI research and development. The model is text-only, with a 1.51TB size and 1M token context window, up from 200K in GLM-5.1. It uses more output tokens per task than peers (43k vs 24-37k), and is available via OpenRouter at $1.40/M input and $4.40/M output tokens.

rss · Simon Willison · Jun 17, 23:58

**Background**: Mixture of Experts (MoE) is a machine learning technique that divides tasks among multiple specialized sub-models (experts), with a gating network selecting which experts to use for each input. This allows models like GLM-5.2 to have a large total parameter count while keeping inference efficient by activating only a subset of parameters. Open-weights models make trained parameters publicly available, enabling customization and self-hosting.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.2">GLM-5.2</a></li>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/ GLM - 5 . 2 · Hugging Face</a></li>
<li><a href="https://www.tensorops.ai/post/what-is-mixture-of-experts-llm">LLM Mixture of Experts Explained</a></li>

</ul>
</details>

**Discussion**: The community is highly impressed by GLM-5.2's benchmark performance and open licensing, with many praising its SVG generation capabilities. However, some note its high token usage and the lack of vision input as limitations.

**Tags**: `#LLM`, `#open-weights`, `#AI`, `#GLM-5.2`, `#Mixture of Experts`

---

<a id="item-3"></a>
## [TypeScript 7.0 RC Released with New Features](https://www.reddit.com/r/programming/comments/1u97we9/announcing_typescript_70_rc/) ⭐️ 9.0/10

The TypeScript team has announced the Release Candidate for TypeScript 7.0, a major version update to the JavaScript superset. This RC introduces new features and improvements, though specific details are not provided in the summary. TypeScript 7.0 represents a significant milestone for the language, which is widely used in large-scale JavaScript development. This release may impact millions of developers and influence the broader JavaScript ecosystem. As a Release Candidate, this version is feature-complete and intended for testing before the final stable release. Users are encouraged to try it and report any issues.

reddit · r/programming · /u/DanielRosenwasser · Jun 18, 14:31

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript, adding optional static typing and other features. Major version releases like 7.0 typically include breaking changes and significant new capabilities.

**Tags**: `#TypeScript`, `#programming languages`, `#release`, `#JavaScript`

---

<a id="item-4"></a>
## [OpenAI AI Helps Diagnose 18 Rare Genetic Diseases in Children](https://openai.com/index/diagnose-rare-childhood-diseases) ⭐️ 8.0/10

Researchers used OpenAI's o3 reasoning model to reanalyze 376 unsolved pediatric genetic cases at Boston Children's Hospital, leading to 18 new diagnoses that had eluded specialists. This demonstrates that AI reasoning models can augment human expertise in diagnosing rare diseases, potentially reducing diagnostic delays and improving outcomes for children with undiagnosed genetic conditions. The study involved 376 cases that had previously undergone standard genomic analysis without a diagnosis; the AI model identified 18 new diagnoses by reinterpreting the genomic data. The model used was OpenAI's o3 reasoning model, which has shown superior performance in clinical reasoning tasks.

rss · OpenAI Blog · Jun 18, 08:00

**Background**: Rare genetic diseases affect millions of children worldwide, but diagnosis often takes years due to the complexity of genomic data and the rarity of conditions. AI reasoning models, like OpenAI's o3, are large language models trained to perform step-by-step logical reasoning, which can be applied to medical data analysis. Previous studies have shown that such models can outperform physicians in diagnostic reasoning tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/318662/20260618/ai-rare-disease-diagnoses-openai-o3-solves-18-cases-specialists-could-not.htm">AI Rare Disease Diagnoses: OpenAI o3 Solves 18 Cases ...</a></li>
<li><a href="https://www.beckershospitalreview.com/healthcare-information-technology/ai/boston-childrens-openai-identify-18-rare-disease-diagnoses/">Boston Children’s, OpenAI identify 18 rare disease diagnoses</a></li>

</ul>
</details>

**Tags**: `#AI`, `#healthcare`, `#rare diseases`, `#reasoning model`, `#OpenAI`

---

<a id="item-5"></a>
## [AI Chemist Using GPT-5.4 Improves Drug-Making Reaction](https://openai.com/index/ai-chemist-improves-reaction) ⭐️ 8.0/10

OpenAI and Molecule.one developed a near-autonomous AI chemist that uses GPT-5.4 to improve a challenging reaction in medicinal chemistry. The AI system autonomously designed and executed experiments to optimize the reaction conditions. This advancement demonstrates the potential of AI-driven autonomous experimentation to accelerate drug discovery by reducing the time and cost of optimizing chemical reactions. It could enable chemists to explore more reaction pathways and discover new drugs faster. The AI chemist integrates GPT-5.4 with Molecule.one's autonomous research system 'Maria' to iteratively design, run, and analyze experiments. GPT-5.4, released in March 2026, features improved reasoning and computer use capabilities, enabling it to control lab equipment and interpret results.

rss · OpenAI Blog · Jun 17, 10:00

**Background**: Medicinal chemistry often involves optimizing complex reactions to synthesize drug candidates, a process that is time-consuming and requires expert intuition. AI models like GPT-5.4 can assist by generating hypotheses and planning experiments, but full autonomy in the lab has been a goal. Molecule.one specializes in retrosynthesis prediction, using AI to propose synthetic routes for molecules.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.4">GPT-5.4</a></li>
<li><a href="https://molecule.one/">molecule . one - Making Molecules . Discovering Chemistry</a></li>

</ul>
</details>

**Tags**: `#AI`, `#medicinal chemistry`, `#autonomous experimentation`, `#drug discovery`, `#GPT-5.4`

---

<a id="item-6"></a>
## [AI Demands More Engineering Discipline, Says Charity Majors](https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything) ⭐️ 8.0/10

Charity Majors argues that AI has made code generation cheap and instant, flipping the economics of code production and requiring more engineering discipline, not less. This insight challenges the common narrative that AI reduces the need for rigorous engineering practices, emphasizing that disposable code demands even greater discipline in testing, review, and architecture. Majors notes that lines of code went from being treasured and carefully curated to disposable and regenerable practically overnight in 2025.

rss · Simon Willison · Jun 17, 17:12

**Background**: The news is a quote from Charity Majors, a respected industry figure, on her Substack blog. She discusses how generative AI has transformed software engineering by making code generation nearly free, which paradoxically increases the need for engineering discipline to manage the resulting complexity and quality issues.

**Tags**: `#ai-assisted-programming`, `#software-engineering`, `#generative-ai`, `#engineering-discipline`

---

<a id="item-7"></a>
## [OpenAI Hires Transformer Co-Inventor and Ex-Trump AI Policy Aide](https://techcrunch.com/2026/06/18/openai-is-bringing-on-some-big-guns-in-the-lead-up-to-its-ipo/) ⭐️ 8.0/10

OpenAI has hired Noam Shazeer, co-inventor of the Transformer architecture, from Google DeepMind, and Dean Ball, former Trump administration AI policy official, in the same week ahead of its IPO. These hires signal OpenAI's strategic focus on both cutting-edge AI research and navigating regulatory landscapes as it prepares for its IPO, potentially influencing the future of AI governance and talent competition. Noam Shazeer co-invented the Transformer architecture that underpins modern large language models like GPT-4, while Dean Ball previously served as senior policy advisor for AI at the White House Office of Science and Technology Policy and will join OpenAI as Head of Strategic Futures.

rss · TechCrunch · Jun 18, 19:59

**Background**: The Transformer architecture, introduced in the 2017 paper 'Attention Is All You Need,' revolutionized natural language processing and is the foundation of most modern AI systems. OpenAI, the creator of ChatGPT, is reportedly preparing for an initial public offering (IPO), which would be a major milestone for the AI industry. Hiring key figures from research and policy domains helps the company strengthen its technical leadership and regulatory positioning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Noam_Shazeer">Noam Shazeer - Wikipedia</a></li>
<li><a href="https://www.thefai.org/posts/dean-ball-joins-openai-as-head-of-strategic-futures">Dean Ball Joins OpenAI as Head of Strategic Futures</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#IPO`, `#AI`, `#hiring`, `#policy`

---

<a id="item-8"></a>
## [Amazon AWS to sell AI chips, challenging Nvidia directly](https://techcrunch.com/2026/06/18/amazon-hopes-to-challenge-nvidia-more-directly-by-selling-its-ai-chips/) ⭐️ 8.0/10

Amazon AWS is negotiating to sell its custom AI chips, including Inferentia and Trainium, to other data centers, aiming to directly compete with Nvidia's dominant AI hardware. This move could disrupt Nvidia's near-monopoly in AI chips, potentially lowering costs and increasing options for AI workloads across the industry. CEO Andy Jassy stated this represents a $50 billion opportunity for Amazon. AWS chips are designed for deep learning inference (Inferentia) and training (Trainium).

rss · TechCrunch · Jun 18, 18:22

**Background**: Nvidia currently dominates the AI chip market with its GPUs, used widely for training and inference. AWS has developed its own chips to optimize performance and cost for cloud customers, but previously only offered them through its own cloud services.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/ai/machine-learning/inferentia/">AI Chip - Amazon Inferentia - AWS</a></li>
<li><a href="https://aws.amazon.com/ai/machine-learning/trainium/">AI Accelerator - AWS Trainium - AWS</a></li>

</ul>
</details>

**Tags**: `#AI chips`, `#AWS`, `#Nvidia`, `#hardware`, `#cloud computing`

---

<a id="item-9"></a>
## [FERC mandates fast-track grid interconnections for AI data centers](https://techcrunch.com/2026/06/18/ai-data-centers-just-got-a-government-mandated-fast-lane-to-the-grid/) ⭐️ 8.0/10

The Federal Energy Regulatory Commission (FERC) has ordered grid operators to prioritize AI data center interconnection requests, creating a fast lane for these facilities to connect to the power grid. This policy accelerates AI infrastructure deployment but ignores the underlying electricity supply shortages, potentially straining grid reliability and raising costs for other consumers. The fast lane applies to interconnection requests for new or upgraded capacity resources of at least 250 MW that can come online within three years, with PJM expecting about 10 months per review.

rss · TechCrunch · Jun 18, 17:49

**Background**: AI data centers consume enormous amounts of electricity, driving a surge in power demand that is straining aging grid infrastructure. FERC's 2023 interconnection queue reforms aimed to clear speculative projects, but the new fast lane specifically targets AI facilities without addressing generation adequacy.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/18/ai-data-centers-just-got-a-government-mandated-fast-lane-to-the-grid/">AI data centers just got a government-mandated fast lane to ...</a></li>
<li><a href="https://mgrid.org/2026/06/09/ferc-approves-pjm-fast-track-interconnection-10-projects-a-year-250-mw-minimum-online-within-3-years/">FERC Approves PJM Fast-Track Interconnection: 10 Projects a ...</a></li>
<li><a href="https://ifp.org/interconnection-for-ai/">Fast and Secure Grid Interconnection for American AI ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#data centers`, `#energy policy`, `#infrastructure`, `#regulation`

---

<a id="item-10"></a>
## [Texas Data Breach Exposes 3M Driver's Licenses, Passports](https://techcrunch.com/2026/06/18/texas-government-data-breach-allowed-hackers-to-steal-3-million-drivers-licenses-and-passports/) ⭐️ 8.0/10

A data breach in Texas compromised over 3 million driver's licenses and passports, as reported by TechCrunch on June 18, 2026. This breach exposes millions to identity theft and fraud, highlighting critical vulnerabilities in government data security systems. The stolen data includes highly sensitive government-issued IDs, which can be used for synthetic identity fraud and other crimes. The exact attack vector and timeline remain undisclosed.

rss · TechCrunch · Jun 18, 17:12

**Background**: Government databases often contain personally identifiable information (PII) such as driver's licenses and passport details. Breaches of such data can lead to long-term identity theft, as victims may not discover misuse for years.

**Tags**: `#data breach`, `#cybersecurity`, `#privacy`, `#government`, `#identity theft`

---

<a id="item-11"></a>
## [General Intuition seeks $300M at $2B valuation for embodied AI](https://techcrunch.com/2026/06/18/general-intuition-in-talks-to-raise-300m-at-around-2b-valuation/) ⭐️ 8.0/10

General Intuition is in talks to raise $300 million at a valuation of around $2 billion to train embodied AI and world models using Medal's dataset of 2 billion videos per year from 10 million monthly active users. This significant funding round highlights strong market interest in embodied AI, which could accelerate the development of robots and autonomous systems that learn from real-world video data. The dataset comes from Medal, a platform with 10 million monthly active users generating 2 billion videos annually, providing a massive source of real-world human actions for training AI models.

rss · TechCrunch · Jun 18, 15:20

**Background**: Embodied AI refers to AI systems that perceive and act in the physical world, often through robots or virtual agents. World models are internal predictive models that allow agents to simulate future states of the environment, enabling planning and sample-efficient learning. General Intuition aims to combine these concepts using large-scale video data.

**Tags**: `#embodied AI`, `#funding`, `#world models`, `#robotics`, `#dataset`

---

<a id="item-12"></a>
## [Amazon Employees Face Termination for Supporting Data Center Limits](https://www.theverge.com/ai-artificial-intelligence/952180/amazon-seattle-data-center-moratorium-aecj-disciplinary-action) ⭐️ 8.0/10

Three Amazon software engineers who testified in favor of a one-year moratorium on new large data centers in Seattle are now facing disciplinary action, including potential termination, from Amazon, which they allege violates Seattle's political speech protections. This case could set a precedent for tech worker activism and corporate retaliation, highlighting tensions between employee rights and corporate interests in the AI era. It also underscores the growing debate over data center regulation and its environmental and social impacts. The employees testified on June 3, 2026, citing Seattle's anti-discrimination law protecting political speech. On June 10, Amazon issued disciplinary warnings, and the employees filed a complaint on June 18 alleging illegal retaliation.

rss · The Verge · Jun 18, 16:00

**Background**: Seattle has a city law that prohibits employers from discriminating against employees based on political speech. In June 2026, the Seattle City Council unanimously passed a one-year moratorium on new large data centers to study their impact on electrical grids, water usage, and utility rates. Amazon, a major tech company, has significant data center operations and opposed the moratorium.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/952180/amazon-seattle-data-center-moratorium-aecj-disciplinary-action">Amazon employees say they’re facing termination for backing data ...</a></li>
<li><a href="https://www.nytimes.com/2026/06/18/technology/amazon-worker-retaliation-data-center-complaints.html">Amazon Retaliated Against Workers Who Supported Regulating Data ...</a></li>
<li><a href="https://vyraa.com/washington-state/seattle-emergency-moratorium-on-large-ai-data-centers">Seattle Enacts Emergency Moratorium on Large-Scale AI Data Centers</a></li>

</ul>
</details>

**Tags**: `#Amazon`, `#employee rights`, `#data centers`, `#AI regulation`, `#political speech`

---

<a id="item-13"></a>
## [Merkle Tree Certificates: Faster, Safer Internet](https://www.reddit.com/r/programming/comments/1u9czhg/keeping_the_internet_fast_and_secure_introducing/) ⭐️ 8.0/10

A new Internet-Draft proposes Merkle Tree Certificates (MTCs) as a novel certificate format for HTTPS/TLS, designed to streamline certificate validation and support post-quantum cryptography. MTCs could significantly reduce the size and validation overhead of certificates, improving internet speed and security, especially as the industry transitions to post-quantum algorithms that are larger and slower. Merkle Tree Certificates leverage Merkle trees to aggregate multiple certificates into a compact structure, enabling efficient batch validation and reducing bandwidth usage.

reddit · r/programming · /u/CircumspectCapybara · Jun 18, 17:41

**Background**: Traditional X.509 certificates are validated individually, which can be slow and bandwidth-intensive, especially with large certificate chains. Merkle trees are hash-based data structures that allow efficient verification of large data sets, commonly used in blockchain and distributed systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Merkle_tree">Merkle tree - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/">draft-ietf-plants-merkle-tree-certs-04 - Merkle Tree Certificates</a></li>
<li><a href="https://grokipedia.com/page/Merkle_Tree_Certificates">Merkle Tree Certificates</a></li>

</ul>
</details>

**Tags**: `#security`, `#cryptography`, `#web infrastructure`, `#certificates`, `#Merkle tree`

---

<a id="item-14"></a>
## [Anthropic SDK Python v0.110.0 Adds Code Execution Tool](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.110.0) ⭐️ 7.0/10

Anthropic released v0.110.0 of its Python SDK on June 18, 2026, adding support for the new code_execution_20260120 tool and fixing several bugs including header merging and Bedrock stream event preservation. The code execution tool enables Claude to run Python code in a secure sandbox, allowing developers to build agents that can perform data analysis, generate visualizations, and execute complex calculations directly through the API. The new tool is named code_execution_20260120, and the release also fixes a bug where the x-stainless-helper header was being overwritten instead of appended during header merges, and preserves stream event types in the Bedrock integration.

github · stainless-app[bot] · Jun 18, 17:18

**Background**: Anthropic's Python SDK provides a convenient interface for developers to interact with the Claude API. The code execution tool is an official feature that allows Claude to execute Python code inside a managed, isolated sandbox container and incorporate the output into its response, useful for tasks like data analysis and visualization.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview">Claude Code overview - Anthropic</a></li>
<li><a href="https://yougo-plus.com/en/what-is-code-execution-tool/">What Is the Code Execution Tool ? A Complete Guide to...</a></li>
<li><a href="https://agno.mintlify.app/examples/models/anthropic/code_execution">Learn how to use Anthropic 's code execution tool with Agno.</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#SDK`, `#Python`, `#API`

---

<a id="item-15"></a>
## [Cornell CS 6120 Advanced Compilers Now Self-Guided Online](https://www.cs.cornell.edu/courses/cs6120/2025fa/self-guided/) ⭐️ 7.0/10

Cornell University's CS 6120: Advanced Compilers course is now available as a self-guided online version, covering topics such as SSA form, dynamic compilation, and trace compilation. This provides free, high-quality compiler education to a global audience, filling a gap for advanced topics beyond introductory compiler courses. The course includes lectures, assignments, and projects, and has been discussed on Hacker News multiple times since 2020, indicating sustained interest.

hackernews · ibobev · Jun 18, 11:04 · [Discussion](https://news.ycombinator.com/item?id=48583606)

**Background**: Static single assignment (SSA) form is an intermediate representation where each variable is assigned exactly once, simplifying compiler optimizations. Dynamic compilation, including just-in-time (JIT) compilation, optimizes code at runtime for better performance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Static_single-assignment_form">Static single-assignment form - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_compilation">Dynamic compilation</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the course's focus on trace compilation may be outdated, as trace compilation is considered a dead end. Some questioned the 'advanced' label, arguing topics like SSA form belong in a first compiler course.

**Tags**: `#compilers`, `#education`, `#programming languages`, `#systems`

---