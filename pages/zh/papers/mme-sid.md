# MME-SID

[← 问题 × 阶段矩阵](../../../README.zh.md#i--tokenization) · [按阶段索引](../index/stages.md) · [按模态索引](../index/modality.md) · [English](../../papers/mme-sid.md) | 中文

| **题目** | *Empowering large language model for sequential recommendation via multimodal embeddings and semantic ids* |
| :-- | :-- |
| **作者** | Wang et al. |
| **发表** | CIKM’25 |
| **问题与阶段** | `I. 信息量` · `编号（Tokenization）` — 补充：`I. 信息量` × `骨干（Backbone）`；`III. SID 与模型对齐` × `骨干（Backbone）`；`III. SID 与模型对齐` × `编号（Tokenization）` |
| **链接** | [论文](https://arxiv.org/abs/2509.02017) · [代码](https://github.com/Applied-Machine-Learning-Lab/MME-SID) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["表征 Representation<br/>Text+Img+CF"] --> T["编号 Tokenization<br/>MM-RQ"] --> B["骨干 Backbone<br/>Dec-Only"] --> TR["训练 Training<br/>Fixed / NTP"] --> I["推理 Inference<br/>Scoring"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef also fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class B also
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+Img+CF`：文本、图像表征结合协同过滤信号。
- `MM-RQ`：多模态残差量化（Multimodal RQ）。
- `Dec-Only`：仅解码器（Decoder-only）自回归架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP`：标准下一 token 预测（Next-Token Prediction）交叉熵损失；基于预训练 LLM 的指令微调（SFT）亦归入此类。
- `Scoring`：直接计算候选物品得分，不逐位生成 SID。

### TL;DR

> [!NOTE]
> MME-SID 将多模态嵌入与经最大均值差异和对比对齐训练的 MM-RQ-VAE SID 嵌入一同输入 LLM，缓解嵌入坍缩与灾难性遗忘。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：SID 或读取它的模型是否充分携带了推荐所需的协同、多模态与时空信号？ |
| 核心贡献 | MME-SID 将多模态嵌入与经最大均值差异和对比对齐训练的 MM-RQ-VAE SID 嵌入一同输入 LLM，缓解嵌入坍缩与灾难性遗忘。 |
| 主要改动阶段 | 编号（Tokenization） |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon 2014 5-core: Beauty (22,332 users / 12,086 items), Toys and Games (19,121 / 11,757), Sports and Outdoors (35,092 / 18,090); items lacking a title or image are removed. Positives are ratings above 3.
  - 出处：5-core Amazon 2014 and item removal: [S5.SS1.SSS1.p1](https://arxiv.org/html/2509.02017v1#S5.SS1.SSS1.p1) and [A2.p1](https://arxiv.org/html/2509.02017v1#A2.p1); statistics: [S5.T1](https://arxiv.org/html/2509.02017v1#S5.T1).
- **切分**：Per user, the N-th (last) item is the test target and the (N-1)-th item the training target; a validation split is not reported. Results averaged over 3 runs.
  - 出处：Last and second-last item as test and training targets: [S5.SS1.SSS1.p1](https://arxiv.org/html/2509.02017v1#S5.SS1.SSS1.p1); three runs: [S5.SS1.SSS4.p1](https://arxiv.org/html/2509.02017v1#S5.SS1.SSS4.p1).
- **候选集**：not reported (full catalog versus sampled); items are scored by dot products between the LLM output and multimodal item embeddings, with HR and nDCG at 5, 10, 20.
  - 出处：Scores over target item embeddings: [S4.SS3.p3](https://arxiv.org/html/2509.02017v1#S4.SS3.p3) and [S6.SS2.p1](https://arxiv.org/html/2509.02017v1#S6.SS2.p1); metrics: [S5.SS1.SSS2.p1](https://arxiv.org/html/2509.02017v1#S5.SS1.SSS2.p1).
- **可见性**：warm; no unseen-item protocol is defined. A frequency-aware fusion module reweights modalities by each item's training-set frequency.
  - 出处：Standard split; frequency-aware fusion for cold versus warm items without an unseen-item protocol: [S5.SS1.SSS1.p1](https://arxiv.org/html/2509.02017v1#S5.SS1.SSS1.p1) and [S4.SS3.p3](https://arxiv.org/html/2509.02017v1#S4.SS3.p3).
- **SID 规格**：Separate collaborative, textual, and visual SIDs from RQ-VAEs with 4 levels x 256 codes (300 for Sports), used as LLM input embeddings alongside projected modality embeddings. The paper states that MME-SID does not need to tackle collisions because multimodal data discriminate between items; no resolution rule is described.
  - 出处：4 levels x 256 (300 for Sports) per modality: [A1.T4](https://arxiv.org/html/2509.02017v1#A1.T4); no collision handling needed by design: [S4.I1.i2.p1](https://arxiv.org/html/2509.02017v1#S4.I1.i2.p1).
- **推理预算**：No autoregressive decoding: one forward pass of Llama3-8B-instruct, then scoring against item embeddings. All experiments on A100 GPUs; inference batch size and latency: not reported.
  - 出处：Scoring instead of autoregressive decoding: [S6.SS2.p1](https://arxiv.org/html/2509.02017v1#S6.SS2.p1); hardware: [S5.SS1.SSS4.p1](https://arxiv.org/html/2509.02017v1#S5.SS1.SSS4.p1).
- **结果来源**：Table 3 (Beauty, Toys, Sports versus ID, multimodal, and SID-based baselines; t-tests); Figure 3 (embedding collapse and SR performance); Appendix Table 4 (hyperparameters).
  - 出处：Main: [S5.T3](https://arxiv.org/html/2509.02017v1#S5.T3); collapse analysis: [S5.SS3.p1](https://arxiv.org/html/2509.02017v1#S5.SS3.p1).

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["MME-SID"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"同期对比"| B["LETTER"]
    P -->|"替代方案"| C["LC-Rec"]
    P -->|"替代方案"| D["ADC-SID"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D peer
```

- **同期对比** · [TIGER](tiger.md): TIGER-MM generates per-modality RQ-VAE semantic IDs autoregressively and must resolve collisions; MME-SID feeds multimodal SIDs and embeddings to an LLM and scores items directly.
  - 出处：MME-SID v1, baseline TIGER-MM: [S5.I2.i7.p1](https://arxiv.org/html/2509.02017v1#S5.I2.i7.p1); collision contrast: [S4.I1.i2.p1](https://arxiv.org/html/2509.02017v1#S4.I1.i2.p1); Table 3: [S5.T3](https://arxiv.org/html/2509.02017v1#S5.T3).
- **同期对比** · [LETTER](letter.md): LETTER regularizes the tokenizer for generative retrieval on a TIGER backbone; MME-SID avoids generation and aligns modalities with an MMD loss.
  - 出处：MME-SID v1, baseline LETTER implemented on TIGER: [S5.I2.i9.p1](https://arxiv.org/html/2509.02017v1#S5.I2.i9.p1); Table 3: [S5.T3](https://arxiv.org/html/2509.02017v1#S5.T3).
- **替代方案** · [LC-Rec](lc-rec.md): LC-Rec aligns an LLM to item indices but decodes autoregressively; MME-SID scores items from the LLM output for lower latency.
  - 出处：MME-SID v1, Section 6.2: [S6.SS2.p1](https://arxiv.org/html/2509.02017v1#S6.SS2.p1).
- **替代方案** · [ADC-SID](adc-sid.md): ADC-SID later compares against MM-RQ-VAE (MME-SID's tokenizer) and adds adaptive behavior-content alignment.
  - 出处：Evidence is from the later ADC-SID paper: MM-RQ-VAE baseline and Table 2: [S4.I3.i6.p1](https://arxiv.org/html/2510.25622v3#S4.I3.i6.p1) and [S4.T2](https://arxiv.org/html/2510.25622v3#S4.T2).

[查看同格全部论文](../../../README.zh.md#i--tokenization)
