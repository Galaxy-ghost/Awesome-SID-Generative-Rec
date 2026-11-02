# Ghost

*Echoes in Filter Bubble: Diagnosing and Curing Popularity Bias in Generative Recommenders* — Yin et al. · NeurIPS’26

`IV. 实用目标` · `Training` · [论文](https://arxiv.org/abs/2605.16825) · [代码](https://github.com/Esperanto-mega/Ghost) · [矩阵](../../../README.zh.md#iv--training) · [English](../../papers/ghost.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>Skeleton R-KM"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP + Aux."] --> I["Inference<br/>–"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `Skeleton R-KM`: Residual k-means organized around a shared semantic skeleton.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `–`: Not reported in the paper.

### TL;DR

> [!NOTE]
> Ghost 将流行度偏差归因于 token 级优化和无差别的物品编号，结合非对称负似然损失与骨架支撑的编号方法加以缓解。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | IV. 实用目标：Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| 核心贡献 | Ghost 将流行度偏差归因于 token 级优化和无差别的物品编号，结合非对称负似然损失与骨架支撑的编号方法加以缓解。 |
| 主要改动阶段 | Training |

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Product Review 2018: Musical Instruments; Arts, Crafts and Sewing; Video Games. Users/items with fewer than five interactions are filtered out.
  - 出处：Appendix C-A: [A3.SS1.p1](https://arxiv.org/html/2605.16825v3#A3.SS1.p1)
- **切分**：User interactions are ordered chronologically; train/validation/test allocation: not reported.
  - 出处：Appendix C-A reports chronological sequences but no holdout allocation: [A3.SS1.p1](https://arxiv.org/html/2605.16825v3#A3.SS1.p1)
- **候选集**：not reported
  - 出处：Section V and Appendix C describe metrics/baselines but not Ghost's candidate protocol: [S5](https://arxiv.org/html/2605.16825v3#S5) and [A3](https://arxiv.org/html/2605.16825v3#A3)
- **可见性**：warm; no unseen-item protocol is defined.
  - 出处：Section V and Appendix C define no unseen-item evaluation: [S5](https://arxiv.org/html/2605.16825v3#S5) and [A3](https://arxiv.org/html/2605.16825v3#A3)
- **SID 规格**：Skeleton RQ-KMeans, 256 centers/level; head length Lh, tail length Lh+Lt with inherited head prefix. Sweeps Lh=3/4/5 and Lt=1/2/3; main numerical lengths and collision handling: not reported.
  - 出处：Section IV-A, Section V-C, Appendix C-D: [S4.SS1.p2](https://arxiv.org/html/2605.16825v3#S4.SS1.p2) and [S5.SS3.p1](https://arxiv.org/html/2605.16825v3#S5.SS3.p1) and [A3.SS4.p2](https://arxiv.org/html/2605.16825v3#A3.SS4.p2)
- **推理预算**：Metrics at K=5/10; decoding algorithm, beam width, inference batch size, latency: not reported. General experimental machine: 8 NVIDIA A100 80GB GPUs; inference-specific allocation: not reported.
  - 出处：Table I and Appendix C-D: [S5.T1](https://arxiv.org/html/2605.16825v3#S5.T1) and [A3.SS4.p2](https://arxiv.org/html/2605.16825v3#A3.SS4.p2)
- **结果来源**：Original Table I: main comparison; Table II: ablations; Table III: backbone scaling. Main and ablation experiments use Qwen2.5-3B; scaling uses Qwen3 0.6B-8B.
  - 出处：Tables I-III and Appendix C-D: [S5.T1](https://arxiv.org/html/2605.16825v3#S5.T1) and [S5.T2](https://arxiv.org/html/2605.16825v3#S5.T2) and [S5.T3](https://arxiv.org/html/2605.16825v3#S5.T3) and [A3.SS4.p1](https://arxiv.org/html/2605.16825v3#A3.SS4.p1)

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["Ghost"]
    P -->|competitor| A["LETTER"]
    P -->|competitor| B["LC-Rec"]
```

- **同期对比** · [LETTER](letter.md): LETTER is evaluated as a standard generative baseline; Ghost addresses popularity bias through skeleton tokenization and asymmetric unlikelihood.
  - 出处：Ghost v3, Section V and Appendix C-B, Table I: https://arxiv.org/html/2605.16825v3#S5.p2; https://arxiv.org/html/2605.16825v3#A3.SS2.p1; https://arxiv.org/html/2605.16825v3#S5.T1.
- **同期对比** · [LC-Rec](lc-rec.md): LC-Rec is a standard generative baseline and the backbone reference for RQ-KMeans ablations; Ghost modifies tokenization and optimization.
  - 出处：Ghost v3, Section V and Table II: https://arxiv.org/html/2605.16825v3#S5.p2; https://arxiv.org/html/2605.16825v3#S5.T2; https://arxiv.org/html/2605.16825v3#S5.SS2.p1.

[查看同格全部论文](../../../README.zh.md#iv--training)
