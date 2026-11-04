# GNPR-SID

[← Problem × Stage Matrix](../../README.md#i--tokenization) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/gnpr-sid.md)

| **Title** | *Generative Next POI Recommendation with Semantic ID* |
| :-- | :-- |
| **Authors** | Wang et al. |
| **Venue** | KDD’25 |
| **Problem × Stage** | `I. Informativeness` · `Tokenization` · `POI` |
| **Changes** | ○ Representation · ● Tokenization |
| **SID inputs** | `Attr` + `Geo` + `Time` + `CF` |
| **Domain** | `POI / Local` |
| **Settings** | `cross-domain` |
| **Links** | [Paper](https://arxiv.org/abs/2506.01375) · [Code](https://github.com/wds1996/GNPR-SID) |
| **Reading level** | Reading Notes (Level 2) |

**On this page**: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [1. Why It Matters](#1-why-this-paper-matters) · [2. Method](#2-how-it-works) · [3. Experiments](#3-experimental-findings) · [4. Limitations](#4-limitations--critical-analysis) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>○ Attr+Geo+CF"] --> T["Tokenization<br/>● RQ-VAE"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Tokenizer: Fixed<br/>Objective: NTP"] --> I["Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class R other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Attr+Geo+CF`: Category and other attributes, plus geography, plus CF (POI).
- `RQ-VAE`: Residual-Quantized Variational AutoEncoder.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### TL;DR

> [!NOTE]
> GNPR-SID replaces random numeric POI IDs with RQ-VAE Semantic IDs built from semantic and collaborative features under a diversity loss, and fine-tunes an LLM to generate the next POI.

---

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Key Findings | On three benchmark datasets, GNPR-SID reports up to 16% improvement in recommendation accuracy over the compared methods (Abstract). |
| Limitation | Operating hours and collaborative features come from check-ins, so a new point of interest (POI) without visits has incomplete features (Sec. 4.1.1). |

---

### 1. Why This Paper Matters

Existing generative POI recommenders assign random numeric IDs to locations, which obscures spatial and semantic similarity across POIs (Abstract). GNPR-SID replaces random IDs with Semantic IDs (SIDs) quantized from spatial, temporal, and collaborative POI features under a diversity loss.

> "To achieve this, we propose the diversity loss, which promotes the distinctiveness of codewords within each codebook layer." (Sec. 1)

---

### 2. How It Works

![GNPR-SID architecture diagram](../../architectures/gnpr-sid.png)

```mermaid
flowchart LR
    subgraph Tok["1. Multi-View POI RQ-VAE Tokenizer"]
        A("Plus Code region") --> D["One-hot feature vectors"]
        B("Top 10 of 24 time slots") --> D
        C("Top 10 frequent visitors") --> D
        D --> E["3-level RQ-VAE (k-means init)"]:::key
        L1{{"Diversity + compactness losses"}}:::key -.-> E
        E --> F{"Collision?"}
        F -->|no| G("3-token POI SID")
        F -->|yes| H["Append 4th suffix token"] --> G
    end
    subgraph Gen["2. LLM Fine-Tuning"]
        G --> I["Augmented check-in prompts"]
        I --> J["LLaMA3-8B + LoRA (NTP)"]
        J --> K("Next POI SID")
    end
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### POI Features

GNPR-SID represents each POI with spatial, temporal, and collaborative features (Sec. 4.1.1). The spatial feature is a Google Plus Code region.

> "Compared to directly using geographic coordinates as spatial features, these region-based codes r ensure that nearby POIs are assigned the same Plus Code, allowing the model to share information among spatially adjacent POIs." (Sec. 4.1.1)

Operating hours are the 10 most visited of 24 hourly time slots, and the collaborative feature records each POI's 10 most frequent visitors (Sec. 4.1.1). All three views are encoded as one-hot vectors (Sec. 4.1.1, Eq. 1).

#### Quantization

A 3-level RQ-VAE (32 codewords per level on NYC, 64 on TKY and CA, dimension 64) quantizes the fused POI representation into discrete codes, while a diversity loss spreads codewords across the semantic space and an appended fourth token resolves any remaining collisions (Abstract, Sec. 4.1.2).

#### Training Data

To increase sequence variety before fine-tuning LLaMA3-8B with LoRA, GNPR-SID applies multiple cropping and fill-in-the-blank augmentation to user check-in trajectories (Appendix A.1).

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Foursquare NYC and TKY, Gowalla CA. POIs with fewer than 10 interactions and users with fewer than 10 check-ins are removed (following Yan et al. 2023). Sizes (users / POIs): NYC 1,083 / 5,135; TKY 2,293 / 7,873; CA 6,592 / 14,027.
  - Source: Datasets, filters, splits: [S5.SS1.p1](https://arxiv.org/html/2506.01375v2#S5.SS1.p1); statistics: [S5.T1](https://arxiv.org/html/2506.01375v2#S5.T1).
- **Split**: Records sorted by time and split 80% / 10% / 10% into training, validation, and test; within each user's test sequence the last visited POI is the target. Separate cross-city test: train on one city and test on the others (Table 5).
  - Source: Temporal 80/10/10 split and last-visit target: [S5.SS1.p1](https://arxiv.org/html/2506.01375v2#S5.SS1.p1); out-of-domain transfer: [S6.T5](https://arxiv.org/html/2506.01375v2#S6.T5).
- **Candidates**: not reported (full catalog versus sampled candidates); the metric is top-1 accuracy (Acc@1) of the generated POI.
  - Source: Top-1 accuracy only: [S5.SS3.p1](https://arxiv.org/html/2506.01375v2#S5.SS3.p1).
- **Visibility**: warm; users and POIs that do not appear in the training set are removed from the test set. The cross-city test in Table 5 uses POIs from another city, but their tokenizer visibility is not reported.
  - Source: Test users and POIs absent from training are removed: [S5.SS1.p1](https://arxiv.org/html/2506.01375v2#S5.SS1.p1).
- **SID**: 3-level RQ-VAE with 32 (NYC) or 64 (TKY, CA) codewords of dimension 64, k-means-initialized, plus diversity and compactness losses. Remaining collisions get an appended fourth token that makes each POI's SID unique (e.g. <d_0>, <d_1>). Table 4 reports unique SIDs and collisions before the suffix (e.g. NYC 590 collisions at lambda=0.25).
  - Source: 3 layers x 32 (NYC) or 64 (TKY, CA), dimension 64, k-means initialization: [S5.SS2.p1](https://arxiv.org/html/2506.01375v2#S5.SS2.p1); collision suffix: [S4.SS1.SSS2.p6](https://arxiv.org/html/2506.01375v2#S4.SS1.SSS2.p6); diversity loss and collision counts: [S4.SS1.SSS3.Px3.p1](https://arxiv.org/html/2506.01375v2#S4.SS1.SSS3.Px3.p1) and [S6.T4](https://arxiv.org/html/2506.01375v2#S6.T4).
- **Inference budget**: LLaMA3-8B with LoRA; decoding method not reported beyond top-1 prediction. Fine-tuning on 4 NVIDIA L40 GPUs (batch 2 per GPU); inference batch size not reported. Table 6 (NYC): total test time 110.62 s versus 230.36 s for LLM4POI.
  - Source: Hardware for fine-tuning: [S5.SS2.p1](https://arxiv.org/html/2506.01375v2#S5.SS2.p1); efficiency table: [S6.T6](https://arxiv.org/html/2506.01375v2#S6.T6); decoding not specified in Section 5.
- **Results from**: Table 2 (Acc@1 on NYC, TKY, CA versus traditional, Transformer, GCN, time-aware, and LLM-based baselines); Table 3 (ablations); Table 4 (diversity-loss weight and SID collisions); Table 5 (cross-city generalization); Table 6 (efficiency).
  - Source: Main: [S6.T2](https://arxiv.org/html/2506.01375v2#S6.T2); ablation: [S6.T3](https://arxiv.org/html/2506.01375v2#S6.T3); diversity loss: [S6.T4](https://arxiv.org/html/2506.01375v2#S6.T4); cross-city: [S6.T5](https://arxiv.org/html/2506.01375v2#S6.T5); efficiency: [S6.T6](https://arxiv.org/html/2506.01375v2#S6.T6).

</details>

- Main comparison: on Foursquare NYC, Foursquare TKY, and Gowalla CA, GNPR-SID improves top-1 accuracy (Acc@1) by up to 16% over traditional, Transformer, GCN, time-aware, and LLM baselines (Abstract, Table 2).
- Ablations and collision rate: Table 3 ablates the spatial, temporal, and collaborative features along with the quantization losses, while Table 4 reports unique SIDs and pre-suffix collisions across diversity-loss weights (590 collisions on NYC at $`\lambda = 0.25`$).
- Cross-city transfer: when trained on one city and evaluated on out-of-domain check-in sequences from the other cities, GNPR-SID retains transfer accuracy across cities (Sec. 6.5, Table 5).
- Efficiency: on NYC, compressing POIs into short SID token counts reduces total test time to 110.62 s compared with 230.36 s for LLM4POI, while also lowering training time and prompt token counts (Sec. 6.6, Table 6).

---

### 4. Limitations & Critical Analysis

**Our analysis.**

- GeoGR refines its `R-KM+EM` codes in an alternating loop with the generator; GNPR-SID trains its `RQ-VAE` codes once and keeps them fixed (`Fixed`).
- LC-Rec aligns its LLM with `Multi-task NTP` over item text; GNPR-SID encodes POI attributes, geography, and collaborative features in the tokenizer (`Attr+Geo+CF`) and fine-tunes the generator with standard `NTP`.

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["GNPR-SID"]
    P -->|"predecessor"| A["LC-Rec"]
    P -->|"alternative"| B["TIGER"]
    P -->|"alternative"| C["GeoGR"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **Predecessor** · [LC-Rec](lc-rec.md): GNPR-SID follows LC-Rec in aligning an LLM to SID tokens through language-task prompts, and adds POI-specific quantization with time-aware prompts.
  - Source: GNPR-SID v2, Section 4.2 builds its prompts inspired by Zheng et al. (2024): [S4.SS2.p2](https://arxiv.org/html/2506.01375v2#S4.SS2.p2).
- **Alternative** · [TIGER](tiger.md): TIGER is cited as generative recommendation with semantic IDs for products; GNPR-SID adapts RQ-VAE SIDs to POIs with diversity and compactness losses and an LLM generator.
  - Source: GNPR-SID v2, Section 2 cites Rajput et al. (2023): [S2.p2](https://arxiv.org/html/2506.01375v2#S2.p2); not a baseline in Table 2.
- **Alternative** · [GeoGR](geogr.md): GeoGR later builds geo-aware SIDs from geographic co-visitation and an EM refinement loop, and reports gains over GNPR-SID's SIDs.
  - Source: Evidence is from the later GeoGR paper: it follows GNPR-SID preprocessing and compares against it in Tables 2, 3, and 5: [S5.SS1.SSS1.p2](https://arxiv.org/html/2602.10411v2#S5.SS1.SSS1.p2), [S5.T2](https://arxiv.org/html/2602.10411v2#S5.T2), [S5.T3](https://arxiv.org/html/2602.10411v2#S5.T3), [S5.T5](https://arxiv.org/html/2602.10411v2#S5.T5).

[View all papers in this cell](../../README.md#i--tokenization)
