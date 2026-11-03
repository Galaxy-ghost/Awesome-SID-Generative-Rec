# FedCGR

[← Problem × Stage Matrix](../../README.md#vi--backbone) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · English | [中文](../zh/papers/fedcgr.md)

| **Title** | *Federated Cross-Domain Generative Recommendation* |
| :-- | :-- |
| **Authors** | Liu et al. |
| **Venue** | CIKM’26 |
| **Problem × Stage** | `VI. Generalization` · `Backbone` |
| **Links** | [Paper](https://arxiv.org/abs/2608.10929) · [Code](https://github.com/ZhuodLiu/FedCGR) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP + Aux."] --> I["Inference<br/>C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text`: Textual item metadata (titles, descriptions, categories, or prompts).
- `RQ-VAE`: Residual-Quantized Variational AutoEncoder.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> FedCGR performs federated cross-domain recommendation over shared Semantic IDs from public metadata, injects local collaborative evidence, and aggregates parameters by domain relatedness, without exchanging private interactions.

---

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Key Contribution | FedCGR performs federated cross-domain recommendation over shared Semantic IDs from public metadata, injects local collaborative evidence, and aggregates parameters by domain relatedness, without exchanging private interactions. |
| Modified Stage | Backbone |

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Review: Grocery, Beauty, Sports, Food, Kitchen; six cross-domain scenarios FK/GB/GS/FKB/GBS/GKBS; per-domain 5-core filtering.
  - Source: Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS1.p1) and [S4.SS1.SSS1.p3](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS1.p3)
- **Split**: Per-user leave-one-out: last item test, second-to-last validation, remaining interactions training.
  - Source: Section 4.1.3: [S4.SS1.SSS3.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS3.p1)
- **Candidates**: full catalog; additionally sampled: 999 random negatives per user, fixed once and shared across methods (seed42). Negative-sampling distribution beyond random and history-item exclusion: not reported.
  - Source: Section 4.1.3: [S4.SS1.SSS3.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS3.p1)
- **Visibility**: warm; no unseen-item protocol is defined. Cold-start analysis groups users by training-history length (<=7, 8-15, >=16), not unseen items. SID metadata pretraining excludes private interactions; local CF uses client interaction sequences. Item-level generator/tokenizer/CF exposure: not reported.
  - Source: Sections 3.1 and 4.4: [S3.SS1.p1](https://arxiv.org/html/2608.10929v1#S3.SS1.p1) and [S4.SS4.p1](https://arxiv.org/html/2608.10929v1#S4.SS4.p1)
- **SID**: Frozen metadata RQ-VAE: 3 levels x 256 codes; colliding items share SID scores, ties broken by validation-set item popularity.
  - Source: Sections 3.2 and 4.1.4: [S3.SS2.p2](https://arxiv.org/html/2608.10929v1#S3.SS2.p2) and [S4.SS1.SSS4.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS4.p1)
- **Inference budget**: Target-domain trie-constrained beam 50; H/NDCG@10; experiments on RTX 4090 GPUs. Inference batch size and latency: not reported.
  - Source: Sections 3.4 and 4.1.4: [S3.SS4.p2](https://arxiv.org/html/2608.10929v1#S3.SS4.p2) and [S4.SS1.SSS4.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS4.p1)
- **Results from**: Original Tables 3/4: full-ranking/sampled comparisons; Table 5: ablation; Table 6: diagnostics; Figures 3-5: user activity, sensitivity, communication efficiency.
  - Source: Tables 3-6 and Figures 3-5: [S4.T3](https://arxiv.org/html/2608.10929v1#S4.T3) and [S4.T4](https://arxiv.org/html/2608.10929v1#S4.T4) and [S4.T5](https://arxiv.org/html/2608.10929v1#S4.T5) and [S4.T6](https://arxiv.org/html/2608.10929v1#S4.T6) and [S4.F3](https://arxiv.org/html/2608.10929v1#S4.F3) and [S4.F4](https://arxiv.org/html/2608.10929v1#S4.F4) and [S4.F5](https://arxiv.org/html/2608.10929v1#S4.F5)

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["FedCGR"]
    P -->|"competitor"| A["TIGER"]
    P -->|"alternative"| B["GenCDR"]
    P -->|"predecessor"| C["VQ-Rec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **Competitor** · [TIGER](tiger.md): TIGER and its FedAvg/FedProx variants are full-ranking baselines.
  - Source: FedCGR v1, Section 4.1.2 and Table 3: [S4.SS1.SSS2.p2](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS2.p2); [S4.T3](https://arxiv.org/html/2608.10929v1#S4.T3).
- **Alternative** · [GenCDR](gencdr.md): GenCDR uses centralized semantic CDR; FedCGR keeps interactions local.
  - Source: FedCGR v1, Section 5: [S5.p1](https://arxiv.org/html/2608.10929v1#S5.p1); [S5.p2](https://arxiv.org/html/2608.10929v1#S5.p2).
- **Predecessor** · [VQ-Rec](vq-rec.md): Related work identifies VQ-Rec as an earlier transferable quantized-item representation method.
  - Source: FedCGR v1, Section 5: [S5.p2](https://arxiv.org/html/2608.10929v1#S5.p2).

[View all papers in this cell](../../README.md#vi--backbone)
