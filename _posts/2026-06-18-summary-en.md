---
layout: default
title: "Horizon Summary: 2026-06-18 (EN)"
date: 2026-06-18
lang: en
---

> From 90 items, 15 important content pieces were selected

---

1. [GLM-5.2: Most Powerful Open-Weight LLM Released](#item-1) ⭐️ 9.0/10
2. [Lore: Open Source Version Control for Game Development](#item-2) ⭐️ 8.0/10
3. [US Delays Blacklisting DeepSeek, Flags 100+ Chinese Firms](#item-3) ⭐️ 8.0/10
4. [AI Chemist Using GPT-5.4 Improves Key Drug Reaction](#item-4) ⭐️ 8.0/10
5. [OpenAI Launches LifeSciBench for AI in Life Sciences](#item-5) ⭐️ 8.0/10
6. [Charity Majors: AI Makes Code Cheap, Demands More Discipline](#item-6) ⭐️ 8.0/10
7. [Export Controls on AI Models Undermine US Cyber Defense](#item-7) ⭐️ 8.0/10
8. [World leaders fear US AI cut-off after Anthropic blackout](#item-8) ⭐️ 8.0/10
9. [Russian-speaking group hacks tens of thousands of Fortinet firewalls](#item-9) ⭐️ 8.0/10
10. [Pramaana Labs raises $27M seed for AI formal verification](#item-10) ⭐️ 8.0/10
11. [RFC 10008 Proposes New HTTP QUERY Method](#item-11) ⭐️ 8.0/10
12. [Datasette 1.0a34 Adds Row Editing in Web UI](#item-12) ⭐️ 7.0/10
13. [Georgi Gerganov Endorses Qwen3.6-27B for Local Coding](#item-13) ⭐️ 7.0/10
14. [FTC lawsuit exposes subscription scam networks' evasion tactics](#item-14) ⭐️ 7.0/10
15. [Odyssey hits $1.45B valuation with Amazon backing](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GLM-5.2: Most Powerful Open-Weight LLM Released](https://simonwillison.net/2026/Jun/17/glm-52/#atom-everything) ⭐️ 9.0/10

Z.ai released GLM-5.2, a 753B parameter open-weights LLM with a 1 million token context window, under the MIT license on June 16, 2026. GLM-5.2 is widely recognized as the most powerful open-weights text-only model, outperforming competitors like MiniMax-M3 and DeepSeek V4 Pro on the Artificial Analysis Intelligence Index, and it offers frontier-level performance at a fraction of the cost of proprietary models. The model uses Mixture of Experts (MoE) with 40 active parameters out of 753B total, and it consumes more output tokens per task (43k) compared to peers. It ranks 2nd on the Code Arena WebDev leaderboard, behind only Claude Fable 5, despite lacking image input.

rss · Simon Willison · Jun 17, 23:58

**Background**: Open-weights LLMs make their trained parameters publicly available, allowing anyone to use and modify them. Mixture of Experts (MoE) activates only a subset of parameters per input, improving efficiency. A 1 million token context window enables processing very long documents or conversations in one go.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/applying-mixture-of-experts-in-llm-architectures/">Applying Mixture of Experts in LLM Architectures | NVIDIA Technical...</a></li>

</ul>
</details>

**Discussion**: Community members are excited about GLM-5.2's performance and low cost, with some calling it a 'huge blow' to proprietary AI companies. However, concerns were raised about reasoning efficiency, as one user reported the model spending 15 minutes and 45k tokens on a simple coding task.

**Tags**: `#LLM`, `#open-weights`, `#AI`, `#GLM-5.2`, `#Z.ai`

---

<a id="item-2"></a>
## [Lore: Open Source Version Control for Game Development](https://lore.org/) ⭐️ 8.0/10

Epic Games has open-sourced Lore, a next-generation version control system designed for scalability, targeting game development as a competitor to Perforce. Lore addresses a critical gap in version control for game development by handling large binary files and exclusive locks better than Git, offering a modern open-source alternative to the proprietary Perforce. Lore is already the built-in version control system for UEFN (Unreal Editor for Fortnite), but the open source tooling currently cannot talk to it due to a proprietary compression format used in UEFN builds.

hackernews · regnerba · Jun 17, 14:30 · [Discussion](https://news.ycombinator.com/item?id=48571081)

**Background**: Version control systems like Git are optimized for text-based files (code) but struggle with large binary files (textures, 3D models, audio) common in game development. Perforce is the industry standard for game development due to its support for large files and exclusive file locking, but it is proprietary and complex to administer. Lore aims to combine the scalability and locking features of Perforce with the openness of Git.

<details><summary>References</summary>
<ul>
<li><a href="https://epicgames.github.io/lore/explanation/system-design/">The Lore Version Control System - Lore Developer Documentation</a></li>
<li><a href="https://github.com/EpicGames/lore">GitHub - EpicGames/ lore : Lore is a next-generation, open source...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Perforce">Perforce - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The Hacker News community largely agrees that Lore fills a real need, with many noting Perforce's dominance in game development and its complexity. Some commenters express hope that Lore will simplify workflows, while others caution that it is still early and the open source tooling is incomplete.

**Tags**: `#version control`, `#game development`, `#open source`, `#scalability`, `#Perforce`

---

<a id="item-3"></a>
## [US Delays Blacklisting DeepSeek, Flags 100+ Chinese Firms](https://www.reuters.com/world/china/us-holds-off-blacklisting-chinas-deepseek-more-than-100-firms-deemed-security-2026-06-17/) ⭐️ 8.0/10

The United States has decided to delay blacklisting Chinese AI startup DeepSeek and over 100 other Chinese firms, despite interagency approval to designate them as national security risks, in an effort to avoid escalating tensions with Beijing. This decision highlights the delicate balance the US must strike between curbing Chinese technological advances and maintaining diplomatic relations, with significant implications for the global AI race and tech decoupling. The blacklist would have restricted US companies from selling goods and services to these firms, but Chinese AI companies like DeepSeek already face export controls on Nvidia GPUs and rely little on US inputs.

hackernews · giuliomagnifico · Jun 17, 03:55 · [Discussion](https://news.ycombinator.com/item?id=48565498)

**Background**: DeepSeek is a Chinese AI company that developed the open-weight DeepSeek-R1 model, which rivals OpenAI's GPT-4 at a fraction of the training cost. Its success has been seen as a 'Sputnik moment' for US AI leadership. The US has been using tariffs and export controls to limit China's tech rise, while China controls rare earth minerals critical for defense and electronics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_(Company)">DeepSeek (Company)</a></li>
<li><a href="https://finance.yahoo.com/news/exclusive-us-holds-off-blacklisting-000212827.html">Exclusive- US holds off blacklisting China 's DeepSeek, more than 100...</a></li>
<li><a href="https://economictimes.indiatimes.com/news/international/business/u-s-held-back-blacklisting-deepseek-over-100-chinese-firms-despite-security-concerns-sources-say/articleshow/131792688.cms">U . S . held back blacklisting DeepSeek, over 100 Chinese firms ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some praised DeepSeek's affordability and utility, while others criticized US policy as hypocritical or unenforceable, comparing it to China's own restrictions. A few noted that the blacklist's practical impact is limited since Chinese firms already face GPU export bans.

**Tags**: `#AI`, `#geopolitics`, `#regulation`, `#DeepSeek`, `#US-China`

---

<a id="item-4"></a>
## [AI Chemist Using GPT-5.4 Improves Key Drug Reaction](https://openai.com/index/ai-chemist-improves-reaction) ⭐️ 8.0/10

OpenAI and Molecule.one demonstrated a near-autonomous AI chemist powered by GPT-5.4 that successfully improved a challenging reaction used in medicinal chemistry. This advancement could accelerate drug discovery by automating complex chemical synthesis, reducing the time and cost of developing new pharmaceuticals. The system leverages GPT-5.4's reasoning and computer use capabilities to plan and execute experiments with minimal human intervention, achieving improved yields for a key reaction.

rss · OpenAI Blog · Jun 17, 10:00

**Background**: Medicinal chemistry often requires optimizing synthetic routes for drug candidates, a process that is time-consuming and relies on expert intuition. AI models like GPT-5.4 can analyze vast chemical data and propose novel reaction conditions, while autonomous systems can run experiments in parallel. This integration marks a step toward fully automated chemical research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.4">GPT-5.4</a></li>
<li><a href="https://molecule.one/">molecule . one - Making Molecules . Discovering Chemistry</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Chemistry`, `#Drug Discovery`, `#Autonomous Systems`, `#GPT-5.4`

---

<a id="item-5"></a>
## [OpenAI Launches LifeSciBench for AI in Life Sciences](https://openai.com/index/introducing-life-sci-bench) ⭐️ 8.0/10

OpenAI has introduced LifeSciBench, a new benchmark authored and reviewed by domain experts to evaluate AI systems on real-world life science research tasks and decisions. This benchmark provides a rigorous, expert-driven evaluation framework that could help ensure AI systems are safe and effective for scientific research, potentially accelerating progress in drug discovery, genomics, and other life science fields. LifeSciBench focuses on end-to-end scientific tasks rather than isolated capabilities, and is designed to avoid contamination from public datasets by using expert-authored, private questions.

rss · OpenAI Blog · Jun 17, 00:00

**Background**: Benchmarks are standardized tests used to measure and compare the performance of AI models. LifeSciBench is part of a broader trend toward expert-authored evaluations that better reflect real-world professional tasks, as seen in benchmarks like Humanity's Last Exam and Scale's expert-driven leaderboards.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-life-sci-bench/">Introducing LifeSciBench | OpenAI</a></li>
<li><a href="https://theplanettools.ai/blog/openai-gpt-rosalind-life-sciences-codex-plugins-lifescibench-june-2026">GPT-Rosalind Gets GPT-5.5: Codex Plugins + LifeSciBench</a></li>
<li><a href="https://www.techtimes.com/articles/317754/20260604/gpt-rosalind-drug-discovery-update-openai-cuts-genomics-compute-expands-global-access.htm">GPT-Rosalind Drug Discovery Update: OpenAI Cuts Genomics...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#benchmark`, `#life sciences`, `#OpenAI`, `#evaluation`

---

<a id="item-6"></a>
## [Charity Majors: AI Makes Code Cheap, Demands More Discipline](https://simonwillison.net/2026/Jun/17/charity-majors/#atom-everything) ⭐️ 8.0/10

Charity Majors argues that AI has flipped the economics of code production, making code generation effectively free and instant, which demands more engineering discipline, not less. This insight challenges the common narrative that AI reduces the need for skilled engineers, emphasizing instead that cheap, disposable code requires stronger engineering practices to manage complexity and maintain quality. Majors notes that lines of code went from being treasured and carefully curated to disposable and regenerable practically overnight in 2025. She warns that nondeterministic AI systems will require more discipline, not less.

rss · Simon Willison · Jun 17, 17:12

**Background**: Historically, writing code was slow and expensive, acting as a natural brake that forced careful thought before writing. With generative AI, code can be produced instantly at near-zero cost, shifting the bottleneck from production to maintenance and system design.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/17/charity-majors/">A quote from Charity Majors | Simon Willison’s Weblog</a></li>
<li><a href="https://charity.wtf/2026/06/15/ai-demands-more-engineering-discipline-not-less-xpost/">AI demands more engineering discipline . Not less (xpost) – charity .wtf</a></li>
<li><a href="https://ghost.madewithlove.dev/blog/ai-didnt-change-the-economics-of-software-engineering/">AI didn't change the economics of software engineering</a></li>

</ul>
</details>

**Discussion**: The community discussion on Simon Willison's blog and the original post highlights agreement with Majors' perspective, with many engineers sharing experiences of AI-generated code introducing subtle bugs and requiring more rigorous review. Some debate whether the shift truly increases discipline or just changes its nature.

**Tags**: `#ai-assisted-programming`, `#software-engineering`, `#generative-ai`, `#economics-of-code`

---

<a id="item-7"></a>
## [Export Controls on AI Models Undermine US Cyber Defense](https://simonwillison.net/2026/Jun/16/fable-5-export-controls/#atom-everything) ⭐️ 8.0/10

The Trump administration imposed export controls on Anthropic's Claude Fable 5 and Mythos 5, citing a jailbreak that allowed the model to fix code vulnerabilities. Cybersecurity expert Kate Moussouris clarified that the so-called jailbreak was actually a legitimate defensive request to patch security bugs. This policy harms US cyber defense by restricting AI models from fixing critical security vulnerabilities, which is exactly what defenders need. It also sets a dangerous precedent for regulating AI capabilities that are essential for cybersecurity. The export controls forced Anthropic to block access to Fable 5 and Mythos 5 for all foreign nationals, including users inside the US and its own employees. The models were banned because they could be prompted to "fix this code" and generate patches, which the administration classified as a cyber attack capability.

rss · Simon Willison · Jun 16, 05:20

**Background**: Claude Fable 5 is a large language model developed by Anthropic, designed for general use with strong safety alignment. Export controls are regulations that restrict the transfer of sensitive technologies to foreign entities, typically to prevent adversaries from gaining military or strategic advantages. In this case, the controls were applied to an AI model for the first time, based on the mistaken belief that its code-fixing ability constitutes a security threat.

<details><summary>References</summary>
<ul>
<li><a href="https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519">Inside the whirlwind 24 hours that led the White House to slap export ...</a></li>

</ul>
</details>

**Discussion**: The discussion highlights widespread agreement that the export controls are counterproductive, with experts like Kate Moussouris emphasizing that fixing bugs is the most valuable defensive use of AI. Commenters note that non-technical decision-makers are conflating defensive code repair with offensive cyber attacks, leading to misguided policy.

**Tags**: `#AI policy`, `#export controls`, `#cybersecurity`, `#AI safety`, `#open source`

---

<a id="item-8"></a>
## [World leaders fear US AI cut-off after Anthropic blackout](https://techcrunch.com/2026/06/17/world-leaders-want-american-ai-they-just-dont-want-america-to-be-able-to-turn-it-off/) ⭐️ 8.0/10

At the G7 summit, French President Macron and Indian PM Modi raised concerns that the US could cut off access to American AI systems, a fear made tangible by the recent Anthropic blackout incident. This highlights growing geopolitical tensions around AI sovereignty, as nations fear dependency on US-controlled AI infrastructure could be used as a political lever, threatening national security and economic autonomy. The Anthropic blackout, where access to Claude was abruptly restricted, served as a concrete example of how US companies could cut off AI services, validating long-standing fears of technological coercion.

rss · TechCrunch · Jun 17, 19:01

**Background**: AI sovereignty refers to a nation's ability to develop, control, and govern its own AI systems without external dependency. The US currently hosts leading AI companies like OpenAI and Anthropic, giving it significant leverage over global AI access.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/why-ai-sovereignty-matters-more-than-you-think-arpit-tandon-ncfmc">Why AI Sovereignty Matters More Than You Think</a></li>

</ul>
</details>

**Tags**: `#AI`, `#geopolitics`, `#AI sovereignty`, `#regulation`, `#Anthropic`

---

<a id="item-9"></a>
## [Russian-speaking group hacks tens of thousands of Fortinet firewalls](https://techcrunch.com/2026/06/17/cybercriminals-allegedly-hacked-tens-of-thousands-of-fortinet-firewalls-used-by-major-companies-all-over-the-world/) ⭐️ 8.0/10

An alleged Russian-speaking cybercriminal group is reportedly compromising tens of thousands of Fortinet firewalls used by major companies worldwide by exploiting previously known passwords. This large-scale attack on enterprise firewalls could lead to widespread data breaches and network compromises, affecting many high-profile organizations and highlighting the dangers of password reuse. The attackers reportedly used previously known passwords, not new vulnerabilities, to gain access. The compromised firewalls include FortiGate devices used for VPN and network security.

rss · TechCrunch · Jun 17, 18:20

**Background**: Fortinet firewalls are widely used by enterprises for network security and VPN access. Cybercriminals often target these devices because they provide a gateway into internal networks. Previous incidents have shown that many organizations fail to change default or weak passwords, making them vulnerable to credential-stuffing attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bleepingcomputer.com/news/security/passwords-exposed-for-almost-50-000-vulnerable-fortinet-vpns/">Passwords exposed for almost 50,000 vulnerable Fortinet VPNs</a></li>
<li><a href="https://pasqualepillitteri.it/en/news/5278/fortibleed-fortinet-vpn-credentials-stolen">FortiBleed: 75,000 Fortinet VPN Credentials Stolen Across 194...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#Fortinet`, `#firewall`, `#vulnerability`, `#cyberattack`

---

<a id="item-10"></a>
## [Pramaana Labs raises $27M seed for AI formal verification](https://techcrunch.com/2026/06/17/pramaana-labs-raises-27-million-seed-round-from-khosla-ventures-to-bring-formal-verification-to-ai/) ⭐️ 8.0/10

Pramaana Labs has raised a $27 million seed round led by Khosla Ventures to apply formal verification techniques to AI systems, targeting high-stakes domains like law, drug discovery, and tax preparation. This funding signals strong investor confidence in formal verification as a solution to AI reliability issues, potentially enabling AI adoption in critical sectors where errors are costly. Pramaana's system provides machine-checkable proofs for AI answers, ensuring accuracy and identifying rule breaches. The company focuses on rule-based, high-stakes verticals where formal verification can guarantee correctness.

rss · TechCrunch · Jun 17, 14:15

**Background**: Formal verification uses mathematical methods to prove or disprove the correctness of a system against a formal specification. It is widely used in hardware and critical software (e.g., CompCert compiler, seL4 kernel) but has been challenging to apply to AI due to the complexity and non-determinism of neural networks. Pramaana aims to bridge this gap for high-reliability applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>
<li><a href="https://www.rediff.com/business/report/pramaana-labs-raises-27-million-led-by-khosla-ventures/20260617.htm">Pramaana Labs Raises $27M To Develop... - Rediff.com Business</a></li>

</ul>
</details>

**Tags**: `#AI`, `#formal verification`, `#funding`, `#reliability`

---

<a id="item-11"></a>
## [RFC 10008 Proposes New HTTP QUERY Method](https://www.reddit.com/r/programming/comments/1u84m2g/rfc_10008_the_http_query_method/) ⭐️ 8.0/10

RFC 10008 introduces a new HTTP QUERY method that allows clients to send a request body in a safe and idempotent manner, standardizing a pattern previously handled by GET or POST. This provides a standardized way to perform queries with a body, improving API design clarity and interoperability, and reducing ambiguity in existing practices. The QUERY method is safe and idempotent, meaning it does not change server state and multiple identical requests have the same effect as a single request. It also defines an Accept-Query header field for content negotiation.

reddit · r/programming · /u/Nimelrian · Jun 17, 08:43

**Background**: HTTP methods like GET are safe and idempotent but do not support a request body, while POST supports a body but is not safe or idempotent. The QUERY method fills this gap by allowing a body while preserving safety and idempotency, which is useful for complex queries in APIs like GraphQL or SPARQL.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rfc-editor.org/info/rfc10008/">RFC 10008 : The HTTP QUERY Method | RFC Editor</a></li>
<li><a href="https://datatracker.ietf.org/doc/draft-ietf-httpbis-safe-method-w-body/12/">draft-ietf-httpbis-safe- method -w-body-12 - The HTTP QUERY Method</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Glossary/Idempotent">Idempotent - Glossary | MDN</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion is active, with many commenters debating the utility of the new method. Some argue it formalizes a common pattern, while others express concerns about potential misuse and complexity. Overall sentiment is cautiously positive, with interest in how it will be adopted.

**Tags**: `#HTTP`, `#RFC`, `#Web Standards`, `#API Design`

---

<a id="item-12"></a>
## [Datasette 1.0a34 Adds Row Editing in Web UI](https://simonwillison.net/2026/Jun/16/datasette/#atom-everything) ⭐️ 7.0/10

Datasette 1.0a34 introduces insert, edit, and delete row capabilities directly in the web interface, available on table pages and row pages. This feature was inspired by Datasette Agent, an AI assistant that already supported SQL write operations. This update addresses a long-standing gap in Datasette's usability, making it a more complete tool for data exploration and management. It reduces the need for external tools or plugins for basic CRUD operations, benefiting all Datasette users. The insert, edit, and delete features are available on table pages, while edit and delete also appear as action items on the row page. The release is an alpha version (1.0a34), indicating it may still have bugs or incomplete features.

rss · Simon Willison · Jun 16, 21:31

**Background**: Datasette is an open-source tool for exploring and publishing data, primarily working with SQLite databases. Previously, users had to rely on plugins or external tools to modify data through the web interface. Datasette Agent is an AI assistant that can write and execute SQL queries, including write operations, which highlighted the absence of a native UI for data manipulation.

<details><summary>References</summary>
<ul>
<li><a href="https://agent.datasette.io/">Datasette Agent : an AI assistant for Datasette to help explore and...</a></li>
<li><a href="https://simonwillison.net/2026/May/21/datasette-agent/">Datasette Agent | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#release`, `#database`, `#web-ui`, `#alpha`

---

<a id="item-13"></a>
## [Georgi Gerganov Endorses Qwen3.6-27B for Local Coding](https://simonwillison.net/2026/Jun/16/georgi-gerganov/#atom-everything) ⭐️ 7.0/10

Georgi Gerganov, creator of llama.cpp, publicly endorsed the Qwen3.6-27B model as a highly capable local coding assistant, sharing that he uses it daily on his M2 Ultra and RTX 5090 machines. This endorsement from a key figure in the local LLM ecosystem validates Qwen3.6-27B as a practical tool for developers, potentially driving wider adoption of local coding assistants and reducing reliance on cloud-based AI services. Gerganov uses a lightweight harness called pi agent with the flags '-nc --offline' and a short system prompt to align the model with his coding style. He noted that he would use it more if not for time spent on PR reviews.

rss · Simon Willison · Jun 16, 16:04

**Background**: Qwen3.6-27B is a dense 27-billion-parameter language model released by Alibaba's Qwen team in April 2026. llama.cpp, created by Georgi Gerganov, is an open-source library that enables efficient local inference of LLMs on consumer hardware, and is the foundation of tools like Ollama and LM Studio.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-27B">Qwen/ Qwen 3 . 6 - 27 B · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://pi.dev/">Pi Coding Agent</a></li>

</ul>
</details>

**Tags**: `#local LLM`, `#coding assistant`, `#llama.cpp`, `#Qwen`

---

<a id="item-14"></a>
## [FTC lawsuit exposes subscription scam networks' evasion tactics](https://techcrunch.com/2026/06/17/ftc-lawsuit-reveals-how-subscription-scam-networks-evade-app-store-enforcement/) ⭐️ 7.0/10

The FTC has filed a lawsuit revealing how subscription scam networks use shell companies and payment infrastructure to evade enforcement by major app stores like Apple's App Store and Google Play. This case highlights systemic gaps in app store enforcement, showing that scammers can remain active despite consumer complaints, which undermines consumer trust and platform accountability. The lawsuit alleges that operators use shell companies to re-list apps after being banned, and leverage payment processors like Paddle to process subscriptions while obscuring their identity.

rss · TechCrunch · Jun 17, 19:46

**Background**: Subscription scams involve apps that lure users into expensive recurring charges, often through deceptive interfaces. App stores have policies against such practices, but enforcement relies on detecting and banning offending apps. Scammers evade this by creating new shell companies and using third-party payment platforms that act as merchant of record, making it harder for stores to track and block them.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/17/ftc-lawsuit-reveals-how-subscription-scam-networks-evade-app-store-enforcement/">FTC lawsuit reveals how subscription scam networks evade app store ...</a></li>
<li><a href="https://www.subscriptioninsider.com/article-type/news/ftc-fines-paddle-5-million-for-facilitating-tech-support-scams-through-its-payment-platform">FTC Fines Paddle $5 Million for Facilitating... - Subscription Insider</a></li>

</ul>
</details>

**Tags**: `#app stores`, `#subscription scams`, `#FTC`, `#consumer protection`, `#platform enforcement`

---

<a id="item-15"></a>
## [Odyssey hits $1.45B valuation with Amazon backing](https://techcrunch.com/2026/06/17/world-model-maker-odyssey-nabs-1-45b-valuation-backed-by-amazon-and-other-big-names/) ⭐️ 7.0/10

Odyssey, a world model startup, raised funding at a $1.45 billion valuation, with Amazon among the investors. This signals that world models are becoming a major focus in AI beyond large language models, attracting big tech investment. Odyssey was founded by self-driving pioneers Oliver Cameron and Jeff Hawke, and previously released a model that streams interactive 3D worlds.

rss · TechCrunch · Jun 17, 17:43

**Background**: World models are AI systems that learn to predict and interact with environments over time, enabling simulation and planning. They are considered the next frontier beyond LLMs for embodied AI and robotics.

<details><summary>References</summary>
<ul>
<li><a href="https://odyssey.ml/">Odyssey</a></li>
<li><a href="https://techcrunch.com/2025/05/28/odysseys-new-ai-model-streams-3d-interactive-worlds/">Odyssey 's new AI model streams 3D interactive worlds | TechCrunch</a></li>

</ul>
</details>

**Tags**: `#AI`, `#world models`, `#funding`, `#startup`, `#Amazon`

---