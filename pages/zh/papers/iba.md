# IBA

*Where Reasoning Matters: Rethinking Latent Reasoning in Semantic ID-based Generative Recommendation* — Yang et al. · arXiv’26

`V. 效率` · `Backbone` · [论文](https://arxiv.org/abs/2607.12425) · [矩阵](../../../README.zh.md#v--backbone) · [English](../../papers/iba.md)

阅读级别：概览（第 1 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>RQ-VAE"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP → (NTP + Aux.)"] --> I["Inference<br/>C-Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class B main
```

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → (NTP + Aux.)`: Next-token prediction, followed by joint optimization of next-token prediction and auxiliary objectives.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> IBA 按信息增益在各 SID 位置之间分配隐式推理步数，将更多计算分给信息量更大的前序位置，替代每个位置固定步数的做法。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | V. 效率：Can it be trained and served within latency and cost budgets? |
| 核心贡献 | IBA 按信息增益在各 SID 位置之间分配隐式推理步数，将更多计算分给信息量更大的前序位置，替代每个位置固定步数的做法。 |
| 主要改动阶段 | Backbone |

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Instruments and Beauty; MicroLens. Users with fewer than 5 interactions removed; training histories capped at 20 items.
  - 出处：Section IV-A1: [S4.SS1.SSS1.p1](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS1.p1)
- **切分**：Leave-one-out, one test target per user; exact validation/test allocation not reported.
  - 出处：Sections IV-A1/IV-A3: [S4.SS1.SSS1.p1](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS1.p1) and [S4.SS1.SSS3.p1](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS3.p1)
- **候选集**：not reported
  - 出处：Section IV-A describes metrics and catalog-valid trie decoding, not evaluation negatives: [S4.SS1.SSS3.p1](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS3.p1) and [S4.SS1.SSS4.p2](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS4.p2)
- **可见性**：warm; no unseen-item protocol is defined. Information-gain prior estimated from training interactions only; tokenizer exposure to test items not reported.
  - 出处：Sections IV-A1/III-A define no item holdout: [S4.SS1.SSS1.p1](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS1.p1) and [S3.SS1.p1](https://arxiv.org/html/2607.12425v1#S3.SS1.p1)
- **SID 规格**：RQ-VAE on Sentence-T5 text embeddings: 4 tokens; codebook sizes and collision handling not reported.
  - 出处：Sections II-A and IV-A: [S2.SS1.p2](https://arxiv.org/html/2607.12425v1#S2.SS1.p2) and [S4.SS1.SSS1.p1](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS1.p1) and [S4.SS1.SSS4.p1](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS4.p1)
- **推理预算**：Trie-constrained beam 20, maximum 10 generated tokens; 6 latent refinement steps with prior (3,2,1,0). NVIDIA RTX 4090 24GB; Instruments generation time 24.61 ms/user (TIGER 20.99, uniform 8-step refinement 25.78). Inference batch size not reported.
  - 出处：Sections IV-A4/IV-F and Table V: [S4.SS1.SSS4.p1](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS4.p1) and [S4.SS1.SSS4.p2](https://arxiv.org/html/2607.12425v1#S4.SS1.SSS4.p2) and [S4.T5](https://arxiv.org/html/2607.12425v1#S4.T5)
- **结果来源**：Original Table II: TIGER/LETTER plus IBA and baselines; Tables III/IV: schedules/ablations; Table V: generation efficiency.
  - 出处：Tables II-V: [S4.T2](https://arxiv.org/html/2607.12425v1#S4.T2) and [S4.T3](https://arxiv.org/html/2607.12425v1#S4.T3) and [S4.T4](https://arxiv.org/html/2607.12425v1#S4.T4) and [S4.T5](https://arxiv.org/html/2607.12425v1#S4.T5)

</details>

### 5. 相关工作

```mermaid
flowchart LR
    P["IBA"]
    P -->|predecessor| A["TIGER"]
    P -->|predecessor| B["LETTER"]
    P -->|alternative| C["SIDReasoner"]
```

- **前序工作** · [TIGER](tiger.md): IBA adds learned latent refinement allocation to TIGER.
  - 出处：IBA v1, Section IV-A2 and Table II: https://arxiv.org/html/2607.12425v1#S4.SS1.SSS2.p1; https://arxiv.org/html/2607.12425v1#S4.T2.
- **前序工作** · [LETTER](letter.md): LETTER is the second tested base model for IBA.
  - 出处：IBA v1, Sections IV-A2/IV-B and Table II: https://arxiv.org/html/2607.12425v1#S4.SS1.SSS2.p1; https://arxiv.org/html/2607.12425v1#S4.SS2.p2; https://arxiv.org/html/2607.12425v1#S4.T2.
- **替代方案** · [SIDReasoner](sidreasoner.md): SIDReasoner aligns IDs with language; IBA allocates hidden refinement steps.
  - 出处：IBA v1, Section V-B2: https://arxiv.org/html/2607.12425v1#S5.SS2.SSS2.p2; https://arxiv.org/html/2607.12425v1#S5.SS2.SSS2.p3.

[查看同格全部论文](../../../README.zh.md#v--backbone)
