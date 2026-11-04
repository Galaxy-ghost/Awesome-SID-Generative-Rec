# HiD-VAE

[← Problem × Stage Matrix](../../README.md#ii--tokenization) · [Papers by Stage](../index/stages.md) · [Papers by Modality](../index/modality.md) · [Papers by Domain](../index/domain.md) · English | [中文](../zh/papers/hid-vae.md)

| **Title** | *Interpretable Generative Recommendation via Hierarchical and Disentangled Semantic IDs* |
| :-- | :-- |
| **Authors** | Fang et al. |
| **Venue** | arXiv’25 |
| **Problem × Stage** | `II. Uniqueness and Validity` · `Tokenization` |
| **Changes** | ○ Representation · ● Tokenization |
| **SID inputs** | `Text` + `Attr` |
| **Domain** | `E-commerce` · `Short video / Live` |
| **Scenario** | `General Item Recommendation`; `Public Benchmarks` |
| **Links** | [Paper](https://arxiv.org/abs/2508.04618) · [Code](https://anonymous.4open.science/r/HiD-VAE-84B2) |
| **Reading level** | Reading Notes (Level 2) |

**On this page**: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [1. Why It Matters](#1-why-this-paper-matters) · [2. Method](#2-how-it-works) · [3. Experiments](#3-experimental-findings) · [4. Limitations](#4-limitations--critical-analysis) · [5. Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>○ Text"] --> T["Tokenization<br/>● Hier. RQ"] --> B["Backbone<br/>Enc-Dec"] --> TR["Training<br/>Tokenizer: Fixed<br/>Objective: NTP"] --> I["Inference<br/>C-Beam"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class R other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class T main
```

- `Text`: Textual item metadata (titles, descriptions, categories, or prompts).
- `Hier. RQ`: Hierarchically supervised residual quantization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

> [!NOTE]
> HiD-VAE aligns each Semantic ID level with multi-level item tags through hierarchically supervised quantization and adds a uniqueness loss against ID collisions, instead of flat unsupervised tokenization.

---

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Key Findings | HiD-VAE cuts Semantic ID collision rates to 2.1% on Beauty, 2.8% on Sports, and 1.9% on KuaiRand versus 18.7%, 19.5%, and 17.8% for unsupervised RQ-VAE, outperforming baselines across all three benchmarks (Abstract, Table 1, Table 3). |
| Limitation | Hierarchically supervised quantization requires multi-level category tags, forcing datasets without taxonomies to rely on LLM-synthesized tags (Sec. 3.4). |

---

### 1. Why This Paper Matters

Unsupervised residual quantization produces flat code hierarchies whose entangled latent spaces map distinct items to identical Semantic IDs (SIDs) (Abstract). HiD-VAE supervises each quantization depth with explicit category tags and penalizes latent overlap before discretization.

> "Concurrently, to combat representation entanglement and prevent ID collisions at the source, we design a novel uniqueness loss that directly penalizes the latent representation overlap between distinct items." (Sec. 1)

---

### 2. How It Works

![HiD-VAE architecture diagram](../../architectures/hid-vae.png)

```mermaid
flowchart LR
    subgraph Tag["Taxonomy Preparation"]
        T0("Raw item titles & categories") --> LLM["2-stage LLM retrieval-then-classification"]
        LLM --> Tags("Multi-level category tags")
    end
    subgraph Quant["HiD-VAE Tokenizer (3 levels x 256)"]
        X("Item text (768-d)") --> Q["Hierarchical residual quantizer"]:::key
        Tags --> L1{{"Per-level tag alignment & prediction"}}
        L1 -.-> Q
        L2{{"Latent uniqueness repulsion loss"}}:::key -.-> Q
    end
    Q --> SID("Low-collision SIDs")
    SID --> Gen["6-layer Enc-Dec generator"]
    Gen --> CD{"Valid corpus prefix?"}
    CD -->|yes| Out("Next item")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### Hierarchical Tag Generation

When a catalog lacks multi-level taxonomies (such as KuaiRand), an LLM synthesizes hierarchical tags through a two-stage "retrieval-then-classification" pipeline over item titles and raw categories (Sec. 1, Sec. 3.4).

#### Hierarchically Supervised Quantization

Each RQ-VAE codebook depth aligns with and predicts the corresponding level of item tags, turning the discrete code prefix into an interpretable coarse-to-fine category path (Abstract).

#### Uniqueness Loss

A uniqueness repulsion loss penalizes latent proximity between distinct items prior to nearest-codeword rounding, reducing collisions while spreading items across the codebook (Abstract, Sec. 1).

> "This mechanism not only resolves the critical ID collision problem but also promotes recommendation diversity by ensuring a more comprehensive utilization of the item representation space." (Abstract)

#### Generation

A 6-layer encoder-decoder predicts the target SID from the user's interaction history under valid-prefix constrained decoding (Sec. 3.3).

> "During inference, constrained decoding ensures that generated IDs correspond to valid items." (Sec. 3.3)

---

### 3. Experimental Findings

<details>
<summary>Experimental setup</summary>

- **Datasets**: Amazon Beauty, Sports and Outdoors, and KuaiRand-1K, with 5-core filtering of users and items. Sizes (users / items / interactions): Beauty 22,363 / 12,101 / 198,360; Sports 35,598 / 18,357 / 296,175; KuaiRand 983 / 29,983 / 953,166. KuaiRand category hierarchies are generated by an LLM from titles and raw categories.
  - Source: Datasets and 5-core: [S4.SS1.p1](https://arxiv.org/html/2508.04618v2#S4.SS1.p1) and [S4.I2.i2.p1](https://arxiv.org/html/2508.04618v2#S4.I2.i2.p1); LLM-built hierarchies: [S4.SS1.p3](https://arxiv.org/html/2508.04618v2#S4.SS1.p3); statistics: [A4.T4](https://arxiv.org/html/2508.04618v2#A4.T4).
- **Split**: Per-user leave-one-out: last item for test, second-to-last for validation, the rest for training.
  - Source: Leave-one-out allocation: [S4.SS1.p5](https://arxiv.org/html/2508.04618v2#S4.SS1.p5).
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); generation is constrained to valid ID prefixes.
  - Source: Metrics only: [S4.SS1.p5](https://arxiv.org/html/2508.04618v2#S4.SS1.p5).
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard split with no unseen-item protocol: [S4.SS1.p5](https://arxiv.org/html/2508.04618v2#S4.SS1.p5).
- **SID**: 3-level hierarchically supervised RQ-VAE x 256 codewords (K-means initialized) over 768-dimensional SentenceTransformer embeddings; each level is aligned with a category-tag level, and a uniqueness loss pushes items apart. Measured collision rate 2.1% (Beauty), 2.8% (Sports), 1.9% (KuaiRand) versus 18.7%, 19.5%, and 17.8% for RQ-VAE. How the remaining collisions are resolved in the full model: not reported; the w/o-uniqueness variant uses TIGER's appended integer.
  - Source: L=3 x K=256, K-means initialization, SentenceTransformer input: [S4.SS1.p6](https://arxiv.org/html/2508.04618v2#S4.SS1.p6); uniqueness loss: [S3.SS6.p1](https://arxiv.org/html/2508.04618v2#S3.SS6.p1); collision rates: [S4.T3](https://arxiv.org/html/2508.04618v2#S4.T3); TIGER suffix only in the w/o DUL variant: [S4.I4.i4.p1](https://arxiv.org/html/2508.04618v2#S4.I4.i4.p1).
- **Inference budget**: Autoregressive generation with constrained decoding against a corpus cache; beam width not reported. 6-layer encoder-decoder (8 heads, hidden 512). Training on NVIDIA 4060 GPUs with FP16; inference batch size and latency: not reported.
  - Source: Constrained decoding: [S4.SS1.p6](https://arxiv.org/html/2508.04618v2#S4.SS1.p6); hardware: [S4.SS1.p6](https://arxiv.org/html/2508.04618v2#S4.SS1.p6).
- **Results from**: Table 1 (Beauty, Sports, KuaiRand versus traditional, Transformer, and generative baselines); Table 2 (ablations of tag alignment, tag prediction, uniqueness loss); Table 3 (ID collision rates).
  - Source: Main: [S4.T1](https://arxiv.org/html/2508.04618v2#S4.T1); ablation: [S4.T2](https://arxiv.org/html/2508.04618v2#S4.T2); collisions: [S4.T3](https://arxiv.org/html/2508.04618v2#S4.T3).

</details>

- Main comparison and collisions: across Amazon Beauty, Sports and Outdoors, and KuaiRand, HiD-VAE outperforms traditional, sequential, and generative baselines while lowering SID collision rates from 18.7% / 19.5% / 17.8% (RQ-VAE) to 2.1% / 2.8% / 1.9% (Abstract, Table 1, Table 3).

---

### 4. Limitations & Critical Analysis

**Our analysis.**

- TIGER pairs unsupervised `RQ-VAE` codes with unconstrained `Beam` search and integer collision suffixes; HiD-VAE supervises `Hier. RQ` codebooks with category tags, repels colliding latents during training, and applies constrained decoding.

---

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["HiD-VAE"]
    P -->|"competitor"| A["TIGER"]
    P -->|"competitor"| B["LC-Rec"]
    P -->|"competitor"| C["VQ-Rec"]
    P -->|"alternative"| D["AdaSID"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C,D peer
```

- **Competitor** · [TIGER](tiger.md): TIGER resolves collisions by appending an integer after unsupervised RQ-VAE; HiD-VAE supervises each level with category tags and adds a uniqueness loss so that fewer items collide.
  - Source: HiD-VAE v2, baselines and Table 1: [S4.SS1.p4](https://arxiv.org/html/2508.04618v2#S4.SS1.p4) and [S4.T1](https://arxiv.org/html/2508.04618v2#S4.T1); TIGER-style suffix in the ablation: [S4.I4.i4.p1](https://arxiv.org/html/2508.04618v2#S4.I4.i4.p1) and [S4.I5.i2.p1](https://arxiv.org/html/2508.04618v2#S4.I5.i2.p1).
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec aligns an LLM to RQ-VAE codes; HiD-VAE changes the tokenizer and keeps a small encoder-decoder; LC-Rec is run with a T5-base backbone for scale parity.
  - Source: HiD-VAE v2, baselines: [S4.SS1.p4](https://arxiv.org/html/2508.04618v2#S4.SS1.p4) and [S4.SS1.p7](https://arxiv.org/html/2508.04618v2#S4.SS1.p7); Table 1: [S4.T1](https://arxiv.org/html/2508.04618v2#S4.T1).
- **Competitor** · [VQ-Rec](vq-rec.md): VQ-Rec's product-quantized codes are adapted to generation here and collide more often (21.2% on Beauty) than HiD-VAE's hierarchical codes.
  - Source: HiD-VAE v2, baselines and adaptation: [S4.SS1.p4](https://arxiv.org/html/2508.04618v2#S4.SS1.p4) and [S4.I3.i2.p1](https://arxiv.org/html/2508.04618v2#S4.I3.i2.p1); Tables 1 and 3: [S4.T1](https://arxiv.org/html/2508.04618v2#S4.T1) and [S4.T3](https://arxiv.org/html/2508.04618v2#S4.T3).
- **Alternative** · [AdaSID](adasid.md): AdaSID later argues that HiD-VAE's overlap-aware objective treats collisions under a fixed standard, and makes the repulsion adaptive.
  - Source: Evidence is from the later AdaSID paper, Sections 1 and 2.2: [S1.p3](https://arxiv.org/html/2604.23522v1#S1.p3) and [S2.SS2.p1](https://arxiv.org/html/2604.23522v1#S2.SS2.p1).

[View all papers in this cell](../../README.md#ii--tokenization)
