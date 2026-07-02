---
layout: default
title: "Horizon Summary: 2026-07-02 (EN)"
date: 2026-07-02
lang: en
---

> From 80 items, 15 important content pieces were selected

---

1. [First Synthetic Cell That Grows and Divides Created](#item-1) ⭐️ 9.0/10
2. [US Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](#item-2) ⭐️ 8.0/10
3. [Claude Sonnet 5 Released with Near-Opus Performance](#item-3) ⭐️ 8.0/10
4. [shot-scraper video lets agents record demos](#item-4) ⭐️ 8.0/10
5. [Apple Hide My Email bug exposes real addresses, researcher says](#item-5) ⭐️ 8.0/10
6. [Together AI Raises $800M, Valuation Hits $8.3B](#item-6) ⭐️ 8.0/10
7. [Cloudflare gives AI firms deadline to separate crawlers or face blocking](#item-7) ⭐️ 8.0/10
8. [Sony to Stop Producing Physical PlayStation Discs by 2028](#item-8) ⭐️ 8.0/10
9. [Anthropic Python SDK v0.115.0 Adds Managed Agents Features](#item-9) ⭐️ 7.0/10
10. [ChatGPT Adoption Expands Globally](#item-10) ⭐️ 7.0/10
11. [Bending Spoons IPO surges 40%, defying SaaS slump](#item-11) ⭐️ 7.0/10
12. [Honda Pivots to Data Center Battery Production](#item-12) ⭐️ 7.0/10
13. [Venice AI Hits Unicorn Status with $65M Series A](#item-13) ⭐️ 7.0/10
14. [Meta Plans Cloud Business to Sell Excess AI Compute](#item-14) ⭐️ 7.0/10
15. [Brain2Qwerty v2 Decodes Sentences from Non-Invasive Brain Signals](#item-15) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [First Synthetic Cell That Grows and Divides Created](https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/) ⭐️ 9.0/10

Researchers at Biotic, led by Kate Adamala, have created SpudCell, the first fully synthetic cell built from scratch that can grow, replicate its DNA, and divide into daughter cells. This breakthrough overcomes a major hurdle in synthetic biology—achieving cell division without a cytoskeleton—and could lead to programmable cells for medicine, materials, and environmental applications. SpudCell's 90 kbp genome is split across seven separate DNA plasmids, smaller than the theoretical minimal genome of 113 kbp, and it demonstrates selection and competition in a fully synthetic chemical system.

hackernews · defrost · Jul 1, 14:20 · [Discussion](https://news.ycombinator.com/item?id=48747304)

**Background**: Synthetic biology aims to build artificial cells from nonliving components. Previous efforts created minimal cells with synthetic genomes but failed to achieve proper division. SpudCell bypasses the need for a cytoskeleton by using a different mechanism to split.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/science/2026/jul/01/synthetic-life-lab-made-dna-spudcells-scientists">‘Beautiful blobs’: synthetic life a step closer as scientists make cells using lab-made DNA | Science | The Guardian</a></li>
<li><a href="https://www.nytimes.com/2026/07/01/science/spud-cell-what-to-know.html">SpudCell: Scientists Made a Cell With Most of the Hallmarks of Life. Here’s What to Know. - The New York Times</a></li>
<li><a href="https://biotic.org/research/spudcell/">Biotic | SpudCell</a></li>

</ul>
</details>

**Discussion**: Comments highlight controversy over the research's publication process, with some peers criticizing the embargo and PR approach. Others express concern about potential risks of synthetic organisms, while some admire the novel approach to cell division.

**Tags**: `#synthetic biology`, `#cell division`, `#groundbreaking research`, `#biotechnology`

---

<a id="item-2"></a>
## [US Lifts Export Controls on Anthropic's Claude Fable 5 and Mythos 5](https://simonwillison.net/2026/Jun/30/anthropic/#atom-everything) ⭐️ 8.0/10

Anthropic announced that the US Department of Commerce has lifted export controls on its advanced AI models Claude Fable 5 and Mythos 5, with access restoration to begin the following day. This signals a shift in US AI export policy, potentially enabling broader international access to cutting-edge models and influencing the global AI landscape. Claude Fable 5 and Mythos 5 are advanced models designed for cybersecurity and other high-stakes domains; they were previously restricted due to safety and misuse concerns.

rss · Simon Willison · Jun 30, 23:58

**Background**: Export controls on AI models were introduced by the US government to prevent sensitive technology from reaching adversaries. Anthropic's Claude Mythos series, including Fable 5, had been under such restrictions due to its potential for misuse in cyber operations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#anthropic`, `#claude`, `#ai`, `#export-controls`, `#generative-ai`

---

<a id="item-3"></a>
## [Claude Sonnet 5 Released with Near-Opus Performance](https://simonwillison.net/2026/Jun/30/claude-sonnet-5/#atom-everything) ⭐️ 8.0/10

Anthropic released Claude Sonnet 5 on June 30, 2026, claiming its performance is close to Opus 4.8 at lower prices. The model features a new tokenizer that produces about 30% more tokens for the same text, effectively raising costs despite unchanged per-token pricing. Sonnet 5 brings near-flagship performance to a more affordable tier, enabling broader adoption for agentic tasks. Its release also highlights Anthropic's navigation of US government safety regulations, as the model's cyber capabilities are deliberately limited to avoid regulatory blocks. The model has a 1 million token context window and 128,000 maximum output tokens, but sampling parameters temperature, top_p, and top_k are no longer supported. Adaptive thinking is enabled by default unless explicitly disabled. The new tokenizer increases token count by roughly 30% for English, 33% for Spanish, and 1% for Simplified Chinese.

rss · Simon Willison · Jun 30, 21:23

**Background**: Claude is a series of large language models by Anthropic, typically released in three sizes: Haiku, Sonnet, and Opus. Sonnet models are the mid-tier, balancing capability and cost. Opus 4.8 is Anthropic's previous flagship, while Mythos 5 is a more capable model restricted to vetted partners due to safety concerns. The US government has scrutinized Anthropic's models for potential misuse, influencing release decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5">What's new in Claude Sonnet 5 - Claude Platform Docs</a></li>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Sonnet">Claude Sonnet</a></li>

</ul>
</details>

**Discussion**: Hacker News comments (via the provided link) likely discuss the tokenizer change and effective price increase, with some users noting the irony of unchanged per-token pricing but higher actual costs. Others may compare Sonnet 5's performance to Opus 4.8 and question the removal of sampling parameters.

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#model release`

---

<a id="item-4"></a>
## [shot-scraper video lets agents record demos](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison released shot-scraper 1.10 with a new `video` command that accepts a `storyboard.yml` file and uses Playwright to record a video of a web application routine. This tool addresses the challenge of having coding agents automatically produce video demos of their work, making it easier to verify and showcase agent-generated changes. The `storyboard.yml` file defines scenes with actions like clicks and pauses, and supports features like custom viewport, cursor visibility, and JavaScript injection for mocking clipboard APIs.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a command-line tool for taking screenshots of web pages, built on Playwright. The new video command extends it to record full browser sessions as videos, enabling automated demo creation for AI agents.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot ...</a></li>
<li><a href="https://letsdatascience.com/news/shot-scraper-launches-video-command-in-110-07962b66">shot-scraper launches video command in 1.10 | Let's Data Science</a></li>
<li><a href="https://www.remio.ai/post/shot-scraper-video-lets-ai-agents-record-demo-videos">Shot-scraper Video Lets AI Agents Record Demo Videos</a></li>

</ul>
</details>

**Tags**: `#developer-tools`, `#AI-agents`, `#testing`, `#automation`, `#video-recording`

---

<a id="item-5"></a>
## [Apple Hide My Email bug exposes real addresses, researcher says](https://techcrunch.com/2026/07/01/apples-hide-my-email-feature-has-a-bug-thats-been-exposing-real-email-addresses-researcher-claims/) ⭐️ 8.0/10

A security researcher claims that Apple's Hide My Email feature has a bug that allows attackers to discover the real email address behind any generated alias, with tests showing 100% of addresses were vulnerable. This bug undermines the core privacy promise of Hide My Email, potentially exposing millions of iCloud+ users to spam, phishing, and identity attacks, and eroding trust in Apple's privacy features. The researcher reported the bug to Apple over a year ago, but it remains unpatched. The vulnerability reportedly works by exploiting how the email forwarding system handles certain headers or metadata.

rss · TechCrunch · Jul 1, 19:18

**Background**: Hide My Email is a privacy feature included with Apple's iCloud+ subscription that lets users generate unique, random email addresses that forward messages to their real inbox, so they don't have to share their actual email. It is commonly used with Sign in with Apple and in Safari forms.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/07/01/apple-hide-my-email-bug-seemingly-allows-100-of-real-email-addresses-to-be-discovered/">Apple Hide My Email bug seemingly allows 100% of real email ...</a></li>
<li><a href="https://www.macrumors.com/2026/07/01/hide-my-email-vulnerability-exposes-real-addresses/">Apple Hide My Email Vulnerability Exposes Real Email ...</a></li>
<li><a href="https://cybersecuritynews.com/apple-hide-my-email-vulnerability/">Apple ‘Hide My Email’ Vulnerability Exposes Users’ Real Email ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#privacy`, `#Apple`, `#bug`, `#email`

---

<a id="item-6"></a>
## [Together AI Raises $800M, Valuation Hits $8.3B](https://techcrunch.com/2026/07/01/neocloud-together-ai-raises-800m-leaps-to-8-3b-valuation/) ⭐️ 8.0/10

Together AI, a neocloud provider specializing in open-source AI models, raised $800 million in a funding round that values the company at $8.3 billion, up from $3.3 billion in early 2025. This massive funding round underscores the growing demand for specialized AI infrastructure, particularly for open-source models, and positions Together AI as a major player in the neocloud market. The company last raised at a $3.3 billion valuation in early 2025, meaning its valuation more than doubled in about 18 months. Together AI counts Zoom and Salesforce among its customers.

rss · TechCrunch · Jul 1, 18:29

**Background**: A neocloud is a specialized cloud computing provider designed from the ground up to handle the extreme demands of AI and high-performance computing, often offering GPU as a Service (GPUaaS). Together AI provides a full-stack platform for production AI, including training, fine-tuning, and running models, with a focus on open-source generative AI.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.equinix.com/blog/2025/10/14/what-is-a-neocloud/">What Is a Neocloud? - Interconnections - The Equinix Blog</a></li>
<li><a href="https://www.together.ai/about-us">About Us | Together AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#neocloud`, `#open-source`, `#valuation`

---

<a id="item-7"></a>
## [Cloudflare gives AI firms deadline to separate crawlers or face blocking](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/) ⭐️ 8.0/10

Cloudflare announced a new policy requiring AI companies to separate web crawlers used for search indexing from those used for AI training and agents by September 15, 2026, or risk being blocked by default on publisher sites using Cloudflare's services. This policy shift from a major internet infrastructure provider directly addresses the contentious issue of unpaid web scraping for AI training, potentially reshaping how AI companies access publisher content and setting a precedent for content compensation in the AI era. The deadline is September 15, 2026, after which AI crawlers not properly separated may be blocked by default on Cloudflare-protected publisher sites. Cloudflare's AI Crawl Control dashboard allows publishers to monitor crawler activity and set granular allow or block rules for individual crawlers.

rss · TechCrunch · Jul 1, 17:48

**Background**: Web crawlers are automated programs that browse the internet to collect data. Search crawlers (e.g., Googlebot) index content for search engines, while AI training crawlers scrape data to train large language models. Publishers have increasingly objected to AI companies using their content without compensation, leading to blocking efforts and legal disputes. Cloudflare, which protects about 20% of all internet traffic, is leveraging its position to enforce this separation.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/ai-crawl-control/">Overview · Cloudflare AI Crawl Control docs</a></li>
<li><a href="https://developers.cloudflare.com/ai-crawl-control/features/manage-ai-crawlers/">Manage AI crawlers · Cloudflare AI Crawl Control docs</a></li>
<li><a href="https://www.cloudflare.com/ai-crawl-control/">AI Crawl Control | Cloudflare</a></li>

</ul>
</details>

**Tags**: `#AI`, `#web crawling`, `#content rights`, `#Cloudflare`, `#policy`

---

<a id="item-8"></a>
## [Sony to Stop Producing Physical PlayStation Discs by 2028](https://www.theverge.com/games/960212/sony-playstation-killing-discs-digital-preservation) ⭐️ 8.0/10

Sony announced it will cease production of physical PlayStation discs starting January 2028, making new PS5 games available only through digital downloads. This shift threatens game preservation and consumer ownership, as digital games are tied to DRM and online services that can be revoked, unlike physical discs. The move aligns with Sony's broader push toward digital-only distribution, but raises concerns about long-term access to games if servers shut down or licenses expire.

rss · The Verge · Jul 1, 15:00

**Background**: Video game preservation involves archiving games in physical or digital forms to prevent loss due to hardware decay or service closures. Physical discs allow ownership independent of online services, while digital games often require online authentication and can be delisted. Sony's decision mirrors industry trends but intensifies debates over digital rights and preservation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Video_game_preservation">Video game preservation - Wikipedia</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2p3OEozX0VCRlpGaV9DRDYxU3J5Z0FQAQ?hl=en-CA&gl=CA&ceid=CA:en">Google News - News about PlayStation • DRM • Sony - Overview</a></li>

</ul>
</details>

**Tags**: `#gaming`, `#digital preservation`, `#Sony`, `#PlayStation`, `#DRM`

---

<a id="item-9"></a>
## [Anthropic Python SDK v0.115.0 Adds Managed Agents Features](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.115.0) ⭐️ 7.0/10

Anthropic released version 0.115.0 of its Python SDK on June 30, 2026, adding support for Managed Agents event delta streaming, agent overrides, reverse pagination, vault credential injection scoping, and webhook events for agents and deployments. These features enable developers to build more interactive and secure agent-based applications, such as streaming in-progress messages, overriding agent configurations per session, and receiving real-time webhook notifications without polling. The event delta streaming uses a different wire format from standard streaming messages, with only event_start and event_delta events and no per-content-block boundaries. Vault credential injection scoping allows controlling whether credentials are injected into headers or body of outbound requests.

github · stainless-app[bot] · Jun 30, 19:47

**Background**: Managed Agents are a feature of Anthropic's Claude platform that allows developers to create and manage autonomous AI agents. Event delta streaming enables real-time updates of agent message generation, while webhooks provide asynchronous notifications for agent lifecycle events. Vault credential injection allows agents to securely use stored secrets from a credential vault.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/managed-agents/events-and-streaming">Session event stream - Claude Platform Docs</a></li>
<li><a href="https://chatforest.com/builders-log/claude-managed-agents-june-30-event-deltas-session-overrides-vault-webhooks-builder-guide/">Claude Managed Agents June 30: Event Deltas, Session ...</a></li>
<li><a href="https://platform.claude.com/docs/en/managed-agents/vaults">Authenticate with vaults - Claude Platform Docs</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#SDK`, `#Python`, `#AI`, `#API`

---

<a id="item-10"></a>
## [ChatGPT Adoption Expands Globally](https://openai.com/index/how-chatgpt-adoption-has-expanded) ⭐️ 7.0/10

OpenAI's new Signals data reveals that ChatGPT adoption is growing globally, with users increasing usage, exploring more capabilities, and driving growth across regions and languages. This official data provides valuable insights into how AI tools like ChatGPT are being integrated into daily workflows worldwide, highlighting trends that can guide developers and businesses in AI adoption strategies. The data comes from OpenAI Signals, a new analytics initiative, and shows increased usage and capability exploration across different regions and languages, though specific numbers or breakdowns are not provided in the summary.

rss · OpenAI Blog · Jun 30, 09:00

**Background**: ChatGPT is a large language model chatbot developed by OpenAI, launched in November 2022. Its adoption has been rapid, with users ranging from individuals to enterprises using it for tasks like content generation, coding, and customer support. OpenAI Signals is a new data platform that tracks usage trends.

**Tags**: `#ChatGPT`, `#AI adoption`, `#OpenAI`, `#data analysis`

---

<a id="item-11"></a>
## [Bending Spoons IPO surges 40%, defying SaaS slump](https://techcrunch.com/2026/07/01/bending-spoons-defies-saas-slump-surges-40-on-first-day-of-trading/) ⭐️ 7.0/10

Bending Spoons, an Italian tech conglomerate, surged 40% on its first day of trading, defying the broader SaaS downturn. The company went public at a valuation of $19 billion. This IPO success signals that investors still value companies with proven strategies for revitalizing legacy tech brands, even as the SaaS sector struggles with slowing growth. It could encourage more M&A activity targeting aging internet properties. Bending Spoons has acquired over 50 brands including AOL, Evernote, Vimeo, and Eventbrite, focusing on increasing revenue and cutting costs. The company's CEO is now worth $2.4 billion after the IPO.

rss · TechCrunch · Jul 1, 22:47

**Background**: The SaaS market has been in a downturn since early 2025, with Q1 2025 showing the worst performance in years and revenue growth declining to 12.2% by Q4 2025. Bending Spoons, founded in 2013, acquires struggling or mature tech products and revamps them for profitability, a strategy that contrasts with the typical venture-backed growth model.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bending_Spoons">Bending Spoons - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2026/06/30/technology/bending-spoons-ipo-aol-vimeo-eventbrite.html">Bending Spoons, Owner of AOL and Other Old Internet Brands, Is Going Public - The New York Times</a></li>
<li><a href="https://www.forbes.com/sites/iainmartin/2026/07/01/how-bending-spoons-built-a-184-billion-empire-by-buying-internet-has-beens-like-aol/">Italian CEO Of Bending Spoons, Owner Of AOL And Evernote, Is Worth $2.4 Billion After IPO</a></li>

</ul>
</details>

**Tags**: `#SaaS`, `#IPO`, `#Tech M&A`, `#Business Strategy`

---

<a id="item-12"></a>
## [Honda Pivots to Data Center Battery Production](https://techcrunch.com/2026/07/01/even-honda-is-pivoting-to-data-centers/) ⭐️ 7.0/10

Honda has begun producing batteries for energy storage systems used in data centers, marking a strategic shift from its traditional automotive focus. The batteries are being manufactured at its Ohio facility in partnership with LG Energy Solution. This move highlights the growing convergence between the automotive and data center industries, as automakers leverage their battery expertise to meet surging demand for energy storage in AI data centers. It also signals a new revenue stream for Honda amid slowing EV adoption. The batteries are designed for Battery Energy Storage Systems (BESS) that store solar power and release it during peak demand, ensuring reliable power for data centers. Honda's Ohio plant was originally built for EV battery production but is now repurposed for stationary storage.

rss · TechCrunch · Jul 1, 17:13

**Background**: Data centers, especially those powering AI workloads, consume enormous amounts of electricity and require uninterrupted power. Battery Energy Storage Systems (BESS) help stabilize the grid, reduce energy costs, and provide backup power. Automakers like Honda have deep expertise in battery manufacturing, making them natural players in the energy storage market.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/01/even-honda-is-pivoting-to-data-centers/">Even Honda is pivoting to data centers | TechCrunch</a></li>
<li><a href="https://www.autoblog.com/news/honda-found-a-new-use-for-its-ev-battery-plant-ai-data-centers">Honda Found A New Use For Its EV Battery Plant: AI Data Centers - Autoblog</a></li>
<li><a href="https://www.gurufocus.com/news/8935621/honda-finds-an-ai-use-for-ev-batteries">Honda Finds an AI Use for EV Batteries</a></li>

</ul>
</details>

**Tags**: `#energy storage`, `#data centers`, `#Honda`, `#batteries`, `#industry pivot`

---

<a id="item-13"></a>
## [Venice AI Hits Unicorn Status with $65M Series A](https://techcrunch.com/2026/07/01/venice-ai-becomes-a-unicorn-with-65m-series-a-as-its-privacy-first-ai-platform-takes-off/) ⭐️ 7.0/10

Venice AI, a privacy-first AI platform, raised $65 million in Series A funding, achieving unicorn status while already profitable with over $70 million in annualized revenue. This milestone is notable because Venice AI reached unicorn status and profitability at the Series A stage, a rare feat in the AI startup landscape, highlighting strong market demand for privacy-focused AI solutions. The company was founded by Erik Voorhees, a cryptocurrency entrepreneur who also founded ShapeShift. Venice AI uses open-source models and does not store user data on servers, relying on local storage and end-to-end encryption.

rss · TechCrunch · Jul 1, 14:25

**Background**: Venice AI is a decentralized, privacy-focused generative AI platform launched in 2024. Unlike mainstream AI platforms, it offers uncensored interactions and ensures user confidentiality by processing data locally. The platform supports text, image, and code generation.

<details><summary>References</summary>
<ul>
<li><a href="https://navtools.ai/tool/venice-ai">Venice AI: Private, Uncensored AI for Text & Images</a></li>
<li><a href="https://en.wikipedia.org/wiki/Erik_Voorhees">Erik Voorhees</a></li>

</ul>
</details>

**Tags**: `#AI`, `#startup funding`, `#privacy`, `#unicorn`

---

<a id="item-14"></a>
## [Meta Plans Cloud Business to Sell Excess AI Compute](https://techcrunch.com/2026/07/01/meta-like-spacex-looks-to-turn-excess-ai-compute-into-cash/) ⭐️ 7.0/10

Meta is developing plans for a cloud infrastructure business that will sell access to AI compute power and models, directly competing with AWS, Google Cloud, and Azure. This move could reshape the cloud AI market by introducing a major new competitor with massive existing infrastructure, potentially lowering costs and increasing options for AI compute customers. The plan is still in development, and Meta has not publicly confirmed details. The company has invested $182.9 billion in infrastructure, and selling excess capacity could help offset those costs.

rss · TechCrunch · Jul 1, 13:43

**Background**: Meta has built massive AI compute infrastructure to support its own products like Facebook and Instagram. Similar to SpaceX selling excess satellite capacity, Meta now aims to monetize its unused compute power by offering cloud services to external customers.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/07/01/meta-like-spacex-looks-to-turn-excess-ai-compute-into-cash/">Meta, like SpaceX, looks to turn excess AI compute into cash | TechCrunch</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-07-01/meta-is-building-a-cloud-business-to-sell-excess-ai-compute">Meta Is Planning a Cloud Business to Sell AI Computing Power - Bloomberg</a></li>
<li><a href="https://qz.com/meta-cloud-business-ai-computing-power-070126">Meta building cloud business to sell excess AI computing capacity</a></li>

</ul>
</details>

**Tags**: `#Meta`, `#cloud computing`, `#AI`, `#competition`, `#infrastructure`

---

<a id="item-15"></a>
## [Brain2Qwerty v2 Decodes Sentences from Non-Invasive Brain Signals](https://www.producthunt.com/products/meta) ⭐️ 7.0/10

Brain2Qwerty v2 is a non-invasive brain-computer interface that can decode full sentences directly from brain signals, building on the previous version that decoded individual words. This advancement could enable communication for people with severe motor disabilities without requiring surgery, and it opens new possibilities for human-computer interaction. The system uses electroencephalography (EEG) and magnetoencephalography (MEG) signals combined with deep learning models to decode speech perception and production.

rss · Product Hunt (AI应用) · Jun 30, 04:22

**Background**: Brain-computer interfaces (BCIs) traditionally require invasive implants to achieve high decoding accuracy. Non-invasive methods like EEG and MEG are safer but historically less precise. Recent advances in deep learning, particularly convolutional neural networks and transformers, have significantly improved non-invasive decoding performance.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/blog/brain2qwerty-brain-ai-human-communication/">From Brain Waves to Words: Brain2Qwerty Offers a New Path to Communication Without Surgery</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/brain2qwerty-a-system-that-decodes-thoughts-using-brain-waves-without-surgery">Brain2Qwerty, A System That Decodes Thoughts Using Brain Waves Without Surgery</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-65499-0">Towards decoding individual words from non-invasive brain recordings | Nature Communications</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#AI`, `#neuroscience`, `#non-invasive`

---