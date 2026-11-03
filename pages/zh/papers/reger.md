# REGER

[← 问题 × 阶段矩阵](../../../README.zh.md#i--training) · [按阶段索引](../index/stages.md) · [按模态索引](../index/modality.md) · [English](../../papers/reger.md) | 中文

| **题目** | *Modeling inter-item Relations with Semantic IDs for Generative Recommendation* |
| :-- | :-- |
| **作者** | Huang et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `I. 信息量` · `训练（Training）` |
| **链接** | [论文](https://arxiv.org/abs/2610.37584) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["表征 Representation<br/>Text"] --> T["编号 Tokenization<br/>RQ-VAE"] --> B["骨干 Backbone<br/>Enc-Dec"] --> TR["训练 Training<br/>Fixed / NTP → (NTP + Aux.)"] --> I["推理 Inference<br/>Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP → (NTP + Aux.)`：先进行下一 token 预测预训练，再联合优化下一 token 预测与辅助目标。
- `Beam`：在 SID token 上执行自回归束搜索（Beam search）。

### TL;DR

> [!NOTE]
> REGER 预训练生成器以产出语义近邻的 SID，结合全局与 ID 边界局部注意力，并沿目标前缀路径蒸馏判别式教师的下一 token 分布。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：SID 或读取它的模型是否充分携带了推荐所需的协同、多模态与时空信号？ |
| 核心贡献 | REGER 预训练生成器以产出语义近邻的 SID，结合全局与 ID 边界局部注意力，并沿目标前缀路径蒸馏判别式教师的下一 token 分布。 |
| 主要改动阶段 | 训练（Training） |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews 2014 Beauty/Sports/Toys and 2023 Instruments/Scientific/Games; 5-core filtering and maximum history 20 items.
  - 出处：[S5.SS1.p1](https://arxiv.org/html/2610.37584v1#S5.SS1.p1) ; #A1.T6
- **切分**：Per-user chronological leave-one-out: latest interaction test, second latest validation, all earlier interactions training.
  - 出处：[A1.SS1.p1](https://arxiv.org/html/2610.37584v1#A1.SS1.p1)
- **候选集**：not reported
  - 出处：Evaluation settings give metrics and seeds but no evaluation universe: [S5.SS1](https://arxiv.org/html/2610.37584v1#S5.SS1) ; #A1.SS1
- **可见性**：warm; no unseen-item protocol is defined. GSR semantic neighbors are drawn from the item catalog; tokenizer and frozen DuoRec teacher exposure to test items/interactions not explicitly separated.
  - 出处：[S5.SS1.p1](https://arxiv.org/html/2610.37584v1#S5.SS1.p1) ; #S4.SS1.p3 ; #S4.SS3.SSS2.p1 ; #A1.SS3.p1
- **SID 规格**：RQ-VAE on Sentence-T5 embeddings reduced to 128 dimensions by PCA/whitening; semantic level count and codebook sizes not reported in paper. Extra token distinguishes identical semantic codes; suffix vocabulary size/assignment not reported. Dataset-specific SID mapping shared across recommender seeds.
  - 出处：[S3.SS1.p1](https://arxiv.org/html/2610.37584v1#S3.SS1.p1) ; #A1.SS3.p1
- **推理预算**：Unconstrained beam 20 for validation/test, without teacher; teacher ablation uses beam 50. Recall/NDCG@5/10. Table 4 efficiency probe on TIGER+HCPD: one L40, FP32, test batch 256, KV cache off, 16 s for full Beauty test set. REGER-specific absolute inference time and general inference batch/hardware not reported.
  - 出处：[A1.SS3.p2](https://arxiv.org/html/2610.37584v1#A1.SS3.p2) ; #A1.SS3.p4 ; #A1.T7 ; #S5.T4 ; #S5.SS4.p3
- **结果来源**：Table 1: 2014 comparisons with reproduced baselines, three seeds 2024/2025/2026; Table 2: training objectives on TIGER; Table 3: REGER ablations. Table 6: 2023 results, with published baseline rows from Latte, OMEGA, DECOR and TopoTok papers.
  - 出处：[S4.T1](https://arxiv.org/html/2610.37584v1#S4.T1) ; #S5.T2 ; #S5.T3 ; #A1.T6 ; #A1.SS3.p2

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["REGER"]
    P -->|"前序工作"| A["TIGER"]
    P -->|"同期对比"| B["GFlowGR"]
    P -->|"同期对比"| C["APAO"]
    P -->|"前序工作"| D["Pctx"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D peer
```

- **前序工作** · [TIGER](tiger.md): REGER uses residual-quantized SID generation and additionally tests its HCPD training objective directly on TIGER.
  - 出处：REGER v1, Section 3.1 and Table 2: [S3.SS1.p1](https://arxiv.org/html/2610.37584v1#S3.SS1.p1); [S5.T2](https://arxiv.org/html/2610.37584v1#S5.T2).
- **同期对比** · [GFlowGR](gflowgr.md): GFlowGR supervises generation with collaborative rewards and flow balance; HCPD directly matches teacher conditional preferences over legal prefix branches, using the same DuoRec teacher.
  - 出处：REGER v1, Section 5.4 and Table 2: [S5.SS4.p2](https://arxiv.org/html/2610.37584v1#S5.SS4.p2); [S5.T2](https://arxiv.org/html/2610.37584v1#S5.T2).
- **同期对比** · [APAO](apao.md): APAO-pointwise is a compared GR training objective; HCPD instead distills full conditional distributions over legal next tokens along observed target paths.
  - 出处：REGER v1, Sections 4.3.2/5.1 and Table 2: [S4.SS3.SSS2.p4](https://arxiv.org/html/2610.37584v1#S4.SS3.SSS2.p4); [S5.SS1.p3](https://arxiv.org/html/2610.37584v1#S5.SS1.p3); [S5.T2](https://arxiv.org/html/2610.37584v1#S5.T2).
- **前序工作** · [Pctx](pctx.md): REGER follows Pctx in choosing DuoRec as its auxiliary recommender, but transfers collaborative preferences through distillation rather than personalized tokenization.
  - 出处：REGER v1, Section 4.3.2: [S4.SS3.SSS2.p1](https://arxiv.org/html/2610.37584v1#S4.SS3.SSS2.p1).

[查看同格全部论文](../../../README.zh.md#i--training)
