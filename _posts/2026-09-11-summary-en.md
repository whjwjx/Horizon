---
layout: default
title: "Horizon Summary: 2026-09-11 (EN)"
date: 2026-09-11
lang: en
---

> From 79 items, 15 important content pieces were selected

---

1. [OpenAI Releases GPT-6 Astra, Its Most Capable Business Model](#item-1) ⭐️ 9.0/10
2. [Calif Research Unveils WeWorm, First Zero-Click WeChat Call Worm Built with AI](#item-2) ⭐️ 9.0/10
3. [Shopify abandons React Native, returns to native Swift and Kotlin](#item-3) ⭐️ 8.0/10
4. [Researchers Question Whether OpenAI Can Be Trusted With Unpublished Math](#item-4) ⭐️ 8.0/10
5. [OpenAI Launches ChatGPT for Financial Services with GPT-6 Astra](#item-5) ⭐️ 8.0/10
6. [OpenAI Launches Managed Agents API Powered by Codex Harness](#item-6) ⭐️ 8.0/10
7. [OpenAI Brings GPT-Live-1 Full-Duplex Voice to the API](#item-7) ⭐️ 8.0/10
8. [trynix.dev Runs Any Nix Package in a Browser VM](#item-8) ⭐️ 8.0/10
9. [IDScan confirms breach exposing 150 million driver's licenses](#item-9) ⭐️ 8.0/10
10. [Google DeepMind Launches AlphaGenome Atlas Mapping 9 Billion DNA Mutations](#item-10) ⭐️ 8.0/10
11. [Cognition launches SWE-2 coding model, rivaling Fable 5.1 at lower cost](#item-11) ⭐️ 7.0/10
12. [Researcher uses Codex and ChatGPT to hunt new antimicrobials](#item-12) ⭐️ 7.0/10
13. [OpenAI launches Data agent in ChatGPT Work](#item-13) ⭐️ 7.0/10
14. [OpenAI and GSA Expand Discounted AI Access to U.S. Governments](#item-14) ⭐️ 7.0/10
15. [Paul Christiano Joins OpenAI Foundation Board](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [OpenAI Releases GPT-6 Astra, Its Most Capable Business Model](https://openai.com/index/gpt-6-astra-next-generation-work) ⭐️ 9.0/10

OpenAI announced GPT-6 Astra, described as its most capable model for business, featuring advanced reasoning, computer use, and stronger writing and design judgment. According to Wikipedia, it was initially released to approved users on September 3, 2026, with general availability the following day, after being delayed following OpenAI's July 2026 Hugging Face incident. A new flagship model from OpenAI positioned as its most capable for business could reshape enterprise workflows around reasoning and autonomous computer use, intensifying competition with Anthropic's Claude and Google's Gemini in the agentic AI space. Its designation as OpenAI's first model to reach the Critical cybersecurity capability level under the Preparedness Framework also signals a new tier of capability and risk for broadly deployed AI. OpenAI states Astra is its most aligned model, with substantial improvements in understanding user intent and model behavior, allowing users to delegate tasks with greater confidence. The GPT-6 Astra System Card notes it is the first model to reach the Critical level of cybersecurity capability under OpenAI's Preparedness Framework, a notable caveat for enterprise deployment.

rss · OpenAI Blog · Sep 9, 11:00

**Background**: Large language models (LLMs) are AI systems trained on vast text data to generate and reason over language; recent "reasoning models" add step-by-step deliberation, which improves accuracy but increases output verbosity and latency. "Computer use" refers to AI models that can control software and browsers much like a human, a capability pioneered by Anthropic's Claude and later adopted by Google's Gemini 2.5 Computer Use. OpenAI's Preparedness Framework is its internal safety scheme that rates models across risk categories such as cybersecurity, with Critical being a high-severity threshold.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra - Wikipedia</a></li>
<li><a href="https://openai.com/index/gpt-6-astra/">GPT-6 Astra: A new generation of intelligence | OpenAI</a></li>
<li><a href="https://deploymentsafety.openai.com/gpt-6-astra">GPT-6 Astra System Card - Deployment Safety Hub - OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#GPT-6`, `#AI`, `#LLM`, `#business`

---

<a id="item-2"></a>
## [Calif Research Unveils WeWorm, First Zero-Click WeChat Call Worm Built with AI](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research released a demo of WeWorm, described as the first zero-click worm that spreads through WeChat calls on both iOS and Android, compromising accounts without the victim answering or interacting with their phone. The team says it found the bug and wrote the first remote code execution (RCE) exploit in about two days with AI assistance, then built the worm in roughly one more week. This is a significant escalation in mobile security: a self-spreading worm that requires no user interaction could theoretically propagate across WeChat's roughly 1.4 billion users, and the fact that AI compressed months of exploit development into days signals a paradigm shift in vulnerability discovery and weaponization. It raises urgent questions for both platform defenders and AI safety researchers about how quickly offensive capabilities can now be produced. The exploit succeeds even if the victim answers the call, in which case they hear nothing, and Calif demonstrated the worm spreading among three test phones. The team emphasized that AI did most of the work while humans supplied judgment about what to target and how to test safely, and the research was published on September 8, 2026 as a demo rather than a live attack.

rss · Simon Willison · Sep 10, 00:56

**Background**: A zero-click exploit is one that compromises a device without any action from the user, making it far more dangerous than attacks that require opening a file or tapping a link. A worm is malware that self-replicates and spreads automatically from victim to victim, and remote code execution (RCE) means an attacker can run arbitrary code on a target's device. WeChat is a Chinese messaging app with roughly 1.4 billion users, and its voice-call feature is the vector this research targets.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls</a></li>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">"Zero-click" WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm – First 0-Click Worm Spreading Through WeChat Calls ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#ai`, `#mobile`, `#exploit`, `#wechat`

---

<a id="item-3"></a>
## [Shopify abandons React Native, returns to native Swift and Kotlin](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify published an engineering post detailing its decision to migrate its mobile apps away from React Native and back to fully native Swift for iOS and Kotlin for Android. The announcement triggered a large Hacker News discussion (748 points, 501 comments) about cross-platform tradeoffs and LLM-assisted rewrites. A major commerce platform reversing a high-profile cross-platform bet is a strong signal that native development is regaining favor, especially as AI code generation lowers the cost of maintaining two codebases. It will influence how other large companies weigh React Native against native stacks. Commenters note that debugging crashes spanning JavaScript, C++, and native threads can cost more than maintaining two separate codebases, and several engineers report that LLM tools like Codex can now scaffold native iOS and Android apps from an existing React Native codebase in hours.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is Meta's open-source framework that lets developers write one JavaScript codebase for both iOS and Android, while Swift is Apple's compiled language for its platforms and Kotlin is JetBrains' language that Google has endorsed as preferred for Android. Cross-platform frameworks trade some performance and platform-specific polish for shared code and smaller teams, a tradeoff that becomes less attractive as apps and engineering organizations scale.

<details><summary>References</summary>
<ul>
<li><a href="https://reactnative.dev/architecture/xplat-implementation">Cross Platform Implementation · React Native</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kotlin_programming_language">Kotlin programming language</a></li>

</ul>
</details>

**Discussion**: Sentiment is broadly supportive of moving off React Native, with native iOS engineers feeling validated, though some push back on the narrative that LLMs made the migration feasible — one commenter says they completed a similar migration largely before LLM assistance. Others argue that since so much code is now generated, there is little upside to starting with React Native at all.

**Tags**: `#react-native`, `#mobile-development`, `#swift`, `#kotlin`, `#engineering-culture`

---

<a id="item-4"></a>
## [Researchers Question Whether OpenAI Can Be Trusted With Unpublished Math](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

A Hacker News discussion, sparked by a Mathstodon thread, raised concerns about whether researchers can trust OpenAI with unpublished mathematical ideas after OpenAI reportedly published results resembling work shared during collaborations with its models, without attributing the researchers. The thread drew 616 comments debating whether OpenAI's models were trained on those conversations or discovered the results independently through reinforcement learning. The episode highlights a growing tension between AI labs' access to cutting-edge research conversations and the academic norms of attribution and credit, which could shape whether mathematicians and scientists feel safe sharing unpublished work with commercial AI systems. It also touches on broader AI safety and research-ethics questions about how frontier labs use user data and how they communicate the provenance of their results. Commenters noted that OpenAI has reportedly given at least 100,000 researchers free access to its models, meaning researchers working on open problems may be feeding fresh training data into those systems. Others pointed out that OpenAI generated 300 billion output tokens from a model still in training shortly after learning a major math proof might be in its training data, which some found suspicious even if each step has a plausible explanation.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: Mathstodon is a Mastodon server for mathematicians, part of the decentralized fediverse, where the original thread was posted. The discussion spread to Hacker News, a widely read tech forum, and referenced posts on X (via the XCancel mirror) and Bluesky, whose decentralized identifiers (DIDs) provide portable identities. The core issue is whether large language models trained on user conversations can later produce results that appear original, and how credit should be assigned when they do.

<details><summary>References</summary>
<ul>
<li><a href="https://samjshah.com/2023/07/01/mastodon-mathstodon-join-us/">Mastodon??? MATHStodon !!! Join Us! | Continuous Everywhere but...</a></li>
<li><a href="https://daringfireball.net/linked/2026/08/16/xcancel">Daring Fireball: XCancel -- An Unofficial Twitter/X Mirror</a></li>
<li><a href="https://statuz.app/features/bluesky-handle-did-system">BlueSky Handle and DID System • Statuz</a></li>

</ul>
</details>

**Discussion**: Commenters were divided: some argued that if OpenAI were a human collaborator, publishing without attribution would be clearly unethical, while others said both explanations can be true—models may absorb intuition from chats while also discovering genuinely new techniques through reinforcement learning on verifiable math. Several expressed skepticism about whether AI is really improving rapidly on open problems or whether researchers are being misled, and one commenter described OpenAI's sequence of actions as feeling like 'parallel construction.'

**Tags**: `#OpenAI`, `#research ethics`, `#AI safety`, `#mathematics`, `#trust`

---

<a id="item-5"></a>
## [OpenAI Launches ChatGPT for Financial Services with GPT-6 Astra](https://openai.com/index/introducing-chatgpt-financial-services) ⭐️ 8.0/10

OpenAI announced ChatGPT for Financial Services, a specialized enterprise offering that combines built-in financial data with the new GPT-6 Astra model for research, modeling, and client-ready materials. The product targets labor-intensive tasks traditionally handled by junior investment bankers, such as pitchbooks and financial analysis. This marks OpenAI's first vertical-specific push into financial services, signaling a broader trend of AI vendors building tailored products for regulated industries. It could disrupt fintech workflows and reshape entry-level finance roles, while raising questions about accuracy, compliance, and data provenance in high-stakes financial work. GPT-6 Astra was released as a limited preview on September 3, 2026, following a delay caused by OpenAI's Hugging Face incident in July 2026, during which the company added more safeguards. The model is described as OpenAI's most capable, built for complex reasoning, coding, computer use, research, and document creation, and is particularly strong at adhering to templates and producing well-structured slides and spreadsheets.

rss · OpenAI Blog · Sep 10, 07:00

**Background**: ChatGPT is OpenAI's conversational AI assistant, and enterprise versions are customized for specific industries. GPT-6 Astra is OpenAI's newest flagship large language model, succeeding earlier GPT generations with improved reasoning and document-generation abilities. Financial services firms have been cautious about adopting generative AI due to regulatory and accuracy concerns, making a purpose-built product notable.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-chatgpt-financial-services/">Introducing ChatGPT for Financial Services - OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#Financial Services`, `#GPT-6`, `#AI Applications`

---

<a id="item-6"></a>
## [OpenAI Launches Managed Agents API Powered by Codex Harness](https://openai.com/index/introducing-the-agents-api) ⭐️ 8.0/10

OpenAI introduced the Agents API, a managed service that lets developers build and launch cloud agents in a single API call by specifying the task, model, tools, and environment. The service is powered by the Codex harness and is available in public beta to all developers with no additional fees beyond standard usage costs. This is a platform-level move that lowers the barrier to building autonomous cloud agents, letting developers offload orchestration, session management, and context handling to OpenAI instead of building that infrastructure themselves. It could accelerate adoption of agentic AI applications and intensify competition among cloud providers offering managed agent runtimes. The Agents API runs the Codex harness and handles automatic context compaction, session management, and orchestration on the developer's behalf, so teams can focus on what makes their agent unique. It is offered alongside hosted sandboxes and is billed through standard usage rather than a separate API fee.

rss · OpenAI Blog · Sep 10, 00:00

**Background**: An agent harness is the reusable loop that drives an AI agent: it feeds context to the model, executes tool calls, and manages state across turns. OpenAI's Codex harness, originally associated with the open-source Codex CLI written in Rust, provides these conventions and context-engineering patterns. The Agents API packages that harness as a managed cloud service, so developers no longer need to run the agent loop or session infrastructure themselves.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-the-agents-api/">Introducing the Agents API - OpenAI</a></li>
<li><a href="https://developers.openai.com/api/docs/guides/agents">Agents API - OpenAI Developers</a></li>
<li><a href="https://community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481">Introducing the Agents API and hosted sandboxes</a></li>

</ul>
</details>

**Discussion**: In the OpenAI community announcement thread, developers welcomed the public beta and the absence of additional fees, while noting that the managed approach means less control over the underlying agent loop compared with running the open Codex harness directly.

**Tags**: `#OpenAI`, `#Agents API`, `#AI agents`, `#cloud infrastructure`, `#developer tools`

---

<a id="item-7"></a>
## [OpenAI Brings GPT-Live-1 Full-Duplex Voice to the API](https://openai.com/index/introducing-gpt-live-1-in-the-api) ⭐️ 8.0/10

OpenAI announced GPT-Live-1 in the API, bringing natural full-duplex voice conversations to developers along with stronger instruction following, custom voices, and telephony support. The model was previously rolled out to ChatGPT users as GPT-Live-1 and GPT-Live-1 mini before this API release. This is a major capability upgrade for developers building voice agents, since full-duplex conversation and telephony support remove two of the biggest barriers to deploying natural-sounding AI phone agents. It signals that real-time speech-to-speech interaction is becoming a standard API primitive rather than a research demo. Full-duplex means the model can listen and speak simultaneously, enabling interruption handling and more natural conversational pacing rather than simple turn-taking. The announcement also highlights custom voices and telephony support, which are critical for call-center and phone-agent use cases where codec quality, jitter, and barge-in matter.

rss · OpenAI Blog · Sep 10, 00:00

**Background**: Full-duplex is a telecommunications concept describing bidirectional communication where both parties can transmit at the same time, as opposed to half-duplex systems like walkie-talkies that require taking turns. Applying this to voice AI lets models listen and speak concurrently, which is essential for natural pacing and handling interruptions. Telephony support matters because phone networks impose constraints such as codec quality and latency that differ from web-based audio.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT-Live | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Duplex_(telecommunications)">Duplex (telecommunications) - Wikipedia</a></li>
<li><a href="https://inworld.ai/resources/best-voice-ai-for-ai-phone-agents">Voice AI for AI Phone Agents: TTS APIs Ranked for Telephony ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#voice AI`, `#API`, `#GPT-Live-1`, `#conversational AI`

---

<a id="item-8"></a>
## [trynix.dev Runs Any Nix Package in a Browser VM](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria launched trynix.dev, a qemu-wasm powered x86_64 Linux virtual machine that runs entirely in the browser and can boot any Nix package from the past 13 years via URL-addressable links such as https://trynix.dev/?pkg=python3%403.6.2. He also released trynix-preview, a GitHub Action that comments a link on a pull request so reviewers can boot that PR's build directly in the browser with no servers involved. This makes historical and reproducible software environments instantly accessible through a URL, removing the need to install Nix or provision servers just to inspect or test a package. It could meaningfully change workflows for Nix users, code reviewers, and anyone needing to reproduce an old build, while showcasing how far WebAssembly-based emulation has come. The VM is built on ktock/qemu-wasm, which compiles QEMU to WebAssembly and uses a hybrid approach where only frequently executed translation blocks are compiled to Wasm while the rest run through the TCI interpreter. Packages are addressed by URL parameters, and the trynix-preview action integrates this into GitHub pull request reviews without requiring any backend infrastructure.

rss · Simon Willison · Sep 10, 23:44

**Background**: Nix is a purely functional package manager created by Eelco Dolstra in 2003 that emphasizes reproducible and declarative builds, so a package that works on one machine should work identically on another. QEMU is a general-purpose machine emulator, and qemu-wasm is a project that compiles it to WebAssembly so full operating systems can run inside a browser tab. trynix.dev combines these ideas, letting a browser-hosted Linux VM boot a specific Nix package chosen from a URL.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/ qemu - wasm : QEMU on browser · GitHub</a></li>
<li><a href="https://nixos.org/">Nix & NixOS | Declarative builds and deployments</a></li>
<li><a href="https://reproducible.nixos.org/">NixOS Reproducible Builds</a></li>

</ul>
</details>

**Tags**: `#Nix`, `#WebAssembly`, `#qemu`, `#reproducible-builds`, `#browser-vm`

---

<a id="item-9"></a>
## [IDScan confirms breach exposing 150 million driver's licenses](https://techcrunch.com/2026/09/10/id-verification-giant-idscan-confirms-data-breach-with-more-than-150-million-drivers-licenses-stolen/) ⭐️ 8.0/10

IDScan.net, a Louisiana-based identity verification company, confirmed that hackers accessed customer data stored in its cloud environment, stealing full names, driver's license numbers, and identity numbers from other government-issued documents such as passports. Reports link the breach to a dark-web marketplace called Nexus and a database containing roughly 153 million stolen driver's licenses, with the FBI now investigating. This is one of the largest known leaks of government-issued identity documents, putting 150 million-plus people at heightened risk of identity theft and fraud. It also undermines trust in the identity verification industry itself, since the very companies collecting sensitive ID data to prevent fraud have become high-value targets. The stolen data includes full names, driver's license numbers, and identity numbers from other government-issued documents like passports, and the breach has been tied to at least three enterprise clients. The FBI is investigating, and affected individuals are being urged to take steps to protect against identity theft.

rss · TechCrunch · Sep 10, 13:21

**Background**: IDScan.net is an AI-powered identity verification platform used for ID fraud prevention, age verification, and access management, meaning it holds large volumes of sensitive identity documents on behalf of businesses. Identity verification vendors are attractive targets because a single breach can expose the personal data of millions of people at once. This incident follows a broader pattern: recent research counted 88 ID-verification breaches that collectively exposed billions of records.

<details><summary>References</summary>
<ul>
<li><a href="https://tech-insider.org/idscan-breach-confirmed-enterprise-clients-2026/">IDScan Confirms Breach: 150M IDs, 3 Clients Hit</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/idscan-confirms-breach-tied-to-153-million-stolen-drivers-licenses/">IDScan confirms breach tied to 153 million stolen driver’s ...</a></li>
<li><a href="https://securityaffairs.com/197855/reports/88-id-verification-breaches-show-the-cost-of-collecting-identity-data.html">88 ID Verification Breaches Show the Cost of Collecting Identity Data</a></li>

</ul>
</details>

**Tags**: `#security`, `#data-breach`, `#privacy`, `#identity-verification`, `#cybersecurity`

---

<a id="item-10"></a>
## [Google DeepMind Launches AlphaGenome Atlas Mapping 9 Billion DNA Mutations](https://www.producthunt.com/products/alphagenome-atlas) ⭐️ 8.0/10

Google DeepMind introduced AlphaGenome Atlas, a database that predicts the molecular effects of all 9 billion possible single-nucleotide variants across the human genome, using its AlphaGenome AI model to pre-calculate regulatory impact and AVI scores. This atlas gives researchers a high-resolution, global view of the genome, potentially accelerating the identification of disease-causing mutations and drug targets, and extending DeepMind's AI-for-science push from protein structure prediction to genomic regulation. The predictions cover every possible single-letter DNA change and include AVI scores, but they are computational predictions rather than experimental measurements, so they are most useful when applied to targeted research questions and require validation.

rss · Product Hunt (AI应用) · Sep 9, 01:41

**Background**: AlphaGenome, released by DeepMind in 2025, is a unifying model that takes DNA sequences up to 1 million base pairs long and predicts thousands of molecular properties characterizing their regulatory activity. The Atlas builds on this model and on DeepMind's earlier AlphaFold work, which predicted three-dimensional protein structures from amino-acid sequences in 2020. Single-nucleotide variants are one-letter changes in DNA that can affect gene regulation and contribute to disease.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/">AlphaGenome Atlas: Molecular predictions for 9 Billion human DNA variants — Google DeepMind</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/google-deepmind/alphagenome-atlas/">AlphaGenome Atlas: a high-resolution map of human DNA</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-02835-4">DeepMind’s new genome ‘atlas’ charts effects of all nine billion human gene mutations | Nature</a></li>

</ul>
</details>

**Tags**: `#genomics`, `#AI`, `#bioinformatics`, `#Google`, `#DNA mutations`

---

<a id="item-11"></a>
## [Cognition launches SWE-2 coding model, rivaling Fable 5.1 at lower cost](https://cognition.com/blog/swe-2) ⭐️ 7.0/10

Cognition released SWE-2, its most advanced coding model yet, which scores 50.0% on FrontierCode 1.1 Main 1 — within one point of Fable 5.1 while being 64% cheaper. The model was post-trained from the open-weight Kimi K3 and represents the first time Cognition scaled reinforcement learning to the multi-trillion-parameter regime. SWE-2 shows that post-training and RL on top of an existing open-weight model can approach frontier coding performance at a fraction of the cost, intensifying competition among AI coding model providers. It also raises questions about whether closed-weight providers can justify their pricing as open-weight alternatives rapidly improve. The model's Terminal Bench 2.1 score of 92.8% contrasts sharply with its Terminal Bench 4 score of 27.3%, a gap that skeptics interpret as evidence of benchmark overfitting rather than genuine generalization. SWE-2 is closed-weight, and its performance claims rest heavily on benchmarks that may not reflect real-world coding tasks.

hackernews · seelos · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645443)

**Background**: Cognition is the startup behind Devin, an autonomous AI coding agent. Kimi K3 is a 2.8-trillion-parameter open-weight multimodal reasoning model from Moonshot AI, particularly strong at navigating large repositories and long-horizon agentic workflows. Fable 5.1 is Anthropic's most capable model for ambitious coding projects, and FrontierCode 1.1 Main 1 is a coding benchmark used to compare frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE-2: Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely skeptical: commenters highlight the massive gap between Terminal Bench 2.1 and 4 as a sign of benchmark overfitting, question the lack of model stats and open weights, and note Cognition's past demo controversies. Some acknowledge that post-training from the capable Kimi K3 makes the model unlikely to be bad, but urge caution about claimed improvements.

**Tags**: `#AI`, `#coding-models`, `#model-release`, `#benchmarking`, `#open-weights`

---

<a id="item-12"></a>
## [Researcher uses Codex and ChatGPT to hunt new antimicrobials](https://openai.com/index/using-codex-chatgpt-to-search-for-new-antimicrobials) ⭐️ 7.0/10

César de la Fuente's lab is using OpenAI's Codex and ChatGPT to mine both living and extinct genomes for novel antimicrobial candidates to fight drug-resistant infections, as detailed in a new OpenAI blog case study. The work applies AI code generation and language models to accelerate the computational search for antibiotic peptides. Antimicrobial resistance is a growing global health crisis, and traditional antibiotic discovery has stalled as major pharmaceutical companies have largely exited the field. Demonstrating that general-purpose AI tools like Codex and ChatGPT can meaningfully accelerate early-stage drug discovery could inspire more labs to adopt AI-driven approaches and help fill the antibiotic pipeline. The approach builds on de la Fuente's prior 'molecular de-extinction' research, which uses machine learning to mine ancient paleoproteomes for antimicrobial peptides (AMPs) that show anti-infective efficacy in preclinical mouse models. Codex is used to help write and run the computational pipelines, while ChatGPT assists with analysis and reasoning tasks, though the blog post does not provide a detailed technical methodology.

rss · OpenAI Blog · Sep 10, 16:00

**Background**: Codex is OpenAI's code-generation model, originally announced in 2021 as a fine-tuned version of GPT-3 and the original engine behind GitHub Copilot; it has since evolved into a family of coding agents. Antimicrobial peptides are short proteins produced by many organisms as part of their innate immune defenses, and they are considered promising alternatives to conventional antibiotics because they can kill bacteria through mechanisms that are harder for pathogens to evade. 'Molecular de-extinction' refers to the idea of computationally resurrecting useful molecules encoded in the genomes of extinct species.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/s41587-023-01959-6">Mining extinct proteomes for antimicrobial peptides - Nature Molecular de-extinction of ancient antimicrobial peptides ... Molecular de-extinction of ancient antimicrobial peptides ... Molecular de-extinction of ancient antimicrobial peptides ... Molecular de-extinction of ancient antimicrobial peptides ... Molecular de-extinction of ancient antimicrobial peptides ... A review on the diversity of antimicrobial peptides and ...</a></li>
<li><a href="https://www.cell.com/cell-host-microbe/fulltext/S1931-3128(23)00296-2">Molecular de-extinction of ancient antimicrobial peptides ...</a></li>

</ul>
</details>

**Tags**: `#AI for science`, `#drug discovery`, `#antimicrobial resistance`, `#Codex`, `#ChatGPT`

---

<a id="item-13"></a>
## [OpenAI launches Data agent in ChatGPT Work](https://openai.com/index/put-data-to-work) ⭐️ 7.0/10

OpenAI has introduced a Data agent in ChatGPT Work that lets users connect company data, uncover insights, and build interactive dashboards using natural language. The agent is also available through the Data plugin in ChatGPT Work and Codex, allowing users to refine, validate, and publish analyses by asking follow-up questions in the same conversation. This marks OpenAI's notable expansion into enterprise analytics and business intelligence workflows, positioning ChatGPT as a tool for data-driven decision-making rather than just conversation. It could affect how business teams access and act on company data, potentially reducing reliance on specialized BI tools and data teams. The Data agent can connect to data sources such as Snowflake, BigQuery, and BI tools, and it uses connected company data and business context to analyze what changed and explain findings. Access control and enterprise safety considerations are highlighted as important factors given the sensitivity of connecting company data.

rss · OpenAI Blog · Sep 10, 15:00

**Background**: ChatGPT Work is OpenAI's enterprise-focused offering, and the Data agent is a specialized capability within it for data analysis tasks. Natural language to dashboard tools are an emerging category that lets users type requirements in plain English and receive visualizations, and OpenAI's entry brings this capability into its existing ChatGPT ecosystem. The Data plugin extends similar functionality to Codex, OpenAI's coding agent.

<details><summary>References</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001518">Using the Data plugin in ChatGPT Work and Codex</a></li>
<li><a href="https://www.xda-developers.com/openai-chatgpt-data-agent-announcement/">OpenAI reveals its new Data agent for ChatGPT Work to make ...</a></li>
<li><a href="https://www.explainx.ai/blog/openai-data-agent-chatgpt-work-enterprise-safety-2026">OpenAI Data Agent in ChatGPT Work (2026) | explainx.ai Blog</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#enterprise AI`, `#data analytics`, `#natural language interfaces`

---

<a id="item-14"></a>
## [OpenAI and GSA Expand Discounted AI Access to U.S. Governments](https://openai.com/index/expanding-ai-access-us-government) ⭐️ 7.0/10

OpenAI for Government and the U.S. General Services Administration (GSA) announced a new multi-year agreement that provides eligible federal, state, local, and tribal governments with $0 license fees (normally $15 per user per month), 50% off usage, and expanded cyber defense support. The deal builds on last year's federal offer and is described as a first-of-its-kind agreement. This significantly lowers the cost barrier for public-sector AI adoption, potentially accelerating deployment of AI tools across U.S. government agencies at all levels. It also signals closer collaboration between leading AI companies and government bodies on cybersecurity, which could shape broader AI policy and procurement standards. The agreement offers $0 license fees for eligible government users, a 50% discount on usage, and expanded cyber defense support, building on a prior federal offer. It is a multi-year commitment, though specific eligibility criteria and the full scope of cyber defense support were not detailed in the announcement.

rss · OpenAI Blog · Sep 10, 07:00

**Background**: The U.S. General Services Administration (GSA) is the federal agency that manages government procurement and shared services, helping agencies acquire technology and other goods efficiently. OpenAI for Government is OpenAI's initiative to provide AI tools to public-sector organizations. This partnership follows a broader trend of governments seeking to adopt AI while addressing cybersecurity risks, and it builds on an earlier federal offer made last year.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/expanding-ai-access-us-government/">Expanding AI access and cyber defense for federal ... - OpenAI</a></li>
<li><a href="https://www.govtech.com/security/openai-ms-isac-launch-ai-cyber-defense-pilot">OpenAI, MS-ISAC Launch AI Cyber Defense Pilot - govtech.com</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#government technology`, `#cybersecurity`, `#OpenAI`, `#public sector`

---

<a id="item-15"></a>
## [Paul Christiano Joins OpenAI Foundation Board](https://openai.com/index/paul-christiano-joins-openai-foundation-board) ⭐️ 7.0/10

Paul Christiano, a leading AI alignment researcher, has joined the OpenAI Foundation Board and its Safety and Security Committee, as announced by OpenAI. He brings deep experience in AI alignment, safety, and standards to the governance body. This appointment signals OpenAI's continued emphasis on safety and alignment at the highest governance level, especially given Christiano's prominent role in the field. It could influence how OpenAI balances rapid capability development with safety oversight, affecting the broader AI ecosystem. The Safety and Security Committee provides governance over safety and security practices across the entire organization, including the OpenAI Group PBC. Christiano's dual role on the Foundation Board and the committee gives him significant influence over safety oversight.

rss · OpenAI Blog · Sep 9, 17:00

**Background**: AI alignment is a subfield of AI safety focused on steering AI systems toward intended goals, preferences, or ethical principles, and it addresses challenges like reward hacking and strategic deception. The OpenAI Foundation holds special voting and governance rights, appointing all members of the OpenAI Group board and able to replace directors at any time. The Safety and Security Committee was created to oversee safety practices across OpenAI, and Paul Christiano is known for his work on alignment research, including at the now-dissolved Superalignment team.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/paul-christiano-joins-openai-foundation-board/">Paul Christiano joins OpenAI Foundation Board</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>
<li><a href="https://openai.com/our-structure/">Our structure - OpenAI</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#AI Safety`, `#AI Alignment`, `#Governance`, `#Personnel`

---