---
layout: default
title: "Horizon Summary: 2026-10-05 (EN)"
date: 2026-10-05
lang: en
---

> From 49 items, 9 important content pieces were selected

---

1. [Strata runs 125B Qwen 3.8 Flash Next on RTX 4090 at 100 tokens/sec](#item-1) ⭐️ 8.0/10
2. [ARC-AGI-3 Kaggle scores jump from 7% to 56% in 30 days](#item-2) ⭐️ 8.0/10
3. [GitHub tool removes Apple Intelligence from macOS 27 to reclaim disk space](#item-3) ⭐️ 7.0/10
4. [Simon Willison Calls for Default Hard Budget Caps on Pay-by-Usage Services](#item-4) ⭐️ 7.0/10
5. [Google freezes open source bug bounty program over AI submissions](#item-5) ⭐️ 7.0/10
6. [Trump Unveils New 'Super Intelligence Force' AI Task Force](#item-6) ⭐️ 7.0/10
7. [Federal Judge Calls Flock 'Indiscriminate Mass Surveillance'](#item-7) ⭐️ 7.0/10
8. [OpenAI safety employee David Robinson resigns, says culture is broken](#item-8) ⭐️ 7.0/10
9. [Jack Dorsey's Bitchat removed from Indian app stores after government order](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Strata runs 125B Qwen 3.8 Flash Next on RTX 4090 at 100 tokens/sec](https://github.com/Niko1221/Strata) ⭐️ 8.0/10

A GitHub project called Strata enables running the 125B-parameter Qwen 3.8 Flash Next model on a consumer RTX 4090 GPU at roughly 100 tokens per second, with one user reporting 124 tokens/sec on a 4090 with 128GB DDR5 and a Ryzen 7950x3d. The project has sparked debate over quantization quality, as a community benchmark found Strata's vision accuracy degraded significantly compared to llama.cpp on the same GGUF weights. This demonstrates that very large 125B-class models can now run at interactive speeds on consumer hardware, potentially democratizing access to frontier-scale AI without expensive cloud GPUs. It also highlights the growing tension between aggressive quantization for speed and the resulting quality degradation, which matters for anyone deploying local LLMs for accuracy-sensitive tasks. Qwen 3.8 Flash Next has 125B total parameters with only 6B activated per token, plus 51B n-gram embeddings and 4B MTP, which explains its feasibility on consumer hardware. A community benchmark showed Strata had a median error of 154.8 pixels on a 50-image vision coordinate task versus 46.5 pixels for llama.cpp on identical weights, and skeptics warn that sub-4-bit quants may cause significant quality degradation.

hackernews · snehesht · Oct 4, 12:51 · [Discussion](https://news.ycombinator.com/item?id=49953495)

**Background**: Qwen 3.8 Flash Next is a large language model from Alibaba's Qwen family that uses a mixture-of-experts-style architecture, activating only a small fraction of its 125B parameters per token to keep inference efficient. Quantization reduces the numerical precision of model weights (e.g., from 16-bit floats to 4-bit integers) to shrink memory usage and speed up inference, but can harm output quality. Strata is a specialized inference runtime built specifically for this model, and llama.cpp is a widely used general-purpose LLM inference engine often used as a performance and quality baseline.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next">Qwen / Qwen 3 . 8 - Flash - Next · Hugging Face</a></li>
<li><a href="https://github.com/qwenlm/qwen3.8-flash-next">GitHub - QwenLM/ Qwen 3 . 8 - Flash - Next : Qwen 3 . 8 - Flash - Next is the...</a></li>
<li><a href="https://www.youtube.com/watch?v=m0VHx73SAG0">The New Way to Run 125 B Models 6× Faster Than... - YouTube</a></li>

</ul>
</details>

**Discussion**: Sentiment is mixed: some users report surprisingly good results (124 tokens/sec on a 4090, 255 tokens/sec decode on an RTX 6000 Pro), while others are skeptical of sub-4-bit quantization and present benchmarks showing Strata's vision accuracy is far worse than llama.cpp on identical weights. One commenter notes Strata links are being spammed across LLM forums and questions how much of the hype will survive the honeymoon period.

**Tags**: `#LLM inference`, `#quantization`, `#consumer hardware`, `#Qwen`, `#performance benchmarking`

---

<a id="item-2"></a>
## [ARC-AGI-3 Kaggle scores jump from 7% to 56% in 30 days](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arc%CE%B1gi3_scores_on_kaggle_just_went_from_7_to/) ⭐️ 8.0/10

Over the past 30 days, top scores on the ARC-AGI-3 benchmark hosted on Kaggle rose from roughly 7% to 56%, achieved by small local models running inside an agent harness. This surge surpasses average human performance on a benchmark explicitly designed to highlight human superiority in abstraction and reasoning. This rapid progress challenges the assumption that ARC-AGI-3 is far out of reach for current AI, and it suggests that agent harness design may matter more than raw model scale for interactive reasoning tasks. It could reshape how researchers, competition organizers, and the public interpret claims about human-level abstraction and AGI timelines. Kaggle rules restrict competitors to small local models, so the 56% figure reflects gains from harness engineering rather than access to frontier cloud-scale systems. The benchmark itself is interactive, requiring agents to explore novel environments, acquire goals on the fly, and build adaptable world models, and the leaderboard graphic cited in the post is noted as slightly out of date.

reddit · r/MachineLearning · /u/we_are_mammals · Oct 4, 10:24 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1wxcd4k/top_arcαgi3_scores_on_kaggle_just_went_from_7_to/)

**Background**: ARC-AGI-3 is the third iteration of the Abstraction and Reasoning Corpus benchmark from the ARC Prize, an interactive reasoning benchmark where AI agents must explore novel environments, infer goals on the fly, and learn continuously rather than solve static puzzles. Earlier ARC-AGI versions used static grid-based tasks, and frontier models have historically scored in the single digits on the interactive version. Kaggle hosts ARC Prize competitions where participants may only use small local models, making harness design a central part of the challenge.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC - AGI - 3</a></li>
<li><a href="https://benchlm.ai/benchmarks/arcAgi3">ARC - AGI - 3 Leaderboard & Scores — July 2026 | BenchLM.ai</a></li>
<li><a href="https://www.vietanh.dev/blog/2026-06-15-plan-once-then-act-small-model-agents">Plan Once, Then Act: When the ReAct Loop Is the Wrong Harness for...</a></li>

</ul>
</details>

**Discussion**: The Reddit post asks the community what they make of the jump, framing it as small local models in a harness beating average humans on a benchmark meant to show human superiority. Commenters are likely to debate whether the result reflects genuine abstraction progress or benchmark-specific harness tuning, and what it implies for AGI claims.

**Tags**: `#ARC-AGI`, `#AGI`, `#benchmark`, `#machine learning`, `#Kaggle`

---

<a id="item-3"></a>
## [GitHub tool removes Apple Intelligence from macOS 27 to reclaim disk space](https://github.com/omlahore/RemoveMacAI) ⭐️ 7.0/10

A GitHub project called RemoveMacAI offers a script to strip Apple Intelligence out of macOS 27 Golden Gate, where the AI features are no longer opt-in and reportedly consume around 27 GB of disk space. The tool has drawn significant attention, with 361 points and 222 comments debating OS bloat, privacy, and user control. This reflects a growing backlash against AI features being forced into operating systems without an easy off switch, echoing the de-crufting culture long associated with Windows. It signals that even Apple, once praised for clean defaults, now faces user demands for control over local AI models and storage. According to community reports, Apple Intelligence in macOS 27 cannot be disabled through normal settings and its disk footprint is roughly 27 GB, though the tool's exact removal method and any side effects are not detailed in the provided content. The project is hosted at github.com/omlahore/RemoveMacAI.

hackernews · privacyisntdead · Oct 4, 19:42 · [Discussion](https://news.ycombinator.com/item?id=49957116)

**Background**: Apple Intelligence is Apple's suite of on-device and cloud-assisted AI features, including an upgraded Siri, introduced across its operating systems. In earlier macOS versions such as Sequoia and Tahoe, users could toggle it off, but macOS 27 Golden Gate makes it mandatory and bundles local inference models with the OS. This has led to comparisons with Windows bloatware and tools like O&O ShutUp10 that remove unwanted components.

<details><summary>References</summary>
<ul>
<li><a href="https://me.pcmag.com/en/macos/38213/is-apple-intelligence-stealing-your-macs-storage-heres-how-to-turn-it-off">Is Apple Intelligence Stealing Your Mac's Storage? Here's How to...</a></li>
<li><a href="https://upstract.com/x/58b113ecdf1fea32">Apple's macOS 27 installs a lot of AI bloatware</a></li>

</ul>
</details>

**Discussion**: Commenters compared the situation to Windows de-crufting, with some frustrated that iOS no longer offers a simple AI toggle while competitors like Microsoft and Firefox provide global switches. Others defended the bundled local models as small, off-the-cloud, and adequate for basic tasks, while one questioned how Apple weighs disk-usage costs against user backlash.

**Tags**: `#macOS`, `#Apple Intelligence`, `#privacy`, `#system optimization`, `#bloatware`

---

<a id="item-4"></a>
## [Simon Willison Calls for Default Hard Budget Caps on Pay-by-Usage Services](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) ⭐️ 7.0/10

Simon Willison published a blog post arguing that pay-by-usage services and APIs should ship with default hard budget caps that cut off usage and return errors once a spending limit is reached, rather than merely sending warning emails. He notes that AWS launched monthly spend limits in September 2026 and Google Cloud introduced Spend Caps in July, suggesting the industry is starting to move in this direction. As AI coding agents and personal agents make it trivially easy to spin up services that consume paid APIs, storage, and compute, runaway costs have become a real risk—one widely reported case saw two AI agents loop for 11 days and rack up a $47,000 bill. Default hard caps would protect individuals and businesses from catastrophic surprise bills, and could shift how developers choose cloud providers. Willison insists the caps must be hard rather than soft, and proposes an opt-in checkbox that explicitly removes the cap and makes the user responsible for subsequent charges. He notes AWS's new spend limit pauses a project for the month when reached, but the feature is still being released to a limited number of customers rather than being generally available.

rss · Simon Willison · Oct 3, 23:34

**Background**: Pay-by-usage cloud and API services bill customers based on consumption, which means a misconfigured or runaway program can generate unlimited charges. Traditionally, providers offered only soft caps—budget alerts and warning emails—leaving the actual spending unchecked. Hard caps, by contrast, automatically stop or pause workloads once a configured monetary limit is hit, functioning as a firm ceiling rather than a notification.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/">We’re going to need default hard budget caps on pretty much...</a></li>
<li><a href="https://academy.codearia.com/en/articles/hard-spend-limits-aws-google-cloud-openai-anthropic">Hard spend limits: AWS, Google Cloud, OpenAI, Vercel</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#API design`, `#cost management`, `#cloud billing`, `#developer tools`

---

<a id="item-5"></a>
## [Google freezes open source bug bounty program over AI submissions](https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/) ⭐️ 7.0/10

Google has paused its Open Source Software Vulnerability Rewards Program (OSS VRP) until next year, citing a "significant rise" in AI-generated submissions that overwhelmed its triage process. The program, which paid researchers for finding flaws in Google's open source projects, was frozen because the volume of low-quality, AI-generated reports made it unsustainable to review. This is a notable industry development showing how AI slop is becoming a systemic problem for security research and open source maintenance. It signals that bug bounty programs, a key mechanism for finding vulnerabilities, may need to fundamentally rethink their submission and triage processes as generative AI makes it cheap to produce plausible-looking but useless reports. The freeze is temporary, with Google planning to resume the program next year, though no specific date or revised process has been announced. The OSS VRP was launched to reward researchers for vulnerabilities in Google's open source projects, and similar AI-driven submission floods have already forced other programs, such as Apple's, to cap or restrict reports.

rss · TechCrunch · Oct 4, 20:31

**Background**: A bug bounty program is an arrangement where organizations pay individuals for reporting security vulnerabilities, especially in software. Google's OSS VRP specifically focused on flaws in its open source projects, which are widely used but often maintained by small teams. AI slop refers to high-volume, low-effort content generated by AI, and in this context it means automated reports that look like legitimate vulnerability findings but lack real security impact.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/10/04/google-froze-its-open-source-bug-bounty-program-due-to-a-significant-rise-in-ai-submissions/">AI slop seems to be overwhelming bug bounty programs .</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bug_bounty_program">Bug bounty program - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Cybersecurity experts had already warned last year that AI slop posed a serious risk to bug bounty programs, and the cURL project previously shut down its own bug bounty program for the same reason. The overall sentiment is that this is a growing, predictable crisis for security triage teams, with little disagreement about the cause.

**Tags**: `#bug-bounty`, `#open-source`, `#AI`, `#security`, `#Google`

---

<a id="item-6"></a>
## [Trump Unveils New 'Super Intelligence Force' AI Task Force](https://techcrunch.com/2026/10/04/trump-unveils-his-new-super-intelligence-force/) ⭐️ 7.0/10

President Donald Trump announced the formation of a new 'Super Intelligence Force' (SIF) on Truth Social, to be led by national intelligence director Jay Clayton, with FTC Chairman Andrew Ferguson and other officials in senior roles. The task force has been given 120 days to report on the risks and opportunities of artificial intelligence. This is a significant political development that directly shapes how the U.S. federal government will engage with AI companies, consumers, and interest groups amid the ongoing AI safety debate. The task force's findings could influence future AI regulation and policy direction, affecting the entire AI/ML ecosystem. According to Trump's Truth Social post, the SIF will coordinate the federal government's engagement with consumers, public interest groups, religious organizations, critical infrastructure providers, and 'Super Intelligence Companies.' The task force includes Jay Clayton, Andrew Ferguson, and other officials, and must deliver its risk-and-opportunity report within 120 days.

rss · TechCrunch · Oct 4, 15:15

**Background**: The 'Super Intelligence Force' is the Trump administration's latest response to the intensifying debate over AI safety and whether and how advanced AI should be regulated. The AI safety debate involves multiple factions with differing views on risks, ranging from near-term harms to speculative AGI concerns. By placing intelligence and trade officials at the helm, the task force signals a focus on both national security and commercial implications of AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/news/story/white-house-announces-new-ai-super-intelligence-force-9444010/">White House announces new AI ' Super Intelligence Force ' | LinkedIn</a></li>
<li><a href="https://sputnikglobe.com/20261004/trump-announces-formation-of-super-intelligence-force-1124833877.html">Trump Announces Formation of Super Intelligence Force</a></li>
<li><a href="https://www.nbcnews.com/politics/trump-administration/trump-announces-members-ai-task-force-rcna601494">Trump announces members of ‘ Super Intelligence Force ’ to...</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#AI safety`, `#government`, `#regulation`, `#Trump administration`

---

<a id="item-7"></a>
## [Federal Judge Calls Flock 'Indiscriminate Mass Surveillance'](https://techcrunch.com/2026/10/03/federal-judge-calls-flock-indiscriminate-mass-surveillance/) ⭐️ 7.0/10

A federal judge ruled that a sheriff's deputy violated a woman's Fourth Amendment rights by using Flock Safety's license plate recognition system to search for her plate without a warrant, labeling the practice 'indiscriminate mass surveillance.' This ruling could set a precedent limiting warrantless use of automated license plate recognition systems by law enforcement nationwide, affecting how police departments deploy surveillance technology and raising broader questions about privacy and civil liberties. The ruling specifically targets Flock Safety, one of the largest ALPR vendors in the U.S. with roughly 120,000 cameras installed, and asserts that searching its database without a warrant constitutes an unreasonable search under the Fourth Amendment.

rss · TechCrunch · Oct 3, 19:33

**Background**: Flock Safety is a company that deploys AI-powered automated license plate recognition (ALPR) cameras across the United States, automatically scanning plates and logging vehicle time, location, and details. The Fourth Amendment to the U.S. Constitution protects against unreasonable searches and seizures, generally requiring law enforcement to obtain a warrant based on probable cause. This case tests whether warrantless queries of aggregated ALPR data violate that protection.

<details><summary>References</summary>
<ul>
<li><a href="https://www.governing.com/management-and-administration/americas-surveillance-problem-is-much-bigger-than-flock">America’s Surveillance Problem Is Much Bigger than Flock</a></li>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers...</a></li>
<li><a href="https://www.findlaw.com/criminal/criminal-rights/the-fourth-amendment-warrant-requirement.html">The Fourth Amendment Warrant Requirement - FindLaw</a></li>

</ul>
</details>

**Tags**: `#surveillance`, `#privacy`, `#fourth-amendment`, `#license-plate-recognition`, `#law-enforcement`

---

<a id="item-8"></a>
## [OpenAI safety employee David Robinson resigns, says culture is broken](https://techcrunch.com/2026/10/03/openai-safety-employee-resigns-claiming-the-companys-culture-is-broken/) ⭐️ 7.0/10

David Robinson, who spent three and a half years at OpenAI leading the writing of safety reports that accompany major product launches, resigned and published an essay in The Atlantic on October 3, 2026 titled 'I quit OpenAI because its culture is broken.' He warned that the time for trial and error in AI safety is over and that the problems run deeper than specific rules or new laws. This resignation adds a prominent internal voice to the growing debate over whether leading AI labs are prioritizing speed over safety, and it could intensify scrutiny of OpenAI's governance as regulators worldwide develop AI oversight frameworks. It also follows earlier high-profile safety departures and the dissolution of OpenAI's dedicated safety team, suggesting a pattern rather than an isolated incident. Robinson led the writing of the safety reports that accompanied OpenAI's major product releases, giving him direct visibility into how safety concerns were documented and communicated. In his essay he argued that the fix requires looking deeper than specific rules or new laws, framing the issue as cultural rather than merely regulatory.

rss · TechCrunch · Oct 3, 16:30

**Background**: OpenAI is the developer of ChatGPT and one of the leading AI labs, and it has faced repeated internal turmoil over safety, including the 2024 dissolution of the high-profile safety team led by Ilya Sutskever and Jan Leike. AI safety governance refers to the policies, laws, and internal practices that direct and oversee AI systems, covering who is accountable, what is governed, and how oversight is implemented. The EU adopted its AI Act in 2024, and debates over whether companies are moving too fast on capabilities at the expense of safety have become central to the industry.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/oct/03/openai-safety-leader-quits-warning-ai-companys-culture-is-broken">OpenAI safety leader quits, warning AI... | The Guardian</a></li>
<li><a href="https://economictimes.indiatimes.com/tech/technology/openai-dissolves-high-profile-safety-team-after-chief-scientist-ilya-sutskevers-exit/articleshow/110223018.cms?from=mdr">OpenAI safety team dissolved: OpenAI dissolves high-profile safety ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_safety_governance">AI safety governance</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#AI governance`, `#tech industry`, `#company culture`

---

<a id="item-9"></a>
## [Jack Dorsey's Bitchat removed from Indian app stores after government order](https://techcrunch.com/2026/10/03/jack-dorseys-bitchat-disappears-from-app-stores-in-india-after-government-order/) ⭐️ 7.0/10

Jack Dorsey's decentralized messaging app Bitchat has been removed from app stores in India following a government order, making it largely unavailable in the country. The removal was reported by TechCrunch on October 3, 2026, and no official reason has been publicly detailed. This highlights growing tensions between governments and privacy-focused, censorship-resistant communication tools, and could set a precedent for how India regulates decentralized apps. It affects software engineers, privacy advocates, and users who rely on such tools in restrictive environments. Bitchat operates over Bluetooth Low Energy mesh networking with end-to-end encryption, allowing offline peer-to-peer messaging without internet infrastructure. Its decentralized design makes it difficult for authorities to block or monitor, which likely triggered the Indian government's action.

rss · TechCrunch · Oct 3, 15:02

**Background**: Bitchat was announced by Jack Dorsey, co-founder of Twitter and Block, in July 2025 as a peer-to-peer encrypted messaging app that uses Bluetooth mesh networking instead of the internet. It is designed for censorship resistance, enabling communication in regions where internet access is restricted or shut down. The app gained attention as a prototype for decentralized, privacy-first messaging.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/BitChat">BitChat - Wikipedia</a></li>
<li><a href="https://www.theverge.com/news/701272/jack-dorsey-bitchat-bluetooth-messaging-app">Jack Dorsey made an encrypted Bluetooth messaging app | The Verge</a></li>
<li><a href="https://techcrunch.com/2025/07/07/jack-dorsey-working-on-bluetooth-messaging-app-bitchat/">Jack Dorsey working on Bluetooth messaging app, Bitchat</a></li>

</ul>
</details>

**Tags**: `#censorship`, `#india`, `#decentralized-messaging`, `#app-store-policy`, `#tech-regulation`

---