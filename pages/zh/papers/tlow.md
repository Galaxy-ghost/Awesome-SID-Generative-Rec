# Tlow

*Flow-based Item Tokenizer for Recommendation* — Li et al. · CIKM’26 Applied

`I. 信息量` · `Tokenization` · [论文](https://arxiv.org/abs/2608.24176) · [代码](https://github.com/wjjln/Tlow) · [矩阵](../../../README.zh.md#i--tokenization) · [English](../../papers/tlow.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>Flow+PQ"] --> B["Backbone<br/>Non-AR"] --> TR["Training<br/>Fixed / MTP + Rel.MSE"] --> I["Inference<br/>Scoring"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `Flow+PQ`: Flow-based representation transformation followed by product quantization.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP + Rel.MSE`: Multi-token prediction jointly optimized with a mean-squared-error objective on relations.

### TL;DR

> [!NOTE]
> Tlow 在独立量化前用归一化流将语义嵌入映射到标准正态隐空间，并对齐码本与 token 嵌入空间，区别于 RQ-VAE 和 OPQ。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | Tlow 在独立量化前用归一化流将语义嵌入映射到标准正态隐空间，并对齐码本与 token 嵌入空间，区别于 RQ-VAE 和 OPQ。 |
| 主要改动阶段 | Tokenization |

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews Sports/Beauty/Toys/CDs; processed Cloth-Sports cross-domain data. WeChat picture/article logs for online multimodal retrieval. Filtering not reported.
  - 出处：Sections 3.1.1/3.6.1: [S3.SS1.SSS1.p1](https://arxiv.org/html/2608.24176v1#S3.SS1.SSS1.p1) and [S3.SS6.SSS1.p1](https://arxiv.org/html/2608.24176v1#S3.SS6.SSS1.p1)
- **切分**：Public: chronological last item test, penultimate validation, earlier interactions train. Online holdout protocol and A/B duration not reported; two weeks refers to model training.
  - 出处：Sections 3.1.1/3.6.2: [S3.SS1.SSS1.p2](https://arxiv.org/html/2608.24176v1#S3.SS1.SSS1.p2) and [S3.SS6.SSS2.p1](https://arxiv.org/html/2608.24176v1#S3.SS6.SSS2.p1)
- **候选集**：full catalog for offline ranking; historical-item exclusion not reported
  - 出处：Section 3.1.3: [S3.SS1.SSS3.p1](https://arxiv.org/html/2608.24176v1#S3.SS1.SSS3.p1)
- **可见性**：Offline: warm; no unseen-item protocol is defined. Cold analysis bins targets by training frequency. Online cold pictures are exposed on publication day; generator/tokenizer exclusion not reported. Tokenizer fits about 1M items, then encodes additional unseen items.
  - 出处：Sections 3.5/3.6.2/3.6.3: [S3.SS5.p1](https://arxiv.org/html/2608.24176v1#S3.SS5.p1) and [S3.SS6.SSS2.p1](https://arxiv.org/html/2608.24176v1#S3.SS6.SSS2.p1) and [S3.SS6.SSS3.p1](https://arxiv.org/html/2608.24176v1#S3.SS6.SSS3.p1)
- **SID 规格**：Flow plus independent PQ: C in {16,32,64,96,128}, 256 codes each; selected C per offline dataset not reported. Online: 16 x 256. Collision handling not reported.
  - 出处：Sections 3.1.4/3.6.2: [S3.SS1.SSS4.p1](https://arxiv.org/html/2608.24176v1#S3.SS1.SSS4.p1) and [S3.SS6.SSS2.p1](https://arxiv.org/html/2608.24176v1#S3.SS6.SSS2.p1)
- **推理预算**：Single-forward parallel token scoring, Recall/NDCG@5/10; temperature searched over 0.03/0.05/0.07. Recommendation hardware, batch size and latency not reported. Online tokenization of tens of millions of new items takes minutes on one unspecified GPU, not per-request serving time.
  - 出处：Sections 3.1.4/3.6.1/3.6.2: [S3.SS1.SSS4.p1](https://arxiv.org/html/2608.24176v1#S3.SS1.SSS4.p1) and [S3.SS6.SSS1.p1](https://arxiv.org/html/2608.24176v1#S3.SS6.SSS1.p1) and [S3.SS6.SSS2.p1](https://arxiv.org/html/2608.24176v1#S3.SS6.SSS2.p1)
- **结果来源**：Tables 2/4/5/6: general/cross-domain/multimodal/online results. General comparison reuses RPG-paper baseline scores and reruns RPG; main semantic embeddings are sentence-t5-base.
  - 出处：Section 3.1.4 and Tables 2/4/5/6: [S3.SS1.SSS4.p1](https://arxiv.org/html/2608.24176v1#S3.SS1.SSS4.p1) and [S3.T2](https://arxiv.org/html/2608.24176v1#S3.T2) and [S3.T4](https://arxiv.org/html/2608.24176v1#S3.T4) and [S3.T5](https://arxiv.org/html/2608.24176v1#S3.T5) and [S3.T6](https://arxiv.org/html/2608.24176v1#S3.T6)

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["Tlow"]
    P -->|predecessor| A["RPG"]
    P -->|competitor| B["TIGER"]
    P -->|competitor| C["ETEGRec"]
```

- **前序工作** · [RPG](rpg.md): Supplies the parallel prediction setup and the rerun controlled baseline.
  - 出处：Tlow v1, Section 3.1.4: https://arxiv.org/html/2608.24176v1#S3.SS1.SSS4.p1.
- **同期对比** · [TIGER](tiger.md): Autoregressive RQ-VAE comparator against independent flow-space tokenization.
  - 出处：Tlow v1, Introduction and Section 3.1.2: https://arxiv.org/html/2608.24176v1#S1.p2; https://arxiv.org/html/2608.24176v1#S3.SS1.SSS2.p1.
- **同期对比** · [ETEGRec](etegrec.md): Included tokenizer comparator; general baseline scores are reused from the RPG paper.
  - 出处：Tlow v1, Sections 3.1.2/3.1.4 and Table 2: https://arxiv.org/html/2608.24176v1#S3.SS1.SSS2.p1; https://arxiv.org/html/2608.24176v1#S3.SS1.SSS4.p1; https://arxiv.org/html/2608.24176v1#S3.T2.

[查看同格全部论文](../../../README.zh.md#i--tokenization)
