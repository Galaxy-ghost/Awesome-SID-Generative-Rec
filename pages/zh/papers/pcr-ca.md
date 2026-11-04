# PCR-CA

[← 问题 × 阶段矩阵](../../../README.zh.md#i--tokenization) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/pcr-ca.md) | 中文

| **题目** | *Parallel Codebook Representations with Contrastive Alignment for Multiple-Category App Recommendation* |
| :-- | :-- |
| **作者** | Tan et al. |
| **发表** | KDD’26 |
| **问题与阶段** | `I. 信息量` · `构码（Tokenization）` |
| **改动** | ● 构码 · ○ 生成骨干 · ○ 编号器更新 · ○ 训练目标 |
| **构码输入** | `Text` + `CF` |
| **领域** | `应用商店` |
| **应用场景** | `排序与重排`；`线上实验或部署` |
| **链接** | [论文](https://arxiv.org/abs/2508.18166) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text+CF"] --> T["构码 Tokenization<br/>● PC-AE"] --> B["生成骨干 Backbone<br/>○ Disc."] --> TR["训练 Training<br/>编号器更新: ○ Joint<br/>训练目标: ○ Discrim."] --> I["推理 Inference<br/>Scoring"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class B,TR other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+CF`：文本表征结合协同过滤信号。
- `PC-AE`：并行码本自编码器（Parallel Codebook Auto-Encoder）。
- `Disc.`：对候选物品打分的判别式推荐骨干。
- `Joint`：推荐生成损失通过可微路径直接反传更新编号器。
- `Discrim.`：判别式候选物品打分损失，不直接生成 SID。
- `Scoring`：直接计算候选物品得分，不逐位生成 SID。

### TL;DR

> [!NOTE]
> PCR-CA 不同于层级 RQ-VAE，学习应用文本的并行码本表示，并通过对比学习将它与协同信号对齐，用于多类目应用的点击率预测。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Microsoft Store impression logs with click/install labels over several months; approximately 80K apps, click rate 6.148%; histories up to 50 interactions. Filtering rules not reported.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2508.18166v1#S4.SS1.p1)
- **切分**：Chronological: 340M training interactions and latest 10M validation samples. Table 2 calls evaluation the test set, but a separate test allocation is not reported. Online A/B lasts two weeks.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2508.18166v1#S4.SS1.p1) ; #S4.T2 ; #S4.T5
- **候选集**：n/a for logged-impression CTR/AUC evaluation; candidate pool for top-10 diversity analysis not reported.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2508.18166v1#S4.SS1.p1) ; #S4.SS1.p6 ; #S4.SS4.p2
- **可见性**：Cold-start validation naturally includes apps/users unseen in CTR training. Unseen by CTR predictor only: PC-AE pretraining iterates over all 80K apps; no generative decoder is used.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2508.18166v1#S4.SS1.p1) ; #S4.SS1.p4
- **SID 规格**：PC-AE: 4 parallel codebooks x 32 entries, 16-dimensional vectors, selecting/summing two nearest codes per book. Codebooks train jointly with CTR prediction after pretraining. Unique-ID collision resolution: n/a; codes supply predictive features.
  - 出处：[S3.SS2.p3](https://arxiv.org/html/2508.18166v1#S3.SS2.p3) ; #S3.SS2.p7 ; #S4.SS1.p2
- **推理预算**：Discriminative scoring; beam n/a; top-10 lists for diversity. Simulated throughput: 120K candidate items/s versus base 150K/s on the same unspecified server. Inference hardware, batch size and request latency not reported; offline text embedding costs 22 ms/new app.
  - 出处：[S4.SS4.p2](https://arxiv.org/html/2508.18166v1#S4.SS4.p2) ; #S4.SS4.p3 ; #S4.SS4.p4
- **结果来源**：Original Table 2: AUC by app-popularity bucket; Tables 3-4: ablations; Table 5: online A/B. SaviorRec is explicitly reimplemented; no baseline-result reuse stated.
  - 出处：[S4.T2](https://arxiv.org/html/2508.18166v1#S4.T2) ; #S4.T3 ; #S4.T4 ; #S4.T5 ; #S4.SS1.p2

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["PCR-CA"]
    P -->|"替代方案"| A["CoST"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A peer
```

- **替代方案** · [CoST](cost.md): CoST uses residual vector quantization; PCR-CA replaces its hierarchy with parallel codebooks for multiple-category app features and CTR prediction.
  - 出处：PCR-CA v1, Introduction and Section 2.2, citing Yongchao Zhu et al. (2024): [S1.p4](https://arxiv.org/html/2508.18166v1#S1.p4); [S2.SS2.p3](https://arxiv.org/html/2508.18166v1#S2.SS2.p3).

[查看同格全部论文](../../../README.zh.md#i--tokenization)
