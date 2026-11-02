# REGER

*Modeling inter-item Relations with Semantic IDs for Generative Recommendation* — Huang et al. · arXiv’26

`I. Informativeness` · `Training` · [Paper](https://arxiv.org/abs/2610.37584) · [Matrix](../../README.md#i--training) · [中文](../zh/papers/reger.md)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP → (NTP + Aux.)"] --> I["Inference<br/>Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → (NTP + Aux.)`: Next-token prediction, followed by joint optimization of next-token prediction and auxiliary objectives.

### TL;DR

> [!NOTE]

> REGER pretrains a generator to produce semantic neighbors' Semantic IDs, combines global and ID-boundary local attention, and distills a discriminative teacher's next-token distributions along the target prefix path.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | REGER pretrains a generator to produce semantic neighbors' Semantic IDs, combines global and ID-boundary local attention, and distills a discriminative teacher's next-token distributions along the target prefix path. |
| Modified Stage | Training |

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Reviews 2014 Beauty/Sports/Toys and 2023 Instruments/Scientific/Games; 5-core filtering and maximum history 20 items.
  - Source: [S5.SS1.p1](https://arxiv.org/html/2610.37584v1#S5.SS1.p1) ; #A1.T6
- **Split**: Per-user chronological leave-one-out: latest interaction test, second latest validation, all earlier interactions training.
  - Source: [A1.SS1.p1](https://arxiv.org/html/2610.37584v1#A1.SS1.p1)
- **Candidates**: not reported
  - Source: Evaluation settings give metrics and seeds but no evaluation universe: [S5.SS1](https://arxiv.org/html/2610.37584v1#S5.SS1) ; #A1.SS1
- **Visibility**: warm; no unseen-item protocol is defined. GSR semantic neighbors are drawn from the item catalog; tokenizer and frozen DuoRec teacher exposure to test items/interactions not explicitly separated.
  - Source: [S5.SS1.p1](https://arxiv.org/html/2610.37584v1#S5.SS1.p1) ; #S4.SS1.p3 ; #S4.SS3.SSS2.p1 ; #A1.SS3.p1
- **SID**: RQ-VAE on Sentence-T5 embeddings reduced to 128 dimensions by PCA/whitening; semantic level count and codebook sizes not reported in paper. Extra token distinguishes identical semantic codes; suffix vocabulary size/assignment not reported. Dataset-specific SID mapping shared across recommender seeds.
  - Source: [S3.SS1.p1](https://arxiv.org/html/2610.37584v1#S3.SS1.p1) ; #A1.SS3.p1
- **Inference budget**: Unconstrained beam 20 for validation/test, without teacher; teacher ablation uses beam 50. Recall/NDCG@5/10. Table 4 efficiency probe on TIGER+HCPD: one L40, FP32, test batch 256, KV cache off, 16 s for full Beauty test set. REGER-specific absolute inference time and general inference batch/hardware not reported.
  - Source: [A1.SS3.p2](https://arxiv.org/html/2610.37584v1#A1.SS3.p2) ; #A1.SS3.p4 ; #A1.T7 ; #S5.T4 ; #S5.SS4.p3
- **Results from**: Table 1: 2014 comparisons with reproduced baselines, three seeds 2024/2025/2026; Table 2: training objectives on TIGER; Table 3: REGER ablations. Table 6: 2023 results, with published baseline rows from Latte, OMEGA, DECOR and TopoTok papers.
  - Source: [S4.T1](https://arxiv.org/html/2610.37584v1#S4.T1) ; #S5.T2 ; #S5.T3 ; #A1.T6 ; #A1.SS3.p2

</details>

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["REGER"]
    P -->|predecessor| A["TIGER"]
    P -->|competitor| B["GFlowGR"]
    P -->|competitor| C["APAO"]
    P -->|predecessor| D["Pctx"]
```

- **前序工作** · [TIGER](tiger.md): REGER uses residual-quantized SID generation and additionally tests its HCPD training objective directly on TIGER.
  - Source: REGER v1, Section 3.1 and Table 2: https://arxiv.org/html/2610.37584v1#S3.SS1.p1; https://arxiv.org/html/2610.37584v1#S5.T2.
- **同期对比** · [GFlowGR](gflowgr.md): GFlowGR supervises generation with collaborative rewards and flow balance; HCPD directly matches teacher conditional preferences over legal prefix branches, using the same DuoRec teacher.
  - Source: REGER v1, Section 5.4 and Table 2: https://arxiv.org/html/2610.37584v1#S5.SS4.p2; https://arxiv.org/html/2610.37584v1#S5.T2.
- **同期对比** · [APAO](apao.md): APAO-pointwise is a compared GR training objective; HCPD instead distills full conditional distributions over legal next tokens along observed target paths.
  - Source: REGER v1, Sections 4.3.2/5.1 and Table 2: https://arxiv.org/html/2610.37584v1#S4.SS3.SSS2.p4; https://arxiv.org/html/2610.37584v1#S5.SS1.p3; https://arxiv.org/html/2610.37584v1#S5.T2.
- **前序工作** · [Pctx](pctx.md): REGER follows Pctx in choosing DuoRec as its auxiliary recommender, but transfers collaborative preferences through distillation rather than personalized tokenization.
  - Source: REGER v1, Section 4.3.2: https://arxiv.org/html/2610.37584v1#S4.SS3.SSS2.p1.

[查看同格全部论文](../../README.md#i--training)
