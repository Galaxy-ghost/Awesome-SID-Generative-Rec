# SpecGR

*Inductive Generative Recommendation via Retrieval-based Speculation* — Ding et al. · AAAI’26

`VI. Generalization` · `Inference`

[Paper](https://arxiv.org/abs/2410.02939) · [Matrix](../../README.md#vi--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+SID` | `RQ-VAE` | `Enc-Dec` | `Fixed / NTP + Rank` | **`Hybrid`** |

- `Text+SID`: Text representation plus semantic IDs (hybrid dense and generative retrieval).
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--inference)
