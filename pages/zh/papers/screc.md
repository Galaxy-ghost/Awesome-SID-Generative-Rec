# SCRec

*Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation* — Dan · RecSys’26

`I. 信息量` · `Representation` · [论文](https://arxiv.org/abs/2609.13678) · [代码](https://github.com/DanJiayi/SCRec) · [矩阵](../../../README.zh.md#i--representation) · [English](../../papers/screc.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+CF"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Non-AR / Enc-Dec"] --> TR["Training<br/>Fixed / MTP + Ctr."] --> I["Inference<br/>Scoring / Beam†"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class R main
```

- `Non-AR / Enc-Dec`: Non-autoregressive and encoder–decoder backbone variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP + Ctr.`: MTP plus a contrastive loss.
- `Scoring / Beam†`: Discriminative candidate scoring vs. generative beam search.

### TL;DR

> [!NOTE]
> SCRec 将文本化的协同信号注入语义编号，在生成时用可学习码嵌入校准语义先验，并对齐码本与语义空间以耦合两个阶段。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | SCRec 将文本化的协同信号注入语义编号，在生成时用可学习码嵌入校准语义先验，并对齐码本与语义空间以耦合两个阶段。 |
| 主要改动阶段 | Representation |

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews Beauty, Sports and Outdoors, Toys and Games. Filtering and maximum history length not reported directly; preprocessing settings delegated to RPG.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2609.13678v1#S4.SS1.p1) ; #S4.SS1.p5
- **切分**：Per-user chronological leave-last-out: final interaction test, penultimate validation, remaining interactions training; shared across baselines.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2609.13678v1#S4.SS1.p1)
- **候选集**：not reported; evaluation configurations are delegated to RPG without specifying the candidate universe or negative sampling.
  - 出处：[S4.SS1.p4](https://arxiv.org/html/2609.13678v1#S4.SS1.p4) ; #S4.SS1.p5
- **可见性**：warm; no unseen-item protocol is defined. SASRec for top-10 collaborative neighbors is pretrained on training data; tokenizer fitting exposure to test items not reported.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2609.13678v1#S4.SS1.p1) ; #S4.SS1.p5
- **SID 规格**：RQ-VAE with 256 entries/codebook and latent dimension 256, quantizing fused item-text and textualized-neighbor embeddings. Semantic level count and collision handling not reported.
  - 出处：[S3.SS1.p9](https://arxiv.org/html/2609.13678v1#S3.SS1.p9) ; #S4.SS1.p5
- **推理预算**：Main decoder-only backbone follows RPG, with TIGER/LIGER module variants. Exact main inference procedure, prediction-head structure and beam width not reported; Recall/NDCG@5/10. General experiment GPU: one RTX 4090; inference batch size and absolute latency not reported. Beauty module inference-time increases: TIGER 6.19%, LIGER 0.54%, averaged over ten runs.
  - 出处：[S3.SS2.p5](https://arxiv.org/html/2609.13678v1#S3.SS2.p5) ; #S4.SS1.p4 ; #S4.SS1.p5 ; #S4.SS5.p1 ; #S4.SS5.p2
- **结果来源**：Original Table 1: main comparison; baselines including RPG rerun in the same environment, TIGER/LIGER evaluated through the same LIGER codebase. Table 2: ablations; Table 3: backbone extensions; Tables 4-5: alternative fusion/alignment. No imported baseline results stated.
  - 出处：[S4.T1](https://arxiv.org/html/2609.13678v1#S4.T1) ; #S4.T2 ; #S4.T3 ; #S4.T4 ; #S4.T5 ; #S4.SS1.p5

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["SCRec"]
    P -->|predecessor| A["RPG"]
    P -->|predecessor| B["TIGER"]
    P -->|predecessor| C["LIGER"]
```

- **前序工作** · [RPG](rpg.md): SCRec adopts a decoder-only backbone following RPG but replaces tokenization with collaborative-enhanced RQ-VAE and adds semantic/manifold alignment modules.
  - 出处：SCRec v1, Sections 3.1/4.1: https://arxiv.org/html/2609.13678v1#S3.SS1.p9; https://arxiv.org/html/2609.13678v1#S4.SS1.p5.
- **前序工作** · [TIGER](tiger.md): SCRec is also added to TIGER as a reusable module, improving collaborative input to tokenization and semantic guidance during generation.
  - 出处：SCRec v1, Section 4.5 and Table 3: https://arxiv.org/html/2609.13678v1#S4.SS5.p1; https://arxiv.org/html/2609.13678v1#S4.T3.
- **前序工作** · [LIGER](liger.md): SCRec augments the hybrid LIGER backbone with the same reusable cross-stage supplementation module and measures its inference overhead.
  - 出处：SCRec v1, Section 4.5 and Table 3: https://arxiv.org/html/2609.13678v1#S4.SS5.p1; https://arxiv.org/html/2609.13678v1#S4.SS5.p2; https://arxiv.org/html/2609.13678v1#S4.T3.

[查看同格全部论文](../../../README.zh.md#i--representation)
