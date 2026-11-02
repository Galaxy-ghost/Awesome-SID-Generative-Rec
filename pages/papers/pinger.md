# PinGER

*Token-Efficient Generative Retrieval with Semantic IDs* — Li et al. · arXiv’26

`V. Efficiency` · `Backbone`

[Paper](https://arxiv.org/abs/2610.33435) · [Matrix](../../README.md#v--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `RQ-VAE` | **`Dec-Only`** | `– / NTP → DPO` | `Div. C-Beam` |

- `Dec-Only`: Decoder-only.
- `–`: Not reported in the paper.
- `NTP → DPO`: NTP, then preference optimization.
- `Div. C-Beam`: Constrained beam search with an explicit diversity mechanism.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Backbone |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Pinterest session-centric UniPinRec data: historical cross-surface actions paired with target-surface session engagements; session sampling reflects traffic. Filtering rules: not reported.
  - Source: Section 5.1: https://arxiv.org/html/2610.33435v1#S5.SS1.SSS0.Px1.p1
- **Split**: Evaluation uses held-out users in a later, non-overlapping window disjoint from training. Window dates, allocation ratios and validation split: not reported.
  - Source: Section 5.1: https://arxiv.org/html/2610.33435v1#S5.SS1.SSS0.Px1.p1
- **Candidates**: full catalog: generated identifiers resolve against the full production corpus.
  - Source: Section 5.1: https://arxiv.org/html/2610.33435v1#S5.SS1.SSS0.Px1.p1
- **Visibility**: warm; no unseen-item protocol is defined. Users are held out; fresh-content analysis uses Pins created within 28 days, without specified generator/tokenizer item holdouts.
  - Source: Section 5.1 and online fresh-content analysis: https://arxiv.org/html/2610.33435v1#S5.SS1.SSS0.Px1.p1 and https://arxiv.org/html/2610.33435v1#S5.SS3.SSS1.p1
- **SID**: RQ-VAE 5x2048; content-only PinCLIP input, OmniSage engagement distillation. Index resolves shared-SID item lists; insufficient leaves fall back to coarser prefixes, with round-robin interleaving across beams.
  - Source: Sections 3.2 and 4.3: https://arxiv.org/html/2610.33435v1#S3.SS2.p1 and https://arxiv.org/html/2610.33435v1#S4.SS3.p1 and https://arxiv.org/html/2610.33435v1#S4.SS3.p2
- **Inference budget**: Offline beam100, Recall@10/100. Online Related Pins beam60/penalty3; notifications beam100/penalty1. Serving L40S at ~200QPS/host: e2e p50/p99 51/77ms (beam60),54/81ms (beam100); batch not reported. Attention microbenchmark: A10G,batch4,history1018.
  - Source: Sections 5.1/5.3, Table 1 and Figure 5: https://arxiv.org/html/2610.33435v1#S5.SS1.SSS0.Px2.p1 and https://arxiv.org/html/2610.33435v1#S5.SS3.SSS1.p1 and https://arxiv.org/html/2610.33435v1#S5.SS3.SSS2.p1 and https://arxiv.org/html/2610.33435v1#S4.T1 and https://arxiv.org/html/2610.33435v1#S4.F5
- **Results from**: Reported Tables 1/2/3/4: serving, offline PinRec/TIGER comparison, diversity, online A/B; Tables 5-8: context sweep, trie costs, segments, ablations. Borrowed-versus-rerun baseline provenance: not reported.
  - Source: Tables 1-4 and Appendix Tables 5-8: https://arxiv.org/html/2610.33435v1#S4.T1 and https://arxiv.org/html/2610.33435v1#S5.T2 and https://arxiv.org/html/2610.33435v1#S5.T3 and https://arxiv.org/html/2610.33435v1#S5.T4 and https://arxiv.org/html/2610.33435v1#A1.T5 and https://arxiv.org/html/2610.33435v1#A1.T8

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER is compared at matched training context and serving-token budgets.
  - Source: PinGER v1, Section 5.2.1 and Table 2: https://arxiv.org/html/2610.33435v1#S5.SS2.SSS1.p1; https://arxiv.org/html/2610.33435v1#S5.T2.
- **Predecessor** · [STATIC](static.md): PinGER adopts STATIC's vectorized trie for valid-SID constrained decoding.
  - Source: PinGER v1, Section 4.2: https://arxiv.org/html/2610.33435v1#S4.SS2.p2.
- **Predecessor** · [COBRA](cobra.md): PinGER retains COBRA-style SID/dense interleaving during training and removes past SIDs at serving.
  - Source: PinGER v1, Section 2: https://arxiv.org/html/2610.33435v1#S2.SS0.SSS0.Px1.p1.

[View all papers in this cell](../../README.md#v--backbone)
