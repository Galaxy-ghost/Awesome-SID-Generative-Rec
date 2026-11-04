# UNGER

[← Problem × Stage Matrix](../../README.md#i--representation) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/unger.md)

| **Title** | *Generative Recommendation with A Unified Code via Semantic and Collaborative Integration* |
| :-- | :-- |
| **Authors** | Xiao et al. |
| **Venue** | TOIS’25 |
| **Problem × Stage** | `I. Informativeness` · `Representation` |
| **Changes** | ● Representation · ○ Objective |
| **SID inputs** | `Text` + `CF` |
| **Domain** | `E-commerce` |
| **Links** | [Paper](https://arxiv.org/abs/2502.06269) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>● Text+CF"] --> T["Tokenization<br/>R-KM"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Tokenizer: Fixed<br/>Objective: ○ NTP + Ctr."] --> I["Inference<br/>Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class R main
```

- `Text+CF`: Text representations combined with collaborative signals.
- `R-KM`: Residual k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `Beam`: Autoregressive beam search over Semantic ID tokens.

### TL;DR

> [!NOTE]
> UNGER learns one integrated semantic-collaborative embedding through cross-modality alignment and next-item prediction, quantizes it into a unified code, and adds intra-modality distillation, instead of separate codes per modality.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Reviews 2014: Beauty, Sports and Outdoors, Toys and Games; user/item 5-core.
  - Source: [S4.SS1.SSS1.p1](https://arxiv.org/html/2502.06269v3#S4.SS1.SSS1.p1) ; Table 2.
- **Split**: Per-user chronological leave-one-out: last item test, penultimate validation, earlier items training; training history capped at 20 items.
  - Source: [S4.SS1.SSS2.p3](https://arxiv.org/html/2502.06269v3#S4.SS1.SSS2.p3)
- **Candidates**: not reported; full-catalog versus sampled evaluation and history exclusion are unspecified.
  - Source: [S4.SS1.SSS2](https://arxiv.org/html/2502.06269v3#S4.SS1.SSS2) ; evaluation reports Recall/NDCG@10/20 but no candidate-pool protocol.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: [S4.SS1.SSS2.p3](https://arxiv.org/html/2502.06269v3#S4.SS1.SSS2.p3)
- **SID**: DIN collaborative and Llama2-7b textual representations are integrated before fixed hierarchical k-means residual quantization; 4 levels, 256 clusters per level; item-code lookup table; main-tokenizer collision handling not reported.
  - Source: [S3.SS3.SSS5](https://arxiv.org/html/2502.06269v3#S3.SS3.SSS5) ; Algorithm 1; [S4.T4](https://arxiv.org/html/2502.06269v3#S4.T4)
- **Inference budget**: Autoregressive beam search, width 100; lookup and confidence ranking for top-k. Beauty speed comparison separately uses top-5 and beam 100; inference hardware and batch size not reported.
  - Source: [S3.SS5.SSS2.p1](https://arxiv.org/html/2502.06269v3#S3.SS5.SSS2.p1) ; [S4.T4](https://arxiv.org/html/2502.06269v3#S4.T4) ; [S1.F4.fig1](https://arxiv.org/html/2502.06269v3#S1.F4.fig1)
- **Results from**: UNGER experiments averaged over 5 runs (seeds 2020–2024), with standard errors in Table 3; unstarred baseline scores copied from Zhou et al. (2020) and Wang et al. (2024c), starred TIGER and ColaRec scores reimplemented for missing statistics.
  - Source: [S4.SS2.SSS2.p1](https://arxiv.org/html/2502.06269v3#S4.SS2.SSS2.p1) ; [S4.T3](https://arxiv.org/html/2502.06269v3#S4.T3)

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["UNGER"]
    P -->|"predecessor"| A["EAGER"]
    P -->|"competitor"| B["TIGER"]
    P -->|"competitor"| C["ColaRec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **Predecessor** · [EAGER](eager.md): Its dual-code design motivates UNGER's unified code.
  - Source: [S1.p3](https://arxiv.org/html/2502.06269v3#S1.p3) ; §3.3.5 follows its quantization approach; §4.2 baseline.
- **Competitor** · [TIGER](tiger.md): Semantic-only generative baseline reimplemented in Table 3.
  - Source: [S4.SS2.SSS1.p3](https://arxiv.org/html/2502.06269v3#S4.SS2.SSS1.p3) ; [S4.T3](https://arxiv.org/html/2502.06269v3#S4.T3)
- **Competitor** · [ColaRec](colarec.md): Collaborative/content baseline reimplemented in Table 3.
  - Source: [S4.SS2.SSS1.p3](https://arxiv.org/html/2502.06269v3#S4.SS2.SSS1.p3) ; [S4.T3](https://arxiv.org/html/2502.06269v3#S4.T3)

[View all papers in this cell](../../README.md#i--representation)
