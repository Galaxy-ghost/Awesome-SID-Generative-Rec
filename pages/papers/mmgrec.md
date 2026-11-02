# MMGRec

*Multimodal Generative Recommendation with Transformer Model* — Liu et al. · TOMM’26

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2404.16555) · [Code](https://github.com/hanliu95/MMGRec) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | **`Graph RQ-VAE`** | `Enc-Dec` | `Fixed / NTP` | `C-Beam` |

- `Graph RQ-VAE`: A graph-informed residual-quantized variational autoencoder.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### TL;DR

MMGRec assigns each item a Rec-ID with Graph RQ-VAE over multimodal and collaborative features and trains a Transformer with relation-aware self-attention to generate it, instead of embed-and-retrieve.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Key Contribution | MMGRec assigns each item a Rec-ID with Graph RQ-VAE over multimodal and collaborative features and trains a Transformer with relation-aware self-attention to generate it, instead of embed-and-retrieve. |
| Modified Stage | Tokenization |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: MovieLens, TikTok, Kwai multimodal recommendation benchmarks; filtering: not reported.
- **Split**: Per-user random interaction split: 80% training, 10% validation, 10% test; non-sequential CF, without temporal labels.
- **Candidates**: not reported
- **Visibility**: warm; no unseen-item protocol is defined. Graph RQ-VAE uses user-item interactions; test-interaction exposure in graph construction: not reported.
- **SID**: Graph RQ-VAE: 3 semantic tokens plus popularity-rank collision suffix. Codebooks tuned over 64/128/256; Kwai analysis favors 128; selected per-dataset sizes not reported.
- **Inference budget**: Constrained beam width K, default K=10. Figure 5 plots approximately 60-125 ms/user across 1/16-to-full Kwai. Hardware, inference batch size and timing scope: not reported.
- **Results from**: This paper's experiments using public baseline implementations: Table 2 main; Tables 3-5 ablations; Figures 4-6 hyperparameters, inference efficiency, Rec-ID design. TIGER is explicitly excluded from the benchmark.

<details>
<summary>Sources</summary>

- **Datasets**: Section 5.1: [S5.SS1.p1](https://arxiv.org/html/2404.16555v4#S5.SS1.p1) and [S5.SS1.p2](https://arxiv.org/html/2404.16555v4#S5.SS1.p2)
- **Split**: Sections 5.1-5.2: [S5.SS1.p3](https://arxiv.org/html/2404.16555v4#S5.SS1.p3) and [S5.SS2.p2](https://arxiv.org/html/2404.16555v4#S5.SS2.p2)
- **Candidates**: Sections 4.4 and 5.1 specify generated top-K lists but no full-catalog/sampled evaluation declaration: [S4.SS4.p1](https://arxiv.org/html/2404.16555v4#S4.SS4.p1) and [S5.SS1.p3](https://arxiv.org/html/2404.16555v4#S5.SS1.p3)
- **Visibility**: Sections 4.2.1 and 5.1 define no unseen-item evaluation: [S4.SS2.SSS1.p1](https://arxiv.org/html/2404.16555v4#S4.SS2.SSS1.p1) and [S5.SS1.p3](https://arxiv.org/html/2404.16555v4#S5.SS1.p3)
- **SID**: Sections 4.2.2, 5.3 and 6.5: [S4.SS2.SSS2.p1](https://arxiv.org/html/2404.16555v4#S4.SS2.SSS2.p1) and [S5.SS3.p1](https://arxiv.org/html/2404.16555v4#S5.SS3.p1) and [S6.SS5.p4](https://arxiv.org/html/2404.16555v4#S6.SS5.p4)
- **Inference budget**: Sections 4.4-4.5, Section 6.4 and Figure 5: [S4.SS4.p1](https://arxiv.org/html/2404.16555v4#S4.SS4.p1) and [S4.SS5.p1](https://arxiv.org/html/2404.16555v4#S4.SS5.p1) and [S5.SS1.p3](https://arxiv.org/html/2404.16555v4#S5.SS1.p3) and [S6.SS4.p1](https://arxiv.org/html/2404.16555v4#S6.SS4.p1) and [S6.F5](https://arxiv.org/html/2404.16555v4#S6.F5)
- **Results from**: Tables 2-5, Figures 4-6 and baseline implementation statement: [S6.T2](https://arxiv.org/html/2404.16555v4#S6.T2) and [S6.T3](https://arxiv.org/html/2404.16555v4#S6.T3) and [S6.T4](https://arxiv.org/html/2404.16555v4#S6.T4) and [S6.T5](https://arxiv.org/html/2404.16555v4#S6.T5) and [S6.F4](https://arxiv.org/html/2404.16555v4#S6.F4) and [S6.F6](https://arxiv.org/html/2404.16555v4#S6.F6) and [S6.F5](https://arxiv.org/html/2404.16555v4#S6.F5) and [S5.SS2.p2](https://arxiv.org/html/2404.16555v4#S5.SS2.p2)

</details>

### 5. Connections to Related Work

- **Predecessor** · [TIGER](tiger.md): MMGRec extends TIGER's RQ-VAE idea with multimodal/CF inputs and popularity-based collision suffixes; TIGER is not evaluated.
  - Source: MMGRec v4, Sections 1, 3 and 5.2: https://arxiv.org/html/2404.16555v4#S1.p4; https://arxiv.org/html/2404.16555v4#S3.p1; https://arxiv.org/html/2404.16555v4#S5.SS2.p2.

[View all papers in this cell](../../README.md#i--tokenization)
