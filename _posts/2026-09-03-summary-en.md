---
layout: default
title: "Horizon Summary: 2026-09-03 (EN)"
date: 2026-09-03
lang: en
---

> From 82 items, 15 important content pieces were selected

---

1. [Meta's Muse Spark 1.3 tops DeepSWE, offers low-cost AI coding](#item-1) ⭐️ 8.0/10
2. [Google Releases Gemini 3.8 Flash and Flash Cyber](#item-2) ⭐️ 8.0/10
3. [OpenAI's Astra Model Hits Critical Cyber Threshold with New Safeguards](#item-3) ⭐️ 8.0/10
4. [OpenAI enables ChatGPT to securely connect EHR and healthcare data](#item-4) ⭐️ 8.0/10
5. [Paint.NET Rewrites Direct2D for Wine Using AI](#item-5) ⭐️ 8.0/10
6. [Claude Fable 5.1 Impresses on Science Benchmark, Pelican Test](#item-6) ⭐️ 8.0/10
7. [US Government Backs OpenAI in Copyright Case, Citing AI Competitiveness](#item-7) ⭐️ 8.0/10
8. [Uber beats Waymo to launch London's first robotaxi service](#item-8) ⭐️ 8.0/10
9. [Anthropic Publishes Claude System Prompts, Tightens Song Lyric Restrictions](#item-9) ⭐️ 7.0/10
10. [OpenAI Codex Desktop App Bundles LibreOffice and Runtimes](#item-10) ⭐️ 7.0/10
11. [Python 3.15.0 Release Candidate 2 Announced](#item-11) ⭐️ 7.0/10
12. [Hackers Likely Breached Major ID Verification Service, 150M Photos Stolen](#item-12) ⭐️ 7.0/10
13. [Google buys 400 MW enhanced geothermal from Fervo, expandable to 1 GW](#item-13) ⭐️ 7.0/10
14. [HiddenLayer Raises $100M for AI Deployment Security](#item-14) ⭐️ 7.0/10
15. [CTTI Performance Claimed Exponential, RTTI Linear](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Meta's Muse Spark 1.3 tops DeepSWE, offers low-cost AI coding](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta has released Muse Spark 1.3, a multimodal reasoning model that achieves a top score of 75.4 on the DeepSWE benchmark, surpassing previous leaders. The model is priced at $1.25 per million input tokens and $4.25 per million output tokens, with a 1,048,576-token context window. This release is significant because it demonstrates that cost-effective models can achieve state-of-the-art performance on challenging benchmarks like DeepSWE, intensifying competition among AI providers. The low pricing and strong performance could drive down costs across the industry and make advanced AI coding assistance more accessible to developers. Muse Spark 1.3 is designed for long-running agentic, multi-agent, and coding workflows, and is available via OpenRouter and other providers. Meta also offers a 'contributor' version with adjusted pricing that explicitly acknowledges training on user data, a move that has drawn positive attention for transparency.

hackernews · bvaldivielso · Sep 2, 19:35 · [Discussion](https://news.ycombinator.com/item?id=49541256)

**Background**: DeepSWE is a long-horizon software engineering benchmark from Datacurve that measures an AI agent's ability to autonomously resolve real-world coding issues end to end, using original tasks from active open-source repositories. It is designed to differentiate models as existing benchmarks saturate. Muse Spark is Meta's series of cost-efficient AI models aimed at practical coding and agentic tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/meta/muse-spark-1.3">Muse Spark 1 . 3 - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://llm-stats.com/models/muse-spark-1.3">Muse Spark 1 . 3 API Pricing, Context Window & Benchmarks</a></li>
<li><a href="https://deepswe.datacurve.ai/">DeepSWE</a></li>

</ul>
</details>

**Discussion**: Community comments are largely positive, with users praising the model's performance and cost-effectiveness. Simon Willison shared a hands-on test showing improved SVG generation quality, while others highlighted the competitive pricing and the transparency of Meta's 'contributor' tier. Some users expressed concerns about data training implications but appreciated the explicit pricing distinction.

**Tags**: `#AI`, `#Meta`, `#Muse Spark`, `#benchmarks`, `#model release`

---

<a id="item-2"></a>
## [Google Releases Gemini 3.8 Flash and Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 8.0/10

Google has released Gemini 3.8 Flash and a specialized variant, Gemini 3.8 Flash Cyber, which is designed to autonomously discover software vulnerabilities and generate patches. The models are available via the Gemini API and are noted for their speed and cost efficiency. This release strengthens Google's position in the competitive AI model market by offering a fast, cheap, and high-performing model that excels in practical tasks like HTML generation and agentic workflows. The Cyber variant addresses the growing need for automated cybersecurity solutions, potentially impacting how vulnerabilities are discovered and patched. Gemini 3.8 Flash supports multimodal input (audio, video, image) and has a 1.0M-token context window, with pricing starting at $0.750 per million input tokens and $3.75 per million output tokens. It offers customizable effort levels (low, medium, high) to balance quality, cost, and latency, and benchmarks show it matches or exceeds models like Opus 5 on certain intelligence scores.

hackernews · bratao · Sep 2, 15:12 · [Discussion](https://news.ycombinator.com/item?id=49537553)

**Background**: Gemini 3.8 Flash is the latest iteration in Google's Gemini 3 model family, building on Gemini 3.7 Flash. It is designed for fast and cost-effective inference, making it suitable for high-volume applications. The Flash Cyber variant is specialized for cybersecurity tasks, such as vulnerability discovery and patch generation, reflecting a trend toward AI-driven security automation.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3.8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://llm-stats.com/models/gemini-3.8-flash">Gemini 3 . 8 Flash API Pricing, Context Window & Benchmarks</a></li>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash">Gemini 3 . 8 Flash | Gemini API | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: Community members are excited about the model's speed and cost-effectiveness, with Simon Willison demonstrating impressive HTML generation for under 2 cents. Others note strong benchmark performance, with one user reporting it tops DeepSwe and matches Opus 5 on intelligence scores. Some users compare it to previous versions, noting potential regressions in low-effort thinking, and highlight its multimodal capabilities as a key differentiator.

**Tags**: `#AI`, `#Gemini`, `#model release`, `#benchmarks`, `#cost efficiency`

---

<a id="item-3"></a>
## [OpenAI's Astra Model Hits Critical Cyber Threshold with New Safeguards](https://openai.com/index/path-to-astra) ⭐️ 8.0/10

OpenAI announced that its upcoming Astra model is the first to meet the Critical cybersecurity capability threshold under its Preparedness Framework, prompting the company to implement stronger safeguards, including training to refuse harmful cyber requests and universal monitoring for risky actions. This marks a significant milestone in AI safety, as it is the first time a model has reached such a high capability level, raising concerns about potential misuse. The enhanced safeguards and collaboration with government agencies set a precedent for how frontier AI models with advanced cyber capabilities should be managed. Astra uses a technique called 'recurrent depth,' which allows the model to operate outside sequential thinking, potentially improving reasoning efficiency. OpenAI has halted a significant number of training runs to implement new safety procedures, and access to some advanced cybersecurity capabilities will be restricted upon release.

rss · OpenAI Blog · Sep 1, 13:00

**Background**: OpenAI's Preparedness Framework defines a Critical cybersecurity threshold for models that can autonomously develop zero-day exploits or devise novel cyberattack strategies. Recurrent depth is a neural architecture technique where layers are reused to create deeper models without increasing parameter count, enabling adaptive computation. These concepts are relevant to understanding the significance of Astra's capabilities and the safety measures being taken.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/">Responding to the next frontier of critical cyber capabilities | OpenAI</a></li>
<li><a href="https://www.wired.com/story/openai-overhauls-safety-protocols-after-its-ai-agents-went-rogue/">OpenAI Overhauls Safety Protocols After Its AI Agents Went Rogue | WIRED</a></li>

</ul>
</details>

**Tags**: `#AI`, `#OpenAI`, `#cybersecurity`, `#model release`, `#safety`

---

<a id="item-4"></a>
## [OpenAI enables ChatGPT to securely connect EHR and healthcare data](https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources) ⭐️ 8.0/10

OpenAI announced that ChatGPT can now securely connect to electronic health records (EHR) and other trusted healthcare data sources, allowing clinicians to access patient context and medical research within the chat interface. This integration is part of a broader effort to apply AI in clinical workflows. This development is significant because it brings large language models into high-stakes healthcare settings, potentially improving clinical efficiency and decision-making. It could affect how clinicians interact with patient data and may set a precedent for AI integration in other sensitive domains. The announcement emphasizes secure connections to trusted healthcare data, but specific technical details about the integration, such as the underlying protocols or partnerships, are not fully disclosed. OpenAI also offers a separate 'ChatGPT Health' experience and a 'Healthcare Public Data' plugin that searches official public sources, which are read-only and do not access patient charts.

rss · OpenAI Blog · Sep 1, 12:00

**Background**: An electronic health record (EHR) is a digital version of a patient's paper chart, containing health information collected over time by providers. EHRs are known to contribute to clinician burnout due to complex record-keeping and administrative burdens. Integrating AI like ChatGPT with EHRs aims to reduce that burden by providing quick access to patient context and relevant research, potentially improving care.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/chatgpt-connects-health-records-and-healthcare-sources/">Healthcare organizations can now connect EHR and additional ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Electronic_health_record">Electronic health record - Wikipedia</a></li>
<li><a href="https://healthit.gov/health-it-basics/benefits-ehrs/">Benefits of EHRs - ONC - Office of the National Coordinator for Health Information Technology</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Healthcare`, `#ChatGPT`, `#EHR`, `#Integration`

---

<a id="item-5"></a>
## [Paint.NET Rewrites Direct2D for Wine Using AI](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Rick Brewster, the developer of Paint.NET, announced that the application now includes an internal, from-scratch, clean-room reverse-engineered rewrite of Direct2D, triggered by a /wine flag, to enable experimental Wine/Linux support. This rewrite, totaling 180,000 lines of code, was primarily written by the AI assistant Claude. This marks a significant milestone in software compatibility, as Direct2D has been the biggest hurdle for running Paint.NET on Wine. It also demonstrates the growing capability of AI-assisted development in complex, large-scale software engineering, potentially influencing how future compatibility layers and reverse-engineering projects are approached. The rewrite is housed in PaintDotNet.Windows.Direct2D1.Managed.dll and is described as 'vibe coded,' meaning it has not been thoroughly reviewed. Brewster noted that he had to supervise Claude to ensure correct resource management, such as proper AddRef() calls for COM reference counting, and occasionally correct poor design decisions, though Claude also performed clever reverse engineering to implement Direct2D's built-in effects library.

rss · Simon Willison · Sep 2, 05:50

**Background**: Direct2D is a 2D vector graphics API from Microsoft, used for high-performance rendering in Windows applications. Wine is a free and open-source compatibility layer that allows Windows applications to run on Unix-like operating systems by translating Windows API calls into POSIX calls. Clean-room reverse engineering involves recreating a design without infringing copyrights, typically by having a team work from specifications without direct knowledge of the original code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct2D">Direct2D - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clean-room_reverse_engineering">Clean-room reverse engineering</a></li>

</ul>
</details>

**Tags**: `#Direct2D`, `#Wine`, `#AI-assisted development`, `#reverse engineering`, `#Paint.NET`

---

<a id="item-6"></a>
## [Claude Fable 5.1 Impresses on Science Benchmark, Pelican Test](https://simonwillison.net/2026/Sep/1/claude-fable-5-1/) ⭐️ 8.0/10

Anthropic released Claude Fable 5.1, which achieved a 52.6% score on the new Terminal-Bench-Science 0.1 benchmark, up from 24.7% for Fable 5. Simon Willison tested its 'pelican' abilities across reasoning levels, finding that low and medium settings skipped reasoning entirely. The significant improvement on the science benchmark suggests Fable 5.1 could be a major step forward for AI in scientific research, potentially accelerating discovery and analysis. The pelican test highlights the model's creative and reasoning capabilities, which are important for user engagement and practical applications. Fable 5.1 offers five reasoning levels (low, medium, high, xhigh, max) with no option to disable reasoning. In Willison's tests, low and medium settings produced no reasoning traces and similar output token counts, suggesting the model may skip reasoning for simple prompts.

rss · Simon Willison · Sep 1, 23:57

**Background**: Terminal-Bench-Science is a new benchmark for evaluating AI agents on expert-curated scientific research workflows. The 'pelican on a bicycle' benchmark, popularized by Simon Willison, tests a model's ability to generate an SVG image of a pelican riding a bicycle, serving as a creative and visual reasoning test.

<details><summary>References</summary>
<ul>
<li><a href="https://www.terminal-bench-science.ai/">TERMINAL-BENCH-SCIENCE</a></li>
<li><a href="https://github.com/harbor-framework/terminal-bench-science/">GitHub - harbor-framework/terminal-bench-science: Terminal ...</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark) - Grokipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Claude`, `#benchmark`, `#Anthropic`, `#LLM`

---

<a id="item-7"></a>
## [US Government Backs OpenAI in Copyright Case, Citing AI Competitiveness](https://techcrunch.com/2026/09/02/u-s-government-sides-with-openai-on-issue-of-training-llms-on-copyrighted-material/) ⭐️ 8.0/10

The Trump administration has filed a legal brief in The New York Times' copyright lawsuit against OpenAI, arguing that training AI models on copyrighted material constitutes fair use. The brief emphasizes the national interest in maintaining a competitive AI industry. This marks a significant government intervention in a landmark case that could set precedent for AI training practices and copyright law. The outcome may shape future regulations and impact the broader AI ecosystem, affecting developers, content creators, and legal frameworks. The lawsuit, filed in December 2023, alleges OpenAI unlawfully used NYT articles to train its models and seeks billions in damages. The government's brief argues that AI training is fair use, aligning with previous court rulings that have favored AI companies.

rss · TechCrunch · Sep 2, 17:09

**Background**: Fair use is a U.S. legal doctrine allowing limited use of copyrighted material without permission for purposes like commentary, criticism, or research. The case is part of a broader debate over whether training AI on copyrighted works infringes copyright, with implications for innovation and content ownership.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fair_use">Fair use - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/The_New_York_Times_v._Microsoft_and_OpenAI">The New York Times v. Microsoft and OpenAI - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/09/02/technology/justice-department-openai-copyright-suit.html">Justice Department Sides With OpenAI in New York Times ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#copyright`, `#legal`, `#policy`, `#OpenAI`

---

<a id="item-8"></a>
## [Uber beats Waymo to launch London's first robotaxi service](https://www.theverge.com/news/988415/uber-wayve-robotaxi-london-launch) ⭐️ 8.0/10

Uber has launched London's first commercial robotaxi service, using autonomous driving technology developed by UK-based startup Wayve. The service, which began on September 2, 2026, initially operates with safety drivers behind the wheel, beating Waymo to this milestone. This marks a significant milestone in the autonomous vehicle industry, as London is a major global city with complex road conditions. It demonstrates Uber's ability to partner with AV startups to deploy robotaxis, potentially reshaping urban mobility and intensifying competition with Waymo. The robotaxis use Wayve's end-to-end deep learning approach, which avoids detailed 3D maps and hand-coded rules. The service will initially feature safety drivers, and London's winding, centuries-old streets present unique challenges compared to cities like Los Angeles and San Francisco.

rss · The Verge · Sep 2, 23:00

**Background**: Wayve is a British autonomous driving company founded in 2017 by University of Cambridge researchers, focusing on self-learning 'AI driver' systems. Uber has been planning a UK launch with Wayve for several years, while Waymo has also been testing its vehicles in London, aiming to launch its own service this year.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wayve">Wayve - Wikipedia</a></li>
<li><a href="https://www.axios.com/2026/09/02/robotaxis-london-uber-wayve">Robotaxis arrive in London — with humans still behind the wheel</a></li>
<li><a href="https://techcrunch.com/2026/04/14/london-gets-closer-to-its-first-robotaxi-service-as-waymo-begins-testing/">London gets closer to its first robotaxi service as... | TechCrunch</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-09-02/uber-wayve-launch-robotaxi-service-in-london-to-compete-with-waymo">Uber, Wayve Launch Robotaxi Service in London to... - Bloomberg</a></li>

</ul>
</details>

**Tags**: `#autonomous vehicles`, `#robotaxi`, `#Uber`, `#Wayve`, `#London`

---

<a id="item-9"></a>
## [Anthropic Publishes Claude System Prompts, Tightens Song Lyric Restrictions](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) ⭐️ 7.0/10

Anthropic has reorganized its published system prompts for Claude consumer apps into a per-model index page, with each model having its own page and historical versions. The latest update for Fable 5.1 adds a substantial new section explicitly prohibiting the reproduction of song lyrics, poems, or book passages, with specific rules about declining reworded requests. This transparency initiative is valuable for AI researchers and users, as it allows for easy diffing of prompts to understand how model behavior evolves. The specific focus on song lyrics reflects ongoing legal and ethical pressures on AI companies to avoid copyright infringement, which could shape future content policies across the industry. The system prompts are available on platform.claude.com/docs, and pages can be accessed in Markdown by appending .md, making them easy to diff. The new lyric restriction applies to works published after 1929, and Claude declines requests when unsure of the work's date, even if the user claims it is their own.

rss · Simon Willison · Sep 2, 14:16

**Background**: System prompts are the hidden instructions given to AI models before user interactions, shaping their behavior and constraints. Anthropic's practice of publishing these prompts is part of a broader trend toward transparency in AI, allowing external scrutiny of how models are guided. The recent update likely responds to legal challenges from music publishers over AI-generated lyrics.

**Tags**: `#AI`, `#Anthropic`, `#system prompts`, `#transparency`, `#Claude`

---

<a id="item-10"></a>
## [OpenAI Codex Desktop App Bundles LibreOffice and Runtimes](https://simonwillison.net/2026/Sep/1/codex-libreoffice/) ⭐️ 7.0/10

Simon Willison discovered that OpenAI's Codex desktop app (now rebranded as ChatGPT) bundles a full Python installation, Node.js, Poppler, git, and LibreOffice in its ~/.cache/codex-runtimes/codex-primary-runtime folder, totaling 1.7GB. The app includes skills in the plugins/documents folder that tell Codex how to use these binaries. This bundling hints at OpenAI's plans to enable local document processing and analysis within the Codex/ChatGPT desktop app, potentially allowing users to work with office documents and PDFs offline. It also raises questions about the app's resource footprint and the strategic use of open-source software. The runtime folder includes 771MB of native binaries, with libreoffice-headless taking 429.7MB, poppler 187.9MB, and git 148.1MB. The presence of skills in the plugins/documents folder suggests Codex is being prepared to handle document-related tasks using these tools.

rss · Simon Willison · Sep 1, 19:03

**Background**: Codex is OpenAI's AI assistant that can execute code and perform tasks on a user's computer. Bundling runtimes like Python and Node.js allows it to run scripts, while LibreOffice and Poppler enable document conversion and PDF rendering. This discovery was made using OmniDiskSweeper, a macOS disk space analyzer that shows file sizes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OmniDiskSweeper">OmniDiskSweeper - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Poppler_(software)">Poppler ( software ) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#OpenAI`, `#Codex`, `#LibreOffice`, `#software`, `#AI`

---

<a id="item-11"></a>
## [Python 3.15.0 Release Candidate 2 Announced](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 7.0/10

Python 3.15.0 release candidate 2 has been announced by release manager Hugo van Kemenade, marking the final RC before the stable release scheduled for October. Third-party maintainers are strongly encouraged to test and publish wheels for Python 3.15. This release candidate is a critical milestone for the Python ecosystem, as it signals the feature freeze and allows maintainers to ensure compatibility before the final release. Early testing helps avoid shipping bugs like the one Simon Willison found in Python 3.10. During the RC phase, only reviewed bug fixes are allowed. Binary wheels built against this RC will work with future Python 3.15 versions. The RC is not yet available on GitHub Actions, but can be tested using actions/setup-python with allow-prereleases and check-latest flags.

rss · Simon Willison · Sep 1, 14:59

**Background**: Python uses a release candidate phase to stabilize the codebase before the final release. Wheels are pre-built binary packages that speed up installation and are essential for projects with C extensions. The manylinux project defines platform tags for portable Linux wheels.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.python.org/2026/08/python-3150-rc1/">Python 3.15.0 candidate 1 is here! | Python Insider</a></li>
<li><a href="https://www.python.org/downloads/release/python-3150rc2/">Python Release Python 3.15.0rc2 | Python.org</a></li>
<li><a href="https://simonwillison.net/2026/Sep/1/python-315-rc-2/">Python 3.15.0 candidate 2 is here! - simonwillison.net</a></li>

</ul>
</details>

**Tags**: `#Python`, `#release`, `#programming language`, `#software development`

---

<a id="item-12"></a>
## [Hackers Likely Breached Major ID Verification Service, 150M Photos Stolen](https://techcrunch.com/2026/09/02/it-sure-looks-like-hackers-breached-a-major-id-card-verification-service/) ⭐️ 7.0/10

An identity theft search site claimed to have stolen more than 150 million driver's license photos from an ID verification service, and the crime site has since shut down. Security researchers suspect the breach originated from the identity verification service IDScan. This breach is highly significant as it exposes sensitive personal data of millions of individuals, potentially enabling identity theft and fraud. It underscores the risks associated with centralized identity verification services and the need for stronger security measures. The stolen data reportedly includes driver's license photos, which can be used for facial recognition and identity fraud. The Department of Defense is aware of the reports and evaluating them, while the FBI is investigating a related service selling over 153 million driver's licenses.

rss · TechCrunch · Sep 2, 19:35

**Background**: Identity verification services like IDScan are used by companies to verify customer identities, often by scanning government-issued IDs. A breach in such a service can expose vast amounts of personal data, which criminals may exploit for identity theft or sell on the dark web.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/09/02/it-sure-looks-like-hackers-breached-a-major-id-card-verification-service/">It sure looks like hackers breached a major ID card verification service</a></li>
<li><a href="https://krebsonsecurity.com/2026/09/fbi-probes-service-selling-153m-drivers-licenses/">FBI Probes Service Selling 153M+ Drivers Licenses – Krebs on Security</a></li>

</ul>
</details>

**Tags**: `#security`, `#data breach`, `#privacy`, `#identity verification`

---

<a id="item-13"></a>
## [Google buys 400 MW enhanced geothermal from Fervo, expandable to 1 GW](https://techcrunch.com/2026/09/02/enhanced-geothermal-notches-another-win-as-google-buys-400-mw-from-fervo/) ⭐️ 7.0/10

Google has signed a deal to purchase 400 megawatts (MW) of enhanced geothermal power from Fervo Energy, with the option to expand to 1 gigawatt (GW). This agreement is intended to supply a very large AI data center in Utah. This deal marks a significant commercial milestone for enhanced geothermal energy, demonstrating its viability as a clean, baseload power source for energy-intensive AI data centers. It could accelerate adoption of EGS technology and help meet the growing electricity demands of the tech industry. The agreement is expandable to 1 GW, which is enough to power a very large AI data center. Fervo Energy is a Houston-based company specializing in enhanced geothermal systems (EGS), and this deal follows its earlier successful pilot project, Project Red, which generated 3 MW of baseload power.

rss · TechCrunch · Sep 2, 16:54

**Background**: Enhanced geothermal systems (EGS) generate electricity by extracting heat from hot, dry, and impermeable rock formations deep underground, using techniques like hydraulic stimulation to create reservoirs. Unlike traditional geothermal, which requires natural hydrothermal resources, EGS can be deployed in more locations, offering a reliable, 24/7 carbon-free energy source. Fervo Energy, co-founded in 2017, is a pioneer in this field and is developing projects like Cape Station.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Enhanced_geothermal_system">Enhanced geothermal system</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fervo_Energy">Fervo Energy</a></li>
<li><a href="https://www.energy.gov/hgeo/geothermal/enhanced-geothermal-systems">Enhanced Geothermal Systems | Department of Energy</a></li>

</ul>
</details>

**Tags**: `#geothermal`, `#renewable energy`, `#AI infrastructure`, `#Google`, `#data centers`

---

<a id="item-14"></a>
## [HiddenLayer Raises $100M for AI Deployment Security](https://techcrunch.com/2026/09/02/hiddenlayer-nabs-100m-as-enterprises-rush-to-secure-their-ai-deployments/) ⭐️ 7.0/10

HiddenLayer has secured $100 million in funding to address the rising demand for AI deployment security, focusing on monitoring agents and their tools. The investment reflects the urgency among enterprises to protect their AI systems. This funding underscores the growing importance of AI security in enterprise deployments, as companies rush to secure their AI investments. It signals strong market validation for AI security startups and highlights a critical area of concern for organizations adopting AI technologies. The funding will likely be used to expand HiddenLayer's capabilities in monitoring AI agents and their associated tools and add-ons. This comes as security companies scramble to build products that can oversee the entire AI ecosystem, including runtime behavior and interactions.

rss · TechCrunch · Sep 2, 15:01

**Background**: AI security is a rapidly evolving field focused on protecting AI systems from threats like prompt injection, data poisoning, and model theft. As enterprises increasingly deploy AI agents that automate decision-making, there is a critical need for monitoring tools that provide runtime visibility and anomaly detection. Companies like Obsidian Security and IBM are also developing solutions to secure AI agent interactions and workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.obsidiansecurity.com/blog/ai-agent-monitoring-tools">Real-Time AI Agent Monitoring: Detecting Threats Before They ...</a></li>
<li><a href="https://www.ibm.com/think/tutorials/ai-agent-security">AI Agent Security Best Practices and Tutorial | IBM</a></li>
<li><a href="https://www.venn.com/learn/ai-security/ai-security-tools/">AI Security Tools: 13 Best Platforms Compared for 2026</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#enterprise`, `#funding`, `#AI deployments`

---

<a id="item-15"></a>
## [CTTI Performance Claimed Exponential, RTTI Linear](https://www.reddit.com/r/programming/comments/1w5ov1s/ctti_is_exponential_rtti_is_linear/) ⭐️ 7.0/10

A Reddit post in r/programming claims that compile-time type information (CTTI) is exponential in performance, while runtime type information (RTTI) is linear, sparking discussion among C++ developers. This comparison highlights a potential performance trade-off between CTTI and RTTI, which could influence developers' choices in performance-critical C++ applications. Understanding these characteristics is important for optimizing compile-time and runtime behavior. The post lacks detailed content, but the claim suggests that CTTI, which resolves type information at compile time, may lead to exponential code bloat or compilation time, whereas RTTI, resolved at runtime, scales linearly. The discussion likely involves trade-offs in compilation speed, binary size, and runtime overhead.

reddit · r/programming · /u/gingerbill · Sep 2, 22:08

**Background**: CTTI (Compile-Time Type Information) is a technique in C++ that provides type information at compile time, often using template metaprogramming, to avoid runtime overhead. RTTI (Run-Time Type Information) is a built-in C++ feature that identifies object types at runtime, typically using typeid and dynamic_cast. The performance characteristics of these approaches are relevant for developers working on large codebases or performance-sensitive systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Manu343726/ctti">GitHub - Manu343726/ctti: Compile Time Type Information for C++</a></li>
<li><a href="https://en.wikipedia.org/wiki/Run-time_type_information">Run-time type information - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/cpp/rtti-run-time-type-information-in-cpp/">RTTI (Run-Time Type Information) in C++ - GeeksforGeeks</a></li>

</ul>
</details>

**Discussion**: No comments were provided in the news item, so community sentiment cannot be summarized.

**Tags**: `#C++`, `#type information`, `#performance`, `#compiler`

---