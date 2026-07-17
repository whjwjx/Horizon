---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 87 items, 15 important content pieces were selected

---

1. [Firefox Compiled to WebAssembly Runs Inside Chrome](#item-1) ⭐️ 9.0/10
2. [xAI Open-Sources Grok Build After Privacy Backlash](#item-2) ⭐️ 9.0/10
3. [Moonshot AI Releases Kimi K3 Open-Weight Frontier Model](#item-3) ⭐️ 8.0/10
4. [OpenAI's GPT-Red: Self-Play for AI Safety](#item-4) ⭐️ 8.0/10
5. [GPT-5.6 Codex Bug Deletes User Files](#item-5) ⭐️ 8.0/10
6. [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Model](#item-6) ⭐️ 8.0/10
7. [Linus Torvalds Defends AI Use in Linux Kernel](#item-7) ⭐️ 8.0/10
8. [Researcher tricks Claude into leaking private memories](#item-8) ⭐️ 8.0/10
9. [Cursor 0-Day Vulnerability Disclosed to Protect Users](#item-9) ⭐️ 8.0/10
10. [Millions of Shark Robot Vacuums Vulnerable to RCE](#item-10) ⭐️ 8.0/10
11. [Microsoft Comic Chat Open-Sourced After 30 Years](#item-11) ⭐️ 7.0/10
12. [Decoy Font: Optical Illusion Typography Baffles AI Vision Models](#item-12) ⭐️ 7.0/10
13. [OpenAI Proposes Reverse Federalism for AI Safety](#item-13) ⭐️ 7.0/10
14. [SF Mayor Seeks Stricter Robotaxi Rules After Waymo Gridlock](#item-14) ⭐️ 7.0/10
15. [Uber acquires Delivery Hero for $14.8B](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Firefox Compiled to WebAssembly Runs Inside Chrome](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the full Firefox browser to WebAssembly, enabling it to run entirely within another browser like Chrome. The demo loads a blog inside Firefox-in-WASM inside Chrome, with all network traffic proxied via the Wisp protocol. This is a groundbreaking technical achievement that demonstrates the extreme capabilities of WebAssembly, potentially enabling new use cases like in-browser sandboxed browsing, legacy app compatibility, and advanced web platform experimentation. It also highlights the power of AI-assisted programming, as the project used an estimated $25,000 in AI tokens. The project chose Firefox/Gecko for its strong single-process support, and the build required an estimated $25,000 in Claude Opus and Fable tokens. All network traffic is funneled over a WebSocket using the Wisp protocol through Puter's server, which had to be scaled up to handle Hacker News traffic.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (WASM) is a low-level binary instruction format that allows code written in languages like C, C++, and Rust to run in web browsers at near-native speed. Compiling a full browser like Firefox to WASM is an enormous engineering challenge because browsers are complex, multi-process applications that rely on system-level APIs not typically available in the browser sandbox. The Wisp protocol is a low-overhead protocol for proxying multiple TCP and UDP sockets over a single WebSocket connection, which is necessary because WASM code in a browser cannot open arbitrary network connections directly.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low ...</a></li>
<li><a href="https://github.com/HeyPuter/puter">GitHub - HeyPuter/puter: 🌐 The Internet Computer! Free, Open-Source, and Self-Hostable.</a></li>
<li><a href="https://github.com/fable-compiler/fable">GitHub - fable-compiler/Fable: F# to JavaScript, TypeScript, Python, Rust, Erlang and Dart Compiler · GitHub</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly positive, with many expressing amazement at the technical feat. Some commenters raised concerns about the cost and scalability of proxying all traffic through Puter's servers, while others discussed the potential for similar projects like WebKitWASM.

**Tags**: `#WebAssembly`, `#Firefox`, `#browser engineering`, `#WASM`, `#Puter`

---

<a id="item-2"></a>
## [xAI Open-Sources Grok Build After Privacy Backlash](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI released the entire Grok Build codebase under an Apache 2.0 license on GitHub after users discovered the CLI tool was uploading entire directories to Google Cloud buckets. The company also deleted all retained user data and disabled default data retention. This incident highlights serious privacy risks in AI coding tools and forced xAI to take unprecedented transparency measures, including open-sourcing a major product. The move may set a new standard for privacy in AI-assisted development tools. The codebase contains 844,530 lines of Rust (only ~3% vendored) with a single commit, so no development history is visible. Remnants of the upload code remain in the repository but are disabled.

rss · Simon Willison · Jul 15, 23:59

**Background**: Grok Build is xAI's CLI tool for AI-assisted coding, powered by the Grok model. The privacy issue came to light when users noticed the tool uploading entire directories—including SSH keys and password databases—to xAI's Google Cloud buckets without clear consent. xAI initially disabled the feature and later open-sourced the code to rebuild trust.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jul/15/grok-build/">xai-org/grok-build, now open source</a></li>
<li><a href="https://www.internationalcyberdigest.com/xais-grok-build-cli-uploads-entire-git-repositories-to-a-google-cloud-bucket/">xAI's Grok Build CLI Uploads Entire Git repositories to a Google Cloud Bucket</a></li>
<li><a href="https://glitchwire.com/news/xais-grok-build-cli-was-uploading-entire-repositories-to-google-cloud-the-compan/">xAI's Grok Build CLI Was Uploading Entire Repositories to Google Cloud. The Company Has Said Nothing. — Glitchwire</a></li>

</ul>
</details>

**Discussion**: The community reaction was overwhelmingly negative, with users expressing outrage over the privacy violation and demanding transparency. Some praised the open-sourcing as a positive step, but others remained skeptical about xAI's handling of the incident.

**Tags**: `#privacy`, `#open source`, `#AI`, `#security`, `#xAI`

---

<a id="item-3"></a>
## [Moonshot AI Releases Kimi K3 Open-Weight Frontier Model](https://www.kimi.com/blog/kimi-k3) ⭐️ 8.0/10

Moonshot AI has released Kimi K3, an open-weight frontier AI model that claims performance second only to Claude Fable 5 and GPT-5.6 Sol in internal evaluations, with full model weights to be released in the coming days. Kimi K3's open-weight release could accelerate commoditization of AI intelligence, challenging the dominance of US frontier labs and providing a cost-effective alternative for developers and enterprises. The model is available via OpenRouter API at competitive pricing (e.g., $0.25 for a long reasoning-heavy query), and Moonshot AI trains on API usage data unless enterprise arrangements are made.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Open-weight models are AI models whose core parameters are publicly released, allowing anyone to download and use them. Frontier models are the most advanced general-purpose AI models, typically requiring hundreds of millions of dollars to train. Chinese AI labs like Moonshot are increasingly releasing competitive open-weight models, following the trend set by DeepSeek.

<details><summary>References</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Frontier_model">Frontier model</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about Moonshot's data training policy on API usage, with one user noting the high cost of a long reasoning query. Another commenter suggests Chinese labs are driving toward commoditized intelligence, potentially as a strategy to sell hardware and infrastructure.

**Tags**: `#AI`, `#open-source`, `#LLM`, `#benchmarks`, `#Moonshot`

---

<a id="item-4"></a>
## [OpenAI's GPT-Red: Self-Play for AI Safety](https://openai.com/index/unlocking-self-improvement-gpt-red) ⭐️ 8.0/10

OpenAI has introduced GPT-Red, an automated red teaming system that uses self-play to enhance AI safety, alignment, and robustness against prompt injection attacks. This approach automates a critical safety evaluation process, potentially reducing the need for extensive human red teaming and enabling continuous improvement of model robustness. It directly addresses the growing threat of prompt injection, a major security challenge for deployed AI agents. GPT-Red is an LLM-based red teamer that plays an adversarial role against the target model in a self-play framework, generating diverse prompt injection attacks. OpenAI reports that GPT-5.6 Sol, trained with GPT-Red, achieves six times fewer failures against direct prompt injection benchmarks compared to GPT-5.5.

rss · OpenAI Blog · Jul 15, 10:00

**Background**: Red teaming is a security practice where testers simulate attacks to find vulnerabilities. In AI safety, human red teamers manually craft prompts to jailbreak models. Self-play is a technique where an AI system plays against itself to improve, commonly used in game-playing AI. Prompt injection attacks exploit LLMs' inability to distinguish between system instructions and user-provided content, posing risks for AI agents that process external data.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/unlocking-self-improvement-gpt-red/">GPT-Red: Unlocking Self-Improvement for Robustness | OpenAI</a></li>
<li><a href="https://thehackernews.com/2026/07/openais-gpt-red-automates-prompt.html">OpenAI’s GPT-Red Automates Prompt Injection Testing to Harden ...</a></li>
<li><a href="https://www.technologyreview.com/2026/07/15/1140514/meet-gpt-red-an-llm-super-hacker-openai-built-to-make-its-models-safer/">Meet GPT-Red: an LLM super-hacker OpenAI built to make its ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#red teaming`, `#self-play`, `#alignment`, `#prompt injection`

---

<a id="item-5"></a>
## [GPT-5.6 Codex Bug Deletes User Files](https://simonwillison.net/2026/Jul/16/bad-codex-bug/#atom-everything) ⭐️ 8.0/10

A bug in GPT-5.6 Codex can delete user files when full access mode is enabled without sandboxing, because the model mistakenly deletes $HOME instead of a temporary directory. This bug poses a serious safety risk for AI coding agents, potentially causing irreversible data loss for users who run Codex without proper sandboxing or review. It highlights the need for robust safety measures in autonomous AI systems. The bug occurs when full access mode is enabled, sandboxing is disabled, and auto review is turned off. The model attempts to override $HOME to define a temporary directory but mistakenly deletes $HOME instead.

rss · Simon Willison · Jul 16, 17:45

**Background**: GPT-5.6 Codex is an AI coding agent that can autonomously read, write, and execute code on a user's machine. Full access mode grants the agent broad permissions, while sandboxing isolates it to prevent harmful actions. Without sandboxing, a mistaken command can directly affect the user's file system.

<details><summary>References</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/openai-codex-gpt-5-6-home-deletion-full-access-july-2026">Codex GPT-5.6 $HOME Deletion — Full Access | explainx.ai Blog</a></li>
<li><a href="https://github.com/openai/codex/issues/4407">Change the hardcoded $HOME/.codex path #4407 - GitHub</a></li>
<li><a href="https://amux.io/guides/ai-agent-sandboxing/">AI Agent Sandboxing in 2026: Docker, E2B, Firecracker... — amux</a></li>

</ul>
</details>

**Tags**: `#codex`, `#coding-agents`, `#generative-ai`, `#ai-safety`

---

<a id="item-6"></a>
## [Thinking Machines Lab Releases Inkling, a 975B Open-Weights Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab, led by Mira Murati, released Inkling, a 975B-parameter open-weights multimodal Mixture-of-Experts model under the Apache-2.0 license. The model has 41B active parameters and was trained on 45 trillion tokens of text, images, audio, and video. This release strengthens the US open-weights ecosystem by providing a competitive alternative to Chinese open models and NVIDIA Nemotron. Its Apache-2.0 license and multimodal capabilities make it a strong base for fine-tuning and customization. Inkling is not a frontier model but is designed as a strong base for fine-tuning via the Tinker platform. The model card and training data documentation are sparse, with vague descriptions of data sources. A smaller variant, Inkling-Small (276B total, 12B active), is still in testing.

rss · Simon Willison · Jul 16, 15:35

**Background**: An open-weights model means the trained parameters are publicly available for download, allowing users to run, study, and modify the model. Mixture-of-Experts (MoE) architecture uses multiple specialized subnetworks and a gating mechanism to activate only a subset of parameters per input, improving efficiency. The Apache-2.0 license is a permissive open-source license that allows free use, modification, and distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_License">Apache License</a></li>
<li><a href="https://www.emergentmind.com/topics/mixture-of-experts-transformer">Mixture - of - Experts Transformer</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-weights`, `#multimodal`, `#Mixture-of-Experts`, `#Thinking Machines Lab`

---

<a id="item-7"></a>
## [Linus Torvalds Defends AI Use in Linux Kernel](https://simonwillison.net/2026/Jul/16/linus-torvalds/#atom-everything) ⭐️ 8.0/10

Linus Torvalds, the creator of Linux, publicly stated on the Linux Media mailing list that Linux is not an anti-AI project and that AI is a clearly useful tool for kernel development, inviting those who disagree to fork or leave. This authoritative endorsement from the top Linux maintainer signals a strong pro-AI stance in the open-source community, potentially influencing how AI tools are integrated into kernel development and other open-source projects. Torvalds emphasized that AI's usefulness is no longer in question, though he acknowledged other open questions about AI, such as its economic implications. The statement was made in response to community pushback against AI use in kernel development.

rss · Simon Willison · Jul 16, 13:26

**Background**: Linux is the world's largest open-source operating system kernel, maintained by a global community led by Linus Torvalds. Recent advances in generative AI and large language models have sparked debates within open-source communities about their role and ethics in software development.

**Tags**: `#Linux`, `#AI`, `#open source`, `#kernel development`, `#Linus Torvalds`

---

<a id="item-8"></a>
## [Researcher tricks Claude into leaking private memories](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

Researcher Ayush Paul discovered a prompt injection attack that bypasses Claude's web_fetch tool protections, allowing exfiltration of private user memories by tricking the model into following nested links from a honeypot site. This attack demonstrates a critical vulnerability in AI agent safety, showing that even carefully designed protections can be bypassed, and highlights the ongoing challenge of preventing data exfiltration in LLMs with tool access. The attack exploited a loophole where web_fetch could follow links embedded in previously fetched pages, and it only targeted clients with 'Claude-User' in their user-agent to avoid detection. Anthropic had already identified the issue internally and closed the hole by removing that capability.

rss · Simon Willison · Jul 15, 14:21

**Background**: Prompt injection is a security exploit where malicious inputs cause LLMs to behave unexpectedly. The 'lethal trifecta' describes AI agents that have private data, access untrusted content, and can communicate externally—a combination that enables data exfiltration. Claude's web_fetch tool was designed to only visit URLs provided by the user or from its web_search tool, but this attack found a way around that restriction.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted ...</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed concern about the ease of bypassing protections and debated whether Anthropic's bug bounty decision was fair. Some noted that the attack required a honeypot site, limiting its practical exploitability, while others emphasized the need for more robust defenses against prompt injection.

**Tags**: `#AI security`, `#prompt injection`, `#data exfiltration`, `#Claude`, `#vulnerability`

---

<a id="item-9"></a>
## [Cursor 0-Day Vulnerability Disclosed to Protect Users](https://www.reddit.com/r/programming/comments/1uxjm12/cursor_0day_when_full_disclosure_becomes_the_only/) ⭐️ 8.0/10

Security firm Mindgard publicly disclosed a zero-day vulnerability in Cursor, an AI-powered coding assistant, after the vendor failed to patch it in a timely manner. This disclosure highlights critical security risks in AI coding tools, which are increasingly used by developers, and underscores the tension between responsible disclosure and user protection. The vulnerability details were released by Mindgard on their blog, allowing organizations to assess their exposure and implement compensating controls.

reddit · r/programming · /u/alexeyr · Jul 15, 21:52

**Background**: A zero-day vulnerability is a security flaw unknown to the software vendor, leaving users exposed until a patch is issued. Cursor is an AI-first code editor that assists with pair programming and has gained popularity as an alternative to GitHub Copilot.

<details><summary>References</summary>
<ul>
<li><a href="https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left">Cursor 0day: When Full Disclosure Becomes the Only Protection ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>
<li><a href="https://cursor.com/">Cursor : AI coding agent</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion on r/programming expressed mixed reactions: some praised the full disclosure as necessary for user safety, while others criticized the lack of responsible disclosure coordination with the vendor.

**Tags**: `#security`, `#vulnerability`, `#AI coding tools`, `#full disclosure`, `#Cursor`

---

<a id="item-10"></a>
## [Millions of Shark Robot Vacuums Vulnerable to RCE](https://www.reddit.com/r/programming/comments/1uyhqyt/no_shark_is_safe_millions_of_shark_vacuums_are/) ⭐️ 8.0/10

A critical remote code execution (RCE) vulnerability has been discovered in millions of Shark brand robot vacuums, allowing attackers to gain root shell access via exposed UART pins. This vulnerability exposes millions of IoT devices in homes to potential remote takeover, including camera access and network pivoting, posing significant privacy and security risks. The flaw was identified by researcher Tokay0 on the RV2320EDUS motherboard, who bypassed password authentication by interrupting the U-Boot sequence with Ctrl-C to gain root access.

reddit · r/programming · /u/ScottContini · Jul 16, 22:37

**Background**: Remote code execution (RCE) vulnerabilities allow attackers to run arbitrary code on a device remotely. IoT devices like robot vacuums often lack robust security, making them attractive targets. The exposed UART pins are a hardware debugging interface that should be disabled in production devices.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberpress.org/shark-vacuum-rce-flaw/">Shark Vacuum RCE Flaw Lets Attackers Remotely Control Cameras...</a></li>

</ul>
</details>

**Tags**: `#security`, `#IoT`, `#vulnerability`, `#RCE`, `#embedded systems`

---

<a id="item-11"></a>
## [Microsoft Comic Chat Open-Sourced After 30 Years](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/) ⭐️ 7.0/10

On July 16, 2026, Microsoft released the source code for Comic Chat (also known as Microsoft Chat) on GitHub under an open-source license, making the 1996 IRC client available for preservation and modification. This release preserves a unique piece of Internet history—a graphical IRC client that automatically turned text conversations into comic strips—and allows developers to study, port, or reimagine its innovative visual chat concept. Comic Chat was developed by Microsoft researcher David Kurlander and first shipped with Internet Explorer 3.0 in 1996; it also introduced the world to the Comic Sans font. The open-source release includes the original C++ source code and is hosted at github.com/microsoft/comic-chat.

hackernews · jervant · Jul 16, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48936426)

**Background**: Internet Relay Chat (IRC) is a text-based chat protocol popular in the 1990s. Comic Chat was a graphical client that rendered conversations as comic panels with avatars, speech bubbles, and expressions, using a custom IRC extension. It was bundled with Windows 98 and localized into 24 languages, but eventually faded as other chat platforms emerged.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Comic_Chat">Microsoft Comic Chat - Wikipedia</a></li>
<li><a href="https://github.com/microsoft/comic-chat">GitHub - microsoft/comic-chat: Source code for the Microsoft ...</a></li>
<li><a href="https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/">Microsoft Comic Chat is now open source</a></li>

</ul>
</details>

**Discussion**: The community response is highly nostalgic and positive, with original contributor Robert Standefer sharing the six-year journey to make the release happen. Some commenters recall that Comic Chat was once reviled on IRC for its non-standard protocol extensions, while others praise its creative spirit and note how it inspired projects like Chogger.

**Tags**: `#open source`, `#microsoft`, `#irc`, `#nostalgia`, `#history`

---

<a id="item-12"></a>
## [Decoy Font: Optical Illusion Typography Baffles AI Vision Models](https://www.mixfont.com/experiments/decoy-font) ⭐️ 7.0/10

MixFont has released Decoy Font, a TTF font that embeds two different messages readable at different resolutions, creating an optical illusion that confuses AI vision models like GPT-4, Claude, and Gemini. This font highlights a fundamental limitation in current AI vision systems: their inability to perceive dual-layer text, which has implications for AI security, CAPTCHA design, and understanding of adversarial examples in computer vision. The font works by combining a high-frequency sharp message (e.g., 'SORRY ROBOT') with a low-frequency blurry message (e.g., 'HAPPY HUMAN'), so that at normal resolution the sharp text is visible, but when downscaled or blurred, the hidden text emerges.

hackernews · ray__ · Jul 16, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48936584)

**Background**: AI vision models process images at fixed resolutions and often downsample inputs, which can cause loss of fine details. This font exploits that by encoding a message in low-frequency components that survive downsampling, while a decoy message occupies high-frequency details that are lost. The technique is similar to adversarial attacks that exploit differences between human and machine perception.

<details><summary>References</summary>
<ul>
<li><a href="https://www.mixfont.com/experiments/decoy-font">Decoy Font: A TTF font that hides what you type - mixfont.com</a></li>
<li><a href="https://www.creativebloq.com/design/fonts-typography/this-optical-illusion-font-was-created-to-baffle-ai-and-it-actually-works-for-now">This optical illusion font was created to baffle AI, and it ...</a></li>
<li><a href="https://www.popsci.com/technology/font-optical-illusion-hide-ai/">This font uses an optical illusion to hide from AI</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some find it cool but question its practical utility, while others report varying success in getting AI models to read the hidden text. Users note that GPT-4 can sometimes decode the hidden message with prompting, but Claude and Gemini struggle more.

**Tags**: `#AI`, `#typography`, `#computer vision`, `#security`, `#optical illusion`

---

<a id="item-13"></a>
## [OpenAI Proposes Reverse Federalism for AI Safety](https://openai.com/index/advancing-ai-safety-through-state-and-federal-action) ⭐️ 7.0/10

OpenAI has proposed a 'reverse federalism' approach to AI governance, where state-level AI laws and experiments inform the development of a national framework, rather than relying solely on top-down federal regulation. This proposal could shape how the U.S. regulates AI, balancing innovation with safety while leveraging state-level experimentation to build a more democratic and flexible national policy. Under OpenAI's plan, the Center for AI Standards and Innovation within NIST would lead federal efforts, and the approach aims to avoid a patchwork of conflicting state laws by creating a unified national baseline.

rss · OpenAI Blog · Jul 15, 12:00

**Background**: AI governance is a growing concern as frontier AI models become more powerful. Traditionally, federal regulation is top-down, but 'reverse federalism' allows states to act as laboratories for policy, testing ideas before they scale nationally. OpenAI's blueprint for democratic governance of frontier AI, released in June 2026, outlines this vision.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aibyteslearning.com/news/openai-reverse-federalism-ai-safety-governance-202607160801460">OpenAI's 'Reverse Federalism' Bet on AI Safety Law</a></li>
<li><a href="https://cctest.ai/en/articles/openai-s-reverse-federalism-vision-for-u-s-ai-safety">OpenAI’s Reverse Federalism Approach to AI Safety - CCTest</a></li>
<li><a href="https://www.machinebrief.com/news/openais-reverse-federalism-could-reshape-ai-governance-he6h">OpenAI's 'Reverse Federalism' Could Reshape AI Governance</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#AI governance`, `#policy`, `#OpenAI`

---

<a id="item-14"></a>
## [SF Mayor Seeks Stricter Robotaxi Rules After Waymo Gridlock](https://techcrunch.com/2026/07/16/san-francisco-mayor-pushes-for-tougher-rules-after-the-waymo-traffic-fiasco/) ⭐️ 7.0/10

San Francisco Mayor Daniel Lurie has called on state regulators to impose tougher requirements on robotaxi operators like Waymo following a massive hours-long gridlock caused by Waymo vehicles during a power outage. This regulatory push could set a precedent for how cities oversee autonomous vehicle operations, potentially slowing deployment but improving safety and public trust. The gridlock occurred during a widespread power outage in San Francisco, leaving multiple Waymo robotaxis immobilized at intersections and requiring towing. Mayor Lurie specifically urged the California Public Utilities Commission to update its rules.

rss · TechCrunch · Jul 16, 23:25

**Background**: Waymo is a leading autonomous vehicle company that operates a robotaxi service in San Francisco. The incident highlights vulnerabilities of Level 4 autonomous vehicles in unexpected scenarios like power outages, where they may fail to navigate safely.

<details><summary>References</summary>
<ul>
<li><a href="https://insideevs.com/news/782523/waymo-robotaxi-san-francisco-outage-power/">When The Power Went Out In San Francisco, So Did Waymo’s ...</a></li>
<li><a href="https://www.firstpost.com/auto/waymo-robotaxis-run-out-of-charge-require-towing-during-san-franciscos-july-4-gridlock-14029301.html">Waymo Robotaxis Run Out of charge, require towing during San ...</a></li>
<li><a href="https://www.msn.com/en-us/news/technology/waymo-halts-san-francisco-robotaxis-after-massive-power-outage/ar-AA1SMlFC">Waymo halts San Francisco robotaxis after massive power outage</a></li>

</ul>
</details>

**Tags**: `#autonomous vehicles`, `#regulation`, `#Waymo`, `#San Francisco`, `#robotaxi`

---

<a id="item-15"></a>
## [Uber acquires Delivery Hero for $14.8B](https://techcrunch.com/2026/07/16/ubers-14-8b-delivery-hero-deal-would-nearly-double-its-global-footprint/) ⭐️ 7.0/10

Uber has agreed to acquire Delivery Hero in a $14.8 billion all-stock deal, which would nearly double Uber's global footprint and create one of the largest food-delivery platforms outside China. This acquisition significantly strengthens Uber's position in the global food-delivery market, allowing it to compete more effectively with rivals like DoorDash and expand into over 60 new countries. The deal is all-stock and not yet finalized; Delivery Hero also agreed to sell its business in 14 markets where Uber Eats already operates to SSW Partners for $1.6 billion.

rss · TechCrunch · Jul 16, 17:12

**Background**: Delivery Hero is a German multinational online food ordering and delivery company operating in over 60 countries. Uber Eats is Uber's food-delivery division, which has been expanding through acquisitions like Postmates in 2020. The deal reflects ongoing consolidation in the food-delivery industry.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/16/ubers-14-8b-delivery-hero-deal-would-nearly-double-its-global-footprint/">Uber 's $14.8B Delivery Hero deal would nearly double... | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Delivery_Hero">Delivery Hero</a></li>

</ul>
</details>

**Tags**: `#acquisition`, `#food delivery`, `#Uber`, `#business`

---