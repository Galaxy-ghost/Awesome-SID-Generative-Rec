# Pctx

[← 问题 × 阶段矩阵](../../../README.zh.md#i--tokenization) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/pctx.md) | 中文

| **题目** | *Tokenizing Personalized Context for Generative Recommendation* |
| :-- | :-- |
| **作者** | Zhong et al. |
| **发表** | CIKM’26 |
| **问题与阶段** | `I. 信息量` · `构码（Tokenization）` |
| **改动** | ● 构码 · ○ 训练目标 · ○ 推理 |
| **构码输入** | `Text` + `CF` |
| **领域** | `电商` |
| **应用场景** | `一般物品推荐`；`公开数据` |
| **链接** | [论文](https://arxiv.org/abs/2510.21276) · [代码](https://github.com/YoungZ365/Pctx) |
| **阅读级别** | 概览（第 1 级） |

**本页目录**：[TL;DR](#tldr) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text+CF"] --> T["构码 Tokenization<br/>● RQ"] --> B["生成骨干 Backbone<br/>Enc-Dec"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ○ NTP"] --> I["推理 Inference<br/>○ Beam+Agg."]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR,I other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+CF`：文本表征结合协同过滤信号。
- `RQ`：残差向量量化（Residual Quantization）。
- `Enc-Dec`：编码器-解码器（Encoder-decoder）架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `NTP`：标准下一 token 预测（Next-Token Prediction）交叉熵损失；基于预训练 LLM 的指令微调（SFT）亦归入此类。
- `Beam+Agg.`：束搜索后对指向同一物品的多条标识符预测聚合得分。

### TL;DR

> [!NOTE]
> Pctx 将用户交互历史作为上下文对物品编号，使同一物品面向不同用户可获得不同 SID，替代静态的纯物品映射。

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews 2023: Musical Instruments, Industrial & Scientific, Video Games; exclude users/items with fewer than five interactions; chronological histories capped at 20 items.
  - 出处：[S3.SS1.SSS0.Px1.p1](https://arxiv.org/html/2510.21276v1#S3.SS1.SSS0.Px1.p1) ; #A3.SS1.p1
- **切分**：Per-user chronological leave-one-out: most recent item test, penultimate validation, remaining interactions training.
  - 出处：[A3.SS3.p1](https://arxiv.org/html/2510.21276v1#A3.SS3.p1)
- **候选集**：full catalog; full-ranking evaluation rather than negative sampling.
  - 出处：[A3.SS3.p1](https://arxiv.org/html/2510.21276v1#A3.SS3.p1)
- **可见性**：warm; no unseen-item protocol is defined. Auxiliary DuoRec is pretrained on the same training data, and representative contexts come from training interactions; textual-tokenizer fitting exposure to test items not reported.
  - 出处：[S2.SS2.p1](https://arxiv.org/html/2510.21276v1#S2.SS2.p1) ; #S2.SS2.SSS1.Px1.p1 ; #S2.SS2.SSS2.p1 ; #A3.SS3.p1
- **SID 规格**：3 x 256 residual semantic codes plus an auxiliary collision token of unreported vocabulary size; multiple context-conditioned SIDs/item. Same-item IDs differing only in collision token are merged; collision tokens distinguish different items. Main text names RQ-VAE; appendix specifies FAISS quantization.
  - 出处：[S2.SS2.SSS2.Px1.p1](https://arxiv.org/html/2510.21276v1#S2.SS2.SSS2.Px1.p1) ; #S2.SS2.SSS2.Px2.p2 ; #A3.SS4.p1
- **推理预算**：Beam decoding with aggregation of generated SID probabilities per item; Recall/NDCG@5/10. GR baseline beam 50; Pctx-specific beam width not separately reported. Inference hardware, batch size and latency not reported.
  - 出处：[S2.SS3.SSS0.Px2.p1](https://arxiv.org/html/2510.21276v1#S2.SS3.SSS0.Px2.p1) ; #A3.SS3.p1 ; #S3.SS1.SSS0.Px3.p1
- **结果来源**：Table 1: Pctx experiments with most baseline rows (including TIGER/LETTER) copied from Zheng et al. (2025); other baselines reconstructed. Table 2: ablations; Table 3: ensemble comparisons; Table 6: explainability.
  - 出处：[S3.T1](https://arxiv.org/html/2510.21276v1#S3.T1) ; #S3.T2 ; #S3.T3 ; #A3.SS4.p1 ; #A4.T6

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["Pctx"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"同期对比"| B["LETTER"]
    P -->|"同期对比"| C["ActionPiece"]
    P -->|"替代方案"| D["LC-Rec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D peer
```

- **同期对比** · [TIGER](tiger.md): TIGER assigns static semantic IDs; Pctx conditions item tokenization on user context and aggregates probabilities across personalized IDs.
  - 出处：Pctx v1, Section 2.4 and Table 1; TIGER results are reused from prior work per Appendix C.4: [S2.SS4.SSS0.Px1.p1](https://arxiv.org/html/2510.21276v1#S2.SS4.SSS0.Px1.p1); [S3.T1](https://arxiv.org/html/2510.21276v1#S3.T1); [A3.SS4.p1](https://arxiv.org/html/2510.21276v1#A3.SS4.p1).
- **同期对比** · [LETTER](letter.md): LETTER injects collaborative information and diversity constraints into item quantization; Pctx adds history-conditioned user interpretations.
  - 出处：Pctx v1, Appendix C.2 and Table 1; LETTER results are reused per Appendix C.4: [A3.SS2.p1](https://arxiv.org/html/2510.21276v1#A3.SS2.p1); [S3.T1](https://arxiv.org/html/2510.21276v1#S3.T1); [A3.SS4.p1](https://arxiv.org/html/2510.21276v1#A3.SS4.p1).
- **同期对比** · [ActionPiece](actionpiece.md): ActionPiece uses adjacent action context; Pctx extends tokenization context to the full user interaction history.
  - 出处：Pctx v1, Section 2.4 and Table 1: [S2.SS4.SSS0.Px3.p1](https://arxiv.org/html/2510.21276v1#S2.SS4.SSS0.Px3.p1); [S3.T1](https://arxiv.org/html/2510.21276v1#S3.T1).
- **替代方案** · [LC-Rec](lc-rec.md): LC-Rec is discussed as static tokenization under a universal item-similarity assumption; Pctx maps an item to personalized IDs under different user contexts.
  - 出处：Pctx v1, Section 2.4: [S2.SS4.SSS0.Px1.p1](https://arxiv.org/html/2510.21276v1#S2.SS4.SSS0.Px1.p1).

[查看同格全部论文](../../../README.zh.md#i--tokenization)
