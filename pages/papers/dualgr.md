# DualGR

*Generative Retrieval with Long and Short-Term Interests Modeling* — Yi et al. · WWW’26 Short

`VI. Generalization` · `Backbone`

[Paper](https://arxiv.org/abs/2511.12518) · [Matrix](../../README.md#vi--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `R-KM` | **`Dec-Only`** | `Fixed / NTP + Rank` | `Dual Beam` |

- `–`: Not reported in the paper.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.
- `Dual Beam`: Beam-search decoding in two branches with merged candidates.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Backbone |

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Kuaishou double-column Explore-feed logs; filtering rules and dataset dates not reported.
  - Source: Section 3: https://arxiv.org/html/2511.12518v1#S3.p1
- **Split**: Offline split not reported; online A/B test lasts one week with 6% traffic.
  - Source: Sections 3 and 3.1: https://arxiv.org/html/2511.12518v1#S3.p1 and https://arxiv.org/html/2511.12518v1#S3.SS1.p1
- **Candidates**: not reported
  - Source: Section 3 describes online HR without specifying a full-catalog or sampled-negative protocol: https://arxiv.org/html/2511.12518v1#S3.p1
- **Visibility**: warm; no unseen-item protocol is defined. Item-level generator/tokenizer exposure: not reported.
  - Source: Sections 2.1 and 3 do not specify generator/tokenizer item holdouts: https://arxiv.org/html/2511.12518v1#S2.SS1 and https://arxiv.org/html/2511.12518v1#S3
- **SID**: Residual k-means: 3 levels x 8192 codes; collision handling not reported.
  - Source: Sections 2.2 and 3: https://arxiv.org/html/2511.12518v1#S2.SS2.p1 and https://arxiv.org/html/2511.12518v1#S3.p1
- **Inference budget**: Two branch-wise beam searches, followed by merging; HR@100/500/1000. Beam width, hardware, inference batch size, and numerical latency not reported; A/B test reports no measurable response-time increase.
  - Source: Section 2.3, Table 1, and Section 3.1: https://arxiv.org/html/2511.12518v1#S2.SS3.p2 and https://arxiv.org/html/2511.12518v1#S3.T1 and https://arxiv.org/html/2511.12518v1#S3.SS1.p1
- **Results from**: Original Table 1: online HR; Table 2: ablations; Section 3.1: A/B results.
  - Source: Tables 1-2 and Section 3.1: https://arxiv.org/html/2511.12518v1#S3.T1 and https://arxiv.org/html/2511.12518v1#S3.T2 and https://arxiv.org/html/2511.12518v1#S3.SS1.p1

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER is reimplemented as the generative baseline; DualGR adds explicit long/short routing and exposure-aware training.
  - Source: DualGR v1, Section 3 and Table 1: https://arxiv.org/html/2511.12518v1#S3.p1; https://arxiv.org/html/2511.12518v1#S3.T1.

[View all papers in this cell](../../README.md#vi--backbone)
