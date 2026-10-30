# Awesome Semantic ID Generative Recommendation [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Discrete semantic tokenization and autoregressive or diffusion recommendation models indexed by failure mode, pipeline stage, and verifiable source anchors.

## Contents

- [Paradigms, Systems, and Benchmarks](#paradigms-systems-and-benchmarks)
- [Problem I: Collaborative Versus Semantic Misalignment](#problem-i-collaborative-versus-semantic-misalignment)
- [Problem II: Codebook Collapse and Prefix Collisions](#problem-ii-codebook-collapse-and-prefix-collisions)
- [Problem III: Distribution Shift and Dynamic Catalogs](#problem-iii-distribution-shift-and-dynamic-catalogs)
- [Problem IV: Tokenization-Generation Objective Gap](#problem-iv-tokenization-generation-objective-gap)
- [Problem V: Autoregressive Exposure Bias and Reward Sparse Signals](#problem-v-autoregressive-exposure-bias-and-reward-sparse-signals)
- [Problem VI: Constrained Decoding Latency and Beam Degeneration](#problem-vi-constrained-decoding-latency-and-beam-degeneration)

## Paradigms, Systems, and Benchmarks

- [TIGER](https://arxiv.org/abs/2305.05065) - Paradigm, system, or benchmark entry (NeurIPS’23) using `RQ-VAE` tokenization and `Enc-Dec` backbone with `NTP` objective.
- [GRID](https://arxiv.org/abs/2507.22224) - Paradigm, system, or benchmark entry (CIKM’25) using `R-KM` tokenization and `Enc-Dec` backbone with `NTP` objective.
- [MiniOneRec](https://arxiv.org/abs/2510.24431) - Paradigm, system, or benchmark entry (arXiv’25) using `RQ-VAE` tokenization and `Dec-Only` backbone with `NTP → RL` objective.
- [OneRec](https://arxiv.org/abs/2502.18965) - Paradigm, system, or benchmark entry (arXiv’25) using `R-KM` tokenization and `Enc-Dec` backbone with `NTP → DPO` objective.
- [FORGE](https://arxiv.org/abs/2509.20904) - Paradigm, system, or benchmark entry (KDD’26) using `RQ-VAE` tokenization and `Dec-Only` backbone with `NTP` objective.
- [GR-Generalize](https://arxiv.org/abs/2603.19809) - Paradigm, system, or benchmark entry (arXiv’26) using `RQ-VAE` tokenization and `Enc-Dec` backbone with `NTP` objective.
- [PLUM](https://arxiv.org/abs/2510.07784) - Paradigm, system, or benchmark entry (WWW’26) using `RQ-VAE` tokenization and `Dec-Only` backbone with `Multi-task NTP` objective.

## Problem I: Collaborative Versus Semantic Misalignment

- [ColaRec](https://arxiv.org/abs/2403.18480) - Addresses Problem I at the Backbone stage (CIKM’24) via `H-KM` tokenization, `Enc-Dec` backbone, and `NTP + Ctr.` objective.
- [CoST](https://arxiv.org/abs/2404.14774) - Addresses Problem I at the Tokenization stage (RecSys’24) via `C-RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [EAGER](https://arxiv.org/abs/2406.14017) - Addresses Problem I at the Backbone stage (KDD’24) via `Dual H-KM` tokenization, `Dual Enc-Dec` backbone, and `NTP + Ctr.` objective.
- [LETTER](https://arxiv.org/abs/2405.07314) - Addresses Problem I at the Tokenization stage (CIKM’24) via `Learn. RQ` tokenization, `Enc-Dec` backbone, and `NTP + Rank` objective.
- [LMIndexer](https://arxiv.org/abs/2310.07815) - Addresses Problem I at the Tokenization stage (ICML’24) via `Self-Sup. ID` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [MBGen](https://arxiv.org/abs/2405.16871) - Addresses Problem I at the Training stage (CIKM’24) via `Bal. VQ+KM` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [Molar](https://arxiv.org/abs/2412.18176) - Addresses Problem I at the Representation stage (arXiv’24) via `–` tokenization, `Dec-Only` backbone, and `Discrim.` objective.
- [ActionPiece](https://arxiv.org/abs/2502.13581) - Addresses Problem I at the Tokenization stage (ICML’25) via `OPQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [ADC-SID](https://arxiv.org/abs/2510.25622) - Addresses Problem I at the Tokenization stage (arXiv’25) via `MoE-VQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [COBRA](https://arxiv.org/abs/2503.02453) - Addresses Problem I at the Backbone stage (NeurIPS’25) via `Casc. RQ` tokenization, `Dec-Only` backbone, and `NTP + Dense` objective.
- [DAS](https://arxiv.org/abs/2508.10584) - Addresses Problem I at the Tokenization stage (CIKM’25) via `Dual RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [DiscRec](https://arxiv.org/abs/2506.15576) - Addresses Problem I at the Backbone stage (arXiv’25) via `RQ-VAE / Learn. RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [EAGER-LLM](https://arxiv.org/abs/2502.14735) - Addresses Problem I at the Tokenization stage (WWW’25) via `Dual H-KM` tokenization, `Dec-Only` backbone, and `Multi-task NTP` objective.
- [GenSAR](https://arxiv.org/abs/2504.05730) - Addresses Problem I at the Tokenization stage (RecSys’25) via `Shared/Spec. RQ` tokenization, `Enc-Dec` backbone, and `Multi-task NTP` objective.
- [GNPR-SID](https://arxiv.org/abs/2506.01375) - Addresses Problem I at the Tokenization stage (KDD’25) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [GRAM](https://arxiv.org/abs/2506.01673) - Addresses Problem I at the Tokenization stage (ACL’25) via `H-KM` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [MME-SID](https://arxiv.org/abs/2509.02017) - Addresses Problem I at the Tokenization stage (CIKM’25) via `MM-RQ` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [MQL4GRec](https://arxiv.org/abs/2504.05314) - Addresses Problem I at the Tokenization stage (ICLR’25) via `Dual RQ` tokenization, `Enc-Dec` backbone, and `Multi-task NTP` objective.
- [OneLoc](https://arxiv.org/abs/2508.14646) - Addresses Problem I at the Representation stage (arXiv’25) via `R-KM` tokenization, `Enc-Dec` backbone, and `NTP → DPO` objective.
- [PSRQ](https://arxiv.org/abs/2508.20359) - Addresses Problem I at the Tokenization stage (CIKM’25) via `Prog. RQ` tokenization, `Encoder` backbone, and `Discrim.` objective.
- [Q-BERT4Rec](https://arxiv.org/abs/2512.02474) - Addresses Problem I at the Representation stage (arXiv’25) via `RQ-VAE` tokenization, `Encoder (Non-AR)` backbone, and `Masked` objective.
- [TokenRec](https://arxiv.org/abs/2406.10450) - Addresses Problem I at the Tokenization stage (TKDE’25) via `Masked VQ` tokenization, `Encoder` backbone, and `Discrim.` objective.
- [CapsID](https://arxiv.org/abs/2605.05096) - Addresses Problem I at the Tokenization stage (arXiv’26) via `Soft-RQ` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [GeoGR](https://arxiv.org/abs/2602.10411) - Addresses Problem I at the Representation stage (arXiv’26) via `R-KM+EM` tokenization, `Dec-Only` backbone, and `Multi-task NTP` objective.
- [LGRID](https://arxiv.org/abs/2607.27944) - Addresses Problem I at the Representation stage (arXiv’26) via `DSRQ` tokenization, `Disc.` backbone, and `Discrim.` objective.
- [LGSID](https://arxiv.org/abs/2511.14221) - Addresses Problem I at the Representation stage (AAAI’26) via `Geo-Idx+RQ` tokenization, `Disc. / Enc-Dec` backbone, and `Discrim. / NTP` objective.
- [MACRec](https://arxiv.org/abs/2511.15122) - Addresses Problem I at the Tokenization stage (AAAI’26) via `Cross RQ` tokenization, `Enc-Dec` backbone, and `NTP + Ctr.` objective.
- [MMGRec](https://arxiv.org/abs/2404.16555) - Addresses Problem I at the Tokenization stage (TOMM’26) via `Graph RQ-VAE` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [MMQ](https://arxiv.org/abs/2508.15281) - Addresses Problem I at the Tokenization stage (WSDM’26) via `MoE-VQ` tokenization, `HeterRec` backbone, and `MTP` objective.
- [MSCGRec](https://arxiv.org/abs/2602.03713) - Addresses Problem I at the Tokenization stage (arXiv’26) via `RQ-VAE+DINO` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [ProGEO](https://arxiv.org/abs/2604.23156) - Addresses Problem I at the Tokenization stage (arXiv’26) via `R-KM+Geo-CB` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [ROS](https://arxiv.org/abs/2601.04562) - Addresses Problem I at the Tokenization stage (ACL’26) via `Geo-Prefix+RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP → RL` objective.
- [SCRec](https://arxiv.org/abs/2609.13678) - Addresses Problem I at the Representation stage (RecSys’26) via `RQ-VAE` tokenization, `Non-AR / Enc-Dec` backbone, and `MTP + Ctr.` objective.
- [SynGR](https://arxiv.org/abs/2605.18920) - Addresses Problem I at the Training stage (ICML’26) via `RQ-VAE` tokenization, `Enc-Dec` backbone, and `NTP + Ctr.` objective.
- [TriAlignGR](https://arxiv.org/abs/2605.05249) - Addresses Problem I at the Representation stage (arXiv’26) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `Multi-task NTP` objective.
- [UniRec](https://arxiv.org/abs/2604.12234) - Addresses Problem I at the Tokenization stage (arXiv’26) via `RQ` tokenization, `Dec-Only` backbone, and `NTP → DPO` objective.

## Problem II: Codebook Collapse and Prefix Collisions

- [CID](https://arxiv.org/abs/2305.06569) - Addresses Problem II at the Tokenization stage (SIGIR-AP’23) via `Spectral Clus.` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [TransRec](https://arxiv.org/abs/2310.06491) - Addresses Problem II at the Tokenization stage (KDD’24) via `Multi-Facet ID` tokenization, `Enc-Dec / Dec-Only` backbone, and `NTP` objective.
- [HiD-VAE](https://arxiv.org/abs/2508.04618) - Addresses Problem II at the Tokenization stage (arXiv’25) via `Hier. RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [PSI](https://arxiv.org/abs/2509.16446) - Addresses Problem II at the Tokenization stage (arXiv’25) via `Post-hoc RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [AdaSID](https://arxiv.org/abs/2604.23522) - Addresses Problem II at the Tokenization stage (arXiv’26) via `RQ` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [CARD](https://arxiv.org/abs/2604.26427) - Addresses Problem II at the Tokenization stage (arXiv’26) via `NU-RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [DIGER](https://arxiv.org/abs/2601.19711) - Addresses Problem II at the Tokenization stage (SIGIR’26) via `Learn. RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [Gwhere](https://arxiv.org/abs/2607.26073) - Addresses Problem II at the Tokenization stage (RecSys’26) via `Contr. RQ` tokenization, `Dec-Only` backbone, and `NTP → DPO` objective.
- [QuaSID](https://arxiv.org/abs/2603.00632) - Addresses Problem II at the Tokenization stage (KDD’26 ADS) via `QA-RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [R3-VAE](https://arxiv.org/abs/2604.11440) - Addresses Problem II at the Tokenization stage (arXiv’26) via `Ref.-RQ` tokenization, `–` backbone, and `NTP` objective.

## Problem III: Distribution Shift and Dynamic Catalogs

- [IDGenRec](https://arxiv.org/abs/2403.19021) - Addresses Problem III at the Tokenization stage (SIGIR’24) via `LLM-Vocab` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [LC-Rec](https://arxiv.org/abs/2311.09049) - Addresses Problem III at the Training stage (ICDE’24) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `Multi-task NTP` objective.
- [SIIT](https://arxiv.org/abs/2412.17171) - Addresses Problem III at the Tokenization stage (arXiv’24) via `Self-Imp.` tokenization, `Enc-Dec` backbone, and `Multi-task NTP` objective.
- [ETEGRec](https://arxiv.org/abs/2409.05546) - Addresses Problem III at the Training stage (SIGIR’25) via `Learn. RQ` tokenization, `Enc-Dec` backbone, and `NTP + Ctr.` objective.
- [GREAM](https://arxiv.org/abs/2510.20815) - Addresses Problem III at the Training stage (arXiv’25) via `RQ-KM` tokenization, `Dec-Only` backbone, and `NTP → RL` objective.
- [LLaDA-Rec](https://arxiv.org/abs/2511.06254) - Addresses Problem III at the Backbone stage (arXiv’25) via `Par. VQ` tokenization, `Non-AR` backbone, and `Masked` objective.
- [OneRec-Think](https://arxiv.org/abs/2510.11639) - Addresses Problem III at the Training stage (arXiv’25) via `R-KM` tokenization, `Dec-Only` backbone, and `NTP → RL` objective.
- [SemConv](https://arxiv.org/abs/2412.13771) - Addresses Problem III at the Tokenization stage (AAAI’25) via `Align. RQ` tokenization, `Dec-Only` backbone, and `Multi-task NTP` objective.
- [Align3GR](https://arxiv.org/abs/2511.11255) - Addresses Problem III at the Tokenization stage (AAAI’26) via `Dual RQ` tokenization, `Dec-Only` backbone, and `NTP → DPO` objective.
- [DECOR](https://arxiv.org/abs/2509.10468) - Addresses Problem III at the Backbone stage (SIGIR’26) via `RQ-VAE` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [DOS](https://arxiv.org/abs/2602.04460) - Addresses Problem III at the Tokenization stage (WWW’26 Short) via `Orth. RQ` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [GRLM](https://arxiv.org/abs/2601.06798) - Addresses Problem III at the Tokenization stage (arXiv’26) via `Term-ID` tokenization, `Dec-Only` backbone, and `Multi-task NTP` objective.
- [Latte](https://arxiv.org/abs/2605.06331) - Addresses Problem III at the Backbone stage (arXiv’26) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [PROMISE](https://arxiv.org/abs/2601.04674) - Addresses Problem III at the Inference stage (arXiv’26) via `RQ-VAE` tokenization, `Enc-Dec` backbone, and `NTP + Aux.` objective.
- [S2GR](https://arxiv.org/abs/2601.18664) - Addresses Problem III at the Backbone stage (KDD’26) via `CoBa RQ-VAE` tokenization, `Enc-Dec` backbone, and `NTP + Ctr.` objective.
- [SIDReasoner](https://arxiv.org/abs/2603.23183) - Addresses Problem III at the Training stage (KDD’26) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP → RL` objective.
- [Think2Go](https://arxiv.org/abs/2607.28997) - Addresses Problem III at the Training stage (KDD’26) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP → RL` objective.

## Problem IV: Tokenization-Generation Objective Gap

- [GEM-Rec](https://arxiv.org/abs/2603.22231) - Addresses Problem IV at the Training stage (arXiv’26) via `RQ-VAE` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [GenRec-JD](https://arxiv.org/abs/2604.14878) - Addresses Problem IV at the Training stage (SIGIR’26) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP → RL` objective.
- [GFlowGR](https://arxiv.org/abs/2506.16114) - Addresses Problem IV at the Training stage (SIGIR’26) via `RQ-VAE / Learn. RQ` tokenization, `Enc-Dec` backbone, and `NTP + Aux.` objective.
- [RecoChain](https://arxiv.org/abs/2604.25787) - Addresses Problem IV at the Backbone stage (arXiv’26) via `RQ` tokenization, `Dec-Only` backbone, and `NTP + Rank` objective.
- [V-STAR](https://arxiv.org/abs/2602.10699) - Addresses Problem IV at the Training stage (KDD’26) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP → RL` objective.

## Problem V: Autoregressive Exposure Bias and Reward Sparse Signals

- [SEATER](https://arxiv.org/abs/2309.13375) - Addresses Problem V at the Tokenization stage (SIGIR-AP’24) via `Tree-Clus.` tokenization, `Enc-Dec` backbone, and `NTP + Ctr.` objective.
- [AtSpeed](https://arxiv.org/abs/2410.05165) - Addresses Problem V at the Inference stage (ICLR’25) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [OneRec-V2](https://arxiv.org/abs/2508.20900) - Addresses Problem V at the Backbone stage (arXiv’25) via `R-KM` tokenization, `Lazy Dec-Only` backbone, and `NTP → RL` objective.
- [RPG](https://arxiv.org/abs/2506.05781) - Addresses Problem V at the Backbone stage (KDD’25) via `Par. OPQ` tokenization, `Non-AR` backbone, and `MTP` objective.
- [NEZHA](https://arxiv.org/abs/2511.18793) - Addresses Problem V at the Inference stage (WWW’26 Industry) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [PAD-Rec](https://arxiv.org/abs/2604.27747) - Addresses Problem V at the Inference stage (arXiv’26) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `Multi-task NTP` objective.
- [STAMP](https://arxiv.org/abs/2604.05329) - Addresses Problem V at the Backbone stage (arXiv’26) via `RQ-VAE` tokenization, `Enc-Dec / Dec-Only` backbone, and `NTP + Aux.` objective.
- [STATIC](https://arxiv.org/abs/2602.22647) - Addresses Problem V at the Inference stage (KDD’26 ADS) via `RQ-VAE` tokenization, `Dec-Only` backbone, and `NTP` objective.

## Problem VI: Constrained Decoding Latency and Beam Degeneration

- [VQ-Rec](https://arxiv.org/abs/2210.12316) - Addresses Problem VI at the Tokenization stage (WWW’23) via `OPQ` tokenization, `Encoder` backbone, and `Discrim.` objective.
- [LIGER](https://arxiv.org/abs/2411.18814) - Addresses Problem VI at the Inference stage (arXiv’24) via `RQ-VAE` tokenization, `Enc-Dec` backbone, and `NTP + Dense` objective.
- [GMC](https://arxiv.org/abs/2507.12871) - Addresses Problem VI at the Tokenization stage (arXiv’25) via `Unified RQ` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [RecBase](https://arxiv.org/abs/2509.03131) - Addresses Problem VI at the Training stage (EMNLP’25) via `Curr. RQ` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [UTGRec](https://arxiv.org/abs/2504.04405) - Addresses Problem VI at the Tokenization stage (arXiv’25) via `Tree` tokenization, `Enc-Dec` backbone, and `NTP` objective.
- [CausalDPO](https://arxiv.org/abs/2603.22335) - Addresses Problem VI at the Training stage (ICML’26) via `LLM-Vocab` tokenization, `Dec-Only` backbone, and `NTP → DPO` objective.
- [DualGR](https://arxiv.org/abs/2511.12518) - Addresses Problem VI at the Backbone stage (WWW’26 Short) via `R-KM` tokenization, `Dec-Only` backbone, and `NTP + Rank` objective.
- [GenCDR](https://arxiv.org/abs/2511.08006) - Addresses Problem VI at the Tokenization stage (AAAI’26) via `RQ+LoRA` tokenization, `Dec-Only` backbone, and `NTP` objective.
- [MBGR](https://arxiv.org/abs/2604.02684) - Addresses Problem VI at the Tokenization stage (arXiv’26) via `RQ` tokenization, `Dec-Only` backbone, and `NTP + Aux.` objective.
- [SpecGR](https://arxiv.org/abs/2410.02939) - Addresses Problem VI at the Inference stage (AAAI’26) via `RQ-VAE` tokenization, `Enc-Dec` backbone, and `NTP + Rank` objective.
- [UniTok](https://arxiv.org/abs/2511.12922) - Addresses Problem VI at the Tokenization stage (AAAI’26) via `TokenMoE` tokenization, `Enc-Dec` backbone, and `NTP` objective.

## Contributing

Contributions follow the deterministic verification gates in [contributing.md](https://github.com/milkshakeforreal/Awesome-SID-Generative-Rec/blob/living-review/schema/README.md).
