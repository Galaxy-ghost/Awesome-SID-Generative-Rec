# Papers by Modality

[← README](../../README.md#where-to-start) · English | [中文](../zh/index/modality.md)

Papers grouped by the signals fed into the SID tokenizer (rules defined in `data/vocab.yaml`). Content groups are evaluated per branch, collaborative and context groups across all branches combined; a paper appears in every matching group with its full branch values and application domains.

| Aspect | Groups |
| :--- | :--- |
| **Content** | [Text (115)](#text) · [Single non-text (9)](#single-non-text) · [Multimodal (36)](#multimodal) · [No content (11)](#no-content) |
| **Collaborative** | [CF only (7)](#cf-only) · [With CF (52)](#with-cf) |
| **Context** | [Attr (8)](#attr) · [Geo (14)](#geo) · [Time (2)](#time) |
| **Other** | [Other (25)](#other) |

## Text

> 115 papers. At least one tokenizer branch uses `Text` as its only content modality (`Img`, `Audio`, `Video`, `MM` absent in that branch).

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [TIGER](../papers/tiger.md) | NeurIPS’23 | Paradigms, Systems and Benchmarks | `Text` | `E-commerce` |
| [VQ-Rec](../papers/vq-rec.md) | WWW’23 | VI × Tokenization | `Text` | `E-commerce` |
| [CoST](../papers/cost.md) | RecSys’24 | I × Tokenization | `Text` | `News` · `E-commerce` |
| [EAGER](../papers/eager.md) | KDD’24 | I × Backbone | semantic: `Text` · behavior: `CF` | `E-commerce` · `POI / Local` |
| [IDGenRec](../papers/idgenrec.md) | SIGIR’24 | III × Tokenization | `Text` | `E-commerce` · `POI / Local` |
| [LC-Rec](../papers/lc-rec.md) | ICDE’24 | III × Training | `Text` | `E-commerce` |
| [LETTER](../papers/letter.md) | CIKM’24 | I × Tokenization | `Text` + `CF` | `E-commerce` · `POI / Local` |
| [LIGER](../papers/liger.md) | arXiv’24 | VI × Inference | `Text` | `E-commerce` · `Games` |
| [LMIndexer](../papers/lmindexer.md) | ICML’24 | I × Tokenization | `Text` | `E-commerce` · `Search` |
| [SIIT](../papers/siit.md) | arXiv’24 | III × Tokenization | `Text` | `E-commerce` · `POI / Local` |
| [TransRec](../papers/transrec.md) | KDD’24 | II × Tokenization | id: – · title: `Text` · attribute: `Text` | `E-commerce` · `POI / Local` |
| [ActionPiece](../papers/actionpiece.md) | ICML’25 | I × Tokenization | `Text` | `E-commerce` |
| [AtSpeed](../papers/atspeed.md) | ICLR’25 | V × Inference | `Text` | `E-commerce` · `Movie` · `Book` |
| [COBRA](../papers/cobra.md) | NeurIPS’25 | I × Backbone | `Text` | `E-commerce` · `Ads` |
| [DAS](../papers/das.md) | CIKM’25 | I × Tokenization | `Text` + `CF` | `Ads` |
| [DiscRec](../papers/discrec.md) | arXiv’25 | I × Backbone | A: `Text` · B: `Text` + `CF` | `E-commerce` |
| [EAGER-LLM](../papers/eager-llm.md) | WWW’25 | I × Tokenization | semantic: `Text` · behavior: `CF` | `E-commerce` |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I × Tokenization | semantic: `Text` + `CF` · collaborative: `CF` | `E-commerce` · `Short video / Live` · `Other` (In-house data from an unnamed commercial platform) |
| [GenSAR](../papers/gensar.md) | RecSys’25 | I × Tokenization | semantic: `Text` + `CF` · collaborative: `Text` + `CF` | `E-commerce` · `Search` |
| [GMC](../papers/gmc.md) | arXiv’25 | VI × Tokenization | `Text` | `E-commerce` |
| [GRAM](../papers/gram.md) | ACL’25 | I × Tokenization | `Text` | `E-commerce` · `POI / Local` |
| [GREAM](../papers/gream.md) | arXiv’25 | III × Training | `Text` | `E-commerce` |
| [GRID](../papers/grid.md) | CIKM’25 | Paradigms, Systems and Benchmarks | `Text` | `E-commerce` |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II × Tokenization | `Text` + `Attr` | `E-commerce` · `Short video / Live` |
| [LLaDA-Rec](../papers/llada-rec.md) | arXiv’25 | III × Backbone | `Text` | `E-commerce` |
| [MiniOneRec](../papers/minionerec.md) | arXiv’25 | Paradigms, Systems and Benchmarks | `Text` | `E-commerce` |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | collaborative: `CF` · text: `Text` · visual: `Img` | `E-commerce` |
| [MQL4GRec](../papers/mql4grec.md) | ICLR’25 | I × Tokenization | text: `Text` · image: `Img` | `E-commerce` |
| [PSI](../papers/psi.md) | arXiv’25 | II × Tokenization | `Text` | `E-commerce` · `Search` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | text: `Text` · image: `Img` · audio: `Audio` · joint_Amazon: `Text` + `Img` · joint_Music: `Text` + `Audio` | `E-commerce` · `Music` |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I × Tokenization | `Text` + `Geo` | `POI / Local` |
| [RecBase](../papers/recbase.md) | EMNLP’25 | VI × Training | `Text` | `News` · `Movie` · `Short video / Live` · `Book` · `POI / Local` · `Games` · `E-commerce` · `Travel / Hotel` |
| [RPG](../papers/rpg.md) | KDD’25 | V × Backbone | `Text` | `E-commerce` |
| [SemConv](../papers/semconv.md) | AAAI’25 | III × Tokenization | `Text` + `CF` | `E-commerce` |
| [UNGER](../papers/unger.md) | TOIS’25 | I × Representation | `Text` + `CF` | `E-commerce` |
| [ACERec](../papers/acerec.md) | arXiv’26 | V × Backbone | `Text` | `E-commerce` |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III × Tokenization | `Text` + `CF` | `E-commerce` · `POI / Local` · `Ads` |
| [APAO](../papers/apao.md) | KDD’26 | IV × Training | `Text` | `E-commerce` · `POI / Local` |
| [API](../papers/api.md) | arXiv’26 | II × Tokenization | `Text` | `E-commerce` |
| [AWARE](../papers/aware.md) | arXiv’26 | VI × Training | `Text` + `Geo` | `POI / Local` |
| [CAPE](../papers/cape.md) | arXiv’26 | I × Inference | `Text` | `E-commerce` · `Music` |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I × Tokenization | `Text` + `Time` | `E-commerce` |
| [CITE](../papers/cite.md) | Electronics’26 | I × Inference | `Text` | `E-commerce` · `POI / Local` |
| [CogRec](../papers/cogrec.md) | arXiv’26 | III × Tokenization | `Text` | `E-commerce` |
| [DACT](../papers/dact.md) | SIGIR’26 | VI × Tokenization | `Text` + `CF` | `E-commerce` |
| [DASO](../papers/daso.md) | arXiv’26 | IV × Training | `Text` + `Other` (Internal 4-level, 2048-code SIDs; input unstated) | `E-commerce` · `Other` (Proprietary user-to-item data, business unstated) |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | A: `Text` · B: `Audio` | `E-commerce` · `Movie` · `Music` |
| [DECOR](../papers/decor.md) | SIGIR’26 | III × Backbone | `Text` | `E-commerce` |
| [DIGER](../papers/diger.md) | SIGIR’26 | II × Tokenization | `Text` | `E-commerce` · `POI / Local` |
| [DOS](../papers/dos.md) | WWW’26 Short | III × Tokenization | `Text` + `CF` | `POI / Local` |
| [DREAM](../papers/dream.md) | arXiv’26 | VI × Tokenization | `Text` + `CF` | `E-commerce` |
| [Evo-Rec](../papers/evo-rec.md) | arXiv’26 | III × Training | `Text` | `E-commerce` |
| [FedCGR](../papers/fedcgr.md) | CIKM’26 | VI × Backbone | `Text` | `E-commerce` |
| [FLASH](../papers/flash.md) | NeurIPS’26 | III × Backbone | `Text` | `E-commerce` |
| [GEM-Rec](../papers/gem-rec.md) | arXiv’26 | IV × Training | `Text` | `Games` · `E-commerce` · `Ads` |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI × Tokenization | `Text` + `Other` (MTM masked-code context, source unstated) | `E-commerce` · `Book` · `Movie` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `Text` + `Geo` + `CF` | `POI / Local` · `Search` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | A: `Text` · B: `Text` + `CF` | `POI / Local` · `E-commerce` · `Ads` · `Search` |
| [Ghost](../papers/ghost.md) | NeurIPS’26 | IV × Training | `Text` | `E-commerce` |
| [GR-Generalize](../papers/gr-generalize.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Text` | `E-commerce` · `Games` · `POI / Local` |
| [GRC](../papers/grc.md) | CIKM’26 | III × Inference | `Text` | `E-commerce` · `Ads` |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I × Tokenization | `Text` + `CF` | `E-commerce` · `News` · `POI / Local` |
| [GRLM](../papers/grlm.md) | arXiv’26 | III × Tokenization | `Text` | `E-commerce` |
| [GTI](../papers/gti.md) | arXiv’26 | III × Training | A: `Text` + `CF` · B: `Text` | `Recruitment` · `E-commerce` |
| [HASTE](../papers/haste.md) | arXiv’26 | IV × Training | A: `Text` · B: `MM` | `E-commerce` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `Text` + `Attr` + `Geo` | `POI / Local` |
| [IBA](../papers/iba.md) | arXiv’26 | V × Backbone | `Text` | `E-commerce` · `Short video / Live` |
| [IDM/CMM](../papers/idm-cmm.md) | arXiv’26 | IV × Training | `Text` | `E-commerce` |
| [Intent-Driven-News](../papers/intent-driven-news.md) | ACL’26 Industry | III × Training | `Text` | `News` |
| [ISD](../papers/isd.md) | arXiv’26 | IV × Inference | `Text` | `E-commerce` |
| [JevRec](../papers/jevrec.md) | arXiv’26 | V × Tokenization | `Text` | `E-commerce` |
| [LESSRec](../papers/lessrec.md) | arXiv’26 | III × Backbone | A: `Text` · B: `Text` + `CF` | `E-commerce` |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I × Representation | `Text` + `Geo` | `POI / Local` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text` + `Geo` + `Attr` + `CF` | `POI / Local` |
| [LION](../papers/lion.md) | CIKM’26 | VI × Backbone | `Text` | `E-commerce` |
| [LoopGR](../papers/loopgr.md) | arXiv’26 | V × Backbone | `Text` | `E-commerce` · `Other` (Tencent production recommender, business unstated) |
| [MACRec](../papers/macrec.md) | AAAI’26 | I × Tokenization | text: `Text` · image: `Img` | `E-commerce` |
| [MDGR](../papers/mdgr.md) | arXiv’26 | III × Backbone | `Text` | `E-commerce` |
| [Merge-and-Branch](../papers/merge-and-branch.md) | arXiv’26 | V × Backbone | `Text` | `E-commerce` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | image: `Img` · text: `Text` · collaborative: `CF` | `E-commerce` · `Short video / Live` |
| [NEO](../papers/neo.md) | arXiv’26 | Paradigms, Systems and Benchmarks | A: `Text` · B: `Audio` | `Music` · `Podcast` · `Book` · `Search` |
| [NEZHA](../papers/nezha.md) | WWW’26 Industry | V × Inference | `Text` | `E-commerce` · `POI / Local` · `Ads` · `Search` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `Text` + `CF` | `E-commerce` · `POI / Local` |
| [PCR-CA](../papers/pcr-ca.md) | KDD’26 | I × Tokenization | `Text` + `CF` | `Apps` |
| [Pctx](../papers/pctx.md) | CIKM’26 | I × Tokenization | `Text` + `CF` | `E-commerce` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `Text` + `Geo` | `POI / Local` · `Search` |
| [PROMISE](../papers/promise.md) | arXiv’26 | III × Inference | `Text` | `E-commerce` · `Short video / Live` |
| [R3-VAE](../papers/r3-vae.md) | arXiv’26 | II × Tokenization | `Text` | `E-commerce` · `Music` · `Movie` · `News` |
| [RAGR](../papers/ragr.md) | arXiv’26 | I × Training | item: `Text` · review: `Text` | `E-commerce` |
| [REGER](../papers/reger.md) | arXiv’26 | I × Training | `Text` | `E-commerce` |
| [ReRankID](../papers/rerankid.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Text` | `Short video / Live` |
| [Retrieval-Grounded-Credit](../papers/retrieval-grounded-credit.md) | arXiv’26 | IV × Training | `Text` | `E-commerce` |
| [ROS](../papers/ros.md) | ACL’26 | I × Tokenization | `Text` + `Geo` | `POI / Local` |
| [S2GR](../papers/s2gr.md) | KDD’26 | III × Backbone | `Text` + `CF` | `E-commerce` · `Short video / Live` |
| [SAHL](../papers/sahl.md) | arXiv’26 | IV × Training | `Text` | `E-commerce` |
| [SAPO](../papers/sapo.md) | arXiv’26 | IV × Training | `Text` | `E-commerce` |
| [SCRec](../papers/screc.md) | RecSys’26 | I × Representation | `Text` + `CF` | `E-commerce` |
| [SID-MLP](../papers/sid-mlp.md) | arXiv’26 | V × Backbone | `Text` | `E-commerce` |
| [SIDReasoner](../papers/sidreasoner.md) | KDD’26 | III × Training | `Text` | `E-commerce` |
| [SPAR](../papers/spar.md) | arXiv’26 | I × Representation | `Text` + `Geo` | `POI / Local` |
| [SpecGR](../papers/specgr.md) | AAAI’26 | VI × Inference | `Text` | `E-commerce` |
| [SPRIG](../papers/sprig.md) | CIKM’26 Short | I × Tokenization | A: `Text` · B: `Audio` | `Movie` · `Music` |
| [SPRINT](../papers/sprint.md) | arXiv’26 | V × Backbone | `Text` | `E-commerce` · `POI / Local` |
| [SST](../papers/sst.md) | CIKM’26 | III × Tokenization | `Text` | `E-commerce` · `POI / Local` |
| [STAMP](../papers/stamp.md) | arXiv’26 | V × Backbone | A: `Text` · B: `Text` + `Img` + `CF` | `E-commerce` |
| [SynGR](../papers/syngr.md) | ICML’26 | I × Training | text: `Text` · image: `Img` | `E-commerce` |
| [TCBSA](../papers/tcbsa.md) | arXiv’26 | IV × Inference | `Text` | `E-commerce` · `POI / Local` |
| [Tlow](../papers/tlow.md) | CIKM’26 Applied | I × Tokenization | A: `Text` · B: `Text` + `Img` | `E-commerce` · `Image / Article` |
| [Token-Weighted](../papers/token-weighted.md) | CIKM’26 | IV × Training | `Text` | `E-commerce` · `POI / Local` · `Movie` |
| [TopoGR](../papers/topogr.md) | arXiv’26 | III × Tokenization | `Text` | `E-commerce` |
| [TRACER](../papers/tracer.md) | NeurIPS’26 | IV × Tokenization | `Text` | `E-commerce` |
| [TrieRec](../papers/trierec.md) | NeurIPS’26 | III × Backbone | `Text` | `E-commerce` · `Movie` |
| [UGR](../papers/ugr.md) | KDD’26 | IV × Training | `Text` | `E-commerce` · `POI / Local` |
| [UniTok](../papers/unitok.md) | AAAI’26 | VI × Tokenization | `Text` | `E-commerce` · `POI / Local` |
| [VarLenRec (TIGER)](../papers/varlenrec-tiger.md) | arXiv’26 | I × Tokenization | `Text` | `E-commerce` · `POI / Local` |

## Single non-text

> 9 papers. At least one tokenizer branch uses exactly one content modality and it is neither `Text` nor composite `MM` (`Img`, `Audio`, or `Video`).

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | collaborative: `CF` · text: `Text` · visual: `Img` | `E-commerce` |
| [MQL4GRec](../papers/mql4grec.md) | ICLR’25 | I × Tokenization | text: `Text` · image: `Img` | `E-commerce` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | text: `Text` · image: `Img` · audio: `Audio` · joint_Amazon: `Text` + `Img` · joint_Music: `Text` + `Audio` | `E-commerce` · `Music` |
| [Deco](../papers/deco.md) | arXiv’26 | V × Backbone | A: `Text` · B: `Audio` | `E-commerce` · `Movie` · `Music` |
| [MACRec](../papers/macrec.md) | AAAI’26 | I × Tokenization | text: `Text` · image: `Img` | `E-commerce` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | image: `Img` · text: `Text` · collaborative: `CF` | `E-commerce` · `Short video / Live` |
| [NEO](../papers/neo.md) | arXiv’26 | Paradigms, Systems and Benchmarks | A: `Text` · B: `Audio` | `Music` · `Podcast` · `Book` · `Search` |
| [SPRIG](../papers/sprig.md) | CIKM’26 Short | I × Tokenization | A: `Text` · B: `Audio` | `Movie` · `Music` |
| [SynGR](../papers/syngr.md) | ICML’26 | I × Training | text: `Text` · image: `Img` | `E-commerce` |

## Multimodal

> 36 papers. At least one tokenizer branch combines two or more content modalities, or uses `MM`.

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I × Tokenization | `Text` + `Img` + `CF` | `E-commerce` · `Ads` |
| [FORGE](../papers/forge.md) | KDD’26 | Paradigms, Systems and Benchmarks | `Text` + `Img` + `CF` | `E-commerce` · `Search` |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I × Representation | `MM` + `Geo` | `POI / Local` |
| [OneRec](../papers/onerec.md) | arXiv’25 | Paradigms, Systems and Benchmarks | `MM` + `CF` | `Short video / Live` |
| [OneRec-Think](../papers/onerec-think.md) | arXiv’25 | III × Training | `MM` + `CF` | `E-commerce` · `Short video / Live` |
| [OneRec-V2](../papers/onerec-v2.md) | arXiv’25 | V × Backbone | `Text` + `Img` + `CF` | `Short video / Live` |
| [PSRQ](../papers/psrq.md) | CIKM’25 | I × Tokenization | text: `Text` · image: `Img` · audio: `Audio` · joint_Amazon: `Text` + `Img` · joint_Music: `Text` + `Audio` | `E-commerce` · `Music` |
| [Q-BERT4Rec](../papers/q-bert4rec.md) | arXiv’25 | I × Representation | `Text` + `Img` | `E-commerce` |
| [UTGRec](../papers/utgrec.md) | arXiv’25 | VI × Tokenization | `Text` + `Img` + `CF` | `E-commerce` |
| [AdaSID](../papers/adasid.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `E-commerce` |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | A: `Other` (Encoder of each compared baseline, unspecified) · B: `Text` + `Img` + `CF` | `E-commerce` · `Other` (Large-scale social media platform) |
| [CARD](../papers/card.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `E-commerce` |
| [CMRec](../papers/cmrec.md) | CIKM’26 Short | VI × Training | `Text` + `Img` + `CF` | `Ads` · `E-commerce` |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV × Training | A (Spotify): `Text` + `Audio` + `CF` · A (POG): `Text` + `Img` + `CF` · B: `Text` + `Img` | `Music` · `E-commerce` |
| [GenRec-JD](../papers/genrec-jd.md) | SIGIR’26 | IV × Training | `Text` + `Img` + `CF` | `E-commerce` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text` + `Img` + `Geo` + `CF` | `POI / Local` |
| [HASTE](../papers/haste.md) | arXiv’26 | IV × Training | A: `Text` · B: `MM` | `E-commerce` |
| [MMGRec](../papers/mmgrec.md) | TOMM’26 | I × Tokenization | `Text` + `Img` + `Audio` + `CF` | `Movie` · `Short video / Live` |
| [MMQ](../papers/mmq.md) | WSDM’26 | I × Tokenization | `Text` + `Img` | `E-commerce` · `Ads` |
| [OneLatent](../papers/onelatent.md) | arXiv’26 | V × Training | `MM` | `Ads` · `POI / Local` |
| [OneLive](../papers/onelive.md) | KDD’26 ADS | VI × Tokenization | `Text` + `Img` + `Audio` + `CF` | `Short video / Live` |
| [OneMall](../papers/onemall.md) | CIKM’26 | Paradigms, Systems and Benchmarks | A: `Text` + `Img` + `CF` · B: `Text` + `Img` + `CF` · C: `CF` + `Other` (Live-stream item-tower embeddings (product SIDs, item features)) | `E-commerce` |
| [OneRec-V2-Quantized](../papers/onerec-v2-quantized.md) | arXiv’26 | V × Inference | `Text` + `Img` + `CF` | `Short video / Live` |
| [PinGER](../papers/pinger.md) | arXiv’26 | V × Backbone | `Text` + `Img` + `CF` | `Image / Article` |
| [PLUM](../papers/plum.md) | WWW’26 | Paradigms, Systems and Benchmarks | `MM` + `CF` | `Long video` · `Short video / Live` |
| [PrefixMem](../papers/prefixmem.md) | arXiv’26 | III × Backbone | `MM` | `Image / Article` |
| [QuaSID](../papers/quasid.md) | KDD’26 ADS | II × Tokenization | `Text` + `Img` + `CF` | `E-commerce` |
| [RecoChain](../papers/recochain.md) | arXiv’26 | IV × Backbone | `MM` | `E-commerce` |
| [RoFiGR](../papers/rofigr.md) | arXiv’26 | I × Tokenization | text: `Text` + `Img` + `CF` · image: `Text` + `Img` + `CF` | `E-commerce` |
| [SAGE-SID](../papers/sage-sid.md) | arXiv’26 | IV × Training | `Text` + `Img` | `E-commerce` · `Short video / Live` · `Ads` |
| [SnapLGR](../papers/snaplgr.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `Short video / Live` |
| [STAMP](../papers/stamp.md) | arXiv’26 | V × Backbone | A: `Text` · B: `Text` + `Img` + `CF` | `E-commerce` |
| [Tlow](../papers/tlow.md) | CIKM’26 Applied | I × Tokenization | A: `Text` · B: `Text` + `Img` | `E-commerce` · `Image / Article` |
| [TriAlignGR](../papers/trialigngr.md) | arXiv’26 | I × Representation | `Text` + `Img` | `E-commerce` |
| [UniRec](../papers/unirec.md) | arXiv’26 | I × Tokenization | `MM` + `Attr` | `E-commerce` |
| [UniSID](../papers/unisid.md) | arXiv’26 | I × Tokenization | `Text` + `Img` | `Ads` · `E-commerce` |

## No content

> 11 papers. No tokenizer branch uses any content modality (`Text`, `Img`, `Audio`, `Video`, `MM`), and inputs across all branches contain no `Other` (nor `n/a`).

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [CID](../papers/cid.md) | SIGIR-AP’23 | II × Tokenization | `CF` | `E-commerce` · `POI / Local` |
| [ColaRec](../papers/colarec.md) | CIKM’24 | I × Backbone | `CF` | `E-commerce` · `Food / Recipe` |
| [MBGen](../papers/mbgen.md) | CIKM’24 | I × Training | `CF` | `E-commerce` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `CF` | `POI / Local` · `E-commerce` · `News` · `Short video / Live` |
| [ETEGRec](../papers/etegrec.md) | SIGIR’25 | III × Training | `CF` | `E-commerce` |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `POI / Local` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr` + `Geo` + `CF` | `POI / Local` |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `Geo` | `POI / Local` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I × Tokenization | `CF` | `Music` · `Movie` · `E-commerce` |
| [KL-MOPD](../papers/kl-mopd.md) | arXiv’26 | IV × Training | `CF` | `E-commerce` · `Ads` |
| [ReSID](../papers/resid.md) | arXiv’26 | I × Representation | `Attr` + `CF` | `E-commerce` |

## CF only

> 7 papers. Across all tokenizer branches combined, `CF` is the only input signal.

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [CID](../papers/cid.md) | SIGIR-AP’23 | II × Tokenization | `CF` | `E-commerce` · `POI / Local` |
| [ColaRec](../papers/colarec.md) | CIKM’24 | I × Backbone | `CF` | `E-commerce` · `Food / Recipe` |
| [MBGen](../papers/mbgen.md) | CIKM’24 | I × Training | `CF` | `E-commerce` |
| [SEATER](../papers/seater.md) | SIGIR-AP’24 | V × Tokenization | `CF` | `POI / Local` · `E-commerce` · `News` · `Short video / Live` |
| [ETEGRec](../papers/etegrec.md) | SIGIR’25 | III × Training | `CF` | `E-commerce` |
| [TokenRec](../papers/tokenrec.md) | TKDE’25 | I × Tokenization | `CF` | `Music` · `Movie` · `E-commerce` |
| [KL-MOPD](../papers/kl-mopd.md) | arXiv’26 | IV × Training | `CF` | `E-commerce` · `Ads` |

## With CF

> 52 papers. Across all tokenizer branches combined, inputs include `CF` together with at least one other modality or signal.

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [EAGER](../papers/eager.md) | KDD’24 | I × Backbone | semantic: `Text` · behavior: `CF` | `E-commerce` · `POI / Local` |
| [LETTER](../papers/letter.md) | CIKM’24 | I × Tokenization | `Text` + `CF` | `E-commerce` · `POI / Local` |
| [ADC-SID](../papers/adc-sid.md) | arXiv’25 | I × Tokenization | `Text` + `Img` + `CF` | `E-commerce` · `Ads` |
| [DAS](../papers/das.md) | CIKM’25 | I × Tokenization | `Text` + `CF` | `Ads` |
| [DiscRec](../papers/discrec.md) | arXiv’25 | I × Backbone | A: `Text` · B: `Text` + `CF` | `E-commerce` |
| [EAGER-LLM](../papers/eager-llm.md) | WWW’25 | I × Tokenization | semantic: `Text` · behavior: `CF` | `E-commerce` |
| [FlexCode](../papers/flexcode.md) | arXiv’25 | I × Tokenization | semantic: `Text` + `CF` · collaborative: `CF` | `E-commerce` · `Short video / Live` · `Other` (In-house data from an unnamed commercial platform) |
| [FORGE](../papers/forge.md) | KDD’26 | Paradigms, Systems and Benchmarks | `Text` + `Img` + `CF` | `E-commerce` · `Search` |
| [GenSAR](../papers/gensar.md) | RecSys’25 | I × Tokenization | semantic: `Text` + `CF` · collaborative: `Text` + `CF` | `E-commerce` · `Search` |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `POI / Local` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr` + `Geo` + `CF` | `POI / Local` |
| [MME-SID](../papers/mme-sid.md) | CIKM’25 | I × Tokenization | collaborative: `CF` · text: `Text` · visual: `Img` | `E-commerce` |
| [OneRec](../papers/onerec.md) | arXiv’25 | Paradigms, Systems and Benchmarks | `MM` + `CF` | `Short video / Live` |
| [OneRec-Think](../papers/onerec-think.md) | arXiv’25 | III × Training | `MM` + `CF` | `E-commerce` · `Short video / Live` |
| [OneRec-V2](../papers/onerec-v2.md) | arXiv’25 | V × Backbone | `Text` + `Img` + `CF` | `Short video / Live` |
| [SemConv](../papers/semconv.md) | AAAI’25 | III × Tokenization | `Text` + `CF` | `E-commerce` |
| [UNGER](../papers/unger.md) | TOIS’25 | I × Representation | `Text` + `CF` | `E-commerce` |
| [UTGRec](../papers/utgrec.md) | arXiv’25 | VI × Tokenization | `Text` + `Img` + `CF` | `E-commerce` |
| [AdaSID](../papers/adasid.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `E-commerce` |
| [Align3GR](../papers/align3gr.md) | AAAI’26 | III × Tokenization | `Text` + `CF` | `E-commerce` · `POI / Local` · `Ads` |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | A: `Other` (Encoder of each compared baseline, unspecified) · B: `Text` + `Img` + `CF` | `E-commerce` · `Other` (Large-scale social media platform) |
| [CARD](../papers/card.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `E-commerce` |
| [CMRec](../papers/cmrec.md) | CIKM’26 Short | VI × Training | `Text` + `Img` + `CF` | `Ads` · `E-commerce` |
| [DACT](../papers/dact.md) | SIGIR’26 | VI × Tokenization | `Text` + `CF` | `E-commerce` |
| [DOS](../papers/dos.md) | WWW’26 Short | III × Tokenization | `Text` + `CF` | `POI / Local` |
| [DPE-Rec](../papers/dpe-rec.md) | arXiv’26 | IV × Training | A (Spotify): `Text` + `Audio` + `CF` · A (POG): `Text` + `Img` + `CF` · B: `Text` + `Img` | `Music` · `E-commerce` |
| [DREAM](../papers/dream.md) | arXiv’26 | VI × Tokenization | `Text` + `CF` | `E-commerce` |
| [GenRec-JD](../papers/genrec-jd.md) | SIGIR’26 | IV × Training | `Text` + `Img` + `CF` | `E-commerce` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `Text` + `Geo` + `CF` | `POI / Local` · `Search` |
| [GFlowGR](../papers/gflowgr.md) | SIGIR’26 | IV × Training | A: `Text` · B: `Text` + `CF` | `POI / Local` · `E-commerce` · `Ads` · `Search` |
| [GrIS (RecDMoN / RQ-GAE)](../papers/gris-recdmon-rq-gae.md) | CIKM’26 | I × Tokenization | `Text` + `CF` | `E-commerce` · `News` · `POI / Local` |
| [GTI](../papers/gti.md) | arXiv’26 | III × Training | A: `Text` + `CF` · B: `Text` | `Recruitment` · `E-commerce` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text` + `Img` + `Geo` + `CF` | `POI / Local` |
| [LESSRec](../papers/lessrec.md) | arXiv’26 | III × Backbone | A: `Text` · B: `Text` + `CF` | `E-commerce` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text` + `Geo` + `Attr` + `CF` | `POI / Local` |
| [MMGRec](../papers/mmgrec.md) | TOMM’26 | I × Tokenization | `Text` + `Img` + `Audio` + `CF` | `Movie` · `Short video / Live` |
| [MSCGRec](../papers/mscgrec.md) | arXiv’26 | I × Tokenization | image: `Img` · text: `Text` · collaborative: `CF` | `E-commerce` · `Short video / Live` |
| [OneLive](../papers/onelive.md) | KDD’26 ADS | VI × Tokenization | `Text` + `Img` + `Audio` + `CF` | `Short video / Live` |
| [OneMall](../papers/onemall.md) | CIKM’26 | Paradigms, Systems and Benchmarks | A: `Text` + `Img` + `CF` · B: `Text` + `Img` + `CF` · C: `CF` + `Other` (Live-stream item-tower embeddings (product SIDs, item features)) | `E-commerce` |
| [OneRec-V2-Quantized](../papers/onerec-v2-quantized.md) | arXiv’26 | V × Inference | `Text` + `Img` + `CF` | `Short video / Live` |
| [PAD-Rec](../papers/pad-rec.md) | arXiv’26 | V × Inference | `Text` + `CF` | `E-commerce` · `POI / Local` |
| [PCR-CA](../papers/pcr-ca.md) | KDD’26 | I × Tokenization | `Text` + `CF` | `Apps` |
| [Pctx](../papers/pctx.md) | CIKM’26 | I × Tokenization | `Text` + `CF` | `E-commerce` |
| [PinGER](../papers/pinger.md) | arXiv’26 | V × Backbone | `Text` + `Img` + `CF` | `Image / Article` |
| [PLUM](../papers/plum.md) | WWW’26 | Paradigms, Systems and Benchmarks | `MM` + `CF` | `Long video` · `Short video / Live` |
| [QuaSID](../papers/quasid.md) | KDD’26 ADS | II × Tokenization | `Text` + `Img` + `CF` | `E-commerce` |
| [ReSID](../papers/resid.md) | arXiv’26 | I × Representation | `Attr` + `CF` | `E-commerce` |
| [RoFiGR](../papers/rofigr.md) | arXiv’26 | I × Tokenization | text: `Text` + `Img` + `CF` · image: `Text` + `Img` + `CF` | `E-commerce` |
| [S2GR](../papers/s2gr.md) | KDD’26 | III × Backbone | `Text` + `CF` | `E-commerce` · `Short video / Live` |
| [SCRec](../papers/screc.md) | RecSys’26 | I × Representation | `Text` + `CF` | `E-commerce` |
| [SnapLGR](../papers/snaplgr.md) | arXiv’26 | II × Tokenization | `Text` + `Img` + `CF` | `Short video / Live` |
| [STAMP](../papers/stamp.md) | arXiv’26 | V × Backbone | A: `Text` · B: `Text` + `Img` + `CF` | `E-commerce` |

## Attr

> 8 papers. Across all tokenizer branches combined, inputs include structured item attributes (`Attr`).

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `POI / Local` |
| [HiD-VAE](../papers/hid-vae.md) | arXiv’25 | II × Tokenization | `Text` + `Attr` | `E-commerce` · `Short video / Live` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr` + `Geo` + `CF` | `POI / Local` |
| [GR4AD-X](../papers/gr4ad-x.md) | arXiv’26 | III × Tokenization | `Other` (Ad semantic embedding, source unstated) + `Attr` | `Ads` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `Text` + `Attr` + `Geo` | `POI / Local` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text` + `Geo` + `Attr` + `CF` | `POI / Local` |
| [ReSID](../papers/resid.md) | arXiv’26 | I × Representation | `Attr` + `CF` | `E-commerce` |
| [UniRec](../papers/unirec.md) | arXiv’26 | I × Tokenization | `MM` + `Attr` | `E-commerce` |

## Geo

> 14 papers. Across all tokenizer branches combined, inputs include geographic or spatial features (`Geo`).

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `POI / Local` |
| [KGTB](../papers/kgtb.md) | arXiv’25 | I × Tokenization | `Attr` + `Geo` + `CF` | `POI / Local` |
| [OneLoc](../papers/oneloc.md) | arXiv’25 | I × Representation | `MM` + `Geo` | `POI / Local` |
| [QT-Mob](../papers/qt-mob.md) | KDD’25 | I × Tokenization | `Text` + `Geo` | `POI / Local` |
| [Spacetime-GR](../papers/spacetime-gr.md) | arXiv’25 | I × Backbone | `Geo` | `POI / Local` |
| [AWARE](../papers/aware.md) | arXiv’26 | VI × Training | `Text` + `Geo` | `POI / Local` |
| [GeoGR](../papers/geogr.md) | arXiv’26 | I × Representation | `Text` + `Geo` + `CF` | `POI / Local` · `Search` |
| [Gwhere](../papers/gwhere.md) | RecSys’26 | II × Tokenization | `Text` + `Img` + `Geo` + `CF` | `POI / Local` |
| [HF-SID](../papers/hf-sid.md) | arXiv’26 | I × Representation | `Text` + `Attr` + `Geo` | `POI / Local` |
| [LGRID](../papers/lgrid.md) | arXiv’26 | I × Representation | `Text` + `Geo` | `POI / Local` |
| [LGSID](../papers/lgsid.md) | AAAI’26 | I × Representation | `Text` + `Geo` + `Attr` + `CF` | `POI / Local` |
| [ProGEO](../papers/progeo.md) | arXiv’26 | I × Tokenization | `Text` + `Geo` | `POI / Local` · `Search` |
| [ROS](../papers/ros.md) | ACL’26 | I × Tokenization | `Text` + `Geo` | `POI / Local` |
| [SPAR](../papers/spar.md) | arXiv’26 | I × Representation | `Text` + `Geo` | `POI / Local` |

## Time

> 2 papers. Across all tokenizer branches combined, inputs include temporal features (`Time`).

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [GNPR-SID](../papers/gnpr-sid.md) | KDD’25 | I × Tokenization | `Attr` + `Geo` + `Time` + `CF` | `POI / Local` |
| [ChronoID](../papers/chronoid.md) | arXiv’26 | I × Tokenization | `Text` + `Time` | `E-commerce` |

## Other

> 25 papers. At least one branch reads an input outside the signals above, or one the paper does not state; each entry says what it is.

| Paper | Venue | Problem × Stage | SID Inputs | Domain |
| :--- | :--- | :--- | :--- | :--- |
| [CapsID](../papers/capsid.md) | arXiv’26 | I × Tokenization | A: `Other` (Encoder of each compared baseline, unspecified) · B: `Text` + `Img` + `CF` | `E-commerce` · `Other` (Large-scale social media platform) |
| [DASO](../papers/daso.md) | arXiv’26 | IV × Training | `Text` + `Other` (Internal 4-level, 2048-code SIDs; input unstated) | `E-commerce` · `Other` (Proprietary user-to-item data, business unstated) |
| [DiGR](../papers/digr.md) | arXiv’26 | IV × Backbone | `Other` (RQ-VAE SIDs, input unstated) | `E-commerce` |
| [DualGR](../papers/dualgr.md) | WWW’26 Short | VI × Backbone | `Other` (RQ-KMeans per OneRec Technical Report, input unstated) | `Short video / Live` |
| [Dynamic-Single-Codebook](../papers/dynamic-single-codebook.md) | arXiv’26 | V × Tokenization | `Other` (Precomputed item embeddings, source unstated) | `E-commerce` · `Short video / Live` · `Other` (Unnamed industrial platform, business unstated) |
| [GenCDR](../papers/gencdr.md) | AAAI’26 | VI × Tokenization | `Text` + `Other` (MTM masked-code context, source unstated) | `E-commerce` · `Book` · `Movie` |
| [GR4AD-X](../papers/gr4ad-x.md) | arXiv’26 | III × Tokenization | `Other` (Ad semantic embedding, source unstated) + `Attr` | `Ads` |
| [Gryphon](../papers/gryphon.md) | CIKM’26 Short | IV × Backbone | `Other` (Residual K-Means SIDs, input unstated) | `Music` |
| [HCGRec](../papers/hcgrec.md) | CIKM’26 | IV × Training | `Other` (Four-token SIDs per GenRec pipeline, input unstated) | `E-commerce` |
| [HoloRec](../papers/holorec.md) | arXiv’26 | III × Tokenization | `Other` (Item "original embedding", source unstated) | `E-commerce` |
| [Latte](../papers/latte.md) | arXiv’26 | III × Backbone | `Other` (PSID with RQ-KMeans, input unstated) | `E-commerce` · `Music` |
| [MBGR](../papers/mbgr.md) | arXiv’26 | VI × Tokenization | `Other` (BID token embeddings; original SID inputs unstated) | `Ads` |
| [MuSID-KD](../papers/musid-kd.md) | arXiv’26 | IV × Training | `Other` (TIGER teacher SIDs; tokenizer inputs unstated) | `E-commerce` · `Games` |
| [NAU](../papers/nau.md) | arXiv’26 | IV × Training | `Other` (Pre-quantization item embeddings; source signals unstated) | `E-commerce` |
| [Netflix-SID-Comparison](../papers/netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | Paradigms, Systems and Benchmarks | `Other` (Content embeddings; constituent modalities unstated) | `Long video` |
| [OneChord](../papers/onechord.md) | arXiv’26 | IV × Training | `Other` (Fixed OPQ index; quantizer inputs unstated) | `E-commerce` |
| [OneMall](../papers/onemall.md) | CIKM’26 | Paradigms, Systems and Benchmarks | A: `Text` + `Img` + `CF` · B: `Text` + `Img` + `CF` · C: `CF` + `Other` (Live-stream item-tower embeddings (product SIDs, item features)) | `E-commerce` |
| [PFA](../papers/pfa.md) | arXiv’26 | V × Inference | `Other` (Four-level SIDs; tokenizer inputs unstated) | `E-commerce` · `Ads` |
| [SIDScope](../papers/sidscope.md) | arXiv’26 | Paradigms, Systems and Benchmarks | `Other` (Released and reconstructed item-to-SID mappings) | `E-commerce` · `POI / Local` |
| [SLIDE](../papers/slide.md) | arXiv’26 | IV × Training | `Other` (FORGE SIDs; Taobao tokenizer inputs unstated) | `E-commerce` · `Search` |
| [SPAR-Youku](../papers/spar-youku.md) | arXiv’26 | I × Backbone | `Other` (RQ-PIB item embeddings; source signals unstated) | `Long video` |
| [STATIC](../papers/static.md) | KDD’26 ADS | V × Inference | `Other` (RQ-VAE item features; source modalities unstated) | `E-commerce` · `Video` |
| [Think2Go](../papers/think2go.md) | KDD’26 | III × Training | `Other` (RQ-VAE POI identifiers; tokenizer inputs unstated) | `POI / Local` |
| [UniSGR-V2](../papers/unisgr-v2.md) | arXiv’26 | I × Backbone | `Other` (Three-level SIDs; tokenizer inputs unstated) | `E-commerce` |
| [V-STAR](../papers/v-star.md) | KDD’26 | IV × Training | `Other` (RQ-VAE SIDs; tokenizer inputs unstated) | `E-commerce` · `Ads` |
