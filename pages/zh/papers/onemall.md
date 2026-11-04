# OneMall

[← 问题 × 阶段矩阵](../../../README.zh.md#范式系统与基准) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/onemall.md) | 中文

| **题目** | *One Architecture, More Scenarios -- End-to-End Generative Recommender Family at Kuaishou E-Commerce* |
| :-- | :-- |
| **作者** | Zhang et al. |
| **发表** | CIKM’26 |
| **问题与阶段** | `范式、系统与基准` · `无单一阶段` |
| **改动** | ○ 物品表示 · ○ 构码 · ○ 生成骨干 · ○ 训练目标 |
| **构码输入** | A: `Text` + `Img` + `CF` · B: `Text` + `Img` + `CF` · C: `CF` + `其他`（直播塔向量：商品编号与特征） |
| **领域** | `电商` |
| **应用场景** | `一般物品推荐`；`线上实验或部署` |
| **链接** | [论文](https://arxiv.org/abs/2601.21770) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>○ Text+Img+CF"] --> T["构码 Tokenization<br/>○ R-KM+FSQ"] --> B["生成骨干 Backbone<br/>○ Enc-Dec"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ○ (NTP + Ctr.) → RL"] --> I["推理 Inference<br/>Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class R,T,B,TR other
```

- `Text+Img+CF`：文本、图像表征结合协同过滤信号。
- `R-KM+FSQ`：残差 k-means 结合有限标量量化（FSQ）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `(NTP + Ctr.) → RL`：先联合训练下一 token 预测与对比损失，再执行强化学习后训练。
- `Beam`：在 SID token 上执行自回归束搜索（Beam search）。

### TL;DR

> [!NOTE]
> OneMall 用业务感知编号器、Query-Former、稀疏 MoE 层以及作为强化学习奖励的排序模型，在单一生成器中统一商品卡、短视频与直播电商。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Kuaishou product-card, short-video, and live-streaming logs; dates/sample counts not reported. Tokenizer: 70M product-product pairs (<=40 occurrences/item), 12M video-product pairs from long views 1-5 minutes before product clicks, excluding News/Comedy/Dance/Film-TV/Selfie videos and downsampling frequent products/same-user pairs.
  - 出处：Sections 3.1.1 and 4: [S3.SS1.SSS1.p1](https://arxiv.org/html/2601.21770v1#S3.SS1.SSS1.p1) and [S4.p1](https://arxiv.org/html/2601.21770v1#S4.p1)
- **切分**：Offline train/validation/test allocation not reported; simulation replays online requests. Online A/B duration and traffic allocation not reported.
  - 出处：Sections 4.2/4.3 describe replay and online tests, not a data split: [S4.SS2.p1](https://arxiv.org/html/2601.21770v1#S4.SS2.p1) and [S4.SS3.p1](https://arxiv.org/html/2601.21770v1#S4.SS3.p1)
- **候选集**：not reported
  - 出处：Section 4 evaluates generated top-K retrieval, without full-catalog/sampled-negative specification: [S4.p1](https://arxiv.org/html/2601.21770v1#S4.p1)
- **可见性**：warm; no unseen-item protocol is defined. Frozen codebooks can tokenize new uploads; encoder/tokenizer exposure to test items not reported.
  - 出处：Sections 2.2/4 define no unseen-item evaluation protocol: [S2.SS2.p1](https://arxiv.org/html/2601.21770v1#S2.SS2.p1) and [S4](https://arxiv.org/html/2601.21770v1#S4)
- **SID 规格**：Two Res-Kmeans levels plus a 4096-code FSQ final level; residual-only baseline uses 3x4096. Final variant's residual codebook sizes not separately stated. FSQ reduces collisions; residual collision resolution not reported.
  - 出处：Sections 3.1.3/4.5: [S3.SS1.SSS3.p1](https://arxiv.org/html/2601.21770v1#S3.SS1.SSS3.p1) and [S4.SS5.p1](https://arxiv.org/html/2601.21770v1#S4.SS5.p1) and [S4.SS5.p2](https://arxiv.org/html/2601.21770v1#S4.SS5.p2)
- **推理预算**：Deployed 0.5B-total/0.1B-active model; HR@50/100/500. Serving beam width, hardware, inference batch size, latency not reported; beam 768 is RL training candidate generation.
  - 出处：Sections 4/4.2/4.4: [S4.p1](https://arxiv.org/html/2601.21770v1#S4.p1) and [S4.SS2.p1](https://arxiv.org/html/2601.21770v1#S4.SS2.p1) and [S4.SS4.p1](https://arxiv.org/html/2601.21770v1#S4.SS4.p1)
- **结果来源**：Original Table 1: scaling; Table 2: replay versus equally sized SASRec/TIGER with identical input features; Table 3: online A/B; Tables 4/5: RL/tokenizer ablations.
  - 出处：Sections 4.2/4.3 and Tables 1-5: [S4.SS2.p1](https://arxiv.org/html/2601.21770v1#S4.SS2.p1) and [S4.T2](https://arxiv.org/html/2601.21770v1#S4.T2) and [S4.T3](https://arxiv.org/html/2601.21770v1#S4.T3) and [S3.T1](https://arxiv.org/html/2601.21770v1#S3.T1) and [S4.T4](https://arxiv.org/html/2601.21770v1#S4.T4) and [S4.T5](https://arxiv.org/html/2601.21770v1#S4.T5)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["OneMall"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"前序工作"| B["OneRec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B peer
```

- **同期对比** · [TIGER](tiger.md): TIGER is the equally sized encoder-decoder replay baseline.
  - 出处：OneMall v1, Section 4.2 and Table 2: [S4.SS2.p1](https://arxiv.org/html/2601.21770v1#S4.SS2.p1); [S4.T2](https://arxiv.org/html/2601.21770v1#S4.T2).
- **前序工作** · [OneRec](onerec.md): OneMall adapts OneRec's end-to-end short-video paradigm to e-commerce scenarios.
  - 出处：OneMall v1, Section 1 (Deng et al., 2025, arXiv:2502.18965; distinct from Zhou et al., 2025 Technical Report): [S1.p5](https://arxiv.org/html/2601.21770v1#S1.p5).

[查看同格全部论文](../../../README.zh.md#范式系统与基准)
