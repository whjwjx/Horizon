---
layout: default
title: "Horizon Summary: 2026-06-21 (EN)"
date: 2026-06-21
lang: en
---

> From 50 items, 11 important content pieces were selected

---

1. [Nobel laureate John Jumper leaves DeepMind for Anthropic](#item-1) ⭐️ 9.0/10
2. [Atlantic Publishes Searchable Database of AI Music Training Data](#item-2) ⭐️ 8.0/10
3. [MCP's Key Value: Auth Isolation Outside Agent Context](#item-3) ⭐️ 7.0/10
4. [VLC creator builds open-source infrastructure for robots](#item-4) ⭐️ 7.0/10
5. [Export Controls on Cybersecurity Software Have a History of Failure](#item-5) ⭐️ 7.0/10
6. [US Questions ASML Chip Tool in China, ASML Denies](#item-6) ⭐️ 7.0/10
7. [Elastic to acquire Deductive AI for up to $85M](#item-7) ⭐️ 7.0/10
8. [NASA Picks Relativity Space for 2028 Mars Mission](#item-8) ⭐️ 7.0/10
9. [Build Your Own LLM Workshop Released on YouTube](#item-9) ⭐️ 7.0/10
10. [Should ML PhDs Graduate Without Top-Tier Papers?](#item-10) ⭐️ 7.0/10
11. [DVD-JEPA: Open-Source Minimal JEPA World Model](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Nobel laureate John Jumper leaves DeepMind for Anthropic](https://techcrunch.com/2026/06/20/nobel-laureate-john-jumper-is-leaving-deepmind-for-rival-anthropic/) ⭐️ 9.0/10

John Jumper, a Nobel laureate and key figure behind AlphaFold, has left Google DeepMind to join rival AI company Anthropic. This move signals a major talent shift in the AI industry, potentially accelerating Anthropic's research while weakening DeepMind's leadership in protein folding and AI for science. Jumper is not the only high-profile departure from DeepMind recently, indicating a broader trend of top talent moving to competing labs.

rss · TechCrunch · Jun 20, 16:39

**Background**: John Jumper led the development of AlphaFold, an AI system that predicts protein structures with high accuracy, earning him a Nobel Prize in Chemistry. DeepMind, a subsidiary of Google, has been a leader in AI research, while Anthropic focuses on safe and ethical AI development.

**Tags**: `#AI`, `#DeepMind`, `#Anthropic`, `#talent`, `#industry news`

---

<a id="item-2"></a>
## [Atlantic Publishes Searchable Database of AI Music Training Data](https://www.theverge.com/ai-artificial-intelligence/953183/the-atlantic-searchable-database-music-ai-training-data) ⭐️ 8.0/10

The Atlantic, through reporter Alex Reisner, uncovered four datasets containing roughly 21.2 million music tracks used to train AI models and made them publicly searchable. The largest dataset includes 12 million tracks, and a second has 9 million tracks. This unprecedented transparency reveals the massive scale of copyrighted material in AI training datasets, enabling scrutiny of copyright and ethical issues. It provides a crucial tool for researchers, artists, and the public to understand what music powers generative AI systems. Two of the datasets are enormous (12 million and 9 million tracks), while the other two are smaller but still significant, each containing about 100,000 tracks. The database is fully searchable, allowing users to look up specific songs or artists.

rss · The Verge · Jun 20, 18:46

**Background**: Generative AI music models, such as those from Suno and Google, are trained on vast collections of audio to learn patterns and generate new music. The datasets used are often scraped from the internet without explicit permission, raising copyright concerns. This investigation brings much-needed transparency to the opaque world of AI training data.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/ai-artificial-intelligence/953183/the-atlantic-searchable-database-music-ai-training-data">The Atlantic created a searchable database of the music used to train AI | The Verge</a></li>
<li><a href="https://hypebeast.com/2026/6/ai-music-datasets-exposed-in-suno-copyright-clash">AI Music Datasets and Suno Copyright Clash Explained | Hypebeast</a></li>
<li><a href="https://www.theatlantic.com/technology/2026/06/ai-music-generators-suno-google-udio/687485/">The Millions of Songs Mashed Into AI -Generated Music - The Atlantic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#music`, `#training data`, `#copyright`, `#transparency`

---

<a id="item-3"></a>
## [MCP's Key Value: Auth Isolation Outside Agent Context](https://simonwillison.net/2026/Jun/19/sean-lynch/#atom-everything) ⭐️ 7.0/10

Sean Lynch proposed that the primary value of the Model Context Protocol (MCP) is isolating authentication flows outside the agent's context window, potentially even outside the harness entirely. He suggested the idealized form of MCP might be just an auth gateway for the API. This insight reframes MCP's role from a general data connectivity protocol to a security-focused layer, which could simplify agent architecture and reduce attack surfaces. It highlights a practical benefit that may drive broader adoption of MCP in production AI systems. Lynch contrasts MCP with traditional skills/CLI approaches, arguing that auth isolation is the real differentiator. He notes that even if MCP does nothing else beyond being an auth gateway, it would still be a win.

rss · Simon Willison · Jun 19, 22:45

**Background**: The Model Context Protocol (MCP) is an open standard announced by Anthropic in November 2024 for connecting AI applications to external data sources and tools. It provides a standardized interface for reading files, executing functions, and handling contextual prompts, and has been adopted by major AI providers like OpenAI and Google DeepMind. In agentic systems, managing authentication securely is challenging because credentials often reside within the agent's context window, creating security risks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#model-context-protocol`, `#llms`, `#ai`, `#authentication`, `#agent`

---

<a id="item-4"></a>
## [VLC creator builds open-source infrastructure for robots](https://techcrunch.com/2026/06/19/he-made-your-free-video-player-run-smoothly-now-hes-doing-that-for-robots/) ⭐️ 7.0/10

Jean-Baptiste Kempf, the lead developer of VLC media player, is building Kyber, an open-source infrastructure layer for real-time control of remote devices like robots and drones. This project could democratize real-time remote device control, enabling developers and companies to build scalable robotics and IoT applications on open-source foundations, similar to how VLC transformed media playback. Kyber aims to provide low-latency, reliable communication between humans or AI agents and remote hardware, addressing challenges like network jitter and synchronization at global scale.

rss · TechCrunch · Jun 20, 00:47

**Background**: Jean-Baptiste Kempf is known for leading VLC, an open-source media player with over 6 billion downloads. He has decades of experience in open-source development and has founded multiple companies. Kyber represents his move into robotics infrastructure, leveraging his expertise in real-time systems.

<details><summary>References</summary>
<ul>
<li><a href="http://jbkempf.com/">Jean-Baptiste Kempf — VLC, VideoLAN, Kyber & Open Source</a></li>
<li><a href="https://github.com/jbkempf">jbkempf (Jean-Baptiste Kempf) · GitHub Top Stories The VLC Creator Is Now Building Open Source Infrastructure ... VLC Developer Kyber Startup $5 M Lightspeed Robotics Drones VLC Player - Jean-Baptiste Kempf, 20 Years of Open Source ... VLC Player - Jean-Baptiste Kempf, 20 Years of Open Source ...</a></li>
<li><a href="https://europeanpurpose.com/news/the-vlc-creator-is-now-building-open-source-infrastructure-for-robots-and-drones">The VLC Creator Is Now Building Open Source Infrastructure ...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#robotics`, `#real-time`, `#infrastructure`, `#IoT`

---

<a id="item-5"></a>
## [Export Controls on Cybersecurity Software Have a History of Failure](https://techcrunch.com/2026/06/19/encryption-spyware-and-now-mythos-history-shows-why-cyber-export-control-doesnt-work/) ⭐️ 7.0/10

A TechCrunch article argues that export controls on cybersecurity software have historically failed, using the example of PGP in the 1990s, and questions their application to Anthropic's unreleased AI model Mythos. This matters because governments are considering export controls on advanced AI models like Mythos, but history suggests such measures are ineffective and may hinder innovation without stopping determined adversaries. The article highlights the U.S. government's failed attempt to control PGP encryption in the 1990s, which spread globally despite restrictions. It draws parallels to current debates over regulating Anthropic's Mythos, a powerful cybersecurity AI model.

rss · TechCrunch · Jun 19, 22:40

**Background**: Export controls are government restrictions on the transfer of certain technologies to other countries, often for national security reasons. PGP (Pretty Good Privacy) is an encryption program that became a symbol of the struggle over cryptography export controls in the 1990s. Anthropic's Mythos is an unreleased AI model that the company claims is too dangerous for public release, sparking global concern.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/19/encryption-spyware-and-now-mythos-history-shows-why-cyber-export-control-doesnt-work/">From PGP to Mythos: a brief history of export controls that didn't stop anyone | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States">Export of cryptography from the United States - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/what-is-mythos-and-why-are-experts-worried-about-anthropics-ai-model/">What is Mythos, Anthropic’s unreleased AI model, and how ...</a></li>

</ul>
</details>

**Tags**: `#export controls`, `#cybersecurity`, `#AI regulation`, `#encryption`, `#Anthropic`

---

<a id="item-6"></a>
## [US Questions ASML Chip Tool in China, ASML Denies](https://techcrunch.com/2026/06/19/the-us-says-asmls-top-chip-tool-may-be-in-china-asml-says-it-isnt/) ⭐️ 7.0/10

The US government has raised concerns that ASML's most advanced chipmaking equipment may be operating in China, but ASML denies the claim, stating it has never sold such tools to Chinese customers. This dispute highlights ongoing tensions in semiconductor export controls, as the US seeks to prevent China from accessing cutting-edge chip technology that could bolster its military and AI capabilities. ASML's extreme ultraviolet (EUV) lithography systems, essential for making the most advanced chips, have never been exported to China due to US-led export restrictions. The company's TWINSCAN NXE:3400B is one such high-end system.

rss · TechCrunch · Jun 19, 07:59

**Background**: ASML is a Dutch company that dominates the market for lithography machines used to print chip designs onto silicon wafers. Since 2018, the US has tightened export controls to restrict China's access to advanced semiconductor technologies, including EUV tools, which use US-origin components.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/tech-industry/china-vexed-at-expansion-of-asml-chip-tool-export-controls-reveals-ministry-statement">China vexed at expansion of ASML chip tool export ... | Tom's Hardware</a></li>
<li><a href="https://www.silicon.co.uk/workspace/asml-china-revoke-544240">ASML Chip System Export Licence For China Partially Revoked</a></li>
<li><a href="https://www.congress.gov/crs-product/R48642">U.S. Export Controls and China: Advanced Semiconductors</a></li>

</ul>
</details>

**Tags**: `#semiconductors`, `#geopolitics`, `#export controls`, `#ASML`, `#chip manufacturing`

---

<a id="item-7"></a>
## [Elastic to acquire Deductive AI for up to $85M](https://techcrunch.com/2026/06/18/source-elastic-agrees-to-buy-crv-backed-deductiveai-for-up-to-85m/) ⭐️ 7.0/10

Elastic has agreed to acquire Deductive AI, a startup that uses AI to automatically detect and resolve software bugs, for up to $85 million. This acquisition signals that AI-native operations tooling is becoming core infrastructure for observability platforms, and validates the market for autonomous incident resolution. Deductive AI was founded three years ago and raised a $7.5 million seed round from CRV less than a year before the acquisition.

rss · TechCrunch · Jun 19, 00:51

**Background**: Elastic is a publicly traded enterprise software company known for its Elasticsearch search and analytics engine. Deductive AI's technology uses artificial intelligence to automatically catch and resolve bugs in software, functioning as an AI site reliability engineer (SRE) for fast-moving teams.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/18/source-elastic-agrees-to-buy-crv-backed-deductiveai-for-up-to-85m/">Source: Elastic agrees to buy CRV-backed Deductive AI for up ...</a></li>
<li><a href="https://startupfortune.com/elastics-85-million-bet-on-deductiveai-is-a-signal-that-ai-native-ops-tooling-is-now-acquisition-currency/">Elastic's $85 million bet on DeductiveAI is a signal that AI ...</a></li>
<li><a href="https://creati.ai/ai-news/2026-06-20/elastic-acquires-deductive-ai-85m/">Elastic Acquires AI Bug-Detection Startup Deductive AI for Up ...</a></li>

</ul>
</details>

**Tags**: `#acquisition`, `#AI`, `#software engineering`, `#bug detection`, `#Elastic`

---

<a id="item-8"></a>
## [NASA Picks Relativity Space for 2028 Mars Mission](https://www.theverge.com/science/952988/nasa-relativity-space-eric-schmidt-mars) ⭐️ 7.0/10

NASA has selected Relativity Space, led by former Google CEO Eric Schmidt, to launch the Aeolus payload to Mars in 2028 under a new public-private partnership. This marks a significant shift toward leveraging private companies for deep space exploration, potentially reducing costs and accelerating Mars science. It also highlights Relativity Space's growing role in NASA's planetary missions. Relativity Space will provide the spacecraft, rocket, and cruise operations, while NASA supplies the Aeolus instrument suite to measure winds, water-ice clouds, and temperature on Mars. The mission is scheduled for 2028.

rss · The Verge · Jun 19, 18:41

**Background**: Relativity Space is an American aerospace company known for using 3D printing to manufacture rockets, including the in-development Terran R. The Aeolus mission aims to provide the first global, seasonal, and diurnal data on Mars' winds and climate, building on decades of Mars exploration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nasa.gov/news-release/nasa-announces-public-private-partnership-to-advance-mars-science/">NASA Announces Public-Private Partnership to Advance Mars Science - NASA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relativity_Space">Relativity Space</a></li>
<li><a href="https://ntrs.nasa.gov/citations/20200000616">The Aeolus Mission Concept, an Innovative Mission to Study the Winds and Climate of Mars - NASA Technical Reports Server (NTRS)</a></li>

</ul>
</details>

**Tags**: `#NASA`, `#Mars mission`, `#public-private partnership`, `#space exploration`, `#Relativity Space`

---

<a id="item-9"></a>
## [Build Your Own LLM Workshop Released on YouTube](https://www.reddit.com/r/MachineLearning/comments/1uazlnd/hi_reddit_i_posted_my_build_your_own_llm_workshop/) ⭐️ 7.0/10

Justin Angel published a free workshop video on YouTube that teaches how to build a large language model from scratch, covering ML fundamentals, transformer architecture, and training, with no math prerequisites. This resource lowers the barrier for beginners to understand and build LLMs, addressing a gap in accessible, code-first educational content for the rapidly evolving AI field. The workshop includes slides, Excel-based math intuition exercises, and coding examples in PyTorch, covering topics like SwiGLU, Kaiming initialization, RMSNorm, and instruction tuning.

reddit · r/MachineLearning · /u/JustinAngel · Jun 20, 15:36

**Background**: Building an LLM typically requires understanding deep learning, transformers, and training techniques. This workshop aims to teach these concepts without assuming prior math or ML knowledge, using code and Excel to build intuition.

<details><summary>References</summary>
<ul>
<li><a href="https://abdulkaderhelwan.medium.com/swiglu-activation-function-77627e0b2b52">SwiGLU Activation Function . SwiGLU (Swish-Gated Linear... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Weight_initialization">Weight initialization - Wikipedia</a></li>
<li><a href="https://machinelearningmastery.com/layernorm-and-rms-norm-in-transformer-models/">LayerNorm and RMS Norm in Transformer Models ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Machine Learning`, `#Tutorial`, `#Deep Learning`, `#Transformers`

---

<a id="item-10"></a>
## [Should ML PhDs Graduate Without Top-Tier Papers?](https://www.reddit.com/r/MachineLearning/comments/1uazlhg/would_you_let_an_ml_phd_student_graduate_without/) ⭐️ 7.0/10

A Reddit discussion asks whether an ML PhD student with solid work but no top-tier publications (e.g., NeurIPS, ICML, ICLR, CVPR) should be allowed to graduate, sparking debate on publication culture. This debate highlights tensions between publication metrics and genuine research quality in ML academia, potentially influencing graduation policies and student well-being. The student has three first-author A-level papers and a coherent thesis, but lacks publications in A* ML venues like NeurIPS, ICML, ICLR, or CVPR.

reddit · r/MachineLearning · /u/Hope999991 · Jun 20, 15:36

**Background**: In machine learning, top-tier conferences (e.g., NeurIPS, ICML, ICLR, CVPR) are highly competitive and often considered essential for academic career progression. Many PhD programs implicitly or explicitly require such publications for graduation.

<details><summary>References</summary>
<ul>
<li><a href="https://alexhernandezgarcia.com/resources/publication-venues-ml.html">Publication venues in machine learning and related fields</a></li>
<li><a href="https://algoverseairesearch.org/blog/icml-iclr-aaai-student-guide">Beyond NeurIPS: A Student's Guide to ICML, ICLR, AAAI, and ...</a></li>
<li><a href="https://icml.cc/public/JournalToConference">The NeurIPS/ICLR/ICML Journal-to-Conference Track</a></li>

</ul>
</details>

**Discussion**: The Reddit community is divided: some argue that solid work and A-level papers should suffice, while others insist that top-tier publications are essential for demonstrating impact and rigor.

**Tags**: `#machine learning`, `#PhD`, `#publication culture`, `#academia`, `#graduation standards`

---

<a id="item-11"></a>
## [DVD-JEPA: Open-Source Minimal JEPA World Model](https://www.reddit.com/r/MachineLearning/comments/1uatlzx/dvdjepa_an_opensource_fullyreproducible_jepa/) ⭐️ 7.0/10

DVD-JEPA is an open-source, fully reproducible implementation of the Joint-Embedding Predictive Architecture (JEPA) that learns to predict representations of a bouncing DVD logo in a 16×16 grid, achieving precise position recovery via linear probe. This work provides a minimal, honest demonstration of the JEPA concept, showing that predicting representations rather than pixels can yield a useful world model, and it runs entirely in a browser, making it accessible for education and experimentation. The model uses a context encoder, an EMA target encoder, and a latent predictor trained without labels or decoder; a linear probe recovers the logo's exact (y,x) position to within 0.73 pixels, and the predictor can 'dream' correct future frames for about 20 steps before latent drift occurs.

reddit · r/MachineLearning · /u/NielsRogge · Jun 20, 10:52

**Background**: JEPA (Joint-Embedding Predictive Architecture) is a self-supervised learning method proposed by Yann LeCun in 2022 that predicts abstract embeddings (latent representations) rather than pixel-level reconstruction. Traditional video prediction models often struggle with unpredictable pixel-level details, while JEPA discards unpredictable information in the encoder. A linear probe is a simple linear classifier attached to frozen representations to assess their semantic content.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Joint_Embedding_Predictive_Architecture">Joint Embedding Predictive Architecture</a></li>
<li><a href="https://www.emergentmind.com/topics/linear-probes">Linear Probes: Neural Network Diagnostics</a></li>

</ul>
</details>

**Discussion**: The community discussion is not provided in the input.

**Tags**: `#world models`, `#JEPA`, `#representation learning`, `#self-supervised learning`, `#video prediction`

---