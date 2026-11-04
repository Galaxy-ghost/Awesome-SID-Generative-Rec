# COBRA

[← Problem × Stage Matrix](../../README.md#i--backbone) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/cobra.md)

| **Title** | *Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations* |
| :-- | :-- |
| **Authors** | Yang et al. |
| **Venue** | NeurIPS’25 |
| **Problem × Stage** | `I. Informativeness` · `Backbone` |
| **Changes** | ○ Representation · ● Backbone · ○ Objective · ○ Inference |
| **SID inputs** | `Text` |
| **Domain** | `E-commerce` · `Ads` |
| **Scenario** | `General Item Recommendation`; `Online Experiment or Deployment` |
| **Links** | [Paper](https://arxiv.org/abs/2503.02453) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>○ Text+SID"] --> T["Tokenization<br/>Casc. RQ"] --> B["Backbone<br/>● Dec-Only"] --> TR["Training<br/>Tokenizer: Fixed<br/>Objective: ○ NTP + Dense"] --> I["Inference<br/>○ BeamFusion"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class R,TR,I other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Casc. RQ`: Cascaded sparse-to-dense residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Dense`: NTP plus dense-vector prediction.
- `BeamFusion`: Joint decoding combining autoregressive SID beam search with dense nearest-neighbor scoring.

### TL;DR

> [!NOTE]
> COBRA generates a sparse Semantic ID and then a dense vector conditioned on it, trains both end to end, and decodes with BeamFusion, which combines beam search with nearest-neighbor scores.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Product Reviews (May 1996-September 2014): Beauty, Sports and Outdoors, Toys and Games, with 5-core filtering of users and items (users / items: 22,363 / 12,101; 35,598 / 18,357; 19,412 / 11,924). Industrial: Baidu advertising logs across list-page, dual-column, and short-video scenarios, about 5 million users and 2 million ads; filtering not reported.
  - Source: Public categories, date range, 5-core filtering: [S4.SS1.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS1.p1); statistics: [S4.T1](https://arxiv.org/html/2503.02453v1#S4.T1); industrial data: [S4.SS2.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS2.SSS1.p1).
- **Split**: Public datasets: train/validation/test allocation not reported. Industrial: first 60 days of logs for training and the following day for testing. Online: A/B test in January 2025 with 10% of user traffic.
  - Source: Public split not stated: [S4.SS1.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS1.p1); industrial 60-day train and next-day test: [S4.SS2.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS2.SSS1.p1); online A/B: [S4.SS4.p1](https://arxiv.org/html/2503.02453v1#S4.SS4.p1).
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); top-K lists are formed by ANN retrieval among items under the top-M generated sparse IDs, fused by BeamFusion. Public K=5 and 10; industrial K=50 to 800.
  - Source: Retrieval combines beam search over sparse IDs with ANN over items under each ID: [S3.SS4.p2](https://arxiv.org/html/2503.02453v1#S3.SS4.p2) and [S3.SS4.p5](https://arxiv.org/html/2503.02453v1#S3.SS4.p5); evaluation metrics: [S4.SS1.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS1.p1).
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard public protocol and next-day industrial test, with no cold-start experiment: [S4.SS1.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS1.p1) and [S4.SS2.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS2.SSS1.p1).
- **SID**: Public: 3-level semantic IDs with codebook size 32 per level, generated from T5 embeddings following TIGER's method. Industrial: 2-level 32 x 32 sparse IDs (the w/o Dense variant uses 3 levels of 256). Items under the same sparse ID are distinguished by a generated dense vector and ANN search within that ID's candidate set; a collision-resolution rule for the sparse IDs is not reported.
  - Source: Public SID: [S4.SS1.SSS3.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS3.p1); industrial SID and the w/o Dense variant: [S4.SS2.SSS3.p1](https://arxiv.org/html/2503.02453v1#S4.SS2.SSS3.p1); items sharing a sparse ID are separated by the dense vector: [S3.SS4.p5](https://arxiv.org/html/2503.02453v1#S3.SS4.p5).
- **Inference budget**: Beam search returns the top M sparse IDs, then ANN retrieves the top N items per ID and BeamFusion combines beam and cosine scores; numerical M and N are not reported. The recall-diversity analysis selects tau=0.9 with the second coefficient fixed at 16. Public model: 1-layer encoder and 2-layer decoder. Hardware, inference batch size, and latency: not reported.
  - Source: Beam search top-M, ANN top-N, BeamFusion coefficients: [S3.SS4.p2](https://arxiv.org/html/2503.02453v1#S3.SS4.p2), [S3.SS4.p5](https://arxiv.org/html/2503.02453v1#S3.SS4.p5), [S3.SS4.p6](https://arxiv.org/html/2503.02453v1#S3.SS4.p6); tau setting: [S4.SS3.SSS2.p1](https://arxiv.org/html/2503.02453v1#S4.SS3.SSS2.p1); architecture: [S4.SS1.SSS3.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS3.p1).
- **Results from**: Table 2 (Beauty, Sports, Toys); Table 3 (Baidu industrial Recall@50-800 with ablated variants); Section 4.4 (online A/B: +3.60% conversion, +4.15% ARPU); Figures 4-6 (embedding analysis and recall-diversity curves).
  - Source: Public table: [S4.T2](https://arxiv.org/html/2503.02453v1#S4.T2); industrial variants: [S4.T3](https://arxiv.org/html/2503.02453v1#S4.T3); online: [S4.SS4.p1](https://arxiv.org/html/2503.02453v1#S4.SS4.p1); diversity curves: [S4.F6](https://arxiv.org/html/2503.02453v1#S4.F6).

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["COBRA"]
    P -->|"competitor"| A["TIGER"]
    P -->|"alternative"| B["LIGER"]
    P -->|"alternative"| C["CapsID"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **Competitor** · [TIGER](tiger.md): TIGER retrieves items from sparse semantic IDs alone; COBRA follows TIGER's SID construction but generates a dense vector after each sparse ID and fuses beam and ANN scores.
  - Source: COBRA v1, baselines and SID setting: [S4.I1.i9.p1](https://arxiv.org/html/2503.02453v1#S4.I1.i9.p1) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS3.p1); Table 2: [S4.T2](https://arxiv.org/html/2503.02453v1#S4.T2); the w/o Dense variant mirrors TIGER: [S4.I2.i2.p1](https://arxiv.org/html/2503.02453v1#S4.I2.i2.p1).
- **Alternative** · [LIGER](liger.md): LIGER (Yang et al., 2024) unifies generative and dense retrieval as a hybrid, while COBRA cascades sparse-ID generation and dense-vector generation inside one decoder.
  - Source: COBRA v1, Section 1 cites Yang et al. (2024), Unifying Generative and Dense Retrieval, for the fine-grained similarity gap of generative methods: [S1.p3](https://arxiv.org/html/2503.02453v1#S1.p3); not a baseline in Table 2.
- **Alternative** · [CapsID](capsid.md): CapsID removes the dense patch and instead makes the SID soft-routed and variable-length, reporting about half of COBRA's per-query latency at similar Recall@100.
  - Source: Evidence is from the later CapsID paper: COBRA is a patch-route baseline in Tables 3, 4, and 6: [S4.T3](https://arxiv.org/html/2605.05096v1#S4.T3), [S4.T4](https://arxiv.org/html/2605.05096v1#S4.T4), [S4.T6](https://arxiv.org/html/2605.05096v1#S4.T6); latency comparison: [S4.SS5.SSS0.Px5.p2](https://arxiv.org/html/2605.05096v1#S4.SS5.SSS0.Px5.p2).

[View all papers in this cell](../../README.md#i--backbone)
