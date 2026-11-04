# MMQ

[← Problem × Stage Matrix](../../README.md#i--tokenization) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/mmq.md)

| **Title** | *Multimodal Mixture-of-Quantization Tokenization for Semantic ID Generation and User Behavioral Adaptation* |
| :-- | :-- |
| **Authors** | Xu et al. |
| **Venue** | WSDM’26 |
| **Problem × Stage** | `I. Informativeness` · `Tokenization` |
| **Changes** | ● Tokenization · ○ Tokenizer · ○ Objective |
| **SID inputs** | `Text` + `Img` |
| **Domain** | `E-commerce` · `Ads` |
| **Links** | [Paper](https://arxiv.org/abs/2508.15281) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text+Img"] --> T["Tokenization<br/>● MoE-VQ"] --> B["Backbone<br/>HeterRec"] --> TR["Training<br/>Tokenizer: ○ Joint<br/>Objective: ○ MTP"] --> I["Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+Img`: Text and visual item representations.
- `MoE-VQ`: Mixture-of-experts vector quantization.
- `HeterRec`: HeterRec, the named recommendation backbone used in the paper.
- `Joint`: The generator loss updates the tokenizer directly.
- `MTP`: Predicts several codes in parallel at once.

### TL;DR

> [!NOTE]
> MMQ trains a multimodal tokenizer with modality-shared and modality-specific experts under orthogonal regularization, then fine-tunes its Semantic IDs on behavior objectives with a multimodal reconstruction loss.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Beauty; retrieval uses user/item 5-core filtering and histories capped at 20. Southeast Asian advertising logs, October 2024-May 2025 (30M users, 40M ads); industrial filters not reported.
  - Source: Section 4.1.1: [S4.SS1.SSS1.p2](https://arxiv.org/html/2508.15281v1#S4.SS1.SSS1.p2) and [S4.SS1.SSS1.p3](https://arxiv.org/html/2508.15281v1#S4.SS1.SSS1.p3)
- **Split**: Beauty ranking: chronological 90% train/10% test; ratings >3 positive, <=3 negative. Retrieval and industrial offline splits not reported. Online A/B: July 6-August 6, 2025; treatment 10% random user traffic.
  - Source: Sections 4.1.1 and 5: [S4.SS1.SSS1.p3](https://arxiv.org/html/2508.15281v1#S4.SS1.SSS1.p3) and [S5.p1](https://arxiv.org/html/2508.15281v1#S5.p1)
- **Candidates**: Retrieval: not reported; ranking evaluates labeled ratings, candidate retrieval n/a.
  - Source: Section 4.1.1/4.1.2 gives labels and metrics, not retrieval candidates: [S4.SS1.SSS1.p3](https://arxiv.org/html/2508.15281v1#S4.SS1.SSS1.p3) and [S4.SS1.SSS2.p3](https://arxiv.org/html/2508.15281v1#S4.SS1.SSS2.p3)
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Section 4.1 defines no item holdout: [S4.SS1](https://arxiv.org/html/2508.15281v1#S4.SS1)
- **SID**: 6 positions: 2 shared, 2 text-specific, 2 visual-specific; codebook size 100 (Beauty), 3000 (industrial). Collision handling not reported.
  - Source: Section 4.1.4: [S4.SS1.SSS4.p2](https://arxiv.org/html/2508.15281v1#S4.SS1.SSS4.p2)
- **Inference budget**: Retrieval K=5/10 using HeterRec; ranking uses PPNet. Decoding budget, hardware, inference batch size, and latency not reported.
  - Source: Sections 4.1.2/4.1.4: [S4.SS1.SSS2.p3](https://arxiv.org/html/2508.15281v1#S4.SS1.SSS2.p3) and [S4.SS1.SSS4.p1](https://arxiv.org/html/2508.15281v1#S4.SS1.SSS4.p1)
- **Results from**: Original Table 1: tokenizer comparisons under HeterRec retrieval/PPNet ranking; Section 5: online A/B versus deployed ItemID system.
  - Source: Table 1 and Section 5: [S4.T1](https://arxiv.org/html/2508.15281v1#S4.T1) and [S5.p1](https://arxiv.org/html/2508.15281v1#S5.p1)

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["MMQ"]
    P -->|"predecessor"| A["TIGER"]
    P -->|"alternative"| B["OneRec"]
    P -->|"alternative"| C["LC-Rec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **Predecessor** · [TIGER](tiger.md): MMQ replaces TIGER's separated tokenizer training with behavior-aware joint adaptation.
  - Source: MMQ v1, Section 3.3: [S3.SS3.p1](https://arxiv.org/html/2508.15281v1#S3.SS3.p1).
- **Alternative** · [OneRec](onerec.md): OneRec aligns modalities before quantization; MMQ separates shared and specific experts.
  - Source: MMQ v1, Section 2: [S2.p3](https://arxiv.org/html/2508.15281v1#S2.p3).
- **Alternative** · [LC-Rec](lc-rec.md): LC-Rec aligns indices through multitask fine-tuning; MMQ adapts multimodal tokenization directly.
  - Source: MMQ v1, Sections 2 and 3.3: [S2.p2](https://arxiv.org/html/2508.15281v1#S2.p2); [S3.SS3.p1](https://arxiv.org/html/2508.15281v1#S3.SS3.p1).

[View all papers in this cell](../../README.md#i--tokenization)
