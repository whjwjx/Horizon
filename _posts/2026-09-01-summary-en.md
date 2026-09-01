---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 54 items, 10 important content pieces were selected

---

1. [Google Removes MV2 Extensions from Chrome Web Store, Including uBlock Origin](#item-1) ⭐️ 8.0/10
2. [Simon Willison Demystifies OpenAI's ChatGPT Work](#item-2) ⭐️ 8.0/10
3. [McKesson Data Breach: Hackers Claim Millions of Patient Records Stolen](#item-3) ⭐️ 8.0/10
4. [Turning Security Cameras into Automatic Bird Identification with BirdNET-Go](#item-4) ⭐️ 7.0/10
5. [ChatGPT Ads Hits $1B Annualized Revenue, Expands Globally](#item-5) ⭐️ 7.0/10
6. [Wrapture: New Python Library for Tracing and Testing](#item-6) ⭐️ 7.0/10
7. [Pentagon Adds ChatGPT and Grok to Its AI Portal](#item-7) ⭐️ 7.0/10
8. [AI's Vulnerability Discovery Could Curb Government Hacking Tools](#item-8) ⭐️ 7.0/10
9. [Nvidia's $3.5B MediaTek Bet Signals Strategy to Stay Essential in AI Infrastructure](#item-9) ⭐️ 7.0/10
10. [FTC and 22 States Sue Amazon Over Secret Ad Surcharges](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Google Removes MV2 Extensions from Chrome Web Store, Including uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

Google has removed all Manifest V2 (MV2) extensions from the Chrome Web Store, including popular ad-blocker uBlock Origin. This marks the final phase of the transition to Manifest V3 (MV3), which began years ago. This affects millions of Chrome users who relied on MV2 extensions like uBlock Origin for ad-blocking and privacy, potentially increasing exposure to malicious ads. It also raises concerns about Google's control over the browser ecosystem and pushes users toward alternatives like Firefox. uBlock Origin received a final stability update on August 31, 2026, but it will no longer function in Chrome after MV2 support ends. Microsoft Edge is also discontinuing MV2 extensions by the end of 2026, following a similar timeline.

hackernews · twapi · Aug 31, 21:10 · [Discussion](https://news.ycombinator.com/item?id=49514878)

**Background**: Manifest V2 was the original extension framework for Chrome, while Manifest V3 introduced stricter security and performance restrictions, limiting capabilities like blocking network requests. Google announced the MV2 deprecation plan years ago, and by 2025, most users had already been migrated to MV3. The removal of MV2 extensions from the store is the final step, with the last developer flag removed in Chrome 151 (July 2026).

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate">Migrate to Manifest V3 | Chrome for Developers</a></li>
<li><a href="https://medium.com/@idmossab/nifest-v2-vs-manifest-v3-chrome-extensions-what-changed-and-why-2025-was-the-turning-point-53b031b70fc6">Manifest V2 vs Manifest V3 (Chrome Extensions): What Changed, and Why 2025 Was the Turning Point | by mossab | Medium</a></li>
<li><a href="https://piunikaweb.com/2026/08/26/ublock-origin-one-last-update-ahead-mv2/">uBlock Origin picks up one last update ahead of MV2 ...</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely negative, with many users expressing frustration and distrust toward Google. Several commenters recommend switching to Firefox, noting that uBlock Origin works best there, and some share personal stories about safety concerns with malicious ads. A few users mention they already migrated to Firefox years ago and haven't missed Chrome.

**Tags**: `#Chrome`, `#ad-blocking`, `#Manifest V2`, `#browser`, `#privacy`

---

<a id="item-2"></a>
## [Simon Willison Demystifies OpenAI's ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

Simon Willison published an analysis clarifying that OpenAI's ChatGPT Work, announced on July 9th, actually consists of two distinct products: a cloud-based version (Work Cloud) and a local desktop app (Work Local). He details the unique features of Work Cloud, including model selection, code execution with internet access, and a headless Chrome browser. This analysis helps developers and AI enthusiasts understand a complex and rapidly evolving product, clarifying when to use Chat versus Work. It highlights the growing trend of AI tools offering agentic capabilities and cloud-based execution, which could impact how users interact with AI assistants. Work Cloud is available to paid subscribers ($20/month and up) and can be accessed via chatgpt.com or mobile apps, while Work Local is part of the ChatGPT desktop app (formerly Codex). Work offers model selection (GPT-5.6 Sol, Luna, Terra) with various reasoning levels, a persistent shared filesystem, and the ability to publish ChatGPT Sites.

rss · Simon Willison · Aug 30, 23:59

**Background**: ChatGPT Work is OpenAI's latest offering aimed at completing tasks with clear outcomes, such as creating briefs, decks, or analyses. It builds on the capabilities of ChatGPT and Codex, integrating agentic features like code execution and browser automation. The product is part of OpenAI's broader push toward more autonomous AI assistants.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/">Understanding ChatGPT Work | Simon Willison’s Weblog</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://nukcloud.com/en/blog/2026-chatgpt-work-codex-merged-chatgpt-desktop-20260710.html">ChatGPT Work Launched: Codex Merges Into ChatGPT Desktop ...</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#AI tools`, `#product analysis`

---

<a id="item-3"></a>
## [McKesson Data Breach: Hackers Claim Millions of Patient Records Stolen](https://techcrunch.com/2026/08/31/hackers-claim-millions-of-patient-records-stolen-during-data-breach-at-healthcare-giant-mckesson/) ⭐️ 8.0/10

Hackers claim to have stolen millions of patient records from McKesson, a major U.S. healthcare distributor. McKesson confirmed the breach and expects intermittent service disruptions. This breach could expose sensitive health data of millions of patients, leading to identity theft and privacy violations. It underscores the ongoing vulnerability of the healthcare sector to cyberattacks, which have been increasing in frequency and severity. The stolen data reportedly includes patient records and McKesson employees' home addresses. The ShinyHunters hacking group has claimed responsibility, and the breach involved unauthorized access to third-party applications and data exfiltration.

rss · TechCrunch · Aug 31, 18:10

**Background**: McKesson is a major distributor of medicines and medical devices to hospitals and healthcare practices across the U.S. Healthcare data breaches are a growing concern; in 2023 alone, over 725 large breaches affected more than 133 million individuals in the U.S. The sensitive nature of health data makes such breaches particularly damaging.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/31/hackers-claim-millions-of-patient-records-stolen-during-data-breach-at-healthcare-giant-mckesson/">Hackers claim millions of patient records stolen during data breach at...</a></li>
<li><a href="https://blog.gridinsoft.com/mckesson-data-breach-2026/">McKesson Data Breach : Confirmed Scope and Response</a></li>
<li><a href="https://www.hipaajournal.com/healthcare-data-breach-statistics/">Healthcare Data Breach Statistics – Updated for 2026</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#data breach`, `#healthcare`, `#privacy`, `#McKesson`

---

<a id="item-4"></a>
## [Turning Security Cameras into Automatic Bird Identification with BirdNET-Go](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) ⭐️ 7.0/10

A developer repurposed their security cameras to run BirdNET-Go, an open-source AI tool, for automatic bird identification. The system listens continuously and identifies bird species in real-time, operating 24/7 on local hardware. This showcases a practical, low-cost way to leverage existing security camera infrastructure for ecological monitoring, making bird identification accessible to hobbyists. It highlights the growing trend of repurposing consumer hardware for AI-driven environmental observation. BirdNET-Go runs 24/7, analyzing audio at 48 kHz in 3-second segments, and can also identify bats. The system supports various alert integrations like Discord, Telegram, and MQTT, and is designed to run on a Raspberry Pi.

hackernews · speckx · Aug 31, 16:47 · [Discussion](https://news.ycombinator.com/item?id=49511856)

**Background**: BirdNET is a deep learning algorithm developed by Cornell University that classifies bird species from audio recordings. BirdNET-Go is a self-hosted, real-time soundscape analyzer that brings this AI to local hardware, enabling continuous monitoring without cloud dependency. Security cameras often have built-in microphones and RTSP streams, making them convenient audio sources for such systems.

<details><summary>References</summary>
<ul>
<li><a href="https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/">How I Turned My Security Cameras Into an Automatic Bird Identification System with BirdNet-Go</a></li>
<li><a href="https://github.com/tphakala/birdnet-go">GitHub - tphakala/birdnet-go: Self-hosted realtime soundscape analyser for birds, bats and other wildlife. Multi-model local AI inference, runs 24/7 on a Raspberry Pi. · GitHub</a></li>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>

</ul>
</details>

**Discussion**: Commenters shared their own implementations, such as using Unifi doorbell cams and Aqara cameras, noting challenges like wind noise and sampling rate limitations. Some suggested alternatives like the Merlin Bird ID app, while others discussed hardware modifications and display enhancements for portability.

**Tags**: `#BirdNET`, `#DIY`, `#computer-vision`, `#audio-classification`, `#security-cameras`

---

<a id="item-5"></a>
## [ChatGPT Ads Hits $1B Annualized Revenue, Expands Globally](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 7.0/10

OpenAI announced that ChatGPT Ads has reached a $1 billion annualized revenue run rate and is expanding globally to support broader access to AI. This milestone demonstrates significant commercial traction for OpenAI's advertising business, indicating a viable monetization path beyond subscriptions. It also supports OpenAI's mission to make AI accessible to more people through free and affordable options. The $1 billion figure is an annualized run rate, not actual annual revenue, and reflects the rapid growth of ads within ChatGPT. The global expansion suggests OpenAI is scaling its advertising infrastructure to new markets, which may involve partnerships and localized ad offerings.

rss · OpenAI Blog · Aug 31, 04:00

**Background**: ChatGPT Ads is OpenAI's advertising platform that displays ads within ChatGPT responses. It was introduced to provide a revenue stream alongside subscriptions, allowing free access to the AI. The run rate metric estimates future annual revenue based on current performance, commonly used in tech to gauge growth.

<details><summary>References</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001047-ads-in-chatgpt">Ads in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://www.seo.com/blog/chatgpt-advertising/">ChatGPT Advertising : Meet Your Next Revenue Channel</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">investopedia.com/terms/r/runrate.asp</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#ChatGPT`, `#AI business`, `#monetization`, `#AI access`

---

<a id="item-6"></a>
## [Wrapture: New Python Library for Tracing and Testing](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

Graham Dumpleton, creator of wrapt, has released Wrapture, a Python library that extends wrapt's monkeypatching to enable tracing and overriding of functions for testing and observability. It includes OpenTelemetry support and a configuration-based mechanism for adding tracing to existing projects. Wrapture offers a potential alternative to unittest.mock for testing and provides a novel way to implement tracing in Python projects. It could simplify observability and testing workflows for Python developers, especially those already using wrapt. Wrapture is a very young project, only a few weeks old, and is Graham's first large entirely agent-driven project, with all code and documentation written by an AI assistant under his direction. It supports configuration-based tracing via TOML files and includes OpenTelemetry support.

rss · Simon Willison · Aug 31, 23:59

**Background**: Monkeypatching is a technique in Python that allows modifying the behavior of functions or methods at runtime, often used in testing to replace or stub out parts of code. wrapt is a well-known library for implementing decorators and monkeypatching in a transparent and efficient way. Tracing involves recording the execution of code, such as function calls and return values, which is useful for debugging and observability.

<details><summary>References</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/60551322/wrapt-decorators-and-monkey-patching">python - @ wrapt decorators and monkey patching - Stack Overflow</a></li>
<li><a href="https://docs.python.org/3/library/trace.html">trace — Trace or track Python statement execution</a></li>
<li><a href="https://pymotw.com/2/sys/tracing.html">Tracing a Program As It Runs - Python Module of the Week</a></li>

</ul>
</details>

**Tags**: `#Python`, `#testing`, `#monkeypatching`, `#tracing`, `#developer tools`

---

<a id="item-7"></a>
## [Pentagon Adds ChatGPT and Grok to Its AI Portal](https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/) ⭐️ 7.0/10

The Pentagon will integrate versions of OpenAI's ChatGPT and SpaceXAI's Grok into its central AI portal, alongside Google's Gemini. This marks the first time these major commercial AI models will be available to the U.S. military through a unified platform. This adoption signals a significant shift in the U.S. military's embrace of commercial AI technologies, potentially accelerating AI integration in defense operations. It also raises important questions about the ethical and security implications of using such models in military contexts. The announcement is brief and lacks technical specifics, such as which versions of ChatGPT and Grok will be deployed or how they will be secured. The integration follows a trend of the Pentagon partnering with major AI companies, including previous collaborations with Anthropic and Google.

rss · TechCrunch · Aug 31, 20:13

**Background**: The Pentagon's central AI portal is a platform designed to provide military personnel with access to various AI tools. OpenAI's ChatGPT is a widely used conversational AI, while SpaceXAI's Grok is a family of large language models known for coding and agentic tasks. The inclusion of these models reflects the growing reliance on commercial AI for defense purposes.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/">The Pentagon now has its own version of ChatGPT and... | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceXAI">SpaceXAI - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/02/26/anthropic-pentagon-ai-amodei.html">cnbc.com/2026/02/26/anthropic- pentagon - ai -amodei.html</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Government`, `#National Security`, `#OpenAI`, `#Grok`

---

<a id="item-8"></a>
## [AI's Vulnerability Discovery Could Curb Government Hacking Tools](https://techcrunch.com/2026/08/31/how-ai-could-make-it-harder-for-governments-to-use-hacking-tools/) ⭐️ 7.0/10

The article discusses how AI's growing effectiveness in finding and exploiting vulnerabilities could make it harder for governments to use hacking tools and spyware, potentially reigniting debates on device backdoors. This matters because it could shift the balance of power in cybersecurity, affecting government surveillance capabilities and national security policies. It also highlights the dual-use nature of AI, which can both defend and attack systems, prompting a reevaluation of encryption and backdoor policies. The article references recent incidents where government hacking tools leaked to cybercriminals, such as a suite targeting iPhones with older iOS versions. It also notes that AI's ability to find vulnerabilities could make it harder for governments to control these tools, as they might be more easily replicated or discovered by adversaries.

rss · TechCrunch · Aug 31, 15:19

**Background**: Government hacking tools are offensive cyber capabilities used for surveillance and intelligence gathering, often exploiting software vulnerabilities. The debate over device backdoors involves balancing law enforcement needs with privacy and security concerns, as backdoors can be exploited by malicious actors. AI's role in vulnerability discovery is a growing concern, as it can automate and accelerate the process, potentially outpacing defensive measures.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/03/03/a-suite-of-government-hacking-tools-targeting-iphones-is-now-being-used-by-cybercriminals/">A suite of government hacking tools targeting iPhones is now being used by cybercriminals | TechCrunch</a></li>
<li><a href="https://www.nextgov.com/cybersecurity/2026/03/potential-us-built-hacking-tools-obtained-foreign-spies-and-cybercriminals-research-says/411861/">Potential US-built hacking tools obtained by foreign spies and cybercriminals, research says - Nextgov/FCW</a></li>
<li><a href="https://www.bu.edu/riscs/2021/05/03/abuse-resistant-government-backdoors/">Abuse-Resistant Government Backdoors | Center for Reliable Information Systems & Cyber Security</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#government hacking`, `#vulnerability discovery`, `#policy`

---

<a id="item-9"></a>
## [Nvidia's $3.5B MediaTek Bet Signals Strategy to Stay Essential in AI Infrastructure](https://techcrunch.com/2026/08/31/nvidias-3-5b-mediatek-bet-reveals-its-plan-for-tackling-big-techs-ai-chip-buildout/) ⭐️ 7.0/10

Nvidia has invested $3.5 billion in Taiwanese chipmaker MediaTek, a move that reveals its strategy to remain essential in AI infrastructure as Big Tech companies develop their own in-house AI chips. The investment positions Nvidia to control the infrastructure behind custom AI chips, turning the shift to custom silicon into a toll business. This investment is significant because it allows Nvidia to maintain influence over the AI chip market even as major tech companies like Google, Amazon, and Microsoft design their own chips. By partnering with MediaTek, Nvidia can leverage MediaTek's edge AI capabilities and expand its reach into diverse device segments, ensuring its technology remains integral to AI infrastructure. The investment is part of Nvidia's broader strategy to secure the infrastructure of intelligence, as highlighted by its recent partnerships with financial firms to mobilize over $500 billion for AI compute infrastructure. MediaTek's NPU (Neural Processing Unit) is a key asset, providing efficient AI acceleration for edge devices such as smartphones, tablets, and IoT devices.

rss · TechCrunch · Aug 31, 15:15

**Background**: Nvidia is a leading designer of GPUs and AI chips, while MediaTek is a major fabless semiconductor company known for its system-on-chips (SoCs) used in smartphones and other devices. As Big Tech companies increasingly design their own custom AI chips to reduce costs and improve performance, Nvidia is seeking ways to remain indispensable by investing in partners and building a tollbooth-like infrastructure for custom AI chip development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/08/31/nvidias-35-billion-mediatek-deal-is-a-tollbooth-for-custom-ai-chips/">Nvidia Turns $3.5 Billion MediaTek Deal Into A Toll ... - Forbes</a></li>
<li><a href="https://blogs.nvidia.com/blog/securing-the-infrastructure-of-intelligence/">Securing the Infrastructure of Intelligence - NVIDIA Blog</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital">NVIDIA Partners With Apollo, BlackRock, Blackstone ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#MediaTek`, `#AI chips`, `#investment`, `#AI infrastructure`

---

<a id="item-10"></a>
## [FTC and 22 States Sue Amazon Over Secret Ad Surcharges](https://www.theverge.com/tech/986982/amazon-advertising-prices-ftc-lawsuit) ⭐️ 7.0/10

The FTC and 22 state attorneys general filed a lawsuit against Amazon on August 31, 2026, alleging that the company secretly inflated advertising prices through a 'secret ad surcharge' scheme, affecting over 1.2 million advertisers and generating over $20 billion in revenue. This lawsuit could reshape digital advertising practices and hold major tech platforms accountable for deceptive pricing, potentially leading to stricter regulations and increased transparency in ad auctions. It also highlights the growing scrutiny of Amazon's high-margin advertising business. The lawsuit, filed in the Western District of Washington, alleges that Amazon concealed the surcharges from advertisers and passed the higher costs on to consumers. FTC Chairman Andrew Ferguson stated that the higher advertising prices were 'largely passed on to American consumers.'

rss · The Verge · Aug 31, 21:41

**Background**: Amazon operates a large advertising platform where advertisers bid for ad placements in auctions. The FTC alleges that Amazon secretly added surcharges to these auction prices, misleading advertisers and inflating costs. This lawsuit is part of broader regulatory scrutiny of big tech companies' business practices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ftc.gov/news-events/news/press-releases/2026/08/ftc-states-sue-amazon-over-secret-ad-surcharge-scheme">FTC, States Sue Amazon Over Secret Ad Surcharge Scheme</a></li>
<li><a href="https://www.nytimes.com/2026/08/31/technology/ftc-amazon-lawsuit-ad-prices.html">FTC and 22 States Sue Amazon Over Advertising Practices</a></li>
<li><a href="https://www.axios.com/2026/08/31/ftc-amazon-deceptive-advertising-lawsuit">FTC , 22 states sue Amazon over deceptive advertising practices</a></li>

</ul>
</details>

**Tags**: `#Amazon`, `#FTC`, `#advertising`, `#lawsuit`, `#e-commerce`

---