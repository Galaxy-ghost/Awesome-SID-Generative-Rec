# GR4AD-X

*Towards Reliable, Scalable, and Value-Aligned Generative Recommendation for Large-Scale Advertising* — Xiao et al. · arXiv’26

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2610.38378) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | **`Multi-Path R-KM+Hash`** | `Enc-Dec` | `Fixed / NTP + PV-RSPO + Rank + Aux.` | `PV-Beam+Rerank` |

- `–`: Not reported in the paper.
- `Multi-Path R-KM+Hash`: Multiple residual-k-means code paths combined with a hash-based identifier component.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + PV-RSPO + Rank + Aux.`: Next-token prediction jointly optimized with prefix-value RSPO, ranking, and auxiliary objectives.
- `PV-Beam+Rerank`: Prefix-value-guided beam search followed by reranking.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--tokenization)
