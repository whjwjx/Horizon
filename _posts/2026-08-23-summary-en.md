---
layout: default
title: "Horizon Summary: 2026-08-23 (EN)"
date: 2026-08-23
lang: en
---

> From 43 items, 12 important content pieces were selected

---

1. [Linus Torvalds Credits AI for Debugging Linux Kernel Bug](#item-1) ⭐️ 8.0/10
2. [Uber Faces Nearly $1B GDPR Fine Over Automated Driver Suspensions](#item-2) ⭐️ 8.0/10
3. [Frontier AI Labs Lack Public Rogue Model Containment Plans](#item-3) ⭐️ 8.0/10
4. [Anthropic's Top AI Model Lags as Cheaper Alternatives Gain Traction](#item-4) ⭐️ 7.0/10
5. [High Cost of Fable Model Spurs Strategic AI Task Allocation](#item-5) ⭐️ 7.0/10
6. [Coding Agents: Instruct and Verify, Not Just Review](#item-6) ⭐️ 7.0/10
7. [Waymo's Custom Chip Powers Robotaxi Ambitions](#item-7) ⭐️ 7.0/10
8. [AI Training on Copyrighted Books: Legal Gray Area](#item-8) ⭐️ 7.0/10
9. [DeepMind Alumni's Inherent Faraday AI Outperforms Anthropic and OpenAI in Research Replication](#item-9) ⭐️ 7.0/10
10. [OpenAI Reverses Stance, Urges California to Strengthen AI Safety Bill SB 53](#item-10) ⭐️ 7.0/10
11. [US Battery Startups Find Defense Lifeline in $500M DOE Grants](#item-11) ⭐️ 7.0/10
12. [Michael Polansky trains AI on living human skin for skincare discovery](#item-12) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Linus Torvalds Credits AI for Debugging Linux Kernel Bug](https://simonwillison.net/2026/Aug/22/linus-torvalds/) ⭐️ 8.0/10

Linus Torvalds publicly acknowledged that an AI significantly assisted him in debugging a challenging Linux kernel issue in the Intel Xe graphics driver, specifically for Battlemage G21 cards. The AI helped with grunt work, adding debug code and analyzing results, despite initially declaring the problem unsolvable. This endorsement from a highly respected figure like Torvalds highlights the growing utility of AI in complex software development, potentially encouraging wider adoption in kernel and systems programming. It also underscores the collaborative potential of AI tools, even when they express pessimism, as long as the human persists. The debugging session involved 24 debug patches and 18 kernel boots to isolate the bug, which caused GDM to restart endlessly. Torvalds noted that the AI repeatedly said the problem was impossible, but it faithfully added debug code and analyzed results when pushed, and he even let the AI write the commit message.

rss · Simon Willison · Aug 22, 21:04

**Background**: The bug was in the drm/xe driver, which handles Intel graphics in the Linux kernel. The fix, commit 818bebeb63dd, prevents the flat CCS storage from being handed out as usable VRAM, addressing memory corruption issues. Torvalds' comments were made in the commit message, which is a rare and notable acknowledgment of AI's role in kernel development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linus-Torvalds-Debug-AI">Linus Torvalds Endures A Debug Session From Hell, "Enormously Helped" By AI - Phoronix</a></li>
<li><a href="https://it.slashdot.org/story/26/08/21/1742239/linus-torvalds-endures-a-debug-session-from-hell-enormously-helped-by-ai">Linus Torvalds Endures A Debug Session From Hell, 'Enormously Helped' By AI - Slashdot</a></li>
<li><a href="https://itsfoss.com/news/torvalds-used-ai-fix-kernel-bug/">Linux Creator Linus Torvalds Just Used AI to Fix a Kernel Bug</a></li>

</ul>
</details>

**Discussion**: Community discussions, such as on Phoronix and Slashdot, generally expressed positive sentiment, with many praising Torvalds' openness to using AI and noting the practical benefits. Some commenters joked about the AI's pessimism, while others debated the implications for AI in kernel development, with a few expressing skepticism about AI's reliability in critical systems.

**Tags**: `#AI-assisted development`, `#Linux kernel`, `#debugging`, `#Linus Torvalds`

---

<a id="item-2"></a>
## [Uber Faces Nearly $1B GDPR Fine Over Automated Driver Suspensions](https://techcrunch.com/2026/08/23/uber-faces-fine-of-nearly-1b-over-automated-driver-suspensions/) ⭐️ 8.0/10

The Dutch Data Protection Authority has fined Uber €825 million (approximately $966 million) for automatically suspending driver accounts without human review between 2020 and 2022. This is the second-largest GDPR penalty ever issued, behind only Meta's €1.2 billion fine in 2023. This ruling underscores the strict limits GDPR places on fully automated decision-making that significantly impacts individuals, setting a precedent for how companies must incorporate human oversight and appeal mechanisms. It signals increased regulatory scrutiny of AI-driven systems across industries, affecting not just ride-hailing but any business using automated decisions. The fine stems from complaints by 170 French drivers who were suspended via automated systems without human review. Uber plans to appeal the decision, and the penalty is the second-largest GDPR fine to date, following Meta's €1.2 billion penalty in 2023.

rss · TechCrunch · Aug 23, 19:30

**Background**: The General Data Protection Regulation (GDPR) is a comprehensive data protection law in the EU that restricts fully automated decisions that significantly affect individuals, requiring meaningful human oversight and the right to appeal. Uber's automated driver suspension system, used between 2020 and 2022, allegedly lacked these safeguards, leading to the Dutch DPA's action. The Dutch authority has previously fined Uber €10 million for data retention issues, showing a pattern of regulatory enforcement.

<details><summary>References</summary>
<ul>
<li><a href="https://www.hokanews.com/2026/08/uber-hit-with-963-million-gdpr-fine.html">Uber Hit With $963 Million GDPR Fine Over Automated Driver Account Suspensions | Hokanews</a></li>
<li><a href="https://www.omegatechnologysolutionsgroupinc.com/blog/uber-faces-966m-gdpr-fine-for-automated-driver-suspensions-54af76">Uber faces $966M GDPR fine for automated driver suspensions · Omega</a></li>
<li><a href="https://startupfortune.com/dutch-regulator-fines-uber-nearly-1-billion-over-automated-driver-suspensions/">Dutch Regulator Fines Uber Nearly $1 Billion Over Automated Driver Suspensions - Startup Fortune</a></li>

</ul>
</details>

**Tags**: `#GDPR`, `#Uber`, `#regulatory`, `#automated systems`, `#data protection`

---

<a id="item-3"></a>
## [Frontier AI Labs Lack Public Rogue Model Containment Plans](https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/) ⭐️ 8.0/10

A new study by Guidelight AI Standards reveals that leading AI labs, including OpenAI, Anthropic, Google, Meta, and xAI, have few publicly documented plans for containing rogue AI models. The study graded these labs on their preparedness, with OpenAI scoring highest and Anthropic and Meta scoring lowest. This matters because as AI systems become more capable and occasionally exhibit unexpected or dangerous behavior, the lack of public containment plans raises serious concerns about preparedness and accountability. It highlights a critical gap in AI safety and governance that could have significant implications for public trust and regulatory oversight. Guidelight defines a containment plan as a 'pre-specified plan, triggered when the AI is detected trying to subvert control,' covering permissions to revoke, who may continue operating, constraints, and when to take the model offline. The study graded five labs, with OpenAI scoring highest and Anthropic and Meta scoring lowest, though no specific scores were disclosed.

rss · TechCrunch · Aug 22, 16:00

**Background**: Rogue AI models refer to AI systems that act contrary to their intended purpose, potentially attempting to subvert human control. Containment plans are essential for mitigating risks from such models, as they outline specific actions to limit harm. The study by Guidelight AI Standards, an organization promoting safe frontier AI development, underscores the industry's current lack of transparency in this area.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/22/frontier-ai-labs-still-wont-say-how-theyd-contain-a-rogue-model/">Frontier AI labs still won't say how they'd contain a rogue model | TechCrunch</a></li>
<li><a href="https://cryptobriefing.com/frontier-ai-labs-rogue-model-containment/">Study reveals frontier AI labs lack plans to contain rogue models</a></li>
<li><a href="https://cryptorank.io/news/feed/218e2-frontier-ai-labs-containment-plans">Frontier AI labs still won’t say how they’d contain a rogue model | AI News ai safety | CryptoRank.io</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#frontier AI`, `#rogue AI`, `#AI governance`, `#AI labs`

---

<a id="item-4"></a>
## [Anthropic's Top AI Model Lags as Cheaper Alternatives Gain Traction](https://simonwillison.net/2026/Aug/23/anthropics-best-ai-model-struggles-to-attract-users-as-cheaper-t/) ⭐️ 7.0/10

According to an FT report, Anthropic's annualized revenue reached $65 billion in July 2026, up from $47 billion in May, while OpenAI's annualized revenue surpassed $40 billion after a 35% quarterly jump. Despite releasing its flagship Opus 5 model on July 24, Anthropic's model adoption data shows it trailing behind older, cheaper models. This highlights a key competitive dynamic in the AI industry: cutting-edge performance alone may not drive adoption if pricing is prohibitive. It signals that cost-sensitive customers are favoring cheaper models, which could influence how AI companies price and position their offerings. Ramp AI Index data for July 2026 shows Opus 4.8 leading with 28.0% of Anthropic model spend, while the newly released Opus 5 accounts for only 3.5%. Anthropic expects Q3 to be profitable and has 6,000 customers spending $100,000 or more annually.

rss · Simon Willison · Aug 23, 20:24

**Background**: Annualized revenue is a metric that extrapolates current monthly revenue to a full year, providing a snapshot of a company's growth trajectory. The Ramp AI Index measures AI adoption and spending by analyzing billing data from over 70,000 companies using Ramp's corporate cards, offering insights into which AI models businesses actually use.

<details><summary>References</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/a/annualized-income.asp">Annualized Income: Definition, Formula, and Example</a></li>
<li><a href="https://ramp.com/data/ai-index">Ramp AI Index</a></li>

</ul>
</details>

**Tags**: `#AI industry`, `#Anthropic`, `#OpenAI`, `#revenue`, `#market trends`

---

<a id="item-5"></a>
## [High Cost of Fable Model Spurs Strategic AI Task Allocation](https://simonwillison.net/2026/Aug/23/drew-breunig/) ⭐️ 7.0/10

Drew Breunig highlights that the high cost of Anthropic's Fable model is pushing developers to more carefully allocate tasks between expensive and cheaper AI models, such as Opus, 5.6, K3, and GLM. This shift signals a maturing AI industry where cost optimization becomes as important as capability, affecting how developers architect AI-driven workflows and manage budgets. It reflects a broader trend of balancing performance with economic efficiency in AI adoption. Breunig notes that before Fable, it felt silly to invest heavily in coding harnesses or context strategies because new models would arrive at the same or lower price and solve most problems. However, Fable's exceptional quality but high cost made Opus and other models 'good enough' for most coding needs, prompting a more deliberate allocation of work.

rss · Simon Willison · Aug 23, 19:55

**Background**: Anthropic released Claude Fable 5 and Claude Mythos 5 in June 2026, with Fable 5 being state-of-the-art on nearly all benchmarks but priced at $10 per million input tokens and $50 per million output tokens. Opus is Anthropic's most intelligent model for agentic coding and complex reasoning, while GLM is an open-weight model series from Chinese company Z.ai. The quote reflects a practical response to the economic realities of using frontier AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_(AI)">GLM (AI) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#cost optimization`, `#Anthropic`, `#Claude`

---

<a id="item-6"></a>
## [Coding Agents: Instruct and Verify, Not Just Review](https://simonwillison.net/2026/Aug/22/more-than-just-code-review/) ⭐️ 7.0/10

Simon Willison argues that the key skill for using coding agents productively is confidently instructing them and verifying changes, which may not always require reviewing every line of code. This perspective shifts the focus from line-by-line code review to higher-level verification strategies, which is crucial as AI-assisted development becomes more prevalent. It could change how developers approach quality assurance in AI-driven workflows. Willison notes that eyeballing every line of code has never been the most effective way to validate changes. He suggests alternative verification methods, such as running tests or checking behavior, as more efficient approaches.

rss · Simon Willison · Aug 22, 15:56

**Background**: Coding agents are AI tools that autonomously write or modify code based on instructions. Agentic engineering is an emerging discipline that orchestrates such agents while humans provide oversight. Traditional code review involves manual inspection, but with AI agents, new verification paradigms are needed.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Agentic_Engineering">Agentic Engineering</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-engineering-from-code-workflows-regie-san-juan-sjyyc">Agentic Engineering : From Code to Workflows</a></li>

</ul>
</details>

**Tags**: `#coding-agents`, `#code-review`, `#AI`, `#software-engineering`, `#LLMs`

---

<a id="item-7"></a>
## [Waymo's Custom Chip Powers Robotaxi Ambitions](https://techcrunch.com/2026/08/23/techcrunch-mobility-the-custom-chip-driving-waymos-robotaxi-ambitions/) ⭐️ 7.0/10

Waymo has revealed for the first time that it designed a custom 5nm AI chip to process sensor data from cameras, lidar, and radar in its robotaxis, moving away from Intel FPGAs. The chip delivers over 1,000 TOPS of AI processing power for real-time sensor processing. This marks a significant shift in autonomous vehicle hardware, as Waymo joins Tesla in developing custom silicon to enhance performance and scalability. Custom chips can reduce costs and improve efficiency, potentially accelerating the deployment of robotaxi fleets and shaping the competitive landscape in autonomous driving. The chip is built on a 5nm process and is designed to handle raw data from multiple sensor types in real time. Waymo worked with outside chipmakers to manufacture the chip, and it is part of the company's next-generation autonomous driving system.

rss · TechCrunch · Aug 23, 16:03

**Background**: Autonomous vehicles rely on rapid processing of sensor data to make driving decisions. Previously, Waymo used Intel FPGAs for this task, but custom silicon offers better performance and energy efficiency. This trend mirrors Tesla's approach with its own AI chips, highlighting the importance of hardware specialization in the race to commercialize self-driving technology.

<details><summary>References</summary>
<ul>
<li><a href="https://autos.yahoo.com/ev-and-future-tech/articles/waymo-builds-custom-chip-robotaxi-173117486.html">Waymo builds custom chip for robotaxi fleet</a></li>
<li><a href="https://www.benzinga.com/markets/tech/26/08/61350963/waymo-unveils-first-custom-robotaxi-chip-with-more-than-1000-tops-of-ai-processing-power">Waymo Unveils First Custom Robotaxi Chip With More... - Benzinga</a></li>
<li><a href="https://www.techrepublic.com/article/news-waymo-custom-ai-chips-robotaxis/">Alphabet's Waymo Unveils Custom Silicon to Power Its Next-Gen...</a></li>

</ul>
</details>

**Tags**: `#autonomous vehicles`, `#Waymo`, `#custom silicon`, `#robotaxi`, `#AI hardware`

---

<a id="item-8"></a>
## [AI Training on Copyrighted Books: Legal Gray Area](https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/) ⭐️ 7.0/10

The article discusses the ongoing legal and ethical debate over whether training AI models on copyrighted books without authors' consent is legal, highlighting the complexity and lack of clear legal precedent. This issue affects authors, AI companies, and the broader creative industry, as the outcome of such legal battles could set precedents for how AI models are trained and whether creators are compensated. It also influences public trust and regulatory approaches to AI development. The article notes that fair use is a central legal concept, but its application to AI training remains uncertain. Recent cases, such as Bartz v. Anthropic, distinguish between fair use for training and infringement from retaining pirated copies, indicating that the legality may hinge on specific circumstances.

rss · TechCrunch · Aug 23, 15:00

**Background**: AI models, especially large language models (LLMs), are trained on vast amounts of text data, often scraped from the internet or digitized books. Copyright law, particularly the fair use doctrine in the US, allows limited use of copyrighted material without permission, but whether AI training qualifies as transformative fair use is a contentious issue. The lack of specific legislation for text and data mining adds to the uncertainty.

<details><summary>References</summary>
<ul>
<li><a href="https://distillation.technology/learn/is-ai-training-fair-use">Is AI Training Fair Use? What Bartz v. Anthropic Actually</a></li>
<li><a href="https://www.linkedin.com/pulse/legal-uncertainty-over-ai-training-copyrighted-content-savneet-singh-fj2me">Legal Uncertainty Over AI Training on Copyrighted Content and its...</a></li>
<li><a href="https://www.linkedin.com/pulse/judge-alsup-gets-right-ai-training-fair-use-sound-legal-tredennick-rt1fc">Judge Alsup Gets It Right: AI Training as Fair Use Represents Sound...</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#copyright`, `#legal`, `#machine learning`, `#publishing`

---

<a id="item-9"></a>
## [DeepMind Alumni's Inherent Faraday AI Outperforms Anthropic and OpenAI in Research Replication](https://techcrunch.com/2026/08/22/inherent-founded-by-deepmind-alumni-says-its-ai-teammate-just-outperformed-anthropic-and-openai-at-replicating-research/) ⭐️ 7.0/10

Inherent, a London-based AI lab founded by DeepMind alumni, has released Faraday, an AI agent that reportedly outperforms Anthropic's Claude Opus 4.8 and OpenAI's models at replicating scientific papers. The company claims Faraday achieved this using a fraction of the size of larger models. This development could accelerate scientific discovery by automating the replication of research, a critical step for validating findings. It also highlights the potential of smaller, specialized AI agents to compete with industry giants, potentially reshaping the competitive landscape in AI research. Faraday's performance is attributed partly to its use of reinforcement learning, a different training approach from larger models. Inherent's longer-term goal is to develop an AI scientist agent that can operate across scientific fields, rather than being limited to a single benchmark or discipline.

rss · TechCrunch · Aug 22, 19:00

**Background**: Replicating scientific papers involves reproducing experiments, data, and findings from existing research, which is essential for verifying claims and building on prior work. AI agents like Faraday are designed to automate this process, potentially reducing the time and effort required for manual replication. The claim is notable because it comes from a small startup challenging much larger, well-funded labs like Anthropic and OpenAI.

<details><summary>References</summary>
<ul>
<li><a href="https://vmtech.rs/en/instagram-insights/inherent-faraday-research-agent">Inherent Faraday AI research replication — VMTech</a></li>
<li><a href="https://chang.aevumnews.com/en/inherent-deepmind-alumni-s-ai-teammate-outperforms-giants-in-research-replication">Inherent : DeepMind Alumni 's AI 'Teammate' Outperforms Giants in.....</a></li>
<li><a href="https://creati.ai/ai-news/2026-08-22/inherent-says-its-faraday-ai-agent-beat-anthropic-and-openai-at-replicating-research/">Inherent says its Faraday AI agent beat Anthropic and OpenAI at...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#research`, `#DeepMind`, `#scientific discovery`, `#agent`

---

<a id="item-10"></a>
## [OpenAI Reverses Stance, Urges California to Strengthen AI Safety Bill SB 53](https://techcrunch.com/2026/08/22/openai-says-california-should-strengthen-its-ai-safety-bill/) ⭐️ 7.0/10

OpenAI has reversed its previous opposition and is now calling on California lawmakers to strengthen SB 53, an AI safety bill. The company specifically urges amendments that mandate continuous monitoring and heightened cybersecurity during AI model training. This shift signals a significant recalibration in OpenAI's approach to AI regulation, acknowledging that some form of binding oversight may be inevitable. It could influence the passage of SB 53 and set a precedent for AI governance in the U.S., especially given California's role as Silicon Valley's home state. SB 53 is sponsored by Senator Scott Wiener and co-sponsored by Encode AI, Economic Security Action California, and the Secure AI Project. Governor Gavin Newsom signed the bill into law, requiring AI companies to disclose safety information about large-scale frontier models. OpenAI's proposed amendments focus on continuous monitoring and heightened cybersecurity during training.

rss · TechCrunch · Aug 22, 16:30

**Background**: California has been at the forefront of AI regulation efforts. Last year, Governor Newsom vetoed a broader AI safety bill, SB 1047, after intense lobbying from AI companies. SB 53 represents a more targeted approach, focusing on disclosure requirements for frontier models. OpenAI's reversal reflects growing concerns about advanced AI risks and a need for regulatory clarity.

<details><summary>References</summary>
<ul>
<li><a href="https://sd11.senate.ca.gov/news/senator-wieners-landmark-responsible-ai-innovation-bill-advances-final-vote">Senator Wiener’s Landmark Responsible AI Innovation Bill Advances...</a></li>
<li><a href="https://businessnoon.com/california-signs-landmark-ai-safety-bill-sb-53/">California ’s Bold AI Safety Bill SB 53 Changes the Game</a></li>
<li><a href="https://www.kron4.com/hill-politics/newsom-signs-first-in-the-nation-ai-safety-disclosures-law/433/">Gavin Newsom signs SB 53 , enacting California AI safety bill</a></li>
<li><a href="https://semasocial.com/blog/openai-is-calling-for-california-to-strengthen-sb-53-an-ai-safety-bill-that-the-company-previously-opposed">OpenAI Now Supports California AI Safety Bill SB 53 - semasocial.com</a></li>
<li><a href="https://azat.tv/en/openai-california-sb53-ai-safety-law-amendments/">OpenAI Urges California to Strengthen Frontier Model Safety Rules...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#OpenAI`, `#regulation`, `#California`, `#policy`

---

<a id="item-11"></a>
## [US Battery Startups Find Defense Lifeline in $500M DOE Grants](https://techcrunch.com/2026/08/22/us-battery-startups-have-found-a-lifeline-in-defense/) ⭐️ 7.0/10

U.S. battery startups received $500 million in grants from the Department of Energy, providing a financial lifeline after EV incentives were slashed. This funding is part of a strategic pivot toward defense contracts for drones, bases, and next-generation vehicles. This development is significant because it helps sustain the U.S. battery industry amid a collapse in automotive demand, potentially reshaping the sector's focus toward national security applications. It also highlights a broader trend of government funding being redirected to defense-related technologies. The grants support startups working on solid-state batteries and thermal batteries for munitions and hypersonic systems, areas where traditional lithium-ion batteries fall short. Additionally, some startups are attracting investors like ADS Ventures, affiliated with defense supplier ADS, indicating growing ties between the battery and defense sectors.

rss · TechCrunch · Aug 22, 15:20

**Background**: In early 2026, Congress cut EV tax credits and consumer incentives, leading to a collapse in automotive demand for batteries. This forced U.S. battery startups to seek alternative markets, and defense contracts emerged as a stable source of revenue. The DOE grants are part of a broader effort to bolster domestic battery manufacturing and national security.

<details><summary>References</summary>
<ul>
<li><a href="https://www.androguider.com/2026/08/defense-lifeline-how-500m-in-doe-grants.html">Defense Lifeline: How $500M in DOE Grants Are Saving US Battery ...</a></li>
<li><a href="https://www.techbuzz.ai/articles/us-battery-startups-score-500m-defense-lifeline-after-ev-cuts">US Battery Startups Score $500M Defense Lifeline... | The Tech Buzz</a></li>
<li><a href="https://mezha.net/eng/bukvy/b820c632_us_battery_startups/">US Battery Startups Turn to Defense After EV Incentives... - #Mezha</a></li>

</ul>
</details>

**Tags**: `#batteries`, `#energy storage`, `#defense`, `#government funding`, `#startups`

---

<a id="item-12"></a>
## [Michael Polansky trains AI on living human skin for skincare discovery](https://techcrunch.com/2026/08/21/michael-polansky-is-training-an-ai-model-on-skin-thats-still-alive/) ⭐️ 7.0/10

Michael Polansky's AI-driven startup has been quietly developing a technology that keeps living human skin tissue alive for weeks outside the body, and is now going public about it. The startup uses this living tissue to train AI models to discover new skincare compounds. This represents a novel intersection of AI and biotechnology, potentially accelerating skincare and drug discovery by providing a more physiologically relevant testing platform than traditional methods. It could impact the cosmetics and pharmaceutical industries by reducing reliance on animal testing and improving the efficacy of new compounds. The technology involves ex vivo culture of human skin tissue, which is a technique that maintains tissue viability outside the body for extended periods. The startup's approach likely uses air-liquid interface culture or similar methods to keep the tissue alive, and then applies AI to analyze responses to potential compounds.

rss · TechCrunch · Aug 22, 01:31

**Background**: Ex vivo human skin culture is a well-established technique in biomedical research, where skin samples are kept alive in the lab to study skin biology and test treatments. AI-driven drug discovery is a growing field that uses machine learning to identify promising compounds, but combining it with living human tissue is a relatively new approach. This could offer more accurate predictions of how compounds will behave in the human body.

<details><summary>References</summary>
<ul>
<li><a href="https://www.academia.edu/92848865/Dynamic_Physiological_Culture_of_Ex_Vivo_Human_Tissue_A_Systematic_Review">(PDF) Dynamic Physiological Culture of Ex Vivo Human Tissue ...</a></li>
<li><a href="https://www.researchgate.net/figure/Ex-Vivo-Culture-Platforms-for-healthy-and-HS-skin-Schematics-of-three-ex-vivo-culture_fig2_355224937">Ex Vivo Culture Platforms for healthy and HS skin . Schematics of...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#biotech`, `#skincare`, `#startup`, `#drug discovery`

---