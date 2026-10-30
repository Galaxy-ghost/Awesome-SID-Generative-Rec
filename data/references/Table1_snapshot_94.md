# Table 1 扩展版

综述 Table 1 的 60 个方法照抄（写法同 `../00_背景/综述_ARR2739.pdf` 第 4 页，缩写见该页表下 Legend；10-25 起不再沿用综述的顺序和 I/II/III 分组，改按“修什么毛病”分成六条带，TIGER（基线）和 6 篇整体范式、框架与基准论文放在最上面一块；本表新增的写法和标记见表下注），再加上本人决定收录的新方法（标 ★，即不在综述里的论文）。术语见 `../README.md`。本文件每次修改记在“修改记录”；对原有格子的全部改动和理由记在“附：改动汇总”。

## 收录标准

收录由本人逐篇决定，只看适不适合放进综述（10-21 起）。原来的两条标准作废：标准 1 是正式录用于公认的会议或期刊，标准 2 是预印本 Semantic Scholar 引用不少于 20。“附：收录筛选”里按这两条写的判断只作参考。

**POI 与本地生活的论文进 Table 1，按同一套规则归类**（10-27 本人定，取代 10-07 的“暂缓”）。

## 填写说明

- **★** = 不在综述里的论文，是本轮新增的方法。综述的 Table 1 和正文都没有引用；**★‡** = 综述正文引用过、但不在综述 Table 1 里（只有 QuaSID，§9，p8）。没有 ★ 的 60 个方法都来自综述 Table 1。方法名写成 `方法名 (第一作者 et al., 年份)`。
- 按六类毛病分组（10-25 起，原综述的 I/II/III 作废），带内先按改动阶段排序（Representation → Tokenization → Backbone → Training → Inference），同一阶段再按 arXiv 首次挂出的先后排，改动所在阶段的格子加粗；改动在 Training 的，只加粗 Tokenizer、Objective 中改了的那一格（10-26 起）。最上面一块收 TIGER（基线）和 6 篇整体新范式、开源框架、基准或分析论文，不贴毛病标签，不加粗。判定规则和逐篇依据见“附：毛病与阶段的依据”。附录里的“归 I/II/III”“I 组”等说法是 10-25 以前的旧分组，已作废，留作记录。方法总表是本地的 `Table2_按仓库分类.md`（本表与仓库方法的并集）；仓库 fork 的 README 只维护仓库条目，不收我找的论文。
- 五列取值沿用本表已有的写法；新写法在附录说明。Venue 写法同表内。Training 拆成的 Tokenizer、Objective 两列只用表下注列出的写法（10-26）。
- 依据写论文中的位置（§、Fig.、Eq.）和 `pdf/` 里 PDF 的页码；AAAI 论文没有节号，写小节标题。
- 原有方法的格子和原文不一致才改，改动写进“附：改动汇总”。

## 修改记录

只记本文件的改动，每条写日期、做了什么、涉及哪些行。格子级的改动和理由见“附：改动汇总”，★ 方法的依据见“附：★ 方法的依据”。

| 日期 | 修改 |
| --- | --- |
| 10-07 | 建立本文件：照抄综述 Table 1 的 60 个方法，写收录标准和填写说明；筛选仓库批 13 个方法（附：收录筛选）；核对 TokenRec、HiD-VAE、GRLM、GenCDR、MACRec、GMC 的五列（Claude 代核） |
| 10-08 | 核对 LETTER、Align3GR、OneRec-Think、SIDReasoner 的五列（Claude 代核） |
| 10-09 | 读 GRID、GFlowGR、S2GR、V-STAR 原文，填五列、归组（新增 4 个 ★）；按外部复核意见再核一轮，MACRec 的 Training 由待定改为 2-Stage，顺带改 CARD、GEM-Rec；DeepContextGR 按 v3 复核；列出待定 3 条。原有方法共改 14 格，见“附：改动汇总” |
| 10-10 | 我找的 30 篇：收录 18 个，按 I 组 5 个、II 组 4 个、III 组 9 个加进主表；附录补依据；填“我找的论文”登记表。表下注补充“–”、track、“A / B”和新写法的说明 |
| 10-10 | 收录标准补一句：其他正式出版的 full paper 有含金量的也收，workshop 不收。按此把 CID、TransRec 加进 I 组，MMGRec 加进 II 组，GPTRec 判为不收；登记表同步改判断 |
| 10-10 | ★ 的含义写明为“不在综述里的论文”；QuaSID 综述正文已引用，改标 ★‡；删除 `候选论文/清单.md`（10-09 摘要级初筛），登记表的引用一并改掉 |
| 10-11 | 补核 MACRec 的 Representation、Tokenization，与综述一致，不改格子；主表给待定 3 条（MQL4GRec、UniTok、DeepContextGR）的格子加“（待定）”，表下注说明；STATIC 依据统一取 Amazon 实验，工业配置移到备注；填写说明改写按仓库分类的表在哪里维护 |
| 10-11 | “我找的论文”补登 ReCast、RGD、TemporalCold、ColdStart-Repro、HSTU，都不收（ReCast、RGD 是预印本，引用不足 20；TemporalCold、ColdStart-Repro 是分析论文；HSTU 不用 SID），主表不变；PDF 放进 `候选论文/` |
| 10-11 | 按本人决定收录 VQ-Rec（仓库“新增论文”一节，WWW’23），加进 II 组，读原文（`pdf/VQ-Rec_2210.12316.pdf`）填五列和依据；收录筛选的判断改为收录；表下注补新写法 Pretrain+FT。主表共 86 个方法 |
| 10-11 | 填“附：PPT case 页”：按本人决定选 9 篇（DECOR、GRID、S2GR、OneRec-V2、DIGER、V-STAR、PLUM、STATIC、AtSpeed），写章 · 子类、标签、插入位置和每页要点；OneRec-V2、PLUM、AtSpeed 的要点按原文摘要核对。主表不变 |
| 10-11 | 待定 3 条按本人决定改：MQL4GRec Inference 改 Beam；UniTok 三列改 Enc-Dec、2-Stage、Beam†（读原文 p5、附录 D.4）；DeepContextGR Inference 改 Beam。原有方法共改 19 格，主表不再有“（待定）” |
| 10-11 | 按外部审核改 4 格：SEATER、FORGE 的 Venue，Molar 的 Tokenization、Inference，原有方法共改 23 格；★ GFlowGR 的 Inference 两套设置都标推定（Beam† / C-Beam†）。写法统一为 NeurIPS、arXiv、2-Stage，占位符统一为 – |
| 10-21 | 收录标准作废，改由本人逐篇决定：改写“收录标准”一节和开头一句；删掉 SCRec、TransRec 依据里“Table 2 记为边界方法”的说法（Table 2 已不分核心、边界、排除）；填写说明里 Table 2 的叫法同步改。主表不变 |
| 10-25 | Table 1 按“修什么毛病”重新分组（Claude 初标）：原 I/II/III 三组换成六条带，TIGER 作基线置顶；每行改动所在阶段的格子加粗；拿不准的标“（待定）”；依据和拿不准的列在“附：毛病与阶段的依据”。五列的值不变 |
| 10-25 | 按本人当天的决定定稿分组：TIGER 和 OneRec、PLUM、MiniOneRec、GRID、FORGE、GR-Generalize 合成最上面一块“Paradigms, Systems and Benchmarks”，不贴毛病标签；DeepContextGR、DeepInterestGR 与 TriAlignGR 同组作者、设计重叠，删去两行，只留 TriAlignGR；其余 25 篇待定按三条补充规则定（规则写进附录），DIGER 改 II、DECOR 改 III、DualGR 改 VI × Backbone，其余照初标；取消“（待定）”；带内同一阶段按 arXiv 首次挂出先后排。顺带改：MMQ-v2 按 arXiv v3 改名 ADC-SID；COBRA 按 NeurIPS 2025（论文集第 38 卷）把年份改为 2025（综述 bib `COBR` 的 year 也写成 2026，改引用时一并改）；STAMP 的 Backbone 由 – 改为 Enc-Dec / Dec-Only，原有方法共改 24 格。主表 84 行：上面一块 7 行，六条带 77 行 |
| 10-26 | 按本人决定把 Training 列拆成 Tokenizer、Objective 两列：Tokenizer 记编号器会不会随生成器更新；Objective 只用 12 种写法，SFT 并进 NTP，因为是否从预训练大模型起步属于 Backbone。46 行回原文（arXiv 最新版）核，38 行由旧写法换算，换算的行里抽查 DiscRec、Latte、ETEGRec、GREAM，与原文一致。旧写法错或会误导的 16 行，加上新值只是推定的 3 行（GR-Generalize、MSCGRec、PAD-Rec），依据见“附：改动汇总”的“Training 拆两列”，推定的格子标 †；这 19 行单列一节，不计入改格数。顺带按原文改 3 格 Backbone：PROMISE、GR-Generalize 由 Dec-Only 改为 Enc-Dec，ADC-SID 由 – 改为 Enc-Dec，原有方法共改 27 格。表下注加两列的写法，“新写法”一条删去只属于旧 Training 列的条目。分组、类名和其余各列不变 |
| 10-26 | 按本人决定定六类的英文类名：I Informativeness、II Uniqueness and Validity、III SID–Model Alignment，IV–VI 不变。表内改三条通栏；类名、通栏问句和出处记在“附：毛病与阶段的依据”开头。分组和各格不变 |
| 10-28 | 按 10-27 本人的决定把 POI 9 篇加进主表（GNPR-SID、GeoGR、Gwhere、LGRID、LGSID、OneLoc、ProGEO、ROS、Think2Go，都标 ★）：毛病、阶段、Tokenizer、Objective 由两家双盲打标、leader 裁决定，阶段按 10-28 本人定的现行规则取贡献列表第一条（OneLoc、ROS 因此记 Representation、Tokenization）；I 带加 7 行，II、III 带各加 1 行。其余五列以 `Table2_按仓库分类.md` 为底，按原文改：OneLoc 的 Tokenization RQ-VAE → R-KM、Representation Text+Img+Geo+CF → Text+Img+Geo†、Venue WSDM’26（待核）→ arXiv’25；LGSID 改为 A / B 写法（Backbone Disc. / Enc-Dec，Inference Scoring / Beam†），LGSID、ROS 的 Venue 去掉“待核”；Think2Go 的 Tokenization 去掉 †；LGRID 的 Backbone 按英文写作 Disc. (DIN etc.)。五列依据同步改进 Table 2 的“附：POI 的五列依据”。表下注加 POI 一条（GeoGR、Gwhere、ROS）和 LGSID 的 A / B 说明；逐篇依据加 9 条；“Training 拆两列”加 POI 9 行；收录标准和收录筛选的 POI 说法同步改；待定加 PLUM 一条。主表 93 行：上面一块 7 行，六条带 86 行 |
| 10-28 | POI 遗留问题收尾：LGRID 的 Backbone 由 Disc. (DIN etc.) 改为 Disc.，与 LGSID 统一，DIN 等例子写进表下注的 POI 一条；填写说明里引用的 `../01_论文清单/五阶段词表.md` 已不存在，改为“五列取值沿用本表已有的写法”。主表不变 |
| 10-28 | PLUM 的 Objective 由 NTP 改为 Multi-task NTP：继续预训练是同一个 NTP 损失，语料混了用户行为序列和“SID 对标题”“SID 对主题”两种对齐模板（§2.2，p4；Table 1，p4），与 GeoGR 的记法一致。依据写进“Training 拆两列”，“待定”里的 PLUM 一条改为已定。主表行数不变 |
| 10-30 | 按本人决定和 DOS 双盲打标的 leader 裁决，新增第 10 篇 POI：★ DOS（WWW’26 Short），归 III × Tokenization；六列为 Text+CF、Orth. RQ（加粗）、Dec-Only†、Fixed†、NTP、–。按阶段及 arXiv 首次挂出顺序放在 GRLM 后、DECOR 前。补逐篇依据、Training 拆两列依据、新写法和推定说明；收录筛选由“POI 暂缓”改为“收录”，Table 2 的 POI 一节同步。主表 94 行：上面一块 7 行，六条带 87 行 |

