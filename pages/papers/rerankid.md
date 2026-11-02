# ReRankID

*Reasoning Reranking with Semantic IDs as the Sole Item Representation* — Tang et al. · arXiv’26

`Paradigms, Systems and Benchmarks` · `No single stage`

[Paper](https://arxiv.org/abs/2610.22797) · [Code](https://github.com/lilv98/ReRankID) · [Matrix](../../README.md#paradigms-systems-and-benchmarks)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `R-KM†` | `Dec-Only` | `Fixed / NTP → RL` | `CoT+Greedy` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `CoT+Greedy`: Reasoning with greedy decoding.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | Paradigms, Systems and Benchmarks: Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| Modified Stage | No single stage |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Kuaishou OpenOneRec-RecIF short-video release, 162074 source users; evaluation requires a renderable positive and >=256 items with both SID/caption histories.
  - Source: Section 3 and Appendix A.2: https://arxiv.org/html/2610.22797v1#S3.SS0.SSS0.Px2.p1 and https://arxiv.org/html/2610.22797v1#A1.SS2.p1 and https://arxiv.org/html/2610.22797v1#A5.p1
- **Split**: User-disjoint SFT/post-training/development/test partitions; 400 development and 400 test users, each balanced 200 explicit-engagement/200 long-view positives; histories precede targets.
  - Source: Appendix A.2: https://arxiv.org/html/2610.22797v1#A1.SS2.p1
- **Candidates**: sampled: 29 negatives plus one positive at anchor; slate sizes 10/20/30/50/100. Exposure-hard negatives plus uniform catalog fill; user-engaged items excluded. Exclusion of other historical exposures: not reported.
  - Source: Appendix A.2-A.3: https://arxiv.org/html/2610.22797v1#A1.SS2.p2 and https://arxiv.org/html/2610.22797v1#A1.SS3.p1
- **Visibility**: warm; evaluation release users/items were exposed during backbone pretraining, while post-training users are disjoint. Reranking supplied slates is a new task.
  - Source: Appendix A.4: https://arxiv.org/html/2610.22797v1#A1.SS4.p1 and https://arxiv.org/html/2610.22797v1#A1.SS4.p3
- **SID**: Released OpenOneRec three-code SIDs from quantized item-text embeddings; quantizer algorithm, codebook sizes and collision handling: not reported.
  - Source: Section 3 and Appendix A.1: https://arxiv.org/html/2610.22797v1#S3.SS0.SSS0.Px2.p1 and https://arxiv.org/html/2610.22797v1#A1.SS1.p1
- **Inference budget**: SID: greedy reasoning 2048 tokens, fallback structured extraction 256 tokens from <=1200 reasoning characters; top-10 indices; A100/BF16. Text APIs: 8192-32768 output-token caps. Inference batch and latency: not reported.
  - Source: Appendix B.1, Table B.2 and Appendix E: https://arxiv.org/html/2610.22797v1#A2.SS1.p2 and https://arxiv.org/html/2610.22797v1#A2.T2 and https://arxiv.org/html/2610.22797v1#A5.p2
- **Results from**: This testbed's paired evaluations: Table 1 initial models/references, Table 2 post-training, Table D.1 full metrics. Each post-training method compares its own initializer; invalid outputs score zero.
  - Source: Tables 1/2/D.1 and Section 5.1: https://arxiv.org/html/2610.22797v1#S4.T1 and https://arxiv.org/html/2610.22797v1#S5.T2 and https://arxiv.org/html/2610.22797v1#A4.T1 and https://arxiv.org/html/2610.22797v1#S5.SS1.p1

### 5. Connections to Related Work

- **Alternative** · [OneRec-Think](onerec-think.md): OneRec-Think reasons before catalog-item generation; ReRankID reasons over a supplied candidate slate.
  - Source: ReRankID v1, Section 2: https://arxiv.org/html/2610.22797v1#S2.SS0.SSS0.Px1.p1.
- **Predecessor** · [TIGER](tiger.md): TIGER's SID-generation paradigm is the background contrasted with SID-only slate reranking.
  - Source: ReRankID v1, Section 2: https://arxiv.org/html/2610.22797v1#S2.SS0.SSS0.Px1.p1.

[View all papers in this cell](../../README.md#paradigms-systems-and-benchmarks)
