# CARD

[← Problem × Stage Matrix](../../README.md#ii--tokenization) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · English | [中文](../zh/papers/card.md)

| **Title** | *Non-Uniform Quantization of Visual Semantic Unit for Generative Recommendation* |
| :-- | :-- |
| **Authors** | Wei et al. |
| **Venue** | arXiv’26 |
| **Problem × Stage** | `II. Uniqueness and Validity` · `Tokenization` |
| **Links** | [Paper](https://arxiv.org/abs/2604.26427) · [Code](https://github.com/HAI-UESTC/CARD) |
| **Reading level** | Overview (Level 1) |

**On this page**: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experiments](#3-experimental-findings) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text+Img+CF"] --> T["Tokenization<br/>NU-RQ"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Fixed / NTP"] --> I["Inference<br/>C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text+Img+CF`: Text and image representations combined with collaborative signals.
- `NU-RQ`: Non-uniform RQ variant.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> CARD fuses text, image, and collaborative signals into a visual semantic unit before encoding and quantizes it with NU-RQ-VAE, whose learnable non-uniform transformation balances skewed embeddings.

---

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Key Contribution | CARD fuses text, image, and collaborative signals into a visual semantic unit before encoding and quantizes it with NU-RQ-VAE, whose learnable non-uniform transformation balances skewed embeddings. |
| Modified Stage | Tokenization |

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Reviews: Grocery and Gourmet Food (Food), Cell Phones and Accessories (Phones), and Clothing, Shoes and Jewelry (Clothing), with 5-core filtering of users and items. Sizes (users / items / interactions): Food 14,681 / 8,713 / 151,254; Phones 27,879 / 10,429 / 194,439; Clothing 39,387 / 23,033 / 278,677.
  - Source: Categories, 5-core filtering, truncation: [S4.SS1.SSS1.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS1.p1); statistics: [S4.T1](https://arxiv.org/html/2604.26427v1#S4.T1).
- **Split**: Per-user leave-one-out: most recent interaction for test, second most recent for validation, the rest for training; histories truncated or padded to the 20 most recent items.
  - Source: Leave-one-out allocation and history length: [S4.SS1.SSS1.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS1.p1).
- **Candidates**: full catalog
  - Source: Full ranking over the entire item set: [S4.SS1.SSS2.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS2.p1).
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard leave-one-out with no cold-start experiment: [S4.SS1.SSS1.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS1.p1).
- **SID**: 4 non-uniform RQ-VAE levels x 256 codewords (dimension 32), quantizing a vision-language embedding of a 512 x 512 rendered card (item image, title, collaborative-neighbor thumbnails). Collision handling: not reported.
  - Source: K=4 codebooks x 256 vectors of dimension 32: [S4.SS1.SSS3.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS3.p1); non-uniform RQ-VAE over a vision-language encoding of a rendered item card: [S3.SS2.SSS1.p1](https://arxiv.org/html/2604.26427v1#S3.SS2.SSS1.p1) and [S4.SS1.SSS3.p2](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS3.p2); no collision rule found in Sections 3-4.
- **Inference budget**: Beam search over the code vocabulary; numerical beam width not reported. T5-style encoder-decoder with 4 layers each and 6 heads. Recall and NDCG at K=5, 10, and 20. Hardware, inference batch size, and latency: not reported.
  - Source: Beam search with top-B partial sequences, no numerical B: [S3.SS3.p2](https://arxiv.org/html/2604.26427v1#S3.SS3.p2); backbone: [S4.SS1.SSS3.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS3.p1).
- **Results from**: Table 2 (Food, Phones, Clothing; paired t-tests against the best baseline); Tables 3-4 (ablations of the two CARD variants); Table 5 (non-uniform quantization with different quantizers); Table 6 (text-only encoding).
  - Source: Main table: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2); ablations: [S4.T3](https://arxiv.org/html/2604.26427v1#S4.T3) and [S4.T4](https://arxiv.org/html/2604.26427v1#S4.T4); plug-in quantizers: [S4.T5](https://arxiv.org/html/2604.26427v1#S4.T5); text-only variants: [S4.T6](https://arxiv.org/html/2604.26427v1#S4.T6).

</details>

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["CARD"]
    P -->|"competitor"| A["MACRec"]
    P -->|"competitor"| B["MQL4GRec"]
    P -->|"competitor"| C["LETTER"]
    P -->|"competitor"| D["TIGER"]
    P -->|"competitor"| E["VQ-Rec"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D,E peer
```

- **Competitor** · [MACRec](macrec.md): MACRec reduces codebook conflicts by cross-modal quantization and multi-aspect alignment of separate modalities; CARD renders image, title, and neighbors into one card and quantizes it with a non-uniform RQ-VAE.
  - Source: CARD v1, Section 4.1.4 baselines: [S4.I1.i9.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i9.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2); Section 2.1: [S2.SS1.p1](https://arxiv.org/html/2604.26427v1#S2.SS1.p1).
- **Competitor** · [MQL4GRec](mql4grec.md): MQL4GRec quantizes each modality into its own SIDs with pre-training; CARD uses one unified visual semantic unit, and the comparison disables MQL4GRec's extra-category pre-training.
  - Source: CARD v1, Section 4.1.4 baselines: [S4.I1.i8.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i8.p1); implementation note on pre-training: [S4.SS1.SSS3.p1](https://arxiv.org/html/2604.26427v1#S4.SS1.SSS3.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2).
- **Competitor** · [LETTER](letter.md): LETTER regularizes a uniform RQ-VAE with collaborative and diversity terms; CARD changes the quantizer to a non-uniform one and the input to a rendered multimodal card.
  - Source: CARD v1, Section 4.1.4 baselines: [S4.I1.i7.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i7.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2).
- **Competitor** · [TIGER](tiger.md): TIGER quantizes text embeddings with a uniform RQ-VAE; CARD keeps the same codebook shape and generator but replaces the input and the quantization rule.
  - Source: CARD v1, Section 4.1.4 baselines: [S4.I1.i6.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i6.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2); Table 6 text-only TIGER variants: [S4.T6](https://arxiv.org/html/2604.26427v1#S4.T6).
- **Competitor** · [VQ-Rec](vq-rec.md): VQ-Rec pools product-quantized code embeddings in a discriminative model; CARD generates hierarchical non-uniform RQ codes autoregressively.
  - Source: CARD v1, Section 4.1.4 baselines: [S4.I1.i5.p1](https://arxiv.org/html/2604.26427v1#S4.I1.i5.p1); Table 2: [S4.T2](https://arxiv.org/html/2604.26427v1#S4.T2).

[View all papers in this cell](../../README.md#ii--tokenization)
