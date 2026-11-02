# CausalDPO

*Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation* — Zhao et al. · ICML’26

`VI. Generalization` · `Training`

[Paper](https://arxiv.org/abs/2603.22335) · [Code](https://github.com/user683/CausalDPO) · [Matrix](../../README.md#vi--training)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

```mermaid
flowchart LR
    R["Representation<br/>Text"] --> T["Tokenization<br/>LLM-Vocab"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP → DPO"] --> I["Inference<br/>Scoring"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class TR main
```

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.

### TL;DR

CausalDPO extends DPO for LLM-based recommendation with backdoor adjustment, soft clustering of latent environments, and invariance constraints, to remove spurious correlations that DPO amplifies under distribution shift.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Key Contribution | CausalDPO extends DPO for LLM-based recommendation with backdoor adjustment, soft clustering of latent environments, and invariance constraints, to remove spurious correlations that DPO amplifies under distribution shift. |
| Modified Stage | Training |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Yelp2018, MovieLens-10M, and Book-Crossing. Users with at least 40 interactions (Yelp2018) or 20 interactions (ML-10M, Book-Crossing) are kept; ratings above 4 (ML-10M, Yelp2018) or above 7 (Book-Crossing) are positives. Sizes (sequences / items / interactions): ML-10M 71,567 / 10,681 / 10,000,054; Yelp2018 31,668 / 38,048 / 1,561,406; Book-Crossing 278,858 / 271,379 / 1,149,780.
- **Split**: Distribution-shift splits: popularity shift (Yelp2018) samples 20% of interactions as a popularity-balanced OOD test set; temporal shift (ML-10M) takes each user's latest 20% of interactions; exposure shift (Book-Crossing) takes the most recent 20% and imputes a fully exposed test set by matrix factorization; mixed shift (Yelp2018) samples 80% popularity-shift and 20% temporal-shift test interactions. The remainder is split 7:1:2 into training, validation, and IID test.
- **Candidates**: full catalog (generated items are scored and ranked over the entire item space and mapped to dataset items).
- **Visibility**: warm; no unseen-item protocol is defined. The distribution shifts concern popularity, time, and exposure of user-item interactions, not unseen items; tokenizer n/a.
- **SID**: n/a (items are generated as text by the LLM and mapped to dataset items; no semantic IDs).
- **Inference budget**: Llama-3.1-8B; decoding strategy and width: not reported. Experiments run on one node with 8 NVIDIA A800 80GB GPUs; inference batch size and latency: not reported. Table 6 reports training time per epoch (CausalDPO 2,971 s versus DPO 2,482 s). HR and NDCG at K=10 and 20.
- **Results from**: Table 1 (popularity, temporal, and exposure shifts on Yelp2018, ML-10M, Book-Crossing); Table 4 (mixed shift); Table 3 (IID test sets); Table 5 (causal regularizer added to other DPO variants); Table 8 (ablations); Table 9 (model sizes).

<details>
<summary>Sources</summary>

- **Datasets**: Dataset list: [S3.SS6.p1](https://arxiv.org/html/2603.22335v2#S3.SS6.p1); user thresholds and positive-rating rules: [A2.SS1.p1](https://arxiv.org/html/2603.22335v2#A2.SS1.p1); statistics: [A2.T2](https://arxiv.org/html/2603.22335v2#A2.T2).
- **Split**: Shift constructions: [A2.I2.i1.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i1.p1), [A2.I2.i2.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i2.p1), [A2.I2.i3.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i3.p1), and [A2.I2.i4.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i4.p1).
- **Candidates**: Scoring and ranking over the entire item space: [S3.SS6.p1](https://arxiv.org/html/2603.22335v2#S3.SS6.p1).
- **Visibility**: OOD shifts concern popularity, time, and exposure, not unseen items: [S3.SS6.p1](https://arxiv.org/html/2603.22335v2#S3.SS6.p1) and [A2.I2.i1.p1](https://arxiv.org/html/2603.22335v2#A2.I2.i1.p1).
- **SID**: Prompts generate items as text: [S3.SS6.p1](https://arxiv.org/html/2603.22335v2#S3.SS6.p1); the item is represented through text in the prompt formulation: [S2.p1](https://arxiv.org/html/2603.22335v2#S2.p1).
- **Inference budget**: Hardware: [A2.SS3.p1](https://arxiv.org/html/2603.22335v2#A2.SS3.p1); training time per epoch: [A2.T6](https://arxiv.org/html/2603.22335v2#A2.T6).
- **Results from**: OOD table: [S3.T1](https://arxiv.org/html/2603.22335v2#S3.T1); IID: [A2.T3](https://arxiv.org/html/2603.22335v2#A2.T3); mixed shift: [A2.T4](https://arxiv.org/html/2603.22335v2#A2.T4); regularizer transfer: [A2.T5](https://arxiv.org/html/2603.22335v2#A2.T5); ablation: [A2.T8](https://arxiv.org/html/2603.22335v2#A2.T8); model sizes: [A2.T9](https://arxiv.org/html/2603.22335v2#A2.T9).

</details>

### 5. Connections to Related Work

```mermaid
flowchart LR
    P["CausalDPO"]
    P -->|alternative| A["OneRec"]
```

- **Alternative** · [OneRec](onerec.md): OneRec uses iterative preference alignment for a generative recommender with semantic IDs; CausalDPO adds backdoor adjustment over latent environments to DPO for text-generating LLM recommenders under distribution shift.
  - Source: CausalDPO v2, Section 4 cites Deng et al. (2025), OneRec, among DPO adoptions in recommendation: https://arxiv.org/html/2603.22335v2#S4.p2; not a baseline in Table 1.

[View all papers in this cell](../../README.md#vi--training)
