---
layout: default
title: "Horizon Summary: 2026-09-16 (EN)"
date: 2026-09-16
lang: en
---

> From 76 items, 14 important content pieces were selected

---

1. [US Military Confirms First Deployment of Weapons in Earth Orbit](#item-1) ⭐️ 9.0/10
2. [TypeSafe AI launches System One Models and Jev for fast typed inference](#item-2) ⭐️ 8.0/10
3. [Maker builds e-ink frame that identifies birds and draws 1800s-style illustrations](#item-3) ⭐️ 8.0/10
4. [Internet Archive Adds Protections as Wayback Machine Faces Scraping Surge](#item-4) ⭐️ 8.0/10
5. [Prior Labs releases TabPFN-3.5, new SOTA tabular foundation model](#item-5) ⭐️ 8.0/10
6. [Bryan Cantrill pushes back on AI extinction fears](#item-6) ⭐️ 7.0/10
7. [Jensen Huang Says AI Safety Should Be Engineered, Not Regulated](#item-7) ⭐️ 7.0/10
8. [US data centers may out-consume Germany and Japan in natural gas by 2035](#item-8) ⭐️ 7.0/10
9. [SpaceX to Attempt First Starship Orbital Flight on September 22](#item-9) ⭐️ 7.0/10
10. [TechCrunch Recaps the Worst Hacks and Data Breaches of 2026](#item-10) ⭐️ 7.0/10
11. [OpenAI, Anthropic, Google DeepMind Hold Weeks of AI Safety Talks](#item-11) ⭐️ 7.0/10
12. [India to Charge 0.4% Merchant Fee on Larger UPI Transactions](#item-12) ⭐️ 7.0/10
13. [Canva launches ProSuite, uniting Affinity, Cavalry, Flourish and Leonardo with 100+ new features](#item-13) ⭐️ 7.0/10
14. [44M-parameter ternary LLM ships in 19.8 MB, runs at 1,900 tok/s on CPU](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [US Military Confirms First Deployment of Weapons in Earth Orbit](https://techcrunch.com/2026/09/15/us-military-confirms-it-launched-space-weapons-into-earths-orbit/) ⭐️ 9.0/10

The U.S. military has publicly confirmed for the first time that it has launched a weapon into Earth's orbit, stating it has fielded "on-orbit space control weapons capable of defending the Joint Force against hostile adversary action." This marks the first official acknowledgment of a space-based weapon in the U.S. arsenal. This is a major geopolitical and technological milestone that signals a significant shift in space policy and could accelerate an arms race among major powers. It has broad implications for international security, satellite operations, and the interpretation of space law, and is likely to draw responses from China and Russia. The acknowledgment refers to "on-orbit space control weapons" designed to defend the Joint Force against hostile adversary action, though specific capabilities, orbital parameters, and deployment dates were not disclosed. Space weapons can include anti-satellite (ASAT) systems, directed-energy devices such as lasers or particle beams, and kinetic interceptors.

rss · TechCrunch · Sep 15, 17:09

**Background**: Space weapons are weapons used in space warfare, including those that can attack space systems in orbit (such as anti-satellite weapons), attack targets on Earth from space, or disable missiles traveling through space. During the Cold War, the contesting superpowers developed such weapons, and some have already been deployed in space. The United States Space Force, established as a separate military branch, traces its origins to the Air Force, Army, and Navy's military space programs created during the early Cold War.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Space_weapon">Space weapon - Wikipedia</a></li>
<li><a href="https://www.cbsnews.com/news/us-confirms-weapons-in-space-china-russia-respond/">U.S. confirms for the first time that it has deployed weapons in space ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/United_States_Space_Force">United States Space Force - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space weapons`, `#military technology`, `#space policy`, `#national security`, `#geopolitics`

---

<a id="item-2"></a>
## [TypeSafe AI launches System One Models and Jev for fast typed inference](https://typesafe.ai/blog/introducing-system-one-models-and-jev) ⭐️ 8.0/10

TypeSafe AI introduced System One Models and Jev, its flagship first model, in early access. Jev evaluates a state and returns typed answers with probabilities, targeting fast, structured decisions for software rather than general-purpose generation. This signals a shift toward embedding AI as primitives inside software instead of autonomous agents, which could make AI-powered automation cheaper, faster, and more controllable. It also sparked a 726-point Hacker News debate about the trade-offs between general-purpose generation and constrained typed inference. Jev takes a state (structured text) plus questions framed as Choice, Score, or Noul, and returns answers with probabilities and confidence; it is priced at $0.042 per million tokens and answers in milliseconds. Unlike an LLM, it does not generate code or choose its own next action, so it cannot do everything a Turing-complete generative model can.

hackernews · albelfio · Sep 15, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49717558)

**Background**: System One models are a class of AI models built to make fast, structured decisions that software can use directly, similar to how an LLM understands natural-language input but constrained to typed outputs. TypeSafe AI positions them as AI primitives that embed into software so code remains in control, contrasting with agentic systems that generate code or act autonomously. Structured output techniques like constrained decoding are already used in inference engines such as vLLM to enforce JSON schemas and speed up generation.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.typesafe.ai/concepts/system-one">System One - TypeSafe AI</a></li>
<li><a href="https://typesafe.ai/blog/introducing-system-one-models-and-jev">Introducing System One Models & Jev - TypeSafe AI Blog</a></li>
<li><a href="https://news.ycombinator.com/item?id=49717558">Introducing System One Models and Jev | Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters praised the idea as genuinely new and promising, especially when combined with design-by-contract patterns, but criticized the announcement for not explaining the model clearly and for a potentially misleading speed comparison against general-purpose generative models. Several pointed readers to the documentation as a better explanation of how Jev takes a state and typed questions to return answers with probabilities.

**Tags**: `#AI`, `#machine-learning`, `#type-systems`, `#inference`, `#Hacker News`

---

<a id="item-3"></a>
## [Maker builds e-ink frame that identifies birds and draws 1800s-style illustrations](https://github.com/arnegiacomo/fugleramme) ⭐️ 8.0/10

A maker named arnegiacomo published a GitHub project called 'fugleramme' (Norwegian for 'bird frame') that uses a microphone to listen for bird calls, identifies species with the BirdNET classifier, and renders each bird as a 19th-century-style illustration on an e-ink display. The Show HN post earned 1283 points and 179 comments, making it one of the standout hardware projects on Hacker News. The project shows how affordable embedded hardware (ESP32-class microcontrollers plus e-ink panels) can combine with open bioacoustics models to create ambient, low-power devices that feel magical rather than utilitarian. It also highlights the growing ecosystem of bird-monitoring projects, from BirdNET-Go to similar DIY builds, which could support citizen-science data collection and everyday nature awareness. The underlying classifier is BirdNET, a traditional convolutional neural network developed for acoustic bird identification rather than an LLM, as commenter divbzero pointed out with a link to the 2021 Ecological Informatics paper. The e-ink display is well suited to this use case because it only needs to refresh when a new bird is detected, allowing very low average power draw.

hackernews · arnemunthekaas · Sep 15, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49711544)

**Background**: BirdNET is an AI-powered sound identification system developed by the Cornell Lab of Ornithology and Chemnitz University of Technology that lets users identify birds from their calls using a phone or dedicated device. E Ink displays use tiny pigment microcapsules that only consume power when the image changes, which is why they are popular for always-on, battery-friendly frames. The ESP32 is a family of low-cost microcontrollers from Espressif with integrated Wi-Fi and Bluetooth, widely used in IoT and maker projects.

<details><summary>References</summary>
<ul>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>
<li><a href="https://en.wikipedia.org/wiki/E_Ink">E Ink - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/ESP32">ESP32 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters were overwhelmingly enthusiastic, with jadbox calling it 'the coolest thing on HN' and praising its blend of ideas into something magical. Others noted that BirdNET is a traditional neural network rather than an LLM, linked related projects like birdnet-go, and shared practical e-ink/ESP32 experiences, including one user whose BTLE e-ink driver should last years on a single charge.

**Tags**: `#e-ink`, `#bird-classification`, `#embedded-systems`, `#ESP32`, `#Show HN`

---

<a id="item-4"></a>
## [Internet Archive Adds Protections as Wayback Machine Faces Scraping Surge](https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/) ⭐️ 8.0/10

The Internet Archive published a blog update on September 15, 2026, reporting that the Wayback Machine has been hit by waves of high-volume automated traffic and that new protections have been put in place to keep the service running. One visible change is a rewritten message shown to users when a request is blocked with an HTTP 429 error. The Internet Archive is critical public infrastructure for digital preservation, so sustained scraping pressure threatens access for researchers, journalists, and ordinary users who rely on archived web pages. The incident also highlights a broader trend of AI and data-scraping operations shifting their load onto free public archives after being blocked elsewhere. The protections include rate limiting that returns HTTP 429 errors, and the Archive notes that some sites have already opted out of being archived as a result of the scraping. Community reports suggest the 429 errors can appear inconsistently, affecting some networks or locations while others still work fine.

hackernews · ChrisArchitect · Sep 15, 17:52 · [Discussion](https://news.ycombinator.com/item?id=49716176)

**Background**: The Wayback Machine is a service run by the nonprofit Internet Archive that stores snapshots of web pages over time, letting users view older versions of sites that may have changed or disappeared. Scrapers are automated programs that download large amounts of data from websites; when they target the Wayback Machine, they consume the same limited bandwidth and server capacity meant for human visitors and preservation work.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.archive.org/2026/09/15/an-update-on-wayback-machine-access/">An Update on Wayback Machine Access | Internet Archive Blogs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive">Internet Archive - Wikipedia</a></li>
<li><a href="https://github.com/sangaline/wayback-machine-scraper">GitHub - sangaline/wayback-machine-scraper: A command-line utility and Scrapy middleware for scraping time series data from Archive.org's Wayback Machine. · GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News were largely supportive of the Internet Archive, with some praising its continued anonymous access via Tor and urging donations, while others shared firsthand experiences of persistent 429 errors from certain networks. Several users noted the Archive is under pressure from multiple directions, and one commenter argued AI companies should pay for the access they consume.

**Tags**: `#internet-archive`, `#web-scraping`, `#infrastructure`, `#digital-preservation`, `#web-archiving`

---

<a id="item-5"></a>
## [Prior Labs releases TabPFN-3.5, new SOTA tabular foundation model](https://www.reddit.com/r/MachineLearning/comments/1wh4xhy/tabpfn35_is_released_as_the_next_sota_tabular/) ⭐️ 8.0/10

Prior Labs released TabPFN-3.5, a new tabular foundation model that tops both the TabArena and BeyondArena leaderboards, with support for datasets up to 1M rows and 20k features. It ships in three variants: TabPFN-3.5-Fast (in alpha, 6x faster than the base model), TabPFN-3.5-Thinking (trades compute for accuracy via API), and TabPFN-3.5-Plus. Tabular data remains the dominant format in enterprise and scientific settings, so a new SOTA foundation model with practical speed and accuracy variants could meaningfully change how practitioners build predictive pipelines. The strong BeyondArena results on text-rich, high-cardinality, and high-dimensional data suggest foundation models are closing gaps that previously favored gradient-boosted trees. On BeyondArena, TabPFN-3.5 leads by +250 Elo over the strongest previous baseline and +150 Elo over the previous overall leader, while TabPFN-3.5-Thinking adds +20 Elo on BeyondArena and +44 Elo on TabArena over the base model. The Fast variant is still in alpha, and the Thinking variant is only available through the API rather than as a local download.

reddit · r/MachineLearning · /u/tuanacelik · Sep 15, 16:18

**Background**: TabPFN is a pre-trained transformer-based foundation model for tabular data, originally trained on a large corpus of synthetic tabular datasets so it can make predictions on new tables without task-specific training. TabArena is a living benchmark for machine learning on small to medium-sized IID tabular data, while BeyondArena extends evaluation to harder conditions such as temporal and grouped tasks across different scales and dimensionalities. Elo ratings, borrowed from chess, are used to compare model strength in head-to-head benchmark matchups.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/PriorLabs/tabpfn">PriorLabs/TabPFN - Foundation Model for Tabular Data - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2506.16791">[2506.16791] TabArena: A Living Benchmark for Machine ... TabArena: A Living Benchmark for Machine Learning on Tabular Data GitHub - j201/tabrepo: A Living Benchmark for Machine ... TabArena: Living Benchmark for Tabular ML</a></li>
<li><a href="https://therevision.co/articles/tabular-ai-benchmarks-have-been-hiding-the-hard-problems">Tabular AI Benchmarks Have Been Hiding the Hard... | The Revision</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#tabular-data`, `#foundation-models`, `#benchmarks`, `#TabPFN`

---

<a id="item-6"></a>
## [Bryan Cantrill pushes back on AI extinction fears](https://simonwillison.net/2026/Sep/14/the-contagion-of-fear/) ⭐️ 7.0/10

Bryan Cantrill published a blog post titled "The contagion of fear" responding to former Anthropic employee Jacob Coxon's tweet claiming many Anthropic researchers believe AI "could kill us all by the end of the decade." Cantrill argues that such claims rely on hand-wavy extrapolation and that domain experts have a duty to be circumspect when raising alarms. This intervention matters because it challenges the growing mainstream narrative of AI existential risk coming from leading labs, and it raises questions about how much trust the public should place in experts who make dramatic, under-specified claims. It also adds a prominent systems engineer's voice to the AI safety debate, potentially influencing how policymakers and the public weigh alarmist warnings. Cantrill specifically criticizes Coxon's citations of "hacking critical infrastructure" and "extinction-level bioweapons" as lacking elaboration, noting Coxon is not an expert in critical infrastructure, bioweapons, or extinction. He also discussed his doubts about bioweapons concerns on the Oxide and Friends podcast, asking for a biologist or bioweapons expert to weigh in.

rss · Simon Willison · Sep 14, 21:18

**Background**: Bryan Cantrill is a respected software engineer, formerly at Sun Microsystems and Joyent, and now co-founder and CTO of Oxide Computer. Jacob Coxon is a former OpenAI and Anthropic employee who resigned from Anthropic over concerns about out-of-control AI development. AI existential risk refers to the hypothesis that advanced artificial general intelligence could lead to human extinction, a topic debated by researchers and tech leaders.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bryan_Cantrill">Bryan Cantrill</a></li>
<li><a href="https://www.wsj.com/tech/ai/anthropic-researcher-quits-over-out-of-control-ai-fears-707b7628">Anthropic Researcher Quits Over 'Out-of-Control' AI Fears - WSJ</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_existential_risk">AI existential risk</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#existential risk`, `#technology criticism`, `#AI ethics`, `#commentary`

---

<a id="item-7"></a>
## [Jensen Huang Says AI Safety Should Be Engineered, Not Regulated](https://techcrunch.com/2026/09/15/we-dont-need-ai-regulation-leave-safety-to-us-nvidias-jensen-huang-says/) ⭐️ 7.0/10

Speaking at Salesforce's Dreamforce conference on Tuesday, Nvidia CEO Jensen Huang argued that AI is not an "alien mind" but simply hardware and software, so safety should be engineered by the companies building AI products rather than imposed through government regulation. He pushed back on existential-risk warnings from figures such as Anthropic CEO Dario Amodei, framing apocalyptic AI rhetoric as a kind of "God complex." Nvidia is the dominant supplier of AI chips, so Huang's stance carries significant weight in the ongoing global debate over how — or whether — to regulate AI. His position aligns with industry pushes for open-weight models and self-governance, and could influence policymakers weighing binding rules against voluntary safety commitments. Huang made the remarks during a Dreamforce panel alongside Salesforce CEO Marc Benioff, Anthropic's Dario Amodei, and Siemens CEO Roland Busch, covering regulation, safety, employment, and enterprise adoption. Nvidia has backed up its rhetoric with concrete tooling, including the NVIDIA AI safety recipe, NeMo Guardrails, and the full-stack Halos safety system, and it has been staffing a new AI safety team to evaluate agents before deployment.

rss · TechCrunch · Sep 16, 00:20

**Background**: The debate over AI regulation pits those who want binding government rules against those who argue safety is best handled by the companies building the technology. Nvidia designs the GPUs that power most large AI models, giving it outsized influence over the industry's direction. Its "safety recipe" and NeMo Guardrails are examples of engineering-level safeguards — such as filtering adversarial prompts and blocking prompt-injection attacks — that vendors can ship without legislation.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/15/we-dont-need-ai-regulation-leave-safety-to-us-nvidias-jensen-huang-says/">We don't need AI regulation — leave safety to us, Nvidia's Jensen ...</a></li>
<li><a href="https://developer.nvidia.com/blog/safeguard-agentic-ai-systems-with-the-nvidia-safety-recipe/">Safeguard Agentic AI Systems with the NVIDIA Safety Recipe | NVIDIA Technical Blog</a></li>
<li><a href="https://www.businessinsider.com/nvidia-staffs-new-ai-safety-team-push-for-open-models-2026-8">Nvidia Staffs New AI Safety Team Amid Its Push for Open Models - Business Insider</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#AI safety`, `#Nvidia`, `#policy`, `#industry`

---

<a id="item-8"></a>
## [US data centers may out-consume Germany and Japan in natural gas by 2035](https://techcrunch.com/2026/09/15/us-data-centers-could-consume-more-natural-gas-than-germany-and-japan-combined-by-2035/) ⭐️ 7.0/10

A new report projects that U.S. data centers, driven by the AI boom, could consume more natural gas than Germany and Japan combined by 2035, making them one of the world's largest gas consumers. The finding highlights how AI infrastructure buildout is turning the tech sector into a major fossil fuel demand center. This projection signals that AI's energy footprint is no longer just an electricity-grid issue but a direct driver of fossil fuel demand, complicating corporate climate pledges and national decarbonization goals. It affects utilities, regulators, energy markets, and the tech companies racing to build ever-larger AI campuses. Industry analyses estimate that a 1 GW data center consumes roughly 140 million cubic feet of natural gas per day, and one forecast puts total U.S. data center gas consumption at about 6.1 billion cubic feet per day by 2030. Many operators are turning to behind-the-meter gas turbines because grid interconnection queues are too slow for AI timelines.

rss · TechCrunch · Sep 15, 18:29

**Background**: Data centers power servers and, increasingly, the GPU clusters used to train and run AI models, and that electricity has historically come mostly from the grid. As AI demand surges, developers are building on-site natural gas plants to get power faster than utilities can deliver it. Natural gas is a fossil fuel that produces roughly half the CO2 of coal when burned, but it still emits greenhouse gases and methane leaks upstream.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rbccm.com/en/insights/2026/05/natural-gas-powers-the-data-center-boom">Natural gas powers the data center boom | RBCCM</a></li>
<li><a href="https://www.enverus.com/blog/why-data-centers-are-looking-to-natural-gas-for-behind-the-meter-power/">Natural Gas Behind-the-Meter Power for Data Centers - Enverus</a></li>
<li><a href="https://www.mcgillenergyjournal.com/post/explaining-variation-in-energy-forecasts-the-role-of-ai-and-data-centers">Explaining Variation in Energy Forecasts: The Role of AI and Data ...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#energy consumption`, `#natural gas`, `#climate impact`

---

<a id="item-9"></a>
## [SpaceX to Attempt First Starship Orbital Flight on September 22](https://techcrunch.com/2026/09/15/spacex-will-try-to-put-starship-in-orbit-for-the-first-time-on-september-22/) ⭐️ 7.0/10

SpaceX plans to attempt the first orbital flight of its Starship rocket on September 22, and will also try to deploy the first V3 Starlink satellites during the same mission. This marks the first time the fully reusable super heavy-lift vehicle would reach orbit rather than fly a suborbital trajectory. Achieving orbit would be a major engineering milestone for Starship, which SpaceX intends to use for deploying large satellites, lunar landings under NASA's Artemis program, and eventual Mars missions. Combining the orbital test with the first V3 Starlink deployment also signals that next-generation internet satellites may soon rely on Starship's much larger payload capacity. Starship consists of the Super Heavy booster and the Starship upper stage, both powered by Raptor engines burning liquid methane and liquid oxygen, and both designed to land vertically for reuse. As of July 2026, the vehicle had launched 13 times with 8 successes and 5 failures, and the program has repeatedly missed its optimistic schedule targets.

rss · TechCrunch · Sep 15, 18:16

**Background**: Starship is a two-stage, fully reusable super heavy-lift launch vehicle under development by SpaceX, intended as the successor to Falcon 9 and Falcon Heavy. An orbital flight means placing a spacecraft on a trajectory where it can remain in space for at least one full orbit, which around Earth requires a speed of roughly 7.8 km/s. SpaceX has followed an iterative, prototype-heavy development approach, with the first full Starship launch in April 2023 ending in an explosion four minutes after liftoff.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Starship_rocket">Starship rocket</a></li>
<li><a href="https://en.wikipedia.org/wiki/Orbital_flight">Orbital flight</a></li>
<li><a href="https://www.spacex.com/vehicles/starship">Starship - SpaceX</a></li>

</ul>
</details>

**Tags**: `#SpaceX`, `#Starship`, `#Starlink`, `#Space Technology`, `#Orbital Launch`

---

<a id="item-10"></a>
## [TechCrunch Recaps the Worst Hacks and Data Breaches of 2026](https://techcrunch.com/2026/09/15/the-worst-hacks-and-breaches-of-2026-so-far/) ⭐️ 7.0/10

TechCrunch published a roundup on September 15, 2026, cataloging the most damaging security incidents of the year so far, including the massive DOGE data breach, compromises of critical infrastructure, and hacks of federal surveillance systems. The roundup highlights how attacks in 2026 have shifted from conventional corporate breaches toward government agencies and critical infrastructure, raising national-security and public-safety concerns for security professionals, software engineers, and policymakers. The article is a summary-level overview rather than a technical deep-dive, and it specifically ties the DOGE breach to sensitive Social Security data allegedly taken by a former DOGE engineer, an allegation under investigation by the Social Security inspector general.

rss · TechCrunch · Sep 15, 16:00

**Background**: DOGE, the Department of Government Efficiency, was a Trump-era initiative that gained broad access to federal systems and data, and its handling of sensitive records has drawn congressional scrutiny. Critical infrastructure refers to essential systems such as power grids, water utilities, and communications networks, while federal surveillance systems are the tools used by agencies to monitor communications and track individuals. A data breach is the unauthorized access to or exfiltration of confidential information, and a ransom note typically signals a ransomware attack in which attackers demand payment to restore access or prevent leaked data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.washingtonpost.com/politics/2026/03/10/social-security-data-breach-doge-2/">DOGE member took Social Security data on a ... - The Washington Post</a></li>
<li><a href="https://oversightdemocrats.house.gov/news/press-releases/ranking-member-robert-garcia-expands-doge-social-security-data-leak-investigation-following-explosive-new-whistleblower-allegations">Ranking Member Robert Garcia Expands DOGE Social Security ...</a></li>
<li><a href="https://www.whitehouse.senate.gov/news/release/whitehouse-wyden-demand-update-on-doge-infiltration-of-the-social-security-administration/">Whitehouse, Wyden Demand Update on DOGE Infiltration of the Social ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#data breaches`, `#hacking`, `#critical infrastructure`, `#cybersecurity`

---

<a id="item-11"></a>
## [OpenAI, Anthropic, Google DeepMind Hold Weeks of AI Safety Talks](https://techcrunch.com/2026/09/15/openai-anthropic-google-have-been-in-talks-on-ai-safety-for-weeks/) ⭐️ 7.0/10

OpenAI has confirmed that it held weeks of AI safety talks with Anthropic and Google DeepMind, according to a TechCrunch report published on September 15, 2026. The talks took place as the Trump administration downplays AI safety concerns and prioritizes keeping pace with China in the AI race. This is a notable instance of the three leading AI labs coordinating on safety even as the U.S. political environment becomes less focused on regulation, which could shape future industry norms and voluntary standards. It signals that frontier labs may try to set safety expectations themselves rather than wait for government mandates, affecting how AI is governed and how competitors in China and elsewhere respond. The report is brief and does not disclose the specific topics, participants, or outcomes of the talks, and it is unclear whether the discussions will produce any formal commitments. The context includes the Trump administration's deregulatory posture and its emphasis on competing with China, which contrasts with the safety-focused stance of the labs involved.

rss · TechCrunch · Sep 15, 15:47

**Background**: AI safety is an interdisciplinary field focused on preventing accidents, misuse, or other harmful consequences from AI systems, including AI alignment, risk monitoring, and robustness. It gained prominence in 2023 amid rapid progress in generative AI, and both the U.S. and U.K. established AI safety institutes during the 2023 AI Safety Summit. OpenAI, Anthropic, and Google DeepMind are among the most prominent frontier AI labs; Anthropic was founded in 2021 by former OpenAI members explicitly to promote AI safety, while OpenAI has faced internal departures of safety researchers who cited the company's deprioritization of safety.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_safety">AI safety</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#Anthropic`, `#Google DeepMind`, `#AI policy`

---

<a id="item-12"></a>
## [India to Charge 0.4% Merchant Fee on Larger UPI Transactions](https://techcrunch.com/2026/09/15/india-ends-free-ride-for-larger-transactions-on-its-ubiquitous-digital-payments-network/) ⭐️ 7.0/10

India's National Payments Corporation of India (NPCI) announced that UPI merchant payments above Rs 2,000 will attract a 0.4% Merchant Discount Rate (MDR) starting October 15, 2026, with the fee paid by merchants rather than consumers. This ends the network's long-standing free-transaction model for larger person-to-merchant payments. UPI is one of the world's largest digital payment networks with hundreds of millions of users, so introducing merchant fees could reshape India's digital payments ecosystem, affect merchant costs, and influence fintech business models built on zero-cost UPI transactions. It signals a shift from growth-at-all-costs to sustainable monetization for public digital infrastructure. The 0.4% MDR applies only to person-to-merchant (P2M) transactions above Rs 2,000, meaning a merchant receiving Rs 10,000 would pay Rs 40; consumer payments remain unchanged. Smaller transactions and person-to-person transfers are unaffected, and the fee is borne entirely by merchants.

rss · TechCrunch · Sep 15, 14:22

**Background**: UPI (Unified Payments Interface) is an instant payment system and protocol developed by the National Payments Corporation of India (NPCI) in 2016, facilitating inter-bank peer-to-peer and person-to-merchant transactions. It has become ubiquitous in India, processing billions of transactions monthly, and was previously free for merchants to encourage adoption. The new MDR marks a policy shift toward charging for larger merchant payments.

<details><summary>References</summary>
<ul>
<li><a href="https://indianexpress.com/article/business/upi-payments-over-rs-2000-to-merchants-will-attract-0-4-fee-10879274/">UPI payments over Rs 2,000 to merchants will attract 0.4% fee</a></li>
<li><a href="https://www.indiatoday.in/business/story/upi-charges-from-october-15-merchant-payments-above-rs-2000-to-attract-0-4-percent-mdr-2995348-2026-09-15">UPI charges from October 15: Merchant payments above Rs 2,000 ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unified_Payments_Interface">Unified Payments Interface - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#UPI`, `#digital-payments`, `#fintech`, `#India`, `#policy`

---

<a id="item-13"></a>
## [Canva launches ProSuite, uniting Affinity, Cavalry, Flourish and Leonardo with 100+ new features](https://www.creativeboom.com/news/canva-launches-prosuite-bringing-affinity-cavalry-flourish-and-leonardo-together-with-more-than-new-100-features/) ⭐️ 7.0/10

Canva has launched ProSuite, a connected set of professional design tools that brings Affinity, Cavalry, Flourish and Leonardo together under one umbrella, accompanied by more than 100 new features. Among the additions is a long-requested Blend Tool, and both Affinity and Cavalry remain free to use. This marks Canva's biggest push yet into the professional designer market, consolidating a portfolio of specialized creative tools that previously competed separately with Adobe's ecosystem. Designers and product teams now have a single connected suite spanning vector design, motion graphics, data visualization and AI image generation, which could reshape how professional creative software is bundled and priced. The suite spans Affinity for vector, raster and desktop publishing work, Cavalry for 2D animation and motion design, Flourish for data visualization, and Leonardo for AI image generation, with the Blend Tool addressing a feature designers had requested for years. Notably, Affinity and Cavalry stay free, which lowers the barrier for professionals to adopt the suite.

rss · Creative Boom (艺术设计) · Sep 15, 11:00

**Background**: Canva is best known as a free-to-use online graphic design tool for social media posts, presentations, posters and videos, and it has been expanding aggressively into professional markets. Affinity is a graphics editor that combines vector, raster and desktop publishing capabilities, originally developed by Serif and now published by Canva. Cavalry is a 2D animation and motion design application for macOS and Windows, while Flourish and Leonardo cover data visualization and AI image generation respectively.

<details><summary>References</summary>
<ul>
<li><a href="https://www.creativeboom.com/news/canva-launches-prosuite-bringing-affinity-cavalry-flourish-and-leonardo-together-with-more-than-new-100-features/">Canva launches ProSuite bringing Affinity, Cavalry, Flourish and Leonardo together with more than new 100 features | Creative Boom</a></li>
<li><a href="https://en.wikipedia.org/wiki/Affinity_(software)">Affinity (software) - Wikipedia</a></li>
<li><a href="https://cavalry.studio/">Free 2D animation & motion graphics software for Mac and ...</a></li>

</ul>
</details>

**Tags**: `#Canva`, `#design tools`, `#Affinity`, `#product launch`, `#creative software`

---

<a id="item-14"></a>
## [44M-parameter ternary LLM ships in 19.8 MB, runs at 1,900 tok/s on CPU](https://www.reddit.com/r/MachineLearning/comments/1wgzpli/i_trained_a_44m_parameter_quantized_llm_from/) ⭐️ 7.0/10

A developer released SHADOW-50M, a 44M-parameter LLM trained from scratch on 45B tokens, which ships as a complete 19.8 MB model with ternary {-1,0,+1} weights and runs at roughly 1,900 tokens per second on a laptop CPU using about 41 MB of RAM. The model replaces a trained embedding table with a 73,880-token vocabulary encoded as fixed 512-bit fingerprints, and uses a 159 KB compiled kernel that also runs in a browser via WebAssembly at around 500 tok/s. It shows that extreme quantization plus a fixed calculation circuit can make small models both tiny and practically useful on commodity CPUs and in browsers, which matters for offline, privacy-preserving, and edge deployments where GPUs are unavailable. It also offers a transparent comparison against a larger bf16 Llama-style baseline, exposing where the approach wins and where it loses. SHADOW-50M is a proof of concept that loses to a 51.8M-parameter bf16 Llama-style model (Supra-50M-Reasoning) on standard benchmarks such as ARC-Easy (0.307 vs 0.435), PIQA (0.570 vs 0.600), and WikiText-2 perplexity (186 vs 165), but it handles arithmetic, dates, and record retrieval through a fixed circuit that emits answers in the same token stream without tool calls. Its disk archive stores attention states at 1 bit (288 bytes/token) with a 22-byte/token index, and a persistent reinforcement trail improved measured top-1 retrieval from 0.571 to 0.743 without retraining.

reddit · r/MachineLearning · /u/Final-Data-1410 · Sep 15, 12:59

**Background**: Ternary weight networks constrain model weights to +1, 0, and -1, which drastically cuts memory and enables efficient integer arithmetic, though it usually costs accuracy compared with full-precision or 8-bit models. Quantized LLM inference on CPUs is typically done with libraries such as llama.cpp or ONNX Runtime, and in-browser inference usually relies on WebGPU or WebAssembly; this project pushes both ideas to an extreme with a tiny custom kernel and fingerprint-based vocabulary.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1605.04711">[1605.04711] Ternary Weight Networks - arXiv.org</a></li>
<li><a href="https://apxml.com/courses/practical-llm-quantization/chapter-6-evaluating-deploying-quantized-llms/hardware-quantized-inference">Hardware (CPU, GPU) for Quantized LLM Inference</a></li>
<li><a href="https://github.com/mlc-ai/web-llm">GitHub - mlc-ai/web-llm: High-performance In-browser LLM Inference Engine · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Quantization`, `#Efficient Inference`, `#Edge Computing`, `#Model Compression`

---