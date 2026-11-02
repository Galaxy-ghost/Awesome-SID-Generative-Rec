# DPE-Rec

| **题目** | *Diversity-Preserving and Efficient Diffusion Language Model Recommendation for Bundle Construction* |
| :-- | :-- |
| **作者** | Ma et al. |
| **会议** | arXiv’26 |
| **问题与阶段** | `IV. 实用目标` · `Training` |
| **链接** | [论文](https://arxiv.org/abs/2610.34700) · [矩阵](../../../README.zh.md#iv--training) · [English](../../papers/dpe-rec.md) |
| **阅读级别** | 概览（第 1 级） |

本页目录：[TL;DR](#tldr) · [速览](#速览) · [3. 实验发现](#3-实验发现) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>– / Text+Img"] --> T["Tokenization<br/>RQ"] --> B["Backbone<br/>Non-AR"] --> TR["Training<br/>Fixed / Masked → RL (→ Masked KD for Fast)"] --> I["Inference<br/>Diff.+Legalize"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `– / Text+Img`: The representation source is unreported in one configuration; text and image representations are used in another.
- `RQ`: Residual quantization.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Masked → RL (→ Masked KD for Fast)`: Masked-prediction pretraining, followed by reinforcement learning and optional masked-prediction distillation for a faster variant.
- `Diff.+Legalize`: Diffusion-based decoding followed by mapping generated codes to valid items.

### TL;DR

> [!NOTE]
> DPE-Rec 用扩散语言模型做捆绑包补全，加入语义分叉感知的 GRPO 保持组合多样性，并用伪轨迹蒸馏在每步去噪中揭示更多 token。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | IV. 实用目标：Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| 核心贡献 | DPE-Rec 用扩散语言模型做捆绑包补全，加入语义分叉感知的 GRPO 保持组合多样性，并用伪轨迹蒸馏在每步去噪中揭示更多 token。 |
| 主要改动阶段 | Training |

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Spotify playlists (K=30/60/90), POG outfits (K=4), IQON3000 outfits (K=8). Remove bundles shorter than K, truncate longer bundles; IQON3000 also drops outfits with missing images. User/item-frequency filtering not reported.
  - 出处：[S5.SS1.SSS0.Px1.p1](https://arxiv.org/html/2610.34700v1#S5.SS1.SSS0.Px1.p1) ; #S8.SS1.SSS0.Px2.p1
- **切分**：Disjoint bundles: released Spotify/POG partitions (ratios not reported); IQON3000 shuffled outfits split 7:1:2. Each evaluation bundle exposes its first K/2 items and predicts the remainder. Training-only adjacent-swap/random contiguous-K augmentation uses r=0.4 for Spotify, 0.8 for POG/IQON3000.
  - 出处：[S8.SS1.SSS0.Px2.p1](https://arxiv.org/html/2610.34700v1#S8.SS1.SSS0.Px2.p1) ; #S8.SS1.SSS0.Px3.p1
- **候选集**：sampled: 100N total, where N=K/2 targets: Spotify K=30/60/90 uses 1,500/3,000/4,500; POG 200; IQON3000 400. Shared sets contain all N targets plus uniformly sampled non-target items; observed-bundle/user-history exclusion not reported.
  - 出处：[S5.SS1.SSS0.Px4.p1](https://arxiv.org/html/2610.34700v1#S5.SS1.SSS0.Px4.p1) ; #S8.SS1.SSS0.Px2.p1
- **可见性**：warm; no unseen-item protocol is defined. Partitions are bundle-disjoint; CLHE representation fitting and SID-quantizer exposure to validation/test items are not separately reported.
  - 出处：[S5.SS1.SSS0.Px1.p1](https://arxiv.org/html/2610.34700v1#S5.SS1.SSS0.Px1.p1) ; #S8.SS1.SSS0.Px2.p1 ; #S8.SS1.SSS0.Px4.p1
- **SID 规格**：Fixed 64D CLHE features (released Spotify/POG; IQON3000 trained on text/image features); 3 residual-VQ tokens with C=256 for Spotify/IQON3000, 128 for POG. A fourth catalog-order token disambiguates collisions (max 74/53/171 for Spotify/POG/IQON3000). Separate level vocabularies plus boundary/MASK tokens; generated SIDs undergo exact-match or reconstructed-embedding cosine legalization, removing selected candidates for distinct outputs.
  - 出处：[S8.SS1.SSS0.Px4.p1](https://arxiv.org/html/2610.34700v1#S8.SS1.SSS0.Px4.p1) ; #S8.SS1.SSS0.Px4.p3 ; #S8.SS1.SSS0.Px5.p5 ; #S4.SS3.p1
- **推理预算**：Sequential AO teacher reveals one SID token/step; Fast reveals confidence-qualified positions in parallel plus a quota meeting budget F. Numeric default F/threshold, model size and inference batch size not reported. All experiments use one A100-80GB. Per-bundle DPE/Fast latency (ms): Spotify K=30 443.59/62.34, K=60 903.41/65.79, K=90 1340.05/66.72; POG 59.38/46.49; IQON3000 112.51/58.32.
  - 出处：[S4.SS2.SSS0.Px1.p5](https://arxiv.org/html/2610.34700v1#S4.SS2.SSS0.Px1.p5) ; #S4.SS2.SSS0.Px4.p1 ; #S4.SS2.SSS0.Px4.p4 ; #S8.SS2.p1 ; #S5.T2
- **结果来源**：Own training/evaluation of all methods with 5 seeds, reporting mean/std quality and measured latency. Spotify/POG backbone pretraining is from scratch with the DDBC recipe; fixed CLHE representations are shared. Compared generators are UniGRec, DiffGRM and DDBC; no imported recommendation-score source is identified.
  - 出处：[S5.SS1.SSS0.Px3.p1](https://arxiv.org/html/2610.34700v1#S5.SS1.SSS0.Px3.p1) ; #S5.SS1.SSS0.Px2.p1 ; #S8.SS2.p1 ; #S5.T2

</details>

---

### 5. 相关工作

```mermaid
flowchart LR
    P["DPE-Rec"]
    P -->|alternative| A["TIGER"]
```

- **替代方案** · [TIGER](tiger.md): Cited SID-based autoregressive recommendation prior; DPE-Rec contrasts fixed left-to-right generation with bidirectional diffusion for unordered bundle construction.
  - 出处：https://arxiv.org/html/2610.34700v1#S1.p2 (Rajput et al., Recommender Systems with Generative Retrieval)

[查看同格全部论文](../../../README.zh.md#iv--training)
