# Dynamic-Single-Codebook

*From a Static Multi-Level Small Semantic Codebook to a Dynamic Single-Level Large Semantic Codebook for Generative Recommendation* — Xie et al. · arXiv’26

`V. 效率` · `Tokenization` · [论文](https://arxiv.org/abs/2608.21012) · [矩阵](../../../README.zh.md#v--tokenization) · [English](../../papers/dynamic-single-codebook.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>–"] --> T["Tokenization<br/>Dyn. KM+Disamb."] --> B["Backbone<br/>Enc-Dec / Lazy Dec-Only"] --> TR["Training<br/>Fixed / NTP†"] --> I["Inference<br/>Beam†"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `–`: Not reported in the paper.
- `Dyn. KM+Disamb.`: Dynamically updated k-means codes combined with disambiguation codes.
- `Enc-Dec / Lazy Dec-Only`: Encoder–decoder and lazy decoder-only backbone variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.

### TL;DR

> [!NOTE]
> Dynamic-Single-Codebook 用大单层码本的一个 token 加协同消歧 token 替代多层残差码，并随曝光分布变化动态更新码本。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | V. 效率：Can it be trained and served within latency and cost budgets? |
| 核心贡献 | Dynamic-Single-Codebook 用大单层码本的一个 token 加协同消歧 token 替代多层残差码，并随曝光分布变化动态更新码本。 |
| 主要改动阶段 | Tokenization |

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Beauty 2014; KuaiRec 2.0 Big Matrix, watch_ratio>=1 and users with >=5 retained events; industrial data. Other filters not reported.
  - 出处：Section 4.1: [S4.SS1.p1](https://arxiv.org/html/2608.21012v1#S4.SS1.p1) and [S4.SS1.p2](https://arxiv.org/html/2608.21012v1#S4.SS1.p2)
- **切分**：Per-user chronological last/penultimate holdouts; separate KuaiRec experiment trains through September 3, validates September 4, tests September 5.
  - 出处：Section 4.1 and fixed-date protocol: [S4.SS1.p2](https://arxiv.org/html/2608.21012v1#S4.SS1.p2) and [S4.SS3.SSS2.p1](https://arxiv.org/html/2608.21012v1#S4.SS3.SSS2.p1)
- **候选集**：not reported
  - 出处：Candidate protocol absent from Sections 4.1-4.5 and Appendices B-E: [S4.SS1](https://arxiv.org/html/2608.21012v1#S4.SS1)
- **可见性**：warm; no unseen-item protocol is defined. Fixed-date validation/test days are excluded from codebook fitting; leave-two-out PV weights use all viewing events. Item-level holdouts: not reported.
  - 出处：Section 4.1 and fixed-date protocol: [S4.SS1.p2](https://arxiv.org/html/2608.21012v1#S4.SS1.p2) and [S4.SS3.SSS2.p1](https://arxiv.org/html/2608.21012v1#S4.SS3.SSS2.p1)
- **SID 规格**：Public data: [1024,512], semantic plus balanced disambiguation code; baseline [256,256,256].
  - 出处：Section 4.1: [S4.SS1.p3](https://arxiv.org/html/2608.21012v1#S4.SS1.p3)
- **推理预算**：K=5/10; beam width, hardware model, inference batch size, absolute latency/QPS not reported. Single-card QPS gains: 28.57%-47.0%.
  - 出处：Sections 4.1 and 4.5: [S4.SS1.p5](https://arxiv.org/html/2608.21012v1#S4.SS1.p5) and [S4.SS5.p1](https://arxiv.org/html/2608.21012v1#S4.SS5.p1)
- **结果来源**：Original Table 2, Figures 3/4/6, Tables 9-14; Section 4.5 online A/B.
  - 出处：Section 4 and Appendices C-E: [S4](https://arxiv.org/html/2608.21012v1#S4) and [A3](https://arxiv.org/html/2608.21012v1#A3) and [A4](https://arxiv.org/html/2608.21012v1#A4) and [A5](https://arxiv.org/html/2608.21012v1#A5)

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["Dynamic-Single-Codebook"]
    P -->|alternative| A["RPG"]
    P -->|alternative| B["LLaDA-Rec"]
    P -->|alternative| C["LETTER"]
```

- **替代方案** · [RPG](rpg.md): RPG parallelizes long SIDs; this method shortens SIDs.
  - 出处：Dynamic-Single-Codebook v1, Section 2.2: https://arxiv.org/html/2608.21012v1#S2.SS2.p2.
- **替代方案** · [LLaDA-Rec](llada-rec.md): LLaDA-Rec uses diffusion with adapted beam search; this method reduces token count.
  - 出处：Dynamic-Single-Codebook v1, Sections 1 and 2.2: https://arxiv.org/html/2608.21012v1#S1.p4; https://arxiv.org/html/2608.21012v1#S2.SS2.p2.
- **替代方案** · [LETTER](letter.md): LETTER regularizes residual quantization; this method changes semantic codebook width and depth.
  - 出处：Dynamic-Single-Codebook v1, Section 2.1: https://arxiv.org/html/2608.21012v1#S2.SS1.p2.

[查看同格全部论文](../../../README.zh.md#v--tokenization)
