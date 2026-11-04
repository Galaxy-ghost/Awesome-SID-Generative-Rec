# COBRA

[← 问题 × 阶段矩阵](../../../README.zh.md#i--backbone) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/cobra.md) | 中文

| **题目** | *Sparse Meets Dense: Unified Generative Recommendations with Cascaded Sparse-Dense Representations* |
| :-- | :-- |
| **作者** | Yang et al. |
| **发表** | NeurIPS’25 |
| **问题与阶段** | `I. 信息量` · `生成骨干（Backbone）` |
| **改动** | ○ 物品表示 · ● 生成骨干 · ○ 训练目标 · ○ 推理 |
| **构码输入** | `Text` |
| **领域** | `电商` · `广告` |
| **链接** | [论文](https://arxiv.org/abs/2503.02453) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>○ Text+SID"] --> T["构码 Tokenization<br/>Casc. RQ"] --> B["生成骨干 Backbone<br/>● Dec-Only"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ○ NTP + Dense"] --> I["推理 Inference<br/>○ BeamFusion"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class R,TR,I other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text+SID`：稠密文本表征拼接离散语义 ID（稠密与生成式混合检索）。
- `Casc. RQ`：稀疏到稠密级联残差量化。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP + Dense`：离散 SID 的下一 token 预测结合稠密向量回归/对比损失。
- `BeamFusion`：融合自回归 SID 束搜索得分与稠密最近邻检索得分的联合解码。

### TL;DR

> [!NOTE]
> COBRA 先生成稀疏 SID 再以它为条件生成稠密向量，端到端联合训练二者，并在解码时用 BeamFusion 融合束搜索分数与最近邻相似度。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Product Reviews (May 1996-September 2014): Beauty, Sports and Outdoors, Toys and Games, with 5-core filtering of users and items (users / items: 22,363 / 12,101; 35,598 / 18,357; 19,412 / 11,924). Industrial: Baidu advertising logs across list-page, dual-column, and short-video scenarios, about 5 million users and 2 million ads; filtering not reported.
  - 出处：Public categories, date range, 5-core filtering: [S4.SS1.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS1.p1); statistics: [S4.T1](https://arxiv.org/html/2503.02453v1#S4.T1); industrial data: [S4.SS2.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS2.SSS1.p1).
- **切分**：Public datasets: train/validation/test allocation not reported. Industrial: first 60 days of logs for training and the following day for testing. Online: A/B test in January 2025 with 10% of user traffic.
  - 出处：Public split not stated: [S4.SS1.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS1.p1); industrial 60-day train and next-day test: [S4.SS2.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS2.SSS1.p1); online A/B: [S4.SS4.p1](https://arxiv.org/html/2503.02453v1#S4.SS4.p1).
- **候选集**：not reported (full catalog versus sampled evaluation candidates); top-K lists are formed by ANN retrieval among items under the top-M generated sparse IDs, fused by BeamFusion. Public K=5 and 10; industrial K=50 to 800.
  - 出处：Retrieval combines beam search over sparse IDs with ANN over items under each ID: [S3.SS4.p2](https://arxiv.org/html/2503.02453v1#S3.SS4.p2) and [S3.SS4.p5](https://arxiv.org/html/2503.02453v1#S3.SS4.p5); evaluation metrics: [S4.SS1.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS1.p1).
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Standard public protocol and next-day industrial test, with no cold-start experiment: [S4.SS1.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS1.p1) and [S4.SS2.SSS1.p1](https://arxiv.org/html/2503.02453v1#S4.SS2.SSS1.p1).
- **SID 规格**：Public: 3-level semantic IDs with codebook size 32 per level, generated from T5 embeddings following TIGER's method. Industrial: 2-level 32 x 32 sparse IDs (the w/o Dense variant uses 3 levels of 256). Items under the same sparse ID are distinguished by a generated dense vector and ANN search within that ID's candidate set; a collision-resolution rule for the sparse IDs is not reported.
  - 出处：Public SID: [S4.SS1.SSS3.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS3.p1); industrial SID and the w/o Dense variant: [S4.SS2.SSS3.p1](https://arxiv.org/html/2503.02453v1#S4.SS2.SSS3.p1); items sharing a sparse ID are separated by the dense vector: [S3.SS4.p5](https://arxiv.org/html/2503.02453v1#S3.SS4.p5).
- **推理预算**：Beam search returns the top M sparse IDs, then ANN retrieves the top N items per ID and BeamFusion combines beam and cosine scores; numerical M and N are not reported. The recall-diversity analysis selects tau=0.9 with the second coefficient fixed at 16. Public model: 1-layer encoder and 2-layer decoder. Hardware, inference batch size, and latency: not reported.
  - 出处：Beam search top-M, ANN top-N, BeamFusion coefficients: [S3.SS4.p2](https://arxiv.org/html/2503.02453v1#S3.SS4.p2), [S3.SS4.p5](https://arxiv.org/html/2503.02453v1#S3.SS4.p5), [S3.SS4.p6](https://arxiv.org/html/2503.02453v1#S3.SS4.p6); tau setting: [S4.SS3.SSS2.p1](https://arxiv.org/html/2503.02453v1#S4.SS3.SSS2.p1); architecture: [S4.SS1.SSS3.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS3.p1).
- **结果来源**：Table 2 (Beauty, Sports, Toys); Table 3 (Baidu industrial Recall@50-800 with ablated variants); Section 4.4 (online A/B: +3.60% conversion, +4.15% ARPU); Figures 4-6 (embedding analysis and recall-diversity curves).
  - 出处：Public table: [S4.T2](https://arxiv.org/html/2503.02453v1#S4.T2); industrial variants: [S4.T3](https://arxiv.org/html/2503.02453v1#S4.T3); online: [S4.SS4.p1](https://arxiv.org/html/2503.02453v1#S4.SS4.p1); diversity curves: [S4.F6](https://arxiv.org/html/2503.02453v1#S4.F6).

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["COBRA"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"替代方案"| B["LIGER"]
    P -->|"替代方案"| C["CapsID"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **同期对比** · [TIGER](tiger.md): TIGER retrieves items from sparse semantic IDs alone; COBRA follows TIGER's SID construction but generates a dense vector after each sparse ID and fuses beam and ANN scores.
  - 出处：COBRA v1, baselines and SID setting: [S4.I1.i9.p1](https://arxiv.org/html/2503.02453v1#S4.I1.i9.p1) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2503.02453v1#S4.SS1.SSS3.p1); Table 2: [S4.T2](https://arxiv.org/html/2503.02453v1#S4.T2); the w/o Dense variant mirrors TIGER: [S4.I2.i2.p1](https://arxiv.org/html/2503.02453v1#S4.I2.i2.p1).
- **替代方案** · [LIGER](liger.md): LIGER (Yang et al., 2024) unifies generative and dense retrieval as a hybrid, while COBRA cascades sparse-ID generation and dense-vector generation inside one decoder.
  - 出处：COBRA v1, Section 1 cites Yang et al. (2024), Unifying Generative and Dense Retrieval, for the fine-grained similarity gap of generative methods: [S1.p3](https://arxiv.org/html/2503.02453v1#S1.p3); not a baseline in Table 2.
- **替代方案** · [CapsID](capsid.md): CapsID removes the dense patch and instead makes the SID soft-routed and variable-length, reporting about half of COBRA's per-query latency at similar Recall@100.
  - 出处：Evidence is from the later CapsID paper: COBRA is a patch-route baseline in Tables 3, 4, and 6: [S4.T3](https://arxiv.org/html/2605.05096v1#S4.T3), [S4.T4](https://arxiv.org/html/2605.05096v1#S4.T4), [S4.T6](https://arxiv.org/html/2605.05096v1#S4.T6); latency comparison: [S4.SS5.SSS0.Px5.p2](https://arxiv.org/html/2605.05096v1#S4.SS5.SSS0.Px5.p2).

[查看同格全部论文](../../../README.zh.md#i--backbone)
