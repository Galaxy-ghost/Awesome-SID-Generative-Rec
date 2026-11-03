# 按构码输入模态索引

[English](../../index/modality.md) | 中文

本页按综述 Table 1 `representation` 列（或记录中的 `modality` 覆盖字段）所报告的构码输入内容模态与协同过滤（`CF`）信号分组列出论文。此处的“协同”仅指构码输入中包含 `CF`，不代表生成骨干或训练目标中的协同信号。`A / B` 双分支配置分别列入各分支对应小节，各小节计不同论文数。

| 内容模态    | 未标 CF           | 含协同（CF）                  |
| :------ | :-------------- | :----------------------- |
| **单模态** | [单模态（82）](#单模态) | [单模态 + 协同（32）](#单模态--协同) |
| **多模态** | [多模态（15）](#多模态) | [多模态 + 协同（21）](#多模态--协同) |
| **其他**  | [其他（1）](#其他)    | [其他 + 协同（10）](#其他--协同)   |

**表征未明**：[25 篇](#表征未明)（`–`、`Multi-Dom`、`Cross-Dom` 或含未报告分支）。

**不适用**：[1 篇](#不适用)（`n/a`）。

**附加信号**：[`Geo`（15）](#geo) · [`Time`（1）](#time) · [`SID`（5）](#sid)。

## 单模态

> 构码输入含单一内容模态（`Text` 或 `Audio`），未标 `CF`。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [TIGER](../papers/tiger.md) | NeurIPS’23 | 范式、系统与基准 | `Text` | – |
| [CoST](../papers/cost.md) | RecSys’24 | I × Tokenization | `Text` | – |
| [IDGenRec](../papers/idgenrec.md) | SIGIR’24 | III × Tokenization | `Text` | – |
| [LC-Rec](../papers/lc-rec.md) | ICDE’24 | III × Training | `Text` | – |
| [LIGER](../papers/liger.md) | arXiv’24 | VI × Inference | `Text+SID` | `SID` |
| [LMIndexer](../papers/lmindexer.md) | ICML’24 | I × Tokenization | `Text` | – |
| [SIIT](../papers/siit.md) | arXiv’24 | III × Tokenization | `Text` | – |
| [TransRec](../papers/transrec.md) | KDD’24 | II × Tokenization | `Text` | – |
| [ActionPiece](../papers/actionpiece.md) | ICML’25 | I × Tokenization | `Text` | – |
| [AtSpeed](../papers/atspeed.md) | ICLR’25 | V × Inference | `Text` | – |
| [COBRA](../papers/cobra.md) | NeurIPS’25 | I × Backbone | `Text+SID` | `SID` |
| [GRID](../papers/grid.md) | CIKM’25 | 范式、系统与基准 | `Text` | – |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II × Tokenization | `Text` | – |
| [LLaDA-Rec](../papers/llada-rec.md) | arXiv’25 | III × Backbone | `Text` | – |
| [MiniOneRec](../papers/minionerec.md) | arXiv’25 | 范式、系统与基准 | `Text` | – |
| [PSI](../papers/psi.md) | arXiv’25 | II × Tokenization | `Text` | – |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I × Tokenization | `Text+Geo` | `Geo` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `Text` | – |
| [RPG](../papers/rpg.md) | KDD’25 | V × Backbone | `Text` | – |
| [ACERec](../papers/acerec.md) | arXiv’26 | V × Backbone | `Text` | – |
| [APAO](../papers/apao.md) | KDD’26 | IV × Training | `Text` | – |
| [API](../papers/api.md) | arXiv’26 | II × Tokenization | `Text` | – |
| [AWARE](../papers/aware.md) | arXiv’26 | VI × Training | `Text+Geo` | `Geo` |
| [CAPE](../papers/cape.md) | arXiv’26 | I × Inference | `Text†` | – |
| [CausalDPO](../papers/causaldpo.md) | ICML’26 | VI × Training | `Text` | – |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I × Tokenization | `Text+Time` | `Time` |
| [CITE](../papers/cite.md) | Electronics’26 | I × Inference | `Text` | – |
| [CogRec](../papers/cogrec.md) | arXiv’26 | III × Tokenization | `Text` | – |
| [DASO](../papers/daso.md) | arXiv’26 | IV × Training | `Text` | – |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | `Text / –` | – |
| [DIGER](../papers/diger.md) | SIGIR’26 | II × Tokenization | `Text` | – |
| [Evo-Rec](../papers/evo-rec.md) | arXiv’26 | III × Training | `Text` | – |
| [FedCGR](../papers/fedcgr.md) | CIKM’26 | VI × Backbone | `Text` | – |
| [FLASH](../papers/flash.md) | NeurIPS’26 | III × Backbone | `Text` | – |
| [GEM-Rec](../papers/gem-rec.md) | arXiv’26 | IV × Training | `Text` | – |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | `Text / Text+CF` | – |
| [Ghost](../papers/ghost.md) | NeurIPS’26 | IV × Training | `Text` | – |
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | 范式、系统与基准 | `Text+SID` | `SID` |
| [GRLM](../papers/grlm.md) | arXiv’26 | III × Tokenization | `Text` | – |
| [GTI](../papers/gti.md) | arXiv’26 | III × Training | `Text+CF / Text` | – |
| [HASTE](../papers/haste.md) | arXiv’26 | IV × Training | `Text / MM` | – |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `Text+Attr+Geo` | `Geo` |
| [IBA](../papers/iba.md) | arXiv’26 | V × Backbone | `Text` | – |
| [IDM/CMM](../papers/idm-cmm.md) | arXiv’26 | IV × Training | `Text` | – |
| [Intent-Driven-News](../papers/intent-driven-news.md) | ACL’26 Industry | III × Training | `Text` | – |
| [ISD](../papers/isd.md) | arXiv’26 | IV × Inference | `Text†` | – |
| [JevRec](../papers/jevrec.md) | arXiv’26 | V × Tokenization | `Text` | – |
| [LESSRec](../papers/lessrec.md) | arXiv’26 | III × Backbone | `Text / Text+CF` | – |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I × Representation | `Text+Geo` | `Geo` |
| [LION](../papers/lion.md) | CIKM’26 | VI × Backbone | `Text†` | – |
| [LoopGR](../papers/loopgr.md) | arXiv’26 | V × Backbone | `Text` | – |
| [Merge-and-Branch](../papers/merge-and-branch.md) | arXiv’26 | V × Backbone | `Text` | – |
| [NEO](../papers/neo.md) | arXiv’26 | 范式、系统与基准 | `Text / Audio` | – |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V × Inference | `Text` | – |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `Text+SID` | `SID` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `Text+Geo` | `Geo` |
| [PROMISE](../papers/promise.md) | arXiv’26 | III × Inference | `Text` | – |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II × Tokenization | `Text` | – |
| [RAGR](../papers/ragr.md) | arXiv’26 | I × Training | `Text` | – |
| [REGER](../papers/reger.md) | arXiv’26 | I × Training | `Text` | – |
| [ReRankID](../papers/rerankid.md) | arXiv’26 | 范式、系统与基准 | `Text` | – |
| [Retrieval-Grounded-Credit](../papers/retrieval-grounded-credit.md) | arXiv’26 | IV × Training | `Text†` | – |
| [ROS](../papers/ros.md) | ACL’26 | I × Tokenization | `Text+Geo` | `Geo` |
| [SAHL](../papers/sahl.md) | arXiv’26 | IV × Training | `Text` | – |
| [SAPO](../papers/sapo.md) | arXiv’26 | IV × Training | `Text` | – |
| [SID-MLP](../papers/sid-mlp.md) | arXiv’26 | V × Backbone | `Text` | – |
| [SIDReasoner](../papers/sidreasoner.md) | KDD’26 | III × Training | `Text` | – |
| [SPAR](../papers/spar.md) | arXiv’26 | I × Representation | `Text+Geo` | `Geo` |
| [SpecGR](../papers/specgr.md) | AAAI’26 | VI × Inference | `Text+SID` | `SID` |
| [SPRIG](../papers/sprig.md) | CIKM’26 Short | I × Tokenization | `Text / Audio` | – |
| [SPRINT](../papers/sprint.md) | arXiv’26 | V × Backbone | `Text` | – |
| [SST](../papers/sst.md) | CIKM’26 | III × Tokenization | `Text` | – |
| [STAMP](../papers/stamp.md) | arXiv’26 | V × Backbone | `Text` | – |
| [TCBSA](../papers/tcbsa.md) | arXiv’26 | IV × Inference | `Text` | – |
| [Tlow](../papers/tlow.md) | CIKM’26 Applied | I × Tokenization | `Text` | – |
| [Token-Weighted](../papers/token-weighted.md) | CIKM’26 | IV × Training | `Text` | – |
| [TopoGR](../papers/topogr.md) | arXiv’26 | III × Tokenization | `Text` | – |
| [TRACER](../papers/tracer.md) | NeurIPS’26 | IV × Tokenization | `Text` | – |
| [TrieRec](../papers/trierec.md) | NeurIPS’26 | III × Backbone | `Text` | – |
| [UGR](../papers/ugr.md) | KDD’26 | IV × Training | `Text` | – |
| [V-STAR](../papers/v-star.md) | KDD’26 | IV × Training | `Text†` | – |
| [VarLenRec (TIGER)](../papers/varlenrec-tiger.md) | arXiv’26 | I × Tokenization | `Text` | – |

## 单模态 + 协同

> 构码输入含单一内容模态并融合协同过滤信号（`CF`）。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [ColaRec](../papers/colarec.md) | CIKM’24 | I × Backbone | `Text+CF` | – |
| [EAGER](../papers/eager.md) | KDD’24 | I × Backbone | `Text+CF` | – |
| [LETTER](../papers/letter.md) | CIKM’24 | I × Tokenization | `Text+CF` | – |
| [DAS](../papers/das.md) | CIKM’25 | I × Tokenization | `Text+CF` | – |
| [DiscRec](../papers/discrec.md) | arXiv’25 | I × Backbone | `Text+CF` | – |
| [EAGER-LLM](../papers/eager-llm.md) | WWW’25 | I × Tokenization | `Text+CF` | – |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I × Tokenization | `Text+CF` | – |
| [GenSAR](../papers/gensar.md) | RecSys’25 | I × Tokenization | `Text+CF` | – |
| [GRAM](../papers/gram.md) | ACL’25 | I × Tokenization | `Text+CF` | – |
| [GREAM](../papers/gream.md) | arXiv’25 | III × Training | `Text+CF` | – |
| [SemConv](../papers/semconv.md) | AAAI’25 | III × Tokenization | `Text+CF` | – |
| [UNGER](../papers/unger.md) | TOIS’25 | I × Representation | `Text+CF` | – |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III × Tokenization | `Text+CF` | – |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | `Text+CF` | – |
| [DACT](../papers/dact.md) | SIGIR’26 | VI × Tokenization | `Text+CF` | – |
| [DECOR](../papers/decor.md) | SIGIR’26 | III × Backbone | `Text+CF` | – |
| [DOS](../papers/dos.md) | WWW’26 Short | III × Tokenization | `Text+CF` | – |
| [DREAM](../papers/dream.md) | arXiv’26 | VI × Tokenization | `Text+CF` | – |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `Text+Geo+CF` | `Geo` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | `Text / Text+CF` | – |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I × Tokenization | `Text+CF` | – |
| [GTI](../papers/gti.md) | arXiv’26 | III × Training | `Text+CF / Text` | – |
| [Latte](../papers/latte.md) | arXiv’26 | III × Backbone | `Text+CF` | – |
| [LESSRec](../papers/lessrec.md) | arXiv’26 | III × Backbone | `Text / Text+CF` | – |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text+Geo+CF` | `Geo` |
| [MBGR](../papers/mbgr.md) | arXiv’26 | VI × Tokenization | `Text+CF` | – |
| [PCR-CA](../papers/pcr-ca.md) | KDD’26 | I × Tokenization | `Text+CF` | – |
| [Pctx](../papers/pctx.md) | CIKM’26 | I × Tokenization | `Text+CF` | – |
| [QuaSID](../papers/quasid.md) | KDD’26 ADS | II × Tokenization | `Text+CF` | – |
| [S2GR](../papers/s2gr.md) | KDD’26 | III × Backbone | `Text+CF` | – |
| [SCRec](../papers/screc.md) | RecSys’26 | I × Representation | `Text+CF` | – |
| [UniRec](../papers/unirec.md) | arXiv’26 | I × Tokenization | `Text+CF` | – |

## 多模态

> 构码输入含两种及以上内容模态（或 `MM`），未标 `CF`。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [MQL4GRec](../papers/mql4grec.md) | ICLR’25 | I × Tokenization | `Text+Img` | – |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I × Representation | `Text+Img+Geo†` | `Geo` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | `Text+Img` | – |
| [AdaSID](../papers/adasid.md) | arXiv’26 | II × Tokenization | `Text+Img` | – |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV × Training | `– / Text+Img` | – |
| [HASTE](../papers/haste.md) | arXiv’26 | IV × Training | `Text / MM` | – |
| [MACRec](../papers/macrec.md) | AAAI’26 | I × Tokenization | `Text+Img` | – |
| [MMQ](../papers/mmq.md) | WSDM’26 | I × Tokenization | `Text+Img` | – |
| [OneLatent](../papers/onelatent.md) | arXiv’26 | V × Training | `MM` | – |
| [PrefixMem](../papers/prefixmem.md) | arXiv’26 | III × Backbone | `MM` | – |
| [RecoChain](../papers/recochain.md) | arXiv’26 | IV × Backbone | `Text+Img` | – |
| [SAGE-SID](../papers/sage-sid.md) | arXiv’26 | IV × Training | `Text+Img†` | – |
| [SynGR](../papers/syngr.md) | ICML’26 | I × Training | `Text+Img` | – |
| [TriAlignGR](../papers/trialigngr.md) | arXiv’26 | I × Representation | `Text+Img` | – |
| [UniSID](../papers/unisid.md) | arXiv’26 | I × Tokenization | `Text+Img+Attr` | – |

## 多模态 + 协同

> 构码输入含两种及以上内容模态（或 `MM`）并融合协同过滤信号（`CF`）。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [Molar](../papers/molar.md) | arXiv’24 | I × Representation | `Text+Img+CF` | – |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I × Tokenization | `Text+Img+CF` | – |
| [FORGE](../papers/forge.md) | KDD’26 | 范式、系统与基准 | `Text+Img+CF` | – |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | `Text+Img+CF` | – |
| [OneRec](../papers/onerec.md) | arXiv’25 | 范式、系统与基准 | `MM+CF` | – |
| [OneRec-Think](../papers/onerec-think.md) | arXiv’25 | III × Training | `Text+Img+CF†` | – |
| [OneRec-V2](../papers/onerec-v2.md) | arXiv’25 | V × Backbone | `Text+Img+CF†` | – |
| [Q-BERT4Rec](../papers/q-bert4rec.md) | arXiv’25 | I × Representation | `Text+Img+CF` | – |
| [CARD](../papers/card.md) | arXiv’26 | II × Tokenization | `Text+Img+CF` | – |
| [CMRec](../papers/cmrec.md) | CIKM’26 Short | VI × Training | `Text+Img+CF` | – |
| [GenRec-JD](../papers/genrec-jd.md) | SIGIR’26 | IV × Training | `Text+Img+CF` | – |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text+Img+Geo+CF` | `Geo` |
| [MMGRec](../papers/mmgrec.md) | TOMM’26 | I × Tokenization | `Text+Img+CF` | – |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | `Text+Img+CF` | – |
| [OneLive](../papers/onelive.md) | KDD’26 ADS | VI × Tokenization | `Text+Img+Audio+CF` | – |
| [OneMall](../papers/onemall.md) | CIKM’26 | 范式、系统与基准 | `Text+Img+CF` | – |
| [OneRec-V2-Quantized](../papers/onerec-v2-quantized.md) | arXiv’26 | V × Inference | `Text+Img+CF†` | – |
| [PinGER](../papers/pinger.md) | arXiv’26 | V × Backbone | `Text+Img+CF` | – |
| [PLUM](../papers/plum.md) | WWW’26 | 范式、系统与基准 | `Text+Img+CF` | – |
| [RoFiGR](../papers/rofigr.md) | arXiv’26 | I × Tokenization | `Text+Img+CF` | – |
| [SnapLGR](../papers/snaplgr.md) | arXiv’26 | II × Tokenization | `Text+Img+CF` | – |

## 其他

> 构码输入仅含非内容模态特征（如纯空间特征），未标 `CF`。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `Geo` | `Geo` |

## 其他 + 协同

> 构码输入为纯协同信号（`CF`）或结构化属性加 `CF`，不含文本、图像或音频模态。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [CID](../papers/cid.md) | SIGIR-AP’23 | II × Tokenization | `CF` | – |
| [MBGen](../papers/mbgen.md) | CIKM’24 | I × Training | `CF` | – |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `CF` | – |
| [ETEGRec](../papers/etegrec.md) | SIGIR’25 | III × Training | `CF` | – |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr+Geo+CF` | `Geo` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr+Geo+CF` | `Geo` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I × Tokenization | `CF` | – |
| [KL-MOPD](../papers/kl-mopd.md) | arXiv’26 | IV × Training | `CF` | – |
| [ReSID](../papers/resid.md) | arXiv’26 | I × Representation | `Attr+CF` | – |
| [Think2Go](../papers/think2go.md) | KDD’26 | III × Training | `Attr+Geo+CF†` | `Geo` |

## 表征未明

> Table 1 的 `representation` 未报告（`–`），或仅记录领域范围（`Multi-Dom`、`Cross-Dom`）且暂无模态覆盖字段。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [VQ-Rec](../papers/vq-rec.md) | WWW’23 | VI × Tokenization | `Multi-Dom` | – |
| [GMC](../papers/gmc.md) | arXiv’25 | VI × Tokenization | `Cross-Dom` | – |
| [UTGRec](../papers/utgrec.md) | arXiv’25 | VI × Tokenization | `Multi-Dom` | – |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | `Text / –` | – |
| [DiGR](../papers/digr.md) | arXiv’26 | IV × Backbone | `–` | – |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV × Training | `– / Text+Img` | – |
| [DualGR](../papers/dualgr.md) | WWW’26 Short | VI × Backbone | `–` | – |
| [Dynamic-Single-Codebook](../papers/dynamic-single-codebook.md) | arXiv’26 | V × Tokenization | `–` | – |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI × Tokenization | `Cross-Dom` | – |
| [GR4AD-X](../papers/gr4ad-x.md) | arXiv’26 | III × Tokenization | `–` | – |
| [GRC](../papers/grc.md) | CIKM’26 | III × Inference | `–` | – |
| [Gryphon](../papers/gryphon.md) | CIKM’26 Short | IV × Backbone | `–` | – |
| [HCGRec](../papers/hcgrec.md) | CIKM’26 | IV × Training | `–` | – |
| [HoloRec](../papers/holorec.md) | arXiv’26 | III × Tokenization | `–` | – |
| [MDGR](../papers/mdgr.md) | arXiv’26 | III × Backbone | `–` | – |
| [MuSID-KD](../papers/musid-kd.md) | arXiv’26 | IV × Training | `–` | – |
| [NAU](../papers/nau.md) | arXiv’26 | IV × Training | `–` | – |
| [Netflix-SID-Comparison](../papers/netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | 范式、系统与基准 | `–` | – |
| [OneChord](../papers/onechord.md) | arXiv’26 | IV × Training | `–` | – |
| [PFA](../papers/pfa.md) | arXiv’26 | V × Inference | `–` | – |
| [SLIDE](../papers/slide.md) | arXiv’26 | IV × Training | `–` | – |
| [SPAR-Youku](../papers/spar-youku.md) | arXiv’26 | I × Backbone | `–` | – |
| [STATIC](../papers/static.md) | KDD’26 ADS | V × Inference | `–` | – |
| [UniSGR-V2](../papers/unisgr-v2.md) | arXiv’26 | I × Backbone | `–` | – |
| [UniTok](../papers/unitok.md) | AAAI’26 | VI × Tokenization | `Multi-Dom` | – |

## 不适用

> 不涉及构码输入表征的诊断资源或非单一方法条目（`n/a`）。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [SIDScope](../papers/sidscope.md) | arXiv’26 | 范式、系统与基准 | `n/a` | – |

## 附加信号

### Geo

> 表征中包含地理或空间特征。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr+Geo+CF` | `Geo` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr+Geo+CF` | `Geo` |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I × Representation | `Text+Img+Geo†` | `Geo` |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I × Tokenization | `Text+Geo` | `Geo` |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `Geo` | `Geo` |
| [AWARE](../papers/aware.md) | arXiv’26 | VI × Training | `Text+Geo` | `Geo` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `Text+Geo+CF` | `Geo` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text+Img+Geo+CF` | `Geo` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `Text+Attr+Geo` | `Geo` |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I × Representation | `Text+Geo` | `Geo` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text+Geo+CF` | `Geo` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `Text+Geo` | `Geo` |
| [ROS](../papers/ros.md) | ACL’26 | I × Tokenization | `Text+Geo` | `Geo` |
| [SPAR](../papers/spar.md) | arXiv’26 | I × Representation | `Text+Geo` | `Geo` |
| [Think2Go](../papers/think2go.md) | KDD’26 | III × Training | `Attr+Geo+CF†` | `Geo` |

### Time

> 表征中包含显式交互时间特征。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I × Tokenization | `Text+Time` | `Time` |

### SID

> 表征中拼接离散 SID（稠密与生成混合检索）。

| 论文 | 发表 | 问题 × 阶段 | 表征（Representation） | 附加信号 |
| :-- | :-- | :-- | :-- | :-- |
| [LIGER](../papers/liger.md) | arXiv’24 | VI × Inference | `Text+SID` | `SID` |
| [COBRA](../papers/cobra.md) | NeurIPS’25 | I × Backbone | `Text+SID` | `SID` |
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | 范式、系统与基准 | `Text+SID` | `SID` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `Text+SID` | `SID` |
| [SpecGR](../papers/specgr.md) | AAAI’26 | VI × Inference | `Text+SID` | `SID` |
