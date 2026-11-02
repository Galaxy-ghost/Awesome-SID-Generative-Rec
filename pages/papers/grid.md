# GRID

*Generative Recommendation with Semantic IDs: A Practitioner's Handbook* — Ju et al. · CIKM’25

`Paradigms, Systems and Benchmarks` · `No single stage`

[Paper](https://arxiv.org/abs/2507.22224) · [Code](https://github.com/snap-research/GRID) · [Matrix](../../README.md#paradigms-systems-and-benchmarks)

Reading level: Reading Notes (Level 2) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [1. Why This Paper Matters](#1-why-this-paper-matters) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [4. Limitations & Critical Analysis](#4-limitations--critical-analysis) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `R-KM` | `Enc-Dec` | `Fixed / NTP` | `Beam` |

- `R-KM`: Residual k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### TL;DR

GRID is an open-source modular framework, not a new recommender: it makes components of Semantic ID generative recommenders swappable and ablates them on public benchmarks.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | Paradigms, Systems and Benchmarks: Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| Key Contribution | GRID is an open-source modular framework, not a new recommender: it makes components of Semantic ID generative recommenders swappable and ablates them on public benchmarks. |
| Modified Stage | No single stage |

### 1. Why This Paper Matters

Varied modeling techniques, hyperparameters, and experimental setups make direct comparisons between generative recommendation (GR) proposals difficult (Abstract). GRID gives these proposals one modular framework in which components can be swapped and ablated.

> "Our comprehensive experiments with GRID reveal that many overlooked architectural components in GR models with SIDs substantially impact performance." (Abstract)

Based on arXiv v1.

### 2. How It Works

![GRID architecture diagram](../../architectures/grid.png)

*Figure source: Fig. 1(a) and Fig. 1(b), original paper.*

```mermaid
flowchart LR
    A[Item content] --> B[Semantic encoder]
    B --> C[SID tokenizer]
    C --> D[Generator]
    D --> E[Beam search]
```

#### Tokenization then Generation

GRID splits GR with Semantic IDs (SIDs) into a tokenization phase and a generation phase (Sec. 3.1).

#### Tokenization Ablations

The study varies the tokenizer algorithm, the size of the semantic encoder, and the number of residual layers $`L`$ and tokens per layer $`W`$ (Sec. 4.1).

> "Unless otherwise noted, we use RK-Means with (L,W)=(3,256) and Flan-T5-XL." (Sec. 4.1)

#### Generation Ablations

The study varies the number of user tokens, encoder-decoder versus decoder-only, data augmentation, de-duplication IDs, and constrained versus unconstrained beam search (Sec. 4.2).

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: 5-core filtered Amazon Beauty, Sports, and Toys; item text from Title, Categories, Description, and Price. Retained corpus sizes: not reported in the body.
  - Source: 5-core Amazon datasets and text features: https://arxiv.org/html/2507.22224v1#S4.p2.
- **Split**: Per-user leave-last-out: last item for test, second-to-last for validation, the rest for training; sliding-window training samples; averages over 5 seeds.
  - Source: Leave-last-out allocation and 5 seeds: https://arxiv.org/html/2507.22224v1#S4.p2.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); top-K lists from beam search.
  - Source: Metrics only: https://arxiv.org/html/2507.22224v1#S4.p2.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2507.22224v1#S4.p2.
- **SID**: Benchmark default: RK-Means with 3 levels x 256 tokens over mean-pooled Flan-T5-XL embeddings; also R-VQ and RQ-VAE, and L x W variants (e.g. 3 x 128, 3 x 512, 2 x 256). Collisions: Table 7 compares TIGER-style appended-digit de-duplication with randomly selecting one item when SIDs conflict; which one is the default setting is not stated.
  - Source: Default RK-Means (3, 256) with Flan-T5-XL: https://arxiv.org/html/2507.22224v1#S4.SS1.p1; dimension study: https://arxiv.org/html/2507.22224v1#S3.T3; de-duplication strategies: https://arxiv.org/html/2507.22224v1#S4.SS2.p5 and https://arxiv.org/html/2507.22224v1#S4.T7.
- **Inference budget**: Beam search with KV cache; constrained and unconstrained beam compared (Table 8), with unconstrained stated to be cheaper; numerical beam width not reported. Tokenizers trained on 8 GPUs (per-device batch 2,048); generator training batch 256; inference hardware, batch size, and latency: not reported.
  - Source: Beam search with KV cache: https://arxiv.org/html/2507.22224v1#S3.SS1.p3; constrained versus free-form beam: https://arxiv.org/html/2507.22224v1#S4.SS2.p6 and https://arxiv.org/html/2507.22224v1#S4.T8; tokenizer GPUs: https://arxiv.org/html/2507.22224v1#S4.p2.
- **Results from**: Tables 1-3 (tokenizer algorithm, encoder size, codebook dimensions); Tables 4-8 (user tokens, encoder-decoder versus decoder-only, augmentation, SID de-duplication, constrained versus free-form beam). Tables 3 and 4 cover Beauty only; the other tables cover Beauty, Sports, and Toys; results average 5 seeds.
  - Source: Tables 1-8: https://arxiv.org/html/2507.22224v1#S3.T1, https://arxiv.org/html/2507.22224v1#S3.T2, https://arxiv.org/html/2507.22224v1#S3.T3, https://arxiv.org/html/2507.22224v1#S4.T4, https://arxiv.org/html/2507.22224v1#S4.T5, https://arxiv.org/html/2507.22224v1#S4.T6, https://arxiv.org/html/2507.22224v1#S4.T7, https://arxiv.org/html/2507.22224v1#S4.T8.

- Main finding: several components assumed essential, which often cost compute or engineering, can be replaced with more efficient alternatives without losing performance (Sec. 5).

  > "Conversely, other, often overlooked design choices prove to be vital, such as encoder-decoder architectures and data augmentation." (Sec. 5)

### 4. Limitations & Critical Analysis

**Our analysis.**

- The ablations change one component at a time against a default configuration (Sec. 4.1). This suggests that interactions between components are not covered.
- TIGER uses `RQ-VAE` codes; GRID's default uses `R-KM` codes, the same tokenization as OneRec.

### 5. Connections to Related Work

- **Predecessor** · [TIGER](tiger.md): TIGER's RQ-VAE tokenizer, user tokens, and appended-digit de-duplication are the components that GRID ablates in one open framework.
  - Source: GRID v1, Section 4.1 on RQ-VAE as the TIGER default: https://arxiv.org/html/2507.22224v1#S4.SS1.p2; Table 4 (TIGER-style user tokens): https://arxiv.org/html/2507.22224v1#S4.T4; Section 4.2 de-duplication: https://arxiv.org/html/2507.22224v1#S4.SS2.p5.
- **Predecessor** · [OneRec](onerec.md): GRID's default RK-Means tokenizer is taken from OneRec; GRID compares it with R-VQ and RQ-VAE.
  - Source: GRID v1, Section 4 setup cites Deng et al. (2025) for RK-Means: https://arxiv.org/html/2507.22224v1#S4.p2; Table 1: https://arxiv.org/html/2507.22224v1#S3.T1.

[View all papers in this cell](../../README.md#paradigms-systems-and-benchmarks)
