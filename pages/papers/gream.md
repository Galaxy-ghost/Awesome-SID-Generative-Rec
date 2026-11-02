# GREAM

*Generative Reasoning Recommendation via LLMs* — Hong et al. · arXiv’25

`III. SID–Model Alignment` · `Training`

[Paper](https://arxiv.org/abs/2510.20815) · [Code](https://github.com/Indolent-Kawhi/GRRM) · [Matrix](../../README.md#iii--training)

Reading level: Reading Notes (Level 2) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [1. Why This Paper Matters](#1-why-this-paper-matters) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [4. Limitations & Critical Analysis](#4-limitations--critical-analysis) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `RQ-KM` | `Dec-Only` | **`Fixed / NTP → RL`** | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).

### TL;DR

GREAM adapts an LLM into a reasoning recommender with collaborative-semantic item indices, a chain-of-thought curriculum, and SRPO post-training, and supports direct and reasoning-first inference modes.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Key Contribution | GREAM adapts an LLM into a reasoning recommender with collaborative-semantic item indices, a chain-of-thought curriculum, and SRPO post-training, and supports direct and reasoning-first inference modes. |
| Modified Stage | Training |
| Limitation | The item indices depend on descriptions rewritten by GPT-5, and the reasoning data comes from an external LLM, so reproduction depends on access to those models (Sec. 4.1, Sec. 4.2). |

### 1. Why This Paper Matters

The authors state that LLMs face two obstacles as generative reasoning recommenders: the gap between textual semantics and collaborative filtering signals, and sparse, stochastic user feedback (Abstract). GREAM targets both while keeping a fast direct mode next to a reasoning mode.

> "GREAM natively supports two complementary inference modes: Direct Sequence Recommendation for high-throughput, low-latency deployment, and Sequential Reasoning Recommendation that first emits an interpretable reasoning chain for causal transparency." (Abstract)

Based on arXiv v1.

### 2. How It Works

![GREAM architecture diagram](../../architectures/gream.png)

*Figure source: Fig. 2, original paper.*

```mermaid
flowchart LR
    A[Item text and reviews] --> B[Rewritten description]
    B --> C[RQ-KMeans indices]
    C --> D[Alignment SFT]
    D --> E[Reasoning curriculum]
    E --> F[SRPO]
```

#### Collaborative-Semantic Alignment

For each item, GPT-5 rewrites the title, the official description, and selected reviews into one description (Sec. 4.1). RQ-KMeans quantizes its embedding into item indices (Sec. 4.1, Eq. 4-5). Auxiliary tasks ground the language representations in interaction semantics (Abstract).

#### Reasoning Curriculum Activation

An external LLM generates structured reasoning paths by reverse reasoning from the recommendation (Sec. 4.2).

> "This process guides the model through a structured, five-stage logical chain—behavioral evidence extraction, latent preference modeling, intent inference, recommendation formulation, and denoised sequence rewriting" (Sec. 1)

#### SRPO

Sparse-Regularized Group Policy Optimization (SRPO) uses a Residual-Sensitive Verifiable Reward and Bonus-Calibrated Group Advantage Estimation to optimize despite sparse successes (Abstract).

> "In the early stages of generative recommendation, exactly correct generations are typically rare." (Sec. 5.2)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Beauty, Sports and Outdoors, Musical Instruments, with 5-core filtering of users and items. Sizes (users / items / interactions): 22,363 / 12,101 / 198,360; 35,598 / 18,357 / 296,175; 24,733 / 9,923 / 206,153. Alignment and reasoning text is synthesized by Qwen3, GPT-5, Llama-3.1, and Gemini.
- **Split**: Leave-one-out; the exact validation/test position allocation is not reported beyond the leave-one-out label.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); direct mode reports Recall and NDCG at 5 and 10, reasoning mode reports Pass@1, 5, 10.
- **Visibility**: warm; no unseen-item protocol is defined.
- **SID**: RQ-KMeans indices over LLM last-hidden-state embeddings of GPT-5-enriched item text; fixed length 5 with 256 values per layer, where the fifth position is a conflict-resolution slot.
- **Inference budget**: Direct mode: beam size 20 for all generative methods. Reasoning mode: sampling with temperature 0.7 and top-p 0.9. Backbone Qwen3-4B-Instruct; experiments on a cluster of 24 NVIDIA A100 GPUs; inference batch size and latency: not reported.
- **Results from**: Table 2 (direct and reasoning modes on Beauty, Sports, Instruments versus traditional, Transformer, generative, and LLM baselines); Table 3 (alignment and RL ablations); Table 4 (data composition); Figure 3 (RL regimes on Instruments).

<details>
<summary>Sources</summary>

- **Datasets**: Datasets and 5-core: [S6.SS1.SSS1.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS1.p1); statistics: [S6.T1](https://arxiv.org/html/2510.20815v1#S6.T1).
- **Split**: Leave-one-out named only: [S6.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS2.p1).
- **Candidates**: Metrics only: [S6.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS2.p1).
- **Visibility**: Standard split with no unseen-item protocol: [S6.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS2.p1).
- **SID**: Length 5 with a conflict-resolution slot, 256 values per layer: [S6.SS1.SSS3.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS3.p1); RQ-KMeans over LLM embeddings of GPT-5-enriched text: [S3.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S3.SS1.SSS2.p1) and [S4.SS1.p1](https://arxiv.org/html/2510.20815v1#S4.SS1.p1).
- **Inference budget**: Beam 20 and sampling settings: [S6.SS1.SSS2.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS2.p1); hardware: [S6.SS1.SSS3.p1](https://arxiv.org/html/2510.20815v1#S6.SS1.SSS3.p1).
- **Results from**: Main: [S6.T2](https://arxiv.org/html/2510.20815v1#S6.T2); ablations: [S6.T3](https://arxiv.org/html/2510.20815v1#S6.T3) and [S6.T4](https://arxiv.org/html/2510.20815v1#S6.T4); RL regimes: [S6.SS5.p2](https://arxiv.org/html/2510.20815v1#S6.SS5.p2).

</details>

- Main comparison: on three public benchmarks, GREAM reports consistent gains over generative and LLM baselines in both direct and reasoning settings (Abstract).
- Index quality: RQ-KMeans on the enriched embeddings reduces index collision rates by about 50% (Sec. 4.1).
- Reasoning scaling: more synthetic Chain-of-Thought data in Reasoning Activation raises Pass@Avg almost linearly across 10^16–10^19 training FLOPs (Sec. 6.4, Fig. 1).

### 4. Limitations & Critical Analysis

**Our analysis.**

- The reasoning mode emits a chain before the item index. This suggests higher latency than the direct mode.
- LC-Rec and EAGER-LLM train their LLMs with `Multi-task NTP`; GREAM adds an RL stage (`NTP → RL`).

### 5. Connections to Related Work

- **Competitor** · [EAGER-LLM](eager-llm.md): EAGER-LLM injects behavioral and semantic signals into a decoder-only LLM recommender; GREAM adds collaborative-semantic alignment data, reasoning curricula, and RL with a prefix-based verifiable reward.
  - Source: GREAM v1, LLM-based baselines: https://arxiv.org/html/2510.20815v1#A2.I4.i2.p1; Table 2: https://arxiv.org/html/2510.20815v1#S6.T2.
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec aligns LLaMA to VQ indices with language tasks; GREAM adds explicit reasoning chains and RL fine-tuning on Qwen3.
  - Source: GREAM v1, LLM-based baselines: https://arxiv.org/html/2510.20815v1#A2.I4.i1.p1; Table 2: https://arxiv.org/html/2510.20815v1#S6.T2.
- **Competitor** · [TIGER](tiger.md): TIGER generates RQ-VAE identifiers with a small T5; GREAM generates RQ-KMeans indices with an LLM that can reason before recommending.
  - Source: GREAM v1, generative baselines: https://arxiv.org/html/2510.20815v1#A2.I3.i2.p1; Table 2: https://arxiv.org/html/2510.20815v1#S6.T2.
- **Competitor** · [CID](cid.md): P5-CID uses collaborative IDs for a T5 recommender; GREAM uses semantic RQ-KMeans indices with LLM reasoning.
  - Source: GREAM v1, generative baselines: https://arxiv.org/html/2510.20815v1#A2.I3.i1.p1; Table 2: https://arxiv.org/html/2510.20815v1#S6.T2.

[View all papers in this cell](../../README.md#iii--training)
