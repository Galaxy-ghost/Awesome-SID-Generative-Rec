# 按模态找论文

[← README](../../../README.zh.md#阅读导航) · [English](../../index/modality.md) | 中文

本页按输入 SID 编号器的信息类型分组列出论文（分组规则定义于 `data/vocab.yaml`）。内容方面按各构码分支分别判定，协同与上下文方面按全部分支合起来判定；同一篇论文可进入多个分组，各节列出完整的构码分支值与应用领域。

| 方面 | 分组 |
| :--- | :--- |
| **内容** | [纯文本（115）](#纯文本) · [单一非文本（8）](#单一非文本) · [多模态（36）](#多模态) · [无内容模态（11）](#无内容模态) |
| **协同** | [仅协同信号（7）](#仅协同信号) · [含协同信号（50）](#含协同信号) |
| **上下文** | [结构化属性（7）](#结构化属性) · [地理空间（14）](#地理空间) · [时间特征（2）](#时间特征) |
| **未知** | [待明确（28）](#待明确) |

## 纯文本

> 共 115 篇。至少一个构码分支的内容模态只有 `Text`（该分支不含 `Img`、`Audio`、`Video`、`MM`）。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [TIGER](../papers/tiger.md) | NeurIPS’23 | 范式、系统与基准 | `Text` | `电商` |
| [VQ-Rec](../papers/vq-rec.md) | WWW’23 | VI × Tokenization | `Text` | `电商` |
| [CoST](../papers/cost.md) | RecSys’24 | I × Tokenization | `Text` | `新闻` · `电商` |
| [EAGER](../papers/eager.md) | KDD’24 | I × Backbone | semantic: `Text` · behavior: `CF` | `电商` · `本地生活与 POI` |
| [IDGenRec](../papers/idgenrec.md) | SIGIR’24 | III × Tokenization | `Text` | `电商` · `本地生活与 POI` |
| [LC-Rec](../papers/lc-rec.md) | ICDE’24 | III × Training | `Text` | `电商` |
| [LETTER](../papers/letter.md) | CIKM’24 | I × Tokenization | `Text` + `CF` | `电商` · `本地生活与 POI` |
| [LIGER](../papers/liger.md) | arXiv’24 | VI × Inference | `Text` | `电商` · `游戏` |
| [LMIndexer](../papers/lmindexer.md) | ICML’24 | I × Tokenization | `Text` | `电商` · `搜索` |
| [SIIT](../papers/siit.md) | arXiv’24 | III × Tokenization | `Text` | `电商` · `本地生活与 POI` |
| [TransRec](../papers/transrec.md) | KDD’24 | II × Tokenization | id: – · title: `Text` · attribute: `Text` | `电商` · `本地生活与 POI` |
| [ActionPiece](../papers/actionpiece.md) | ICML’25 | I × Tokenization | `Text` | `电商` |
| [AtSpeed](../papers/atspeed.md) | ICLR’25 | V × Inference | `Text` | `电商` · `电影` · `图书与有声书` |
| [COBRA](../papers/cobra.md) | NeurIPS’25 | I × Backbone | `Text` | `电商` · `广告` |
| [DAS](../papers/das.md) | CIKM’25 | I × Tokenization | `Text` + `CF` | `广告` |
| [DiscRec](../papers/discrec.md) | arXiv’25 | I × Backbone | A: `Text` · B: `Text` + `CF` | `电商` |
| [EAGER-LLM](../papers/eager-llm.md) | WWW’25 | I × Tokenization | semantic: `Text` · behavior: `CF` | `电商` |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I × Tokenization | semantic: `Text` + `CF` · collaborative: `CF` | `电商` · `短视频与直播` · `工业场景未明` |
| [GenSAR](../papers/gensar.md) | RecSys’25 | I × Tokenization | semantic: `Text` + `CF` · collaborative: `Text` + `CF` | `电商` · `搜索` |
| [GMC](../papers/gmc.md) | arXiv’25 | VI × Tokenization | `Text` | `电商` |
| [GRAM](../papers/gram.md) | ACL’25 | I × Tokenization | `Text` | `电商` · `本地生活与 POI` |
| [GREAM](../papers/gream.md) | arXiv’25 | III × Training | `Text` | `电商` |
| [GRID](../papers/grid.md) | CIKM’25 | 范式、系统与基准 | `Text` | `电商` |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II × Tokenization | `Text` + `Attr` | `电商` · `短视频与直播` |
| [LLaDA-Rec](../papers/llada-rec.md) | arXiv’25 | III × Backbone | `Text` | `电商` |
| [MiniOneRec](../papers/minionerec.md) | arXiv’25 | 范式、系统与基准 | `Text` | `电商` |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | collaborative: `CF` · text: `Text` · visual: `Img` | `电商` |
| [MQL4GRec](../papers/mql4grec.md) | ICLR’25 | I × Tokenization | text: `Text` · image: `Img` | `电商` |
| [PSI](../papers/psi.md) | arXiv’25 | II × Tokenization | `Text` | `电商` · `搜索` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | text: `Text` · image: `Img` · audio: `Audio` · joint_Amazon: `Text` + `Img` · joint_Music: `Text` + `Audio` | `电商` · `音乐` |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I × Tokenization | `Text` + `Geo` | `本地生活与 POI` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `Text` | `新闻` · `电影` · `短视频与直播` · `图书与有声书` · `本地生活与 POI` · `游戏` · `电商` · `旅行与酒店` |
| [RPG](../papers/rpg.md) | KDD’25 | V × Backbone | `Text` | `电商` |
| [SemConv](../papers/semconv.md) | AAAI’25 | III × Tokenization | `Text` + `CF` | `电商` |
| [UNGER](../papers/unger.md) | TOIS’25 | I × Representation | `Text` + `CF` | `电商` |
| [ACERec](../papers/acerec.md) | arXiv’26 | V × Backbone | `Text` | `电商` |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III × Tokenization | `Text` + `CF` | `电商` · `本地生活与 POI` · `广告` |
| [APAO](../papers/apao.md) | KDD’26 | IV × Training | `Text` | `电商` · `本地生活与 POI` |
| [API](../papers/api.md) | arXiv’26 | II × Tokenization | `Text` | `电商` |
| [AWARE](../papers/aware.md) | arXiv’26 | VI × Training | `Text` + `Geo` | `本地生活与 POI` |
| [CAPE](../papers/cape.md) | arXiv’26 | I × Inference | `Text` | `电商` · `音乐` |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I × Tokenization | `Text` + `Time` | `电商` |
| [CITE](../papers/cite.md) | Electronics’26 | I × Inference | `Text` | `电商` · `本地生活与 POI` |
| [CogRec](../papers/cogrec.md) | arXiv’26 | III × Tokenization | `Text` | `电商` |
| [DACT](../papers/dact.md) | SIGIR’26 | VI × Tokenization | `Text` + `CF` | `电商` |
| [DASO](../papers/daso.md) | arXiv’26 | IV × Training | `Text` + `unknown` | `电商` · `工业场景未明` |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | A: `Text` · B: `unknown` | `电商` · `电影` · `音乐` |
| [DECOR](../papers/decor.md) | SIGIR’26 | III × Backbone | `Text` | `电商` |
| [DIGER](../papers/diger.md) | SIGIR’26 | II × Tokenization | `Text` | `电商` · `本地生活与 POI` |
| [DOS](../papers/dos.md) | WWW’26 Short | III × Tokenization | `Text` + `CF` | `本地生活与 POI` |
| [DREAM](../papers/dream.md) | arXiv’26 | VI × Tokenization | `Text` + `CF` | `电商` |
| [Evo-Rec](../papers/evo-rec.md) | arXiv’26 | III × Training | `Text` | `电商` |
| [FedCGR](../papers/fedcgr.md) | CIKM’26 | VI × Backbone | `Text` | `电商` |
| [FLASH](../papers/flash.md) | NeurIPS’26 | III × Backbone | `Text` | `电商` |
| [GEM-Rec](../papers/gem-rec.md) | arXiv’26 | IV × Training | `Text` | `游戏` · `电商` · `广告` |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI × Tokenization | `Text` + `unknown` | `电商` · `图书与有声书` · `电影` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `Text` + `Geo` + `CF` | `本地生活与 POI` · `搜索` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | A: `Text` · B: `Text` + `CF` | `本地生活与 POI` · `电商` · `广告` · `搜索` |
| [Ghost](../papers/ghost.md) | NeurIPS’26 | IV × Training | `Text` | `电商` |
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | 范式、系统与基准 | `Text` | `电商` · `游戏` · `本地生活与 POI` |
| [GRC](../papers/grc.md) | CIKM’26 | III × Inference | `Text` | `电商` · `广告` |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I × Tokenization | `Text` + `CF` | `电商` · `新闻` · `本地生活与 POI` |
| [GRLM](../papers/grlm.md) | arXiv’26 | III × Tokenization | `Text` | `电商` |
| [GTI](../papers/gti.md) | arXiv’26 | III × Training | A: `Text` + `CF` · B: `Text` | `招聘` · `电商` |
| [HASTE](../papers/haste.md) | arXiv’26 | IV × Training | A: `Text` · B: `MM` | `电商` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `Text` + `Attr` + `Geo` | `本地生活与 POI` |
| [IBA](../papers/iba.md) | arXiv’26 | V × Backbone | `Text` | `电商` · `短视频与直播` |
| [IDM/CMM](../papers/idm-cmm.md) | arXiv’26 | IV × Training | `Text` | `电商` |
| [Intent-Driven-News](../papers/intent-driven-news.md) | ACL’26 Industry | III × Training | `Text` | `新闻` |
| [ISD](../papers/isd.md) | arXiv’26 | IV × Inference | `Text` | `电商` |
| [JevRec](../papers/jevrec.md) | arXiv’26 | V × Tokenization | `Text` | `电商` |
| [LESSRec](../papers/lessrec.md) | arXiv’26 | III × Backbone | A: `Text` · B: `Text` + `CF` | `电商` |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I × Representation | `Text` + `Geo` | `本地生活与 POI` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text` + `Geo` + `Attr` + `CF` | `本地生活与 POI` |
| [LION](../papers/lion.md) | CIKM’26 | VI × Backbone | `Text` | `电商` |
| [LoopGR](../papers/loopgr.md) | arXiv’26 | V × Backbone | `Text` | `电商` · `工业场景未明` |
| [MACRec](../papers/macrec.md) | AAAI’26 | I × Tokenization | text: `Text` · image: `Img` | `电商` |
| [MDGR](../papers/mdgr.md) | arXiv’26 | III × Backbone | `Text` | `电商` |
| [Merge-and-Branch](../papers/merge-and-branch.md) | arXiv’26 | V × Backbone | `Text` | `电商` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | image: `Img` · text: `Text` · collaborative: `CF` | `电商` · `短视频与直播` |
| [NEO](../papers/neo.md) | arXiv’26 | 范式、系统与基准 | A: `Text` · B: `Audio` | `音乐` · `播客` · `图书与有声书` · `搜索` |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V × Inference | `Text` | `电商` · `本地生活与 POI` · `广告` · `搜索` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `Text` + `CF` | `电商` · `本地生活与 POI` |
| [PCR-CA](../papers/pcr-ca.md) | KDD’26 | I × Tokenization | `Text` + `CF` | `应用商店` |
| [Pctx](../papers/pctx.md) | CIKM’26 | I × Tokenization | `Text` + `CF` | `电商` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `Text` + `Geo` | `本地生活与 POI` · `搜索` |
| [PROMISE](../papers/promise.md) | arXiv’26 | III × Inference | `Text` | `电商` · `短视频与直播` |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II × Tokenization | `Text` | `电商` · `音乐` · `电影` · `新闻` |
| [RAGR](../papers/ragr.md) | arXiv’26 | I × Training | item: `Text` · review: `Text` | `电商` |
| [REGER](../papers/reger.md) | arXiv’26 | I × Training | `Text` | `电商` |
| [ReRankID](../papers/rerankid.md) | arXiv’26 | 范式、系统与基准 | `Text` | `短视频与直播` |
| [Retrieval-Grounded-Credit](../papers/retrieval-grounded-credit.md) | arXiv’26 | IV × Training | `Text` | `电商` |
| [ROS](../papers/ros.md) | ACL’26 | I × Tokenization | `Text` + `Geo` | `本地生活与 POI` |
| [S2GR](../papers/s2gr.md) | KDD’26 | III × Backbone | `Text` + `CF` | `电商` · `短视频与直播` |
| [SAHL](../papers/sahl.md) | arXiv’26 | IV × Training | `Text` | `电商` |
| [SAPO](../papers/sapo.md) | arXiv’26 | IV × Training | `Text` | `电商` |
| [SCRec](../papers/screc.md) | RecSys’26 | I × Representation | `Text` + `CF` | `电商` |
| [SID-MLP](../papers/sid-mlp.md) | arXiv’26 | V × Backbone | `Text` | `电商` |
| [SIDReasoner](../papers/sidreasoner.md) | KDD’26 | III × Training | `Text` | `电商` |
| [SPAR](../papers/spar.md) | arXiv’26 | I × Representation | `Text` + `Geo` | `本地生活与 POI` |
| [SpecGR](../papers/specgr.md) | AAAI’26 | VI × Inference | `Text` | `电商` |
| [SPRIG](../papers/sprig.md) | CIKM’26 Short | I × Tokenization | A: `Text` · B: `Audio` | `电影` · `音乐` |
| [SPRINT](../papers/sprint.md) | arXiv’26 | V × Backbone | `Text` | `电商` · `本地生活与 POI` |
| [SST](../papers/sst.md) | CIKM’26 | III × Tokenization | `Text` | `电商` · `本地生活与 POI` |
| [STAMP](../papers/stamp.md) | arXiv’26 | V × Backbone | A: `Text` · B: `Text` + `Img` + `unknown` | `电商` |
| [SynGR](../papers/syngr.md) | ICML’26 | I × Training | text: `Text` · image: `Img` | `电商` |
| [TCBSA](../papers/tcbsa.md) | arXiv’26 | IV × Inference | `Text` | `电商` · `本地生活与 POI` |
| [Tlow](../papers/tlow.md) | CIKM’26 Applied | I × Tokenization | A: `Text` · B: `Text` + `Img` | `电商` · `图文与文章` |
| [Token-Weighted](../papers/token-weighted.md) | CIKM’26 | IV × Training | `Text` | `电商` · `本地生活与 POI` · `电影` |
| [TopoGR](../papers/topogr.md) | arXiv’26 | III × Tokenization | `Text` | `电商` |
| [TRACER](../papers/tracer.md) | NeurIPS’26 | IV × Tokenization | `Text` | `电商` |
| [TrieRec](../papers/trierec.md) | NeurIPS’26 | III × Backbone | `Text` | `电商` · `电影` |
| [UGR](../papers/ugr.md) | KDD’26 | IV × Training | `Text` | `电商` · `本地生活与 POI` |
| [UniTok](../papers/unitok.md) | AAAI’26 | VI × Tokenization | `Text` | `电商` · `本地生活与 POI` |
| [VarLenRec (TIGER)](../papers/varlenrec-tiger.md) | arXiv’26 | I × Tokenization | `Text` | `电商` · `本地生活与 POI` |

## 单一非文本

> 共 8 篇。至少一个构码分支的内容模态只有一种，且不是 `Text` 或未细分的 `MM`（即 `Img`、`Audio` 或 `Video`）。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | collaborative: `CF` · text: `Text` · visual: `Img` | `电商` |
| [MQL4GRec](../papers/mql4grec.md) | ICLR’25 | I × Tokenization | text: `Text` · image: `Img` | `电商` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | text: `Text` · image: `Img` · audio: `Audio` · joint_Amazon: `Text` + `Img` · joint_Music: `Text` + `Audio` | `电商` · `音乐` |
| [MACRec](../papers/macrec.md) | AAAI’26 | I × Tokenization | text: `Text` · image: `Img` | `电商` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | image: `Img` · text: `Text` · collaborative: `CF` | `电商` · `短视频与直播` |
| [NEO](../papers/neo.md) | arXiv’26 | 范式、系统与基准 | A: `Text` · B: `Audio` | `音乐` · `播客` · `图书与有声书` · `搜索` |
| [SPRIG](../papers/sprig.md) | CIKM’26 Short | I × Tokenization | A: `Text` · B: `Audio` | `电影` · `音乐` |
| [SynGR](../papers/syngr.md) | ICML’26 | I × Training | text: `Text` · image: `Img` | `电商` |

## 多模态

> 共 36 篇。至少一个构码分支包含两种以上内容模态，或包含 `MM`。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I × Tokenization | `Text` + `Img` + `CF` | `电商` · `广告` |
| [FORGE](../papers/forge.md) | KDD’26 | 范式、系统与基准 | `Text` + `Img` + `CF` | `电商` · `搜索` |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I × Representation | `MM` + `Geo` | `本地生活与 POI` |
| [OneRec](../papers/onerec.md) | arXiv’25 | 范式、系统与基准 | `MM` + `CF` | `短视频与直播` |
| [OneRec-Think](../papers/onerec-think.md) | arXiv’25 | III × Training | `MM` + `CF` | `电商` · `短视频与直播` |
| [OneRec-V2](../papers/onerec-v2.md) | arXiv’25 | V × Backbone | `Text` + `Img` + `CF` | `短视频与直播` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | text: `Text` · image: `Img` · audio: `Audio` · joint_Amazon: `Text` + `Img` · joint_Music: `Text` + `Audio` | `电商` · `音乐` |
| [Q-BERT4Rec](../papers/q-bert4rec.md) | arXiv’25 | I × Representation | `Text` + `Img` | `电商` |
| [UTGRec](../papers/utgrec.md) | arXiv’25 | VI × Tokenization | `Text` + `Img` + `CF` | `电商` |
| [AdaSID](../papers/adasid.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `电商` |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | A: `unknown` · B: `Text` + `Img` + `CF` | `电商` · `工业场景未明` |
| [CARD](../papers/card.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `电商` |
| [CMRec](../papers/cmrec.md) | CIKM’26 Short | VI × Training | `Text` + `Img` + `CF` | `广告` · `电商` |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV × Training | A: `unknown` · B: `Text` + `Img` | `音乐` · `电商` |
| [GenRec-JD](../papers/genrec-jd.md) | SIGIR’26 | IV × Training | `Text` + `Img` + `CF` | `电商` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text` + `Img` + `Geo` + `CF` | `本地生活与 POI` |
| [HASTE](../papers/haste.md) | arXiv’26 | IV × Training | A: `Text` · B: `MM` | `电商` |
| [MMGRec](../papers/mmgrec.md) | TOMM’26 | I × Tokenization | `Text` + `Img` + `Audio` + `CF` | `电影` · `短视频与直播` |
| [MMQ](../papers/mmq.md) | WSDM’26 | I × Tokenization | `Text` + `Img` | `电商` · `广告` |
| [OneLatent](../papers/onelatent.md) | arXiv’26 | V × Training | `MM` | `广告` · `本地生活与 POI` |
| [OneLive](../papers/onelive.md) | KDD’26 ADS | VI × Tokenization | `Text` + `Img` + `Audio` + `CF` | `短视频与直播` |
| [OneMall](../papers/onemall.md) | CIKM’26 | 范式、系统与基准 | A: `Text` + `Img` + `CF` · B: `Text` + `Img` + `CF` · C: `CF` + `unknown` | `电商` |
| [OneRec-V2-Quantized](../papers/onerec-v2-quantized.md) | arXiv’26 | V × Inference | `Text` + `Img` + `CF` | `短视频与直播` |
| [PinGER](../papers/pinger.md) | arXiv’26 | V × Backbone | `Text` + `Img` + `CF` | `图文与文章` |
| [PLUM](../papers/plum.md) | WWW’26 | 范式、系统与基准 | `MM` + `CF` | `长视频` · `短视频与直播` |
| [PrefixMem](../papers/prefixmem.md) | arXiv’26 | III × Backbone | `MM` | `图文与文章` |
| [QuaSID](../papers/quasid.md) | KDD’26 ADS | II × Tokenization | `Text` + `Img` + `CF` | `电商` |
| [RecoChain](../papers/recochain.md) | arXiv’26 | IV × Backbone | `MM` | `电商` |
| [RoFiGR](../papers/rofigr.md) | arXiv’26 | I × Tokenization | text: `Text` + `Img` + `CF` · image: `Text` + `Img` + `CF` | `电商` |
| [SAGE-SID](../papers/sage-sid.md) | arXiv’26 | IV × Training | `Text` + `Img` | `电商` · `短视频与直播` · `广告` |
| [SnapLGR](../papers/snaplgr.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `短视频与直播` |
| [STAMP](../papers/stamp.md) | arXiv’26 | V × Backbone | A: `Text` · B: `Text` + `Img` + `unknown` | `电商` |
| [Tlow](../papers/tlow.md) | CIKM’26 Applied | I × Tokenization | A: `Text` · B: `Text` + `Img` | `电商` · `图文与文章` |
| [TriAlignGR](../papers/trialigngr.md) | arXiv’26 | I × Representation | `Text` + `Img` | `电商` |
| [UniRec](../papers/unirec.md) | arXiv’26 | I × Tokenization | `MM` + `Attr` | `电商` |
| [UniSID](../papers/unisid.md) | arXiv’26 | I × Tokenization | `Text` + `Img` | `广告` · `电商` |

## 无内容模态

> 共 11 篇。所有构码分支都不含内容模态（`Text`、`Img`、`Audio`、`Video`、`MM`），且所有分支合起来不含 `unknown`（及 `n/a`）。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [CID](../papers/cid.md) | SIGIR-AP’23 | II × Tokenization | `CF` | `电商` · `本地生活与 POI` |
| [ColaRec](../papers/colarec.md) | CIKM’24 | I × Backbone | `CF` | `电商` · `美食与食谱` |
| [MBGen](../papers/mbgen.md) | CIKM’24 | I × Training | `CF` | `电商` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `CF` | `本地生活与 POI` · `电商` · `新闻` · `短视频与直播` |
| [ETEGRec](../papers/etegrec.md) | SIGIR’25 | III × Training | `CF` | `电商` |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `本地生活与 POI` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr` + `Geo` + `CF` | `本地生活与 POI` |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `Geo` | `本地生活与 POI` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I × Tokenization | `CF` | `音乐` · `电影` · `电商` |
| [KL-MOPD](../papers/kl-mopd.md) | arXiv’26 | IV × Training | `CF` | `电商` · `广告` |
| [ReSID](../papers/resid.md) | arXiv’26 | I × Representation | `Attr` + `CF` | `电商` |

## 仅协同信号

> 共 7 篇。所有构码分支合起来只有 `CF`。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [CID](../papers/cid.md) | SIGIR-AP’23 | II × Tokenization | `CF` | `电商` · `本地生活与 POI` |
| [ColaRec](../papers/colarec.md) | CIKM’24 | I × Backbone | `CF` | `电商` · `美食与食谱` |
| [MBGen](../papers/mbgen.md) | CIKM’24 | I × Training | `CF` | `电商` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `CF` | `本地生活与 POI` · `电商` · `新闻` · `短视频与直播` |
| [ETEGRec](../papers/etegrec.md) | SIGIR’25 | III × Training | `CF` | `电商` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I × Tokenization | `CF` | `音乐` · `电影` · `电商` |
| [KL-MOPD](../papers/kl-mopd.md) | arXiv’26 | IV × Training | `CF` | `电商` · `广告` |

## 含协同信号

> 共 50 篇。所有构码分支合起来含 `CF`，且还有其他模态或信号。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [EAGER](../papers/eager.md) | KDD’24 | I × Backbone | semantic: `Text` · behavior: `CF` | `电商` · `本地生活与 POI` |
| [LETTER](../papers/letter.md) | CIKM’24 | I × Tokenization | `Text` + `CF` | `电商` · `本地生活与 POI` |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I × Tokenization | `Text` + `Img` + `CF` | `电商` · `广告` |
| [DAS](../papers/das.md) | CIKM’25 | I × Tokenization | `Text` + `CF` | `广告` |
| [DiscRec](../papers/discrec.md) | arXiv’25 | I × Backbone | A: `Text` · B: `Text` + `CF` | `电商` |
| [EAGER-LLM](../papers/eager-llm.md) | WWW’25 | I × Tokenization | semantic: `Text` · behavior: `CF` | `电商` |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I × Tokenization | semantic: `Text` + `CF` · collaborative: `CF` | `电商` · `短视频与直播` · `工业场景未明` |
| [FORGE](../papers/forge.md) | KDD’26 | 范式、系统与基准 | `Text` + `Img` + `CF` | `电商` · `搜索` |
| [GenSAR](../papers/gensar.md) | RecSys’25 | I × Tokenization | semantic: `Text` + `CF` · collaborative: `Text` + `CF` | `电商` · `搜索` |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `本地生活与 POI` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr` + `Geo` + `CF` | `本地生活与 POI` |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | collaborative: `CF` · text: `Text` · visual: `Img` | `电商` |
| [OneRec](../papers/onerec.md) | arXiv’25 | 范式、系统与基准 | `MM` + `CF` | `短视频与直播` |
| [OneRec-Think](../papers/onerec-think.md) | arXiv’25 | III × Training | `MM` + `CF` | `电商` · `短视频与直播` |
| [OneRec-V2](../papers/onerec-v2.md) | arXiv’25 | V × Backbone | `Text` + `Img` + `CF` | `短视频与直播` |
| [SemConv](../papers/semconv.md) | AAAI’25 | III × Tokenization | `Text` + `CF` | `电商` |
| [UNGER](../papers/unger.md) | TOIS’25 | I × Representation | `Text` + `CF` | `电商` |
| [UTGRec](../papers/utgrec.md) | arXiv’25 | VI × Tokenization | `Text` + `Img` + `CF` | `电商` |
| [AdaSID](../papers/adasid.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `电商` |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III × Tokenization | `Text` + `CF` | `电商` · `本地生活与 POI` · `广告` |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | A: `unknown` · B: `Text` + `Img` + `CF` | `电商` · `工业场景未明` |
| [CARD](../papers/card.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `电商` |
| [CMRec](../papers/cmrec.md) | CIKM’26 Short | VI × Training | `Text` + `Img` + `CF` | `广告` · `电商` |
| [DACT](../papers/dact.md) | SIGIR’26 | VI × Tokenization | `Text` + `CF` | `电商` |
| [DOS](../papers/dos.md) | WWW’26 Short | III × Tokenization | `Text` + `CF` | `本地生活与 POI` |
| [DREAM](../papers/dream.md) | arXiv’26 | VI × Tokenization | `Text` + `CF` | `电商` |
| [GenRec-JD](../papers/genrec-jd.md) | SIGIR’26 | IV × Training | `Text` + `Img` + `CF` | `电商` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `Text` + `Geo` + `CF` | `本地生活与 POI` · `搜索` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | A: `Text` · B: `Text` + `CF` | `本地生活与 POI` · `电商` · `广告` · `搜索` |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I × Tokenization | `Text` + `CF` | `电商` · `新闻` · `本地生活与 POI` |
| [GTI](../papers/gti.md) | arXiv’26 | III × Training | A: `Text` + `CF` · B: `Text` | `招聘` · `电商` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text` + `Img` + `Geo` + `CF` | `本地生活与 POI` |
| [LESSRec](../papers/lessrec.md) | arXiv’26 | III × Backbone | A: `Text` · B: `Text` + `CF` | `电商` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text` + `Geo` + `Attr` + `CF` | `本地生活与 POI` |
| [MMGRec](../papers/mmgrec.md) | TOMM’26 | I × Tokenization | `Text` + `Img` + `Audio` + `CF` | `电影` · `短视频与直播` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | image: `Img` · text: `Text` · collaborative: `CF` | `电商` · `短视频与直播` |
| [OneLive](../papers/onelive.md) | KDD’26 ADS | VI × Tokenization | `Text` + `Img` + `Audio` + `CF` | `短视频与直播` |
| [OneMall](../papers/onemall.md) | CIKM’26 | 范式、系统与基准 | A: `Text` + `Img` + `CF` · B: `Text` + `Img` + `CF` · C: `CF` + `unknown` | `电商` |
| [OneRec-V2-Quantized](../papers/onerec-v2-quantized.md) | arXiv’26 | V × Inference | `Text` + `Img` + `CF` | `短视频与直播` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `Text` + `CF` | `电商` · `本地生活与 POI` |
| [PCR-CA](../papers/pcr-ca.md) | KDD’26 | I × Tokenization | `Text` + `CF` | `应用商店` |
| [Pctx](../papers/pctx.md) | CIKM’26 | I × Tokenization | `Text` + `CF` | `电商` |
| [PinGER](../papers/pinger.md) | arXiv’26 | V × Backbone | `Text` + `Img` + `CF` | `图文与文章` |
| [PLUM](../papers/plum.md) | WWW’26 | 范式、系统与基准 | `MM` + `CF` | `长视频` · `短视频与直播` |
| [QuaSID](../papers/quasid.md) | KDD’26 ADS | II × Tokenization | `Text` + `Img` + `CF` | `电商` |
| [ReSID](../papers/resid.md) | arXiv’26 | I × Representation | `Attr` + `CF` | `电商` |
| [RoFiGR](../papers/rofigr.md) | arXiv’26 | I × Tokenization | text: `Text` + `Img` + `CF` · image: `Text` + `Img` + `CF` | `电商` |
| [S2GR](../papers/s2gr.md) | KDD’26 | III × Backbone | `Text` + `CF` | `电商` · `短视频与直播` |
| [SCRec](../papers/screc.md) | RecSys’26 | I × Representation | `Text` + `CF` | `电商` |
| [SnapLGR](../papers/snaplgr.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `短视频与直播` |

## 结构化属性

> 共 7 篇。所有构码分支合起来含结构化属性（`Attr`）。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `本地生活与 POI` |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II × Tokenization | `Text` + `Attr` | `电商` · `短视频与直播` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr` + `Geo` + `CF` | `本地生活与 POI` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `Text` + `Attr` + `Geo` | `本地生活与 POI` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text` + `Geo` + `Attr` + `CF` | `本地生活与 POI` |
| [ReSID](../papers/resid.md) | arXiv’26 | I × Representation | `Attr` + `CF` | `电商` |
| [UniRec](../papers/unirec.md) | arXiv’26 | I × Tokenization | `MM` + `Attr` | `电商` |

## 地理空间

> 共 14 篇。所有构码分支合起来含地理或空间特征（`Geo`）。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `本地生活与 POI` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr` + `Geo` + `CF` | `本地生活与 POI` |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I × Representation | `MM` + `Geo` | `本地生活与 POI` |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I × Tokenization | `Text` + `Geo` | `本地生活与 POI` |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `Geo` | `本地生活与 POI` |
| [AWARE](../papers/aware.md) | arXiv’26 | VI × Training | `Text` + `Geo` | `本地生活与 POI` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `Text` + `Geo` + `CF` | `本地生活与 POI` · `搜索` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text` + `Img` + `Geo` + `CF` | `本地生活与 POI` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `Text` + `Attr` + `Geo` | `本地生活与 POI` |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I × Representation | `Text` + `Geo` | `本地生活与 POI` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text` + `Geo` + `Attr` + `CF` | `本地生活与 POI` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `Text` + `Geo` | `本地生活与 POI` · `搜索` |
| [ROS](../papers/ros.md) | ACL’26 | I × Tokenization | `Text` + `Geo` | `本地生活与 POI` |
| [SPAR](../papers/spar.md) | arXiv’26 | I × Representation | `Text` + `Geo` | `本地生活与 POI` |

## 时间特征

> 共 2 篇。所有构码分支合起来含时间特征（`Time`）。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `本地生活与 POI` |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I × Tokenization | `Text` + `Time` | `电商` |

## 待明确

> 共 28 篇。构码输入模态整体或部分未明（至少一个分支含 `unknown`；待核信号见 `modality_open`）。

| 论文 | 发表 | 问题 × 阶段 | 构码输入 | 领域 |
| :--- | :--- | :--- | :--- | :--- |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | A: `unknown` · B: `Text` + `Img` + `CF` | `电商` · `工业场景未明` |
| [DASO](../papers/daso.md) | arXiv’26 | IV × Training | `Text` + `unknown` | `电商` · `工业场景未明` |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | A: `Text` · B: `unknown` | `电商` · `电影` · `音乐` |
| [DiGR](../papers/digr.md) | arXiv’26 | IV × Backbone | `unknown` | `电商` |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV × Training | A: `unknown` · B: `Text` + `Img` | `音乐` · `电商` |
| [DualGR](../papers/dualgr.md) | WWW’26 Short | VI × Backbone | `unknown` | `短视频与直播` |
| [Dynamic-Single-Codebook](../papers/dynamic-single-codebook.md) | arXiv’26 | V × Tokenization | `unknown` | `电商` · `短视频与直播` · `工业场景未明` |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI × Tokenization | `Text` + `unknown` | `电商` · `图书与有声书` · `电影` |
| [GR4AD-X](../papers/gr4ad-x.md) | arXiv’26 | III × Tokenization | `unknown` | `广告` |
| [Gryphon](../papers/gryphon.md) | CIKM’26 Short | IV × Backbone | `unknown` | `音乐` |
| [HCGRec](../papers/hcgrec.md) | CIKM’26 | IV × Training | `unknown` | `电商` |
| [HoloRec](../papers/holorec.md) | arXiv’26 | III × Tokenization | `unknown` | `电商` |
| [Latte](../papers/latte.md) | arXiv’26 | III × Backbone | `unknown` | `电商` · `音乐` |
| [MBGR](../papers/mbgr.md) | arXiv’26 | VI × Tokenization | `unknown` | `工业场景未明` |
| [MuSID-KD](../papers/musid-kd.md) | arXiv’26 | IV × Training | `unknown` | `电商` · `游戏` |
| [NAU](../papers/nau.md) | arXiv’26 | IV × Training | `unknown` | `电商` |
| [Netflix-SID-Comparison](../papers/netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | 范式、系统与基准 | `unknown` | `长视频` |
| [OneChord](../papers/onechord.md) | arXiv’26 | IV × Training | `unknown` | `电商` |
| [OneMall](../papers/onemall.md) | CIKM’26 | 范式、系统与基准 | A: `Text` + `Img` + `CF` · B: `Text` + `Img` + `CF` · C: `CF` + `unknown` | `电商` |
| [PFA](../papers/pfa.md) | arXiv’26 | V × Inference | `unknown` | `电商` · `广告` |
| [SIDScope](../papers/sidscope.md) | arXiv’26 | 范式、系统与基准 | `unknown` | `电商` · `本地生活与 POI` |
| [SLIDE](../papers/slide.md) | arXiv’26 | IV × Training | `unknown` | `电商` · `搜索` |
| [SPAR-Youku](../papers/spar-youku.md) | arXiv’26 | I × Backbone | `unknown` | `长视频` |
| [STAMP](../papers/stamp.md) | arXiv’26 | V × Backbone | A: `Text` · B: `Text` + `Img` + `unknown` | `电商` |
| [STATIC](../papers/static.md) | KDD’26 ADS | V × Inference | `unknown` | `电商` · `视频` |
| [Think2Go](../papers/think2go.md) | KDD’26 | III × Training | `unknown` | `本地生活与 POI` |
| [UniSGR-V2](../papers/unisgr-v2.md) | arXiv’26 | I × Backbone | `unknown` | `电商` |
| [V-STAR](../papers/v-star.md) | KDD’26 | IV × Training | `unknown` | `电商` · `广告` |
