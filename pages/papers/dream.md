# DREAM

*Dynamic Refinement of Early Assignment Mappings* — Guan et al. · arXiv’26

`VI. Generalization` · `Tokenization`

[Paper](https://arxiv.org/abs/2606.06947) · [Matrix](../../README.md#vi--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`CART`** | `Dec-Only` | `Altern. / NTP + Aux.` | `C-Beam` |

- `CART`: Collaborative-Aware Refined Tokenization.
- `Dec-Only`: Decoder-only.
- `Altern.`: Tokenizer and generator are updated in turns.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | VI. Generalization: Does it still work for new items, new domains, and shifting interests? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#vi--tokenization)
