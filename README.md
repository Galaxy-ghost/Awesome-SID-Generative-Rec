<!--lint disable awesome-github-->
# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Scope

This list collects 181 papers on generative recommendation with Semantic IDs (SIDs). The matrix places 169 of them by the problem each paper fixes and the pipeline stage it mainly changes. The other 12 are paradigms, systems and benchmarks. It also includes methods that use SIDs as features. Papers on POI and local-life recommendation carry a `POI` tag and are listed in the [POI index](pages/index/poi.md).

## Where to Start

- New to the topic: [Start Here](guides/start-here.md)
- Looking for research problems: [Problem × Stage Matrix](#problem--stage-matrix)
- Choosing a method by stage: [Papers by Stage](pages/index/stages.md)
- Looking for code: [Papers with Code](pages/index/code.md)
- LLMs and tools: [llms.txt](llms.txt)

## Starter Papers

- [TIGER][] - TIGER encodes item text into RQ-VAE Semantic IDs and trains a Transformer encoder-decoder to decode the next item's ID, instead of retrieving items by approximate nearest neighbor search.
- [OneLoc][] - OneLoc extends end-to-end generative recommendation to local-life videos by adding geographic information to tokenization, encoder attention, and a decoder prompt, and by DPO with geographic and GMV rewards.
- [RPG][] - RPG predicts long, unordered OPQ Semantic IDs in parallel with a multi-token prediction loss and decodes over a graph of valid IDs, replacing autoregressive beam search over short IDs.

## Problem × Stage Matrix

| Problem                         |                                      Representation                                     |                                       Tokenization                                      |                                      Backbone                                     |                                      Training                                      |                                     Inference                                      |  Total  |
| :------------------------------ | :-------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: | :-----: |
| **I.** Informativeness          | [![12](https://img.shields.io/badge/12-2171b5?style=for-the-badge)](#i--representation) |  [![34](https://img.shields.io/badge/34-08306b?style=for-the-badge)](#i--tokenization)  |  [![7](https://img.shields.io/badge/7-6baed6?style=for-the-badge)](#i--backbone)  |  [![4](https://img.shields.io/badge/4-6baed6?style=for-the-badge)](#i--training)   |  [![2](https://img.shields.io/badge/2-c6dbef?style=for-the-badge)](#i--inference)  |  **59** |
| **II.** Uniqueness and Validity |                                                                                         |  [![12](https://img.shields.io/badge/12-2171b5?style=for-the-badge)](#ii--tokenization) |                                                                                   |                                                                                    |                                                                                    |  **12** |
| **III.** SID–Model Alignment    |                                                                                         | [![11](https://img.shields.io/badge/11-2171b5?style=for-the-badge)](#iii--tokenization) | [![9](https://img.shields.io/badge/9-2171b5?style=for-the-badge)](#iii--backbone) | [![9](https://img.shields.io/badge/9-2171b5?style=for-the-badge)](#iii--training)  | [![2](https://img.shields.io/badge/2-c6dbef?style=for-the-badge)](#iii--inference) |  **31** |
| **IV.** Utility                 |                                                                                         |   [![1](https://img.shields.io/badge/1-c6dbef?style=for-the-badge)](#iv--tokenization)  |  [![3](https://img.shields.io/badge/3-c6dbef?style=for-the-badge)](#iv--backbone) | [![22](https://img.shields.io/badge/22-08306b?style=for-the-badge)](#iv--training) | [![2](https://img.shields.io/badge/2-c6dbef?style=for-the-badge)](#iv--inference)  |  **28** |
| **V.** Efficiency               |                                                                                         |   [![3](https://img.shields.io/badge/3-c6dbef?style=for-the-badge)](#v--tokenization)   | [![11](https://img.shields.io/badge/11-2171b5?style=for-the-badge)](#v--backbone) |  [![1](https://img.shields.io/badge/1-c6dbef?style=for-the-badge)](#v--training)   |  [![6](https://img.shields.io/badge/6-6baed6?style=for-the-badge)](#v--inference)  |  **21** |
| **VI.** Generalization          |                                                                                         |   [![9](https://img.shields.io/badge/9-2171b5?style=for-the-badge)](#vi--tokenization)  |  [![3](https://img.shields.io/badge/3-c6dbef?style=for-the-badge)](#vi--backbone) |  [![4](https://img.shields.io/badge/4-6baed6?style=for-the-badge)](#vi--training)  | [![2](https://img.shields.io/badge/2-c6dbef?style=for-the-badge)](#vi--inference)  |  **18** |
| **Total**                       |                                          **12**                                         |                                          **70**                                         |                                       **33**                                      |                                       **40**                                       |                                       **14**                                       | **169** |

Click a count to jump to its papers; darker means more papers.

| Mark       | Meaning                                                                                           |
| :--------- | :------------------------------------------------------------------------------------------------ |
| `†`        | Inferred: the paper does not restate the setting; it is inferred from the configuration it names. |
| `A / B`    | Different branches or configurations of the method.                                               |
| `–`        | Not reported.                                                                                     |
| `n/a`      | Not applicable.                                                                                   |
| **Bold**   | The stage the paper mainly changes.                                                               |
| Empty cell | No paper has that cell as its main label yet. It does not mean a research gap.                    |
| `warm`     | A protocol label in a setup card. It does not prove that every test item appeared in training.    |

The [glossary](guides/glossary.md) defines every value in the paper pages.

## Recent Updates

- 2026-11-01: The paper pages gained a new template with reading levels, setup cards, and related-work links; five sample pages were rewritten, and index pages and a glossary were added. Papers: [TIGER][], [RPG][], [OneLoc][], [LETTER][], [SIDScope][].
- 2026-10-30: Table 1 of the survey was frozen at 181 papers, and the records were synchronized with it.

## All Papers

- [Paradigms, Systems and Benchmarks][]
- [I. Informativeness][]
- [II. Uniqueness and Validity][]
- [III. SID–Model Alignment][]
- [IV. Utility][]
- [V. Efficiency][]
- [VI. Generalization][]

## Paradigms, Systems and Benchmarks

> Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources.

- [TIGER][] - NeurIPS’23<br>
  TIGER encodes item text into RQ-VAE Semantic IDs and trains a Transformer encoder-decoder to decode the next item's ID, instead of retrieving items by approximate nearest neighbor search.<br>
  [Paper](https://arxiv.org/abs/2305.05065) · [Code (third-party)](https://github.com/baiyimeng/TIGER)
- [FORGE][] - KDD’26<br>
  [Paper](https://arxiv.org/abs/2509.20904) · [Code](https://github.com/selous123/al_sid)
- [GRID][] - CIKM’25<br>
  [Paper](https://arxiv.org/abs/2507.22224)
- [MiniOneRec][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2510.24431) · [Code](https://github.com/AkaliKong/MiniOneRec)
- [OneRec][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2502.18965)
- [GR-Generalize][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2603.19809)
- [NEO][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2603.17533)
- [Netflix-SID-Comparison][] - NeurIPS’26 PALM Workshop<br>
  [Paper](https://arxiv.org/abs/2610.15864)
- [OneMall][] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2601.21770)
- [PLUM][] - WWW’26<br>
  [Paper](https://arxiv.org/abs/2510.07784)
- [ReRankID][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.22797)
- [SIDScope][] - arXiv’26<br>
  SIDScope is a diagnostic resource, not a new recommender: it checks released Semantic ID mappings for code organization, item resolution, and model compatibility after a refresh.<br>
  [Paper](https://arxiv.org/abs/2608.18779) · [Code](https://github.com/jdding/sidscope)

## I. Informativeness

> Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs?

### I × Representation

- [Molar][] - arXiv’24<br>
  [Paper](https://arxiv.org/abs/2412.18176)
- [OneLoc][] - arXiv’25 · `POI`<br>
  OneLoc extends end-to-end generative recommendation to local-life videos by adding geographic information to tokenization, encoder attention, and a decoder prompt, and by DPO with geographic and GMV rewards.<br>
  [Paper](https://arxiv.org/abs/2508.14646)
- [Q-BERT4Rec][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2512.02474)
- [UNGER][] - TOIS’25<br>
  [Paper](https://arxiv.org/abs/2502.06269)
- [GeoGR][] - arXiv’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2602.10411)
- [HF-SID][] - arXiv’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2608.30479)
- [LGRID][] - arXiv’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2607.27944)
- [LGSID][] - AAAI’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2511.14221)
- [ReSID][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2602.02338)
- [SCRec][] - RecSys’26<br>
  [Paper](https://arxiv.org/abs/2609.13678)
- [SPAR][] - arXiv’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2609.02062)
- [TriAlignGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2605.05249)

### I × Tokenization

- [CoST][] - RecSys’24<br>
  [Paper](https://arxiv.org/abs/2404.14774)
- [LETTER][] - CIKM’24<br>
  LETTER regularizes an RQ-VAE tokenizer with a collaborative alignment loss and a diversity loss, so that item SIDs carry collaborative signals and reduce code assignment bias found in earlier identifiers.<br>
  [Paper](https://arxiv.org/abs/2405.07314) · [Code](https://github.com/HonghuiBao2000/LETTER)
- [LMIndexer][] - ICML’24<br>
  [Paper](https://arxiv.org/abs/2310.07815)
- [ActionPiece][] - ICML’25<br>
  [Paper](https://arxiv.org/abs/2502.13581) · [Code](https://github.com/google-deepmind/action_piece)
- [ADC-SID][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2510.25622)
- [DAS][] - CIKM’25<br>
  [Paper](https://arxiv.org/abs/2508.10584)
- [EAGER-LLM][] - WWW’25<br>
  [Paper](https://arxiv.org/abs/2502.14735)
- [FlexCode][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2511.20673)
- [GenSAR][] - RecSys’25<br>
  [Paper](https://arxiv.org/abs/2504.05730)
- [GNPR-SID][] - KDD’25 · `POI`<br>
  [Paper](https://arxiv.org/abs/2506.01375) · [Code](https://github.com/wds1996/GNPR-SID)
- [GRAM][] - ACL’25<br>
  [Paper](https://arxiv.org/abs/2506.01673)
- [KGTB][] - arXiv’25 · `POI`<br>
  [Paper](https://arxiv.org/abs/2509.12350)
- [MME-SID][] - CIKM’25<br>
  [Paper](https://arxiv.org/abs/2509.02017)
- [MQL4GRec][] - ICLR’25<br>
  [Paper](https://arxiv.org/abs/2504.05314)
- [PSRQ][] - CIKM’25<br>
  [Paper](https://arxiv.org/abs/2508.20359)
- [QT-Mob][] - KDD’25 · `POI`<br>
  [Paper](https://arxiv.org/abs/2506.11109)
- [TokenRec][] - TKDE’25<br>
  [Paper](https://arxiv.org/abs/2406.10450)
- [CapsID][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2605.05096)
- [ChronoID][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2606.14260)
- [GrIS (RecDMoN / RQ-GAE)][gris-recdmon-rq-gae] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2610.01533)
- [MACRec][] - AAAI’26<br>
  [Paper](https://arxiv.org/abs/2511.15122)
- [MMGRec][] - TOMM’26<br>
  [Paper](https://arxiv.org/abs/2404.16555)
- [MMQ][] - WSDM’26<br>
  [Paper](https://arxiv.org/abs/2508.15281)
- [MSCGRec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2602.03713)
- [PCR-CA][] - KDD’26<br>
  [Paper](https://arxiv.org/abs/2508.18166)
- [Pctx][] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2510.21276)
- [ProGEO][] - arXiv’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2604.23156)
- [RoFiGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.39470)
- [ROS][] - ACL’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2601.04562)
- [SPRIG][] - CIKM’26 Short<br>
  [Paper](https://arxiv.org/abs/2610.06590)
- [Tlow][] - CIKM’26 Applied<br>
  [Paper](https://arxiv.org/abs/2608.24176)
- [UniRec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.12234)
- [UniSID][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2602.10445)
- [VarLenRec (TIGER)][varlenrec-tiger] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2605.17779)

### I × Backbone

- [ColaRec][] - CIKM’24<br>
  [Paper](https://arxiv.org/abs/2403.18480)
- [EAGER][] - KDD’24<br>
  [Paper](https://arxiv.org/abs/2406.14017) · [Code](https://github.com/yewzz/EAGER)
- [COBRA][] - NeurIPS’25<br>
  [Paper](https://arxiv.org/abs/2503.02453)
- [DiscRec][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2506.15576)
- [Spacetime-GR][] - arXiv’25 · `POI`<br>
  [Paper](https://arxiv.org/abs/2508.16126)
- [SPAR-Youku][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.27898)
- [UniSGR-V2][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.16132)

### I × Training

- [MBGen][] - CIKM’24<br>
  [Paper](https://arxiv.org/abs/2405.16871)
- [RAGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2605.17267)
- [REGER][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.37584)
- [SynGR][] - ICML’26<br>
  [Paper](https://arxiv.org/abs/2605.18920)

### I × Inference

- [CAPE][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.29298)
- [CITE][] - Electronics’26<br>
  [Paper](https://doi.org/10.3390/electronics15204749)

## II. Uniqueness and Validity

> Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly?

### II × Tokenization

- [CID][] - SIGIR-AP’23<br>
  [Paper](https://arxiv.org/abs/2305.06569)
- [TransRec][] - KDD’24<br>
  [Paper](https://arxiv.org/abs/2310.06491)
- [HiD-VAE][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2508.04618)
- [PSI][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2509.16446)
- [AdaSID][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.23522)
- [API][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.36763)
- [CARD][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.26427)
- [DIGER][] - SIGIR’26<br>
  [Paper](https://arxiv.org/abs/2601.19711)
- [Gwhere][] - RecSys’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2607.26073) · [Code](https://github.com/alibaba/SimCIT)
- [QuaSID][] - KDD’26 ADS<br>
  [Paper](https://arxiv.org/abs/2603.00632)
- [R3-VAE][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.11440)
- [SnapLGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2607.28895)

## III. SID–Model Alignment

> Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal?

### III × Tokenization

- [IDGenRec][] - SIGIR’24<br>
  [Paper](https://arxiv.org/abs/2403.19021)
- [SIIT][] - arXiv’24<br>
  [Paper](https://arxiv.org/abs/2412.17171)
- [SemConv][] - AAAI’25<br>
  [Paper](https://arxiv.org/abs/2412.13771)
- [Align3GR][] - AAAI’26<br>
  [Paper](https://arxiv.org/abs/2511.11255)
- [CogRec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2607.24402)
- [DOS][] - WWW’26 Short · `POI`<br>
  [Paper](https://arxiv.org/abs/2602.04460)
- [GR4AD-X][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.38378)
- [GRLM][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2601.06798)
- [HoloRec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2606.15331)
- [SST][] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2608.22734)
- [TopoGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2607.25216)

### III × Backbone

- [LLaDA-Rec][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2511.06254)
- [DECOR][] - SIGIR’26<br>
  [Paper](https://arxiv.org/abs/2509.10468)
- [FLASH][] - NeurIPS’26<br>
  [Paper](https://arxiv.org/abs/2610.07402)
- [Latte][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2605.06331)
- [LESSRec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.37286)
- [MDGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2601.19501)
- [PrefixMem][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2606.00324)
- [S2GR][] - KDD’26<br>
  [Paper](https://arxiv.org/abs/2601.18664)
- [TrieRec][] - NeurIPS’26<br>
  [Paper](https://arxiv.org/abs/2602.21677)

### III × Training

- [LC-Rec][] - ICDE’24<br>
  [Paper](https://arxiv.org/abs/2311.09049)
- [ETEGRec][] - SIGIR’25<br>
  [Paper](https://arxiv.org/abs/2409.05546)
- [GREAM][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2510.20815)
- [OneRec-Think][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2510.11639)
- [Evo-Rec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2609.29973)
- [GTI][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.02324)
- [Intent-Driven-News][] - ACL’26 Industry<br>
  [Paper](https://arxiv.org/abs/2605.07613)
- [SIDReasoner][] - KDD’26<br>
  [Paper](https://arxiv.org/abs/2603.23183)
- [Think2Go][] - KDD’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2607.28997)

### III × Inference

- [GRC][] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2602.23639)
- [PROMISE][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2601.04674)

## IV. Utility

> Are training and search aimed at what users and the platform value, rather than at token likelihood?

### IV × Tokenization

- [TRACER][] - NeurIPS’26<br>
  [Paper](https://arxiv.org/abs/2606.07688)

### IV × Backbone

- [DiGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2602.07847)
- [Gryphon][] - CIKM’26 Short<br>
  [Paper](https://arxiv.org/abs/2606.08604)
- [RecoChain][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.25787)

### IV × Training

- [APAO][] - KDD’26<br>
  [Paper](https://arxiv.org/abs/2603.02730)
- [DASO][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2608.20611)
- [DPE-Rec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.34700)
- [GEM-Rec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2603.22231)
- [GenRec-JD][] - SIGIR’26<br>
  [Paper](https://arxiv.org/abs/2604.14878)
- [GFlowGR][] - SIGIR’26<br>
  [Paper](https://arxiv.org/abs/2506.16114)
- [Ghost][] - NeurIPS’26<br>
  [Paper](https://arxiv.org/abs/2605.16825)
- [HASTE][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.17368)
- [HCGRec][] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2608.11980)
- [IDM/CMM][idm-cmm] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.32943)
- [KL-MOPD][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.36973)
- [MuSID-KD][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.35218)
- [NAU][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.27232)
- [OneChord][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.25805)
- [Retrieval-Grounded-Credit][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2609.29983)
- [SAGE-SID][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2601.21452)
- [SAHL][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.25093)
- [SAPO][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2605.17648)
- [SLIDE][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.34764)
- [Token-Weighted][] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2601.17787)
- [UGR][] - KDD’26<br>
  [Paper](https://arxiv.org/abs/2602.11719)
- [V-STAR][] - KDD’26<br>
  [Paper](https://arxiv.org/abs/2602.10699)

### IV × Inference

- [ISD][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2607.24995)
- [TCBSA][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.32098)

## V. Efficiency

> Can it be trained and served within latency and cost budgets?

### V × Tokenization

- [SEATER][] - SIGIR-AP’24<br>
  [Paper](https://arxiv.org/abs/2309.13375)
- [Dynamic-Single-Codebook][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2608.21012)
- [JevRec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.36937)

### V × Backbone

- [OneRec-V2][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2508.20900)
- [RPG][] - KDD’25<br>
  RPG predicts long, unordered OPQ Semantic IDs in parallel with a multi-token prediction loss and decodes over a graph of valid IDs, replacing autoregressive beam search over short IDs.<br>
  [Paper](https://arxiv.org/abs/2506.05781) · [Code](https://github.com/facebookresearch/RPG_KDD2025)
- [ACERec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2602.13573)
- [Deco][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.32980)
- [IBA][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2607.12425)
- [LoopGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.34157)
- [Merge-and-Branch][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.37973)
- [PinGER][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.33435)
- [SID-MLP][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2605.12617)
- [SPRINT][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2609.34306)
- [STAMP][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.05329)

### V × Training

- [OneLatent][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.30675)

### V × Inference

- [AtSpeed][] - ICLR’25<br>
  [Paper](https://arxiv.org/abs/2410.05165)
- [NEZHA][] - WWW’26 Industry<br>
  [Paper](https://arxiv.org/abs/2511.18793)
- [OneRec-V2-Quantized][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2603.11486)
- [PAD-Rec][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.27747)
- [PFA][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2610.39273)
- [STATIC][] - KDD’26 ADS<br>
  [Paper](https://arxiv.org/abs/2602.22647)

## VI. Generalization

> Does it still work for new items, new domains, and shifting interests?

### VI × Tokenization

- [VQ-Rec][] - WWW’23<br>
  [Paper](https://arxiv.org/abs/2210.12316)
- [GMC][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2507.12871)
- [UTGRec][] - arXiv’25<br>
  [Paper](https://arxiv.org/abs/2504.04405)
- [DACT][] - SIGIR’26<br>
  [Paper](https://arxiv.org/abs/2603.29705)
- [DREAM][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2606.06947)
- [GenCDR][] - AAAI’26<br>
  [Paper](https://arxiv.org/abs/2511.08006)
- [MBGR][] - arXiv’26<br>
  [Paper](https://arxiv.org/abs/2604.02684)
- [OneLive][] - KDD’26 ADS<br>
  [Paper](https://arxiv.org/abs/2602.08612)
- [UniTok][] - AAAI’26<br>
  [Paper](https://arxiv.org/abs/2511.12922)

### VI × Backbone

- [DualGR][] - WWW’26 Short<br>
  [Paper](https://arxiv.org/abs/2511.12518)
- [FedCGR][] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2608.10929)
- [LION][] - CIKM’26<br>
  [Paper](https://arxiv.org/abs/2609.15598)

### VI × Training

- [RecBase][] - EMNLP’25<br>
  [Paper](https://arxiv.org/abs/2509.03131)
- [AWARE][] - arXiv’26 · `POI`<br>
  [Paper](https://arxiv.org/abs/2605.11807)
- [CausalDPO][] - ICML’26<br>
  [Paper](https://arxiv.org/abs/2603.22335)
- [CMRec][] - CIKM’26 Short<br>
  [Paper](https://arxiv.org/abs/2609.28972)

### VI × Inference

- [LIGER][] - arXiv’24<br>
  [Paper](https://arxiv.org/abs/2411.18814)
- [SpecGR][] - AAAI’26<br>
  [Paper](https://arxiv.org/abs/2410.02939)

## Contributing

Add one YAML record and run `make build && make check`; see [`CONTRIBUTING.md`](CONTRIBUTING.md).

[paradigms, systems and benchmarks]: #paradigms-systems-and-benchmarks
[i. informativeness]: #i-informativeness
[ii. uniqueness and validity]: #ii-uniqueness-and-validity
[iii. sid–model alignment]: #iii-sidmodel-alignment
[iv. utility]: #iv-utility
[v. efficiency]: #v-efficiency
[vi. generalization]: #vi-generalization
[acerec]: pages/papers/acerec.md
[actionpiece]: pages/papers/actionpiece.md
[adasid]: pages/papers/adasid.md
[adc-sid]: pages/papers/adc-sid.md
[align3gr]: pages/papers/align3gr.md
[apao]: pages/papers/apao.md
[api]: pages/papers/api.md
[atspeed]: pages/papers/atspeed.md
[aware]: pages/papers/aware.md
[cape]: pages/papers/cape.md
[capsid]: pages/papers/capsid.md
[card]: pages/papers/card.md
[causaldpo]: pages/papers/causaldpo.md
[chronoid]: pages/papers/chronoid.md
[cid]: pages/papers/cid.md
[cite]: pages/papers/cite.md
[cmrec]: pages/papers/cmrec.md
[cobra]: pages/papers/cobra.md
[cogrec]: pages/papers/cogrec.md
[colarec]: pages/papers/colarec.md
[cost]: pages/papers/cost.md
[dact]: pages/papers/dact.md
[das]: pages/papers/das.md
[daso]: pages/papers/daso.md
[deco]: pages/papers/deco.md
[decor]: pages/papers/decor.md
[diger]: pages/papers/diger.md
[digr]: pages/papers/digr.md
[discrec]: pages/papers/discrec.md
[dos]: pages/papers/dos.md
[dpe-rec]: pages/papers/dpe-rec.md
[dream]: pages/papers/dream.md
[dualgr]: pages/papers/dualgr.md
[dynamic-single-codebook]: pages/papers/dynamic-single-codebook.md
[eager]: pages/papers/eager.md
[eager-llm]: pages/papers/eager-llm.md
[etegrec]: pages/papers/etegrec.md
[evo-rec]: pages/papers/evo-rec.md
[fedcgr]: pages/papers/fedcgr.md
[flash]: pages/papers/flash.md
[flexcode]: pages/papers/flexcode.md
[forge]: pages/papers/forge.md
[gem-rec]: pages/papers/gem-rec.md
[gencdr]: pages/papers/gencdr.md
[genrec-jd]: pages/papers/genrec-jd.md
[gensar]: pages/papers/gensar.md
[geogr]: pages/papers/geogr.md
[gflowgr]: pages/papers/gflowgr.md
[ghost]: pages/papers/ghost.md
[gmc]: pages/papers/gmc.md
[gnpr-sid]: pages/papers/gnpr-sid.md
[gr-generalize]: pages/papers/gr-generalize.md
[gr4ad-x]: pages/papers/gr4ad-x.md
[gram]: pages/papers/gram.md
[grc]: pages/papers/grc.md
[gream]: pages/papers/gream.md
[grid]: pages/papers/grid.md
[gris-recdmon-rq-gae]: pages/papers/gris-recdmon-rq-gae.md
[grlm]: pages/papers/grlm.md
[gryphon]: pages/papers/gryphon.md
[gti]: pages/papers/gti.md
[gwhere]: pages/papers/gwhere.md
[haste]: pages/papers/haste.md
[hcgrec]: pages/papers/hcgrec.md
[hf-sid]: pages/papers/hf-sid.md
[hid-vae]: pages/papers/hid-vae.md
[holorec]: pages/papers/holorec.md
[iba]: pages/papers/iba.md
[idgenrec]: pages/papers/idgenrec.md
[idm-cmm]: pages/papers/idm-cmm.md
[intent-driven-news]: pages/papers/intent-driven-news.md
[isd]: pages/papers/isd.md
[jevrec]: pages/papers/jevrec.md
[kgtb]: pages/papers/kgtb.md
[kl-mopd]: pages/papers/kl-mopd.md
[latte]: pages/papers/latte.md
[lc-rec]: pages/papers/lc-rec.md
[lessrec]: pages/papers/lessrec.md
[letter]: pages/papers/letter.md
[lgrid]: pages/papers/lgrid.md
[lgsid]: pages/papers/lgsid.md
[liger]: pages/papers/liger.md
[lion]: pages/papers/lion.md
[llada-rec]: pages/papers/llada-rec.md
[lmindexer]: pages/papers/lmindexer.md
[loopgr]: pages/papers/loopgr.md
[macrec]: pages/papers/macrec.md
[mbgen]: pages/papers/mbgen.md
[mbgr]: pages/papers/mbgr.md
[mdgr]: pages/papers/mdgr.md
[merge-and-branch]: pages/papers/merge-and-branch.md
[minionerec]: pages/papers/minionerec.md
[mme-sid]: pages/papers/mme-sid.md
[mmgrec]: pages/papers/mmgrec.md
[mmq]: pages/papers/mmq.md
[molar]: pages/papers/molar.md
[mql4grec]: pages/papers/mql4grec.md
[mscgrec]: pages/papers/mscgrec.md
[musid-kd]: pages/papers/musid-kd.md
[nau]: pages/papers/nau.md
[neo]: pages/papers/neo.md
[netflix-sid-comparison]: pages/papers/netflix-sid-comparison.md
[nezha]: pages/papers/nezha.md
[onechord]: pages/papers/onechord.md
[onelatent]: pages/papers/onelatent.md
[onelive]: pages/papers/onelive.md
[oneloc]: pages/papers/oneloc.md
[onemall]: pages/papers/onemall.md
[onerec]: pages/papers/onerec.md
[onerec-think]: pages/papers/onerec-think.md
[onerec-v2]: pages/papers/onerec-v2.md
[onerec-v2-quantized]: pages/papers/onerec-v2-quantized.md
[pad-rec]: pages/papers/pad-rec.md
[pcr-ca]: pages/papers/pcr-ca.md
[pctx]: pages/papers/pctx.md
[pfa]: pages/papers/pfa.md
[pinger]: pages/papers/pinger.md
[plum]: pages/papers/plum.md
[prefixmem]: pages/papers/prefixmem.md
[progeo]: pages/papers/progeo.md
[promise]: pages/papers/promise.md
[psi]: pages/papers/psi.md
[psrq]: pages/papers/psrq.md
[q-bert4rec]: pages/papers/q-bert4rec.md
[qt-mob]: pages/papers/qt-mob.md
[quasid]: pages/papers/quasid.md
[r3-vae]: pages/papers/r3-vae.md
[ragr]: pages/papers/ragr.md
[recbase]: pages/papers/recbase.md
[recochain]: pages/papers/recochain.md
[reger]: pages/papers/reger.md
[rerankid]: pages/papers/rerankid.md
[resid]: pages/papers/resid.md
[retrieval-grounded-credit]: pages/papers/retrieval-grounded-credit.md
[rofigr]: pages/papers/rofigr.md
[ros]: pages/papers/ros.md
[rpg]: pages/papers/rpg.md
[s2gr]: pages/papers/s2gr.md
[sage-sid]: pages/papers/sage-sid.md
[sahl]: pages/papers/sahl.md
[sapo]: pages/papers/sapo.md
[screc]: pages/papers/screc.md
[seater]: pages/papers/seater.md
[semconv]: pages/papers/semconv.md
[sid-mlp]: pages/papers/sid-mlp.md
[sidreasoner]: pages/papers/sidreasoner.md
[sidscope]: pages/papers/sidscope.md
[siit]: pages/papers/siit.md
[slide]: pages/papers/slide.md
[snaplgr]: pages/papers/snaplgr.md
[spacetime-gr]: pages/papers/spacetime-gr.md
[spar]: pages/papers/spar.md
[spar-youku]: pages/papers/spar-youku.md
[specgr]: pages/papers/specgr.md
[sprig]: pages/papers/sprig.md
[sprint]: pages/papers/sprint.md
[sst]: pages/papers/sst.md
[stamp]: pages/papers/stamp.md
[static]: pages/papers/static.md
[syngr]: pages/papers/syngr.md
[tcbsa]: pages/papers/tcbsa.md
[think2go]: pages/papers/think2go.md
[tiger]: pages/papers/tiger.md
[tlow]: pages/papers/tlow.md
[token-weighted]: pages/papers/token-weighted.md
[tokenrec]: pages/papers/tokenrec.md
[topogr]: pages/papers/topogr.md
[tracer]: pages/papers/tracer.md
[transrec]: pages/papers/transrec.md
[trialigngr]: pages/papers/trialigngr.md
[trierec]: pages/papers/trierec.md
[ugr]: pages/papers/ugr.md
[unger]: pages/papers/unger.md
[unirec]: pages/papers/unirec.md
[unisgr-v2]: pages/papers/unisgr-v2.md
[unisid]: pages/papers/unisid.md
[unitok]: pages/papers/unitok.md
[utgrec]: pages/papers/utgrec.md
[v-star]: pages/papers/v-star.md
[varlenrec-tiger]: pages/papers/varlenrec-tiger.md
[vq-rec]: pages/papers/vq-rec.md
