# MDGR

[← 问题 × 阶段矩阵](../../../README.zh.md#iii--backbone) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/mdgr.md) | 中文

| **题目** | *Masked Diffusion Generative Recommendation* |
| :-- | :-- |
| **作者** | Mu et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `III. SID 与模型对齐` · `生成骨干（Backbone）` |
| **改动** | ● 生成骨干 · ○ 训练目标 · ○ 推理 |
| **构码输入** | `Text` |
| **领域** | `电商` |
| **应用场景** | `一般物品推荐`；`线上实验或部署` |
| **链接** | [论文](https://arxiv.org/abs/2601.19501) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>–"] --> T["构码 Tokenization<br/>Par. OPQ"] --> B["生成骨干 Backbone<br/>● Non-AR"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ○ Masked"] --> I["推理 Inference<br/>○ Diff.+Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR,I other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Par. OPQ`：并行优化乘积量化，生成无序多子空间码。
- `Non-AR`：非自回归（Non-autoregressive）并行预测架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `Masked`：掩码部分码位并重构（含离散掩码扩散目标）。
- `Diff.+Beam`：离散扩散解码结合束搜索。

### TL;DR

> [!NOTE]
> MDGR 采用并行码本、沿时间步与样本自适应的掩码策略以及预热两阶段并行解码做掩码扩散推荐，替代固定顺序的自回归 SID 解码。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Electronics/Books: remove users with fewer than five interactions, maximum history 20. Industrial Southeast Asian e-commerce logs: May-December 2025, >1B interactions, 18M users, 25M items, mean history 128; industrial filtering not reported.
  - 出处：[S5.SS1.SSS1.p1](https://arxiv.org/html/2601.19501v1#S5.SS1.SSS1.p1)
- **切分**：Sliding-window next-item training; chronological leave-one-out: latest interaction test, penultimate validation, remainder training. Online A/B: January 5-12, 2026, control/treatment each 20% uniformly sampled users.
  - 出处：[S5.SS1.SSS1.p1](https://arxiv.org/html/2601.19501v1#S5.SS1.SSS1.p1) ; #S5.SS6.p1
- **候选集**：not reported
  - 出处：Section 5.1 gives metrics but no evaluation universe or negative-sampling protocol: [S5.SS1](https://arxiv.org/html/2601.19501v1#S5.SS1)
- **可见性**：warm; no unseen-item protocol is defined. Tokenizer fitting exposure to test items not reported.
  - 出处：[S5.SS1.SSS1.p1](https://arxiv.org/html/2601.19501v1#S5.SS1.SSS1.p1) ; #S5.SS1.SSS3.p1
- **SID 规格**：OPQ-based parallel codebooks: 8 x 300, 256-dimensional code vectors, using Qwen3-8B content embeddings. Complete SIDs map to item sets through an offline index; collision disambiguation not reported.
  - 出处：[S4.SS2](https://arxiv.org/html/2601.19501v1#S4.SS2) ; #S5.SS1.SSS3.p1
- **推理预算**：Beam 50; four single-position warm-up steps, then two positions/step. Table 3 reports six total steps and 2.527 QPS versus 2.212 for eight serial steps; implementation text inconsistently says four subsequent parallel steps. Recall/NDCG@5/10; inference-specific hardware, batch size and latency not reported.
  - 出处：[S5.SS1.SSS3.p1](https://arxiv.org/html/2601.19501v1#S5.SS1.SSS3.p1) ; #S5.T3 ; #S5.SS3.SSS2.p2
- **结果来源**：Original Table 2: offline three-dataset comparison; baseline-result reuse not stated. Table 3: industrial efficiency; Table 4: industrial ablations; Section 5.6: online A/B against production TIGER.
  - 出处：[S4.T2](https://arxiv.org/html/2601.19501v1#S4.T2) ; #S5.T3 ; #S5.T4 ; #S5.SS6.p1

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["MDGR"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"同期对比"| B["RPG"]
    P -->|"同期对比"| C["COBRA"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **同期对比** · [TIGER](tiger.md): TIGER generates residual-quantized IDs autoregressively; MDGR denoises parallel-codebook IDs and is also tested against production TIGER online.
  - 出处：MDGR v1, Sections 5.1.2/5.6 and Table 2: [S5.SS1.SSS2.p1](https://arxiv.org/html/2601.19501v1#S5.SS1.SSS2.p1); [S5.SS6.p1](https://arxiv.org/html/2601.19501v1#S5.SS6.p1); [S4.T2](https://arxiv.org/html/2601.19501v1#S4.T2).
- **同期对比** · [RPG](rpg.md): RPG uses multi-token prediction and graph-constrained parallel decoding; MDGR uses masked denoising with confidence-guided position scheduling.
  - 出处：MDGR v1, Sections 4.4/5.1.2 and Table 2: [S4.SS4](https://arxiv.org/html/2601.19501v1#S4.SS4); [S5.SS1.SSS2.p1](https://arxiv.org/html/2601.19501v1#S5.SS1.SSS2.p1); [S4.T2](https://arxiv.org/html/2601.19501v1#S4.T2).
- **同期对比** · [COBRA](cobra.md): COBRA supplements sparse IDs with dense vectors; MDGR instead changes discrete-ID supervision and decoding through masked diffusion.
  - 出处：MDGR v1, Sections 2.1/5.1.2 and Table 2: [S2.SS1.p1](https://arxiv.org/html/2601.19501v1#S2.SS1.p1); [S5.SS1.SSS2.p1](https://arxiv.org/html/2601.19501v1#S5.SS1.SSS2.p1); [S4.T2](https://arxiv.org/html/2601.19501v1#S4.T2).

[查看同格全部论文](../../../README.zh.md#iii--backbone)
