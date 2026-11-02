# KGTB

*Knowledge Graph Tokenization for Behavior-Aware Generative Next POI Recommendation* — Sun et al. · arXiv’25

`I. Informativeness` · `Tokenization` · `POI`

[Paper](https://arxiv.org/abs/2509.12350) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Attr+Geo+CF` | **`KG-RQ`** | `Dec-Only` | `Fixed / Multi-task NTP` | `–` |

- `Attr+Geo+CF`: Category and other attributes, plus geography, plus CF (POI).
- `KG-RQ`: Residual quantization informed by knowledge-graph structure.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
