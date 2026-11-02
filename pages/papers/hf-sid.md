# HF-SID

*High-Fidelity Semantic IDs for Generative Retrieval in Location-Based Services* — Lin et al. · arXiv’26

`I. Informativeness` · `Representation` · `POI`

[Paper](https://arxiv.org/abs/2608.30479) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Attr+Geo`** | `R-KM` | `Dec-Only` | `Fixed / NTP` | `C-Beam` |

- `Text+Attr+Geo`: Text, structured attributes, and geographic information.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
