# PSRQ

*Progressive Semantic Residual Quantization for Multimodal-Joint Interest Modeling in Music Recommendation* — Wang et al. · CIKM’25

`I. 信息量` · `Tokenization` · [论文](https://arxiv.org/abs/2508.20359) · [矩阵](../../../README.zh.md#i--tokenization) · [English](../../papers/psrq.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+Img"] --> T["Tokenization<br/>Prog. RQ"] --> B["Backbone<br/>Encoder"] --> TR["Training<br/>Fixed / Discrim."] --> I["Inference<br/>Scoring"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `Prog. RQ`: Progressive RQ variant.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Discrim.`: Scores items; does not generate SIDs.

### TL;DR

> [!NOTE]
> PSRQ 生成保留前缀语义特征的模态特定与模态联合 SID，并用多码本交叉注意力建模音乐兴趣，减轻残差量化中的语义漂移。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | PSRQ 生成保留前缀语义特征的模态特定与模态联合 SID，并用多码本交叉注意力建模音乐兴趣，减轻残差量化中的语义漂移。 |
| 主要改动阶段 | Tokenization |

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Baby (81,423 users / 33,652 items; ratings of 4 or more are positives), an industrial music-streaming dataset from one week of logs (4,926,656 users / 1,387,247 songs; collections are positives, played-but-not-collected are negatives), and Music4all (14,127 users / 99,596 songs; repeated plays are positives). Items with fewer than 30 interactions are marked cold-start. Further filtering: not reported.
  - 出处：Datasets and labels: [S5.SS1.SSS1.p1](https://arxiv.org/html/2508.20359v1#S5.SS1.SSS1.p1), [S5.I2.i1.p1](https://arxiv.org/html/2508.20359v1#S5.I2.i1.p1), [S5.I2.i2.p1](https://arxiv.org/html/2508.20359v1#S5.I2.i2.p1), [S5.I2.i3.p1](https://arxiv.org/html/2508.20359v1#S5.I2.i3.p1); statistics: [S5.T1](https://arxiv.org/html/2508.20359v1#S5.T1).
- **切分**：not reported (sequences are built by timestamp and trained for one epoch, but the train/test division is not described). Online: A/B test in February 2025 on the music platform against a DLRM ranker.
  - 出处：Timestamp-ordered sequences, no split rule: [S5.I2.i1.p1](https://arxiv.org/html/2508.20359v1#S5.I2.i1.p1) and [S5.SS1.SSS2.p1](https://arxiv.org/html/2508.20359v1#S5.SS1.SSS2.p1); online test: [S5.SS3.p1](https://arxiv.org/html/2508.20359v1#S5.SS3.p1).
- **候选集**：n/a for ranking candidates: evaluation is pointwise AUC and Logloss on labeled positive and negative samples; how negatives relate to user history is defined by the labels above.
  - 出处：Pointwise AUC on labeled samples: [S5.SS1.SSS3.p1](https://arxiv.org/html/2508.20359v1#S5.SS1.SSS3.p1).
- **可见性**：warm; no unseen-item protocol is defined. 'Cold AUC' covers items with fewer than 30 interactions, which are low-frequency, not unseen.
  - 出处：Cold-start = fewer than 30 interactions, not unseen: [S5.SS1.SSS1.p1](https://arxiv.org/html/2508.20359v1#S5.SS1.SSS1.p1).
- **SID 规格**：Progressive Semantic Residual Quantization (PSRQ): layer-wise K-means over modality embeddings (text, image or audio) that preserves the prefix semantic feature, producing modal-specific and modal-joint semantic IDs; clusters per layer k = 64 (Amazon Baby), 256 (Industrial), 128 (Music4all), 3 layers. Collision handling: not reported.
  - 出处：Clusters k and layers l per dataset: [S5.SS1.SSS2.p1](https://arxiv.org/html/2508.20359v1#S5.SS1.SSS2.p1); PSRQ name and modal-specific/modal-joint IDs: [abstract1](https://arxiv.org/html/2508.20359v1#abstract1) and [S4.SS1.p1](https://arxiv.org/html/2508.20359v1#S4.SS1.p1).
- **推理预算**：n/a for generation (SIDs feed a DIN-style ranker with cross-attention, MCCA). MLLM feature extractors run on NVIDIA A100 GPUs; ranker inference batch size and latency: not reported.
  - 出处：Discriminative ranker, hardware for feature extraction: [S5.SS1.SSS2.p1](https://arxiv.org/html/2508.20359v1#S5.SS1.SSS2.p1).
- **结果来源**：Table 2 (All AUC, Cold AUC, Logloss versus multimodal and quantization-based rankers); Table 3 (quantizers added to DIN with text only); Table 4 (MCCA ablation); Section 5.3 (online A/B: collect +2.81%, full play +0.95%).
  - 出处：Main: [S5.T2](https://arxiv.org/html/2508.20359v1#S5.T2); quantizers in DIN: [S5.T3](https://arxiv.org/html/2508.20359v1#S5.T3); ablation: [S5.T4](https://arxiv.org/html/2508.20359v1#S5.T4); online: [S5.SS3.p1](https://arxiv.org/html/2508.20359v1#S5.SS3.p1).

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["PSRQ"]
    P -->|alternative| A["TIGER"]
    P -->|alternative| B["VQ-Rec"]
    P -->|alternative| C["OneRec"]
```

- **替代方案** · [TIGER](tiger.md): TIGER introduced RQ-VAE semantic IDs for generative retrieval; PSRQ quantizes multimodal embeddings with progressive semantic residual K-means and uses the IDs as ranking features for cold-start items.
  - 出处：PSRQ v1, Section 1 and Section 2.2 cite Rajput et al. (2023): https://arxiv.org/html/2508.20359v1#S1.p3 and https://arxiv.org/html/2508.20359v1#S2.SS2.p1; RQ-VAE is a quantizer baseline in Table 3: https://arxiv.org/html/2508.20359v1#S5.T3.
- **替代方案** · [VQ-Rec](vq-rec.md): VQ-Rec framed vector quantization for transferable recommenders; PSRQ adds modal-specific and modal-joint codebooks for multimodal cold-start ranking.
  - 出处：PSRQ v1, Section 1 and Section 2.2: https://arxiv.org/html/2508.20359v1#S1.p3 and https://arxiv.org/html/2508.20359v1#S2.SS2.p1.
- **替代方案** · [OneRec](onerec.md): OneRec uses residual K-means SIDs inside an end-to-end generator; PSRQ keeps a discriminative ranker and feeds it multimodal SID embeddings.
  - 出处：PSRQ v1, contribution list and Section 2.2 cite OneRec: https://arxiv.org/html/2508.20359v1#S1.I1.i2.p1 and https://arxiv.org/html/2508.20359v1#S2.SS2.p1.

[查看同格全部论文](../../../README.zh.md#i--tokenization)
