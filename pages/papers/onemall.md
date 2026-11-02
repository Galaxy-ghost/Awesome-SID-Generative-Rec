# OneMall

*One Architecture, More Scenarios -- End-to-End Generative Recommender Family at Kuaishou E-Commerce* — Zhang et al. · CIKM’26

`Paradigms, Systems and Benchmarks` · `No single stage`

[Paper](https://arxiv.org/abs/2601.21770) · [Matrix](../../README.md#paradigms-systems-and-benchmarks)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `R-KM+FSQ` | `Enc-Dec` | `Fixed / (NTP + Ctr.) → RL` | `Beam` |

- `R-KM+FSQ`: Residual k-means combined with finite scalar quantization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `(NTP + Ctr.) → RL`: Joint next-token and contrastive training, followed by a reinforcement-learning stage; retained losses are specified per paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | Paradigms, Systems and Benchmarks: Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| Modified Stage | No single stage |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#paradigms-systems-and-benchmarks)
