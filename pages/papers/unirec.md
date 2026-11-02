# UniRec

| **Title** | *Bridging the Expressive Gap between Generative and Discriminative Recommendation via Chain-of-Attribute* |
| :-- | :-- |
| **Authors** | Wang et al. |
| **Venue** | arXiv’26 |
| **Problem × Stage** | `I. Informativeness` · `Tokenization` |
| **Links** | [Paper](https://arxiv.org/abs/2604.12234) · [Matrix](../../README.md#i--tokenization) · [中文](../zh/papers/unirec.md) |
| **Reading level** | Overview (Level 1) |

On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text+CF"] --> T["Tokenization<br/>RQ"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP → DPO"] --> I["Inference<br/>C-Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> UniRec prefixes each Semantic ID with category, seller, and brand tokens through Chain-of-Attribute, to recover the item-side feature crossing of discriminative models, and adds capacity-constrained quantization.

---

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | UniRec prefixes each Semantic ID with category, seller, and brand tokens through Chain-of-Attribute, to recover the item-side feature crossing of discriminative models, and adds capacity-constrained quantization. |
| Modified Stage | Tokenization |

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Shopee main-feed production logs over 9 consecutive days, billions of interactions (impressions, clicks, add-to-cart, purchases). Filtering and catalog size: not reported.
  - Source: Shopee production logs: [S4.SS1.SSS1.Px1.p1](https://arxiv.org/html/2604.12234v5#S4.SS1.SSS1.Px1.p1).
- **Split**: not reported (the 9-day window is described, but not how training and test are divided). Online A/B test in feed and landing scenarios (Table 5); duration and traffic: not reported.
  - Source: No train/test division stated; online A/B: [S4.T5](https://arxiv.org/html/2604.12234v5#S4.T5).
- **Candidates**: not reported (full catalog versus sampled); Hit Ratio at 50, 100, 200 on all samples and on purchase samples.
  - Source: Hit Ratio on all and order samples: [S4.T1](https://arxiv.org/html/2604.12234v5#S4.T1).
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: No unseen-item protocol: [S4.SS1.SSS1.Px1.p1](https://arxiv.org/html/2604.12234v5#S4.SS1.SSS1.Px1.p1).
- **SID**: Capacity-constrained residual K-means SIDs with 3 layers x 4,000 codes, using exposure-weighted capacity penalties (tolerance 1.05) instead of equal item counts; Chain-of-Attribute prefixes each SID with category tokens (L2, L3) decoded first. Collision handling: not reported.
  - Source: Capacity-constrained SIDs, 3 layers x 4000, tau=1.05; CoA attribute prefix: [S4.SS1.SSS1.Px3.p1](https://arxiv.org/html/2604.12234v5#S4.SS1.SSS1.Px3.p1) and [S3.SS3.SSS0.Px2.p2](https://arxiv.org/html/2604.12234v5#S3.SS3.SSS0.Px2.p2).
- **Inference budget**: Autoregressive decoding of attribute tokens then SID tokens; beam width not reported. Online end-to-end latency 110 ms versus 266 ms for the traditional pipeline; hardware and batch size: not reported. Decoder-only model with cross-attention (d_model 256, 3 layers).
  - Source: End-to-end latency: [S4.SS2.SSS0.Px3.p1](https://arxiv.org/html/2604.12234v5#S4.SS2.SSS0.Px3.p1); model size: [S4.SS1.SSS1.Px3.p1](https://arxiv.org/html/2604.12234v5#S4.SS1.SSS1.Px3.p1).
- **Results from**: Table 1 (HR on all and order samples versus SASRec, TIGER, OneRec-V2); Table 2 (CoA configurations); Table 3 (SID construction, ablation, scaling); Table 4 (multi-scene task-conditioned BOS); Table 5 (online A/B: orders +4.76%, GMV +5.60%).
  - Source: Results: [S4.T1](https://arxiv.org/html/2604.12234v5#S4.T1), [S4.T2](https://arxiv.org/html/2604.12234v5#S4.T2), [S4.T3](https://arxiv.org/html/2604.12234v5#S4.T3), [S4.T4](https://arxiv.org/html/2604.12234v5#S4.T4), [S4.T5](https://arxiv.org/html/2604.12234v5#S4.T5).

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["UniRec"]
    P -->|competitor| A["OneRec-V2"]
    P -->|competitor| B["TIGER"]
    P -->|predecessor| C["OneRec"]
    P -->|alternative| D["CapsID"]
```

- **Competitor** · [OneRec-V2](onerec-v2.md): OneRec-V2 decodes SIDs with a decoder-only model over user context; UniRec first decodes coarse item attributes, uses exposure-capacity-constrained SIDs, and aligns to GMV with RFT and DPO.
  - Source: UniRec v5, baselines: https://arxiv.org/html/2604.12234v5#S4.I2.i3.p1; Table 1: https://arxiv.org/html/2604.12234v5#S4.T1.
- **Competitor** · [TIGER](tiger.md): TIGER generates RQ-VAE IDs without any item-side attribute conditioning, which UniRec adds through Chain-of-Attribute.
  - Source: UniRec v5, baselines: https://arxiv.org/html/2604.12234v5#S4.I2.i2.p1; Table 1: https://arxiv.org/html/2604.12234v5#S4.T1.
- **Predecessor** · [OneRec](onerec.md): UniRec starts from OneRec's balanced quantization and replaces equal item counts with exposure-weighted capacity limits.
  - Source: UniRec v5, Section 3.2: https://arxiv.org/html/2604.12234v5#S3.SS2.p1; RQ-KMeans ablation in Table 3: https://arxiv.org/html/2604.12234v5#S4.SS1.SSS3.Px1.p1.
- **Alternative** · [CapsID](capsid.md): CapsID later compares against a UniRec-style Chain-of-Attribute patch and argues that a variable-length SID can avoid extra attribute decoding.
  - Source: Evidence is from the later CapsID paper: baselines and Table 3: https://arxiv.org/html/2605.05096v1#S4.SS1.SSS0.Px2.p1 and https://arxiv.org/html/2605.05096v1#S4.T3.

[View all papers in this cell](../../README.md#i--tokenization)