## Table 1

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Paradigms, Systems and Benchmarks** |  |  |  |  |  |  |  |
| TIGER (Rajput et al., 2023)（基线） | NeurIPS’23 | Text | RQ-VAE | Enc-Dec | Fixed | NTP | Beam |
| OneRec (Deng et al., 2025) | arXiv’25 | Text+CF | R-KM | Enc-Dec | Fixed | NTP → DPO | Sess. Beam |
| ★ [PLUM](https://arxiv.org/abs/2510.07784) (He et al., 2026) | WWW’26 | Text+Img+CF | RQ-VAE | Dec-Only | Fixed | Multi-task NTP | Beam |
| MiniOneRec (Kong et al., 2025) | arXiv’25 | Text | RQ-VAE | Dec-Only | Fixed | NTP → RL | Beam |
| ★ [GRID](https://arxiv.org/abs/2507.22224) (Ju et al., 2025) | CIKM’25 | Text | R-KM | Enc-Dec | Fixed | NTP | Beam |
| FORGE (Fu et al., 2025) | KDD’26 | Text+Img | RQ-VAE | Dec-Only | Fixed | NTP | Dyn. Beam |
| GR-Generalize (Ding et al., 2026) | arXiv’26 | Text+SID | RQ-VAE | Enc-Dec | Fixed† | NTP† | Hybrid |
| **I. Informativeness** |  |  |  |  |  |  |  |
| Molar (Luo et al., 2024) | arXiv’24 | **Text+Img+CF** | – | Dec-Only | – | Discrim. | Scoring |
| ★ [OneLoc](https://arxiv.org/abs/2508.14646) (Wei et al., 2025) | arXiv’25 | **Text+Img+Geo†** | R-KM | Enc-Dec | Fixed | NTP → DPO | Beam |
| ★ [LGSID](https://arxiv.org/abs/2511.14221) (Jiang et al., 2026) | AAAI’26 | **Text+Geo+CF** | Geo-Idx+RQ | Disc. / Enc-Dec | Fixed | Discrim. / NTP | Scoring / Beam† |
| Q-BERT4Rec (Huang and Gai, 2025) | arXiv’25 | **Text+Img+CF** | RQ-VAE | Encoder (Non-AR) | Fixed | Masked | Non-AR |
| ★ [GeoGR](https://arxiv.org/abs/2602.10411) (Wang et al., 2026) | arXiv’26 | **Text+Geo+CF** | R-KM+EM | Dec-Only | Altern.† | Multi-task NTP | Beam |
| TriAlignGR (Zeng et al., 2026) | arXiv’26 | **Text+Img** | RQ-VAE | Dec-Only | Fixed | Multi-task NTP | C-Beam |
| ★ [LGRID](https://arxiv.org/abs/2607.27944) (Zhang et al., 2026) | arXiv’26 | **Text+Geo** | DSRQ | Disc. | Fixed | Discrim. | Scoring |
| ★ [SCRec](https://arxiv.org/abs/2609.13678) (Dan, 2026) | RecSys’26 | **Text+CF** | RQ-VAE | Non-AR / Enc-Dec | Fixed | MTP + Ctr. | Scoring / Beam† |
| ★ [LMIndexer](https://arxiv.org/abs/2310.07815) (Jin et al., 2024) | ICML’24 | Text | **Self-Sup. ID** | Enc-Dec | Fixed | NTP | C-Beam |
| CoST (Zhu et al., 2024) | RecSys’24 | Text | **C-RQ** | Enc-Dec | Fixed | NTP | Beam |
| ★ [MMGRec](https://arxiv.org/abs/2404.16555) (Liu et al., 2026) | TOMM’26 | Text+Img+CF | **Graph RQ-VAE** | Enc-Dec | Fixed | NTP | C-Beam |
| LETTER (Wang et al., 2024a) | CIKM’24 | Text+CF | **Learn. RQ** | Enc-Dec | Fixed | NTP + Rank | C-Beam |
| TokenRec (Qu et al., 2025) | TKDE’25 | CF | **Masked VQ** | Encoder | Fixed | Discrim. | Scoring |
| ActionPiece (Hou et al., 2025c) | ICML’25 | Text | **OPQ** | Enc-Dec | Fixed | NTP | Ensemble |
| ★ [EAGER-LLM](https://arxiv.org/abs/2502.14735) (Hong et al., 2025) | WWW’25 | Text+CF | **Dual H-KM** | Dec-Only | Fixed | Multi-task NTP | Beam |
| MQL4GRec (Zhai et al.) | ICLR’25 | Text+Img | **Dual RQ** | Enc-Dec | Fixed | Multi-task NTP | Beam |
| ★ [GenSAR](https://arxiv.org/abs/2504.05730) (Shi et al., 2025) | RecSys’25 | Text+CF | **Shared/Spec. RQ** | Enc-Dec | Fixed | Multi-task NTP | C-Beam |
| ★ [GNPR-SID](https://arxiv.org/abs/2506.01375) (Wang et al., 2025) | KDD’25 | Attr+Geo+CF | **RQ-VAE** | Dec-Only | Fixed | NTP | – |
| GRAM (Lee et al., 2025) | ACL’25 | Text+CF | **H-KM** | Enc-Dec | Fixed | NTP | C-Beam |
| DAS (Ye et al., 2025) | CIKM’25 | Text+CF | **Dual RQ** | Enc-Dec | Fixed | NTP | Beam |
| ★ [MMQ](https://arxiv.org/abs/2508.15281) (Xu et al., 2026) | WSDM’26 | Text+Img | **MoE-VQ** | HeterRec | Joint | MTP | – |
| PSRQ (Wang et al., 2025a) | CIKM’25 | Text+Img | **Prog. RQ** | Encoder | Fixed | Discrim. | Scoring |
| MME-SID (Wang et al., 2025b) | CIKM’25 | Text+Img+CF | **MM-RQ** | Dec-Only | Fixed | NTP | Scoring |
| ADC-SID (Xu et al., 2025) | arXiv’25 | Text+Img+CF | **MoE-VQ** | Enc-Dec | Fixed† | NTP | – |
| MACRec (Zhang et al., 2026a) | AAAI’26 | Text+Img | **Cross RQ** | Enc-Dec | Fixed | NTP + Ctr. | C-Beam |
| ★ [ROS](https://arxiv.org/abs/2601.04562) (Lv et al., 2026) | ACL’26 | Text+Geo | **Geo-Prefix+RQ-VAE** | Dec-Only | Fixed | NTP → RL | CoT+C-Beam |
| MSCGRec (Vandenhirtz et al., 2026) | arXiv’26 | Text+Img+CF | **RQ-VAE+DINO** | Enc-Dec | Fixed† | NTP | Trie/C-Beam |
| UniRec (Wang et al., 2026b) | arXiv’26 | Text+CF | **RQ** | Dec-Only | Fixed | NTP → DPO | C-Beam |
| ★ [ProGEO](https://arxiv.org/abs/2604.23156) (He et al., 2026) | arXiv’26 | Text+Geo | **R-KM+Geo-CB** | Dec-Only | Fixed | NTP | Beam+Geo-Filter |
| CapsID (Cheng et al., 2026) | arXiv’26 | Text+CF | **Soft-RQ** | Dec-Only | Fixed | NTP | C-Beam |
| ColaRec (Wang et al., 2024c) | CIKM’24 | Text+CF | H-KM | **Enc-Dec** | Fixed | NTP + Ctr. | C-Beam |
| EAGER (Wang et al., 2024b) | KDD’24 | Text+CF | Dual H-KM | **Dual Enc-Dec** | Fixed | NTP + Ctr. | Fusion |
| COBRA (Yang et al., 2025) | NeurIPS’25 | Text+SID | Casc. RQ | **Dec-Only** | Fixed | NTP + Dense | BeamFusion |
| ★ [DiscRec](https://arxiv.org/abs/2506.15576) (Liu et al., 2025) | arXiv’25 | Text+CF | RQ-VAE / Learn. RQ | **Enc-Dec** | Fixed | NTP | C-Beam |
| ★ [MBGen](https://arxiv.org/abs/2405.16871) (Liu et al., 2024) | CIKM’24 | CF | Bal. VQ+KM | Enc-Dec | Fixed | **NTP** | Beam |
| SynGR (Chen et al., 2026b) | ICML’26 | Text+Img | RQ-VAE | Enc-Dec | Fixed | **NTP + Ctr.** | C-Beam |
| **II. Uniqueness and Validity** |  |  |  |  |  |  |  |
| ★ [CID](https://arxiv.org/abs/2305.06569) (Hua et al., 2023) | SIGIR-AP’23 | CF | **Spectral Clus.** | Enc-Dec | Fixed | NTP | C-Beam |
| ★ [TransRec](https://arxiv.org/abs/2310.06491) (Lin et al., 2024) | KDD’24 | Text | **Multi-Facet ID** | Enc-Dec / Dec-Only | Fixed | NTP | FM-Index+Agg. |
| HiD-VAE (Fang et al., 2025) | arXiv’25 | Text | **Hier. RQ** | Enc-Dec | Fixed | NTP | C-Beam |
| PSI (Zhang et al., 2025a) | arXiv’25 | Text | **Post-hoc RQ** | Enc-Dec | Fixed | NTP | Beam |
| ★ [DIGER](https://arxiv.org/abs/2601.19711) (Fu et al., 2026) | SIGIR’26 | Text | **Learn. RQ** | Enc-Dec | Joint | NTP | Beam† |
| ★‡ [QuaSID](https://arxiv.org/abs/2603.00632) (Hu et al., 2026) | KDD’26 ADS | Text+CF | **QA-RQ** | Enc-Dec | Fixed | NTP | Beam† |
| R3-VAE (Wan et al., 2026) | arXiv’26 | Text | **Ref.-RQ** | – | Fixed | NTP | Beam |
| AdaSID (Pan et al., 2026) | arXiv’26 | Text+Img | **RQ** | Dec-Only | Fixed | NTP | C-Beam |
| CARD (Wei et al., 2026) | arXiv’26 | Text+Img+CF | **NU-RQ** | Enc-Dec | Fixed | NTP | C-Beam |
| ★ [Gwhere](https://arxiv.org/abs/2607.26073) (Zhai et al., 2026) | RecSys’26 | Text+Img+Geo+CF | **Contr. RQ** | Dec-Only | Fixed | NTP → DPO | – |
| **III. SID–Model Alignment** |  |  |  |  |  |  |  |
| IDGenRec (Tan et al., 2024) | SIGIR’24 | Text | **LLM-Vocab** | Enc-Dec | Altern. | NTP | C-Beam |
| ★ [SemConv](https://arxiv.org/abs/2412.13771) (Li et al., 2025) | AAAI’25 | Text+CF | **Align. RQ** | Dec-Only | Fixed | Multi-task NTP | Beam |
| SIIT (Chen et al., 2024) | arXiv’24 | Text | **Self-Imp.** | Enc-Dec | Altern. | Multi-task NTP | C-Beam |
| Align3GR (Ye et al., 2026) | AAAI’26 | Text+CF | **Dual RQ** | Dec-Only | Fixed | NTP → DPO | Beam |
| GRLM (Zhang et al., 2026c) | arXiv’26 | Text | **Term-ID** | Dec-Only | Fixed | Multi-task NTP | Beam |
| ★ [DOS](https://arxiv.org/abs/2602.04460) (Yin et al., 2026) | WWW’26 Short | Text+CF | **Orth. RQ** | Dec-Only† | Fixed† | NTP | – |
| ★ [DECOR](https://arxiv.org/abs/2509.10468) (Liu et al., 2026) | SIGIR’26 | Text+CF | RQ-VAE | **Enc-Dec** | Fixed | NTP | Beam |
| LLaDA-Rec (Shi et al., 2025) | arXiv’25 | Text | Par. VQ | **Non-AR** | Fixed | Masked | Diff. |
| ★ [S2GR](https://arxiv.org/abs/2601.18664) (Guo et al., 2026) | KDD’26 | Text+CF | CoBa RQ-VAE | **Enc-Dec** | Fixed | NTP + Ctr. | Beam |
| Latte (Hou et al., 2026) | arXiv’26 | Text+CF | RQ-VAE | **Dec-Only** | Fixed | NTP | C-Beam |
| LC-Rec (Zheng et al., 2024) | ICDE’24 | Text | RQ-VAE | Dec-Only | Fixed | **Multi-task NTP** | Beam |
| ETEGRec (Liu et al., 2025a) | SIGIR’25 | CF | Learn. RQ | Enc-Dec | **Altern.** | NTP + Ctr. | Beam |
| OneRec-Think (Liu et al., 2025b) | arXiv’25 | Text+Img+CF† | R-KM† | Dec-Only | Fixed | **NTP → RL** | CoT |
| GREAM (Hong et al., 2025) | arXiv’25 | Text+CF | RQ-KM | Dec-Only | Fixed | **NTP → RL** | Beam |
| SIDReasoner (He et al., 2026) | KDD’26 | Text | RQ-VAE | Dec-Only | Fixed | **NTP → RL** | C-Beam |
| ★ [Think2Go](https://arxiv.org/abs/2607.28997) (Zhuang et al., 2026) | KDD’26 | Attr+Geo+CF† | RQ-VAE | Dec-Only | Fixed | **NTP → RL** | CoT+Beam |
| PROMISE (Guo et al., 2026) | arXiv’26 | Text | RQ-VAE | Enc-Dec | Fixed† | NTP + Aux. | **PRM-Beam** |
| **IV. Utility** |  |  |  |  |  |  |  |
| RecoChain (Liu and Cao, 2026) | arXiv’26 | Text+Img | RQ | **Dec-Only** | Fixed | NTP + Rank | Hybrid |
| ★ [GFlowGR](https://arxiv.org/abs/2506.16114) (Wang et al., 2026) | SIGIR’26 | Text / Text+CF | RQ-VAE / Learn. RQ | Enc-Dec† | Fixed | **NTP + Aux.** | Beam† / C-Beam† |
| ★ [V-STAR](https://arxiv.org/abs/2602.10699) (Jiang et al., 2026) | KDD’26 | Text† | RQ-VAE | Dec-Only | Fixed | **NTP → RL** | C-Beam |
| GEM-Rec (Jiang et al., 2026) | arXiv’26 | Text | RQ-VAE | Enc-Dec | Fixed | **NTP** | Bid-Aware Beam |
| GenRec-JD (Zou et al., 2026) | SIGIR’26 | Text+Img+CF | RQ-VAE | Dec-Only | Fixed | **NTP → RL** | Beam |
| **V. Efficiency** |  |  |  |  |  |  |  |
| SEATER (Si et al., 2024) | SIGIR-AP’24 | CF | **Tree-Clus.** | Enc-Dec | Fixed | NTP + Ctr. | C-Beam |
| RPG (Hou et al., 2025b) | KDD’25 | Text+Img | Par. OPQ | **Non-AR** | Fixed | MTP | Graph |
| ★ [OneRec-V2](https://arxiv.org/abs/2508.20900) (Zhou et al., 2025) | arXiv’25 | Text+Img+CF† | R-KM† | **Lazy Dec-Only** | Fixed | NTP → RL | Beam |
| STAMP (Zhan et al., 2026) | arXiv’26 | Text | RQ-VAE | **Enc-Dec / Dec-Only** | Fixed | NTP + Aux. | C-Beam |
| ★ [AtSpeed](https://arxiv.org/abs/2410.05165) (Lin et al., 2025) | ICLR’25 | Text | RQ-VAE | Dec-Only | Fixed | NTP | **Spec. Dec.** |
| ★ [NEZHA](https://arxiv.org/abs/2511.18793) (Wang et al., 2026) | WWW’26 Industry | Text | RQ-VAE | Dec-Only | Fixed | NTP | **Self-Draft+Hash** |
| ★ [STATIC](https://arxiv.org/abs/2602.22647) (Su et al., 2026) | KDD’26 ADS | – | RQ-VAE | Dec-Only | Fixed | NTP | **Vec. C-Beam** |
| PAD-Rec (Chen et al., 2026a) | arXiv’26 | Text+SID | RQ-VAE | Dec-Only | Fixed | Multi-task NTP† | **Spec. Dec.** |
| **VI. Generalization** |  |  |  |  |  |  |  |
| ★ [VQ-Rec](https://arxiv.org/abs/2210.12316) (Hou et al., 2023) | WWW’23 | Multi-Dom | **OPQ** | Encoder | Fixed | Discrim. | Scoring |
| UTGRec (Zheng et al., 2025) | arXiv’25 | Multi-Dom | **Tree** | Enc-Dec | Fixed | NTP | Beam |
| GMC (Jin et al., 2025) | arXiv’25 | Cross-Dom | **Unified RQ** | Enc-Dec | Fixed | NTP | C-Beam |
| GenCDR (Hu et al., 2026a) | AAAI’26 | Cross-Dom | **RQ+LoRA** | Dec-Only | Fixed | NTP | C-Beam |
| UniTok (Hou and Shin, 2026) | AAAI’26 | Multi-Dom | **TokenMoE** | Enc-Dec | Fixed | NTP | Beam† |
| MBGR (Li et al., 2026) | arXiv’26 | Text+CF | **RQ** | Dec-Only | Fixed† | NTP + Aux. | C-Beam |
| ★ [DualGR](https://arxiv.org/abs/2511.12518) (Yi et al., 2026) | WWW’26 Short | – | R-KM | **Dec-Only** | Fixed | NTP + Rank | Dual Beam |
| RecBase (Zhou et al., 2025) | EMNLP’25 | Text | Curr. RQ | Dec-Only | Fixed | **NTP** | Beam |
| CausalDPO (Zhao et al., 2026) | ICML’26 | Text | LLM-Vocab | Dec-Only | Fixed | **NTP → DPO** | Scoring |
| ★ [SpecGR](https://arxiv.org/abs/2410.02939) (Ding et al., 2026) | AAAI’26 | Text+SID | RQ-VAE | Enc-Dec | Fixed | NTP + Rank | **Hybrid** |
| LIGER (Yang et al., 2024) | arXiv’24 | Text+SID | RQ-VAE | Enc-Dec | Fixed | NTP + Dense | **Hybrid** |

注：
- 加粗的格是这个方法改动所在的阶段；带是它修的毛病（I–VI）。最上面一块“Paradigms, Systems and Benchmarks”不贴毛病标签：TIGER 是基线；OneRec、PLUM、MiniOneRec 五个阶段一起换，说不出主要修哪个毛病；GRID、FORGE、GR-Generalize 是开源框架、基准和分析论文。
- Tokenizer、Objective 两列由原来的 Training 列拆出（10-26），写法不再沿用综述 Legend。Tokenizer：Fixed = 先建好 SID，训生成器时不再改；Altern. = 编号器和生成器轮流更新；Joint = 生成器的损失直接更新编号器；– = 不构建 SID。Objective 只用 12 种写法：NTP = 只用下一 token 预测损失，从预训练大模型接着训（SFT）也记 NTP；Multi-task NTP = 同一损失训多种任务；NTP + Ctr. / Rank / Dense / Aux. = 另加对比、排序、稠密向量预测或其他辅助损失；NTP → DPO、NTP → RL = 之后再做偏好优化或强化学习（GRPO、GBPO 等）；MTP = 一次并行预测多个码；MTP + Ctr. = MTP 另加对比损失；Masked = 遮蔽部分码再还原（含掩码扩散）；Discrim. = 给物品打分，不生成 SID。
- † 为推定值，原文没有直接写，依据见附录。OneRec-Think 按工业设置推定，公开数据集上的设置原文没有披露；UniTok 的 Inference 按所沿用的 TIGER 推定；DOS 的 Backbone 按 HSTU 原作的因果自回归设置推定；Tokenizer、Objective 两列的推定见“附：改动汇总”的“Training 拆两列”。
- “A / B”表示原文在两个骨干上各做一套：GFlowGR、DiscRec 前为 TIGER、后为 LETTER；TransRec 前为 BART-large、后为 LLaMA-7B；SCRec 前为主实验（仿 RPG 的并行预测头）、后为接到 TIGER 上的版本；STAMP 前为 GRID 框架上的 T5、后为 FORGE 框架上的 Qwen2.5-0.5B；LGSID 前为判别式模型（DIN、TWIN、ETA 等，原文 Table 1）、后为生成式模型（TIGER、OneRec，原文 Table 2）。
- ADC-SID 即原综述的 MMQ-v2：arXiv 2510.25622 自 v3（2026-03-11）起改名，题名改为 Taming the Long Tail: Denoising Collaborative Information for Robust Semantic ID Generation。综述 bib（`MMQ-v2`）用的是 v1 题名，写正文时按 v3 改。
- “–”在本轮新增行里表示原文没有报告这一环节（DualGR、STATIC 的 Representation，MMQ、GNPR-SID、Gwhere、DOS 的 Inference），不是推定为空。
- Venue 后的 Short、Industry、ADS 是录用的 track（WWW 短文、WWW 工业、KDD Applied Data Science），不是 research full paper。
- 新写法：Bid-Aware Beam = 按实时出价调整 logits 后做束搜索（GEM-Rec）；CoBa RQ-VAE = 融入物品共现协同信号、带码本均匀和负载均衡约束的 RQ-VAE（S2GR）。本轮新增行的新写法（Self-Sup. ID、Bal. VQ+KM、Dual Beam、Vec. C-Beam、Self-Draft+Hash、HeterRec、Shared/Spec. RQ、Lazy Dec-Only、Align. RQ、QA-RQ、Spectral Clus.、Multi-Facet ID、FM-Index+Agg.、Graph RQ-VAE）的含义写在“附：★ 方法的依据”各行备注。理由见“附：改动汇总”和“附：★ 方法的依据”。
- POI 10 行（9 行 10-28 加入，DOS 10-30 加入）：五列依据和新写法的含义见 `Table2_按仓库分类.md`“附：POI 的五列依据”；Tokenizer、Objective 的依据见“附：改动汇总”的“Training 拆两列”。Representation 里的 Geo 指地理信号（经纬度、区域编码、地址等）；Backbone 的 Disc. 指 SID 只作 DIN 等判别式推荐模型的特征。
  - GeoGR 的 Altern.†：交替发生在构码阶段，EM 算法里 LLM 和 SID 轮流更新（§4.1.3，Algorithm 1，p5）；最终的生成器从基座重新训练，训练时 SID 已经定好（§4.2.1，p5）。
  - Gwhere 的 NTP → DPO：EAKTO 是 KTO 的变体，属于偏好优化；继续预训练里另有遮蔽 SID 预测和 SID–属性匹配判别两个辅助任务（§3.3.1，p4），12 种写法里没有对应的组合。
  - ROS 的 CoT+C-Beam：主实验只报 HR@1，只用 CoT；C-Beam 只用在 Top-K 扩展实验（“Top-K Recommendation via Two-Stage Inference”，p7）。
  - DOS 的 Orth. RQ 指 Orthogonal Residual Quantization（ORQ），即正交变换、任务相关维度选择与逐层残差量化（§2.2，p2–3）。Backbone 和 Objective 取 HSTU 生成实验（§3.2.2，Table 2，p4）；原文未交代 HSTU 架构细节及其训练时是否更新编号器，分别记 Dec-Only†、Fixed†；编号器内部的联合损失不等于生成器联合更新。

## 附：毛病与阶段的依据（10-25）

六类的英文类名和通栏问句（10-26 本人定）。出处只取原始顶会论文和 TKDE、TOIS 高引综述；HKBU、Tri-Decoupled 是预印本，只拿来对照叫法。

| 类 | 英文类名 | 通栏问句 | 出处 |
| --- | --- | --- | --- |
| I 信息不够 | Informativeness | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | 借自表示学习：DCI-ES（ICLR 2023，§2）沿用 Eastwood & Williams（ICLR 2018）的 informativeness，指从表示里能预测出关键因素的程度；2018 年原文没下载到 |
| II 编号和物品对不上 | Uniqueness and Validity | Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? | TIGER（NeurIPS 2023，arXiv 版）p5“Handling Collisions … to make them unique”，p10“Invalid IDs (i.e., IDs that do not map to any item…)”；GENRE（ICLR 2021）p4“only decode valid entity identifiers” |
| III 模型读不懂、写不好编号 | SID–Model Alignment | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | LC-Rec（ICDE 2024）摘要“a large semantic gap between LLMs and recommender systems”，对策叫 alignment tuning；ETEGRec（SIGIR 2025）的 sequence-item alignment 和 preference-semantic alignment |
| IV 目标没对准 | Utility | Are training and search aimed at what users and the platform value, rather than at token likelihood? | Adomavicius & Tuzhilin（TKDE 2005）§2 式 (1)，pp. 734–735：效用函数 u 衡量“the usefulness of item s to user c” |
| V 太慢太贵 | Efficiency | Can it be trained and served within latency and cost budgets? | Lin et al.（TOIS 2025）§5.1 “Training Efficiency”、§5.2 “Inference Latency” |
| VI 环境一变就失灵 | Generalization | Does it still work for new items, new domains, and shifting interests? | Wang et al. 的领域泛化综述（TKDE，2022 年在线发表）摘要“generalize to unseen distributions”；TIGER 摘要也用 generalize 说没有交互记录的新物品 |

最上面一块叫 Paradigms, Systems and Benchmarks，不贴毛病标签。

判定规则（10-25 本人同意）：

- 毛病：看摘要里明说、且论文为它加了新设计的抱怨（“新”相对于它所基于的方法），多条时取多数。
- 一比一打平时依次看：新设计多数在修哪条；题目点名的是哪条；第一件新设计修的是哪条。
- 先照摘要里的抱怨定；抱怨落不进六类时，才看新设计补的是什么。
- IV：抱怨训练目标本身有缺陷就算，不必明写“目标不对”；光用强化学习不算。
- 整体新范式、开源框架、基准和分析论文不贴毛病标签，和 TIGER 一起放进最上面一块。
- 同一组作者先后挂出、设计重叠的论文只留最新最完整的一篇：DeepContextGR（2604.20861）、DeepInterestGR（2602.18907）并入 TriAlignGR（2605.05249），正文里作为早期版本引用。
- 阶段：看新设计的组件装在哪；几处时取对付该毛病的那一处；仍分不出，取贡献列表第一条。

引文出自 arXiv 摘要（ADC-SID 即 MMQ-v2 的 API 摘要截断）；少数阶段判断读了引言的贡献列表，已注明。

### 原来拿不准的 32 篇（10-25 按补充规则定）

| 方法 | 候选 | 定为 | 依据的规则 | 理由 |
| --- | --- | --- | --- | --- |
| SEATER | V / III | V × Tokenization | 先看抱怨 | 摘要只说前人 "fall short in efficiency and effectiveness"：efficiency 对应平衡树（V），effectiveness 落不进六类；两项对比任务学的是标识 token 的层级语义（偏 III） |
| TokenRec | I / VI / V | I × Tokenization | 打平：第一件设计 | MQ tokenizer 同时对付 I、VI，检索范式对付 V，设计数打平；题目 "Learning to Tokenize ID" 点的也是 tokenizer；tokenizer 先写的作用是 "incorporation of high-order collaborative knowledge"（I） |
| HiD-VAE | I / II | II × Tokenization | 打平：多数设计 | 两条抱怨一比一："lacking a coherent hierarchy"（层级监督引入了标签信息，偏 I）和 "ID collisions"（II）；层级监督也写了 "yielding more uniform and disentangled IDs"，两件设计都服务 II，建议 II |
| GRLM | II / III | III × Tokenization | 打平：多数设计 | 两条抱怨一比一：文本 ID "leading to hallucination"（II）和 SID 的 "semantic gap between SIDs and LLMs' native vocabulary"（III）；Context-aware Term Generation 和 Integrative Instruction Fine-tuning 都为贴近 LLM 词表（III），只有 Elastic Identifier Grounding 管映射（II） |
| R3-VAE | II / V | II × Tokenization | 打平：多数设计 | 两条抱怨一比一："training instability"（新设计写明 "prevent codebook collapse"，II）和 "costly GR training and A/B testing" 的评估成本（V）；前者是方法主体，建议 II |
| GRID | 无对应类 | 上面一块 | 范式、系统与基准 | 摘要抱怨的是 "the absence of an open-source, unified framework"，属于开源框架和基准，六类都套不上；可作跨阶段章里公平对照的证据 |
| DIGER | III / II | II × Tokenization | 打平：多数设计 | 两条抱怨一比一："objective mismatch"（III）和 "codebook collapse"（II）。摘要称可微化是 "A natural approach"，不是本文的新设计；本文新加的 Gumbel 噪声和两种不确定性衰减都为缓解码本塌缩，按多数设计归 II（初标建议 III） |
| DualGR | I / III / VI | VI × Backbone | 打平：题目 | 三条抱怨各一件设计，打平；题目 "Long and Short-Term Interests Modeling" 点名 "long-short interest interference"，按“口味变化算 VI”归 VI；对付它的 DBR 装在 Backbone（初标建议 I × Training） |
| CID | II / I | II × Tokenization | 先看抱怨 | 摘要的抱怨是 "hallucinated recommendations" 和要 "uniquely identify each item"（II）；但本文提出的 CID 实际是把协同信号写进 ID（I），摘要没说前人缺 CF |
| MQL4GRec | I / VI | I × Tokenization | 先看抱怨 | 明说的抱怨是 "rarely consider the complementary knowledge between the multimodal information"（I）和 PLM 通用知识与推荐需求不符（落不进六类）；全文目标是跨域、跨模态的 "recommendation knowledge transfer"，也可归 VI |
| GenCDR | VI / I | VI × Tokenization | 打平：多数设计 | 两条抱怨："item ID tokenization dilemma"（含 "fails to capture high-order collaborative knowledge"，偏 I）和 "insufficient domain-specific modeling"（VI）；全文是跨域推荐，建议 VI |
| FORGE | V / 无对应类 | 上面一块 | 范式、系统与基准 | 两条抱怨里只有 "SID assessment typically relies on costly GR training" 落进 V；主体是 SID 构造的基准和免训练评估指标，同 GRID 归基准 |
| MME-SID | I / III | I × Tokenization | 打平：第一件设计 | 两条抱怨一比一："embedding collapse"（融入多模态嵌入来缓解，I）和 "catastrophic forgetting of quantized embeddings"（用码嵌入初始化 LLM 来缓解，III），设计数打平；题目 "Multimodal Embeddings and Semantic IDs" 两条都点到；第一件设计是融入多模态嵌入（I） |
| CARD | I / II | II × Tokenization | 打平：题目 | 两条抱怨一比一："insufficient supervision for heterogeneous fusion"（I，视觉语义单元，装在 Representation）和 "codeword imbalance"（II，NU-RQ-VAE，装在 Tokenization）；题名是 Non-Uniform Quantization，建议 II；若归 I 则阶段改为 Representation |
| MMGRec | I / V | I × Tokenization | 抱怨落不进六类，看设计 | 摘要抱怨的是嵌入检索范式的 "inference cost, interaction modeling, and false-negative issues"，不是 SID 方法的毛病；相对 TIGER 的新设计主要是把多模态和 CF 写进 Rec-ID，建议 I |
| OneRec | 无对应类 / IV | 上面一块 | 范式、系统与基准 | 摘要只抱怨级联框架 "the generative model functions only as a selector during the retrieval stage"；编码器—解码器、session-wise 生成和偏好对齐一起换，说不出主要修哪个毛病 |
| Align3GR | III / I | III × Tokenization | 先看抱怨 | 抱怨只有一条 "semantic and behavioral misalignment"（LLM 与推荐的鸿沟，III）；但第一件设计 "Dual tokenization fusing user-item semantic and collaborative signals" 补了 CF 信息，按“补信息算 I”也可归 I |
| MiniOneRec | 无对应类 / III / IV | 上面一块 | 范式、系统与基准 | 摘要只问 scaling law 是否成立和最小后训练配方，是开源的完整系统，没有对应六类的抱怨 |
| OneRec-Think | 无对应类 / III | III × Training | 缺推理不单开一类 | 抱怨是 "lacking the capacity for explicit and controllable reasoning"；“缺推理”不单开一类，itemic alignment 和推理训练都是让模型学懂、用好编号（III），都装在 Training |
| LIGER | VI / 无对应类 | VI × Inference | 抱怨落不进六类，看设计 | 摘要的抱怨是缺少 "a comprehensive comparison"，冷启动只作为效果出现在 "enhancing cold-start item recommendation"；正文的动机是冷启动，按此建议 VI |
| RecoChain | IV / III | IV × Backbone | IV 门槛 | 抱怨 "hard to estimate which items are better from them ... leading to a gap between generation and ranking performance"，是似然和排序不一致，符合 IV 的定义，但摘要没有直接说“目标不对”；阶段也可记 Inference（推理时先生成再排序） |
| MBGR | VI / II | VI × Tokenization | 先看抱怨 | 两条抱怨都来自多业务场景："seesaw phenomenon in multi-business scenarios" 和统一 SID 空间的 "representation confusion"；多业务按跨域算 VI，后一条也可看作不同业务挤在同一编号空间（II） |
| GR-Generalize | 无对应类 / VI | 上面一块 | 范式、系统与基准 | 抱怨的是缺少验证泛化假设的方法，属于分析论文；附带的 indicator 只是按样本组合两种范式 |
| GenRec-JD | IV / V | IV × Training | IV 门槛 | 三条挑战：分页导致 "inconsistent outputs"（Page-wise NTP 解决 point-wise 训练的一对多歧义，按 IV 门槛算 IV）、"the prohibitive cost of encoding long user behavior sequences"（V）、"aligning the generative policy with nuanced user preference signals"（IV）；三条里两条是 IV，取多数 |
| MSCGRec | I / 无对应类 | I × Tokenization | 抱怨落不进六类，看设计 | 摘要的抱怨只是在大物品集上 "have yet to surpass traditional sequential recommenders"，没说缺什么；但设计都是在补多模态和 CF 信息，题名是 Fusing Semantic and Collaborative Signals |
| TriAlignGR | I / III | I × Representation | 打平：多数设计 | 两条抱怨一比一：SCD 是量化 "discard critical multimodal and interest-level semantics"（I）；SSO 是模型 "without truly comprehending their underlying meaning"（III）；三件设计里两件对付 SCD，建议 I |
| GFlowGR | IV / 无对应类 | IV × Training | IV 门槛 | 抱怨的是 SFT 和 DPO 两种微调目标都忽略未观测正样本（exposure bias），指的是训练目标的缺陷，但摘要没有直接写“似然与奖励不一致” |
| S2GR | III / 无对应类 | III × Backbone | 先看抱怨 | 总体抱怨是 "failing to activate deeper reasoning capabilities"，属于“缺推理”；第一条具体抱怨是推理与生成分离造成 "imbalanced computational focus across hierarchical SID codes, degrading quality for SID codes"，即模型写不好 SID（III） |
| PLUM | 无对应类 / III | 上面一块 | 范式、系统与基准 | 摘要没有抱怨前人，只介绍让预训练 LLM 适应工业推荐的完整框架：SID、继续预训练、生成检索微调 |
| OneRec-V2 | V / IV | V × Backbone | 打平：第一件设计 | 两条抱怨一比一："97.66% of resources are consumed by sequence encoding"（V，Lazy Decoder-Only）和 "reinforcement learning relying solely on reward models"（IV，真实反馈对齐）；Lazy Decoder-Only 排第一，建议 V；若归 IV 则阶段改为 Training |
| DECOR | I / III | III × Backbone | 打平：第一件设计 | 总的抱怨是两阶段 "objective misalignment"（III）；两条具体抱怨 "suboptimal static tokenization"（III）和 "discarded pretrained semantics"（I）各一件设计，打平；题目 "Decomposed Contextual" 两件都点到；第一件 contextualized token composition 修的是静态分词（III）（初标建议 I） |
| DiscRec | I / III | I × Backbone | 打平：题目 | 两条抱怨一比一："token-item misalignment"（模型读不出 SID 的物品结构，III）和 "semantic-collaborative signal entanglement"（信号融合不当，I）；题名强调 Disentangled Semantic-Collaborative，建议 I |

### 逐篇依据

| 方法 | 毛病 | 阶段 | 依据 |
| --- | --- | --- | --- |
| IDGenRec | III | Tokenization | 摘要：“struggles to effectively encode recommendation items within the text-to-text framework”。新设计是与 LLM 推荐器一起训练的文本 ID 生成器，装在 Tokenization（已定例子） |
| SEATER | V | Tokenization | 摘要：“these methods fall short in efficiency and effectiveness for large-scale recommendations”。新设计是平衡 k 叉树标识（"maintains consistent and fast inference speed"），装在 Tokenization；另有两项对比学习任务 |
| CoST | I | Tokenization | 摘要：“fails to capture the essential neighborhood relationships”。新设计是对比量化，把物品邻域关系写进码，装在 Tokenization |
| ActionPiece | I | Tokenization | 摘要：“without considering contextual relationships”。新设计是按上下文合并特征的分词词表，装在 Tokenization |
| ETEGRec | III | Training | 摘要：“treat item tokenization and generative recommendation training as separate processes”。新设计是两项对齐目标加交替优化，装在 Training（已定例子） |
| TokenRec | I | Tokenization | 摘要：“challenges remain in efficiently capturing high-order collaborative knowledge into discrete tokens”；“difficulties in generalizing effectively to new/unseen users or items”。新设计是 Masked VQ tokenizer（同时对付前两条）和免逐码解码的检索范式 |
| RecBase | VI | Training | 摘要：“cross-domain generalization is hindered by a fundamental mismatch between language-centric pretraining and the recommendation task”。新设计是用推荐目标在跨域语料上预训练（"pretrained with a recommendation-oriented objective"），装在 Training；统一 tokenizer 是 "further" 的辅助件 |
| HiD-VAE | II | Tokenization | 摘要：“semantically flat and uninterpretable, lacking a coherent hierarchy”；“prone to representation entanglement (i.e., ``ID collisions'')”。新设计是用多级标签监督的量化和 uniqueness loss，都装在 Tokenization |
| PSI | II | Tokenization | 摘要：“suffer from semantic ID conflicts”。新设计是放宽最近质心分配的 ECM、RRS，装在 Tokenization |
| SIIT | III | Tokenization | 摘要：“may not align with the LLM's internal pretrained tokenization schema”。新设计是训练中由 LLM 周期性修正物品的分词结果，装在 Tokenization |
| COBRA | I | Backbone | 摘要：“significant information loss due to the separation of stages such as quantization and sequence modeling”。量化丢信息按 UNGER 先例归 I；新设计是先生成稀疏 ID、再生成稠密向量的级联生成，装在 Backbone |
| GRLM | III | Tokenization | 摘要：“Text-based methods introduce LLMs' vast output space, leading to hallucination”；“encounter a semantic gap between SIDs and LLMs' native vocabulary”。新设计是 Term ID，装在 Tokenization；另有指令微调和 Elastic Identifier Grounding |
| R3-VAE | II | Tokenization | 摘要：“training instability, stemming from insufficient gradient propagation”；“inefficient SID quality assessment, where industrial practice still depends on costly GR training and A/B testing”。新设计是参考向量、打分式量化（"prevent codebook collapse"）和两个 SID 评估指标，都装在 Tokenization |
| Latte | III | Backbone | 摘要：“making it difficult to distinguish among them based on user-specific preferences”。自回归 SID 生成的树结构让模型表达不了简单模式，没有补信息；新设计是在每个 SID 前插入潜在 token，SID 本身不变，装在 Backbone |
| CapsID | I | Tokenization | 摘要：“collapses multi-faceted item semantics at cluster boundaries”。量化丢信息归 I；新设计是胶囊路由替代硬残差量化，装在 Tokenization |
| STAMP | V | Backbone | 摘要：“prohibitive training overhead due to sequence expansion”。另一条 "unstable performance reliability" 落不进六类；新设计 SAP 在前向中剪掉冗余 token，装在 Backbone（该格原为 –），MAP 是辅助多步目标 |
| GRID | — | — | 摘要：“the absence of an open-source, unified framework hinders systematic benchmarking and extension”。开源框架和系统消融，没有针对六类毛病的新设计；结论落在 "overlooked architectural components"，暂标 Backbone |
| DIGER | II | Tokenization | 摘要：“This leads to an objective mismatch”；“this often causes codebook collapse, where only a few codes are used”。新设计是可微 SID 加 Gumbel 噪声和不确定性衰减，装在 Tokenization |
| LMIndexer | I | Tokenization | 摘要：“each step introduces potential information loss”。两步流程丢信息归 I；新设计是自监督的语义索引器，装在 Tokenization |
| MBGen | I | Training | 摘要：“neglecting the value of integrating the target behavior type into the learning objective”。缺行为类型信号归 I；贡献第一条是 "integrate target behavior types into the learning objective"（引言），即交替生成行为 token 和物品 token 的统一 NTP 目标，记 Training；按位置路由的稀疏结构（Backbone）是为扩容 |
| DualGR | VI | Backbone | 摘要：“long-short interest interference, context-induced noise in hierarchical SID generation, and the lack of explicit learning from exposed-but-unclicked feedback”。三条抱怨对应三件设计：DBR（Backbone）、S2D（Inference）、ENTP-Loss（Training） |
| STATIC | V | Inference | 摘要：“incur severe latency penalties on hardware accelerators (TPUs/GPUs)”。新设计是把前缀树展平为 CSR 矩阵的向量化约束解码，装在 Inference |
| CID | II | Tokenization | 摘要：“To avoid generating excessively long text and hallucinated recommendations”；“creating LLM-compatible item IDs to uniquely identify each item is essential”。新设计是协同、语义、混合等索引方式（表内记共现图谱聚类），装在 Tokenization |
| TransRec | II | Tokenization | 摘要：“either lose semantics or lack adequate distinctiveness”；“might generate invalid identifiers”。第一条贡献是 multi-facet identifiers，装在 Tokenization（已定例子） |
| MQL4GRec | I | Tokenization | 摘要：“rarely consider the complementary knowledge between the multimodal information of items”。新设计是把文本、图像量化成共享词表的 quantitative translator，装在 Tokenization；另有生成任务和预训练迁移 |
| RPG | V | Backbone | 摘要：“they often suffer from inefficient inference due to the reliance on resource-intensive beam search”。贡献是并行生成长 SID，记 Backbone（已定例子） |
| LLaDA-Rec | III | Backbone | 摘要：“error accumulation, where the fixed left-to-right generation order causes prediction errors in early tokens to propagate”。另一条 "unidirectional constraints" 也是模型读写 SID 的问题，没有补信息；新设计是离散扩散生成，装在 Backbone |
| GenCDR | VI | Tokenization | 摘要：“item ID tokenization dilemma”；“insufficient domain-specific modeling”。新设计是 Domain-adaptive Tokenization（第一件），另有跨域自回归模块和域感知前缀树 |
| MACRec | I | Tokenization | 摘要：“remain limited in their ability to harness multimodal information”。新设计是跨模态量化（第一件，顺带降低冲突率），装在 Tokenization |
| GMC | VI | Tokenization | 摘要：“may be unavailable in non-overlapped recommendation scenarios”。跨域归 VI；新设计是带域感知对比损失的域共享 SID，装在 Tokenization |
| UTGRec | VI | Tokenization | 摘要：“typically domain-specific, limiting their ability for effective transfer or adaptation to new domains”。新设计是基于 MLLM 的通用 tokenizer，装在 Tokenization |
| UniTok | VI | Tokenization | 摘要：“require training separate models for each item domain, limiting generalization”。新设计是 MoE 统一 tokenizer，装在 Tokenization |
| ADC-SID | I | Tokenization | 摘要：“leading to the loss of critical multimodal information”。长尾物品的协同噪声污染内容表示归 I；新设计是自适应行为—内容对齐和行为 SID 动态加权，装在 Tokenization（arXiv 摘要截断，按可见部分判） |
| FORGE | — | — | 摘要：“their SID assessment typically relies on costly GR training”。新设计是 SID 构造的基准和两个免训练评估指标，归 SID 构造，记 Tokenization |
| MME-SID | I | Tokenization | 摘要：“embedding collapse when incorporating pre-trained collaborative embeddings”；“catastrophic forgetting of quantized embeddings when utilizing semantic IDs”。新设计是融入多模态嵌入、MM-RQ-VAE、用码嵌入初始化 LLM 和 LoRA 融合 |
| PAD-Rec | V | Inference | 摘要：“decoding remains sequential and thus latency-prone”。新设计是给草稿模型加位置感知信号的投机解码，装在 Inference |
| CARD | II | Tokenization | 摘要：“provides insufficient supervision for heterogeneous fusion”；“non-uniform embeddings lead to codeword imbalance and generation bias”。新设计是视觉语义单元（Representation）和 NU-RQ-VAE（Tokenization） |
| AdaSID | II | Tokenization | 摘要：“effective SID learning is hindered by collisions”。新设计是自适应地调节 SID 重叠，装在 Tokenization |
| SynGR | I | Training | 摘要：“underexplore synergistic information across modalities”。新设计是训练时按显著性遮蔽占优模态（引言 p2 "saliency-aware masking mechanism"），装在 Training |
| PSRQ | I | Tokenization | 摘要：“intra-modal semantic degradation”；“inter-modal modeling gaps”。两条都是信息丢失或融合不足，归 I；PSRQ（Tokenization）和 MCCA（Backbone）各对付一条，取贡献第一条 PSRQ，记 Tokenization |
| Q-BERT4Rec | I | Representation | 摘要：“rely on discrete item IDs that lack semantic meaning and ignore rich multimodal information”。新设计第一步是融合文本、视觉、结构特征的 cross-modal semantic injection，装在 Representation |
| AtSpeed | V | Inference | 摘要：“excessive inference latency caused by autoregressive decoding”。新设计是 top-K 对齐的投机解码，记 Inference（已定例子） |
| NEZHA | V | Inference | 摘要：“severely hindered by high inference latency”。新设计是自起草头加 hash 校验，表内记在 Inference |
| MMQ | I | Tokenization | 摘要：“balancing cross-modal synergy with modality-specific uniqueness”；“bridging the semantic-behavioral gap”。新设计是共享与专用专家的多模态 tokenizer 和行为感知微调，装在 Tokenization |
| GenSAR | I | Tokenization | 摘要：“integrating both semantic and collaborative signals into item representations”。另一条“区分搜索和推荐的需求”落不进六类；新设计是双用途标识（共享加专用码本），装在 Tokenization |
| MMGRec | I | Tokenization | 摘要：“this paradigm suffers from inference cost, interaction modeling, and false-negative issues”。新设计是从 "multimodal and CF information" 生成 Rec-ID 的 Graph RQ-VAE，另有关系感知自注意力 |
| VQ-Rec | VI | Tokenization | 摘要：“exaggerating the negative impact of domain gap”。新设计是 text → code → representation 的物品表示，装在 Tokenization |
| LC-Rec | III | Training | 摘要：“there exists a large semantic gap between LLMs and recommender systems”。对付语义鸿沟的是 alignment tuning 任务，装在 Training；索引的作用是 "non-conflicting IDs" |
| EAGER | I | Backbone | 摘要：“focus solely on either behavioral or semantic aspects of item information”。新设计是双流生成结构，记 Backbone（已定例子） |
| ColaRec | I | Backbone | 摘要：“How to integrate content knowledge and collaborative interaction signals in a generative framework tailored for item recommendation is still an open research challenge”。新设计是 CF 构造的 GID 加内容聚合的用户输入；贡献第一条是 "an encoder-decoder model to jointly capture content information and collaborative signals"（引言），记 Backbone；备选 Tokenization（GID 由预训练 CF 模型构造） |
| LETTER | I | Tokenization | 摘要：“shortcomings in encoding semantic information, incorporating collaborative signals, or handling code assignment bias”。记 Tokenization（已定例子） |
| GRAM | I | Tokenization | 摘要：“(i) incorporating implicit item relationships and (ii) utilizing rich yet lengthy item information”。两条都归 I；semantic-to-lexical translation（Tokenization）排第一，late fusion 在 Backbone，取第一条 |
| DAS | I | Tokenization | 摘要：“their lack of collaborative signals results in a misalignment”；“inevitable information loss during alignment”。新设计是一阶段同时做量化和对齐的 dual-aligned SID，装在 Tokenization |
| OneRec | — | — | 摘要：“the generative model functions only as a selector during the retrieval stage”。摘要抱怨的是级联框架；新设计是 MoE 编解码器、session-wise 生成和 DPO 偏好对齐 |
| Align3GR | III | Tokenization | 摘要：“fundamental challenges arise when transforming LLMs into real-world recommender systems due to semantic and behavioral misalignment”。三级对齐的第一件是双路 tokenization，装在 Tokenization |
| CausalDPO | VI | Training | 摘要：“significantly undermining the generalization capability of LLM-based generative recommendation methods in out of distribution (OOD) scenarios”。新设计是带因果不变性约束的 DPO，装在 Training |
| GREAM | III | Training | 摘要：“the intrinsic modeling gap between textual semantics and collaborative filtering signals”。另一条 "sparsity and stochasticity of user feedback" 由 SRPO 稳定训练，没说目标不对；三件设计里对齐任务、推理课程和 SRPO 都在 Training |
| MiniOneRec | — | — | 摘要：“most industrial deployments remain proprietary”。开源框架；新设计是后训练的 "full-process SID alignment" 和带约束解码与混合奖励的 RL，装在 Training |
| OneRec-Think | III | Training | 摘要：“critically lacking the capacity for explicit and controllable reasoning”。新设计是 itemic alignment、推理激活和推荐专用奖励，都在 Training |
| PROMISE | III | Inference | 摘要：“errors in early, high-level tokens irreversibly divert the generation trajectory”。新设计是 PRM 引导束搜索，记 Inference（已定例子） |
| LIGER | VI | Inference | 摘要：“mitigating performance differences and enhancing cold-start item recommendation”。新设计是把稠密检索并入生成检索，推理时混合两路候选，记 Inference |
| RecoChain | IV | Backbone | 摘要：“leading to a gap between generation and ranking performance”。新设计是让同一个 Transformer 同时产出候选和排序分，贡献第一条 "a single generative model to serve both candidate generation and ranking score estimation"（引言），记 Backbone |
| MBGR | VI | Tokenization | 摘要：“a seesaw phenomenon in multi-business scenarios”；“a unified SID space causes”。新设计 BID（Tokenization）、MBP（Backbone）、LDR（Training），取第一件 BID |
| GEM-Rec | IV | Training | 摘要：“do not address concerns such as monetization via ad revenue and incorporation of bids”。广告收益归 IV；控制 token 和 Bid-Aware Decoding 都对付收益，按贡献第一条 "integrates explicit control tokens into the Semantic ID vocabulary"（引言）记 Training（表内 E2E (Ctrl. Tok.)）；按出价解码在 Inference |
| GR-Generalize | — | — | 摘要：“there is few systematic way to verify this hypothesis”。分析论文；新设计只有按样本混合 GR 与 ID 模型的 memorization-aware indicator，记 Inference |
| SIDReasoner | III | Training | 摘要：“Itemic tokens are not natively meaningful to LLMs”。新设计是 SID—语言对齐的多任务训练和结果驱动的 RL，装在 Training |
| UniRec | I | Tokenization | 摘要：“GR decodes over compact SID tokens without item-side signal”。新设计 Chain-of-Attribute 在 SID 前加属性 token，改的是物品标识序列，记 Tokenization；RFT+DPO 的 "business objectives" 只是次要一件 |
| GenRec-JD | IV | Training | 摘要：“aligning the generative policy with nuanced user preference signals”。三件设计：Page-wise NTP（Training）、Token Merger（prefill 压缩）、GRPO-SR（Training） |
| MSCGRec | I | Tokenization | 摘要：“these methods have yet to surpass traditional sequential recommenders on large item sets”。新设计是多语义模态、基于 DINO 的图像量化、把 CF 当作单独模态，装在 Tokenization；另有约束序列学习 |
| Molar | I | Representation | 摘要：“inherently lack collaborative filtering information, relying primarily on textual content data neglecting other modalities”。新设计第一件是用 MLLM 生成统一物品表示，装在 Representation；CF 后对齐在 Training |
| TriAlignGR | I | Representation | 摘要：“SID Content Degradation (SCD)”；“SID Semantic Opacity (SSO)”。新设计 CMSA、MDIM 在量化前补信息（Representation），TMT 多任务训练（Training） |
| GFlowGR | IV | Training | 摘要：“Both methods ignore the exploration of possible positive unobserved samples, which is commonly referred to as the exposure bias problem”。新设计是基于 GFlowNet 的微调框架，装在 Training |
| S2GR | III | Backbone | 摘要：“degrading quality for SID codes”。新设计是在每个 SID 码前插入思考 token 的逐步推理，装在 Backbone；码本优化（Tokenization）是基础件 |
| V-STAR | IV | Training | 摘要：“fine-tuning these models with Reinforcement Learning (RL) often suffers from a fundamental probability-reward mismatch”。明说概率与奖励不一致，进 IV；VED 为 RL 构造候选、Sibling-GRPO 改优势计算，都服务训练，测试时默认用标准束搜索，记 Training |
| PLUM | — | — | 摘要：“a framework designed to adapt pre-trained LLMs for industry-scale recommendation tasks”。新设计是 SID、继续预训练和生成检索微调，核心是 CPT，装在 Training |
| OneRec-V2 | V | Backbone | 摘要：“inefficient computational allocation where 97.66% of resources are consumed by sequence encoding rather than generation”；“limitations in reinforcement learning relying solely on reward models”。新设计 Lazy Decoder-Only（Backbone）和基于真实反馈的偏好对齐（Training） |
| EAGER-LLM | I | Tokenization | 摘要：“poor integration of traditional RS features”。补的是外生的行为与语义信号，按“补信息算 I”归 I；对付它的是 "dual-source knowledge-rich item indices"，装在 Tokenization |
| SemConv | III | Tokenization | 摘要：“a notable discrepancy persists between the sparse collaborative semantics typically found in recommendation systems and the dense token representations within LLMs”。没有补新信息；Alignment Tokenization（第一件，Tokenization）和对齐任务（Training）都对付这条，取第一件 |
| QuaSID | II | Tokenization | 摘要：“Collision problem”。摘要只抱怨撞号，CF 目标不是抱怨，记 Tokenization（已定例子） |
| DECOR | III | Backbone | 摘要：“suboptimal static tokenization”；“discarded pretrained semantics”。新设计是上下文化的 token 组合和分解嵌入融合，都在生成器的 token 嵌入层，装在 Backbone |
| DiscRec | I | Backbone | 摘要：“token-item misalignment”；“semantic-collaborative signal entanglement”。新设计是物品级位置嵌入和双分支解耦，都装在生成器嵌入层，记 Backbone |
| SCRec | I | Representation | 摘要：“item tokenization is largely dominated by textual semantics with limited incorporation of collaborative signals”；“the generation stage tends to overlook the original semantic information”。第一件 collaborative-enhanced tokenization 把协同邻居写成文本、编码后再量化，改的是量化输入，装在 Representation |
| SpecGR | VI | Inference | 摘要：“struggle to recommend unseen items”。新设计是起草器提候选、GR 验证，装在 Inference |
| GNPR-SID | I | Tokenization | 摘要（p1）：“employ random numeric IDs for POIs, limiting the ability to model semantic relationships between similar locations”。新设计是用语义和协同特征量化得到 POI 的 SID（贡献第 2 条，p2；§4.1，p3–5），装在 Tokenization；diversity loss 只为让 SID 分布均匀，摘要没把撞号写成前人的毛病，不取 II |
| GeoGR | I | Representation | 摘要（p1）：“inadequate modeling of high-quality SIDs that capture cross-category spatio-temporal collaborative relationships”；“poor alignment between large language models (LLMs) and the POI recommendation task”。两条一比一（I、III），新设计数也打平，题目 “Enabling Spatio-Temporal Aware …” 点的是 I，取 I。修 I 的是地理约束共访对上的对比表示学习 L_P2P（式 (4)，p4），装在 Representation；EM 式 SID 修正（Algorithm 1，p5）和继续预训练偏 III |
| Gwhere | II | Tokenization | 摘要（p1）：“redundant or colliding token assignments”；“insufficient integration of heterogeneous item signals”。两条一比一（II、I），都由全对比 RQ tokenizer 对付；去掉重构损失、改用对比损失是为区分物品（§3.2，p3），结论也写 “alleviate code collision”（p8），按多数设计取 II（两家都拿不准，备选 I）。装在 Tokenization |
| LGRID | I | Representation | 摘要（p1）：“semantic entanglement … causing key attributes to be insufficiently preserved during quantization, degrading SID quality, and leading to severe SID collisions”。主语是地理、品牌、类别等关键属性没保住，撞号是后果，归 I；另一条可解释性落不进六类。新设计 SD-Block 和 Synergistic Alignment 作用在 LLM 隐状态上、量化之前（§3，Fig. 2，p3），装在 Representation |
| LGSID | I | Representation | 摘要（p1）：“simply injecting location information into prompts fails to capture fine-grained spatial characteristics and real-world distance awareness among items”。RL 地理对齐和层次地理分词两件设计都修这一条，分不出，取贡献列表第一条：对齐编码物品的 LLM（p2；G-DPO，p4），装在 Representation |
| OneLoc | I | Representation | 摘要（p1）：“how to make full use of geographic information”；“how to balance multiple objectives, including user interests, the distance between user and stores, and some other business objectives”。两条一比一（I、IV）；修 I 的三件（geo-aware SID、编码器里的 geo-aware self-attention、解码器里的 neighbor-aware prompt）多于修 IV 的两件奖励，取 I。抱怨落得进六类，所以不放最上面一块（OneRec 放进去，是因为它只抱怨级联框架）。三件分装在 Representation 和 Backbone，取贡献列表第一条 geo-aware SID（p3）：沿用 OneRec 的 res-kmeans，改动只在输入嵌入里加位置上下文（§2.2，p3），装在 Representation |
| ProGEO | I | Tokenization | 摘要（p1）：“existing semantic codebooks neglect geographic constraints, often resulting in recommendations that are semantically relevant yet geographically unreachable”。地理上不可达不是 II 说的“生成的 SID 不对应真实物品”，归 I。新设计 geo-centroid 局部坐标和 GEO-RoPE 都作用在第三层地理码本上（Fig. 2，p3；§3，p3–4），装在 Tokenization |
| ROS | I | Tokenization | 摘要（p1）：“existing LLM-based recommenders remain limited in leveraging geographic signals”。抱怨对象是地理信号，取 I；备选 III（引言把缺口收窄为没用推理能力处理地理，p1）。Hierarchical Spatial SID、Mobility CoT、spatial-guided RL 三件设计都修这一条，分装在 Tokenization 和 Training，取贡献列表第一条 Hierarchical Spatial SID（引言第 (1) 条，p2），装在 Tokenization |
| Think2Go | III | Training | 摘要（p1）：非推理模型 “limit the computational capacity … to capture deep intent”；LLM “lack a deep understanding of semantic IDs (SIDs) when SIDs are trained separately”。后一条是模型读不懂 SID（III），前一条按“缺推理不单开一类”也归 III。新设计是把 SFT 和基于 RL 的推理放进一个架构联合优化，另加两种 advantage 加权（§4.1–4.2，p4–6），改的是 Objective |
| DOS | III | Tokenization | 摘要（p1）抱怨码本空间与生成空间脱节（III）、量化造成语义损失（I），分别由 DFI 和 ORQ 对付；两条一比一，新设计和题目也各占一件，按第一项贡献 DFI 的对齐目标取 III。第一项贡献是用户与物品双流加共享码本（§1 贡献列表，p2），把协同关系直接融入量化，装在 Tokenization（§2.1，p2；Fig. 1(a)，p3）；按 10-30 双盲打标和 leader 裁决定 |

## 附：改动汇总

核对范围：综述原有方法中的 10 个——TokenRec、HiD-VAE、GRLM（I 组），GenCDR、MACRec、GMC（II 组），LETTER、Align3GR、OneRec-Think、SIDReasoner（III 组）。Claude 10-07 核前 6 个，10-08 核后 4 个；MACRec 的 Representation、Tokenization 10-11 补核，至此 10 个方法的五列都逐项核过。10-09 按外部复核意见再核一轮：MACRec 的 Training 从“待定”改为确定更正；CARD、GEM-Rec 不在名单里，是这一轮顺带发现的。DeepContextGR（arXiv 2604.20861）按本人 10-09 的决定以当前版本 v3 为准复核，综述参考文献用的是 v1 题名。和仓库有关的处理（TokenRec 不挪、MACRec 留在核心方法、GenCDR 和 SIDReasoner 的卡片）记在 `../03_仓库整理/整理方案.md` 的纠错清单。

### 改了的格子（27 格）

| 方法 | 列 | 综述原值 → 改为 | 理由（原文位置） |
| --- | --- | --- | --- |
| GRLM | Inference | C-Beam → Beam | p6“Beam search strategy is used during the model’s inference process”，没有前缀树约束；生成的 Term ID 再由 EIG 映射到物品（§3.3，p5，Eq. 4）；§5.4（p8）Table 5 的生成有效率 VR@10 为 98.9%–99.8%（Sports 最低；正文写“consistently exceeding 99%”，与表不符），不到 100%，也说明没有硬约束 |
| MACRec | Inference | Scoring → C-Beam | p5“generate multiple candidate semantic IDs for different modalities using constrained beam search”：文本、图像 SID 各用约束束搜索生成候选，再平均两模态分数合并。分数只用来合并两路结果，不给外部候选打分 |
| MACRec | Training | Joint → 2-Stage | p5“Through the aforementioned trained RQ-VAE model, we obtain discrete semantic IDs … The recommendation model is then trained in a next-token prediction manner”：先训好 RQ-VAE 得到 SID，再用固定的 SID 训练 T5；Conclusion（p7）“cross-modal interactions at two stages: semantic ID training and generative model training”。作者代码（zhangfw123/MACRec）的 README 按“训练 RQ-VAE → 生成 code → finetune”的顺序执行，`data.py` 读入预先生成的 SID 文件。跨模态对齐在两个阶段内部各自进行，tokenizer 和推荐器不联合训练 |
| GMC | Inference | Beam → C-Beam | §3.5（p5）“apply constrained generation on the prefix tree constructed from the code identifiers of items”，束宽 20（§5.1.4，p6） |
| CARD | Backbone | Dec-Only → Enc-Dec | 不在核对名单，10-09 顺带发现。§4.1.3（p7）“We implement the Transformer encoder–decoder architecture based on the T5 model”，编码器、解码器各 4 层 |
| LETTER | Inference | Beam → C-Beam | §3.2.2（p5）“we follow [14] to employ constrained generation [8] via Trie”，每步只允许生成合法的后继 token |
| OneRec-Think | Training | SFT+RL → SFT+GRPO | §4.3（p5）“we optimize the model using GRPO”；附录 A.3（p17）在 VERL 里实现，每个输入采样 16 条推理路径。SFT+GRPO 是词表已有写法（同 MiniOneRec） |
| OneRec-Think | Tokenization | H-KM → R-KM（推定） | 原文没写分词方法，只说“Following OneRec (Zhou et al., 2025a; Rajput et al., 2023)”（§3，p2）。所引 OneRec Technical Report（arXiv 2506.13695v4）§2.1.2 用 RQ-Kmeans，即逐层对残差做 K-means（综述 OneRec 行也记 R-KM），Table 11 为三层、每层 8,192 的码本，和本文工业设置一致（§5.4.1，p6）。H-KM 在两篇里都没有依据。公开数据集的 4 层×256 SID 怎么构造，原文没写。主表标 † |
| OneRec-Think | Representation | Text+CF → Text+Img+CF（推定） | 原文写 itemic token 由物品的“multi-modal and collaborative content”生成（§3，p2）；OneRec 技术报告 §2.1.1 用 caption、tag、ASR、OCR、封面图和 5 帧，经 miniCPM-V-8B 编码后和协同信号对齐。本文没说用了哪些视觉输入。主表标 † |
| GEM-Rec | Backbone | Dec-Only → Enc-Dec | 不在核对名单，10-09 顺带发现。附录 B.2（p17）“we employ a T5-based encoder-decoder”；附录 F（p20）编码器、解码器各 6 层；§5.4（p9）沿用 Yang et al.（2024）复现的 TIGER |
| GEM-Rec | Inference | Pref.-Align → Bid-Aware Beam | 同上。§4.4（p7）分两步：先在按出价调整的 logits 上采样 `<ORG>`/`<AD>` 标志，再在调整后的 logits 上做宽度为 K 的束搜索生成 SID；调整方式见 §4.1 Eq. 3–4（p5–6）。综述 Legend 的 Pref.-Align（preference-aligned decoding）与此不符。词表没有现成写法，新写 Bid-Aware Beam。原文贡献列表称“Bid-Aware Constrained Decoding”（p2），但没写前缀树约束，所以不记 C-Beam |
| DeepContextGR | Tokenization | RQ → RQ-VAE | 以 v3 为准，10-09 复核。§III-D（p4）“quantized by the same RQ-VAE configuration used in MiniOneRec-style SID construction”：文本嵌入（Qwen3-Embedding-4B）与图像嵌入拼接投影后送入 RQ-VAE（Eq. 6–7）。综述的 RQ 不算错，按原文写得更具体 |
| DeepContextGR | Training | RL → SFT+GRPO | 同上。§III-E（p4–5）分两步：Stage 1 用 NLL 做 SFT（Eq. 8，p4），Stage 2 用带 QARM 奖励的 GRPO（p5）；实验设置写 SFT 3 个 epoch、GRPO 2 个 epoch（p6）。SFT+GRPO 是词表已有写法 |
| SIDReasoner | Venue | arXiv’26 → KDD’26 | 本地 PDF（arXiv v2，2026-06-09）首页页脚“KDD ’26, August 09–13, 2026, Jeju Island”，DOI 10.1145/3770855.3818122 |
| MQL4GRec | Inference | Scoring → Beam | 10-11 本人决定按原文改（原列为待定）。原文（arXiv 2504.05314）p6 为文本、图像两个子任务各用束搜索生成推荐列表，再按 Eq. 7 合并重排 |
| UniTok | Backbone | – → Enc-Dec | 10-11 本人决定按原文改（原列为待定）。附录 D.4（p15）下游推荐器采用 TIGER，保留 T5 骨干 |
| UniTok | Training | – → 2-Stage | 同上。p5“we first train UniTok on all items”，再把物品转成 token，由 LLM 推荐器学习预测下一物品 token |
| UniTok | Inference | – → Beam（推定） | 同上。全文没写解码方式（没有 beam 一词），按所沿用的 TIGER 推定。主表标 † |
| DeepContextGR | Inference | C-Beam → Beam | 10-11 本人决定按原文改（原列为待定）。v3 只写“beam size 20”（p6），没报告前缀约束；RL 阶段另设“生成的 SID 是否合法”的格式奖励（Eq. 12，p5），说明至少 RL 采样不受硬约束 |
| SEATER | Venue | SIGIR’24 → SIGIR-AP’24 | 10-11 外部审核指出。正式版发表于 SIGIR-AP ’24（东京），DOI 10.1145/3673791.3698408 |
| FORGE | Venue | arXiv’25 → KDD’26 | 10-11 外部审核指出。已有 KDD ’26 正式版，DOI 10.1145/3770855.3817477（Crossref 记录为 KDD ’26 论文集 V.2） |
| Molar | Tokenization | LLM-Vocab → – | 10-11 外部审核指出，按 SID 口径改：Molar 用多模态 LLM 产出用户、物品嵌入，按相似度推荐，不构建物品 SID；内容分词不算 SID 构建 |
| Molar | Inference | Fusion → Scoring | 同上。推理按嵌入相似度给物品打分；训练期的表示对齐不是推理期融合 |
| STAMP | Backbone | – → Enc-Dec / Dec-Only | 10-25 核对（arXiv v3）。§1（p2）“We implemented STAMP on two representative architectures: Encoder-Decoder (T5) and Decoder-Only (Qwen)”；§5.1.4（p6）GRID 框架上是 4+4 层 T5，FORGE 框架上是 Qwen2.5-0.5B-Instruct。按“A / B”写法，前为 T5、后为 Qwen |
| PROMISE | Backbone | Dec-Only → Enc-Dec | 10-26 拆 Training 列时发现。§3.1（p3）“We take an encoder-decoder approach”；Fig. 2（p4）题注“An encoder-decoder architecture optimized via the NTP loss” |
| GR-Generalize | Backbone | Dec-Only → Enc-Dec | 同上。p5“We benchmark two models: TIGER (Rajput et al., 2023), representing the generative recommendation paradigm, and SASRec”；TIGER 是 encoder–decoder |
| ADC-SID | Backbone | – → Enc-Dec | 同上。p7“For generative retrieval tasks, we adopt an encoder-decoder generative recommendation framework, REG4REC”。编号器论文，生成式检索实验在 REG4REC 上做 |

### 没改的格子及依据

| 方法 | 结论与依据 |
| --- | --- |
| TokenRec | Inference 保留 Scoring：LLM（T5-small）只编码出用户表示，再与 GNN 物品表示算余弦相似度，给全部物品排序取 top-K，不逐码生成 SID（§II-D.3，p6，Eq. 17–19；§II-E.2，p7） |
| HiD-VAE | 五列一致（768 维 SentenceTransformer 文本嵌入，p5；§3.7 前缀约束解码，p4；§3.8 两阶段训练、§4.1 encoder-decoder，p5） |
| GRLM | 其余四列一致 |
| GenCDR | Backbone 保留 Dec-Only：用 Qwen2.5-7B（Implementation Details，p6），Fig. 2 标“LLM Decoder”（p4） |
| MACRec | Inference、Training 见上表。Backbone 保留 Enc-Dec：p5“based on the encoder-decoder architecture as the GR model”。Representation 保留 Text+Img：文本用 LLaMA 编码，图像用 ViT 编码（Dual-modality Pseudo-label Generation，p3；Implementation Details 写 LLaMA 和 ViT-L/14，p6）。Tokenization 保留 Cross RQ：文本、图像嵌入经各自的 MLP 编码器后，各用一套 RQ 码本做残差量化，分别得到文本 SID 和图像 SID；量化时用对方模态的 K-means 伪标签做跨模态对比学习，并对两模态的量化表示做对齐（Cross-modal Item Quantization，p3–4，Eq. 6、13）；码本大小 256、4 层（p6）。10-11 补核 |
| GMC | 其余四列一致。Training 原文分三步（学 SID、训统一推荐器、各域 LoRA 微调），按 GenCDR 的写法记 2-Stage |
| LETTER | 其余四列一致（§3.1，p3；Eq. 3–5，p4；§3.2，p4）。Backbone 保留 Enc-Dec：原文另在 LC-Rec（LLaMA-7B，只有解码器）上实例化一次（§4.1.3，p5），但消融（Table 2，p6）和码分配分析都在 LETTER-TIGER 上做 |
| Align3GR | 五列一致（Token-level Alignment，p3–4：冻结的语义编码器和协同编码器，原文分别以 T5、DIN 举例（p3“initialized with LMs like T5”“e.g., DIN”），用户、物品各一个 RQ-VAE；Multi-task SFT，p4；Progressive DPO，p4–5，Eq. 3；Implementation Details 与 Evaluation Metrics，p5：Llama2-7B，束宽 20，正文未报告前缀约束） |
| OneRec-Think | Backbone、Inference 一致（Qwen-8B，§5.4.1，p6；先生成推理文本再生成 itemic token，Eq. 2，p3；束宽 10，附录 A.1，p12） |
| SIDReasoner | 五列一致（§3.2.1 文本元数据和 RQ-VAE，p4；§3.2.2 用 NTP 目标做多任务对齐、§3.3.1 SFT、§3.3.2 GRPO，p4–5；Qwen3-1.7B，§4.1.3，p6）。C-Beam 正文没写，依据是代码（HappyPointer/SIDReasoner，commit 2575927 的 `evaluate_Qwen3_think.py`，静态读码，没有运行）：生成完推理文本后用束宽 10 的束搜索，只允许物品表里存在的 SID 前缀 |

OneRec-Think 和 SIDReasoner 的训练流程相同：用下一 token 预测做多任务对齐，再用 SFT 激活推理，最后 GRPO。综述一个写 SFT 开头、一个写 NTP 开头，各自对应原文用词，不统一；比较时归为同一类。

### 待定

原列的 MQL4GRec、UniTok、DeepContextGR 3 条，10-11 本人决定按原文改，已移入“改了的格子”。

STAMP 的 Tokenization（10-25 发现）：arXiv v3 的 GRID 一路用 RK-Means（§5.1.4，p6），FORGE 一路用 FORGE 预处理好的 AL-GR-Tiny 数据，没写 SID 怎么构造。原值 RQ-VAE 和 GRID 一路不符；综述引用的若是 v1，先核 v1 再改。

PLUM 的 Objective（10-28 记，当天定）：回原文 §2.2（p4）核过，继续预训练是同一个 NTP 损失训行为序列和 SID 对齐模板的混合语料，改记 Multi-task NTP，已移入“Training 拆两列”。

### Training 拆两列（10-26）

10-26 本人决定把 Training 列拆成 Tokenizer、Objective 两列，写法见表下注。84 行里 46 行由 Claude 回原文（arXiv 最新版）核；另 38 行没有歧义，由旧写法换算（如 2-Stage、Enc-Dec → Fixed、NTP），其中 DiscRec、Latte、ETEGRec、GREAM 抽查原文一致。附录各行依据里的 Training 旧写法（2-Stage、Joint、E2E 等）是 10-26 以前的，留作记录。

下表是旧写法错、会误导，或新值是推定的 19 行（含 ★ 方法），末尾另有 10-28 回原文改的 PLUM 一行。页码按 arXiv 最新版。

| 方法 | 旧写法 | Tokenizer | Objective | 理由（原文位置） |
| --- | --- | --- | --- | --- |
| GR-Generalize | 2-Stage | Fixed† | NTP† | 分析论文，测的生成式模型是 TIGER（p5），SID 设置“consistent with Rajput et al. (2023)”（p7），没有单独写训练方式；两格按 TIGER 推定 |
| Molar | 2-Stage (Post-Align) | – | Discrim. | 不构建 SID；推荐器用 BCE 加对比式对齐训练，给物品打分（p3“a joint optimization framework integrates ID-based and content-based user embeddings using a contrastive learning mechanism”）。旧写法的两阶段指先微调物品编码器 MIRM，不是先编号器后生成器 |
| TriAlignGR | Joint | Fixed | Multi-task NTP | Stage 1 先用 RQ-VAE 建 SID；joint 指八个任务一起微调 LLM（p4“The LLM is jointly trained on eight complementary tasks”），编号器不随生成器更新 |
| GRAM | E2E | Fixed | NTP | 层次文本 ID 在训练前由聚类建好（p2“encode item relationships into textual representations prior to training”），生成器从 T5-small 起步，用 seq2seq 交叉熵训练 |
| DAS | Joint | Fixed | NTP | 和编号器一起训的是一个 ID 协同过滤模型，不是生成器（p2“jointly optimizes quantization and alignment through co-training”）；生成器 TIGER++ 在此之后才训 |
| ADC-SID | – | Fixed† | NTP | 生成式检索实验训了 Enc-Dec 生成器 REG4REC（p7），SID 生成损失按学到的权重加权（p8“the learned weights are utilized as loss weights for SID generation”）。没写生成器会不会更新编号器，Fixed 为推定 |
| MSCGRec | Constr.-NTP | Fixed† | NTP | 受约束的序列损失是 NTP 的变体（p8“a constrained sequence loss that restricts the search space to the subset of permissible next tokens”）。RQ-DINO 是否先于生成器训好，原文没有明说，Fixed 为推定 |
| ColaRec | Joint | Fixed | NTP + Ctr. | GID 在训练前由预训练 LightGCN 上的约束 K-means 建好；joint 指多个任务和损失一起训（p5“ColaRec is trained with the above described tasks jointly”），其中有对比损失 |
| EAGER | Joint | Fixed | NTP + Ctr. | 双码由预训练嵌入上的层次 K-means 建好；joint 指四种损失相加（p5“We combine the generation, contrastive, reconstruction and recognition losses”） |
| COBRA | E2E | Fixed | NTP + Dense | 稀疏 ID 来自预先建好的 RQ-VAE；端到端指稠密向量编码器和生成器一起训（p5“a composite loss function that combines losses for sparse ID prediction and dense vector prediction”） |
| SynGR | Joint | Fixed | NTP + Ctr. | RQ-VAE 在冻结编码器的嵌入上建 SID；生成损失另加协同对比损失 L_Syn（p6“The final objective integrates this generative loss with L_Syn”） |
| IDGenRec | 2-Stage | Altern. | NTP | ID 生成器和推荐器轮流训，每轮重算 ID（p4“alternating the training sessions of the ID generator and the base recommender”） |
| PROMISE | 2-Stage (SFT+PRM) | Fixed† | NTP + Aux. | PRM 和生成器同时训，不是后一阶段（p4“The next-token prediction task and the PRM task are trained jointly in an end-to-end manner”）；生成器是从头训的 Enc-Dec（见“改了的格子”）。没写 SID 怎么建，Fixed 按常规流程推定 |
| RecoChain | E2E | Fixed | NTP + Rank | SID 来自现成的编号器（RQ-VAE、RQ-Kmeans）；Stage II 在 SID 生成损失上加候选重排的排序损失（p3“Stage II jointly performs candidate generation and candidate-aware reranking”）。端到端指召回和重排在一个模型里 |
| GEM-Rec | E2E (Ctrl. Tok.) | Fixed | NTP | SID 沿用 TIGER 的 RQ-VAE；控制 token 加在目标序列前，用普通 NTP 训（p5“we train a Transformer to minimize the negative log-likelihood of the sequence x”） |
| STAMP | Joint | Fixed | NTP + Aux. | NTP 主损失加一个预测更远 token 的辅助头（p5“trained end-to-end with the primary NTP loss (Eq. 2) plus the MAP objective”）；端到端不涉及编号器 |
| ★ AtSpeed | Draft Align. | Fixed | NTP | 目标模型是 LC-Rec 的 LLaMA-7B，用推荐损失做 LoRA 微调（p7“we fine-tune the target LLM using the recommendation loss LRec with the parameter-efficient fine-tuning technique LoRA”）；旧写法说的是另外训的草稿模型 |
| PAD-Rec | 2-Stage | Fixed | Multi-task NTP† | 目标模型“following LC-Rec”（p6），按 LC-Rec 的多任务训练推定；草稿模块在目标模型冻结后另训 |
| MBGR | E2E | Fixed† | NTP + Aux. | 损失是逐业务的下一 SID token 预测加 BID 重建（p4“a carefully designed multi-objective loss function that combines contrastive learning with semantic reconstruction”）；端到端指 BID 表示模块。没写 SID 怎么建，Fixed 为推定 |
| ★ PLUM | CPT+SFT | Fixed | Multi-task NTP | 10-28 改（10-26 由旧写法换算为 NTP）。先训 SID，再继续预训练，最后做生成检索 SFT（§2.2，p4；§2.3，p4–5）。继续预训练用同一个 NTP 损失：“we train the model using next-token predictions on a large-scale corpus constructed from two primary sources”（§2.2，p4）；语料由用户行为序列和视频元数据各占一半（“each source accounting for 50% of the training examples”，p4），元数据一路有“SID 对标题”“SID 对主题”两种对齐模板（`Video <sid> has title (en): <video_title>`、`The topics in video <sid> are: <topics>`，Table 1，p4）。按表下注“同一损失训多种任务”记 Multi-task NTP，与 GeoGR 一致；原文没有自称多任务，分类看方法做了什么 |

MBGen、GEM-Rec、RecBase 的改动在 Training，加粗的 Objective 却只是 NTP：MBGen 改的是目标序列（行为 token 和物品 token 交替），GEM-Rec 在目标前加控制 token，RecBase 做跨域大规模预训练，损失都是普通 NTP。具体做法写进正文。

POI 10 行（9 行 10-28 加入，DOS 10-30 加入）的两列由两家双盲打标、leader 裁决定，没有用旧写法换算。前 9 行的旧写法取自 `Table2_按仓库分类.md` 的 Training 列；DOS 首次收录，没有旧写法，记“–”。页码为 PDF 物理页码。

| 方法 | 旧写法 | Tokenizer | Objective | 理由（原文位置） |
| --- | --- | --- | --- | --- |
| GNPR-SID | 2-Stage | Fixed | NTP | 先训 RQ-VAE 得到 SID，再用 LoRA 微调 LLaMA3-8B（§4.2，p6；§5，p7）；SFT 数据以真实下一 POI 的 SID 为输出（§4.2.2，p6） |
| GeoGR | CPT+SFT | Altern.† | Multi-task NTP | 构码时的 EM 算法里，LLM 做下一 POI 预测：真实下一 POI 的 SID 不在 beam 候选里时，用最高概率的候选替换；LLM 和 SID 轮流更新，作者说是为了 “mutual alignment between the LLM and the SIDs”（§4.1.3，Algorithm 1，p5）。最终推荐器从基座 θ0 重新做继续预训练加 SFT（§4.2.1，p5），所以标 †，见表下注。继续预训练用 “multi-task CPT datasets with various prompt templates”（§4.2.1，式 (9)，p5），按 LC-Rec 的口径记 Multi-task NTP。旧写法漏掉了交替构码 |
| Gwhere | CPT+SFT+EAKTO | Fixed | NTP → DPO | “Based on these SIDs, Gwhere adapts LLMs”（p1），SID 离线建好后再训 LLM（Fig. 1，p6）。继续预训练（§3.3.1，p4）→ SFT（交叉熵，§3.3.2，p4）→ EAKTO（§3.4，式 (1)，p4–5）；EAKTO 基于 KTO，用 π_θ/π_ref 的对数比作隐式奖励、不做 rollout，属于偏好优化，记 NTP → DPO。继续预训练里的两个辅助任务见表下注 |
| LGRID | 2-Stage | Fixed | Discrim. | slot 表示收敛并固定后再训 DSRQ，全部 SID 离线生成、线上查表（§3.6.2–3.6.3，p5）；任务定义为 “learning a scoring function to estimate the interaction probability”（§3.1，p3），SID 作为 DIN 等判别式模型的特征，按 AUC 评（Table 1，p6） |
| LGSID | 2-Stage | Fixed | Discrim. / NTP | 先对齐 LLM、建 SID，再训推荐模型（Fig. 2，p3）。判别式（DIN、TWIN、ETA 等，Table 1）和生成式（TIGER、OneRec，Table 2）各做一套实验（p5–6），贡献第 3 条明说 “both discriminative and generative recommendation models”（p2）；Backbone、Inference 也按 A / B 写 |
| OneLoc | NTP+DPO | Fixed | NTP → DPO | 量化沿用 OneRec 的 res-kmeans，先建好 SID（§2.2，p3）；预训练用 NTP 交叉熵（式 (20)–(21)，p5），之后用 DPO 对齐，偏好对由束搜索采样、两种奖励打分构造（§2.5，式 (24)，p5） |
| ProGEO | 2-Stage | Fixed | NTP | 先建码本，再训 Qwen2.5-1.5B 生成 SID 列表（附录 B，p11） |
| ROS | PT+SFT+GRPO | Fixed | NTP → RL | 先构造 SID（§2.2，p2），再做 SID grounding 预训练和 CoT SFT（§2.3，p3），之后做 GRPO，奖励含格式、准确和距离三项（§2.4，p4；附录 A.3，p12） |
| Think2Go | SFT+RL | Fixed | NTP → RL | SID 由 RQ-VAE 预先学好（p7），作者批评的 SID 与模型分开训练靠推理训练补，没有让生成器更新编号器（§5.8，p9）。损失由 L_SFT 和 L_DAPO 组成（p4），两部分在一个阶段里联合训，不是先 SFT 后 RL；12 种写法里没有更贴切的，记 NTP → RL |
| DOS | – | Fixed† | NTP | DOS 的量化训练与 HSTU 生成评估分开说明（§2.2，式 (11)，p3；§3.1.1，p3；§3.2.2，p4），推定先构码再训生成器；原文没写 HSTU 训练时是否冻结编号器，故 Fixed 标 †。§3.2.2 明确写下一 token 预测，Objective 记 NTP，不加 †。式 (11) 的 BCE、正交、互信息、重构和 VQ 损失用于编号器训练，不记为生成器的 NTP + Aux.；Table 2 的单列 Training 暂记 2-Stage†，对应本表 Fixed†、NTP |

## 附：★ 方法的依据

每个 ★ 方法写五列各自的依据；词表里没有的新写法在备注说明原因。

| 方法 | 依据 | 备注 |
| --- | --- | --- |
| ★ GRID | 归 I：开源框架加系统消融，不提新模型（摘要，p1），只用文本，和 TIGER 同组。PDF 为 arXiv v1。框架各环节都可替换，下面记原文实验的默认设置。**Representation**：物品文本特征为 Title、Categories、Description、Price，用 Flan-T5 均值池化得到嵌入（§4 Setup，p3）。**Tokenization**：“Unless otherwise noted, we use RK-Means with (L,W) = (3, 256) and Flan-T5-XL”（§4.1，p3）；框架另支持 R-VQ、RQ-VAE，Table 1 中 RK-Means 不差于 RQ-VAE。**Backbone**：编码器、解码器各 4 层（§4 Setup，p3）；Table 5（§4.2，p4）中 Dec-only 明显更差；代码默认 `SemanticIDEncoderDecoder`，T5 编码器、解码器各 4 层（`configs/experiment/tiger_train_flat.yaml`）。**Training**：§3.1（p2）“tokenization-then-generation”，先生成 SID，再用下一 token 预测加滑窗增强训练生成模型。**Inference**：束搜索，可选是否限制到合法 SID（§3.1，p2）；Table 8（§4.2，p4）约束与不约束效果相近，不约束更省；代码 `should_check_prefix` 默认 `False`（`src/models/modules/semantic_id/tiger_generation_model.py`，commit 2fe3475，静态读码，没有运行），所以记 Beam | R-KM 即原文的 RK-Means（残差 mini-batch K-means），词表已有 |
| ★ GFlowGR | 归 III：微调框架，用 GFlowNet 让生成概率与物品效用对齐（摘要，p1），和 MiniOneRec、Align3GR 一样属于对齐类。PDF 为 arXiv v3。**Representation、Tokenization**：方法本身不改 tokenizer，装在 TIGER 和 LETTER 两个骨干上（§4.1，p6）；物品按标题和描述分词，Yelp 另加品牌、类目（§4.1，p6）。斜杠前后分别取本表 TIGER、LETTER 两行的值。**Backbone**：原文只称“LLM-based GR backbones”（§4，p6），没写结构；TIGER、LETTER 在本表都是 Enc-Dec，按此推定。**Training**：先训 tokenizer（Algorithm 1 第 5 行，p5），再用 SFT 损失加 λ 倍 GFlowNet 损失微调（§3.3 Eq. 7，p6；§3.4，p6），两项损失同时优化，不是先后两步。**Inference**：§3.4（p6）写推理时“GFlowGR is not involved”，沿用骨干；Algorithm 1（p5）只写生成 L 个 token 再解码，没报告束宽和前缀约束，按两个骨干在本表的值推定 | 新写法 SFT+GFlowNet：词表没有 GFlowNet 目标。代码仓库 Applied-Machine-Learning-Lab/SIGIR26_GFlowGR 10-09 只有 README（“Code is still being prepared”），无法用代码核对。已部署到淘宝搜索广告（§4.7，p9） |
| ★ S2GR | 归 III：核心是在每个 SID 码之前插入隐式思考 token，做逐步推理（摘要，p1；§4.3，p5–6），属推理类。PDF 为 arXiv v3，首页是 ACM 模板占位，KDD’26 的依据见“附：收录筛选”。**Representation**：Beauty 用 Qwen3-Embedding-4B 编码标题和描述（§5.1.3，p7），量化前沿物品共现图传播，融入协同信号（§4.2.1，p4，Eq. 3–5）；工业数据用视频帧经自有多模态大模型编码（§5.1.3，p7）。表中按公开数据记。**Tokenization**：CoBa RQ-VAE（§4.2，p4–5），在 RQ-VAE 上加共现协同、码本均匀损失（Eq. 10–12）和负载均衡（Eq. 13–14）。**Backbone**：T5，编码器、解码器各 4 层（§5.1.3，p7）。**Training**：先做码本优化（§5.1.3，p7 “codebook optimization stage”；§5.3 消融把 CoBa RQ-VAE 换成普通 RQ-VAE，p7），再用 L_Rec + L_Think 训练生成模型（Eq. 22–24，p6）。**Inference**：束搜索，每个束在一步内连续产出思考 token 和其后的 SID 码，不为思考 token 单独扩展束（附录 B.1，p10）；没报告前缀约束 | 新写法 CoBa RQ-VAE：原文名称（Collaborative and Balanced RQ-VAE），词表没有同时含协同信号和负载均衡的 RQ 变体。思考 token 是连续向量，不生成文本，所以 Inference 不记 CoT，只记 SID 的搜索方式 |
| ★ V-STAR | 归 III：用价值引导的解码构造候选，再用 Sibling-GRPO 做强化学习微调（摘要，p1；§4.4，p6），和 MiniOneRec 同属对齐类。PDF 为 arXiv v2。**Representation**：数据预处理沿用 MiniOneRec（§5.1，p6 “we follow the procedure described in [20]”）；价值模型的稠密监督用冻结文本编码器编码物品文本描述（§4.1，p4）。SID 由什么嵌入构造，原文没直接写，按 MiniOneRec（本表记 Text）推定。**Tokenization**：“a 3-level SID derived from the RQ-VAE codebook”（§5.1，p6）。**Backbone**：Qwen2.5-1.5B（§5.1 Implementation Details，p6）。**Training**：“trained in two stages: supervised fine-tuning (SFT) followed by RL with GRPO”（p6）；RL 在标准 GRPO 之外加 Sibling-GRPO（§3.1，p3；§4.3，p5），训练时由 VED 为每个查询构造 16 个候选（p6）。**Inference**：测试时默认用标准束搜索（§4.4，p6；Implementation Details，p6），所有生成式解码器都在只允许合法 SID 的硬约束下运行（§5.1，p6）；VED 也可选用于推理（§4.4，p6） | SFT+GRPO 取词表已有写法：Sibling-GRPO 保留 GRPO 的更新形式（§4.3，p5），只改优势的分组方式 |
| ★ VQ-Rec | 归 II：核心是跨领域、跨平台迁移的序列推荐器（摘要，p1），同 GenCDR。PDF 为 arXiv v2（WWW’23 正式版，DOI 10.1145/3543507.3583434）。**Representation**：物品文本（Amazon 数据拼接 title、categories、brand，§3.1.1，p5）用固定的 BERT 取 [CLS] 编码（§2.2.1 式 1，p3），在 5 个 Amazon 领域的混合数据上预训练，再迁移到新领域和新平台（§3.1.1，p5），按 UTGRec、UniTok 的写法记 Multi-Dom。**Tokenization**：对文本编码做 OPQ，每个物品得到 D 维离散 code，再查 code 嵌入表求和得物品表示（§2.2.1–2.2.2，p3）。**Backbone**：仿 SASRec 的 Transformer 编码器（§2.3.1，p4）。**Training**：先在多领域混合数据上做对比预训练，用半合成和混合领域 code 作难负例（§2.3.2，p4）；再在目标领域分两步微调：先用可微置换矩阵对齐 code 与嵌入，再微调 code 嵌入表（§2.4，p4–5）。**Inference**：按式 10 用序列表示与物品表示的内积对全物品做 softmax（p5），评测时把真值放在全部物品中排序（§3.1.3，p5） | 新写法 Pretrain+FT = 多领域对比预训练后在目标领域微调，PPT p28 也把它列在 Pretrain → Finetune。不生成 SID：code 只作物品表示，推理是对全物品打分，同 TokenRec、PSRQ 的 Scoring；仓库判为排除方法，Table 2 照旧记“排除”。10-11 本人决定收进 Table 1 |

以下 21 个是“我找的论文”中收录的方法（10-10 填写，Claude 代读原文；CID、TransRec、MMGRec 是 10-10 按补充的收录标准从“待定”改为收录）。PDF 在 `候选论文/`，页码为 PDF 物理页码。

| 方法 | 依据 | 备注 |
| --- | --- | --- |
| ★ DIGER | 归 I：推荐损失的梯度经 Gumbel 软更新流回 RQ-VAE 码本，tokenizer 与生成器联合学习（§4，p3–5），和 ETEGRec 同类，只用文本。PDF 为 arXiv v3。**Representation**：数据处理沿用 LETTER，用 LLaMA-7B 依据标题和描述生成物品内容（§5，p6），再经“LLM → RQ-VAE encoder”得到表示（§4.1，p4）。**Tokenization**：RQ-VAE 码本由生成损失经 Gumbel 噪声和软更新可微学习，按码频做不确定性衰减（§4.1–4.2，p4–5）；从预训练 RQ-VAE 初始化，K=256、3 位加 1 位去重（p6）。**Backbone**：T5 式编码器、解码器各 6 层（p6）。**Training**：SID 构造和生成器全程联合优化，并与 Two-Stage 对比（§6.1，p6；Table 2，p7）。**Inference**：原文只说生成的 SID 确定性映射回物品（§3，p3），没写解码方式；实现“followed the settings in [29]”即 ETEGRec（p6），按 ETEGRec 在本表的 Beam 推定 | Learn. RQ 取词表已有写法（同 ETEGRec）；E2E 同 COBRA |
| ★ LMIndexer | 归 I：自监督学习文本物品的 SID，只用文本。PDF 为 arXiv v3。**Representation**：直接以物品文本为输入，由语言模型编码（§3.1，p3），不用预先算好的嵌入。**Tokenization**：语义编码器逐位生成 ID，用文本重建、渐进训练和对比损失学习（§3.1–3.2，p3–5；Fig. 1，p4）。**Backbone**：T5-base（§4.1，p5）。**Training**：先自监督学 ID，再在推荐任务上微调：输入用户历史文本，生成下一物品 ID（§3.3、Fig. 2，p5；§5.1，p7）。**Inference**：“constrained beam search decoding with a prefix tree”（§3.3，p5），推荐实验束宽 20（§5.1，p7） | 新写法 Self-Sup. ID：自监督语义索引器，不是 RQ-VAE |
| ★ MBGen | 归 I：只用协同信号，同 TokenRec、ETEGRec 的 CF 行。PDF 为 arXiv v2。**Representation**：用预训练多行为序列模型 MB-STR 的物品嵌入表作输入（§4.1.4，p6）。**Tokenization**：Balanced SID，第一位用单层量化自编码器，第二、三位在同前缀物品内各拟合 k-means（§3.2，p3–4）。表内取这一种；Balanced Chunked ID 是不用物品特征的随机编码对照。**Backbone**：位置—行为感知的编码器—解码器 Transformer，按 token 位置路由 FFN 专家（§3.3–3.4，p4–5）。**Training**：先构造 ID，再训练交替生成行为 token 和物品 token 的统一模型（§3.1–3.3，p3–5）。**Inference**：束搜索，50 个 beam（§4.1.3，p6）；没报告前缀约束 | 新写法 Bal. VQ+KM：单层 VQ 加逐前缀 k-means 的均衡 SID |
| ★ DualGR | 归 I：工业生成检索架构，不涉及多模态或对齐。PDF 为 arXiv v3。**Representation**：原文没写 SID 由什么嵌入构造，记“–”。**Tokenization**：“pre-quantize videos into L=3 hierarchical SIDs via residual k-means (RQ-KMeans)”（§2.2，p3）。**Backbone**：“encoder-free, decoder-centric backbone”，前端只有 embeddings + LayerNorm，目标 SID 逐步交叉注意用户行为（§1–2.2，p2–3）。**Training**：先量化，再用 ENTP-Loss 训练，把未点击曝光当作 level-1 的困难负样本（§2.5，p3）。**Inference**：长、短期两个分支各自束搜索生成完整 SID，再合并去重（§2.3、Fig. 1，p2–3）；细粒度解码前，S2D 按 level-1 桶筛选用户历史行为（§2.4.2，p3），不是前缀树约束 | 新写法 Exp.-NTP：曝光感知的下一 token 预测；Dual Beam：双分支束搜索后合并。WWW’26 Best Short Paper（arXiv 注释） |
| ★ STATIC | 归 I：约束解码的硬件实现，单一模态。PDF 为 arXiv v3。推理模块，其余列统一取原文公开数据上的 Amazon 冷启动实验（§6.1，p8–9），工业实验的配置见备注。**Representation**：原文没写物品表示，记“–”。**Tokenization**：为每个 Amazon 子集单独训练 RQ-VAE，L=4、\|V\|=256（p8）。**Backbone**：每个子集单独训练一个 Gemma 架构、1B 稠密参数的生成检索模型（p9）。**Training**：先训 RQ-VAE，再训生成检索模型（p8–9）。**Inference**：把前缀树展平为 CSR 稀疏矩阵加前几层稠密掩码，在 TPU/GPU 上向量化执行约束束搜索（§4，p4–6）；Amazon 实验束宽 20（p9） | 新写法 Vec. C-Beam：向量化的约束束搜索。工业实验（§5.1，p7）是另一套配置：“Gemini-based generative retrieval model similar to PLUM”，非 MoE、3B 稠密参数，SID 为 L=8、\|V\|=2048，束宽 70；Table 1（p7）的 948×、1033× 出自工业配置，是约束逻辑本身的耗时对比，不是端到端加速。两套配置的 Backbone 都是 Dec-Only，主表五列不变。ADS track 依据 KDD 2026 官网论文列表，10-10 核对 |
| ★ AtSpeed | 归 II：投机解码加速，同 PAD-Rec。PDF 为 arXiv v3。**Representation、Tokenization、Backbone**：实例化在 LC-Rec 上，目标模型 LLaMA-7B，物品标识沿用 LC-Rec 的 RQ-VAE（§4.1 Implementation Details，p7；附录 A.3.1，p21）；Representation 取本表 LC-Rec 的值。**Training**：目标模型按 LC-Rec 训练；本文贡献是草稿模型的 top-K 对齐训练，AtSpeed-S 对应 strict 验证、AtSpeed-R 对应 relaxed 采样验证（§3.2–3.3，p4–6）。**Inference**：草稿模型每步束搜索出 N 条序列，目标模型做 N-to-K 验证（§3.1，p3–4）。strict 验证的排序结果无损（p8）；relaxed 只保证分布近似（§3.3，p6；附录 A.2.3，p21） | 新写法 Draft Align.：草稿模型与目标模型的 top-K 对齐训练。Spec. Dec. 取词表已有写法（同 PAD-Rec） |
| ★ NEZHA | 归 II：解码加速，同 PAD-Rec。PDF 为 arXiv v2。**Representation**：物品属性转成文本，经公开 embedding API 得到表示（§4.1 Implementation Details，p6，脚注 2）。**Tokenization**：RQ-VAE，L=3，每层 512（p6）。**Backbone**：公开数据用 Llama-1B 和 Qwen3-0.8B（§4.1，p6）；生产用 0.6B、3B（Table 1，p2）。**Training**：先分词，再以 teacher forcing 训练 LLM 和自起草头（§3.4，p6；Algorithm 3）。**Inference**：一次 prefill 后由轻量自回归头逐位生成 SID，用 hash set 过滤不存在的 SID（§3.1–3.3，p4–5）。hash 只检查存在性，不做目标模型概率验证；Table 3（p7）部分质量指标有下降 | 新写法 Self-Draft+Hash：自起草头生成加 hash 合法性过滤。Industry track 依据 WWW 2026 官方日程 |
| ★ MMQ | 归 II：多模态 tokenizer，同 MMQ-v2。PDF 为 arXiv v1。组件论文，其余列取原文的生成检索实例。**Representation**：文本用 Qwen3-Embedding-7B，视觉用 Pailitao 预训练模型（§4.1.4 Implementation Details，p6）；行为信号在微调阶段进入，不在量化输入里。**Tokenization**：共享专家与文本、视觉专用专家，余弦量化加正交约束，SID 长 6（§3.2，p3–5；p6）。**Backbone**：生成检索用 HeterRec（“a strong multi-token prediction model”，§4.1.4，p6），结构本文没写。**Training**：先训多模态 tokenizer，再用软索引让 tokenizer 随下游检索、排序损失联合微调（§3.3，p5；Fig. 2，p4）。**Inference**：原文没写解码，记“–” | MoE-VQ 取词表已有写法（同 MMQ-v2）。新写法 HeterRec：直接写原文用的生成框架名；2-Stage (Joint FT)：先训 tokenizer，再与下游任务联合微调。与 MMQ-v2（2510.25622）是同团队的不同论文 |
| ★ GenSAR | 归 II：统一搜索和推荐两个任务，同 II 组的跨域方法。本地 PDF 为 arXiv v2，题名 Unified Generative Search and Recommendation；正式版 RecSys’25 题名为 GenSAR: Unifying Balanced Search and Recommendation with Generative Retrieval。**Representation**：BGE 语义嵌入加预训练序列推荐模型（如 SASRec）的协同嵌入（§3.2，p3）。**Tokenization**：先过共享码本，再分别过语义专用、协同专用码本的残差量化（§3.2、Fig. 2，p3–4）。**Backbone**：T5-small（Table 1，p6）。**Training**：下一 token 预测，联合训练搜索、推荐和辅助对齐任务（§3.3–3.4.1，p5）。**Inference**：约束束搜索（§3.4.2，p5） | 新写法 Shared/Spec. RQ：共享码本加任务专用码本。实验数字按同一版本取：本地 v2 的 Commercial 数据写 10,000 users（Table 2，p6），作者补充材料写 5,000 |
| ★ PLUM | 归 III：让预训练 LLM 与 SID 对齐，同 LC-Rec。PDF 为 arXiv v1。**Representation**：两路多模态视频嵌入（文本、视觉、音频）拼接投影（§2.1.1，p3；Fig. 1，p4），协同信号用共现对比损失注入（§2.1.3，p3）。**Tokenization**：RQ-VAE，另加多分辨率码本、渐进掩码和共现对比正则（§2.1.2–2.1.4，p3–4）。**Backbone**：Gemini-1.5 MoE 系 decoder-only（§3.1，p5；p6）。**Training**：先训 SID，再在 SID 与文本混合语料上继续预训练（§2.2，p4），最后做生成检索 SFT（§2.3，p4–5）。**Inference**：束搜索解码多条 SID 并映射到视频；没有约束，SFT 后非法 SID 少于 5%（§2.3，p5） | 新写法 CPT+SFT：继续预训练后监督微调。p6 Table 3 是在现有候选池里加生成召回、与等量强基线比较，不是替换整套排序系统 |
| ★ OneRec-V2 | 归 III：同 OneRec。PDF 为 arXiv v4，技术报告。**Representation、Tokenization**：“semantic tokenizer that generates 3 semantic IDs … as in OneRec-V1”（§2.2.2，p8），没写细节；按 OneRec 技术报告推定，处理同本表 OneRec-Think（见“附：改动汇总”）。**Backbone**：Lazy Decoder-Only，上下文作为静态条件，经上下文处理器生成各层共享的 KV，解码器只处理目标 SID 并做交叉注意（§2.2，p6–8；Fig. 4，p7）。**Training**：预训练（§2）后用真实用户反馈做强化学习，算法为 GBPO（§3.1，p13–17）。**Inference**：线上 1B 模型，束宽 512（§4，p20） | 新写法 Lazy Dec-Only：原文架构名；NTP+GBPO：预训练加 GBPO 强化学习。线上 A/B 用 1B 模型、5% 流量、一周（p20），8B 是离线扩展实验 |
| ★ EAGER-LLM | 归 III：同 EAGER。PDF 为 arXiv v1。**Representation**：语义特征取 LLM 骨干自身的隐状态，行为特征取双塔模型（如 DIN）的编码器（§3.2，p4）。**Tokenization**：语义嵌入和行为嵌入分别做层次 K-Means（§3.2，p4–5），每个物品 4 个 token（p5）。**Backbone**：Llama-7b（§4.1.3，p6），另报告 Llama2-7b（p7）。**Training**：先做带多尺度对齐重建任务的初始训练（§3.3、§3.4，p5），再做 Annealing Adapter Tuning（§3.4，p5）。**Inference**：束搜索直接生成目标物品 ID，束宽 20（p6–7） | Dual H-KM 取词表已有写法（同 EAGER）。新写法 Multi-Task+AAT：多任务对齐训练后做退火 adapter 微调 |
| ★ SemConv | 归 III：行为语义与 LLM 对齐，同 LC-Rec。PDF 为 arXiv v1；AAAI 论文没有节号，写小节标题。**Representation**：码本输入是只用行为训练的 DCCF 物品嵌入，另用 LLM 对标题和描述的嵌入做对齐损失（Alignment Tokenization，p2–3）。**Tokenization**：4 层级联码本的残差量化，加行为对齐和 LLM 对齐损失，不用自编码器重建（同小节，p3）。**Backbone**：Llama-7B（Alignment Task，p4）。**Training**：先训码本，再用序列、文本、查询对齐和负样本任务做指令微调（Alignment Task，p4）。**Inference**：沿用 LC-Rec 的提示词束搜索生成 top-K 码，只保留合法码；线上预先缓存每个用户的结果（Inference，p4；Fig. 3） | 新写法 Align. RQ：不带自编码器、带对齐损失的残差量化。缓存是部署方式，生成仍由 LLM 束搜索完成 |
| ★‡ QuaSID | 归 III：在 tokenizer 中注入协同信号并处理碰撞，同 LETTER。原综述 §9（p8）已引用（Hu et al., 2026b），本轮只补进 Table 1。PDF 为 arXiv v1，首页是 ACM 模板占位。**Representation**：公开数据用 Sentence-T5-XXL 编码 Title、Brand、Categories、Price（§5.1.1，p6），协同信号经双塔对比学习注入 tokenizer（§4.1，p4）；工业数据用多模态 LLM 嵌入（p6）。**Tokenization**：RQ-VAE 上加 CVPM（§4.2.1，p4）和 Hamming-guided margin repulsion（§4.2.2，p5）。**Backbone**：“employ TIGER as the generative recommendation backbone”（§5.1.4，p6；附录 A.2，p10）。**Training**：先离线训练 tokenizer，再训生成模型（Fig. 4，p5）。**Inference**：原文没写解码，按 TIGER 推定 | 新写法 QA-RQ：Qualification-Aware 的 RQ-VAE。ADS track 依据 KDD 2026 官网论文列表，10-10 核对 |
| ★ DECOR | 归 III：融合预训练语义和协同信号，同 ColaRec。PDF 为 arXiv v2。**Representation**：Sentence-T5 文本嵌入经 RQ-VAE 得到冻结的码本嵌入作预训练语义，另学协同 token 嵌入，二者分解后按上下文融合（§3.3–3.4，p4–5；Fig. 2，p4）。**Tokenization**：RQ-VAE，256×3 加 1 位去重（§4.1.2，p6），SID 分配不变。**Backbone**：T5（§4.1.2，p6）。**Training**：Stage 1 分词预训练，Stage 2 训练推荐器（Fig. 2，p4）。**Inference**：束搜索，推理开销实验束宽 50（§4.8，p9；Table 5，p10）；没报告前缀约束 | 改的是 token 表示，不是 SID 分配 |
| ★ DiscRec | 归 III：语义与协同信号解耦建模。PDF 为 arXiv v2，预印本，10-10 引用数 21，满足标准 2。**Representation**：LLaMA2 编码标题和描述（§IV-A，p7）；推荐端拆成语义分支和协同分支，用 gating 融合（§III，p4–6）。**Tokenization**：装在 TIGER 和 LETTER 上（§I，p2；§IV-A，p7），斜杠前后分别取两行的值。**Backbone**：T5 编码器—解码器（§II-B，p3）。**Training**：先分词，再训推荐模型（§II-A–B，p3）。**Inference**：束搜索约束到合法 SID 前缀，束宽 20（§IV-A，p7） | — |
| ★ SCRec | 归 III：跨阶段对齐语义与协同信号。文件名 CrossStage 是本地别名，作者的方法名是 SCRec（代码 github.com/DanJiayi/SCRec，p1 脚注）。PDF 为 arXiv v1。**Representation**：把物品自身文本和协同邻居（SASRec 相似物品）的标题分别写成提示，用 sentence-t5-base 编码后加权合成（§3.1，p3；p6）。**Tokenization**：RQ-VAE（§3.1，p4；p6）。**Backbone**：主实验“adopt a decoder-only backbone generative model following RPG”（p6）；代码 `genrec/models/CSA/model_csa.py` 是 2 层 GPT-2 加每位一个预测头、并行预测各位 code（10-10 静态读码，没有运行），按本表 RPG 的写法记 Non-AR；另在 TIGER、LIGER 上验证（p8）。**Training**：先训 RQ-VAE，再以生成损失加对比对齐和双曲流形对齐训练生成端（§3.2–3.3，p4–5）。**Inference**：正文没写；代码 `generate()` 对全部物品取各位 log-softmax 的平均分再取 top-K，即全物品打分；接到 TIGER 上的版本按 TIGER 推定为 Beam | 主实验不逐码生成 SID |
| ★ SpecGR | 归 III：起草器与 SID 生成器混合，同 LIGER、GR-Generalize 的 Hybrid。PDF 为 arXiv v2。**Representation**：起草器用物品文本表示检索候选（SpecGR_Aux 用 UniSRec，SpecGR++ 用 GR 编码器输出），GR 用 SID（Fig. 2，p3；p4–5），按 LIGER 的写法记 Text+SID。**Tokenization、Backbone**：沿用 TIGER（Implementation Details，p5）。**Training**：SpecGR++ 用生成损失和对比损失多任务训练，再做 learning-to-rank 微调（p5）。**Inference**：起草器提出候选（可含新物品），GR 按似然验证，不够时用已生成前缀引导再起草，最后用束搜索补齐（Fig. 2，p3；p3–4） | Hybrid 取词表已有写法；不是严格无损的投机解码。新写法 Multi-Task+LTR：多任务训练后做 learning-to-rank 微调。Games 的 unseen R@50 上 LIGER 高于 SpecGR（Table 2，p6） |
| ★ CID | 归 I：只用协同信号建 ID，同 SEATER。PDF 为 arXiv v6。**Representation**：在训练集上建物品共现图，只用交互信号（§4.2，p4）。**Tokenization**：在共现图上按谱矩阵分解做谱聚类，并在每个簇内递归聚类，得到层次 ID（§4.2.1，p4–5；Fig. 1，p5）。**Backbone**：沿用 P5，T5 编码器、解码器各 6 层（§5.2，p6）。**Training**：先建 ID，再按 P5 的提示模板训练（p2，§5.2）。**Inference**：用前缀树约束解码，只生成存在的 ID（p2） | 新写法 Spectral Clus.：共现图递归谱聚类。论文还比较了随机、标题、序列等多种索引，表内记本文提出的 CID |
| ★ TransRec | 归 I：文本标识，同 IDGenRec、GRLM。PDF 为 arXiv v2。**Representation**：物品的数字 ID、标题和属性都按文本处理（§3.1，p3–4）。**Tokenization**：多面标识，同时用 ID、标题子串和属性（§3.1，p3–4；Fig. 4）。**Backbone**：BART-large（编码器—解码器）和 LLaMA-7B（仅解码器）两套（§4.1，p5–6），斜杠前后分别对应。**Training**：指令微调，LLaMA 用 LoRA（§2.1，p3；p6）。**Inference**：用 FM-index 做不限位置的约束生成，各面分别生成合法标识，再由聚合打分落到物品（§3.2，p4–5），束宽 20（p6） | 新写法 Multi-Facet ID、Instr. Tuning、FM-Index+Agg.。最终物品由聚合打分决定（同 GRLM） |
| ★ MMGRec | 归 II：多模态量化，同 MACRec。PDF 为 arXiv v4，正式版为 ACM TOMM（DOI 10.1145/3838594）。**Representation**：视觉、声学、文本特征拼接，再用图网络融合协同信号（§3，p5–6）。**Tokenization**：Graph RQ-VAE 产生语义 token，同语义 token 的物品按热度排序，排名作为最后一位 token 去冲突（p3；§3，p6–7）。**Backbone**：Transformer 编码器—解码器，编码器用关系感知自注意力（Fig. 2，p8；p9）。**Training**：先分配 Rec-ID，再训练生成模型，两阶段（p5）。**Inference**：束搜索加约束，避免生成不存在的 Rec-ID（§4.4，p10） | 新写法 Graph RQ-VAE。Representation 另含声学特征，表内按词表记 Text+Img+CF |

## 附：收录筛选

查询日期 2026-10-07。引用数取自 Semantic Scholar；venue 依据见“出处”列。“待核”表示只有 Semantic Scholar 的 venue 字段或模板痕迹，还没找到 DOI、论文集或作者声明，读原文时确认。

### 仓库批（13 个综述没有的方法）

| 方法 | Venue | 出处 | 引用数 | 判断 | 理由 |
| --- | --- | --- | ---: | --- | --- |
| GNPR-SID | KDD’25 | arXiv 注释“accepted by KDD 2025” | 73 | 收录 | 满足标准 1、2；10-27 本人定 POI 进 Table 1 |
| GRID | CIKM’25 | DOI 10.1145/3746252.3761612 | 48 | 收录 | 标准 1、2 |
| GFlowGR | SIGIR’26 | DOI 10.1145/3805712.3809663 | 5 | 收录 | 标准 1 |
| S2GR | KDD’26 | arXiv 注释“Accepted by KDD 2026” | 7 | 收录 | 标准 1 |
| V-STAR | KDD’26 | DOI 10.1145/3770855.3817873 | 3 | 收录 | 标准 1 |
| Think2Go | KDD’26 | arXiv 注释“Accepted by KDD 2026 Research Track” | 3 | 收录 | 满足标准 1；10-27 本人定 POI 进 Table 1 |
| Gwhere | RecSys’26 | PDF 首页 ACM Reference Format：RecSys ’26 | 0 | 收录 | 满足标准 1；10-27 本人定 POI 进 Table 1 |
| OneLoc | arXiv’25 | arXiv 只有 v1（2025-08-20），没有 comments 和 journal-ref；PDF 是 ACM 模板占位；Semantic Scholar 的 venue 字段写 WSDM，检索不到 WSDM 2026 的录用信息（10-28 核） | 18 | 收录 | 两条都不满足；10-27 本人定 POI 进 Table 1 |
| LGSID | AAAI’26 | AAAI 第 40 卷第 17 期，DOI 10.1609/aaai.v40i17.38514（10-28 核）；PDF 首页有 AAAI 2026 版权行，arXiv 无录用注释 | 7 | 收录 | 满足标准 1；10-27 本人定 POI 进 Table 1 |
| ROS | ACL’26 | ACL 2026 Long，ACL Anthology 2026.acl-long.332（10-28 核） | 2 | 收录 | 满足标准 1；10-27 本人定 POI 进 Table 1 |
| GeoGR | arXiv’26 | PDF 是 ACM 模板占位 | 1 | 收录 | 两条都不满足；10-27 本人定 POI 进 Table 1 |
| ProGEO | arXiv’26 | — | 2 | 收录 | 两条都不满足；10-27 本人定 POI 进 Table 1 |
| LGRID | arXiv’26 | — | 0 | 收录 | 两条都不满足；10-27 本人定 POI 进 Table 1 |

### 仓库“新增论文”一节（10 篇）

这一节已于 10-07 在仓库 fork 的 README 里拆进现有分类（见 `../03_仓库整理/整理方案.md`）。对照 Table 1 的结果：

| 方法 | 在 Table 1 | 处理 |
| --- | --- | --- |
| HiD-VAE、GRLM、MACRec、GenCDR、GMC、OneRec-Think | 是 | 在核对的 10 个里，已核完，见“附：改动汇总” |
| GREAM、IDGenRec、MQL4GRec | 是 | 已在 Table 1，PPT 也已有 case 页，不用再加 |
| VQ-Rec | 否 | 收录（10-11 本人决定）：WWW’23，满足标准 1，归 II 组，依据见“附：★ 方法的依据”。量化 code 只作序列推荐器的表示，不生成 SID，推理对全物品打分（仓库判为排除方法） |

### 我找的论文

我自己检索到的论文直接登记在这里，不进仓库（导师 10-05：“先不用同步你新找的”）。登记时先在 `../01_论文清单/方法对照表.csv` 里按方法名或 arXiv ID 查重；PDF 存进 `pdf/`，文件名用 `方法名_arXivID.pdf`。收录的方法标 ★ 加进 Table 1，五列依据写进“附：★ 方法的依据”。

10-09 检索到 30 篇，PDF 在 `候选论文/`（没有挪进 `pdf/`），10-09 的摘要级初筛清单已于 10-10 删除，结论以本表为准；逐篇审核见 `候选论文/审核报告_2026-10-10_已采纳.md`。下表是 10-10 的结论：收录 21 篇，不收 8 篇，POI 暂缓 1 篇。原先待定的 4 篇按补充的收录标准处理：CID、TransRec、MMGRec 收录，GPTRec 不收。引用数取自 Semantic Scholar，查询日期 2026-10-10。查重对照 `方法对照表.csv` 和综述 PDF，30 篇都没有 arXiv ID 重复。10-11 补登 5 篇（ReCast 起的末 5 行，PDF 复制自 `~/papers-backlog/B0/`），全部不收；引用数查询日期 2026-10-11。

| 方法 | 题名（链接） | Venue | 出处 | 引用数 | 查重 | 判断 | 理由 |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| DIGER | [Differentiable Semantic ID for Generative Recommendation](https://arxiv.org/abs/2601.19711) | SIGIR’26 | arXiv 注释、DOI 10.1145/3805712.3809641 | 36 | 无 | 收录 | 标准 1、2 |
| LMIndexer | [Language Models As Semantic Indexers](https://arxiv.org/abs/2310.07815) | ICML’24 | PMLR 235 | 37 | 无 | 收录 | 标准 1、2 |
| MBGen | [Multi-Behavior Generative Recommendation](https://arxiv.org/abs/2405.16871) | CIKM’24 | arXiv 注释、DOI 10.1145/3627673.3679730 | 54 | 无 | 收录 | 标准 1、2 |
| DualGR | [DualGR: Generative Retrieval with Long and Short-Term Interests Modeling](https://arxiv.org/abs/2511.12518) | WWW’26 Short | arXiv 注释、DOI 10.1145/3774904.3792851 | 7 | 无 | 收录 | 标准 1（短文） |
| STATIC | [Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators](https://arxiv.org/abs/2602.22647) | KDD’26 ADS | arXiv journal_ref、DOI 10.1145/3770855.3818506、KDD 官网论文列表 | 12 | 无 | 收录 | 标准 1 |
| AtSpeed | [Efficient Inference for Large Language Model-based Generative Recommendation](https://arxiv.org/abs/2410.05165) | ICLR’25 | arXiv 注释、ICLR 论文集 | 32 | 无 | 收录 | 标准 1、2 |
| NEZHA | [NEZHA: A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations](https://arxiv.org/abs/2511.18793) | WWW’26 Industry | DOI 10.1145/3774904.3792797、WWW 官方日程 | 21 | 无 | 收录 | 标准 1、2 |
| MMQ | [MMQ: Multimodal Mixture-of-Quantization Tokenization for Semantic ID Generation and User Behavioral Adaptation](https://arxiv.org/abs/2508.15281) | WSDM’26 | arXiv journal_ref、DOI 10.1145/3773966.3777923 | 29 | 与 MMQ-v2（2510.25622）同团队，不是同一篇 | 收录 | 标准 1、2 |
| GenSAR | [Unified Generative Search and Recommendation](https://arxiv.org/abs/2504.05730) | RecSys’25 | DOI 10.1145/3705328.3748071；正式题名 GenSAR: Unifying Balanced Search and Recommendation with Generative Retrieval | 20 | 无 | 收录 | 标准 1、2 |
| PLUM | [PLUM: Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations](https://arxiv.org/abs/2510.07784) | WWW’26 | DOI 10.1145/3774904.3792802 | 58 | 无 | 收录 | 标准 1、2 |
| OneRec-V2 | [OneRec-V2 Technical Report](https://arxiv.org/abs/2508.20900) | arXiv’25 | — | 27 | Table 1 已有 OneRec，本篇是后续版本 | 收录 | 标准 2 |
| EAGER-LLM | [EAGER-LLM: Enhancing Large Language Models as Recommenders through Exogenous Behavior-Semantic Integration](https://arxiv.org/abs/2502.14735) | WWW’25 | arXiv 注释、DOI 10.1145/3696410.3714933 | 42 | Table 1 已有 EAGER，本篇是 LLM 版 | 收录 | 标准 1、2 |
| SemConv | [Semantic Convergence: Harmonizing Recommender Systems via Two-Stage Alignment and Behavioral Semantic Tokenization](https://arxiv.org/abs/2412.13771) | AAAI’25 | arXiv 注释、AAAI 论文集 | 24 | 无 | 收录 | 标准 1、2 |
| QuaSID | [Stop Treating Collisions Equally: Qualification-Aware Semantic ID Learning for Recommendation at Industrial Scale](https://arxiv.org/abs/2603.00632) | KDD’26 ADS | DOI 10.1145/3770855.3818486、KDD 官网论文列表 | 12 | 综述 §9（p8）已引用，不在 Table 1 | 收录 | 标准 1 |
| DECOR | [Learning Decomposed Contextual Token Representations from Pretrained and Collaborative Signals for Generative Recommendation](https://arxiv.org/abs/2509.10468) | SIGIR’26 | arXiv 注释、DOI 10.1145/3805712.3809578 | 2 | 无 | 收录 | 标准 1 |
| DiscRec | [DiscRec: Disentangled Semantic-Collaborative Modeling for Generative Recommendation](https://arxiv.org/abs/2506.15576) | arXiv’25 | — | 21 | 无 | 收录 | 标准 2 |
| SCRec | [Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation](https://arxiv.org/abs/2609.13678) | RecSys’26 | arXiv 注释（Main Track）、DOI 10.1145/3773078.3831736 | 0 | 无；本地文件名 CrossStage | 收录 | 标准 1 |
| SpecGR | [Inductive Generative Recommendation via Retrieval-based Speculation](https://arxiv.org/abs/2410.02939) | AAAI’26 | arXiv 注释（oral） | 25 | 无 | 收录 | 标准 1、2；按 LIGER 的 Hybrid 口径 |
| TransRec | [Bridging Items and Language: A Transition Paradigm for Large Language Model-Based Recommendation](https://arxiv.org/abs/2310.06491) | KDD’24 | arXiv 注释、DOI 10.1145/3637528.3671884 | 93 | 无 | 收录 | 标准 1。多面文本标识，最终靠聚合打分落到物品（§3.1–3.2，p3–5），口径同 IDGenRec、GRLM；Table 2 记为边界 |
| CID | [How to Index Item IDs for Recommendation Foundation Models](https://arxiv.org/abs/2305.06569) | SIGIR-AP’23 | arXiv 注释（full paper）、DOI 10.1145/3624918.3625339 | 232 | 无 | 收录 | SIGIR-AP full paper，按补充的标准收。协同共现图递归谱聚类建 ID，P5 用前缀树约束生成（p2，§4.2） |
| GPTRec | [Generative Sequential Recommendation with GPTRec](https://arxiv.org/abs/2306.11114) | Gen-IR@SIGIR’23 | arXiv 注释 | 39 | 无 | 不收 | workshop 论文。SVD 后逐维分桶得到 sub-item token（§4.2，p4–5），写正文时作为早期协同分词的例子 |
| MMGRec | [MMGRec: Multimodal Generative Recommendation with Transformer Model](https://arxiv.org/abs/2404.16555) | TOMM’26 | DOI 10.1145/3838594（2026-10-08 在线） | 63 | 无；与 MMQ-v2、MME-SID 是不同论文 | 收录 | ACM TOMM 正式论文，按补充的标准收。多模态与协同量化，约束束搜索（§4.4，p10） |
| SETRec | [Order-agnostic Identifier for Large Language Model-based Generative Recommendation](https://arxiv.org/abs/2502.10833) | SIGIR’25 | DOI 10.1145/3726302.3730053 | 61 | 无 | 不收 | 用连续 token，不用离散 SID（p4 脚注 1），再对全物品打分（Eq. 7）；留作正文里连续标识的对照 |
| MERGE | [MERGE: Next-Generation Item Indexing Paradigm for Large-Scale Streaming Recommendation](https://arxiv.org/abs/2601.20199) | CIKM’26 | arXiv 注释 | 5 | 无 | 不收 | 目前只用于传统检索，扩展到生成式检索是未来工作（§6，p7） |
| ScalingView | [Understanding Generative Recommendation with Semantic IDs from a Model-scaling View](https://arxiv.org/abs/2509.25522) | KDD’26 | arXiv 注释、KDD 官网论文列表 | 17 | 无 | 不收 | 分析论文，不提出新推荐方法；写正文用 |
| CollisionGenRec | [Faithful Evaluation of Semantic-ID Tokenizers for Generative Recommendation](https://arxiv.org/abs/2605.25330) | CIKM’26 | arXiv 注释（Full Research Paper） | 2 | 无 | 不收 | 评测论文（SID 碰撞与物品级评测）；写正文用 |
| SID-Repro | [What Makes a Good Semantic ID for Generative Recommendation? A Reproducibility Study](https://arxiv.org/abs/2609.24430) | SIGIR-AP’26 | arXiv 注释 | 2 | 无 | 不收 | 复现研究，不提出新方法；写正文用 |
| Snapchat-SID | [Semantic IDs for Recommender Systems at Snapchat: Use Cases, Technical Challenges, and Design Choices](https://arxiv.org/abs/2604.03949) | SIGIR’26 Industry | arXiv 注释 | 8 | 生成架构沿用已收录的 GRID | 不收 | 工业经验总结；写正文用 |
| JointSR | [Semantic IDs for Joint Generative Search and Recommendation](https://arxiv.org/abs/2508.10478) | RecSys’25 LBR | arXiv 注释 | 40 | 无 | 不收 | Late-Breaking Results，主要比较 SID 构造方式；写正文用 |
| DOS | [DOS: Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan](https://arxiv.org/abs/2602.04460) | WWW’26 Short | arXiv 注释、DOI 10.1145/3774904.3792845 | 3 | 无 | 收录 | 餐饮本地生活场景（§2.1，p2）；10-30 本人定收入 Table 1，按 POI 双盲打标和 leader 裁决归 III × Tokenization，取代 10-07 的暂缓决定 |
| ReCast | [ReCast: Recasting Learning Signals for Reinforcement Learning in Generative Recommendation](https://arxiv.org/abs/2604.22169) | arXiv’26 | — | 0 | 无 | 不收 | 两条都不满足。方法属 SID 生成：在 OpenOneRec 的 RL 阶段只改组内优势，全零组注入真值作正例，再只更新最强正例和按 SID 前缀相似度选的最难负例（§3，p4–6）；Qwen3-1.7B（§5.1，p7）。录用或引用够了再收 |
| RGD | [Reward Guided Decoding for Generative Recommendation](https://arxiv.org/abs/2607.25344) | arXiv’26 | PDF 是 ACM 模板占位 | 1 | 无 | 不收 | 两条都不满足。方法属 SID 生成：推理时用奖励模型逐层给候选码打分，按 KL 正则的闭式分布改写束搜索，不重训生成器（§3.2，p3–4；Algorithm 1，p5）；已在快手上线（摘要，p1）。录用或引用够了再收 |
| TemporalCold | [Can Generative Recommendation Reach Cold Items? A Temporal Perspective on Semantic-ID Generation](https://arxiv.org/abs/2607.21101) | arXiv’26 | PDF 是 ACM 模板占位 | 1 | 无 | 不收 | 分析论文，不提出新方法：按绝对时间划分，分析 SID 模型能否生成新物品，含未见 token、前缀探针（摘要，p1–2）；写正文用 |
| ColdStart-Repro | [Cold-Starts in Generative Recommendation: A Reproducibility Study](https://arxiv.org/abs/2603.29845) | arXiv’26 | — | 5 | 无 | 不收 | 复现研究，不提出新方法：统一冷启动协议下比较模型规模、标识设计和训练策略（摘要，p1）；写正文用，同 SID-Repro |
| HSTU | [Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations](https://arxiv.org/abs/2402.17152) | ICML’24 | arXiv 注释 | 354 | 无 | 不收 | 满足标准 1，但不用 SID：物品用原始类别 ID，把排序和召回改写成序列转导（§2.1–2.2，p2–3），全文没有语义 ID，在 Table 1 范围外；写正文作工业 scaling 背景 |

## 附：PPT case 页

10-11 按本人决定定为 9 篇：原审核的 6 篇，加 OneRec-V2、PLUM、AtSpeed，补 Backbone、Inference 两章 case 页偏少的问题，并给 Training 总览页里还没有 case 页的“Pretrain → Finetune”配一篇。章取论文核心贡献所在的阶段；子类取该章总览页已有的子类，见 `../01_论文清单/PPT目录.md`。QuaSID、GFlowGR 只进表。

“插入后页码”按 9 页全部插入后计；原 40 页的对应关系见表下。

| 方法 | 章 · 子类 | Case Study 标签 | 插在原第几页之后 | 插入后页码 | 这页要讲清的点 |
| --- | --- | --- | ---: | ---: | --- |
| DECOR | Representation · 晚期融合 | Case Study 4 晚期融合 | 14 | 15 | 固定 SID 下增强 token 表示：语义与协同表示融合，上下文相关的 token 组合 |
| GRID | Tokenization · 4.1 量化方法 | Case Study 3 量化方法的公开数据对照 | 18 | 20 | R-KMeans 与其他 tokenizer 在公开数据上的对照；结论限定在论文的数据和设置内。原 OneRec 页已用“R-KMeans 在生成式推荐的应用”，标签不重复 |
| S2GR | Backbone · Encoder–Decoder（跨阶段） | Case Study 3 潜空间逐步推理 | 25 | 28 | 连续思考 token 之外，交代 CoBa 码本与语义引导；主图包含逐步潜空间推理部分；页内注明跨阶段 |
| OneRec-V2 | Backbone · Decoder-only | Case Study 4 Decoder-only 的工业扩展 | 25 | 29 | Lazy Decoder-Only：V1 的 Encoder 占 97.66% 计算；改后总计算降 94%，扩到 8B 时 loss 符合 scaling law。真实反馈偏好对齐属于 Training，只在总结里带一句 |
| DIGER | Training · 端到端训练 | Case Study 5 端到端训练中的码本坍塌 | 32 | 37 | 问题限定在论文的具体训练设置；方法写可微分配、探索与不确定性衰减；不写成“直接回传梯度必然坍塌” |
| V-STAR | Training · 强化学习 | Case Study 6 价值引导的强化学习 | 32 | 38 | 价值引导采样和 Sibling-GRPO 都讲；“兄弟”指同一父前缀下的候选分支；和第 32 页 GREAM 对照训练与搜索机制的补充 |
| PLUM | Training · Pretrain → Finetune | Case Study 7 持续预训练后微调 | 32 | 39 | SID 物品化 + 领域数据持续预训练（CPT）+ 生成式召回微调；YouTube 工业数据，收益对照的是线上大 embedding 表基线 |
| STATIC | Inference · Constraint Beam Search: Trie | Case Study 3 Trie 约束解码的向量化 | 36 | 44 | 约束结构的向量化执行与批量掩码；速度收益只写论文实测的部分 |
| AtSpeed | Inference · Beam Search | Case Study 4 Beam Search 的推理加速 | 36 | 45 | 投机解码要求 top-K 序列都被草稿命中；方法为 top-K 对齐目标 AtSpeed-S 和放宽验证的 AtSpeed-R；严格验证约 2 倍、放宽验证最高 2.5 倍加速（论文两个公开数据集） |

原页码与插入后页码：原 1–14 不变；原 15–18 → 16–19；原 19–25 → 21–27；原 26–32 → 30–36；原 33–36 → 40–43；原 37–40 → 46–49。原第 17 页 OneRec 变为第 18 页。全部共 49 页。
