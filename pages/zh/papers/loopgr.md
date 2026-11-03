# LoopGR

[← 问题 × 阶段矩阵](../../../README.zh.md#v--backbone) · [按阶段索引](../index/stages.md) · [按模态索引](../index/modality.md) · [English](../../papers/loopgr.md) | 中文

| **题目** | *Parameter-Efficient Scaling for Generative Recommendation via Recurrent Depth* |
| :-- | :-- |
| **作者** | Zhang et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `V. 效率` · `骨干（Backbone）` |
| **链接** | [论文](https://arxiv.org/abs/2610.34157) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["表征 Representation<br/>Text"] --> T["编号 Tokenization<br/>RQ-VAE"] --> B["骨干 Backbone<br/>Enc-Dec"] --> TR["训练 Training<br/>Fixed / NTP / NTP + Aux."] --> I["推理 Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP / NTP + Aux.`：单独使用下一 token 预测，或与辅助损失联合优化。

### TL;DR

> [!NOTE]
> LoopGR 交替运行共享生成解码器与轻量上下文更新器以增加循环深度，并蒸馏出低开销学生模型，在不按比例扩大参数量的前提下扩展计算。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | V. 效率：训练与在线服务能否满足实际的延迟、显存与吞吐预算？ |
| 核心贡献 | LoopGR 交替运行共享生成解码器与轻量上下文更新器以增加循环深度，并蒸馏出低开销学生模型，在不按比例扩大参数量的前提下扩展计算。 |
| 主要改动阶段 | 骨干（Backbone） |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews 2014 Beauty, Sports and Outdoors, CDs and Vinyl; Tencent industrial data. Filtering and industrial dataset statistics not reported.
  - 出处：Section 5.1 and Appendix A.1: [S5.SS1.SSS0.Px1.p1](https://arxiv.org/html/2610.34157v1#S5.SS1.SSS0.Px1.p1) and [A1.SS1.p1](https://arxiv.org/html/2610.34157v1#A1.SS1.p1)
- **切分**：Interactions ordered chronologically; sliding-window next-item training. Train/validation/test allocation not reported.
  - 出处：Section 5.1: [S5.SS1.SSS0.Px1.p1](https://arxiv.org/html/2610.34157v1#S5.SS1.SSS0.Px1.p1)
- **候选集**：not reported
  - 出处：Evaluation protocol in Section 5.1 and Appendix A.1 does not specify candidate enumeration or sampling: [S5.SS1](https://arxiv.org/html/2610.34157v1#S5.SS1) and [A1.SS1](https://arxiv.org/html/2610.34157v1#A1.SS1)
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Section 5.1 and Appendix A.1 define no item-level cold-start experiment: [S5.SS1](https://arxiv.org/html/2610.34157v1#S5.SS1) and [A1.SS1](https://arxiv.org/html/2610.34157v1#A1.SS1)
- **SID 规格**：Sentence-T5 embeddings; 3 RQ-VAE digits plus fourth anti-collision digit for unique SIDs. Codebook sizes not reported.
  - 出处：Section 5.1: [S5.SS1.SSS0.Px3.p1](https://arxiv.org/html/2610.34157v1#S5.SS1.SSS0.Px3.p1)
- **推理预算**：Experiments on 4 NVIDIA H20 GPUs; beam width not reported. Public Recall/NDCG@5/10; industrial Recall@5/10/20/50/100. Table 6, batch 1: 16/8/4 cycles, 211.08/104.01/49.82ms, 17.408/8.415/3.918 GFLOPs.
  - 出处：Section 5.1, Table 2, and Appendix A.2/Table 6: [S5.SS1.SSS0.Px3.p1](https://arxiv.org/html/2610.34157v1#S5.SS1.SSS0.Px3.p1) and [S5.T2](https://arxiv.org/html/2610.34157v1#S5.T2) and [A1.SS2.p1](https://arxiv.org/html/2610.34157v1#A1.SS2.p1) and [A1.T6](https://arxiv.org/html/2610.34157v1#A1.T6)
- **结果来源**：Tables 1/2: public/industrial comparisons; Table 6: trajectory compression. Industrial baselines adapted by authors; public-baseline reproduction versus copied scores not reported.
  - 出处：Section 5.1 and Tables 1/2/6: [S5.SS1.SSS0.Px2.p1](https://arxiv.org/html/2610.34157v1#S5.SS1.SSS0.Px2.p1) and [S5.T1](https://arxiv.org/html/2610.34157v1#S5.T1) and [S5.T2](https://arxiv.org/html/2610.34157v1#S5.T2) and [A1.T6](https://arxiv.org/html/2610.34157v1#A1.T6)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["LoopGR"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"同期对比"| B["RPG"]
    P -->|"同期对比"| C["ActionPiece"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **同期对比** · [TIGER](tiger.md): Encoder-decoder baseline; LoopGR adds shared recurrent context refinement.
  - 出处：LoopGR v1, Section 5.1 and Tables 1/2: [S5.SS1.SSS0.Px2.p1](https://arxiv.org/html/2610.34157v1#S5.SS1.SSS0.Px2.p1); [S5.T1](https://arxiv.org/html/2610.34157v1#S5.T1); [S5.T2](https://arxiv.org/html/2610.34157v1#S5.T2).
- **同期对比** · [RPG](rpg.md): Parallel graph-guided decoding contrasts with LoopGR's recurrent RQ-VAE SID generation.
  - 出处：LoopGR v1, Section 5.2 and Table 1: [S5.SS2.p2](https://arxiv.org/html/2610.34157v1#S5.SS2.p2); [S5.T1](https://arxiv.org/html/2610.34157v1#S5.T1).
- **同期对比** · [ActionPiece](actionpiece.md): Context-dependent action tokens contrast with LoopGR's standard RQ-VAE identifiers.
  - 出处：LoopGR v1, Section 5.2 and Table 1: [S5.SS2.p2](https://arxiv.org/html/2610.34157v1#S5.SS2.p2); [S5.T1](https://arxiv.org/html/2610.34157v1#S5.T1).

[查看同格全部论文](../../../README.zh.md#v--backbone)
