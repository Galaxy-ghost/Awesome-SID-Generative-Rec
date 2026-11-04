# KL-MOPD

[← 问题 × 阶段矩阵](../../../README.zh.md#iv--training) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/kl-mopd.md) | 中文

| **题目** | *Discrepancy-Aware Multi-Objective On-Policy Distillation for Generative Recommendation* |
| :-- | :-- |
| **作者** | Yang et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `IV. 实用目标` · `训练（Training）` |
| **改动** | ● 训练目标 |
| **构码输入** | `CF` |
| **领域** | `电商` · `广告` |
| **链接** | [论文](https://arxiv.org/abs/2610.36973) · [代码](https://github.com/Yandorn/KL-MOPD) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>CF"] --> T["构码 Tokenization<br/>R-KM"] --> B["生成骨干 Backbone<br/>Enc-Dec"] --> TR["训练 Training<br/>编号器更新: Fixed†<br/>训练目标: ● (NTP† / (NTP + Aux.)†) → KL-weighted OPD"] --> I["推理 Inference<br/>C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class TR main
```

- `CF`：纯协同过滤交互信号。
- `R-KM`：残差 k-means 量化（Residual k-means）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed†`：生成器训练期间冻结编号器（由配置推断）。
- `(NTP† / (NTP + Aux.)†) → KL-weighted OPD`：先进行下一 token 预训练初始化，再执行 KL 加权的同策略蒸馏（OPD）。
- `C-Beam`：受合法物品集合约束的束搜索（Constrained beam search）。

### TL;DR

> [!NOTE]
> KL-MOPD 按教师与学生的初始 KL 散度加权，将点击与转化教师逐 token 蒸馏到学生生成器，改进标准在线策略蒸馏。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：TencentGR (CTR/CVR), YooChoose (CTR/GMV), Taobao (CTR/CVR), industrial advertising (CTR/eCPM). Filtering: not reported.
  - 出处：Section 4.1: [S4.SS1.p1](https://arxiv.org/html/2610.36973v1#S4.SS1.p1)
- **切分**：Public: chronological 70% student pretraining, 20% teacher tuning/student distillation, 10% evaluation. Industry: penultimate day tuning, final day evaluation, >11M requests/day; pretraining allocation not reported. Sliding windows; history caps 100 public/128 Industry.
  - 出处：Section 4.1: [S4.SS1.p1](https://arxiv.org/html/2610.36973v1#S4.SS1.p1) and [S4.SS1.p4](https://arxiv.org/html/2610.36973v1#S4.SS1.p4)
- **候选集**：not reported
  - 出处：Section 4.1 states decoding and cutoffs without specifying candidate sampling: [S4.SS1.p5](https://arxiv.org/html/2610.36973v1#S4.SS1.p5)
- **可见性**：warm; no unseen-item protocol is defined. Two-tower CF embedding exposure to test items: not reported.
  - 出处：Section 4.1 defines no unseen-item evaluation: [S4.SS1.p1](https://arxiv.org/html/2610.36973v1#S4.SS1.p1) and [S4.SS1.p2](https://arxiv.org/html/2610.36973v1#S4.SS1.p2)
- **SID 规格**：RQ-KMeans of two-tower CF embeddings: TencentGR 5x64, YooChoose 5x128, Taobao 8x64, Industry 8x310. Collision handling: not reported.
  - 出处：Section 4.1: [S4.SS1.p2](https://arxiv.org/html/2610.36973v1#S4.SS1.p2)
- **推理预算**：Constrained beam 50, K=10/20 public; beam 200, K=100/200 Industry. Inference hardware, batch size, latency: not reported.
  - 出处：Section 4.1: [S4.SS1.p5](https://arxiv.org/html/2610.36973v1#S4.SS1.p5)
- **结果来源**：This study's adapted/tuned baselines: Table 3 public TIGER/REG4Rec, Table 4 ablations, Table 5 industrial TIGER, Table 6 five-day online A/B (10% control, 10% treatment).
  - 出处：Tables 3-6 and baseline setup: [S2.T3](https://arxiv.org/html/2610.36973v1#S2.T3) and [S4.T4](https://arxiv.org/html/2610.36973v1#S4.T4) and [S4.T5](https://arxiv.org/html/2610.36973v1#S4.T5) and [S4.T6](https://arxiv.org/html/2610.36973v1#S4.T6) and [S4.SS1.p3](https://arxiv.org/html/2610.36973v1#S4.SS1.p3)

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["KL-MOPD"]
    P -->|"前序工作"| A["TIGER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A peer
```

- **前序工作** · [TIGER](tiger.md): TIGER is a backbone for token-wise multi-teacher distillation, with CF-derived SIDs in this study.
  - 出处：KL-MOPD v1, Section 4.1 and Table 3: [S4.SS1.p2](https://arxiv.org/html/2610.36973v1#S4.SS1.p2); [S2.T3](https://arxiv.org/html/2610.36973v1#S2.T3).

[查看同格全部论文](../../../README.zh.md#iv--training)
