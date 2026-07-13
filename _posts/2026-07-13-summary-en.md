---
layout: default
title: "Horizon Summary: 2026-07-13 (EN)"
date: 2026-07-13
lang: en
---

> From 35 items, 4 important content pieces were selected

---

1. [Zer0Fit: MCP Server for Google's TabFM & TimesFM](#item-1) ⭐️ 8.0/10
2. [Claude Code vs OpenCode: Token Overhead Comparison](#item-2) ⭐️ 7.0/10
3. [CISA built incident playbook during real incident](#item-3) ⭐️ 7.0/10
4. [Apple's failed car project birthed powerful AI chips](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Zer0Fit: MCP Server for Google's TabFM & TimesFM](https://www.reddit.com/r/MachineLearning/comments/1uue8cc/zer0fit_i_took_googles_new_tabfm_timesfm_ml/) ⭐️ 8.0/10

A graduate student created Zer0Fit, an MCP server that wraps Google's new TabFM and TimesFM foundation models, enabling zero-shot forecasting, classification, and regression from a chat interface. The server runs locally in a Docker container and requires 16GB VRAM. This project makes cutting-edge zero-shot ML models accessible to non-experts via a simple chat interface, lowering the barrier to using foundation models for tabular and time-series tasks. It demonstrates how MCP can bridge LLMs and traditional ML models. Zer0Fit achieved 94.7% accuracy on the Iris dataset and an R² of 0.91 on California housing regression, all without any fine-tuning. It supports CSV input (with XLS, XLSX, JSON, JSONL coming soon) and dynamically loads/unloads models with a 5-minute TTL to free VRAM.

reddit · r/MachineLearning · /u/Porespellar · Jul 12, 12:32

**Background**: TabFM and TimesFM are foundation models from Google Research for tabular data and time-series forecasting, respectively. They enable zero-shot inference, meaning they can make predictions on new datasets without task-specific training. MCP (Model Context Protocol) is a standard for connecting AI models to tools and data sources, often used with LLMs like those in Open WebUI or Claude Code.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/">Introducing TabFM : A zero-shot foundation model for tabular data</a></li>
<li><a href="https://github.com/google-research/timesfm">google-research/ timesfm : TimesFM ( Time Series Foundation Model )...</a></li>
<li><a href="https://machinelearningmastery.com/building-a-simple-mcp-server-in-python/">Building a Simple MCP Server in Python - Machine Learning Mastery</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#foundation models`, `#MCP server`, `#zero-shot`, `#time series`

---

<a id="item-2"></a>
## [Claude Code vs OpenCode: Token Overhead Comparison](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 7.0/10

An empirical study found that Claude Code sends approximately 33,000 tokens before reading the user's prompt, while OpenCode sends only about 7,000 tokens, revealing significant token inefficiency in Claude Code's cache strategy and harness overhead. This token waste directly increases costs for users of Claude Code, especially for large or complex tasks, and raises questions about the economic incentives of AI coding agent providers. The study logged all requests between the coding tools and Anthropic's endpoint, capturing usage blocks for comparison. The authors note that sub-agents and tool call overhead further amplify token consumption.

hackernews · systima · Jul 12, 18:25 · [Discussion](https://news.ycombinator.com/item?id=48883275)

**Background**: AI coding agents like Claude Code and OpenCode use large language models to assist with software development tasks. They send system prompts, tool definitions, and conversation history with each request, which contributes to token overhead. Efficient token usage is critical for cost management in production environments.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/drona23/claude-token-efficient">GitHub - drona23/claude-token-efficient: One CLAUDE.md file. Keeps Claude responses terse. Reduces output verbosity on heavy workflows. Drop-in, no code changes. · GitHub</a></li>
<li><a href="https://buildtolaunch.substack.com/p/claude-code-token-optimization">Claude Code Token Optimization: 19 Changes to Cut Costs (2026)</a></li>
<li><a href="https://www.firecrawl.dev/blog/claude-code-token-efficiency">12 Ways to Cut Token Consumption in Claude Code</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that sub-agents are a major source of token burn, with one user reporting 7 sub-agents launched for a single task. Others suspect Anthropic's business model incentivizes higher token usage, and note that prompt minimalism is not the only factor—tooling quality and roundtrips matter too.

**Tags**: `#AI coding agents`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#software engineering`

---

<a id="item-3"></a>
## [CISA built incident playbook during real incident](https://techcrunch.com/2026/07/10/us-cyber-agency-cisa-had-to-build-its-incident-playbook-during-the-incident-agency-reveals/) ⭐️ 7.0/10

CISA revealed it had to develop its incident response playbook while responding to a real incident involving exposed passwords in a contractor's GitHub repository, as reported by cybersecurity journalist Brian Krebs. This highlights a significant gap in preparedness at a leading cybersecurity agency, raising concerns about government cybersecurity practices and the effectiveness of incident response across federal agencies. The incident was discovered by a security researcher from GitGuardian, who alerted Krebs about exposed passwords in a publicly accessible GitHub repository belonging to a CISA contractor. CISA acknowledged it lacked a pre-existing playbook and had to create one during the response.

rss · TechCrunch · Jul 11, 01:01

**Background**: CISA is the U.S. federal agency responsible for cybersecurity and infrastructure security. Incident response playbooks are standardized procedures that guide organizations through detecting, responding to, and recovering from cybersecurity incidents. Executive Order 14028 directed CISA to develop such playbooks for federal civilian agencies, but this incident suggests internal gaps remain.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks">Federal Government Cybersecurity Incident and Vulnerability Response Playbooks | CISA</a></li>
<li><a href="https://www.cisa.gov/sites/default/files/2024-08/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf">TLP:CLEAR Cybersecurity Incident & Vulnerability Response Playbooks</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#CISA`, `#incident response`, `#government`, `#data breach`

---

<a id="item-4"></a>
## [Apple's failed car project birthed powerful AI chips](https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra) ⭐️ 7.0/10

Apple's abandoned self-driving car program indirectly led to the development of powerful AI chips, such as the M7 and M8, which now power its devices. The car project's need for on-device AI processing drove chip innovations that later benefited Apple's broader product line. This reveals a significant, previously underappreciated impact of Apple's failed car project on its chip development, with implications for AI hardware. It shows how ambitious projects can yield valuable spin-off technologies even when the main goal is abandoned. The car processor was never finished, but the neural processing units (NPUs) designed for autonomous driving were repurposed for Apple's M-series chips. Reports indicate that future M7 and M8 chips will focus even more on AI support rather than raw speed or power efficiency.

rss · The Verge · Jul 12, 16:27

**Background**: Apple's self-driving car project, known as Project Titan, was canceled in February 2024 after years of development. During the project, Apple realized the need for powerful on-device AI processing to handle autonomous driving tasks, which led to the development of advanced neural engines. These neural engines later became a key component of Apple's M-series chips, enabling on-device AI features like Apple Intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apple_car_project">Apple car project - Wikipedia</a></li>
<li><a href="https://www.macrumors.com/roundup/apple-car/">Apple Car: Apple Car: Now Canceled, What we know</a></li>
<li><a href="https://appleinsider.com/articles/26/07/12/power-of-apples-m7-m8-chips-was-born-from-apple-car-research">Power of Apple's M7 & M8 chips was born from Apple Car research</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#AI chips`, `#self-driving cars`, `#hardware`

---