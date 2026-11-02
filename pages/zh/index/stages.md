# 按阶段索引

[English](../../index/stages.md) | 中文

每张表列出主要改动落在某一阶段的论文，以及该阶段在 Table 1 中的取值。范式、系统与基准类论文不对应单一阶段，见 [README](../../../README.zh.md#范式系统与基准)。

并排比较（英文）：[Tokenizer](../../../comparisons/tokenizer.md) · [Training](../../../comparisons/training.md) · [Inference](../../../comparisons/inference.md)

## Representation

| 论文 | 会议 | 问题 | Representation |
| :-- | :-- | :-- | :-- |
| [Molar](../papers/molar.md) | arXiv’24 | I. 信息量 | `Text+Img+CF` |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I. 信息量 | `Text+Img+Geo†` |
| [Q-BERT4Rec](../papers/q-bert4rec.md) | arXiv’25 | I. 信息量 | `Text+Img+CF` |
| [UNGER](../papers/unger.md) | TOIS’25 | I. 信息量 | `Text+CF` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I. 信息量 | `Text+Geo+CF` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I. 信息量 | `Text+Attr+Geo` |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I. 信息量 | `Text+Geo` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I. 信息量 | `Text+Geo+CF` |
| [ReSID](../papers/resid.md) | arXiv’26 | I. 信息量 | `Attr+CF` |
| [SCRec](../papers/screc.md) | RecSys’26 | I. 信息量 | `Text+CF` |
| [SPAR](../papers/spar.md) | arXiv’26 | I. 信息量 | `Text+Geo` |
| [TriAlignGR](../papers/trialigngr.md) | arXiv’26 | I. 信息量 | `Text+Img` |

## Tokenization

| 论文 | 会议 | 问题 | Tokenization |
| :-- | :-- | :-- | :-- |
| [CID](../papers/cid.md) | SIGIR-AP’23 | II. 唯一性与合法性 | `Spectral Clus.` |
| [VQ-Rec](../papers/vq-rec.md) | WWW’23 | VI. 泛化 | `OPQ` |
| [CoST](../papers/cost.md) | RecSys’24 | I. 信息量 | `C-RQ` |
| [IDGenRec](../papers/idgenrec.md) | SIGIR’24 | III. SID 与模型对齐 | `LLM-Vocab` |
| [LETTER](../papers/letter.md) | CIKM’24 | I. 信息量 | `Learn. RQ` |
| [LMIndexer](../papers/lmindexer.md) | ICML’24 | I. 信息量 | `Self-Sup. ID` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V. 效率 | `Tree-Clus.` |
| [SIIT](../papers/siit.md) | arXiv’24 | III. SID 与模型对齐 | `Self-Imp.` |
| [TransRec](../papers/transrec.md) | KDD’24 | II. 唯一性与合法性 | `Multi-Facet ID` |
| [ActionPiece](../papers/actionpiece.md) | ICML’25 | I. 信息量 | `OPQ` |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I. 信息量 | `MoE-VQ` |
| [DAS](../papers/das.md) | CIKM’25 | I. 信息量 | `Dual RQ` |
| [EAGER-LLM](../papers/eager-llm.md) | WWW’25 | I. 信息量 | `Dual H-KM` |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I. 信息量 | `Dual RQ-VAE` |
| [GenSAR](../papers/gensar.md) | RecSys’25 | I. 信息量 | `Shared/Spec. RQ` |
| [GMC](../papers/gmc.md) | arXiv’25 | VI. 泛化 | `Unified RQ` |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I. 信息量 | `RQ-VAE` |
| [GRAM](../papers/gram.md) | ACL’25 | I. 信息量 | `H-KM` |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II. 唯一性与合法性 | `Hier. RQ` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I. 信息量 | `KG-RQ` |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I. 信息量 | `MM-RQ` |
| [MQL4GRec](../papers/mql4grec.md) | ICLR’25 | I. 信息量 | `Dual RQ` |
| [PSI](../papers/psi.md) | arXiv’25 | II. 唯一性与合法性 | `Post-hoc RQ` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I. 信息量 | `Prog. RQ` |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I. 信息量 | `RQ-VAE` |
| [SemConv](../papers/semconv.md) | AAAI’25 | III. SID 与模型对齐 | `Align. RQ` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I. 信息量 | `Masked VQ` |
| [UTGRec](../papers/utgrec.md) | arXiv’25 | VI. 泛化 | `Tree` |
| [AdaSID](../papers/adasid.md) | arXiv’26 | II. 唯一性与合法性 | `RQ` |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III. SID 与模型对齐 | `Dual RQ` |
| [API](../papers/api.md) | arXiv’26 | II. 唯一性与合法性 | `PID (P-SAE)` |
| [CapsID](../papers/capsid.md) | arXiv’26 | I. 信息量 | `Soft-RQ` |
| [CARD](../papers/card.md) | arXiv’26 | II. 唯一性与合法性 | `NU-RQ` |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I. 信息量 | `RQ-VAE / Par. VQ` |
| [CogRec](../papers/cogrec.md) | arXiv’26 | III. SID 与模型对齐 | `R-KM+Graph` |
| [DACT](../papers/dact.md) | SIGIR’26 | VI. 泛化 | `RQ-VAE` |
| [DIGER](../papers/diger.md) | SIGIR’26 | II. 唯一性与合法性 | `Learn. RQ` |
| [DOS](../papers/dos.md) | WWW’26 Short | III. SID 与模型对齐 | `Orth. RQ` |
| [DREAM](../papers/dream.md) | arXiv’26 | VI. 泛化 | `CART` |
| [Dynamic-Single-Codebook](../papers/dynamic-single-codebook.md) | arXiv’26 | V. 效率 | `Dyn. KM+Disamb.` |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI. 泛化 | `RQ+LoRA` |
| [GR4AD-X](../papers/gr4ad-x.md) | arXiv’26 | III. SID 与模型对齐 | `Multi-Path R-KM+Hash` |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I. 信息量 | `RecDMoN / RQ-GAE` |
| [GRLM](../papers/grlm.md) | arXiv’26 | III. SID 与模型对齐 | `Term-ID` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II. 唯一性与合法性 | `Contr. RQ` |
| [HoloRec](../papers/holorec.md) | arXiv’26 | III. SID 与模型对齐 | `Nested RQ` |
| [JevRec](../papers/jevrec.md) | arXiv’26 | V. 效率 | `Freq. R-KM` |
| [MACRec](../papers/macrec.md) | AAAI’26 | I. 信息量 | `Cross RQ` |
| [MBGR](../papers/mbgr.md) | arXiv’26 | VI. 泛化 | `RQ` |
| [MMGRec](../papers/mmgrec.md) | TOMM’26 | I. 信息量 | `Graph RQ-VAE` |
| [MMQ](../papers/mmq.md) | WSDM’26 | I. 信息量 | `MoE-VQ` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I. 信息量 | `RQ-VAE+DINO` |
| [OneLive](../papers/onelive.md) | KDD’26 ADS | VI. 泛化 | `R-KM` |
| [PCR-CA](../papers/pcr-ca.md) | KDD’26 | I. 信息量 | `PC-AE` |
| [Pctx](../papers/pctx.md) | CIKM’26 | I. 信息量 | `RQ` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I. 信息量 | `R-KM+Geo-CB` |
| [QuaSID](../papers/quasid.md) | KDD’26 ADS | II. 唯一性与合法性 | `QA-RQ` |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II. 唯一性与合法性 | `Ref.-RQ` |
| [RoFiGR](../papers/rofigr.md) | arXiv’26 | I. 信息量 | `CF-Aligned MM RQ` |
| [ROS](../papers/ros.md) | ACL’26 | I. 信息量 | `Geo-Prefix+RQ-VAE` |
| [SnapLGR](../papers/snaplgr.md) | arXiv’26 | II. 唯一性与合法性 | `RQ-VAE+PPR` |
| [SPRIG](../papers/sprig.md) | CIKM’26 Short | I. 信息量 | `R-KM` |
| [SST](../papers/sst.md) | CIKM’26 | III. SID 与模型对齐 | `RQ+IST` |
| [Tlow](../papers/tlow.md) | CIKM’26 Applied | I. 信息量 | `Flow+PQ` |
| [TopoGR](../papers/topogr.md) | arXiv’26 | III. SID 与模型对齐 | `BDQ` |
| [TRACER](../papers/tracer.md) | NeurIPS’26 | IV. 实用目标 | `Soft Reassign. RQ` |
| [UniRec](../papers/unirec.md) | arXiv’26 | I. 信息量 | `RQ` |
| [UniSID](../papers/unisid.md) | arXiv’26 | I. 信息量 | `Direct SID Heads` |
| [UniTok](../papers/unitok.md) | AAAI’26 | VI. 泛化 | `TokenMoE` |
| [VarLenRec (TIGER)](../papers/varlenrec-tiger.md) | arXiv’26 | I. 信息量 | `HARQ` |

## Backbone

| 论文 | 会议 | 问题 | Backbone |
| :-- | :-- | :-- | :-- |
| [ColaRec](../papers/colarec.md) | CIKM’24 | I. 信息量 | `Enc-Dec` |
| [EAGER](../papers/eager.md) | KDD’24 | I. 信息量 | `Dual Enc-Dec` |
| [COBRA](../papers/cobra.md) | NeurIPS’25 | I. 信息量 | `Dec-Only` |
| [DiscRec](../papers/discrec.md) | arXiv’25 | I. 信息量 | `Enc-Dec` |
| [LLaDA-Rec](../papers/llada-rec.md) | arXiv’25 | III. SID 与模型对齐 | `Non-AR` |
| [OneRec-V2](../papers/onerec-v2.md) | arXiv’25 | V. 效率 | `Lazy Dec-Only` |
| [RPG](../papers/rpg.md) | KDD’25 | V. 效率 | `Non-AR` |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I. 信息量 | `Dec-Only` |
| [ACERec](../papers/acerec.md) | arXiv’26 | V. 效率 | `Non-AR` |
| [Deco](../papers/deco.md) | arXiv’26 | V. 效率 | `Dec-Only` |
| [DECOR](../papers/decor.md) | SIGIR’26 | III. SID 与模型对齐 | `Enc-Dec` |
| [DiGR](../papers/digr.md) | arXiv’26 | IV. 实用目标 | `Dec-Only` |
| [DualGR](../papers/dualgr.md) | WWW’26 Short | VI. 泛化 | `Dec-Only` |
| [FedCGR](../papers/fedcgr.md) | CIKM’26 | VI. 泛化 | `Enc-Dec` |
| [FLASH](../papers/flash.md) | NeurIPS’26 | III. SID 与模型对齐 | `Non-AR` |
| [Gryphon](../papers/gryphon.md) | CIKM’26 Short | IV. 实用目标 | `Enc-Dec` |
| [IBA](../papers/iba.md) | arXiv’26 | V. 效率 | `Enc-Dec` |
| [Latte](../papers/latte.md) | arXiv’26 | III. SID 与模型对齐 | `Dec-Only` |
| [LESSRec](../papers/lessrec.md) | arXiv’26 | III. SID 与模型对齐 | `Enc-Dec` |
| [LION](../papers/lion.md) | CIKM’26 | VI. 泛化 | `Enc-Dec` |
| [LoopGR](../papers/loopgr.md) | arXiv’26 | V. 效率 | `Enc-Dec` |
| [MDGR](../papers/mdgr.md) | arXiv’26 | III. SID 与模型对齐 | `Non-AR` |
| [Merge-and-Branch](../papers/merge-and-branch.md) | arXiv’26 | V. 效率 | `Dec-Only` |
| [PinGER](../papers/pinger.md) | arXiv’26 | V. 效率 | `Dec-Only` |
| [PrefixMem](../papers/prefixmem.md) | arXiv’26 | III. SID 与模型对齐 | `Dec-Only` |
| [RecoChain](../papers/recochain.md) | arXiv’26 | IV. 实用目标 | `Dec-Only` |
| [S2GR](../papers/s2gr.md) | KDD’26 | III. SID 与模型对齐 | `Enc-Dec` |
| [SID-MLP](../papers/sid-mlp.md) | arXiv’26 | V. 效率 | `Enc-MLP` |
| [SPAR-Youku](../papers/spar-youku.md) | arXiv’26 | I. 信息量 | `Dec-Only` |
| [SPRINT](../papers/sprint.md) | arXiv’26 | V. 效率 | `Non-AR` |
| [STAMP](../papers/stamp.md) | arXiv’26 | V. 效率 | `Enc-Dec / Dec-Only` |
| [TrieRec](../papers/trierec.md) | NeurIPS’26 | III. SID 与模型对齐 | `Enc-Dec` |
| [UniSGR-V2](../papers/unisgr-v2.md) | arXiv’26 | I. 信息量 | `Enc-Dec` |

## Training

| 论文 | 会议 | 问题 | Training |
| :-- | :-- | :-- | :-- |
| [LC-Rec](../papers/lc-rec.md) | ICDE’24 | III. SID 与模型对齐 | `Fixed / Multi-task NTP` |
| [MBGen](../papers/mbgen.md) | CIKM’24 | I. 信息量 | `Fixed / NTP` |
| [ETEGRec](../papers/etegrec.md) | SIGIR’25 | III. SID 与模型对齐 | `Altern. / NTP + Ctr.` |
| [GREAM](../papers/gream.md) | arXiv’25 | III. SID 与模型对齐 | `Fixed / NTP → RL` |
| [OneRec-Think](../papers/onerec-think.md) | arXiv’25 | III. SID 与模型对齐 | `Fixed / NTP → RL` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI. 泛化 | `Fixed / NTP` |
| [APAO](../papers/apao.md) | KDD’26 | IV. 实用目标 | `Fixed / NTP + Rank` |
| [AWARE](../papers/aware.md) | arXiv’26 | VI. 泛化 | `Fixed / NTP` |
| [CausalDPO](../papers/causaldpo.md) | ICML’26 | VI. 泛化 | `Fixed / NTP → DPO` |
| [CMRec](../papers/cmrec.md) | CIKM’26 Short | VI. 泛化 | `– / NTP` |
| [DASO](../papers/daso.md) | arXiv’26 | IV. 实用目标 | `Fixed / NTP → RL` |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV. 实用目标 | `Fixed / Masked → RL (→ Masked KD for Fast)` |
| [Evo-Rec](../papers/evo-rec.md) | arXiv’26 | III. SID 与模型对齐 | `Fixed / NTP → RL` |
| [GEM-Rec](../papers/gem-rec.md) | arXiv’26 | IV. 实用目标 | `Fixed / NTP` |
| [GenRec-JD](../papers/genrec-jd.md) | SIGIR’26 | IV. 实用目标 | `Fixed / NTP → RL` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV. 实用目标 | `Fixed / NTP + Aux.` |
| [Ghost](../papers/ghost.md) | NeurIPS’26 | IV. 实用目标 | `Fixed / NTP + Aux.` |
| [GTI](../papers/gti.md) | arXiv’26 | III. SID 与模型对齐 | `Fixed / Multi-task NTP` |
| [HASTE](../papers/haste.md) | arXiv’26 | IV. 实用目标 | `Fixed / NTP + Aux.` |
| [HCGRec](../papers/hcgrec.md) | CIKM’26 | IV. 实用目标 | `Fixed / NTP → RL` |
| [IDM/CMM](../papers/idm-cmm.md) | arXiv’26 | IV. 实用目标 | `Fixed / MTP + Aux.` |
| [Intent-Driven-News](../papers/intent-driven-news.md) | ACL’26 Industry | III. SID 与模型对齐 | `Fixed / Multi-task NTP` |
| [KL-MOPD](../papers/kl-mopd.md) | arXiv’26 | IV. 实用目标 | `Fixed† / (NTP† / (NTP + Aux.)†) → KL-weighted OPD` |
| [MuSID-KD](../papers/musid-kd.md) | arXiv’26 | IV. 实用目标 | `Fixed / NTP + Aux.` |
| [NAU](../papers/nau.md) | arXiv’26 | IV. 实用目标 | `Fixed / NTP + Aux.` |
| [OneChord](../papers/onechord.md) | arXiv’26 | IV. 实用目标 | `Fixed / Next-item CE + Cons. KD + Rank KD` |
| [OneLatent](../papers/onelatent.md) | arXiv’26 | V. 效率 | `Fixed / Multi-task NTP` |
| [RAGR](../papers/ragr.md) | arXiv’26 | I. 信息量 | `Fixed / NTP → DPO` |
| [REGER](../papers/reger.md) | arXiv’26 | I. 信息量 | `Fixed / NTP → (NTP + Aux.)` |
| [Retrieval-Grounded-Credit](../papers/retrieval-grounded-credit.md) | arXiv’26 | IV. 实用目标 | `Fixed / NTP → RL` |
| [SAGE-SID](../papers/sage-sid.md) | arXiv’26 | IV. 实用目标 | `Fixed† / NTP → RL` |
| [SAHL](../papers/sahl.md) | arXiv’26 | IV. 实用目标 | `Fixed / (MTP + Masked Rec.) → MTP` |
| [SAPO](../papers/sapo.md) | arXiv’26 | IV. 实用目标 | `Fixed / NTP → RL` |
| [SIDReasoner](../papers/sidreasoner.md) | KDD’26 | III. SID 与模型对齐 | `Fixed / NTP → RL` |
| [SLIDE](../papers/slide.md) | arXiv’26 | IV. 实用目标 | `Fixed / NTP` |
| [SynGR](../papers/syngr.md) | ICML’26 | I. 信息量 | `Fixed / NTP + Ctr.` |
| [Think2Go](../papers/think2go.md) | KDD’26 | III. SID 与模型对齐 | `Fixed / NTP → RL` |
| [Token-Weighted](../papers/token-weighted.md) | CIKM’26 | IV. 实用目标 | `Fixed / NTP` |
| [UGR](../papers/ugr.md) | KDD’26 | IV. 实用目标 | `Fixed / NTP → (RL + Rank)` |
| [V-STAR](../papers/v-star.md) | KDD’26 | IV. 实用目标 | `Fixed / NTP → RL` |

## Inference

| 论文 | 会议 | 问题 | Inference |
| :-- | :-- | :-- | :-- |
| [LIGER](../papers/liger.md) | arXiv’24 | VI. 泛化 | `Hybrid` |
| [AtSpeed](../papers/atspeed.md) | ICLR’25 | V. 效率 | `Spec. Dec.` |
| [CAPE](../papers/cape.md) | arXiv’26 | I. 信息量 | `Hybrid` |
| [CITE](../papers/cite.md) | Electronics’26 | I. 信息量 | `Scoring` |
| [GRC](../papers/grc.md) | CIKM’26 | III. SID 与模型对齐 | `GRC+Beam` |
| [ISD](../papers/isd.md) | arXiv’26 | IV. 实用目标 | `ISD Beam` |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V. 效率 | `Self-Draft+Hash` |
| [OneRec-V2-Quantized](../papers/onerec-v2-quantized.md) | arXiv’26 | V. 效率 | `FP8+RecoGEM` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V. 效率 | `Spec. Dec.` |
| [PFA](../papers/pfa.md) | arXiv’26 | V. 效率 | `Beam` |
| [PROMISE](../papers/promise.md) | arXiv’26 | III. SID 与模型对齐 | `PRM-Beam` |
| [SpecGR](../papers/specgr.md) | AAAI’26 | VI. 泛化 | `Hybrid` |
| [STATIC](../papers/static.md) | KDD’26 ADS | V. 效率 | `Vec. C-Beam` |
| [TCBSA](../papers/tcbsa.md) | arXiv’26 | IV. 实用目标 | `CF-Guided C-Beam` |
