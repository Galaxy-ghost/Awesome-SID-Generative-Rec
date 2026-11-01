<!--lint disable awesome-github-->
# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 181 papers on generative recommendation with Semantic IDs, sorted by the problem each paper fixes (rows) and the pipeline stage it changes (columns).

| Problem                         |                                      Representation                                     |                                       Tokenization                                      |                                      Backbone                                     |                                      Training                                      |                                     Inference                                      |  Total  |
| :------------------------------ | :-------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------: | :-----: |
| **I.** Informativeness          | [![12](https://img.shields.io/badge/12-2171b5?style=for-the-badge)](#i--representation) |  [![34](https://img.shields.io/badge/34-08306b?style=for-the-badge)](#i--tokenization)  |  [![7](https://img.shields.io/badge/7-6baed6?style=for-the-badge)](#i--backbone)  |  [![4](https://img.shields.io/badge/4-6baed6?style=for-the-badge)](#i--training)   |  [![2](https://img.shields.io/badge/2-c6dbef?style=for-the-badge)](#i--inference)  |  **59** |
| **II.** Uniqueness and Validity |                                            ·                                            |  [![12](https://img.shields.io/badge/12-2171b5?style=for-the-badge)](#ii--tokenization) |                                         ·                                         |                                         ·                                          |                                         ·                                          |  **12** |
| **III.** SID–Model Alignment    |                                            ·                                            | [![11](https://img.shields.io/badge/11-2171b5?style=for-the-badge)](#iii--tokenization) | [![9](https://img.shields.io/badge/9-2171b5?style=for-the-badge)](#iii--backbone) | [![9](https://img.shields.io/badge/9-2171b5?style=for-the-badge)](#iii--training)  | [![2](https://img.shields.io/badge/2-c6dbef?style=for-the-badge)](#iii--inference) |  **31** |
| **IV.** Utility                 |                                            ·                                            |   [![1](https://img.shields.io/badge/1-c6dbef?style=for-the-badge)](#iv--tokenization)  |  [![3](https://img.shields.io/badge/3-c6dbef?style=for-the-badge)](#iv--backbone) | [![22](https://img.shields.io/badge/22-08306b?style=for-the-badge)](#iv--training) | [![2](https://img.shields.io/badge/2-c6dbef?style=for-the-badge)](#iv--inference)  |  **28** |
| **V.** Efficiency               |                                            ·                                            |   [![3](https://img.shields.io/badge/3-c6dbef?style=for-the-badge)](#v--tokenization)   | [![11](https://img.shields.io/badge/11-2171b5?style=for-the-badge)](#v--backbone) |  [![1](https://img.shields.io/badge/1-c6dbef?style=for-the-badge)](#v--training)   |  [![6](https://img.shields.io/badge/6-6baed6?style=for-the-badge)](#v--inference)  |  **21** |
| **VI.** Generalization          |                                            ·                                            |   [![9](https://img.shields.io/badge/9-2171b5?style=for-the-badge)](#vi--tokenization)  |  [![3](https://img.shields.io/badge/3-c6dbef?style=for-the-badge)](#vi--backbone) |  [![4](https://img.shields.io/badge/4-6baed6?style=for-the-badge)](#vi--training)  | [![2](https://img.shields.io/badge/2-c6dbef?style=for-the-badge)](#vi--inference)  |  **18** |
| **Total**                       |                                          **12**                                         |                                          **70**                                         |                                       **33**                                      |                                       **40**                                       |                                       **14**                                       | **169** |

Click a count to jump to its papers; darker means more papers, `·` means none yet. Another 12 papers on paradigms, systems and benchmarks are listed first. Every entry links to a generated page with its Table 1 specification, architecture diagram where one exists, and notes; [TIGER](pages/papers/tiger.md), [RPG](pages/papers/rpg.md) and [OneLoc](pages/papers/oneloc.md) carry annotated walkthroughs. One YAML record per paper lives in [`data/papers/`](data/papers/); [`llms.txt`](llms.txt) and [`llms-full.txt`](llms-full.txt) are the machine-readable views.

## Contents

- [Paradigms, Systems and Benchmarks](#paradigms-systems-and-benchmarks)
- [I. Informativeness](#i-informativeness)
- [II. Uniqueness and Validity](#ii-uniqueness-and-validity)
- [III. SID–Model Alignment](#iii-sidmodel-alignment)
- [IV. Utility](#iv-utility)
- [V. Efficiency](#v-efficiency)
- [VI. Generalization](#vi-generalization)

## Paradigms, Systems and Benchmarks

> Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources.

- [TIGER](https://arxiv.org/abs/2305.05065) - Recommender Systems with Generative Retrieval. Rajput et al., NeurIPS’23 · [Page](pages/papers/tiger.md). `Text` → `RQ-VAE` → `Enc-Dec` → `Fixed / NTP` → `Beam`.
- [FORGE](https://arxiv.org/abs/2509.20904) - Forming semantic identifiers for generative retrieval in industrial datasets. Fu et al., KDD’26 · [Page](pages/papers/forge.md) · [Code](https://github.com/selous123/al_sid). `Text+Img` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → `Dyn. Beam`.
- [GRID](https://arxiv.org/abs/2507.22224) - Generative Recommendation with Semantic IDs: A Practitioner's Handbook. Ju et al., CIKM’25 · [Page](pages/papers/grid.md). `Text` → `R-KM` → `Enc-Dec` → `Fixed / NTP` → `Beam`.
- [MiniOneRec](https://arxiv.org/abs/2510.24431) - An Open-Source Framework for Scaling Generative Recommendation. Kong et al., arXiv’25 · [Page](pages/papers/minionerec.md) · [Code](https://github.com/AkaliKong/MiniOneRec). `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP → RL` → `Beam`.
- [OneRec](https://arxiv.org/abs/2502.18965) - Unifying retrieve and rank with generative recommender and iterative preference alignment. Deng et al., arXiv’25 · [Page](pages/papers/onerec.md). `Text+CF` → `R-KM` → `Enc-Dec` → `Fixed / NTP → DPO` → `Sess. Beam`.
- [GR-Generalize](https://arxiv.org/abs/2603.19809) - How Well Does Generative Recommendation Generalize? Ding et al., arXiv’26 · [Page](pages/papers/gr-generalize.md). `Text+SID` → `RQ-VAE` → `Enc-Dec` → `Fixed† / NTP†` → `Hybrid`.
- [NEO](https://arxiv.org/abs/2603.17533) - A Unified Language Model for Large Scale Search, Recommendation, and Reasoning. De Nadai et al., arXiv’26 · [Page](pages/papers/neo.md). `Text / Audio` → `R-KM` → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam`.
- [Netflix-SID-Comparison](https://arxiv.org/abs/2610.15864) - Personalized LLM Recommendation with Semantic IDs: Autoregressive Beam Search vs. Multi-Token Prediction. Oh et al., NeurIPS’26 PALM Workshop · [Page](pages/papers/netflix-sid-comparison.md). `–` → `RQ-VAE` → `Dec-Only / Non-AR` → `Fixed / Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT` → `C-Beam / Scoring`.
- [OneMall](https://arxiv.org/abs/2601.21770) - One Architecture, More Scenarios -- End-to-End Generative Recommender Family at Kuaishou E-Commerce. Zhang et al., CIKM’26 · [Page](pages/papers/onemall.md). `Text+Img+CF` → `R-KM+FSQ` → `Enc-Dec` → `Fixed / (NTP + Ctr.) → RL` → `Beam`.
- [PLUM](https://arxiv.org/abs/2510.07784) - Adapting Pre-trained Language Models for Industrial-scale Generative Recommendations. He et al., WWW’26 · [Page](pages/papers/plum.md). `Text+Img+CF` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam`.
- [ReRankID](https://arxiv.org/abs/2610.22797) - Reasoning Reranking with Semantic IDs as the Sole Item Representation. Tang et al., arXiv’26 · [Page](pages/papers/rerankid.md). `Text` → `R-KM†` → `Dec-Only` → `Fixed / NTP → RL` → `CoT+Greedy`.
- [SIDScope](https://arxiv.org/abs/2608.18779) - A Diagnostic Resource for Semantic-ID Interfaces in Generative Recommendation. Ding et al., arXiv’26 · [Page](pages/papers/sidscope.md). `n/a` → `n/a` → `n/a` → `n/a / n/a` → `n/a`.

## I. Informativeness

> Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs?

### I × Representation

- [Molar](https://arxiv.org/abs/2412.18176) - Multimodal llms with collaborative filtering alignment for enhanced sequential recommendation. Luo et al., arXiv’24 · [Page](pages/papers/molar.md). **`Text+Img+CF`** → `n/a` → `Dec-Only` → `n/a / Discrim.` → `Scoring`.
- [OneLoc](https://arxiv.org/abs/2508.14646) - Geo-Aware Generative Recommender Systems for Local Life Service. Wei et al., arXiv’25 · `POI` · [Page](pages/papers/oneloc.md). **`Text+Img+Geo†`** → `R-KM` → `Enc-Dec` → `Fixed / NTP → DPO` → `Beam`.
- [Q-BERT4Rec](https://arxiv.org/abs/2512.02474) - Quantized Semantic-ID Representation Learning for Multimodal Recommendation. Huang and Gai, arXiv’25 · [Page](pages/papers/q-bert4rec.md). **`Text+Img+CF`** → `RQ-VAE` → `Encoder (Non-AR)` → `Fixed / Masked` → `Non-AR`.
- [UNGER](https://arxiv.org/abs/2502.06269) - Generative Recommendation with A Unified Code via Semantic and Collaborative Integration. Xiao et al., TOIS’25 · [Page](pages/papers/unger.md). **`Text+CF`** → `R-KM` → `Enc-Dec` → `Fixed / NTP + Ctr.` → `Beam`.
- [GeoGR](https://arxiv.org/abs/2602.10411) - Enabling Spatio-Temporal Aware Industrial-Scale Generative POI Recommendations. Wang et al., arXiv’26 · `POI` · [Page](pages/papers/geogr.md). **`Text+Geo+CF`** → `R-KM+EM` → `Dec-Only` → `Altern.† / Multi-task NTP` → `Beam`.
- [HF-SID](https://arxiv.org/abs/2608.30479) - High-Fidelity Semantic IDs for Generative Retrieval in Location-Based Services. Lin et al., arXiv’26 · `POI` · [Page](pages/papers/hf-sid.md). **`Text+Attr+Geo`** → `R-KM` → `Dec-Only` → `Fixed / NTP` → `C-Beam`.
- [LGRID](https://arxiv.org/abs/2607.27944) - Interpretable Representation via LLM-Driven Generative Disentanglement for Local-Life Service Recommendation. Zhang et al., arXiv’26 · `POI` · [Page](pages/papers/lgrid.md). **`Text+Geo`** → `DSRQ` → `Disc.` → `Fixed / Discrim.` → `Scoring`.
- [LGSID](https://arxiv.org/abs/2511.14221) - LLM-Aligned Geographic Item Tokenization for Local-Life Recommendation. Jiang et al., AAAI’26 · `POI` · [Page](pages/papers/lgsid.md). **`Text+Geo+CF`** → `Geo-Idx+RQ` → `Disc. / Enc-Dec` → `Fixed / Discrim. / NTP` → `Scoring / Beam†`.
- [ReSID](https://arxiv.org/abs/2602.02338) - Rethinking Generative Recommender Tokenizer: Recsys-Native Encoding and Semantic Quantization Beyond LLMs. Liang et al., arXiv’26 · [Page](pages/papers/resid.md). **`Attr+CF`** → `GAOQ` → `Enc-Dec` → `Fixed / NTP` → `Beam`.
- [SCRec](https://arxiv.org/abs/2609.13678) - Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation. Dan, RecSys’26 · [Page](pages/papers/screc.md). **`Text+CF`** → `RQ-VAE` → `Non-AR / Enc-Dec` → `Fixed / MTP + Ctr.` → `Scoring / Beam†`.
- [SPAR](https://arxiv.org/abs/2609.02062) - Enhancing Industrial-Scale Generative POI Recommendation via Real-World Spatial Perception. Wang et al., arXiv’26 · `POI` · [Page](pages/papers/spar.md). **`Text+Geo`** → `R-KM` → `Dec-Only` → `Fixed / Multi-task NTP` → `–`.
- [TriAlignGR](https://arxiv.org/abs/2605.05249) - Triangular Multitask Alignment with Multimodal Deep Interest Mining for Generative Recommendation. Zeng et al., arXiv’26 · [Page](pages/papers/trialigngr.md). **`Text+Img`** → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam`.

### I × Tokenization

- [CoST](https://arxiv.org/abs/2404.14774) - Contrastive quantization based semantic tokenization for generative recommendation. Zhu et al., RecSys’24 · [Page](pages/papers/cost.md). `Text` → **`C-RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam`.
- [LETTER](https://arxiv.org/abs/2405.07314) - Learnable item tokenization for generative recommendation. Wang et al., CIKM’24 · [Page](pages/papers/letter.md) · [Code](https://github.com/HonghuiBao2000/LETTER). `Text+CF` → **`Learn. RQ`** → `Enc-Dec` → `Fixed / NTP + Rank` → `C-Beam`.
- [LMIndexer](https://arxiv.org/abs/2310.07815) - Language Models As Semantic Indexers. Jin et al., ICML’24 · [Page](pages/papers/lmindexer.md). `Text` → **`Self-Sup. ID`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam`.
- [ActionPiece](https://arxiv.org/abs/2502.13581) - Contextually Tokenizing Action Sequences for Generative Recommendation. Hou et al., ICML’25 · [Page](pages/papers/actionpiece.md) · [Code](https://github.com/google-deepmind/action_piece). `Text` → **`OPQ`** → `Enc-Dec` → `Fixed / NTP` → `Ensemble`.
- [ADC-SID](https://arxiv.org/abs/2510.25622) - Taming the Long Tail: Denoising Collaborative Information for Robust Semantic ID Generation. Xu et al., arXiv’25 · [Page](pages/papers/adc-sid.md). `Text+Img+CF` → **`MoE-VQ`** → `Enc-Dec` → `Fixed† / NTP` → `–`.
- [DAS](https://arxiv.org/abs/2508.10584) - Dual-Aligned Semantic IDs Empowered Industrial Recommender System. Ye et al., CIKM’25 · [Page](pages/papers/das.md). `Text+CF` → **`Dual RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam`.
- [EAGER-LLM](https://arxiv.org/abs/2502.14735) - Enhancing Large Language Models as Recommenders through Exogenous Behavior-Semantic Integration. Hong et al., WWW’25 · [Page](pages/papers/eager-llm.md). `Text+CF` → **`Dual H-KM`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam`.
- [FlexCode](https://arxiv.org/abs/2511.20673) - Semantics Meet Signals: Dual Codebook Representationl Learning for Generative Recommendation. Hui et al., arXiv’25 · [Page](pages/papers/flexcode.md). `Text+CF` → **`Dual RQ-VAE`** → `–` → `Joint / NTP` → `–`.
- [GenSAR](https://arxiv.org/abs/2504.05730) - Unified Generative Search and Recommendation. Shi et al., RecSys’25 · [Page](pages/papers/gensar.md). `Text+CF` → **`Shared/Spec. RQ`** → `Enc-Dec` → `Fixed / Multi-task NTP` → `C-Beam`.
- [GNPR-SID](https://arxiv.org/abs/2506.01375) - Generative Next POI Recommendation with Semantic ID. Wang et al., KDD’25 · `POI` · [Page](pages/papers/gnpr-sid.md) · [Code](https://github.com/wds1996/GNPR-SID). `Attr+Geo+CF` → **`RQ-VAE`** → `Dec-Only` → `Fixed / NTP` → `–`.
- [GRAM](https://arxiv.org/abs/2506.01673) - Generative recommendation via semantic-aware multi-granular late fusion. Lee et al., ACL’25 · [Page](pages/papers/gram.md). `Text+CF` → **`H-KM`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam`.
- [KGTB](https://arxiv.org/abs/2509.12350) - Knowledge Graph Tokenization for Behavior-Aware Generative Next POI Recommendation. Sun et al., arXiv’25 · `POI` · [Page](pages/papers/kgtb.md). `Attr+Geo+CF` → **`KG-RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `–`.
- [MME-SID](https://arxiv.org/abs/2509.02017) - Empowering large language model for sequential recommendation via multimodal embeddings and semantic ids. Wang et al., CIKM’25 · [Page](pages/papers/mme-sid.md). `Text+Img+CF` → **`MM-RQ`** → `Dec-Only` → `Fixed / NTP` → `Scoring`.
- [MQL4GRec](https://arxiv.org/abs/2504.05314) - MULTIMODAL QUANTITATIVE LANGUAGE FOR GEN-ERATIVE RECOMMENDATION. Zhai et al., ICLR’25 · [Page](pages/papers/mql4grec.md). `Text+Img` → **`Dual RQ`** → `Enc-Dec` → `Fixed / Multi-task NTP` → `Beam`.
- [PSRQ](https://arxiv.org/abs/2508.20359) - Progressive Semantic Residual Quantization for Multimodal-Joint Interest Modeling in Music Recommendation. Wang et al., CIKM’25 · [Page](pages/papers/psrq.md). `Text+Img` → **`Prog. RQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring`.
- [QT-Mob](https://arxiv.org/abs/2506.11109) - Enhancing Large Language Models for Mobility Analytics with Semantic Location Tokenization. Chen et al., KDD’25 · `POI` · [Page](pages/papers/qt-mob.md). `Text+Geo` → **`RQ-VAE`** → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam`.
- [TokenRec](https://arxiv.org/abs/2406.10450) - Learning to tokenize id for llm-based generative recommendations. Qu et al., TKDE’25 · [Page](pages/papers/tokenrec.md). `CF` → **`Masked VQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring`.
- [CapsID](https://arxiv.org/abs/2605.05096) - Soft-Routed Variable-Length Semantic IDs for Generative Recommendation. Cheng et al., arXiv’26 · [Page](pages/papers/capsid.md). `Text+CF` → **`Soft-RQ`** → `Dec-Only` → `Fixed / NTP` → `C-Beam`.
- [ChronoID](https://arxiv.org/abs/2606.14260) - Infusing Explicit Temporal Signals into Semantic IDs for Generative Recommendation. Nian et al., arXiv’26 · [Page](pages/papers/chronoid.md). `Text+Time` → **`RQ-VAE / Par. VQ`** → `Dec-Only†` → `Fixed / NTP` → `Beam†`.
- [GrIS (RecDMoN / RQ-GAE)](https://arxiv.org/abs/2610.01533) - Graph-Informed Semantic IDs (RecDMoN / RQ-GAE) for Generative Recommendation. Medvedev et al., CIKM’26 · [Page](pages/papers/gris-recdmon-rq-gae.md). `Text+CF` → **`RecDMoN / RQ-VAE`** → `Enc-Dec` → `Fixed / –` → `–`.
- [MACRec](https://arxiv.org/abs/2511.15122) - Multi-aspect cross-modal quantization for generative recommendation. Zhang et al., AAAI’26 · [Page](pages/papers/macrec.md). `Text+Img` → **`Cross RQ`** → `Enc-Dec` → `Fixed / NTP + Ctr.` → `C-Beam`.
- [MMGRec](https://arxiv.org/abs/2404.16555) - Multimodal Generative Recommendation with Transformer Model. Liu et al., TOMM’26 · [Page](pages/papers/mmgrec.md). `Text+Img+CF` → **`Graph RQ-VAE`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam`.
- [MMQ](https://arxiv.org/abs/2508.15281) - Multimodal Mixture-of-Quantization Tokenization for Semantic ID Generation and User Behavioral Adaptation. Xu et al., WSDM’26 · [Page](pages/papers/mmq.md). `Text+Img` → **`MoE-VQ`** → `HeterRec` → `Joint / MTP` → `–`.
- [MSCGRec](https://arxiv.org/abs/2602.03713) - Multimodal Generative Recommendation for Fusing Semantic and Collaborative Signals. Vandenhirtz et al., arXiv’26 · [Page](pages/papers/mscgrec.md). `Text+Img+CF` → **`RQ-VAE+DINO`** → `Enc-Dec` → `Fixed† / NTP` → `Trie/C-Beam`.
- [PCR-CA](https://arxiv.org/abs/2508.18166) - Parallel Codebook Representations with Contrastive Alignment for Multiple-Category App Recommendation. Tan et al., KDD’26 · [Page](pages/papers/pcr-ca.md). `Text+CF` → **`PC-AE`** → `Disc.` → `Joint / Discrim.` → `Scoring`.
- [Pctx](https://arxiv.org/abs/2510.21276) - Tokenizing Personalized Context for Generative Recommendation. Zhong et al., CIKM’26 · [Page](pages/papers/pctx.md). `Text+CF` → **`RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam+Agg.`.
- [ProGEO](https://arxiv.org/abs/2604.23156) - Birds of a Feather Cluster Nearby: A Proximity-Aware Geo-Codebook for Local Service Recommendation. He et al., arXiv’26 · `POI` · [Page](pages/papers/progeo.md). `Text+Geo` → **`R-KM+Geo-CB`** → `Dec-Only` → `Fixed / NTP` → `Beam+Geo-Filter`.
- [RoFiGR](https://arxiv.org/abs/2610.39470) - Coarse Routing, Fine Refinement via Level-Adaptive Distillation in Multimodal Generative Recommendation. Dai et al., arXiv’26 · [Page](pages/papers/rofigr.md). `Text+Img+CF` → **`CF-Aligned MM RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `C-Beam`.
- [ROS](https://arxiv.org/abs/2601.04562) - Reasoning Over Space: Enabling Geographic Reasoning for LLM-Based Generative Next POI Recommendation. Lv et al., ACL’26 · `POI` · [Page](pages/papers/ros.md). `Text+Geo` → **`Geo-Prefix+RQ-VAE`** → `Dec-Only` → `Fixed / NTP → RL` → `CoT+C-Beam`.
- [SPRIG](https://arxiv.org/abs/2610.06590) - Semantic-ID-enhanced Paths for Knowledge Graph-based Generative Recommendation. Hangoebl et al., CIKM’26 Short · [Page](pages/papers/sprig.md). `Text / Audio` → **`R-KM`** → `Dec-Only` → `Fixed / NTP` → `Div. Beam`.
- [Tlow](https://arxiv.org/abs/2608.24176) - Flow-based Item Tokenizer for Recommendation. Li et al., CIKM’26 Applied · [Page](pages/papers/tlow.md). `Text` → **`Flow+PQ`** → `Non-AR` → `Fixed / MTP + Rel.MSE` → `Scoring`.
- [UniRec](https://arxiv.org/abs/2604.12234) - Bridging the Expressive Gap between Generative and Discriminative Recommendation via Chain-of-Attribute. Wang et al., arXiv’26 · [Page](pages/papers/unirec.md). `Text+CF` → **`RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `C-Beam`.
- [UniSID](https://arxiv.org/abs/2602.10445) - End-to-End Semantic ID Generation for Generative Advertisement Recommendation. Jiang et al., arXiv’26 · [Page](pages/papers/unisid.md). `Text+Img+Attr` → **`Direct SID Heads`** → `–` → `– / –` → `–`.
- [VarLenRec (TIGER)](https://arxiv.org/abs/2605.17779) - Learning Variable-Length Tokenization for Generative Recommendation. Wang et al., arXiv’26 · [Page](pages/papers/varlenrec-tiger.md). `Text` → **`HARQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `C-Beam`.

### I × Backbone

- [ColaRec](https://arxiv.org/abs/2403.18480) - Content-based collaborative generation for recommender systems. Wang et al., CIKM’24 · [Page](pages/papers/colarec.md). `Text+CF` → `H-KM` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `C-Beam`.
- [EAGER](https://arxiv.org/abs/2406.14017) - Two-Stream Generative Recommender with Behavior-Semantic Collaboration. Wang et al., KDD’24 · [Page](pages/papers/eager.md) · [Code](https://github.com/yewzz/EAGER). `Text+CF` → `Dual H-KM` → **`Dual Enc-Dec`** → `Fixed / NTP + Ctr.` → `Fusion`.
- [COBRA](https://arxiv.org/abs/2503.02453) - Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations. Yang et al., NeurIPS’25 · [Page](pages/papers/cobra.md). `Text+SID` → `Casc. RQ` → **`Dec-Only`** → `Fixed / NTP + Dense` → `BeamFusion`.
- [DiscRec](https://arxiv.org/abs/2506.15576) - Disentangled Semantic-Collaborative Modeling for Generative Recommendation. Liu et al., arXiv’25 · [Page](pages/papers/discrec.md). `Text+CF` → `RQ-VAE / Learn. RQ` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam`.
- [Spacetime-GR](https://arxiv.org/abs/2508.16126) - A Spacetime-Aware Generative Model for Large Scale Online POI Recommendation. Lin et al., arXiv’25 · `POI` · [Page](pages/papers/spacetime-gr.md). `Geo` → `Geo-Idx` → **`Dec-Only`** → `Fixed / NTP → DPO` → `Beam`.
- [SPAR-Youku](https://arxiv.org/abs/2610.27898) - SPAR: Stepwise Personalized Autoregressive Recommendation with Prefix-Balanced Semantic IDs. Zhang et al., arXiv’26 · [Page](pages/papers/spar-youku.md). `–` → `RQ-PIB` → **`Dec-Only`** → `Fixed / NTP → DPO` → `C-Beam`.
- [UniSGR-V2](https://arxiv.org/abs/2610.16132) - Stepwise Target-Side Feature Anticipation and Crossing for Generative Recommendation. Yang et al., arXiv’26 · [Page](pages/papers/unisgr-v2.md). `–` → `–` → **`Enc-Dec`** → `– / NTP + Rank` → `Beam`.

### I × Training

- [MBGen](https://arxiv.org/abs/2405.16871) - Multi-Behavior Generative Recommendation. Liu et al., CIKM’24 · [Page](pages/papers/mbgen.md). `CF` → `Bal. VQ+KM` → `Enc-Dec` → **`Fixed / NTP`** → `Beam`.
- [RAGR](https://arxiv.org/abs/2605.17267) - Review-Augmented Generative Recommendation. Zhang et al., arXiv’26 · [Page](pages/papers/ragr.md). `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP → DPO`** → `Beam† / –`.
- [REGER](https://arxiv.org/abs/2610.37584) - Modeling inter-item Relations with Semantic IDs for Generative Recommendation. Huang et al., arXiv’26 · [Page](pages/papers/reger.md). `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP → (NTP + Aux.)`** → `Beam`.
- [SynGR](https://arxiv.org/abs/2605.18920) - Unleashing the Potential of Cross-Modal Synergy for Generative Recommendation. Chen et al., ICML’26 · [Page](pages/papers/syngr.md). `Text+Img` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP + Ctr.`** → `C-Beam`.

### I × Inference

- [CAPE](https://arxiv.org/abs/2610.29298) - Generative Recommenders Forget the Long Tail: Restoring Memorization in Retrieval and Ranking. Huang et al., arXiv’26 · [Page](pages/papers/cape.md). `Text†` → `RQ-VAE†` → `Dec-Only / Enc-Dec` → `Fixed / Multi-task NTP† / NTP†` → **`Hybrid`**.
- [CITE](https://doi.org/10.3390/electronics15204749) - Contextual Item Transition Embeddings for Generative Recommendation with Parallel Semantic Identifiers. Ma et al., Electronics’26 · [Page](pages/papers/cite.md). `Text` → `Par. OPQ` → `Non-AR` → `Fixed / Discrim.` → **`Scoring`**.

## II. Uniqueness and Validity

> Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly?

### II × Tokenization

- [CID](https://arxiv.org/abs/2305.06569) - How to Index Item IDs for Recommendation Foundation Models. Hua et al., SIGIR-AP’23 · [Page](pages/papers/cid.md). `CF` → **`Spectral Clus.`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam`.
- [TransRec](https://arxiv.org/abs/2310.06491) - Bridging Items and Language: A Transition Paradigm for Large Language Model-Based Recommendation. Lin et al., KDD’24 · [Page](pages/papers/transrec.md). `Text` → **`Multi-Facet ID`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `FM-Index+Agg.`.
- [HiD-VAE](https://arxiv.org/abs/2508.04618) - Interpretable Generative Recommendation via Hierarchical and Disentangled Semantic IDs. Fang et al., arXiv’25 · [Page](pages/papers/hid-vae.md). `Text` → **`Hier. RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam`.
- [PSI](https://arxiv.org/abs/2509.16446) - Purely Semantic Indexing for LLM-based Generative Recommendation and Retrieval. Zhang et al., arXiv’25 · [Page](pages/papers/psi.md). `Text` → **`Post-hoc RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam`.
- [AdaSID](https://arxiv.org/abs/2604.23522) - Beyond Static Collision Handling: Adaptive Semantic ID Learning for Multimodal Recommendation at Industrial Scale. Pan et al., arXiv’26 · [Page](pages/papers/adasid.md). `Text+Img` → **`RQ`** → `Dec-Only` → `Fixed / NTP` → `C-Beam`.
- [API](https://arxiv.org/abs/2610.36763) - The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features for Generative Recommendation. Luo et al., arXiv’26 · [Page](pages/papers/api.md). `Text` → **`PID (P-SAE)`** → `Enc-Dec / Dec-Only (AR); Non-AR (PR)` → `Fixed / NTP + Rank + Aux. / MTP + Rank + Aux.` → `C-Beam / Scoring`.
- [CARD](https://arxiv.org/abs/2604.26427) - Non-Uniform Quantization of Visual Semantic Unit for Generative Recommendation. Wei et al., arXiv’26 · [Page](pages/papers/card.md). `Text+Img+CF` → **`NU-RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam`.
- [DIGER](https://arxiv.org/abs/2601.19711) - Differentiable Semantic ID for Generative Recommendation. Fu et al., SIGIR’26 · [Page](pages/papers/diger.md). `Text` → **`Learn. RQ`** → `Enc-Dec` → `Joint / NTP` → `Beam†`.
- [Gwhere](https://arxiv.org/abs/2607.26073) - Guess Where You Go: Generative Next Point-of-Interest Recommendation in Amap. Zhai et al., RecSys’26 · `POI` · [Page](pages/papers/gwhere.md) · [Code](https://github.com/alibaba/SimCIT). `Text+Img+Geo+CF` → **`Contr. RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `–`.
- [QuaSID](https://arxiv.org/abs/2603.00632) - Stop Treating Collisions Equally: Qualification-Aware Semantic ID Learning for Recommendation at Industrial Scale. Hu et al., KDD’26 ADS · [Page](pages/papers/quasid.md). `Text+CF` → **`QA-RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam†`.
- [R3-VAE](https://arxiv.org/abs/2604.11440) - Reference Vector-Guided Rating Residual Quantization VAE for Generative Recommendation. Wan et al., arXiv’26 · [Page](pages/papers/r3-vae.md). `Text` → **`Ref.-RQ`** → `–` → `Fixed / NTP` → `Beam`.
- [SnapLGR](https://arxiv.org/abs/2607.28895) - LLM-Based Generative Retrieval for Snapchat Content Recommendation. Collins et al., arXiv’26 · [Page](pages/papers/snaplgr.md). `Text+Img+CF` → **`RQ-VAE+PPR`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam`.

## III. SID–Model Alignment

> Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal?

### III × Tokenization

- [IDGenRec](https://arxiv.org/abs/2403.19021) - Llm-recsys alignment with textual id learning. Tan et al., SIGIR’24 · [Page](pages/papers/idgenrec.md). `Text` → **`LLM-Vocab`** → `Enc-Dec` → `Altern. / NTP` → `C-Beam`.
- [SIIT](https://arxiv.org/abs/2412.17171) - Enhancing item tokenization for generative recommendation through self-improvement. Chen et al., arXiv’24 · [Page](pages/papers/siit.md). `Text` → **`Self-Imp.`** → `Enc-Dec` → `Altern. / Multi-task NTP` → `C-Beam`.
- [SemConv](https://arxiv.org/abs/2412.13771) - Semantic Convergence: Harmonizing Recommender Systems via Two-Stage Alignment and Behavioral Semantic Tokenization. Li et al., AAAI’25 · [Page](pages/papers/semconv.md). `Text+CF` → **`Align. RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam`.
- [Align3GR](https://arxiv.org/abs/2511.11255) - Align$^3$GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation. Ye et al., AAAI’26 · [Page](pages/papers/align3gr.md). `Text+CF` → **`Dual RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `Beam`.
- [CogRec](https://arxiv.org/abs/2607.24402) - Structure-Cognitive Fast-and-Slow Reasoning for Generative Recommendation. Liu et al., arXiv’26 · [Page](pages/papers/cogrec.md). `Text` → **`R-KM+Graph`** → `Dec-Only` → `Fixed / Multi-task NTP` → `CoT+C-Beam`.
- [DOS](https://arxiv.org/abs/2602.04460) - Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan. Yin et al., WWW’26 Short · `POI` · [Page](pages/papers/dos.md). `Text+CF` → **`Orth. RQ`** → `Dec-Only†` → `Fixed† / NTP` → `–`.
- [GR4AD-X](https://arxiv.org/abs/2610.38378) - Towards Reliable, Scalable, and Value-Aligned Generative Recommendation for Large-Scale Advertising. Xiao et al., arXiv’26 · [Page](pages/papers/gr4ad-x.md). `–` → **`Multi-Path R-KM+Hash`** → `Enc-Dec` → `Fixed / NTP + PV-RSPO + Rank + Aux.` → `PV-Beam+Rerank`.
- [GRLM](https://arxiv.org/abs/2601.06798) - Unleashing the Native Recommendation Potential: LLM-Based Generative Recommendation via Structured Term Identifiers. Zhang et al., arXiv’26 · [Page](pages/papers/grlm.md). `Text` → **`Term-ID`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam`.
- [HoloRec](https://arxiv.org/abs/2606.15331) - Holistic Encoding and Interleaved Reasoning for Generative Recommendation. Zhao et al., arXiv’26 · [Page](pages/papers/holorec.md). `–` → **`Nested RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `–`.
- [SST](https://arxiv.org/abs/2608.22734) - Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms to Semantic Subwords. Miao et al., CIKM’26 · [Page](pages/papers/sst.md). `Text` → **`RQ+IST`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam`.
- [TopoGR](https://arxiv.org/abs/2607.25216) - Revealing and Preserving Latent Structure of Semantic ID in Generative Recommendation. Zheng et al., arXiv’26 · [Page](pages/papers/topogr.md). `Text` → **`BDQ`** → `Non-AR` → `Fixed / MTP + Aux.` → `Scoring+Rerank`.

### III × Backbone

- [LLaDA-Rec](https://arxiv.org/abs/2511.06254) - Discrete Diffusion for Parallel Semantic ID Generation in Generative Recommendation. Shi et al., arXiv’25 · [Page](pages/papers/llada-rec.md). `Text` → `Par. VQ` → **`Non-AR`** → `Fixed / Masked` → `Diff.`.
- [DECOR](https://arxiv.org/abs/2509.10468) - Learning Decomposed Contextual Token Representations from Pretrained and Collaborative Signals for Generative Recommendation. Liu et al., SIGIR’26 · [Page](pages/papers/decor.md). `Text+CF` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP` → `Beam`.
- [FLASH](https://arxiv.org/abs/2610.07402) - Rethinking Semantic ID Construction for Generative Recommendation: SimHash with Parallel Decoding and Semantic Alignment. Liu et al., NeurIPS’26 · [Page](pages/papers/flash.md). `Text` → `SimHash` → **`Non-AR`** → `Fixed / MTP + Aux.` → `Scoring`.
- [Latte](https://arxiv.org/abs/2605.06331) - Expressiveness Limits of Autoregressive Semantic ID Generation in Generative Recommendation. Hou et al., arXiv’26 · [Page](pages/papers/latte.md). `Text+CF` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam`.
- [LESSRec](https://arxiv.org/abs/2610.37286) - Level-Specific History Modeling for Semantic ID-Based Recommendation. Yang et al., arXiv’26 · [Page](pages/papers/lessrec.md). `Text / Text+CF` → `RQ-VAE / R-KM / LETTER` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam`.
- [MDGR](https://arxiv.org/abs/2601.19501) - Masked Diffusion Generative Recommendation. Mu et al., arXiv’26 · [Page](pages/papers/mdgr.md). `–` → `Par. OPQ` → **`Non-AR`** → `Fixed / Masked` → `Diff.+Beam`.
- [PrefixMem](https://arxiv.org/abs/2606.00324) - LLMs Need Encoders for Semantic IDs Too. Chen et al., arXiv’26 · [Page](pages/papers/prefixmem.md). `MM` → `RQ-VAE` → **`Dec-Only`** → `Fixed / Multi-task NTP` → `Beam`.
- [S2GR](https://arxiv.org/abs/2601.18664) - Stepwise Semantic-Guided Reasoning in Latent Space for Generative Recommendation. Guo et al., KDD’26 · [Page](pages/papers/s2gr.md). `Text+CF` → `CoBa RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `Beam`.
- [TrieRec](https://arxiv.org/abs/2602.21677) - Trie-Aware Transformers for Generative Recommendation. Xu et al., NeurIPS’26 · [Page](pages/papers/trierec.md). `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed† / NTP†` → `C-Beam`.

### III × Training

- [LC-Rec](https://arxiv.org/abs/2311.09049) - Adapting large language models by integrating collaborative semantics for recommendation. Zheng et al., ICDE’24 · [Page](pages/papers/lc-rec.md). `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `Beam`.
- [ETEGRec](https://arxiv.org/abs/2409.05546) - Generative recommender with end-to-end learnable item tokenization. Liu et al., SIGIR’25 · [Page](pages/papers/etegrec.md). `CF` → `Learn. RQ` → `Enc-Dec` → **`Altern. / NTP + Ctr.`** → `Beam`.
- [GREAM](https://arxiv.org/abs/2510.20815) - Generative Reasoning Recommendation via LLMs. Hong et al., arXiv’25 · [Page](pages/papers/gream.md). `Text+CF` → `RQ-KM` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam`.
- [OneRec-Think](https://arxiv.org/abs/2510.11639) - In-text reasoning for generative recommendation. Liu et al., arXiv’25 · [Page](pages/papers/onerec-think.md). `Text+Img+CF†` → `R-KM†` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT`.
- [Evo-Rec](https://arxiv.org/abs/2609.29973) - Learning Better Reasoning for Generative Recommendation with Semantic IDs. Zhu et al., arXiv’26 · [Page](pages/papers/evo-rec.md). `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam`.
- [GTI](https://arxiv.org/abs/2604.02324) - Grounded Token Initialization for New Vocabulary in LMs for Generative Recommendation. Chen et al., arXiv’26 · [Page](pages/papers/gti.md). `Text+CF / Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `–`.
- [Intent-Driven-News](https://arxiv.org/abs/2605.07613) - Intent-Driven Semantic ID Generation for Grounded Conversational News Recommendation. Su et al., ACL’26 Industry · [Page](pages/papers/intent-driven-news.md). `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `CoT+Fuzzy Match`.
- [SIDReasoner](https://arxiv.org/abs/2603.23183) - Reasoning over Semantic IDs Enhances Generative Recommendation. He et al., KDD’26 · [Page](pages/papers/sidreasoner.md). `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam`.
- [Think2Go](https://arxiv.org/abs/2607.28997) - Generative Next POI Recommendation with LLM Reasoning. Zhuang et al., KDD’26 · `POI` · [Page](pages/papers/think2go.md). `Attr+Geo+CF†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+Beam`.

### III × Inference

- [GRC](https://arxiv.org/abs/2602.23639) - Learning to Reflect and Correct: Towards Better Decoding Trajectories for Large-Scale Generative Recommendation. Xing et al., CIKM’26 · [Page](pages/papers/grc.md). `–` → `RQ-VAE` → `Enc-Dec` → `Fixed / NTP → RL` → **`GRC+Beam`**.
- [PROMISE](https://arxiv.org/abs/2601.04674) - Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations. Guo et al., arXiv’26 · [Page](pages/papers/promise.md). `Text` → `RQ-VAE` → `Enc-Dec` → `Fixed† / NTP + Aux.` → **`PRM-Beam`**.

## IV. Utility

> Are training and search aimed at what users and the platform value, rather than at token likelihood?

### IV × Tokenization

- [TRACER](https://arxiv.org/abs/2606.07688) - Token ReAssignment for Concept ERasure in Generative Recommendation. Chen et al., NeurIPS’26 · [Page](pages/papers/tracer.md). `Text` → **`Soft Reassign. RQ`** → `Dec-Only / Enc-Dec` → `Joint / NTP + Aux.` → `Beam`.

### IV × Backbone

- [DiGR](https://arxiv.org/abs/2602.07847) - From Token Generation to Item Ranking: Direct Generative Recommendation with Semantic IDs. Zhao et al., arXiv’26 · [Page](pages/papers/digr.md). `–` → `RQ-VAE` → **`Dec-Only`** → `Fixed / Discrim.` → `Scoring`.
- [Gryphon](https://arxiv.org/abs/2606.08604) - A Unified Architecture for Semantic-ID Generation and Item-Level Scoring in Industrial Recommendations. Tikhonovich et al., CIKM’26 Short · [Page](pages/papers/gryphon.md). `–` → `R-KM` → **`Enc-Dec`** → `Fixed / NTP + Rank` → `Hybrid`.
- [RecoChain](https://arxiv.org/abs/2604.25787) - Harmonizing Generative Retrieval and Ranking in Chain-of-Recommendation. Liu and Cao, arXiv’26 · [Page](pages/papers/recochain.md). `Text+Img` → `RQ` → **`Dec-Only`** → `Fixed / NTP + Rank` → `Hybrid`.

### IV × Training

- [APAO](https://arxiv.org/abs/2603.02730) - Bridging the Training-Inference Gap in Generative Recommendation via Adaptive Prefix-Aware Optimization. Yu et al., KDD’26 · [Page](pages/papers/apao.md). `Text` → `R-KM` → `Enc-Dec / Dec-Only` → **`Fixed / NTP + Rank`** → `Beam`.
- [DASO](https://arxiv.org/abs/2608.20611) - Difficulty-Aware Semantic-ID Optimization for Generative Recommendation. Yu et al., arXiv’26 · [Page](pages/papers/daso.md). `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam`.
- [DPE-Rec](https://arxiv.org/abs/2610.34700) - Diversity-Preserving and Efficient Diffusion Language Model Recommendation for Bundle Construction. Ma et al., arXiv’26 · [Page](pages/papers/dpe-rec.md). `– / Text+Img` → `RQ` → `Non-AR` → **`Fixed / Masked → RL (→ Masked KD for Fast)`** → `Diff.+Legalize`.
- [GEM-Rec](https://arxiv.org/abs/2603.22231) - One Model, Two Markets: Bid-Aware Generative Recommendation. Jiang et al., arXiv’26 · [Page](pages/papers/gem-rec.md). `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `Bid-Aware Beam`.
- [GenRec-JD](https://arxiv.org/abs/2604.14878) - GenRec: A Preference-Oriented Generative Framework for Large-Scale Recommendation. Zou et al., SIGIR’26 · [Page](pages/papers/genrec-jd.md). `Text+Img+CF` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam`.
- [GFlowGR](https://arxiv.org/abs/2506.16114) - Fine-Tuning Generative Recommendation Frameworks with Generative Flow Networks. Wang et al., SIGIR’26 · [Page](pages/papers/gflowgr.md). `Text / Text+CF` → `RQ-VAE / Learn. RQ` → `Enc-Dec†` → **`Fixed / NTP + Aux.`** → `Beam† / C-Beam†`.
- [Ghost](https://arxiv.org/abs/2605.16825) - Echoes in Filter Bubble: Diagnosing and Curing Popularity Bias in Generative Recommenders. Yin et al., NeurIPS’26 · [Page](pages/papers/ghost.md). `Text` → `Skeleton R-KM` → `Dec-Only` → **`Fixed / NTP + Aux.`** → `–`.
- [HASTE](https://arxiv.org/abs/2610.17368) - Hierarchical and Attribute-aware Supervision for Generative Recommendation. Shukla et al., arXiv’26 · [Page](pages/papers/haste.md). `Text / MM` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP + Aux.`** → `–`.
- [HCGRec](https://arxiv.org/abs/2608.11980) - Learning from Unreachable Rewards: Hint-Conditioned Reinforcement Learning for Generative Recommendation. Zhang et al., CIKM’26 · [Page](pages/papers/hcgrec.md). `–` → `RQ` → `Dec-Only` → **`Fixed / NTP → RL`** → `Beam`.
- [IDM/CMM](https://arxiv.org/abs/2610.32943) - Knowledge Distillation across Item and Code Spaces for Parallel Generative Recommendation. Xu et al., arXiv’26 · [Page](pages/papers/idm-cmm.md). `Text` → `Subspace RQ` → `Non-AR` → **`Fixed / MTP + Aux.`** → `Scoring`.
- [KL-MOPD](https://arxiv.org/abs/2610.36973) - Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative Recommendation. Yang et al., arXiv’26 · [Page](pages/papers/kl-mopd.md). `CF` → `R-KM` → `Enc-Dec` → **`Fixed† / (NTP† / (NTP + Aux.)†) → KL-weighted OPD`** → `C-Beam`.
- [MuSID-KD](https://arxiv.org/abs/2610.35218) - Multigranularity Knowledge Distillation for Generative Recommendation with Semantic IDs. Zhang et al., arXiv’26 · [Page](pages/papers/musid-kd.md). `–` → `RQ-VAE` → `Enc-MLP` → **`Fixed / NTP + Aux.`** → `C-Beam`.
- [NAU](https://arxiv.org/abs/2610.27232) - Neighborhood-Aware Unlearning for Generative Recommendation. Lubitzsch et al., arXiv’26 · [Page](pages/papers/nau.md). `–` → `R-KM` → `Enc-Dec†` → **`Fixed / NTP + Aux.`** → `–`.
- [OneChord](https://arxiv.org/abs/2610.25805) - Distill What You Rank, Recommend in One Pass. Li et al., arXiv’26 · [Page](pages/papers/onechord.md). `–` → `Par. OPQ` → `Non-AR` → **`Fixed / Next-item CE + Cons. KD + Rank KD`** → `Scoring`.
- [Retrieval-Grounded-Credit](https://arxiv.org/abs/2609.29983) - From Interests to Semantic IDs: Retrieval-Grounded Credit Assignment for Generative Recommendation. Zhu et al., arXiv’26 · [Page](pages/papers/retrieval-grounded-credit.md). `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam`.
- [SAGE-SID](https://arxiv.org/abs/2601.21452) - SAGE: Sequence-level Adaptive Gradient Evolution for Generative Recommendation. Xie et al., arXiv’26 · [Page](pages/papers/sage-sid.md). `Text+Img†` → `R-KM†` → `Dec-Only†` → **`Fixed† / NTP → RL`** → `–`.
- [SAHL](https://arxiv.org/abs/2610.25093) - Structure-Aligned History Learning with Subspace-Structured Semantic IDs for Generative Recommendation. Wei et al., arXiv’26 · [Page](pages/papers/sahl.md). `Text` → `SRBQ` → `Non-AR` → **`Fixed / (MTP + Masked Rec.) → MTP`** → `Graph`.
- [SAPO](https://arxiv.org/abs/2605.17648) - Step-Aligned Policy Optimization for Reasoning-Based Generative Recommendation. Zheng et al., arXiv’26 · [Page](pages/papers/sapo.md). `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `CoT+C-Beam`.
- [SLIDE](https://arxiv.org/abs/2610.34764) - Search-to-List Item Distillation for Single-Rollout Generative Retrieval. Zhan et al., arXiv’26 · [Page](pages/papers/slide.md). `–` → `–` → `Dec-Only` → **`Fixed / NTP`** → `Greedy`.
- [Token-Weighted](https://arxiv.org/abs/2601.17787) - Beyond Uniform Token Training: A Multi-Target Framework for Learning Token-Weighted Objectives in Generative Recommenders. Chiu et al., CIKM’26 · [Page](pages/papers/token-weighted.md). `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP`** → `C-Beam`.
- [UGR](https://arxiv.org/abs/2602.11719) - Uncertainty-aware Generative Recommendation. Fan et al., KDD’26 · [Page](pages/papers/ugr.md). `Text` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → (RL + Rank)`** → `Beam`.
- [V-STAR](https://arxiv.org/abs/2602.10699) - Spend Search Where It Pays: Value-Guided Structured Sampling and Optimization for Generative Recommendation. Jiang et al., KDD’26 · [Page](pages/papers/v-star.md). `Text†` → `RQ-VAE` → `Dec-Only` → **`Fixed / NTP → RL`** → `C-Beam`.

### IV × Inference

- [ISD](https://arxiv.org/abs/2607.24995) - Understanding Semantic IDs: From Item Representation to Item Selection in Generative Recommendation. Wang et al., arXiv’26 · [Page](pages/papers/isd.md). `Text†` → `RQ-VAE†` → `Enc-Dec†` → `Fixed / NTP†` → **`ISD Beam`**.
- [TCBSA](https://arxiv.org/abs/2610.32098) - From Item Scores to Semantic Tokens: Test-Time Collaborative Adaptation for Generative Recommendation. Shan et al., arXiv’26 · [Page](pages/papers/tcbsa.md). `Text` → `R-KM` → `Enc-Dec† / Dec-Only†` → `Fixed / NTP† / NTP → RL` → **`CF-Guided C-Beam`**.

## V. Efficiency

> Can it be trained and served within latency and cost budgets?

### V × Tokenization

- [SEATER](https://arxiv.org/abs/2309.13375) - Generative retrieval with semantic tree-structured identifiers and contrastive learning. Si et al., SIGIR-AP’24 · [Page](pages/papers/seater.md). `CF` → **`Tree-Clus.`** → `Enc-Dec` → `Fixed / NTP + Ctr.` → `C-Beam`.
- [Dynamic-Single-Codebook](https://arxiv.org/abs/2608.21012) - From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level Large Semantic Codebook for Generative Recommendation. Xie et al., arXiv’26 · [Page](pages/papers/dynamic-single-codebook.md). `–` → **`Dyn. KM+Disamb.`** → `Enc-Dec / Lazy Dec-Only` → `Fixed / NTP†` → `Beam†`.
- [JevRec](https://arxiv.org/abs/2610.36937) - Linguistic Encoding with Jev-like Decision Modeling for LLM-based Generative Recommendation. Zhong et al., arXiv’26 · [Page](pages/papers/jevrec.md). `Text` → **`Freq. R-KM`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `Length-Quota Beam`.

### V × Backbone

- [OneRec-V2](https://arxiv.org/abs/2508.20900) - Technical Report. Zhou et al., arXiv’25 · [Page](pages/papers/onerec-v2.md). `Text+Img+CF†` → `R-KM†` → **`Lazy Dec-Only`** → `Fixed / NTP → RL` → `Beam`.
- [RPG](https://arxiv.org/abs/2506.05781) - Generating long semantic ids in parallel for recommendation. Hou et al., KDD’25 · [Page](pages/papers/rpg.md). `Text+Img` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP` → `Graph`.
- [ACERec](https://arxiv.org/abs/2602.13573) - Unleash the Potential of Long Semantic IDs for Generative Recommendation. Xia et al., arXiv’26 · [Page](pages/papers/acerec.md). `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP + Ctr. + Aux.` → `Scoring`.
- [Deco](https://arxiv.org/abs/2610.32980) - Separating Thinking from Spelling for Efficient Generative Recommendation. Gusak et al., arXiv’26 · [Page](pages/papers/deco.md). `Text / –` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam`.
- [IBA](https://arxiv.org/abs/2607.12425) - Where Reasoning Matters: Rethinking Latent Reasoning in Semantic ID-based Generative Recommendation. Yang et al., arXiv’26 · [Page](pages/papers/iba.md). `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP → (NTP + Aux.)` → `C-Beam`.
- [LoopGR](https://arxiv.org/abs/2610.34157) - Parameter-Efficient Scaling for Generative Recommendation via Recurrent Depth. Zhang et al., arXiv’26 · [Page](pages/papers/loopgr.md). `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP / NTP + Aux.` → `–`.
- [Merge-and-Branch](https://arxiv.org/abs/2610.37973) - Merge and Branch: Efficient Tree-Structured Supervised Fine-Tuning of LLMs for Recommendation. Zhu et al., arXiv’26 · [Page](pages/papers/merge-and-branch.md). `Text` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam`.
- [PinGER](https://arxiv.org/abs/2610.33435) - Token-Efficient Generative Retrieval with Semantic IDs. Li et al., arXiv’26 · [Page](pages/papers/pinger.md). `Text+Img+CF` → `RQ-VAE` → **`Dec-Only`** → `– / NTP → DPO` → `Div. C-Beam`.
- [SID-MLP](https://arxiv.org/abs/2605.12617) - MLPs are Efficient Distilled Generative Recommenders. Guo et al., arXiv’26 · [Page](pages/papers/sid-mlp.md). `Text` → `RQ-VAE†` → **`Enc-MLP`** → `Fixed / NTP + Aux.` → `C-Beam`.
- [SPRINT](https://arxiv.org/abs/2609.34306) - Single-Step Generative Recommendation via Average Probability Velocity. Cai et al., arXiv’26 · [Page](pages/papers/sprint.md). `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring`.
- [STAMP](https://arxiv.org/abs/2604.05329) - Semantic Trimming and Auxiliary Multi-step Prediction for Generative Recommendation. Zhan et al., arXiv’26 · [Page](pages/papers/stamp.md). `Text` → `RQ-VAE` → **`Enc-Dec / Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam`.

### V × Training

- [OneLatent](https://arxiv.org/abs/2610.30675) - Latent Reasoning for Efficient Foundation Recommendation Models. Jiang et al., arXiv’26 · [Page](pages/papers/onelatent.md). `MM` → `R-KM` → `Dec-Only` → **`Fixed / Multi-task NTP`** → `Beam`.

### V × Inference

- [AtSpeed](https://arxiv.org/abs/2410.05165) - Efficient Inference for Large Language Model-based Generative Recommendation. Lin et al., ICLR’25 · [Page](pages/papers/atspeed.md). `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Spec. Dec.`**.
- [NEZHA](https://arxiv.org/abs/2511.18793) - A Zero-sacrifice and Hyperspeed Decoding Architecture for Generative Recommendations. Wang et al., WWW’26 Industry · [Page](pages/papers/nezha.md). `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Self-Draft+Hash`**.
- [OneRec-V2-Quantized](https://arxiv.org/abs/2603.11486) - Quantized Inference for OneRec-V2. Su et al., arXiv’26 · [Page](pages/papers/onerec-v2-quantized.md). `Text+Img+CF†` → `R-KM†` → `Lazy Dec-Only†` → `Fixed† / NTP → RL†` → **`FP8+RecoGEM`**.
- [PAD-Rec](https://arxiv.org/abs/2604.27747) - Position-Aware Drafting for Inference Acceleration in LLM-Based Generative List-Wise Recommendation. Chen et al., arXiv’26 · [Page](pages/papers/pad-rec.md). `Text+SID` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP†` → **`Spec. Dec.`**.
- [PFA](https://arxiv.org/abs/2610.39273) - Attention Can Be Progressively Focused in Long-Sequence Generative Recommendation. Zhou et al., arXiv’26 · [Page](pages/papers/pfa.md). `–` → `–` → `Enc-Dec` → `– / –` → **`Beam`**.
- [STATIC](https://arxiv.org/abs/2602.22647) - Vectorizing the Trie: Efficient Constrained Decoding for LLM-based Generative Retrieval on Accelerators. Su et al., KDD’26 ADS · [Page](pages/papers/static.md). `–` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Vec. C-Beam`**.

## VI. Generalization

> Does it still work for new items, new domains, and shifting interests?

### VI × Tokenization

- [VQ-Rec](https://arxiv.org/abs/2210.12316) - Learning Vector-Quantized Item Representation for Transferable Sequential Recommenders. Hou et al., WWW’23 · [Page](pages/papers/vq-rec.md). `Multi-Dom` → **`OPQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring`.
- [GMC](https://arxiv.org/abs/2507.12871) - Generative Multi-Target Cross-Domain Recommendation. Jin et al., arXiv’25 · [Page](pages/papers/gmc.md). `Cross-Dom` → **`Unified RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam`.
- [UTGRec](https://arxiv.org/abs/2504.04405) - Universal Item Tokenization for Transferable Generative Recommendation. Zheng et al., arXiv’25 · [Page](pages/papers/utgrec.md). `Multi-Dom` → **`Tree`** → `Enc-Dec` → `Fixed / NTP` → `Beam`.
- [DACT](https://arxiv.org/abs/2603.29705) - Drift-Aware Continual Tokenization for Generative Recommendation. Feng et al., SIGIR’26 · [Page](pages/papers/dact.md). `Text+CF` → **`RQ-VAE`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `–`.
- [DREAM](https://arxiv.org/abs/2606.06947) - Dynamic Refinement of Early Assignment Mappings. Guan et al., arXiv’26 · [Page](pages/papers/dream.md). `Text+CF` → **`CART`** → `Dec-Only` → `Altern. / NTP + Aux.` → `C-Beam`.
- [GenCDR](https://arxiv.org/abs/2511.08006) - From ids to semantics: A generative framework for cross-domain recommendation with adaptive semantic tokenization. Hu et al., AAAI’26 · [Page](pages/papers/gencdr.md). `Cross-Dom` → **`RQ+LoRA`** → `Dec-Only` → `Fixed / NTP` → `C-Beam`.
- [MBGR](https://arxiv.org/abs/2604.02684) - Multi-Business Prediction for Generative Recommendation at Meituan. Li et al., arXiv’26 · [Page](pages/papers/mbgr.md). `Text+CF` → **`RQ`** → `Dec-Only` → `Fixed† / NTP + Aux.` → `C-Beam`.
- [OneLive](https://arxiv.org/abs/2602.08612) - Dynamically Unified Generative Framework for Live-Streaming Recommendation. Wang et al., KDD’26 ADS · [Page](pages/papers/onelive.md). `Text+Img+Audio+CF` → **`R-KM`** → `Lazy Dec-Only` → `Fixed / NTP → RL` → `Beam`.
- [UniTok](https://arxiv.org/abs/2511.12922) - Tokenize Once, Recommend Anywhere: Unified Item Tokenization for Multi-domain LLM-based Recommendation. Hou and Shin, AAAI’26 · [Page](pages/papers/unitok.md). `Multi-Dom` → **`TokenMoE`** → `Enc-Dec` → `Fixed / NTP` → `Beam†`.

### VI × Backbone

- [DualGR](https://arxiv.org/abs/2511.12518) - Generative Retrieval with Long and Short-Term Interests Modeling. Yi et al., WWW’26 Short · [Page](pages/papers/dualgr.md). `–` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Rank` → `Dual Beam`.
- [FedCGR](https://arxiv.org/abs/2608.10929) - Federated Cross-Domain Generative Recommendation. Liu et al., CIKM’26 · [Page](pages/papers/fedcgr.md). `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP + Aux.` → `C-Beam`.
- [LION](https://arxiv.org/abs/2609.15598) - Self-Evolving Memory for Generative Recommendation. Lin et al., CIKM’26 · [Page](pages/papers/lion.md). `Text†` → `RQ-VAE†` → **`Enc-Dec`** → `Fixed† / NTP + Aux.` → `Beam`.

### VI × Training

- [RecBase](https://arxiv.org/abs/2509.03131) - Generative foundation model pretraining for zero-shot recommendation. Zhou et al., EMNLP’25 · [Page](pages/papers/recbase.md). `Text` → `Curr. RQ` → `Dec-Only` → **`Fixed / NTP`** → `Beam`.
- [AWARE](https://arxiv.org/abs/2605.11807) - Why Users Go There: World Knowledge-Augmented Generative Next POI Recommendation. Ding et al., arXiv’26 · `POI` · [Page](pages/papers/aware.md). `Text+Geo` → `Geo-Prefix+HClus` → `Dec-Only` → **`Fixed / NTP`** → `–`.
- [CausalDPO](https://arxiv.org/abs/2603.22335) - Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation. Zhao et al., ICML’26 · [Page](pages/papers/causaldpo.md). `Text` → `LLM-Vocab` → `Dec-Only` → **`Fixed / NTP → DPO`** → `Scoring`.
- [CMRec](https://arxiv.org/abs/2609.28972) - Cross-Country Code-Mixing for Generative Recommendation. Gao et al., CIKM’26 Short · [Page](pages/papers/cmrec.md). `Text+Img+CF` → `RQ-VAE` → `Dec-Only†` → **`– / NTP`** → `–`.

### VI × Inference

- [LIGER](https://arxiv.org/abs/2411.18814) - Unifying generative and dense retrieval for sequential recommendation. Yang et al., arXiv’24 · [Page](pages/papers/liger.md). `Text+SID` → `RQ-VAE` → `Enc-Dec` → `Fixed / NTP + Dense` → **`Hybrid`**.
- [SpecGR](https://arxiv.org/abs/2410.02939) - Inductive Generative Recommendation via Retrieval-based Speculation. Ding et al., AAAI’26 · [Page](pages/papers/specgr.md). `Text+SID` → `RQ-VAE` → `Enc-Dec` → `Fixed / NTP + Rank` → **`Hybrid`**.

## Contributing

Add one YAML record and run `make build && make check`; see [`CONTRIBUTING.md`](CONTRIBUTING.md).
