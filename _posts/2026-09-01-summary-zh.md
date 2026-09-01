---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> 从 54 条内容中筛选出 10 条重要资讯。

---

1. [谷歌从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](#item-1) ⭐️ 8.0/10
2. [Simon Willison 解读 OpenAI 的 ChatGPT Work](#item-2) ⭐️ 8.0/10
3. [McKesson 数据泄露：黑客声称窃取数百万患者记录](#item-3) ⭐️ 8.0/10
4. [将安防摄像头变成自动鸟类识别系统：BirdNET-Go 应用](#item-4) ⭐️ 7.0/10
5. [ChatGPT 广告年化收入达 10 亿美元，全球扩展](#item-5) ⭐️ 7.0/10
6. [Wrapture：用于追踪和测试的新 Python 库](#item-6) ⭐️ 7.0/10
7. [五角大楼将 ChatGPT 和 Grok 纳入其 AI 门户](#item-7) ⭐️ 7.0/10
8. [AI 漏洞发现能力或限制政府黑客工具使用](#item-8) ⭐️ 7.0/10
9. [英伟达 35 亿美元投资联发科，意在保持 AI 基础设施核心地位](#item-9) ⭐️ 7.0/10
10. [FTC 与 22 州起诉亚马逊秘密广告附加费](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌从 Chrome 网上应用店移除 MV2 扩展，包括 uBlock Origin](https://webiterate.dev/google-removed-extensions-ublock-origin-108/) ⭐️ 8.0/10

谷歌已从 Chrome 网上应用店移除所有 Manifest V2（MV2）扩展，包括流行的广告拦截器 uBlock Origin。这标志着向 Manifest V3（MV3）过渡的最后阶段，该过渡始于多年前。 这影响了数百万依赖 uBlock Origin 等 MV2 扩展进行广告拦截和隐私保护的 Chrome 用户，可能增加他们接触恶意广告的风险。同时，这也引发了对谷歌对浏览器生态系统控制的担忧，并促使部分用户转向 Firefox 等替代品。 uBlock Origin 于 2026 年 8 月 31 日收到了最终稳定性更新，但在 MV2 支持结束后将无法在 Chrome 中运行。微软 Edge 也将在 2026 年底前停止支持 MV2 扩展，遵循类似的时间表。

hackernews · twapi · 8月31日 21:10 · [社区讨论](https://news.ycombinator.com/item?id=49514878)

**背景**: Manifest V2 是 Chrome 最初的扩展框架，而 Manifest V3 引入了更严格的安全和性能限制，限制了拦截网络请求等能力。谷歌多年前就宣布了 MV2 弃用计划，到 2025 年，大多数用户已迁移到 MV3。从商店移除 MV2 扩展是最后一步，最后一个开发者标志在 Chrome 151（2026 年 7 月）中被删除。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate">Migrate to Manifest V3 | Chrome for Developers</a></li>
<li><a href="https://medium.com/@idmossab/nifest-v2-vs-manifest-v3-chrome-extensions-what-changed-and-why-2025-was-the-turning-point-53b031b70fc6">Manifest V2 vs Manifest V3 (Chrome Extensions): What Changed, and Why 2025 Was the Turning Point | by mossab | Medium</a></li>
<li><a href="https://piunikaweb.com/2026/08/26/ublock-origin-one-last-update-ahead-mv2/">uBlock Origin picks up one last update ahead of MV2 ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，许多用户对谷歌表示失望和不信任。多位评论者建议改用 Firefox，并指出 uBlock Origin 在 Firefox 上表现最佳；还有人分享了关于恶意广告安全问题的个人经历。一些用户提到他们多年前就已迁移到 Firefox，并不怀念 Chrome。

**标签**: `#Chrome`, `#ad-blocking`, `#Manifest V2`, `#browser`, `#privacy`

---

<a id="item-2"></a>
## [Simon Willison 解读 OpenAI 的 ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/) ⭐️ 8.0/10

Simon Willison 发表了一篇分析文章，澄清了 OpenAI 于 7 月 9 日发布的 ChatGPT Work 实际上包含两个不同的产品：基于云的版本（Work Cloud）和本地桌面应用（Work Local）。他详细介绍了 Work Cloud 的独特功能，包括模型选择、带互联网访问的代码执行环境以及无头 Chrome 浏览器。 这一分析帮助开发者和 AI 爱好者理解一个复杂且快速发展的产品，明确了何时使用 Chat 与 Work。它凸显了 AI 工具提供代理能力和云端执行的增长趋势，这可能影响用户与 AI 助手的交互方式。 Work Cloud 仅向付费订阅用户（每月 20 美元及以上）开放，可通过 chatgpt.com 或移动应用访问，而 Work Local 是 ChatGPT 桌面应用（前身为 Codex）的一部分。Work 提供模型选择（GPT-5.6 Sol、Luna、Terra）及多种推理级别，并具有持久化共享文件系统和发布 ChatGPT Sites 的能力。

rss · Simon Willison · 8月30日 23:59

**背景**: ChatGPT Work 是 OpenAI 最新推出的产品，旨在完成具有明确结果的任务，例如创建简报、演示文稿或分析。它基于 ChatGPT 和 Codex 的能力，集成了代码执行和浏览器自动化等代理功能。该产品是 OpenAI 向更自主的 AI 助手迈进的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/">Understanding ChatGPT Work | Simon Willison’s Weblog</a></li>
<li><a href="https://openai.com/chatgpt-work/">ChatGPT Work for every team | OpenAI</a></li>
<li><a href="https://nukcloud.com/en/blog/2026-chatgpt-work-codex-merged-chatgpt-desktop-20260710.html">ChatGPT Work Launched: Codex Merges Into ChatGPT Desktop ...</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#AI tools`, `#product analysis`

---

<a id="item-3"></a>
## [McKesson 数据泄露：黑客声称窃取数百万患者记录](https://techcrunch.com/2026/08/31/hackers-claim-millions-of-patient-records-stolen-during-data-breach-at-healthcare-giant-mckesson/) ⭐️ 8.0/10

黑客声称从美国大型医疗分销商 McKesson 窃取了数百万条患者记录。McKesson 已确认此次泄露，并预计服务会间歇性中断。 此次泄露可能暴露数百万患者的敏感健康数据，导致身份盗窃和隐私侵犯。这凸显了医疗行业对网络攻击的持续脆弱性，此类攻击的频率和严重性正在上升。 据报道，被盗数据包括患者记录和 McKesson 员工的家庭住址。黑客组织 ShinyHunters 声称对此负责，此次泄露涉及对第三方应用程序的未经授权访问和数据外泄。

rss · TechCrunch · 8月31日 18:10

**背景**: McKesson 是美国向医院和医疗机构分销药品和医疗设备的主要分销商。医疗数据泄露日益令人担忧；仅 2023 年，美国就有超过 725 起大型泄露事件，影响超过 1.33 亿人。健康数据的敏感性使得此类泄露尤其具有破坏性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/31/hackers-claim-millions-of-patient-records-stolen-during-data-breach-at-healthcare-giant-mckesson/">Hackers claim millions of patient records stolen during data breach at...</a></li>
<li><a href="https://blog.gridinsoft.com/mckesson-data-breach-2026/">McKesson Data Breach : Confirmed Scope and Response</a></li>
<li><a href="https://www.hipaajournal.com/healthcare-data-breach-statistics/">Healthcare Data Breach Statistics – Updated for 2026</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#data breach`, `#healthcare`, `#privacy`, `#McKesson`

---

<a id="item-4"></a>
## [将安防摄像头变成自动鸟类识别系统：BirdNET-Go 应用](https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/) ⭐️ 7.0/10

一位开发者将安防摄像头改造为运行 BirdNET-Go（一个开源 AI 工具），用于自动识别鸟类。该系统持续监听，实时识别鸟类物种，并在本地硬件上全天候运行。 这展示了一种利用现有安防摄像头基础设施进行生态监测的实用且低成本的方法，使鸟类识别对爱好者变得触手可及。它凸显了将消费级硬件重新用于 AI 驱动的环境观测的日益增长的趋势。 BirdNET-Go 全天候运行，以 48 kHz 采样率分析音频，每 3 秒一个片段，并且还能识别蝙蝠。该系统支持多种警报集成，如 Discord、Telegram 和 MQTT，并设计为可在树莓派上运行。

hackernews · speckx · 8月31日 16:47 · [社区讨论](https://news.ycombinator.com/item?id=49511856)

**背景**: BirdNET 是康奈尔大学开发的深度学习算法，可从音频录音中分类鸟类物种。BirdNET-Go 是一个自托管的实时声景分析器，将这种 AI 带到本地硬件上，实现无需云依赖的连续监测。安防摄像头通常内置麦克风并支持 RTSP 流，使其成为此类系统的便捷音频源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jasontucker.blog/how-i-turned-my-security-cameras-into-an-automatic-bird-identification-system-with-birdnet-go/">How I Turned My Security Cameras Into an Automatic Bird Identification System with BirdNet-Go</a></li>
<li><a href="https://github.com/tphakala/birdnet-go">GitHub - tphakala/birdnet-go: Self-hosted realtime soundscape analyser for birds, bats and other wildlife. Multi-model local AI inference, runs 24/7 on a Raspberry Pi. · GitHub</a></li>
<li><a href="https://birdnet.cornell.edu/">BirdNET – AI-Powered Sound ID</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了他们自己的实现，例如使用 Unifi 门铃摄像头和 Aqara 摄像头，并指出了风噪和采样率限制等挑战。一些人推荐了 Merlin Bird ID 应用等替代方案，而另一些人则讨论了硬件改造和便携性显示增强。

**标签**: `#BirdNET`, `#DIY`, `#computer-vision`, `#audio-classification`, `#security-cameras`

---

<a id="item-5"></a>
## [ChatGPT 广告年化收入达 10 亿美元，全球扩展](https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads) ⭐️ 7.0/10

OpenAI 宣布 ChatGPT 广告的年化收入运行率已达到 10 亿美元，并正在全球扩展，以支持更广泛地获取 AI。 这一里程碑表明 OpenAI 广告业务具有显著的商业吸引力，表明除了订阅之外还有可行的变现途径。这也支持了 OpenAI 通过免费和负担得起的选项让更多人使用 AI 的使命。 10 亿美元的数字是年化运行率，而非实际年收入，反映了 ChatGPT 内广告的快速增长。全球扩展表明 OpenAI 正在将其广告基础设施扩展到新市场，这可能涉及合作伙伴关系和本地化的广告产品。

rss · OpenAI Blog · 8月31日 04:00

**背景**: ChatGPT 广告是 OpenAI 的广告平台，在 ChatGPT 回复中展示广告。它被引入以提供除订阅之外的收入来源，允许免费使用 AI。运行率指标根据当前表现估算未来年收入，常用于科技行业衡量增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://help.openai.com/en/articles/20001047-ads-in-chatgpt">Ads in ChatGPT | OpenAI Help Center</a></li>
<li><a href="https://www.seo.com/blog/chatgpt-advertising/">ChatGPT Advertising : Meet Your Next Revenue Channel</a></li>
<li><a href="https://www.investopedia.com/terms/r/runrate.asp">investopedia.com/terms/r/runrate.asp</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#ChatGPT`, `#AI business`, `#monetization`, `#AI access`

---

<a id="item-6"></a>
## [Wrapture：用于追踪和测试的新 Python 库](https://simonwillison.net/2026/Aug/31/introducing-wrapture/) ⭐️ 7.0/10

wrapt 的创造者 Graham Dumpleton 发布了 Wrapture，这是一个 Python 库，扩展了 wrapt 的猴子补丁功能，以实现函数的追踪和覆盖，用于测试和可观测性。它包含 OpenTelemetry 支持，并提供了基于配置的机制来为现有项目添加追踪。 Wrapture 为测试提供了 unittest.mock 的潜在替代方案，并为 Python 项目实现追踪提供了一种新颖的方式。它可能简化 Python 开发者的可观测性和测试工作流程，特别是那些已经使用 wrapt 的开发者。 Wrapture 是一个非常年轻的项目，只有几周的历史，是 Graham 第一个完全由代理驱动的大型项目，所有代码和文档都是由 AI 助手在他的指导下编写的。它支持通过 TOML 文件进行基于配置的追踪，并包含 OpenTelemetry 支持。

rss · Simon Willison · 8月31日 23:59

**背景**: 猴子补丁是 Python 中的一种技术，允许在运行时修改函数或方法的行为，常用于测试中替换或存根代码部分。wrapt 是一个知名的库，用于以透明高效的方式实现装饰器和猴子补丁。追踪涉及记录代码的执行，如函数调用和返回值，这对于调试和可观测性很有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/60551322/wrapt-decorators-and-monkey-patching">python - @ wrapt decorators and monkey patching - Stack Overflow</a></li>
<li><a href="https://docs.python.org/3/library/trace.html">trace — Trace or track Python statement execution</a></li>
<li><a href="https://pymotw.com/2/sys/tracing.html">Tracing a Program As It Runs - Python Module of the Week</a></li>

</ul>
</details>

**标签**: `#Python`, `#testing`, `#monkeypatching`, `#tracing`, `#developer tools`

---

<a id="item-7"></a>
## [五角大楼将 ChatGPT 和 Grok 纳入其 AI 门户](https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/) ⭐️ 7.0/10

五角大楼将把 OpenAI 的 ChatGPT 和 SpaceXAI 的 Grok 的版本整合到其中央 AI 门户中，与谷歌的 Gemini 并列。这标志着这些主要的商业 AI 模型首次通过统一平台向美国军方提供。 这一采用标志着美国军方对商业 AI 技术的接受发生了重大转变，可能加速 AI 在国防行动中的整合。这也引发了关于在军事背景下使用此类模型的伦理和安全影响的重要问题。 该公告简短，缺乏技术细节，例如将部署哪个版本的 ChatGPT 和 Grok，以及如何确保其安全性。此次整合延续了五角大楼与主要 AI 公司合作的趋势，包括之前与 Anthropic 和谷歌的合作。

rss · TechCrunch · 8月31日 20:13

**背景**: 五角大楼的中央 AI 门户是一个旨在为军事人员提供各种 AI 工具访问权限的平台。OpenAI 的 ChatGPT 是一种广泛使用的对话式 AI，而 SpaceXAI 的 Grok 是一系列以编码和代理任务著称的大型语言模型。纳入这些模型反映了国防领域对商业 AI 日益增长的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/31/the-pentagon-now-has-its-own-version-of-chatgpt-and-grok/">The Pentagon now has its own version of ChatGPT and... | TechCrunch</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceXAI">SpaceXAI - Wikipedia</a></li>
<li><a href="https://www.cnbc.com/2026/02/26/anthropic-pentagon-ai-amodei.html">cnbc.com/2026/02/26/anthropic- pentagon - ai -amodei.html</a></li>

</ul>
</details>

**标签**: `#AI`, `#Government`, `#National Security`, `#OpenAI`, `#Grok`

---

<a id="item-8"></a>
## [AI 漏洞发现能力或限制政府黑客工具使用](https://techcrunch.com/2026/08/31/how-ai-could-make-it-harder-for-governments-to-use-hacking-tools/) ⭐️ 7.0/10

文章讨论了 AI 在发现和利用漏洞方面日益增强的能力，可能使政府更难使用黑客工具和间谍软件，并可能重新引发关于设备后门的辩论。 这一点很重要，因为它可能改变网络安全中的力量平衡，影响政府的监控能力和国家安全政策。同时，它也凸显了 AI 的双重用途性质，既能防御也能攻击系统，促使人们重新评估加密和后门政策。 文章提到了近期政府黑客工具泄露给网络犯罪分子的事件，例如一套针对旧版 iOS 的 iPhone 攻击工具。文章还指出，AI 发现漏洞的能力可能使政府更难控制这些工具，因为对手可能更容易复制或发现它们。

rss · TechCrunch · 8月31日 15:19

**背景**: 政府黑客工具是用于监控和情报收集的进攻性网络能力，通常利用软件漏洞。关于设备后门的辩论涉及在执法需求与隐私和安全担忧之间取得平衡，因为后门可能被恶意行为者利用。AI 在漏洞发现中的作用日益受到关注，因为它可以自动化和加速这一过程，可能超过防御措施的速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/03/03/a-suite-of-government-hacking-tools-targeting-iphones-is-now-being-used-by-cybercriminals/">A suite of government hacking tools targeting iPhones is now being used by cybercriminals | TechCrunch</a></li>
<li><a href="https://www.nextgov.com/cybersecurity/2026/03/potential-us-built-hacking-tools-obtained-foreign-spies-and-cybercriminals-research-says/411861/">Potential US-built hacking tools obtained by foreign spies and cybercriminals, research says - Nextgov/FCW</a></li>
<li><a href="https://www.bu.edu/riscs/2021/05/03/abuse-resistant-government-backdoors/">Abuse-Resistant Government Backdoors | Center for Reliable Information Systems & Cyber Security</a></li>

</ul>
</details>

**标签**: `#AI`, `#cybersecurity`, `#government hacking`, `#vulnerability discovery`, `#policy`

---

<a id="item-9"></a>
## [英伟达 35 亿美元投资联发科，意在保持 AI 基础设施核心地位](https://techcrunch.com/2026/08/31/nvidias-3-5b-mediatek-bet-reveals-its-plan-for-tackling-big-techs-ai-chip-buildout/) ⭐️ 7.0/10

英伟达向台湾芯片制造商联发科投资 35 亿美元，此举揭示了其在大科技公司自主研发 AI 芯片的背景下，保持其在 AI 基础设施中核心地位的战略。该投资使英伟达能够控制定制 AI 芯片背后的基础设施，将向定制硅片的转变转化为一种“收费”业务。 这项投资意义重大，因为它使英伟达能够在谷歌、亚马逊和微软等大型科技公司设计自家芯片的情况下，保持对 AI 芯片市场的影响力。通过与联发科合作，英伟达可以利用联发科的边缘 AI 能力，并将其影响力扩展到各种设备领域，确保其技术仍然是 AI 基础设施不可或缺的一部分。 这项投资是英伟达更广泛战略的一部分，旨在保障智能基础设施，正如其最近与金融公司合作，调动超过 5000 亿美元用于 AI 计算基础设施所凸显的那样。联发科的 NPU（神经网络处理单元）是一项关键资产，为智能手机、平板电脑和物联网设备等边缘设备提供高效的 AI 加速。

rss · TechCrunch · 8月31日 15:15

**背景**: 英伟达是 GPU 和 AI 芯片的领先设计者，而联发科是一家主要的无晶圆厂半导体公司，以其用于智能手机和其他设备的系统级芯片（SoC）而闻名。随着大科技公司越来越多地设计自己的定制 AI 芯片以降低成本并提高性能，英伟达正寻求通过投资合作伙伴并构建类似收费站的基础设施来保持其不可或缺的地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/08/31/nvidias-35-billion-mediatek-deal-is-a-tollbooth-for-custom-ai-chips/">Nvidia Turns $3.5 Billion MediaTek Deal Into A Toll ... - Forbes</a></li>
<li><a href="https://blogs.nvidia.com/blog/securing-the-infrastructure-of-intelligence/">Securing the Infrastructure of Intelligence - NVIDIA Blog</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital">NVIDIA Partners With Apollo, BlackRock, Blackstone ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#MediaTek`, `#AI chips`, `#investment`, `#AI infrastructure`

---

<a id="item-10"></a>
## [FTC 与 22 州起诉亚马逊秘密广告附加费](https://www.theverge.com/tech/986982/amazon-advertising-prices-ftc-lawsuit) ⭐️ 7.0/10

2026 年 8 月 31 日，FTC 与 22 个州的总检察长对亚马逊提起诉讼，指控其通过“秘密广告附加费”计划暗中抬高广告价格，影响了超过 120 万广告客户，并创造了超过 200 亿美元的收入。 这起诉讼可能重塑数字广告实践，并追究大型科技平台在欺骗性定价方面的责任，可能导致更严格的监管和广告拍卖透明度的提高。这也凸显了亚马逊高利润广告业务受到的日益严格的审查。 该诉讼在华盛顿西区法院提起，指控亚马逊向广告客户隐瞒附加费，并将更高的成本转嫁给消费者。FTC 主席安德鲁·弗格森表示，更高的广告价格“大部分转嫁给了美国消费者”。

rss · The Verge · 8月31日 21:41

**背景**: 亚马逊运营着一个大型广告平台，广告客户在拍卖中竞标广告位。FTC 指控亚马逊在这些拍卖价格中秘密添加附加费，误导广告客户并抬高成本。这起诉讼是监管机构对大型科技公司商业行为进行更广泛审查的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ftc.gov/news-events/news/press-releases/2026/08/ftc-states-sue-amazon-over-secret-ad-surcharge-scheme">FTC, States Sue Amazon Over Secret Ad Surcharge Scheme</a></li>
<li><a href="https://www.nytimes.com/2026/08/31/technology/ftc-amazon-lawsuit-ad-prices.html">FTC and 22 States Sue Amazon Over Advertising Practices</a></li>
<li><a href="https://www.axios.com/2026/08/31/ftc-amazon-deceptive-advertising-lawsuit">FTC , 22 states sue Amazon over deceptive advertising practices</a></li>

</ul>
</details>

**标签**: `#Amazon`, `#FTC`, `#advertising`, `#lawsuit`, `#e-commerce`

---