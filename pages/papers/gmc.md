# GMC

*Generative Multi-Target Cross-Domain Recommendation* — Jin et al. · arXiv’25

`VI. Generalization` · `Tokenization`

[Paper](https://arxiv.org/abs/2507.12871) · [Matrix](../../README.md#vi--tokenization)

Reading level: Reading Notes (Level 2) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [1. Why This Paper Matters](#1-why-this-paper-matters) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [4. Limitations & Critical Analysis](#4-limitations--critical-analysis) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Cross-Dom` | **`Unified RQ`** | `Enc-Dec` | `Fixed / NTP` | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

GMC assigns domain-shared Semantic IDs with a domain-aware contrastive loss and trains one sequence-to-sequence generator across domains, instead of relying on users or items shared between domains.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Key Contribution | GMC assigns domain-shared Semantic IDs with a domain-aware contrastive loss and trains one sequence-to-sequence generator across domains, instead of relying on users or items shared between domains. |
| Modified Stage | Tokenization |
| Limitation | The Semantic IDs (SIDs) come from text embeddings only, so collaborative signals reach the model only through the generator's training sequences (Sec. 3). |

### 1. Why This Paper Matters

Existing multi-target cross-domain recommendation (MTCDR) methods rely on users or items shared between domains, which non-overlapped scenarios do not have (Abstract). Methods based on domain-sharable semantic representations often need extensive auxiliary data for pre-training (Abstract).

> "The core idea of GMC is to leverage semantically quantized discrete item identifiers as a medium for integrating multi-domain knowledge within a unified generative model." (Abstract)

Based on arXiv v3.

### 2. How It Works

![GMC architecture diagram](../../architectures/gmc.png)

*Figure source: Fig. 2, original paper.*

```mermaid
flowchart LR
    A[Item text] --> B[LLM embeddings]
    B --> C[Residual quantization]
    C --> D[Shared SIDs]
    D --> E[Unified generator]
    E --> F[Domain LoRA]
```

#### Semantic Identifier Learning

GMC quantizes LLM text embeddings with residual vector quantization into SIDs shared across domains (Sec. 3). A domain-aware contrastive loss is added to this step (Sec. 3.3, Eq. 6).

> "Specifically, since items within the same domain are generally more similar to each other than items from different domains, we introduce a novel domain-aware contrastive loss that brings quantized embeddings of intra-domain items closer together." (Sec. 1)

#### Domain-Specific Fine-Tuning

After unified training, each domain gets its own LoRA module (Sec. 1, Sec. 3.5).

> "Specifically, we incorporate domain-specific LoRA modules (Hu et al., 2022) into the unified recommender and update the corresponding LoRA parameters using domain-specific data, while freezing all other parameters of the unified model." (Sec. 1)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Multi-target cross-domain task on five Amazon 2018 Reviews subsets: Scientific, Pantry, Instruments, Arts, Office. Items without titles are removed and 5-core filtering is applied to users and items; sequences capped at 20 items. Sizes (users / items): 8,317 / 4,344; 13,073 / 4,897; 24,772 / 9,922; 45,141 / 20,956; 86,554 / 25,847.
  - Source: Five Amazon subsets, title filter, 5-core, length 20: https://arxiv.org/html/2507.12871v3#S5.SS1.SSS1.p1; statistics: https://arxiv.org/html/2507.12871v3#S5.T2.
- **Split**: Per-user leave-one-out: last item for test, second latest for validation, the rest for training; results reported per domain and as a user-weighted average.
  - Source: Leave-one-out allocation: https://arxiv.org/html/2507.12871v3#S5.SS1.SSS3.p1.
- **Candidates**: full catalog (the target item is ranked over the entire item set).
  - Source: Ranking over the entire item set: https://arxiv.org/html/2507.12871v3#S5.SS1.SSS3.p1.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2507.12871v3#S5.SS1.SSS3.p1.
- **SID**: 4-level RQ-VAE x 256 codewords (dimension 32) over LLaMA-3.1-8B text embeddings (D=4,096), with a codebook shared across domains and a domain-aware contrastive loss; first-level codes separate domains and deeper levels are shared. Collision handling: not reported.
  - Source: L=4 x N=256, d=32, LLaMA-3.1 4,096-dimensional embeddings, shared codebook across domains: https://arxiv.org/html/2507.12871v3#S5.SS1.SSS4.p1 and https://arxiv.org/html/2507.12871v3#S5.SS4.SSS1.p2; no collision rule found.
- **Inference budget**: Beam size 20 for item generation; T5-small backbone with domain-specific LoRA. Recall and NDCG at K=5 and 10. Hardware, inference batch size, and latency: not reported.
  - Source: Beam size 20: https://arxiv.org/html/2507.12871v3#S5.SS1.SSS4.p2; T5-small backbone: https://arxiv.org/html/2507.12871v3#S5.SS1.SSS4.p2.
- **Results from**: Table 3 (five domains and user-weighted average versus ID, ID-text, pre-training, and generative baselines); Table 4 (ablations); Figures 3-5 (code sharing, code similarity, multi-domain settings).
  - Source: Main: https://arxiv.org/html/2507.12871v3#S5.T3; ablation: https://arxiv.org/html/2507.12871v3#S5.T4; code analysis: https://arxiv.org/html/2507.12871v3#S5.F3 and https://arxiv.org/html/2507.12871v3#S5.F4; domain settings: https://arxiv.org/html/2507.12871v3#S5.F5.

- Main comparison: on five public datasets, GMC reports better performance than a range of baselines (Abstract).

### 4. Limitations & Critical Analysis

**Our analysis.**

- The contrastive loss pulls items of one domain together. This suggests a trade-off with code sharing across domains.
- VQ-Rec also transfers across domains, with `OPQ` codes in an `Encoder` and `Scoring`; GMC generates `Unified RQ` codes with an `Enc-Dec` generator.

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER learns one-domain RQ-VAE identifiers; GMC learns a domain-shared codebook with a domain-aware contrastive loss and adds domain-specific LoRA tuning to a unified generator.
  - Source: GMC v3, generative baselines: https://arxiv.org/html/2507.12871v3#S5.I1.i4.I1.i2.p1; Table 1 comparison: https://arxiv.org/html/2507.12871v3#S3.T1; Table 3: https://arxiv.org/html/2507.12871v3#S5.T3.
- **Competitor** · [VQ-Rec](vq-rec.md): VQ-Rec transfers across domains through vector-quantized codes for a discriminative model, pre-trained here on the five target domains; GMC generates shared semantic identifiers.
  - Source: GMC v3, pre-training baselines with the adapted setting: https://arxiv.org/html/2507.12871v3#S5.I1.i3.p1 and https://arxiv.org/html/2507.12871v3#S5.I1.i3.I1.i2.p1; Table 3: https://arxiv.org/html/2507.12871v3#S5.T3.
- **Competitor** · [CID](cid.md): P5-CID builds collaborative identifiers by spectral clustering within a domain; GMC builds semantic identifiers shared across domains.
  - Source: GMC v3, generative baselines: https://arxiv.org/html/2507.12871v3#S5.I1.i4.I1.i1.p1; Table 3: https://arxiv.org/html/2507.12871v3#S5.T3.
- **Competitor** · [IDGenRec](idgenrec.md): IDGenRec learns textual IDs with an ID generator; GMC quantizes LLM embeddings into codebook IDs shared across domains.
  - Source: GMC v3, generative baselines: https://arxiv.org/html/2507.12871v3#S5.I1.i4.I1.i3.p1; Table 3: https://arxiv.org/html/2507.12871v3#S5.T3.

[View all papers in this cell](../../README.md#vi--tokenization)
