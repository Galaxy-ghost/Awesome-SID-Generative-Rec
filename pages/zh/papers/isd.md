# ISD

[← 问题 × 阶段矩阵](../../../README.zh.md#iv--inference) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/isd.md) | 中文

| **题目** | *Understanding Semantic IDs: From Item Representation to Item Selection in Generative Recommendation* |
| :-- | :-- |
| **作者** | Wang et al. |
| **发表** | arXiv’26 |
| **问题与阶段** | `IV. 实用目标` · `推理（Inference）` |
| **改动** | ● 推理 |
| **构码输入** | `Text` |
| **领域** | `电商` |
| **链接** | [论文](https://arxiv.org/abs/2607.24995) · [代码](https://anonymous.4open.science/r/ISD-CF7C) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text†"] --> T["构码 Tokenization<br/>RQ-VAE†"] --> B["生成骨干 Backbone<br/>Enc-Dec†"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: NTP†"] --> I["推理 Inference<br/>● ISD Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class I main
```

- `Text†`：物品文本表征（由配置推断）。
- `RQ-VAE†`：残差量化变分自编码器（由配置推断）。
- `Enc-Dec†`：编码器-解码器架构（由配置推断）。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP†`：下一 token 预测损失（由配置推断）。
- `ISD Beam`：由用户侧物品打分支撑前缀保留的束搜索（Item-Supported Beam）。

### TL;DR

> [!NOTE]
> ISD 在指出 SID 丢失局部物品结构后，于推理阶段无需重训地用用户特定物品排序支撑 SID 前缀，避免它们在束搜索中被过早剪枝。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews: Baby, Office, Scientific; filtering rules not reported.
  - 出处：[S6.SS1.SSS1.p1](https://arxiv.org/html/2607.24995v1#S6.SS1.SSS1.p1) ; #A1.T6
- **切分**：Per-user chronological leave-one-out: final interaction test, preceding interaction validation, remainder training.
  - 出处：[S6.SS1.SSS1.p1](https://arxiv.org/html/2607.24995v1#S6.SS1.SSS1.p1) ; #A1.SS4.SSS1.p1
- **候选集**：full catalog of eligible items, with the same consumed-item mask for all methods.
  - 出处：[S6.SS1.SSS3.p1](https://arxiv.org/html/2607.24995v1#S6.SS1.SSS3.p1) ; #A1.SS4.SSS1.p1 ; #A1.SS4.SSS2.p1
- **可见性**：warm; no unseen-item protocol is defined. Separate item scorer and transition/co-consumption statistics use training interactions; tokenizer exposure to test items not reported.
  - 出处：[S6.SS1](https://arxiv.org/html/2607.24995v1#S6.SS1) ; #A1.SS2.SSS1.p1 ; #S5.SS1.SSS1.p1
- **SID 规格**：TIGER/LIGER assignments remain fixed: three semantic positions plus a collision-resolution suffix. Codebook sizes and suffix-assignment rule not reported; primary filtering diagnostic uses RQ-VAE.
  - 出处：[S3.SS3.p1](https://arxiv.org/html/2607.24995v1#S3.SS3.p1) ; #A1.SS2.p1 ; #A1.SS3.SSS1.p1 ; #S6.SS4.p1
- **推理预算**：Beam 50; one decoder pass; top-50 item-support ranking constructed once per history; reciprocal-rank fusion kappa=60; at most 50 output items, evaluated at K=10/20. Ranker construction is excluded from decoding complexity. Hardware, inference batch size and latency not reported.
  - 出处：[A1.SS3.SSS1.p1](https://arxiv.org/html/2607.24995v1#A1.SS3.SSS1.p1) ; #S5.SS2.SSS2.p1 ; #S5.SS3.p1 ; #A1.SS4.SSS2.p1
- **结果来源**：Original Table 3: matched recommendation comparisons, means across three seeds; Table 4: SID reassignment; Table 5: filtering/ordering ablations. Tables 1-2: encoder/SID representation diagnostics.
  - 出处：[S5.T3](https://arxiv.org/html/2607.24995v1#S5.T3) ; #S6.T4 ; #S6.T5 ; #A1.SS4.SSS2.p1

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["ISD"]
    P -->|"前序工作"| A["TIGER"]
    P -->|"前序工作"| B["LIGER"]
    P -->|"同期对比"| C["ETEGRec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **前序工作** · [TIGER](tiger.md): ISD augments a frozen TIGER decoder with item-supported prefix selection and final ordering, without changing its SIDs or retraining.
  - 出处：ISD v1, Sections 5.2/6.1.2 and Table 3: [S5.SS2](https://arxiv.org/html/2607.24995v1#S5.SS2); [S6.SS1.SSS2.p1](https://arxiv.org/html/2607.24995v1#S6.SS1.SSS2.p1); [S5.T3](https://arxiv.org/html/2607.24995v1#S5.T3).
- **前序工作** · [LIGER](liger.md): ISD also operates inside LIGER before beam reduction; LIGER already combines SID generation with dense retrieval and ranking.
  - 出处：ISD v1, Sections 4/6.1.2 and Table 3: [S4.p3](https://arxiv.org/html/2607.24995v1#S4.p3); [S6.SS1.SSS2.p1](https://arxiv.org/html/2607.24995v1#S6.SS1.SSS2.p1); [S5.T3](https://arxiv.org/html/2607.24995v1#S5.T3).
- **同期对比** · [ETEGRec](etegrec.md): ETEGRec jointly trains the tokenizer and recommender; ISD instead changes inference with the SID assignment and decoder fixed.
  - 出处：ISD v1, Sections 5.2/6.1.2 and Table 3: [S5.SS2](https://arxiv.org/html/2607.24995v1#S5.SS2); [S6.SS1.SSS2.p1](https://arxiv.org/html/2607.24995v1#S6.SS1.SSS2.p1); [S5.T3](https://arxiv.org/html/2607.24995v1#S5.T3).

[查看同格全部论文](../../../README.zh.md#iv--inference)
