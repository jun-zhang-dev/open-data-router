# Open Data Router

按需求找优质公开数据源的路由表。每一条都有可机判的探针，由 `verify.py` 验证后生成本文件。

- 最近验证：2026-11-03 05:49 UTC；共 77 条：✅ 73 · ⚠️ 4 · ❌ 0
- ✅ 探针通过且近期有更新（或有意冻结的快照）；⚠️ 降级：超过 540 天未更新 / 声称实时但已停更 / 仓库已归档 / 被限流；❌ 探针失败
- 这里不追求全：长尾需求先去「人工清单」与「数据平台」两类入口
- 「为什么优质」写的是信号来源（谁在筛、凭什么筛），不是对内容的担保；许可列为源头自报，使用前以源头为准
- 改动只改 `sources.toml`，然后跑 `python3 verify.py` 重新生成

## 目录

- [社区信号](#社区信号)（11）
- [人工清单](#人工清单)（8）
- [学术](#学术)（6）
- [百科知识](#百科知识)（4）
- [书籍文化](#书籍文化)（5）
- [视频音频](#视频音频)（4）
- [代码开发](#代码开发)（4）
- [法律政府](#法律政府)（6）
- [金融](#金融)（4）
- [新闻事件](#新闻事件)（3）
- [网页语料](#网页语料)（4）
- [消费兴趣](#消费兴趣)（5）
- [生物医学](#生物医学)（2）
- [物理AI](#物理ai)（3）
- [AI交互评测](#ai交互评测)（4）
- [数据平台](#数据平台)（4）

## 社区信号

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [open-index/hacker-news](https://huggingface.co/datasets/open-index/hacker-news) | 要 HN 全量帖子/评论（2006 起，Parquet），做 HackerTube 式的推荐挖掘；要最新数据补跑官方 API | HackerTube 的直接原料；技术人群近 20 年的主动推荐 | ⚠️ 声称持续更新，但已 71 天未更新 | 2026-08-23 | odc-by |
| [hacker-news.firebaseio.com](https://hacker-news.firebaseio.com/v0/maxitem.json) | 要 HN 实时单条数据（官方 API） | 官方源，上面 HF 镜像的上游 | ✅ | — | — |
| [play.clickhouse.com](https://play.clickhouse.com/?user=play&query=SELECT+count()+FROM+hackernews) | 不下载、直接用 SQL 试查 HN / GitHub 事件等表 | 预装 hackernews、github_events 等表，原型验证零成本 | ✅ | — | — |
| [open-index/arctic](https://huggingface.co/datasets/open-index/arctic) | 要 Reddit 全量（2005 起，157 亿条），按 subreddit 切高质量社区 | Pushshift 停服后的社区接替，覆盖所有公开 subreddit | ✅ | 2026-08-06 | other |
| [ArthurHeitmann/arctic_shift](https://github.com/ArthurHeitmann/arctic_shift) | 要 Reddit 存档的上游工具 / 在线查询 API | 上面 HF 镜像的源头 | ✅ | 2026-10-11 | — |
| [HuggingFaceH4/stack-exchange-preferences](https://huggingface.co/datasets/HuggingFaceH4/stack-exchange-preferences) 🧊 | 要 StackExchange 问答 + 投票（偏好对） | 投票即质量信号 | ✅ | 2023-03-08 | cc-by-sa-4.0 |
| [lobste.rs](https://lobste.rs/hottest.json) | 要比 HN 更窄更硬核的技术链接流 | 邀请制社区，噪声低 | ✅ | — | — |
| [www.v2ex.com](https://www.v2ex.com/api/topics/hot.json) | 要中文技术社区热帖 | 中文程序员社区的长期主阵地 | ✅ | — | — |
| [wangrui6/Zhihu-KOL](https://huggingface.co/datasets/wangrui6/Zhihu-KOL) 🧊 | 要中文知乎高质量问答快照 | KOL 回答，带点赞 | ✅ | 2023-04-23 | — |
| [alpindale/two-million-bluesky-posts](https://huggingface.co/datasets/alpindale/two-million-bluesky-posts) 🧊 | 要 Bluesky 帖子样本 | 开放协议社交网络的公开数据 | ✅ | 2024-11-28 | apache-2.0 |
| [kagisearch/smallweb](https://github.com/kagisearch/smallweb) | 要人工挑过的独立博客 / 小站列表（带 RSS） | Kagi 人工维护，排除 SEO 农场 | ✅ | 2026-11-01 | MIT |

## 人工清单

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) | 找某主题的公开数据集（本路由没覆盖到的长尾先去这里） | 8 万星，按主题分类，元数据在 apd-core 可机读 | ✅ | 2026-11-02 | MIT |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 找免费 API | 最大的公开 API 清单 | ✅ | 2026-11-01 | MIT |
| [Developer-Y/cs-video-courses](https://github.com/Developer-Y/cs-video-courses) | 要有视频的大学 CS 课程 | 按学科整理的公开课视频 | ✅ | 2026-10-31 | — |
| [kilimchoi/engineering-blogs](https://github.com/kilimchoi/engineering-blogs) | 要公司技术博客列表 | 3.9 万星；注意 2024 后更新放缓 | ⚠️ 803 天未更新 | 2024-08-21 | — |
| [timqian/chinese-independent-blogs](https://github.com/timqian/chinese-independent-blogs) | 要中文独立博客（多数带 RSS） | 社区维护，带 RSS 地址 | ✅ | 2026-11-03 | MIT |
| [ruanyf/weekly](https://github.com/ruanyf/weekly) | 要中文人工筛过的科技链接（历年每期 Markdown） | 每周人工筛选，全文在 GitHub 易抽取 | ✅ | 2026-10-31 | — |
| [plenaryapp/awesome-rss-feeds](https://github.com/plenaryapp/awesome-rss-feeds) | 要按主题/国家分类的 RSS（带 OPML） | OPML 可直接导入阅读器或采集器 | ✅ | 2026-10-05 | CC0-1.0 |
| [zudochkin/awesome-newsletters](https://github.com/zudochkin/awesome-newsletters) | 要英文 Newsletter 列表 | 按领域整理 | ✅ | 2026-10-01 | — |

## 学术

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [api.openalex.org](https://api.openalex.org/works?per-page=1) | 要全学科论文 + 引用 + 作者 + 机构图谱（CC0） | MAG 的开放继任者，引用数是天然质量信号；API 现按额度计费（免费每日约 $0.1 额度） | ✅ | — | — |
| [open-index/open-arxiv](https://huggingface.co/datasets/open-index/open-arxiv) | 要 arXiv 全量元数据（约 300 万篇，CC0，Parquet） | Cornell 官方 Kaggle 元数据的 Parquet 版 | ✅ | 2026-03-24 | cc0-1.0 |
| [scholarweave/arxiv-latex](https://huggingface.co/datasets/scholarweave/arxiv-latex) | 要 arXiv 论文 LaTeX 正文 | 正文级，近期仍更新 | ✅ | 2026-10-27 | other |
| [api.semanticscholar.org](https://api.semanticscholar.org/graph/v1/paper/search?query=transformer&limit=1) | 要论文检索 / 影响力引用 / 推荐 API（无 key 共享额度常 429，申请免费 key） | AI2 维护，有 influentialCitationCount | ⚠️ HTTP 429 限流（端点存在，数据未取到） | — | — |
| [eutils.ncbi.nlm.nih.gov](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=crispr&retmax=1&retmode=json) | 要生物医学文献检索（官方 API） | NCBI 官方 | ✅ | — | — |
| [ncbi/pubmed](https://huggingface.co/datasets/ncbi/pubmed) 🧊 | 要 PubMed 摘要批量 | NCBI 官方上传 | ✅ | 2024-01-26 | other |

## 百科知识

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [wikimedia/wikipedia](https://huggingface.co/datasets/wikimedia/wikipedia) 🧊 | 要多语言维基正文（批量） | Wikimedia 官方 | ✅ | 2024-01-09 | cc-by-sa-3.0,gfdl |
| [wikimedia/structured-wikipedia](https://huggingface.co/datasets/wikimedia/structured-wikipedia) | 要结构化维基（infobox、章节） | Wikimedia Enterprise 官方 | ✅ | 2026-05-19 | cc-by-sa-4.0 |
| [dumps.wikimedia.org](https://dumps.wikimedia.org/index.json) | 要最新维基 / Wikidata 全量 dump | 上游官方 dump | ✅ | — | — |
| [open-index/open-library](https://huggingface.co/datasets/open-index/open-library) | 要图书元数据（书目、作者、ISBN） | Internet Archive Open Library 的 Parquet 版 | ✅ | 2026-03-24 | cc0-1.0 |

## 书籍文化

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [PleIAs/common_corpus](https://huggingface.co/datasets/PleIAs/common_corpus) | 要全开放许可的大语料（书、报纸、政府、科学，2.27T token） | 逐文档可追溯许可 | ✅ | 2026-05-06 | — |
| [institutional/institutional-books-hl](https://huggingface.co/datasets/institutional/institutional-books-hl) 🔒 | 要哈佛图书馆公版书（需申请） | 图书馆馆藏级 | ✅ | 2026-08-19 | — |
| [storytracer/US-PD-Books](https://huggingface.co/datasets/storytracer/US-PD-Books) 🧊 | 要美国公版书全文 | 公版，可商用 | ✅ | 2024-03-13 | cc0-1.0 |
| [gutendex.com](https://gutendex.com/books/?ids=1342) | 要古登堡计划书目/全文（JSON API） | 公版经典 | ✅ | — | — |
| [archive.org](https://archive.org/advancedsearch.php?q=collection%3Aopensource&fl%5B%5D=identifier&rows=1&output=json) | 要网页快照 / 老书 / 音视频档案 | 最大的公共数字档案馆 | ✅ | — | — |

## 视频音频

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [PleIAs/YouTube-Commons](https://huggingface.co/datasets/PleIAs/YouTube-Commons) 🧊 | 要 CC-BY YouTube 视频转写（按内容找视频） | 只收 CC-BY 授权视频 | ✅ | 2024-06-26 | cc-by-4.0 |
| [HuggingFaceFV/finevideo](https://huggingface.co/datasets/HuggingFaceFV/finevideo) 🔒 | 要带细粒度标注的视频 | HF 官方，含场景/情绪标注 | ✅ | 2026-04-30 | cc |
| [podcastindex.org](https://podcastindex.org/) | 要开放播客目录（有公开 DB dump 与 API） | 开放的播客索引，替代 Apple 封闭目录 | ✅ | — | — |
| [amphion/Emilia-Dataset](https://huggingface.co/datasets/amphion/Emilia-Dataset) 🔒 🧊 | 要大规模多语种真实语音 | 真实场景语音，中英为主 | ✅ | 2025-02-28 | cc-by-4.0 |

## 代码开发

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [data.gharchive.org](https://data.gharchive.org/2024-01-01-0.json.gz) | 要 GitHub 全部公开事件（2011 起，每小时一个文件） | star/fork/PR 是开发者的行为信号 | ✅ | — | — |
| [open-index/open-github](https://huggingface.co/datasets/open-index/open-github) | 要 GH Archive 的 Parquet 实时镜像（注意卡片称历史仍在回填） | 免解析，直接 DuckDB | ⚠️ 声称持续更新，但已 208 天未更新 | 2026-04-09 | odc-by |
| [bigcode/the-stack-v2](https://huggingface.co/datasets/bigcode/the-stack-v2) 🔒 | 要许可清洗过的源码大集 | BigCode 官方，带许可证过滤 | ✅ | 2026-08-03 | other |
| [SALT-NLP/SWE-chat](https://huggingface.co/datasets/SALT-NLP/SWE-chat) 🔒 | 要真实开发者与编码 agent 的对话 | 真实使用而非合成 | ✅ | 2026-10-03 | odc-by |

## 法律政府

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [common-pile/caselaw_access_project](https://huggingface.co/datasets/common-pile/caselaw_access_project) 🧊 | 要美国判例全文 | 哈佛法学院 CAP | ✅ | 2025-06-06 | — |
| [www.courtlistener.com](https://www.courtlistener.com/api/rest/v4/) | 要美国判例 / 庭审文件实时 API | Free Law Project，持续更新 | ✅ | — | — |
| [isaacus/open-australian-legal-corpus](https://huggingface.co/datasets/isaacus/open-australian-legal-corpus) | 要澳洲法律全文 | 官方来源汇编，开放许可 | ✅ | 2026-03-07 | other |
| [ourworldindata.org](https://ourworldindata.org/grapher/life-expectancy.csv?v=1&csvType=filtered&useColumnShortNames=true) | 要国家级长期统计（每张图都能下 CSV） | 带出处与方法说明 | ✅ | — | — |
| [api.worldbank.org](https://api.worldbank.org/v2/country/CHN/indicator/NY.GDP.MKTP.CD?format=json&per_page=1) | 要世界银行宏观指标 API | 官方 | ✅ | — | — |
| [catalog.data.gov](https://catalog.data.gov/) | 要美国政府开放数据目录（2026 起 CKAN API 迁到 api.gsa.gov，需免费 api_key） | 官方目录 | ✅ | — | — |

## 金融

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [TeraflopAI/SEC-EDGAR](https://huggingface.co/datasets/TeraflopAI/SEC-EDGAR) | 要美股公司公告批量 | 一手披露文件 | ✅ | 2026-04-17 | apache-2.0 |
| [defeatbeta/yahoo-finance-data](https://huggingface.co/datasets/defeatbeta/yahoo-finance-data) | 要美股行情 / 财报（每日更新） | 持续更新，下载量高 | ✅ | 2026-11-03 | odc-by |
| [kurry/sp500_earnings_transcripts](https://huggingface.co/datasets/kurry/sp500_earnings_transcripts) | 要标普 500 财报电话会转写 | 管理层原话 | ✅ | 2025-05-21 | mit |
| [Anthropic/EconomicIndex](https://huggingface.co/datasets/Anthropic/EconomicIndex) | 要 AI 在各职业任务中的实际使用分布 | Anthropic 一手使用数据 | ✅ | 2026-09-30 | mit |

## 新闻事件

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [data.gdeltproject.org](http://data.gdeltproject.org/gdeltv2/lastupdate.txt) | 要全球新闻事件流（15 分钟更新） | 覆盖面最广的开放事件库 | ✅ | — | — |
| [dell-research-harvard/newswire](https://huggingface.co/datasets/dell-research-harvard/newswire) 🧊 | 要美国历史通讯社稿（1878-1977） | 哈佛整理，历史一手稿 | ✅ | 2025-08-30 | cc-by-4.0 |
| [index.commoncrawl.org](https://index.commoncrawl.org/collinfo.json) | 要原始网页抓取（含 CC-NEWS） | 所有开放网页语料的上游 | ✅ | — | — |

## 网页语料

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [HuggingFaceFW/fineweb-edu](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu) | 要按教育价值打分过的英文网页 | 分类器打分，可按分数阈值取 | ✅ | 2025-07-11 | odc-by |
| [HuggingFaceFW/fineweb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) | 要多语种（含中文）清洗网页 | HF 官方，1000+ 语种 | ✅ | 2025-10-27 | odc-by |
| [HuggingFaceFW/finepdfs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs) | 要网上 PDF 抽取文本（报告、论文、手册） | PDF 信息密度高于普通网页 | ✅ | 2026-04-03 | odc-by |
| [CASIA-LM/ChineseWebText2.0](https://huggingface.co/datasets/CASIA-LM/ChineseWebText2.0) 🧊 | 要带质量分的中文网页 | 中科院自动化所，多维质量标签 | ✅ | 2024-12-02 | apache-2.0 |

## 消费兴趣

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [McAuley-Lab/Amazon-Reviews-2023](https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023) 🧊 | 要商品评论 + 元数据（推荐系统经典） | UCSD 官方，规模最大 | ✅ | 2024-12-08 | — |
| [FronkonGames/steam-games-dataset](https://huggingface.co/datasets/FronkonGames/steam-games-dataset) | 要 Steam 游戏元数据与评价 | 持续更新 | ✅ | 2026-11-02 | mit |
| [Lichess/standard-chess-games](https://huggingface.co/datasets/Lichess/standard-chess-games) | 要全量棋局 / 残局题 | Lichess 官方，CC0 | ✅ | 2025-10-16 | cc0-1.0 |
| [musicbrainz.org](https://musicbrainz.org/ws/2/artist/?query=radiohead&limit=1&fmt=json) | 要音乐元数据（艺人、专辑、录音） | 开放音乐百科，CC0 核心数据 | ✅ | — | — |
| [planet.openstreetmap.org](https://planet.openstreetmap.org/) | 要全球地图 / POI | 开放地图的上游 | ✅ | — | — |

## 生物医学

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [HuggingFaceBio/FineDNA](https://huggingface.co/datasets/HuggingFaceBio/FineDNA) | 要清洗过的 DNA 序列语料 | HF 官方新发 | ✅ | 2026-10-30 | apache-2.0 |
| [ibrahimhamamci/CT-RATE](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE) 🔒 | 要 CT 影像 + 放射报告 | 影像-报告配对，持续维护 | ✅ | 2026-10-12 | cc-by-nc-sa-4.0 |

## 物理AI

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [nvidia/PhysicalAI-Autonomous-Vehicles](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles) 🔒 | 要自动驾驶多传感器数据 | NVIDIA 官方，规模大 | ✅ | 2026-10-23 | other |
| [allenai/objaverse](https://huggingface.co/datasets/allenai/objaverse) | 要大规模 3D 物体 | AI2 官方 | ✅ | 2026-10-08 | odc-by |
| [builddotai/Egocentric-10K](https://huggingface.co/datasets/builddotai/Egocentric-10K) 🔒 | 要第一人称工厂作业视频 | 真实工作场景 | ✅ | 2026-02-16 | apache-2.0 |

## AI交互评测

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [allenai/WildChat-1M](https://huggingface.co/datasets/allenai/WildChat-1M) 🧊 | 要真实用户与 ChatGPT 的对话 | 真实流量，非合成 | ✅ | 2024-10-17 | odc-by |
| [lmsys/lmsys-chat-1m](https://huggingface.co/datasets/lmsys/lmsys-chat-1m) 🔒 🧊 | 要多模型真实对话 | Chatbot Arena 真实流量 | ✅ | 2024-07-27 | — |
| [cais/hle](https://huggingface.co/datasets/cais/hle) 🔒 | 要前沿难度评测题 | 专家出题 | ✅ | 2026-01-20 | mit |
| [openai/gdpval](https://huggingface.co/datasets/openai/gdpval) | 要真实职业任务评测 | 按职业 GDP 权重选题 | ✅ | 2026-02-10 | — |

## 数据平台

| 源 | 什么时候来这里 | 为什么优质 | 状态 | 最近更新 | 许可 |
|---|---|---|---|---|---|
| [zenodo.org](https://zenodo.org/api/records?size=1) | 要论文配套数据（带 DOI） | CERN 运营，学术数据存档 | ✅ | — | — |
| [registry.opendata.aws](https://registry.opendata.aws/) | 要 TB 级云上公开数据（卫星、基因组、气象） | 原地计算不用下载 | ✅ | — | — |
| [source.coop](https://source.coop/) | 要地理空间 / 云原生格式数据 | Radiant Earth 运营 | ✅ | — | — |
| [academictorrents.com](https://academictorrents.com/) | 要超大学术数据（BT 分发，含旧 Reddit dump） | 大体量分发通道 | ✅ | — | — |

🔒 需申请访问　🧊 有意冻结的快照（不按久未更新降级）

## 许可

本文档与 `sources.toml` 以 CC0-1.0 发布；`verify.py` 以 MIT 发布。各数据源遵循其自身许可。
