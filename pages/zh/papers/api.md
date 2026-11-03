# API

[← 问题 × 阶段矩阵](../../../README.zh.md#ii--tokenization) · [按阶段索引](../index/stages.md) · [按模态索引](../index/modality.md) · [English](../../papers/api.md) | 中文

| **题目** | *The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features for Generative Recommendation* |
| :-- | :-- |
| **作者** | Luo et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `II. 唯一性与合法性` · `编号（Tokenization）` |
| **链接** | [论文](https://arxiv.org/abs/2610.36763) · [代码](https://anonymous.4open.science/r/API-C1F9/) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["表征 Representation<br/>Text"] --> T["编号 Tokenization<br/>PID (P-SAE)"] --> B["骨干 Backbone<br/>Enc-Dec / Dec-Only (AR); Non-AR (PR)"] --> TR["训练 Training<br/>Fixed / NTP + Rank + Aux. / MTP + Rank + Aux."] --> I["推理 Inference<br/>C-Beam / Scoring"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `PID (P-SAE)`：基于预训练稀疏自编码器的可解释标识符（Pretrained Interpretable ID）。
- `Enc-Dec / Dec-Only (AR); Non-AR (PR)`：自回归分支采用编码器-解码器或仅解码器，并行分支采用非自回归骨干。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP + Rank + Aux. / MTP + Rank + Aux.`：自回归或并行 token 预测联合排序损失与辅助损失。
- `C-Beam / Scoring`：依配置采用约束束搜索或直接候选打分。

### TL;DR

> [!NOTE]
> API 直接复用预训练稀疏自编码器的特征下标作为可解释 SID 词表，并训练适配器预测下标与激活强度，无需重新拟合词表。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | II. 唯一性与合法性：每个物品是否拥有无冲突的唯一 SID，生成的 SID 是否对应真实物品，码本是否均衡利用？ |
| 核心贡献 | API 直接复用预训练稀疏自编码器的特征下标作为可解释 SID 词表，并训练适配器预测下标与激活强度，无需重新拟合词表。 |
| 主要改动阶段 | 编号（Tokenization） |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Beauty, Sports, and Toys as preprocessed in prior work (P5, GRID), keeping their splits; item text from title, brand, category, and price. Sizes: Appendix A (not restated here).
  - 出处：Benchmark aligned with P5 and GRID: [S5.SS1.p1](https://arxiv.org/html/2610.36763v1#S5.SS1.p1).
- **切分**：The prior-work (P5 / GRID) splits and evaluation protocol are retained (allocation not restated); checkpoints selected by validation Recall@5.
  - 出处：Inherited splits; PID statistics from training items only: [S5.SS1.p1](https://arxiv.org/html/2610.36763v1#S5.SS1.p1).
- **候选集**：full catalog (complete test split, full catalog without sampled negatives).
  - 出处：Full catalog without sampled negatives: [S5.SS1.p4](https://arxiv.org/html/2610.36763v1#S5.SS1.p4).
- **可见性**：warm; no unseen-item protocol is defined. PID selection statistics and activation calibration are estimated from training-item contents.
  - 出处：PID statistics estimated from training-item contents; no unseen-item protocol: [S5.SS1.p1](https://arxiv.org/html/2610.36763v1#S5.SS1.p1).
- **SID 规格**：Pretrained Interpretable IDs: K in {4, 8, 16} feature indices selected by a priority rule from the 32 strongest of 24,576 labeled sparse-autoencoder features of a frozen GPT-2-small, plus their relative activation strengths, which separate items whose index sequences coincide. Collision-affected items at K=4: 15.16% on Beauty (77.37% with native SAE selection).
  - 出处：PID from frozen GPT-2 SAE features with K tokens and activation strengths: [S5.SS1.p3](https://arxiv.org/html/2610.36763v1#S5.SS1.p3), [S4.SS1.p3](https://arxiv.org/html/2610.36763v1#S4.SS1.p3); collisions: [S5.T3](https://arxiv.org/html/2610.36763v1#S5.T3).
- **推理预算**：Two decoders: parallel prediction (PR) with exact catalog scoring, and autoregressive (AR) with catalog-constrained beam search of width 50; T5- and GPT-2-style backbones trained from scratch. Hardware, inference batch size, and latency: not reported.
  - 出处：Decoding settings: [S5.SS1.p4](https://arxiv.org/html/2610.36763v1#S5.SS1.p4).
- **结果来源**：Table 1 (full API versus sequential and generative recommenders); Table 2 (tokenizers under T5 and GPT-2 backbones with AR and PR decoding); Table 3 (collision rates by token budget); Table 4 (content alignment); Table 5 (preference and strength ablation); Figure 3 (cross-domain vocabulary reuse).
  - 出处：Results: [S4.T1](https://arxiv.org/html/2610.36763v1#S4.T1), [S5.T2](https://arxiv.org/html/2610.36763v1#S5.T2), [S5.T3](https://arxiv.org/html/2610.36763v1#S5.T3), [S5.T4](https://arxiv.org/html/2610.36763v1#S5.T4), [S5.F3](https://arxiv.org/html/2610.36763v1#S5.F3).

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["API"]
    P -->|"前序工作"| A["GRID"]
    P -->|"同期对比"| B["RPG"]
    P -->|"同期对比"| C["TIGER"]
    P -->|"同期对比"| D["HiD-VAE"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D peer
```

- **前序工作** · [GRID](grid.md): API keeps GRID's preprocessed data and its residual-quantization tokenizer baselines, and replaces learned codes with pretrained interpretable SAE feature IDs.
  - 出处：API v1, benchmark and tokenization baselines aligned with GRID: [S5.SS1.p1](https://arxiv.org/html/2610.36763v1#S5.SS1.p1) and [S5.SS1.p2](https://arxiv.org/html/2610.36763v1#S5.SS1.p2); Table 2: [S5.T2](https://arxiv.org/html/2610.36763v1#S5.T2).
- **同期对比** · [RPG](rpg.md): RPG's parallel-prediction implementation is the PR backbone; API swaps its OPQ codes for SAE feature indices with activation strengths.
  - 出处：API v1, PR implementation based on RPG: [S5.SS1.p2](https://arxiv.org/html/2610.36763v1#S5.SS1.p2); Tables 1-2: [S4.T1](https://arxiv.org/html/2610.36763v1#S4.T1) and [S5.T2](https://arxiv.org/html/2610.36763v1#S5.T2).
- **同期对比** · [TIGER](tiger.md): TIGER's autoregressive implementation is the AR backbone and RQ-VAE is a tokenizer baseline.
  - 出处：API v1, AR implementation based on TIGER: [S5.SS1.p2](https://arxiv.org/html/2610.36763v1#S5.SS1.p2); Tables 1-2: [S4.T1](https://arxiv.org/html/2610.36763v1#S4.T1) and [S5.T2](https://arxiv.org/html/2610.36763v1#S5.T2).
- **同期对比** · [HiD-VAE](hid-vae.md): HiD-VAE supervises quantization levels with category tags for interpretability; API takes interpretability from labeled pretrained SAE features.
  - 出处：API v1, tokenization baselines: [S5.SS1.p2](https://arxiv.org/html/2610.36763v1#S5.SS1.p2); Table 2: [S5.T2](https://arxiv.org/html/2610.36763v1#S5.T2).

[查看同格全部论文](../../../README.zh.md#ii--tokenization)
