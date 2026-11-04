# UniSID

[← 问题 × 阶段矩阵](../../../README.zh.md#i--tokenization) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/unisid.md) | 中文

| **题目** | *End-to-End Semantic ID Generation for Generative Advertisement Recommendation* |
| :-- | :-- |
| **作者** | Jiang et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `I. 信息量` · `构码（Tokenization）` |
| **改动** | ○ 物品表示 · ● 构码 |
| **构码输入** | `Text` + `Img` |
| **领域** | `广告` · `电商` |
| **链接** | [论文](https://arxiv.org/abs/2602.10445) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>○ Text+Img+Attr"] --> T["构码 Tokenization<br/>● Direct SID Heads"] --> B["生成骨干 Backbone<br/>–"] --> TR["训练 Training<br/>编号器更新: –<br/>训练目标: –"] --> I["推理 Inference<br/>–"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class R other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+Img+Attr`：文本、图像与结构化物品属性。
- `Direct SID Heads`：直接输出语义 ID 码位的预测头。

### TL;DR

> [!NOTE]
> UniSID 通过多粒度对比学习与基于摘要的重构，从原始广告数据端到端联合优化嵌入与 SID，替代先提取嵌入再后验量化的两步做法。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Tencent Ad-60W and Ad-100W multimodal advertising datasets, plus Amazon Beauty. Filtering rules not reported; public preprocessing is described only as standard practice.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2602.10445v3#S4.SS1.p1) ; #S4.T1
- **切分**：Table 1 train/test counts: Ad-60W 500K/100K, Ad-100W 1M/1M, Beauty 12101/12101. Split procedure, count granularity and validation allocation not reported.
  - 出处：[S4.T1](https://arxiv.org/html/2602.10445v3#S4.T1) ; #S4.SS1.p1
- **候选集**：Embedding retrieval sampled: 1000 total (one positive plus 999 negatives); negative sampling distribution and history exclusion not reported. Next-ad and Beauty recommendation candidate protocols not reported.
  - 出处：[S4.SS1.p3](https://arxiv.org/html/2602.10445v3#S4.SS1.p3)
- **可见性**：warm; no unseen-item protocol is defined. SID-model fitting exposure to test items not reported.
  - 出处：[S4.SS1.p1](https://arxiv.org/html/2602.10445v3#S4.SS1.p1) ; #S4.SS1.p3 ; #A1.SS3.p1
- **SID 规格**：Three direct categorical SID heads x 2048 entries, using per-layer argmax on Qwen2.5-VL-3B outputs rather than residual quantization. Collision handling not reported.
  - 出处：[S3.SS2.p3](https://arxiv.org/html/2602.10445v3#S3.SS2.p3) ; #A1.SS3.p1
- **推理预算**：Beauty replaces the TIGER tokenizer with UniSID; industrial next-ad predictor details not reported. Metrics at K=1/5/10/20. Downstream decoding/beam, inference hardware, batch size and latency not reported; tokenizer training batch 512 is not an inference setting.
  - 出处：[S4.SS1.p3](https://arxiv.org/html/2602.10445v3#S4.SS1.p3) ; #S4.SS2.p5 ; #A1.SS3.p1
- **结果来源**：Original Table 2: SID quality/next-ad prediction; Table 3: embedding retrieval; Table 5: ablations. Table 4: UniSID in TIGER on Beauty, with baseline results explicitly taken from LETTER.
  - 出处：[S4.T2](https://arxiv.org/html/2602.10445v3#S4.T2) ; #S4.T3 ; #S4.T4 ; #S4.T5 ; #S4.SS2.p5

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["UniSID"]
    P -->|"前序工作"| A["TIGER"]
    P -->|"同期对比"| B["LETTER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B peer
```

- **前序工作** · [TIGER](tiger.md): On Beauty, UniSID replaces TIGER RQ-VAE tokenization with direct multimodal SID heads while retaining the TIGER training and evaluation framework.
  - 出处：UniSID v3, Section 4.2 and Table 4: [S4.SS2.p5](https://arxiv.org/html/2602.10445v3#S4.SS2.p5); [S4.T4](https://arxiv.org/html/2602.10445v3#S4.T4).
- **同期对比** · [LETTER](letter.md): LETTER supplies the published Beauty baseline results, including TIGER-LETTER; UniSID jointly learns embeddings and direct SIDs from raw features.
  - 出处：UniSID v3, Sections 3/4.2 and Table 4; baseline numbers are reused: [S3.p1](https://arxiv.org/html/2602.10445v3#S3.p1); [S4.SS2.p5](https://arxiv.org/html/2602.10445v3#S4.SS2.p5); [S4.T4](https://arxiv.org/html/2602.10445v3#S4.T4).

[查看同格全部论文](../../../README.zh.md#i--tokenization)
