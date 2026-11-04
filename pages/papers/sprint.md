# SPRINT

[← Problem × Stage Matrix](../../README.md#v--backbone) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/sprint.md)

| **Title** | *Single-Step Generative Recommendation via Average Probability Velocity* |
| :-- | :-- |
| **Authors** | Cai et al. |
| **Venue** | arXiv’26 |
| **Problem × Stage** | `V. Efficiency` · `Backbone` |
| **Changes** | ● Backbone · ○ Objective |
| **SID inputs** | `Text` |
| **Domain** | `E-commerce` · `POI / Local` |
| **Links** | [Paper](https://arxiv.org/abs/2609.34306) · [Code](https://github.com/iamZhuoCai/SPRINT) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>Par. OPQ"] --> B["Backbone<br/>● Non-AR"] --> TR["Training<br/>Tokenizer: Fixed<br/>Objective: ○ Dual-level Flow Ctr."] --> I["Inference<br/>Scoring"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text`: Textual item metadata (titles, descriptions, categories, or prompts).
- `Par. OPQ`: Parallel optimized product quantization into unordered sub-codes.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Dual-level Flow Ctr.`: Contrastive training at token and complete-identifier levels in a flow-based model.
- `Scoring`: Direct candidate scoring without step-by-step SID generation.

### TL;DR

> [!NOTE]
> SPRINT predicts all Semantic ID token probabilities in one forward pass of a bidirectional Transformer, based on average probability velocity, and restores token coherence with a dual-level flow contrastive objective.

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Reviews 2014 Sports, Beauty and Toys; Amazon Reviews 2023 Instruments, Scientific, Games and Arts; Yelp. Filtering thresholds: not reported.
  - Source: Sec.4.1 and Appendix D.1: [S4.SS1.p1](https://arxiv.org/html/2609.34306v1#S4.SS1.p1) and [A4.SS1.p1](https://arxiv.org/html/2609.34306v1#A4.SS1.p1)
- **Split**: Per-user timestamp-ordered leave-one-out: last interaction test, penultimate validation, remainder training; history cap 20.
  - Source: Appendix D.1 and D.3: [A4.SS1.p1](https://arxiv.org/html/2609.34306v1#A4.SS1.p1) and [A4.SS3.p1](https://arxiv.org/html/2609.34306v1#A4.SS3.p1)
- **Candidates**: Full catalog: score valid SIDs with the sum of separately normalized token-probability and joint-SID similarity scores, returning top K. History-item exclusion: not reported. The 100/1000 sampled negative SIDs are training settings.
  - Source: Sec.4.1 and Sec.3.4 inference; sampled SIDs in Eq.9 are training negatives: [S4.SS1.p1](https://arxiv.org/html/2609.34306v1#S4.SS1.p1) and [S3.SS4.p3](https://arxiv.org/html/2609.34306v1#S3.SS4.p3) and [S3.SS3.p6](https://arxiv.org/html/2609.34306v1#S3.SS3.p6) and [S4.SS1.p3](https://arxiv.org/html/2609.34306v1#S4.SS1.p3)
- **Visibility**: warm; no unseen-item protocol is defined. Tokenizer exposure to test items: not reported.
  - Source: Sec.4.1 and Appendix D.1/D.3 define standard evaluation without unseen-item experiments: [S4.SS1](https://arxiv.org/html/2609.34306v1#S4.SS1) and [A4.SS1.p1](https://arxiv.org/html/2609.34306v1#A4.SS1.p1) and [A4.SS3.p1](https://arxiv.org/html/2609.34306v1#A4.SS3.p1)
- **SID**: OPQ on sentence-t5-base content embeddings; four parallel codebooks x 256 codewords, four tokens/item. Collision handling: not reported.
  - Source: Sec.3.1 and Appendix D.3: [S3.SS1.p2](https://arxiv.org/html/2609.34306v1#S3.SS1.p2) and [A4.SS3.p1](https://arxiv.org/html/2609.34306v1#A4.SS3.p1)
- **Inference budget**: One encoder-decoder pass from four masks, followed by all-valid-SID scoring with precomputed item-side vectors; beam n/a for SPRINT. Test batch 256/history20; efficiency baselines use beam10 where applicable, embedding256. Recall/NDCG@5/10; additional K=20/50/100/1000. Whole-test-set seconds on Sports/Beauty/Toys/Scientific/Instruments/Games: 2.65/1.52/1.28/4.08/4.62/7.55. Hardware, per-request latency, and inclusion of precomputation/data loading/metric computation in timing: not reported.
  - Source: Sec.3.4, Sec.4.1, Table3, Appendix D.3/D.11 and Algorithm2: [S3.SS4.p2](https://arxiv.org/html/2609.34306v1#S3.SS4.p2) and [S3.SS4.p3](https://arxiv.org/html/2609.34306v1#S3.SS4.p3) and [S4.SS1.p1](https://arxiv.org/html/2609.34306v1#S4.SS1.p1) and [S4.T3](https://arxiv.org/html/2609.34306v1#S4.T3) and [A4.SS3.p2](https://arxiv.org/html/2609.34306v1#A4.SS3.p2) and [A4.SS11.p1](https://arxiv.org/html/2609.34306v1#A4.SS11.p1) and [alg2](https://arxiv.org/html/2609.34306v1#alg2)
- **Results from**: Paper's comparisons/ablations, averaged over five random-seed runs (seed values not reported). Tables2/8 main accuracy, Table12 Yelp/Arts, Tables3/10 whole-test inference time, Table9 per-epoch training time. Efficiency configurations are shared; accuracy settings follow original papers and are tuned per dataset. Table10 accelerators use TIGER backbones. Explicit borrowed-versus-rerun score attribution: not reported.
  - Source: Sec.4.1, Tables2/3/4 and Appendix D.3/D.6/D.8: [S4.SS1.p3](https://arxiv.org/html/2609.34306v1#S4.SS1.p3) and [S4.T2](https://arxiv.org/html/2609.34306v1#S4.T2) and [S4.T3](https://arxiv.org/html/2609.34306v1#S4.T3) and [S4.T4](https://arxiv.org/html/2609.34306v1#S4.T4) and [A4.SS3.p2](https://arxiv.org/html/2609.34306v1#A4.SS3.p2) and [A4.SS6.p2](https://arxiv.org/html/2609.34306v1#A4.SS6.p2) and [A4.SS8.p1](https://arxiv.org/html/2609.34306v1#A4.SS8.p1)

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["SPRINT"]
    P -->|"competitor"| A["RPG"]
    P -->|"competitor"| B["LLaDA-Rec"]
    P -->|"competitor"| C["SID-MLP"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **Competitor** · [RPG](rpg.md): RPG is the compared single-step baseline with longer SIDs.
  - Source: SPRINT v1, Sec.1 and Sec.4.2: [S1.p2](https://arxiv.org/html/2609.34306v1#S1.p2); [S4.SS2.p2](https://arxiv.org/html/2609.34306v1#S4.SS2.p2).
- **Competitor** · [LLaDA-Rec](llada-rec.md): LLaDA-Rec is compared under one-step and four-step generation.
  - Source: SPRINT v1, Table1 and Sec.4.1: [S1.T1](https://arxiv.org/html/2609.34306v1#S1.T1); [S4.SS1.p2](https://arxiv.org/html/2609.34306v1#S4.SS1.p2).
- **Competitor** · [SID-MLP](sid-mlp.md): SID-MLP is the closest compared efficiency-oriented baseline.
  - Source: SPRINT v1, Appendix D.6: [A4.SS6.p2](https://arxiv.org/html/2609.34306v1#A4.SS6.p2); [A4.T10](https://arxiv.org/html/2609.34306v1#A4.T10).

[View all papers in this cell](../../README.md#v--backbone)
