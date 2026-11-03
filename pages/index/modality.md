# Papers by Tokenizer Input Modality

English | [中文](../zh/index/modality.md)

Papers grouped by the content modality and collaborative filtering (`CF`) signal reported in the survey's Table 1 `representation` column (or paper-level `modality` override where recorded). Collaborative signal here refers only to `CF` in the tokenizer input, not to collaborative supervision in the generator backbone or training objective. Dual-branch `A / B` configurations appear in each branch's section, with distinct papers counted per section.

| Content Modality | No CF tagged                       | With CF                                     |
| :--------------- | :--------------------------------- | :------------------------------------------ |
| **Single-modal** | [Single-modal (82)](#single-modal) | [Single-modal + CF (32)](#single-modal--cf) |
| **Multimodal**   | [Multimodal (15)](#multimodal)     | [Multimodal + CF (21)](#multimodal--cf)     |
| **Other**        | [Other (1)](#other)                | [Other + CF (10)](#other--cf)               |

**Unspecified representation**: [25 papers](#unspecified-representation) (`–`, `Multi-Dom`, `Cross-Dom`, or an unreported branch).

**Not applicable**: [1 paper](#not-applicable) (`n/a`).

**Auxiliary signals**: [`Geo` (15)](#geo) · [`Time` (1)](#time) · [`SID` (5)](#sid).

## Single-modal

> One content modality (`Text` or `Audio`), without `CF` in the tokenizer input.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
| :-- | :-- | :-- | :-- | :-- |
| [TIGER](../papers/tiger.md) | NeurIPS’23 | Paradigms, Systems and Benchmarks | `Text` | – |
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
| [GRID](../papers/grid.md) | CIKM’25 | Paradigms, Systems and Benchmarks | `Text` | – |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II × Tokenization | `Text` | – |
| [LLaDA-Rec](../papers/llada-rec.md) | arXiv’25 | III × Backbone | `Text` | – |
| [MiniOneRec](../papers/minionerec.md) | arXiv’25 | Paradigms, Systems and Benchmarks | `Text` | – |
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
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Text+SID` | `SID` |
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
| [NEO](../papers/neo.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Text / Audio` | – |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V × Inference | `Text` | – |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `Text+SID` | `SID` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `Text+Geo` | `Geo` |
| [PROMISE](../papers/promise.md) | arXiv’26 | III × Inference | `Text` | – |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II × Tokenization | `Text` | – |
| [RAGR](../papers/ragr.md) | arXiv’26 | I × Training | `Text` | – |
| [REGER](../papers/reger.md) | arXiv’26 | I × Training | `Text` | – |
| [ReRankID](../papers/rerankid.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Text` | – |
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

## Single-modal + CF

> One content modality combined with collaborative filtering (`CF`) in the tokenizer input.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
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

## Multimodal

> Two or more content modalities (or `MM`), without `CF` in the tokenizer input.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
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

## Multimodal + CF

> Two or more content modalities (or `MM`) combined with `CF` in the tokenizer input.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
| :-- | :-- | :-- | :-- | :-- |
| [Molar](../papers/molar.md) | arXiv’24 | I × Representation | `Text+Img+CF` | – |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I × Tokenization | `Text+Img+CF` | – |
| [FORGE](../papers/forge.md) | KDD’26 | Paradigms, Systems and Benchmarks | `Text+Img+CF` | – |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | `Text+Img+CF` | – |
| [OneRec](../papers/onerec.md) | arXiv’25 | Paradigms, Systems and Benchmarks | `MM+CF` | – |
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
| [OneMall](../papers/onemall.md) | CIKM’26 | Paradigms, Systems and Benchmarks | `Text+Img+CF` | – |
| [OneRec-V2-Quantized](../papers/onerec-v2-quantized.md) | arXiv’26 | V × Inference | `Text+Img+CF†` | – |
| [PinGER](../papers/pinger.md) | arXiv’26 | V × Backbone | `Text+Img+CF` | – |
| [PLUM](../papers/plum.md) | WWW’26 | Paradigms, Systems and Benchmarks | `Text+Img+CF` | – |
| [RoFiGR](../papers/rofigr.md) | arXiv’26 | I × Tokenization | `Text+Img+CF` | – |
| [SnapLGR](../papers/snaplgr.md) | arXiv’26 | II × Tokenization | `Text+Img+CF` | – |

## Other

> Non-content tokenizer representations (such as spatial features alone), without `CF`.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
| :-- | :-- | :-- | :-- | :-- |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `Geo` | `Geo` |

## Other + CF

> Pure collaborative (`CF`) or structured-attribute + `CF` representations without text, image, or audio.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
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

## Unspecified Representation

> Table 1 `representation` is unreported (`–`) or records domain scope (`Multi-Dom`, `Cross-Dom`) without a modality override.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
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
| [Netflix-SID-Comparison](../papers/netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | Paradigms, Systems and Benchmarks | `–` | – |
| [OneChord](../papers/onechord.md) | arXiv’26 | IV × Training | `–` | – |
| [PFA](../papers/pfa.md) | arXiv’26 | V × Inference | `–` | – |
| [SLIDE](../papers/slide.md) | arXiv’26 | IV × Training | `–` | – |
| [SPAR-Youku](../papers/spar-youku.md) | arXiv’26 | I × Backbone | `–` | – |
| [STATIC](../papers/static.md) | KDD’26 ADS | V × Inference | `–` | – |
| [UniSGR-V2](../papers/unisgr-v2.md) | arXiv’26 | I × Backbone | `–` | – |
| [UniTok](../papers/unitok.md) | AAAI’26 | VI × Tokenization | `Multi-Dom` | – |

## Not Applicable

> Diagnostic or non-method entries where tokenizer input representation does not apply (`n/a`).

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
| :-- | :-- | :-- | :-- | :-- |
| [SIDScope](../papers/sidscope.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `n/a` | – |

## Auxiliary Signals

### Geo

> Geographic or spatial features in the representation.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
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

> Explicit interaction timestamps in the representation.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
| :-- | :-- | :-- | :-- | :-- |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I × Tokenization | `Text+Time` | `Time` |

### SID

> Discrete Semantic IDs concatenated with dense representations.

| Paper | Venue | Problem × Stage | Representation | Auxiliary |
| :-- | :-- | :-- | :-- | :-- |
| [LIGER](../papers/liger.md) | arXiv’24 | VI × Inference | `Text+SID` | `SID` |
| [COBRA](../papers/cobra.md) | NeurIPS’25 | I × Backbone | `Text+SID` | `SID` |
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Text+SID` | `SID` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `Text+SID` | `SID` |
| [SpecGR](../papers/specgr.md) | AAAI’26 | VI × Inference | `Text+SID` | `SID` |
