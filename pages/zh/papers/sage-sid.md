# SAGE-SID

[← 问题 × 阶段矩阵](../../../README.zh.md#iv--training) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/sage-sid.md) | 中文

| **题目** | *SAGE: Sequence-level Adaptive Gradient Evolution for Generative Recommendation* |
| :-- | :-- |
| **作者** | Xie et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `IV. 实用目标` · `训练（Training）` |
| **改动** | ● 训练目标 |
| **构码输入** | `Text` + `Img` |
| **领域** | `电商` · `短视频与直播` · `广告` |
| **应用场景** | `一般物品推荐` · `对话与指令推荐` · `排序与重排`；`公开数据` |
| **链接** | [论文](https://arxiv.org/abs/2601.21452) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text+Img†"] --> T["构码 Tokenization<br/>R-KM†"] --> B["生成骨干 Backbone<br/>Dec-Only†"] --> TR["训练 Training<br/>编号器更新: Fixed†<br/>训练目标: ● NTP → RL"] --> I["推理 Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `Text+Img†`：文本与图像多模态表征（由配置推断）。
- `R-KM†`：残差 k-means 编号（由配置推断）。
- `Dec-Only†`：仅解码器自回归架构（由配置推断）。
- `Fixed†`：生成器训练期间冻结编号器（由配置推断）。
- `NTP → RL`：先进行下一 token 预测微调，再执行强化学习（如 GRPO、GBPO 等）。

### TL;DR

> [!NOTE]
> SAGE-SID 用几何平均序列比率、解耦的多目标优势、非对称自适应裁剪界与熵感知惩罚优化列表级生成器，替代 GBPO 的对称裁剪界。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews 2014 Sports/Beauty/Toys; RecIF-Bench: about 120M interactions, 200K users, Short Video/Ad/Product. Filtering not reported.
  - 出处：Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p1) and [S4.SS1.SSS1.p2](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p2)
- **切分**：RecIF: 20% users held out, per-user histories separated temporally from future targets. Amazon split and validation allocation not reported.
  - 出处：Section 4.1.1: [S4.SS1.SSS1.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p3)
- **候选集**：not reported for the SID branch
  - 出处：Section 4.1.4 identifies inherited SID evaluation settings but does not specify candidate enumeration: [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3)
- **可见性**：warm; no unseen-item protocol is defined. Amazon cold items are bottom 5% by training interaction frequency; RecIF holds out users, not explicitly items.
  - 出处：Sections 4.1.1/4.1.3: [S4.SS1.SSS1.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS1.p3) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p1)
- **SID 规格**：OneRec-SAGE uses Semantic IDs and OpenOneRec checkpoints/settings; SID length, codebook sizes and collision handling not reported here.
  - 出处：Sections 4.1.2/4.1.4: [S4.SS1.SSS2.p4](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p4) and [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3)
- **推理预算**：Reported slate length 10; Amazon Recall/NDCG@5/10; RecIF Pass/Recall@1/32 and label AUC. SID beam width, inference hardware, batch size and latency not reported.
  - 出处：Sections 4.1.3/4.1.4: [S4.SS1.SSS3.p1](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p1) and [S4.SS1.SSS3.p2](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS3.p2) and [S4.SS1.SSS4.p1](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p1) and [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3)
- **结果来源**：OneRec-SAGE rows in Tables 1/2 (Amazon) and 3/4 (RecIF). RecIF task-specific sequential and TIGER baseline numbers are reused from the benchmark; OneRec variants use public checkpoints/settings.
  - 出处：Tables 1-4 and Section 4.1.4: [S3.T1](https://arxiv.org/html/2601.21452v3#S3.T1) and [S3.T2](https://arxiv.org/html/2601.21452v3#S3.T2) and [S3.T3](https://arxiv.org/html/2601.21452v3#S3.T3) and [S4.T4](https://arxiv.org/html/2601.21452v3#S4.T4) and [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["SAGE-SID"]
    P -->|"前序工作"| A["OneRec-V2"]
    P -->|"同期对比"| B["LC-Rec"]
    P -->|"同期对比"| C["TIGER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **前序工作** · [OneRec-V2](onerec-v2.md): SAGE extends the GBPO optimizer evaluated as OneRec-GBPO.
  - 出处：SAGE v3, Sections 3.4.1/4.1.2: [S3.SS4.SSS1.p1](https://arxiv.org/html/2601.21452v3#S3.SS4.SSS1.p1); [S4.SS1.SSS2.p4](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p4).
- **同期对比** · [LC-Rec](lc-rec.md): Adapted to a Qwen3-8B backbone for the RecIF comparison.
  - 出处：SAGE v3, Section 4.1.2: [S4.SS1.SSS2.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS2.p3).
- **同期对比** · [TIGER](tiger.md): RecIF comparison reuses TIGER's reported benchmark numbers.
  - 出处：SAGE v3, Section 4.1.4: [S4.SS1.SSS4.p3](https://arxiv.org/html/2601.21452v3#S4.SS1.SSS4.p3).

[查看同格全部论文](../../../README.zh.md#iv--training)
