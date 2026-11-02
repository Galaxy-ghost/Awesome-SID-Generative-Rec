# HCGRec

*Learning from Unreachable Rewards: Hint-Conditioned Reinforcement Learning for Generative Recommendation* — Zhang et al. · CIKM’26

`IV. Utility` · `Training` · [Paper](https://arxiv.org/abs/2608.11980) · [Code](https://github.com/WncFht/GRec) · [Matrix](../../README.md#iv--training) · [中文](../zh/papers/hcgrec.md)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>–"] --> T["Tokenization<br/>RQ"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP → RL"] --> I["Inference<br/>Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `–`: Not reported in the paper.
- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

### TL;DR

> [!NOTE]
> HCGRec gives a minimal target-prefix hint when GRPO rollouts miss the correct item, training hinted tokens with supervised loss and sampled suffixes with GRPO, to recover signal from zero-reward groups.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Key Contribution | HCGRec gives a minimal target-prefix hint when GRPO rollouts miss the correct item, training hinted tokens with supervised loss and sampled suffixes with GRPO, to recover signal from zero-reward groups. |
| Modified Stage | Training |

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Musical Instruments, Arts/Crafts/Sewing, Video Games; maximum history 50. Filtering: not reported.
  - Source: Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS1.p1)
- **Split**: Per-user chronological leave-one-out: last item test, penultimate validation, remaining interactions training.
  - Source: Section 4.1.2: [S4.SS1.SSS2.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS2.p1)
- **Candidates**: full catalog
  - Source: Section 4.1.2: [S4.SS1.SSS2.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS2.p1)
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Section 4.1 defines no unseen-item evaluation: [S4.SS1](https://arxiv.org/html/2608.11980v2#S4.SS1)
- **SID**: Four-token residual-quantization SIDs, shared across variants; codebook sizes and collision handling: not reported.
  - Source: Sections 3.1 and 4.1.1: [S3.SS1.p1](https://arxiv.org/html/2608.11980v2#S3.SS1.p1) and [S4.SS1.SSS1.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS1.p1)
- **Inference budget**: Beam 50; HR/NDCG@5/10/50; no target-prefix hints at inference. Inference hardware, batch size, latency: not reported.
  - Source: Sections 3.5 and 4.1.2: [S3.SS5.p1](https://arxiv.org/html/2608.11980v2#S3.SS5.p1) and [S4.SS1.SSS2.p1](https://arxiv.org/html/2608.11980v2#S4.SS1.SSS2.p1)
- **Results from**: Original Table 2: main comparison; Figures 2-6 and Sections 4.3-4.5: reachability, hint policy, task/loss ablations, credit weight.
  - Source: Table 2 and Figures 2-6: [S4.T2](https://arxiv.org/html/2608.11980v2#S4.T2) and [S4.F2](https://arxiv.org/html/2608.11980v2#S4.F2) and [S4.F6](https://arxiv.org/html/2608.11980v2#S4.F6)

</details>

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["HCGRec"]
    P -->|predecessor| A["LC-Rec"]
    P -->|competitor| B["MiniOneRec"]
    P -->|competitor| C["TIGER"]
```

- **Predecessor** · [LC-Rec](lc-rec.md): LC-Rec provides the supervised semantic-alignment checkpoint in this pipeline.
  - Source: HCGRec v2, Section 4.2: https://arxiv.org/html/2608.11980v2#S4.SS2.p2.
- **Competitor** · [MiniOneRec](minionerec.md): MiniOneRec shares the SFT checkpoint and controlled post-training budget.
  - Source: HCGRec v2, Section 4.2 and Table 2: https://arxiv.org/html/2608.11980v2#S4.SS2.p1; https://arxiv.org/html/2608.11980v2#S4.T2.
- **Competitor** · [TIGER](tiger.md): TIGER is the semantic-ID generative baseline in the main comparison.
  - Source: HCGRec v2, Section 4.2 and Table 2: https://arxiv.org/html/2608.11980v2#S4.SS2.p2; https://arxiv.org/html/2608.11980v2#S4.T2.

[View all papers in this cell](../../README.md#iv--training)
