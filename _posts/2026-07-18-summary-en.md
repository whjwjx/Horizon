---
layout: default
title: "Horizon Summary: 2026-07-18 (EN)"
date: 2026-07-18
lang: en
---

> From 76 items, 15 important content pieces were selected

---

1. [AWS Billing Bug Shows $1.7 Billion Estimated Bill](#item-1) ⭐️ 9.0/10
2. [Firefox Compiled to WebAssembly Runs Inside Another Browser](#item-2) ⭐️ 9.0/10
3. [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Model](#item-3) ⭐️ 9.0/10
4. [xAI open-sources Grok Build after privacy backlash](#item-4) ⭐️ 9.0/10
5. [Anthropic Python SDK v0.117.0 Adds Dreaming and MCP Tunnels](#item-5) ⭐️ 8.0/10
6. [First Atmosphere Detected on Rocky Exoplanet in Habitable Zone](#item-6) ⭐️ 8.0/10
7. [Moonshot AI Unveils Kimi K3, a 2.8 Trillion Parameter Open-Weight Model](#item-7) ⭐️ 8.0/10
8. [GPT-5.6 Codex Bug Can Delete $HOME Directory](#item-8) ⭐️ 8.0/10
9. [Linus Torvalds: Linux Is Not Anti-AI, Fork If You Disagree](#item-9) ⭐️ 8.0/10
10. [CMOV Instruction: Surprisingly Expensive Due to False Dependencies](#item-10) ⭐️ 8.0/10
11. [1193 Backends Blocked on Append Operation](#item-11) ⭐️ 8.0/10
12. [SF orders Apple and Google to remove 'nudify' apps](#item-12) ⭐️ 7.0/10
13. [Apple's Lawsuit Could Disrupt OpenAI's IPO Plans](#item-13) ⭐️ 7.0/10
14. [Patreon blocks AI bots with Cloudflare, drops robots.txt reliance](#item-14) ⭐️ 7.0/10
15. [Zoox Recalls Robotaxis Over Smoke Confusion](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AWS Billing Bug Shows $1.7 Billion Estimated Bill](https://news.ycombinator.com/item?id=48945241) ⭐️ 9.0/10

An AWS billing system bug caused many users to see estimated bills as high as $1.7 billion due to a unit conversion error where bytes were used instead of gigabytes. This incident highlights the critical importance of accurate billing in cloud services, as such errors can cause panic and erode trust among customers, especially small businesses and individual developers. The bug occurred when the billing system defaulted to bytes instead of gigabytes for data transfer charges, multiplying costs by roughly 1 billion times. AWS acknowledged the issue and fixed it promptly.

hackernews · nprateem · Jul 17, 09:42

**Background**: AWS billing aggregates usage data from various services and applies pricing plans to generate estimated bills. A unit conversion error in the pricing plan definition can lead to wildly inflated estimates, as seen here.

**Discussion**: The community reacted with a mix of humor and concern, with many users sharing their own experiences of seeing huge estimated bills. Some commenters noted that similar unit errors have occurred before at AWS, indicating a recurring issue.

**Tags**: `#AWS`, `#billing`, `#bug`, `#cloud`, `#incident`

---

<a id="item-2"></a>
## [Firefox Compiled to WebAssembly Runs Inside Another Browser](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has successfully compiled the full Firefox browser to WebAssembly, allowing it to run inside another browser like Chrome. The project used an estimated $25,000 worth of AI tokens (Claude Opus and Fable) but cost much less due to a subscription plan. This demonstrates a groundbreaking technical achievement that could enable new levels of browser isolation, security, and web-based computing. It also showcases the potential of WebAssembly to run complex, full-featured applications within the browser. The demo uses the Wisp protocol to funnel all network traffic through Puter's server, as browser code cannot open arbitrary network connections. The project chose Firefox/Gecko for its strong single-process support, and claims end-to-end encryption is supported.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (Wasm) is a low-level binary instruction format that runs in modern web browsers with near-native performance, allowing languages like C/C++ and Rust to be compiled for the web. Compiling a full browser like Firefox to Wasm is an extremely complex task due to the browser's size and dependencies. The Wisp protocol is a low-overhead protocol for proxying multiple TCP/UDP sockets over a single WebSocket connection.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/WebAssembly">WebAssembly - MDN Web Docs - Mozilla</a></li>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly positive, with many impressed by the technical feat. Some comments noted the server scaling challenges due to traffic spikes, and there was curiosity about the practical applications and limitations of such a setup.

**Tags**: `#WebAssembly`, `#Firefox`, `#browser engineering`, `#compilation`, `#demo`

---

<a id="item-3"></a>
## [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 9.0/10

Thinking Machines Lab, founded by Mira Murati, released Inkling, a 975B total parameter (41B active) Mixture-of-Experts multimodal model under the Apache-2.0 license, trained on 45 trillion tokens of text, images, audio, and video. This release strengthens the US open-weights AI ecosystem, offering a competitive alternative to Chinese open models and providing a strong base for fine-tuning via the Tinker platform. The model card is sparse, with minimal training data documentation, and the model is not a frontier model but intended as a base for customization. A smaller 276B (12B active) variant, Inkling-Small, is still being tested.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) models use multiple specialized sub-networks (experts) and a gating mechanism to activate only a subset of parameters per input, enabling larger total parameter counts with lower computational cost. Open-weights models release trained parameters under permissive licenses like Apache-2.0, allowing free use, modification, and distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you've been told</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#Mira Murati`

---

<a id="item-4"></a>
## [xAI open-sources Grok Build after privacy backlash](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI has open-sourced the entire Grok Build codebase under the Apache 2.0 license after its CLI tool was found to upload entire directories to the cloud, including sensitive user files. The company also disabled the upload feature and deleted all previously retained user data. This incident highlights serious privacy risks in AI-powered developer tools and sets a precedent for transparency by open-sourcing the entire codebase. The move could restore user trust and influence how other AI companies handle data privacy. The Grok Build repository contains 844,530 lines of Rust code, with only about 3% vendored, and includes a self-contained terminal renderer for Mermaid diagrams. The codebase was released in a single commit, so no development history is visible.

rss · Simon Willison · Jul 15, 23:59

**Background**: Grok Build is xAI's terminal-based AI coding agent that runs as a full-screen TUI, capable of editing files, executing shell commands, and managing tasks. The Apache 2.0 license is a permissive open-source license that allows users to freely use, modify, and distribute the software.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xai-org/grok-build">xai-org/grok-build - GitHub</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>

</ul>
</details>

**Discussion**: The community expressed outrage over the privacy violation, with one user reporting that running the tool in their home directory uploaded SSH keys and password databases. Elon Musk responded by promising to delete all uploaded data, and the open-sourcing move was seen as a positive step to regain trust.

**Tags**: `#AI`, `#privacy`, `#open source`, `#xAI`, `#CLI`

---

<a id="item-5"></a>
## [Anthropic Python SDK v0.117.0 Adds Dreaming and MCP Tunnels](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.117.0) ⭐️ 8.0/10

Anthropic released v0.117.0 of its Python SDK, adding API support for dreaming and MCP Tunnels, and fixing a credential security issue by using SecretStr to keep credentials out of traceback frames. These features enable developers to build self-improving AI agents with persistent memory (dreaming) and securely connect to private MCP servers (MCP Tunnels), significantly expanding the capabilities and security of Anthropic's platform for enterprise use. Dreaming is in research preview and limited to Managed Agents, allowing agents to reflect on past sessions and store curated memories. MCP Tunnels, also in research preview, enable outbound-only connections to private MCP servers without opening inbound ports.

github · stainless-app[bot] · Jul 16, 19:36

**Background**: Anthropic's Claude platform offers Managed Agents as a pre-built agent harness for multi-step tasks. Dreaming lets agents create a curated memory store from past sessions, improving future performance. MCP Tunnels provide a secure way to connect Claude to internal systems via the Model Context Protocol without exposing them to the public internet.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/05/anthropics-claude-can-now-dream-sort-of/">Anthropic's Claude Managed Agents can now "dream," sort of - Ars Technica</a></li>
<li><a href="https://www.infoq.com/news/2026/05/claude-mcp-tunnels/">Anthropic Introduces MCP Tunnels for Private Agent Access to Internal Systems - InfoQ</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview">MCP tunnels - Claude Platform Docs</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#SDK`, `#Python`, `#API`, `#AI`

---

<a id="item-6"></a>
## [First Atmosphere Detected on Rocky Exoplanet in Habitable Zone](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

Astronomers using the James Webb Space Telescope have detected an atmosphere on LHS 1140 b, a rocky exoplanet located 48 light-years away in the habitable zone of its red dwarf star. This marks the first confirmed atmosphere on an Earth-like planet in a habitable zone. This discovery is a major milestone in exoplanet science, as it demonstrates that rocky planets in habitable zones can retain atmospheres, a key requirement for potential habitability. It also showcases JWST's capability to characterize temperate, Earth-sized worlds, bringing us closer to finding signs of life beyond Earth. LHS 1140 b is about 5.6 times Earth's mass and 1.7 times its radius, placing it in the super-Earth category, and is likely an ocean world with 9-19% water by mass. The planet receives 43% of the incident flux Earth gets from the Sun, and its atmosphere was confirmed via JWST emission spectroscopy as it passed behind its star.

hackernews · neversaydie · Jul 17, 14:06 · [Discussion](https://news.ycombinator.com/item?id=48947560)

**Background**: LHS 1140 b was discovered in 2017 by the MEarth Project and initially thought to be a dense rocky planet, but later measurements suggested a lower density consistent with a water-rich world. The habitable zone is the region around a star where liquid water could exist on a planet's surface. Red dwarfs like LHS 1140 are cooler and smaller than the Sun, making their habitable zones much closer, which historically raised concerns about atmospheric stripping due to stellar activity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LHS_1140_b">LHS 1140 b</a></li>
<li><a href="https://www.bbc.com/news/articles/cy4kdd1e0ejo">First atmosphere found around Earth-like planet LHS 1140 b</a></li>
<li><a href="https://lweb.cfa.harvard.edu/MEarth/lhs1140b.pdf">LHS 1140 b _arXiv</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a mix of excitement and skepticism. Some questioned whether a rocky planet around a red dwarf could retain an atmosphere, but others noted that JWST data ruled out a mini-Neptune scenario. There were also discussions about the Fermi paradox and the narrow time window for technological civilizations, as well as suggestions to build a solar lens telescope for future observations.

**Tags**: `#exoplanets`, `#astronomy`, `#JWST`, `#habitability`, `#atmosphere`

---

<a id="item-7"></a>
## [Moonshot AI Unveils Kimi K3, a 2.8 Trillion Parameter Open-Weight Model](https://simonwillison.net/2026/Jul/16/kimi-k3/#atom-everything) ⭐️ 8.0/10

Moonshot AI announced Kimi K3, a 2.8 trillion parameter open-weight model that outperforms GPT-5.5 and Claude Opus 4.8 on several benchmarks, with an open-weight release promised by July 27, 2026. Kimi K3 is the largest open-weight model to date, signaling a new scale frontier for open AI research and potentially democratizing access to cutting-edge capabilities. The model costs $3 per million input tokens and $15 per million output tokens, making it the most expensive Chinese AI lab model yet, and it uses 21% fewer output tokens than its predecessor K2.6 on the Artificial Analysis Intelligence Index.

rss · Simon Willison · Jul 16, 20:19

**Background**: Open-weight models release trained parameters but not the full training pipeline, allowing researchers to fine-tune and deploy them. Moonshot AI is one of China's 'AI Tigers' competing with frontier labs like OpenAI and Anthropic. The 'pelican benchmark' is an informal test where models generate an SVG of a pelican riding a bicycle, used to qualitatively compare model capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/16/kimi-k3/">Kimi K3, and what we can still learn from the pelican benchmark</a></li>
<li><a href="https://huggingface.co/spaces/victor/pelican-benchmark">Pelican Benchmark - a Hugging Face Space by victor</a></li>
<li><a href="https://en.wikipedia.org/wiki/Moonshot_AI">Moonshot AI</a></li>

</ul>
</details>

**Discussion**: The community discussion is not provided in the input, so this field is left empty.

**Tags**: `#AI`, `#large language models`, `#open-weight`, `#benchmarks`, `#Moonshot AI`

---

<a id="item-8"></a>
## [GPT-5.6 Codex Bug Can Delete $HOME Directory](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

A bug in GPT-5.6's Codex agent can cause it to delete the user's $HOME directory instead of a temporary directory when full access mode is enabled without sandboxing. This bug highlights critical safety risks in AI coding agents, which can have destructive consequences if not properly sandboxed, especially as such agents become more autonomous. The bug occurs when Codex attempts to override the $HOME environment variable to define a temporary directory but mistakenly deletes $HOME instead. It requires full access mode and no sandboxing or auto-review to trigger.

rss · Simon Willison · Jul 16, 17:45

**Background**: Codex is an AI coding agent from OpenAI that runs locally or in the cloud to automate software engineering tasks. Sandboxing isolates the agent's execution environment to prevent it from affecting the host system. The $HOME environment variable points to the user's home directory, which contains personal files and configurations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in your terminal · GitHub</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor... — Northflank</a></li>
<li><a href="https://www.hostinger.com/tutorials/linux-environment-variables">How to Manage Linux Environment Variables in 2026 + Tips</a></li>

</ul>
</details>

**Tags**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`, `#bug`

---

<a id="item-9"></a>
## [Linus Torvalds: Linux Is Not Anti-AI, Fork If You Disagree](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds explicitly stated on the Linux Media mailing list that Linux is not an anti-AI project and that AI is a clearly useful tool, inviting dissenters to fork the kernel or walk away. This strong endorsement from the Linux creator signals a major policy stance, likely influencing the open-source community's acceptance of AI tools in kernel development and beyond. Torvalds emphasized that AI's usefulness is no longer in question, though he acknowledged other open questions about AI's economic impact. The statement was made in the context of kernel development discussions.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linus Torvalds is the creator and longtime maintainer of the Linux kernel, one of the largest open-source projects. AI tools, especially large language models, have been increasingly used in software development, but some community members have raised ethical and practical concerns.

**Tags**: `#Linux`, `#AI`, `#Open Source`, `#Kernel Development`

---

<a id="item-10"></a>
## [CMOV Instruction: Surprisingly Expensive Due to False Dependencies](https://www.reddit.com/r/programming/comments/1uyt0tf/the_most_expensive_instruction_might_be_cmov/) ⭐️ 8.0/10

A technical analysis reveals that the CMOV (conditional move) instruction on x86 can be surprisingly expensive due to false dependencies and increased register pressure, challenging the common belief that it always outperforms branches. This insight is crucial for low-level optimization and systems programming, as developers often use CMOV to avoid branch misprediction penalties, but may inadvertently degrade performance in certain scenarios. The CMOV instruction creates a false dependency on the destination register, tying it to previous computations and limiting out-of-order execution. Additionally, using CMOV can increase register pressure, potentially causing spills and further slowdowns.

reddit · r/programming · /u/_shadowbannedagain · Jul 17, 07:44

**Background**: CMOV is an x86 instruction that conditionally moves data based on flags, avoiding branch mispredictions. However, on out-of-order CPUs, it introduces a data dependency that can stall the pipeline. The trade-off between CMOV and conditional branches depends on branch predictability and code size.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rcollins.org/p6/opcodes/CMOV.html">New P6 OpCodes: CMOV - Conditional Move - rcollins.org</a></li>
<li><a href="https://www.reddit.com/r/programming/comments/8fqgy/cmov_instruction_a_bad_idea_on_outoforder_cpus/">r/programming on Reddit: CMOV instruction a bad idea on out-of-order CPUs - a.k.a. why to compile for i586 not i686</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion highlights that CMOV performance has improved in recent cores, but the triple input-dependency issue persists. Some commenters note that compilers often overuse CMOV, and manual tuning is still needed for optimal performance.

**Tags**: `#x86`, `#assembly`, `#performance`, `#optimization`, `#low-level`

---

<a id="item-11"></a>
## [1193 Backends Blocked on Append Operation](https://www.reddit.com/r/programming/comments/1uzdl0h/1193_backends_waiting_on_an_append/) ⭐️ 8.0/10

A deep-dive analysis reveals that 1193 backend services are blocked waiting on a single append operation, exposing a severe performance bottleneck in a distributed system. This bottleneck can cause cascading failures and degrade system throughput, highlighting the critical need for careful design of append-heavy workloads in distributed databases or log systems. The analysis likely involves a replicated log (e.g., Raft) where all writes go through a single leader, making the append operation a serialization point. The number 1193 suggests a large-scale deployment with many followers waiting for the leader's append to complete.

reddit · r/programming · /u/andreiross · Jul 17, 22:01

**Background**: In distributed consensus algorithms like Raft, all write operations must be appended to the leader's log before being replicated to followers. The leader becomes a bottleneck under high write loads, as every append must complete before the next can proceed. This design ensures consistency but can lead to performance issues when many backends depend on the same leader.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@Omkar-Wagholikar/distributed-systems-deep-dive-single-leader-replication-0a96fb303036">Distributed Systems Deep Dive: Single Leader Replication | by Omkar Wagholikar | Medium</a></li>
<li><a href="https://medium.com/@vishalgoel2668/solving-performance-bottlenecks-in-complex-distributed-systems-a-practical-guide-7015f2fba76f">Solving Performance Bottlenecks in Complex Distributed Systems: A Practical Guide | by Vishalgoel | Medium</a></li>

</ul>
</details>

**Tags**: `#distributed systems`, `#performance`, `#backend`, `#database`, `#concurrency`

---

<a id="item-12"></a>
## [SF orders Apple and Google to remove 'nudify' apps](https://techcrunch.com/2026/07/17/apple-and-google-ordered-to-purge-nudify-apps-from-app-stores/) ⭐️ 7.0/10

San Francisco City Attorney David Chiu sent letters to Apple and Google ordering them to remove 'nudify' apps from their app stores, citing violations of state law. This regulatory action targets major tech platforms over harmful deepfake apps, potentially setting a precedent for app store policies and user safety enforcement. The letters claim that Apple and Google have long been aware that they are hosting apps violating state law. 'Nudify' apps use AI to create non-consensual deepfake nude images, which are illegal in many jurisdictions.

rss · TechCrunch · Jul 17, 19:49

**Background**: Deepfake pornography uses AI to alter photos or videos to depict individuals nude without consent, often used for revenge porn. Such technology has existed for years but has become more accessible through apps and online tools, prompting legal and regulatory scrutiny.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nudify_apps">Nudify apps</a></li>
<li><a href="https://www.theguardian.com/news/ng-interactive/2026/jan/11/how-grok-nudification-tool-went-viral-x-elon-musk">‘Add blood, forced smile’: how Grok’s nudification tool... | The Guardian</a></li>

</ul>
</details>

**Tags**: `#app stores`, `#regulation`, `#privacy`, `#safety`, `#tech policy`

---

<a id="item-13"></a>
## [Apple's Lawsuit Could Disrupt OpenAI's IPO Plans](https://techcrunch.com/video/how-apples-big-lawsuit-could-disrupt-openais-ipo-plans/) ⭐️ 7.0/10

Apple filed a trade secrets lawsuit against OpenAI last Friday, alleging a pattern of misconduct and claiming over 400 former Apple employees now work at OpenAI. The lawsuit could disrupt OpenAI's reported IPO plans. This lawsuit could delay or derail OpenAI's IPO, impacting its valuation and ability to raise capital. It also highlights the intense competition for AI talent and intellectual property between major tech companies. The complaint alleges misconduct reaching up to OpenAI's chief hardware officer. OpenAI's response has been carefully hedged, and the timing is critical as the company reportedly eyes an IPO.

rss · TechCrunch · Jul 17, 17:45

**Background**: Trade secrets lawsuits are legal actions to protect confidential business information. Apple and OpenAI are major players in AI, with Apple focusing on on-device AI and OpenAI on large language models. The lawsuit alleges that OpenAI hired former Apple employees who brought trade secrets with them.

**Tags**: `#Apple`, `#OpenAI`, `#lawsuit`, `#IPO`, `#AI`

---

<a id="item-14"></a>
## [Patreon blocks AI bots with Cloudflare, drops robots.txt reliance](https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/) ⭐️ 7.0/10

Patreon has partnered with Cloudflare to actively block AI bots from scraping creator content, moving away from relying solely on the voluntary robots.txt protocol. This shift represents a significant escalation in the fight against unauthorized AI training data collection, setting a precedent for other platforms to adopt active blocking measures and better protect creator rights. Patreon uses Cloudflare's Bot Management service, which provides real-time bot detection and mitigation at the network edge without adding latency for legitimate users. The move comes amid a 340% increase in AI crawler traffic from 2023 to 2024.

rss · TechCrunch · Jul 17, 15:21

**Background**: Robots.txt is a standard from 1994 that tells web crawlers which parts of a site they may access, but compliance is voluntary and often ignored by AI companies. Cloudflare's Bot Management provides granular control, per-request bot scoring, and automatic blocking of malicious bots, making it a more effective defense than passive text files.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/bots/get-started/bot-management/">Bot Management · Cloudflare bot solutions docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Robots.txt">robots . txt - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI scraping`, `#Patreon`, `#Cloudflare`, `#creator rights`, `#web scraping`

---

<a id="item-15"></a>
## [Zoox Recalls Robotaxis Over Smoke Confusion](https://techcrunch.com/2026/07/17/zoox-issues-software-recall-after-a-robotaxi-got-confused-by-heavy-smoke/) ⭐️ 7.0/10

Zoox issued a software recall for 105 robotaxis after one of its vehicles failed to navigate heavy smoke at a fire scene in June 2026. The company deployed a software update to address the issue. This incident highlights a critical failure mode for autonomous vehicles—heavy smoke—and comes amid heightened regulatory scrutiny from NHTSA, which warned that AVs interfering with first responders pose a danger to the public. The recall covers 105 Zoox robotaxis, and the software update aims to improve detection and navigation in smoke-filled environments. Zoox previously recalled 332 vehicles in December 2025 for a separate software error involving lane crossings.

rss · TechCrunch · Jul 17, 14:12

**Background**: Autonomous vehicles rely on sensors like cameras, lidar, and radar to perceive their environment. Heavy smoke can degrade sensor performance, causing confusion. NHTSA has recently warned AV developers that vehicles must safely interact with first responders, citing multiple incidents of interference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/07/17/amazon-zoox-recalls-robotaxi-smoke.html">Amazon's Zoox issues software recall after robotaxi drove into heavy smoke</a></li>
<li><a href="https://techcrunch.com/2026/07/17/zoox-issues-software-recall-after-a-robotaxi-got-confused-by-heavy-smoke/">Zoox issues software recall after a robotaxi got confused by heavy smoke | TechCrunch</a></li>
<li><a href="https://www.nhtsa.gov/press-releases/av-developers-automated-vehicle-that-cannot-safely-interact-first-responders-danger">Trump’s Transportation Department to AV Developers: ‘An Automated Vehicle That Cannot Safely Interact With First Responders is a Danger to the General Public’ | NHTSA</a></li>

</ul>
</details>

**Tags**: `#autonomous vehicles`, `#software recall`, `#safety`, `#regulation`, `#Zoox`

---