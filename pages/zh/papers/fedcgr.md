# FedCGR

[← 问题 × 阶段矩阵](../../../README.zh.md#vi--backbone) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/fedcgr.md) | 中文

| **题目** | *Federated Cross-Domain Generative Recommendation* |
| :-- | :-- |
| **作者** | Liu et al. |
| **发表** | CIKM’26 |
| **问题与阶段** | `VI. 泛化` · `生成骨干（Backbone）` |
| **改动** | ● 生成骨干 · ○ 训练目标 |
| **构码输入** | `Text` |
| **领域** | `电商` |
| **特殊设置** | `跨域迁移` |
| **应用场景** | `一般物品推荐`；`公开数据` |
| **链接** | [论文](https://arxiv.org/abs/2608.10929) · [代码](https://github.com/ZhuodLiu/FedCGR) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text"] --> T["构码 Tokenization<br/>RQ-VAE"] --> B["生成骨干 Backbone<br/>● Enc-Dec"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ○ NTP + Aux."] --> I["推理 Inference<br/>C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `RQ-VAE`：残差量化变分自编码器（Residual-Quantized VAE）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP + Aux.`：下一 token 预测结合辅助正则或对齐损失。
- `C-Beam`：受合法物品集合约束的束搜索（Constrained beam search）。

### TL;DR

> [!NOTE]
> FedCGR 在基于公开元数据构建的共享 SID 上做联邦跨域推荐，注入本地协同证据并按域相关性聚合参数，无需交换私有交互数据。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Review: Grocery, Beauty, Sports, Food, Kitchen; six cross-domain scenarios FK/GB/GS/FKB/GBS/GKBS; per-domain 5-core filtering.
  - 出处：Section 4.1.1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS1.p1) and [S4.SS1.SSS1.p3](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS1.p3)
- **切分**：Per-user leave-one-out: last item test, second-to-last validation, remaining interactions training.
  - 出处：Section 4.1.3: [S4.SS1.SSS3.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS3.p1)
- **候选集**：full catalog; additionally sampled: 999 random negatives per user, fixed once and shared across methods (seed42). Negative-sampling distribution beyond random and history-item exclusion: not reported.
  - 出处：Section 4.1.3: [S4.SS1.SSS3.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS3.p1)
- **可见性**：warm; no unseen-item protocol is defined. Cold-start analysis groups users by training-history length (<=7, 8-15, >=16), not unseen items. SID metadata pretraining excludes private interactions; local CF uses client interaction sequences. Item-level generator/tokenizer/CF exposure: not reported.
  - 出处：Sections 3.1 and 4.4: [S3.SS1.p1](https://arxiv.org/html/2608.10929v1#S3.SS1.p1) and [S4.SS4.p1](https://arxiv.org/html/2608.10929v1#S4.SS4.p1)
- **SID 规格**：Frozen metadata RQ-VAE: 3 levels x 256 codes; colliding items share SID scores, ties broken by validation-set item popularity.
  - 出处：Sections 3.2 and 4.1.4: [S3.SS2.p2](https://arxiv.org/html/2608.10929v1#S3.SS2.p2) and [S4.SS1.SSS4.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS4.p1)
- **推理预算**：Target-domain trie-constrained beam 50; H/NDCG@10; experiments on RTX 4090 GPUs. Inference batch size and latency: not reported.
  - 出处：Sections 3.4 and 4.1.4: [S3.SS4.p2](https://arxiv.org/html/2608.10929v1#S3.SS4.p2) and [S4.SS1.SSS4.p1](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS4.p1)
- **结果来源**：Original Tables 3/4: full-ranking/sampled comparisons; Table 5: ablation; Table 6: diagnostics; Figures 3-5: user activity, sensitivity, communication efficiency.
  - 出处：Tables 3-6 and Figures 3-5: [S4.T3](https://arxiv.org/html/2608.10929v1#S4.T3) and [S4.T4](https://arxiv.org/html/2608.10929v1#S4.T4) and [S4.T5](https://arxiv.org/html/2608.10929v1#S4.T5) and [S4.T6](https://arxiv.org/html/2608.10929v1#S4.T6) and [S4.F3](https://arxiv.org/html/2608.10929v1#S4.F3) and [S4.F4](https://arxiv.org/html/2608.10929v1#S4.F4) and [S4.F5](https://arxiv.org/html/2608.10929v1#S4.F5)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["FedCGR"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"替代方案"| B["GenCDR"]
    P -->|"前序工作"| C["VQ-Rec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **同期对比** · [TIGER](tiger.md): TIGER and its FedAvg/FedProx variants are full-ranking baselines.
  - 出处：FedCGR v1, Section 4.1.2 and Table 3: [S4.SS1.SSS2.p2](https://arxiv.org/html/2608.10929v1#S4.SS1.SSS2.p2); [S4.T3](https://arxiv.org/html/2608.10929v1#S4.T3).
- **替代方案** · [GenCDR](gencdr.md): GenCDR uses centralized semantic CDR; FedCGR keeps interactions local.
  - 出处：FedCGR v1, Section 5: [S5.p1](https://arxiv.org/html/2608.10929v1#S5.p1); [S5.p2](https://arxiv.org/html/2608.10929v1#S5.p2).
- **前序工作** · [VQ-Rec](vq-rec.md): Related work identifies VQ-Rec as an earlier transferable quantized-item representation method.
  - 出处：FedCGR v1, Section 5: [S5.p2](https://arxiv.org/html/2608.10929v1#S5.p2).

[查看同格全部论文](../../../README.zh.md#vi--backbone)
