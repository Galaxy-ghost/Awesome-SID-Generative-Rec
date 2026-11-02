# AWARE

*Why Users Go There: World Knowledge-Augmented Generative Next POI Recommendation* — Ding et al. · arXiv’26

`VI. Generalization` · `Training` · `POI`

[Paper](https://arxiv.org/abs/2605.11807) · [Matrix](../../README.md#vi--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Geo` | `Geo-Prefix+HClus` | `Dec-Only` | **`Fixed / NTP`** | `–` |

- `Geo-Prefix+HClus`: Geographic prefixes combined with hierarchical clustering codes.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--training)
