# DPE-Rec

*Diversity-Preserving and Efficient Diffusion Language Model Recommendation for Bundle Construction* — Ma et al. · arXiv’26

`IV. Utility` · `Training` · [Paper](https://arxiv.org/abs/2610.34700) · [Matrix](../../README.md#iv--training) · [中文](../zh/papers/dpe-rec.md)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

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
> DPE-Rec completes bundles with a diffusion language model, adding semantic-fork-aware GRPO to keep bundles diverse and pseudo-trajectory distillation to reveal more tokens per denoising step.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Key Contribution | DPE-Rec completes bundles with a diffusion language model, adding semantic-fork-aware GRPO to keep bundles diverse and pseudo-trajectory distillation to reveal more tokens per denoising step. |
| Modified Stage | Training |

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Spotify playlists (K=30/60/90), POG outfits (K=4), IQON3000 outfits (K=8). Remove bundles shorter than K, truncate longer bundles; IQON3000 also drops outfits with missing images. User/item-frequency filtering not reported.
  - Source: [S5.SS1.SSS0.Px1.p1](https://arxiv.org/html/2610.34700v1#S5.SS1.SSS0.Px1.p1) ; #S8.SS1.SSS0.Px2.p1
- **Split**: Disjoint bundles: released Spotify/POG partitions (ratios not reported); IQON3000 shuffled outfits split 7:1:2. Each evaluation bundle exposes its first K/2 items and predicts the remainder. Training-only adjacent-swap/random contiguous-K augmentation uses r=0.4 for Spotify, 0.8 for POG/IQON3000.
  - Source: [S8.SS1.SSS0.Px2.p1](https://arxiv.org/html/2610.34700v1#S8.SS1.SSS0.Px2.p1) ; #S8.SS1.SSS0.Px3.p1
- **Candidates**: sampled: 100N total, where N=K/2 targets: Spotify K=30/60/90 uses 1,500/3,000/4,500; POG 200; IQON3000 400. Shared sets contain all N targets plus uniformly sampled non-target items; observed-bundle/user-history exclusion not reported.
  - Source: [S5.SS1.SSS0.Px4.p1](https://arxiv.org/html/2610.34700v1#S5.SS1.SSS0.Px4.p1) ; #S8.SS1.SSS0.Px2.p1
- **Visibility**: warm; no unseen-item protocol is defined. Partitions are bundle-disjoint; CLHE representation fitting and SID-quantizer exposure to validation/test items are not separately reported.
  - Source: [S5.SS1.SSS0.Px1.p1](https://arxiv.org/html/2610.34700v1#S5.SS1.SSS0.Px1.p1) ; #S8.SS1.SSS0.Px2.p1 ; #S8.SS1.SSS0.Px4.p1
- **SID**: Fixed 64D CLHE features (released Spotify/POG; IQON3000 trained on text/image features); 3 residual-VQ tokens with C=256 for Spotify/IQON3000, 128 for POG. A fourth catalog-order token disambiguates collisions (max 74/53/171 for Spotify/POG/IQON3000). Separate level vocabularies plus boundary/MASK tokens; generated SIDs undergo exact-match or reconstructed-embedding cosine legalization, removing selected candidates for distinct outputs.
  - Source: [S8.SS1.SSS0.Px4.p1](https://arxiv.org/html/2610.34700v1#S8.SS1.SSS0.Px4.p1) ; #S8.SS1.SSS0.Px4.p3 ; #S8.SS1.SSS0.Px5.p5 ; #S4.SS3.p1
- **Inference budget**: Sequential AO teacher reveals one SID token/step; Fast reveals confidence-qualified positions in parallel plus a quota meeting budget F. Numeric default F/threshold, model size and inference batch size not reported. All experiments use one A100-80GB. Per-bundle DPE/Fast latency (ms): Spotify K=30 443.59/62.34, K=60 903.41/65.79, K=90 1340.05/66.72; POG 59.38/46.49; IQON3000 112.51/58.32.
  - Source: [S4.SS2.SSS0.Px1.p5](https://arxiv.org/html/2610.34700v1#S4.SS2.SSS0.Px1.p5) ; #S4.SS2.SSS0.Px4.p1 ; #S4.SS2.SSS0.Px4.p4 ; #S8.SS2.p1 ; #S5.T2
- **Results from**: Own training/evaluation of all methods with 5 seeds, reporting mean/std quality and measured latency. Spotify/POG backbone pretraining is from scratch with the DDBC recipe; fixed CLHE representations are shared. Compared generators are UniGRec, DiffGRM and DDBC; no imported recommendation-score source is identified.
  - Source: [S5.SS1.SSS0.Px3.p1](https://arxiv.org/html/2610.34700v1#S5.SS1.SSS0.Px3.p1) ; #S5.SS1.SSS0.Px2.p1 ; #S8.SS2.p1 ; #S5.T2

</details>

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["DPE-Rec"]
    P -->|alternative| A["TIGER"]
```

- **Alternative** · [TIGER](tiger.md): Cited SID-based autoregressive recommendation prior; DPE-Rec contrasts fixed left-to-right generation with bidirectional diffusion for unordered bundle construction.
  - Source: https://arxiv.org/html/2610.34700v1#S1.p2 (Rajput et al., Recommender Systems with Generative Retrieval)

[View all papers in this cell](../../README.md#iv--training)
