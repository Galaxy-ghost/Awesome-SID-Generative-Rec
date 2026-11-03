# SST

[← 问题 × 阶段矩阵](../../../README.zh.md#iii--tokenization) · [按阶段索引](../index/stages.md) · [按模态索引](../index/modality.md) · [English](../../papers/sst.md) | 中文

| **题目** | *Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms to Semantic Subwords* |
| :-- | :-- |
| **作者** | Miao et al. |
| **发表** | CIKM’26 |
| **问题与阶段** | `III. SID 与模型对齐` · `编号（Tokenization）` |
| **链接** | [论文](https://arxiv.org/abs/2608.22734) · [代码](https://github.com/mxrcandy/Semantic-Subword-Tokenization) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["表征 Representation<br/>Text"] --> T["编号 Tokenization<br/>RQ+IST"] --> B["骨干 Backbone<br/>Enc-Dec"] --> TR["训练 Training<br/>Fixed / NTP"] --> I["推理 Inference<br/>C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `RQ+IST`：残差量化结合序列内子词合并（Item-level Subword Tokenization）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP`：标准下一 token 预测（Next-Token Prediction）交叉熵损失；基于预训练 LLM 的指令微调（SFT）亦归入此类。
- `C-Beam`：受合法物品集合约束的束搜索（Constrained beam search）。

### TL;DR

> [!NOTE]
> SST 将历史物品表示为由稳定相邻 SID token 合并而成的变长子词，同时保持目标侧定长解码，以减少编码器在单个物品内部的注意力开销。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | III. SID 与模型对齐：生成模型能否理解并推理离散 SID，编号器与生成器的优化目标是否一致？ |
| 核心贡献 | SST 将历史物品表示为由稳定相邻 SID token 合并而成的变长子词，同时保持目标侧定长解码，以减少编码器在单个物品内部的注意力开销。 |
| 主要改动阶段 | 编号（Tokenization） |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Beauty/Instruments and Yelp; user/item 5-core filtering, chronological histories capped at 20.
  - 出处：Section 3.1.1: [S3.SS1.SSS1.p1](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS1.p1)
- **切分**：Per-user last interaction test, penultimate validation, earlier interactions training.
  - 出处：Section 3.1.3: [S3.SS1.SSS3.p1](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS3.p1)
- **候选集**：full catalog; no sampled negatives.
  - 出处：Section 3.1.3: [S3.SS1.SSS3.p1](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS3.p1)
- **可见性**：warm; no unseen-item protocol is defined. Tokenizer/collaborative encoder exposure to test items not reported.
  - 出处：Section 3.1 defines no unseen-item holdout: [S3.SS1](https://arxiv.org/html/2608.22734v1#S3.SS1)
- **SID 规格**：Sentence-T5 text embeddings; TIGER-VAE, TIGER-KM or LETTER targets retain 4 levels x 256 codes. History-side IST adds semantic subwords (merge budget tuned 64-512). Collision handling not reported.
  - 出处：Section 3.1.4: [S3.SS1.SSS4.p2](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS4.p2)
- **推理预算**：Full-trie beam 20; Recall/NDCG@5/10. Hardware, inference batch size and standalone latency not reported; Table 3 wall time combines training, checkpoint loading and test evaluation.
  - 出处：Sections 3.1.4/3.5: [S3.SS1.SSS4.p3](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS4.p3) and [S3.SS5.p1](https://arxiv.org/html/2608.22734v1#S3.SS5.p1)
- **结果来源**：Original Table 1: SST on three backbones; SARQ/VSID re-adapted to history-only variable lengths while preserving fixed target decoding. Table 6 reports all tokenizer-criterion variants.
  - 出处：Table 1 and Section 3.1.2: [S3.T1](https://arxiv.org/html/2608.22734v1#S3.T1) and [S3.SS1.SSS2.p5](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS2.p5) and [A1.T6](https://arxiv.org/html/2608.22734v1#A1.T6)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["SST"]
    P -->|"前序工作"| A["TIGER"]
    P -->|"前序工作"| B["LETTER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B peer
```

- **前序工作** · [TIGER](tiger.md): SST compresses TIGER-VAE/TIGER-KM histories while retaining fixed-length target SIDs.
  - 出处：SST v1, Sections 3.1.2/3.1.4 and Table 1: [S3.SS1.SSS2.p2](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS2.p2); [S3.SS1.SSS4.p2](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS4.p2); [S3.T1](https://arxiv.org/html/2608.22734v1#S3.T1).
- **前序工作** · [LETTER](letter.md): LETTER is the collaborative-tokenization backbone used for the third SST configuration.
  - 出处：SST v1, Section 3.1.2 and Table 1: [S3.SS1.SSS2.p2](https://arxiv.org/html/2608.22734v1#S3.SS1.SSS2.p2); [S3.T1](https://arxiv.org/html/2608.22734v1#S3.T1).

[查看同格全部论文](../../../README.zh.md#iii--tokenization)
