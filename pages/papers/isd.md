# ISD

*Understanding Semantic IDs: From Item Representation to Item Selection in Generative Recommendation* — Wang et al. · arXiv’26

`IV. Utility` · `Inference`

[Paper](https://arxiv.org/abs/2607.24995) · [Matrix](../../README.md#iv--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text†` | `RQ-VAE†` | `Enc-Dec†` | `Fixed / NTP†` | **`ISD Beam`** |

- `Fixed`: SIDs are built first and not changed while the generator trains.
- `ISD Beam`: Item-supported beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iv--inference)
