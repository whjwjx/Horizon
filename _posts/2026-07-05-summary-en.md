---
layout: default
title: "Horizon Summary: 2026-07-05 (EN)"
date: 2026-07-05
lang: en
---

> From 44 items, 11 important content pieces were selected

---

1. [Prompt Injection Leaks YouTube Creators' Private Videos](#item-1) ⭐️ 9.0/10
2. [Politician probing spyware hacked with Pegasus](#item-2) ⭐️ 9.0/10
3. [Newer Claude Models Worse at Tool Schema Adherence](#item-3) ⭐️ 8.0/10
4. [Current AI Launches Open Source AI Gap Map](#item-4) ⭐️ 8.0/10
5. [Course Creator Reports 50%+ Revenue Drop Due to AI](#item-5) ⭐️ 8.0/10
6. [NASA Launches Emergency Mission to Save Swift Observatory](#item-6) ⭐️ 8.0/10
7. [TLA+ Used to Hunt 16-Year-Old SQLite Bug, Check dqlite](#item-7) ⭐️ 8.0/10
8. [Command & Conquer Generals Natively Ported to Apple Devices via Fable](#item-8) ⭐️ 7.0/10
9. [World Map in 500 Bytes via Deflate and Fetch](#item-9) ⭐️ 7.0/10
10. [White House deletes energy conservation pages during heatwave](#item-10) ⭐️ 7.0/10
11. [Linux Containers Go Native on All Major Platforms](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Prompt Injection Leaks YouTube Creators' Private Videos](https://javoriuski.com/post/youtube) ⭐️ 9.0/10

A security researcher discovered that prompt injection in YouTube's AI comment reply feature can leak creators' private video titles and other sensitive data. This vulnerability poses a serious privacy risk to YouTube creators, as attackers could extract information about unlisted or private videos through crafted comments. The attack works when a creator clicks a suggested AI reply in YouTube Studio, causing the model to execute injected instructions and reveal data from the creator's channel.

hackernews · javxfps · Jul 4, 16:45 · [Discussion](https://news.ycombinator.com/item?id=48786781)

**Background**: Prompt injection is a security exploit where malicious inputs cause an AI model to behave unexpectedly. YouTube's AI comment reply feature uses large language models to suggest responses, but fails to properly separate user comments from system instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights mixed reactions: some users confirm the vulnerability, while others report it didn't work in their tests. A former Google employee explains internal handling challenges, and many criticize YouTube for not treating prompt injection as a bug.

**Tags**: `#security`, `#prompt injection`, `#YouTube`, `#privacy`, `#AI`

---

<a id="item-2"></a>
## [Politician probing spyware hacked with Pegasus](https://techcrunch.com/2026/07/02/politician-who-investigated-spyware-abuses-had-his-phone-hacked-with-pegasus-spyware/) ⭐️ 9.0/10

A European politician serving on the EU's PEGA Committee, which investigates spyware abuses, had their phone hacked with NSO Group's Pegasus spyware by a government customer of NSO. This incident demonstrates direct retaliation against a politician investigating the spyware industry, highlighting the urgent need for stronger regulation and accountability for surveillance technology vendors. The PEGA Committee was established in 2022 after the Pegasus Project revelations, and the hacked politician had traveled to interview spyware victims and probe high-profile cases.

rss · TechCrunch · Jul 3, 05:05

**Background**: Pegasus is spyware developed by Israeli company NSO Group, capable of remotely infecting mobile phones to access data, microphones, and cameras. NSO claims it sells only to authorized governments for combating crime and terror, but it has been repeatedly linked to surveillance of journalists, activists, and political figures.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus ( spyware ) - Wikipedia</a></li>
<li><a href="https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/">Espionage Against the European Parliament: Member of Committee Investigating Spyware Hacked with Pegasus - The Citizen Lab</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#surveillance`, `#NSO Group`, `#Pegasus`, `#privacy`

---

<a id="item-3"></a>
## [Newer Claude Models Worse at Tool Schema Adherence](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 8.0/10

Armin Ronacher reports that newer Claude models (Opus 4.8, Sonnet 5) invent extra fields in tool calls, causing schema validation failures in Pi's edit tool, while older models do not exhibit this behavior. This regression in tool-calling accuracy for state-of-the-art models could undermine reliability of third-party coding harnesses and highlights a tension between model training for specific tools and general schema adherence. The issue occurs specifically with Pi's edit tool, where the model adds made-up keys to the nested 'edits[]' array, causing Pi to reject the call. Armin suspects reinforcement learning for Claude Code's built-in edit tool is the cause.

rss · Simon Willison · Jul 4, 22:53

**Background**: LLM tool calling allows models to invoke external functions by generating structured JSON matching a provided schema. Third-party coding harnesses like Pi define custom edit tools with specific schemas. Anthropic's Claude Code uses a built-in search-and-replace edit tool, and newer models may be overtrained to use that specific tool, harming generalization.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview">Tool use with Claude - Anthropic</a></li>
<li><a href="https://github.com/can1357/oh-my-pi">GitHub - can1357/oh-my-pi: ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more</a></li>
<li><a href="https://arxiv.org/html/2604.13519v1">ToolSpec: Accelerating Tool Calling via Schema -Aware and...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#tool calling`, `#Anthropic`, `#Claude`, `#regression`

---

<a id="item-4"></a>
## [Current AI Launches Open Source AI Gap Map](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit launched at the AI Action Summit in Paris in February 2025, has released the Open Source AI Gap Map v0.1, which indexes 421 open source AI products across software, models, datasets, and hardware. The underlying data, including 1,184 YAML files, is available on GitHub under an MIT license. This map provides a structured overview of the open source AI ecosystem, helping identify gaps and opportunities for investment and development. It is a significant resource for researchers, developers, and policymakers aiming to strengthen open source AI. The map details 266 software tools, 85 models, 50 datasets, and 20 hardware projects from 228 organizations, organized into 14 categories across three stack layers. An additional 24,400 artifacts remain uncategorized and unscored until further research.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global non-profit partnership founded at the AI Action Summit in Paris in February 2025, with $400 million in committed funding. The Gap Map aims to map the open source AI stack to identify missing components and high-leverage areas for building new tools or investing in capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem mapping`, `#non-profit`, `#Current AI`

---

<a id="item-5"></a>
## [Course Creator Reports 50%+ Revenue Drop Due to AI](https://simonwillison.net/2026/Jul/3/josh-w-comeau/#atom-everything) ⭐️ 8.0/10

Josh W. Comeau reported that his new course launch sold only one-third of typical copies, and his existing courses saw revenue down over 50%, which he attributes to AI-driven uncertainty about developer jobs and LLMs replacing paid learning resources. This firsthand account provides concrete data on how AI is disrupting the developer education market, potentially threatening the livelihoods of independent course creators and signaling a shift in how developers learn new skills. Comeau launched his third course, Whimsical Animations, and it is on track to sell roughly one-third as many copies as a typical launch; he also noted that multiple other course creators are seeing the same 50%+ revenue decline trend.

rss · Simon Willison · Jul 3, 21:25

**Background**: Online courses for developers have been a popular way for creators to monetize expertise, but the rise of LLMs like GPT-4 offers free or low-cost personalized tutoring, reducing the incentive to pay for courses. Additionally, widespread AI-driven uncertainty about the future of developer jobs makes people hesitant to invest time and money in learning new skills.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@keshavarangarajan/the-impact-of-llms-on-learning-and-education-3cd2a8367c23">The Impact of LLMs on Learning and Education | by keshava rangarajan | Medium</a></li>
<li><a href="https://www.psychologytoday.com/us/blog/the-digital-self/202412/five-ways-llms-transform-education">Five Ways LLMs Transform Education | Psychology Today</a></li>
<li><a href="https://www.a3logics.com/blog/role-of-llms-in-education/">The Role of LLMs in Education: Transforming Learning with AI</a></li>

</ul>
</details>

**Tags**: `#AI impact`, `#developer education`, `#online courses`, `#job market`, `#LLMs`

---

<a id="item-6"></a>
## [NASA Launches Emergency Mission to Save Swift Observatory](https://www.theverge.com/science/961459/nasa-emergency-save-swift-observatory-katalyst-space-technologies) ⭐️ 8.0/10

NASA has launched an emergency mission with Katalyst Space Technologies to prevent the Swift Observatory from burning up in Earth's atmosphere due to orbit decay caused by solar storms. The LINK servicing spacecraft was launched on July 3, 2026, with the goal of docking with Swift and boosting its orbit. This mission is significant because it aims to save a valuable scientific observatory that has been operating for over 20 years, and if successful, it will be the first commercial spacecraft to dock with a government-owned spacecraft not designed for servicing. It also demonstrates a new capability for on-orbit satellite servicing and debris mitigation. The Swift Observatory was launched in 2004 and has a nominal lifetime of two years, but has been operating for over 20 years. Recent solar storms have increased atmospheric drag, lowering its orbit and risking uncontrolled reentry by the end of 2026.

rss · The Verge · Jul 4, 19:06

**Background**: The Neil Gehrels Swift Observatory is a NASA multi-wavelength space telescope designed to study gamma-ray bursts and other astrophysical transients. It was launched in 2004 and has far exceeded its planned two-year mission. Solar storms heat and expand Earth's upper atmosphere, increasing drag on low-Earth orbit satellites and causing their orbits to decay faster.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Swift_Observatory">Swift Observatory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Katalyst_Space_Technologies">Katalyst Space Technologies</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_Boost_Mission">Swift Boost Mission - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space`, `#NASA`, `#satellite rescue`, `#space debris`, `#Swift Observatory`

---

<a id="item-7"></a>
## [TLA+ Used to Hunt 16-Year-Old SQLite Bug, Check dqlite](https://www.reddit.com/r/programming/comments/1umi3j4/hunting_a_16yearold_sqlite_bug_with_tla_is_dqlite/) ⭐️ 8.0/10

A developer used TLA+ formal verification to discover a 16-year-old bug in SQLite and then investigated whether dqlite, a distributed SQLite extension, is also affected. This demonstrates the power of formal methods like TLA+ in finding long-standing bugs in critical infrastructure software, and highlights the importance of verifying distributed systems built on such foundations. The bug was present in SQLite for 16 years and was uncovered through model checking with TLA+. The author also checked dqlite, which uses SQLite as its storage engine, to see if it inherited the vulnerability.

reddit · r/programming · /u/yusufaytas · Jul 3, 15:50

**Background**: TLA+ is a formal specification language used for model checking concurrent and distributed systems. SQLite is a widely embedded database engine. dqlite extends SQLite to support replication and high availability across a cluster.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.internetcomputer.org/guides/security/formal-verification/">Formal verification | ICP Developer Docs</a></li>
<li><a href="https://dbdb.io/db/dqlite">Dqlite - Database of Databases</a></li>
<li><a href="https://github.com/canonical/dqlite">GitHub - canonical/ dqlite : Embeddable, replicated and fault-tolerant...</a></li>

</ul>
</details>

**Tags**: `#SQLite`, `#TLA+`, `#formal verification`, `#bug hunting`, `#database`

---

<a id="item-8"></a>
## [Command & Conquer Generals Natively Ported to Apple Devices via Fable](https://github.com/ammaarreshi/Generals-Mac-iOS-iPad/tree/main) ⭐️ 7.0/10

Command & Conquer Generals has been natively ported to macOS, iPhone, and iPad using the AI-assisted Fable tool, built on EA's GPL v3 source release via the GeneralsX project. This demonstrates a practical application of AI-assisted conversion for game porting, potentially enabling many classic games to reach modern platforms with less manual effort. The port requires users to own the game on Steam and uses a custom touch control scheme for iOS/iPadOS, including tap-select, drag-box, and pinch zoom. The engine code is GPL v3, but game assets are not included.

hackernews · asronline · Jul 4, 19:41 · [Discussion](https://news.ycombinator.com/item?id=48788283)

**Background**: Command & Conquer Generals is a 2003 real-time strategy game by EA. EA released its source code under GPL v3 in 2021, enabling community ports. The Fable tool uses AI to assist in converting codebases to new platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Command_&_Conquer">Command & Conquer - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised the port as a good use of AI for mass conversion, though some noted the AI-generated documentation style is grating. Others discussed the potential for porting similar games like Emperor: Battle for Dune.

**Tags**: `#game porting`, `#AI-assisted development`, `#open source`, `#macOS`, `#iOS`

---

<a id="item-9"></a>
## [World Map in 500 Bytes via Deflate and Fetch](https://simonwillison.net/2026/Jul/4/building-a-world-map-with-only-500-bytes/#atom-everything) ⭐️ 7.0/10

Iwo Kadziela, assisted by Codex, created a credible ASCII world map using only 445 bytes of data by leveraging deflate compression and a JavaScript fetch with a data URI. This demonstrates a clever technique for extreme data compression on the web, showcasing how modern browser APIs like DecompressionStream can be combined with data URIs to deliver rich content in minimal bytes. The technique uses the deflate-raw compression algorithm and pipes the decompressed stream through DecompressionStream, then converts it to text and displays it in a pre element. The entire payload is embedded in a base64-encoded data URI.

rss · Simon Willison · Jul 4, 23:09

**Background**: Deflate is a lossless compression algorithm combining LZ77 and Huffman coding, widely used in ZIP, PNG, and gzip. The DecompressionStream API is part of the Compression Streams standard, allowing streaming decompression in browsers. Data URIs allow embedding data directly in URLs, and fetch() can retrieve them as if they were network resources.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DEFLATE_compression_algorithm">DEFLATE compression algorithm</a></li>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/API/DecompressionStream">DecompressionStream - Web APIs | MDN</a></li>
<li><a href="https://stackoverflow.com/questions/66573468/why-can-i-fetch-data-uris">Why can I fetch data URIs? - Stack Overflow</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion praised the cleverness of the approach and the use of modern web APIs. Some commenters noted that the map quality is surprisingly good for such a small size, while others discussed alternative compression methods.

**Tags**: `#compression`, `#JavaScript`, `#ASCII art`, `#data URI`, `#web development`

---

<a id="item-10"></a>
## [White House deletes energy conservation pages during heatwave](https://www.theverge.com/policy/961449/white-house-mamdani-heatwave-deletion) ⭐️ 7.0/10

The US Department of Energy deleted approximately 6,000 web pages related to energy conservation during a historic heatwave, following Republican criticism of New York City Mayor Zohran Mamdani's request to set air conditioners to 78°F to reduce grid strain. This deletion raises concerns about government transparency and the politicization of energy policy, especially as extreme heat events become more frequent due to climate change. The deletion was timed suspiciously after Republicans like Ted Cruz attacked Mamdani's conservation request, and the pages removed included practical tips for reducing energy use during heatwaves.

rss · The Verge · Jul 4, 16:19

**Background**: The US Department of Energy maintains a large online repository of energy conservation information. The deletion of these pages during a heatwave, when such information is most needed, has drawn criticism from environmental and transparency advocates.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zohran_Mamdani">Zohran Mamdani</a></li>

</ul>
</details>

**Tags**: `#energy policy`, `#climate change`, `#government transparency`, `#US politics`

---

<a id="item-11"></a>
## [Linux Containers Go Native on All Major Platforms](https://www.reddit.com/r/programming/comments/1um497y/linux_has_officially_won/) ⭐️ 7.0/10

Apple released version 1.0 of its native container manager for macOS, and Microsoft announced native container support in Windows 11 via WSL, making OCI-compatible Linux containers run natively on Windows, macOS, BSD, and Linux. This universal native support means developers can rely on Linux containers everywhere without third-party tools, marking a major victory for Linux and open-source software and making Linux knowledge essential for developers on any platform. Apple's container manager is available as an optional download with macOS 26/Tahoe, while Microsoft's WSL container CLI (wslc.exe) is built into Windows 11, both supporting OCI-compatible containers without requiring Docker.

reddit · r/programming · /u/BankApprehensive7612 · Jul 3, 04:23

**Background**: Containers package applications with their dependencies, ensuring consistent behavior across environments. The Open Container Initiative (OCI) defines standards for container formats and runtimes, enabling interoperability. Previously, running Linux containers on Windows or macOS required a virtual machine or Docker Desktop; now native support eliminates that overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/windows/wsl/wsl-container?tabs=csharp">WSL container | Microsoft Learn</a></li>

</ul>
</details>

**Tags**: `#Linux`, `#containers`, `#OCI`, `#cross-platform`, `#open-source`

---