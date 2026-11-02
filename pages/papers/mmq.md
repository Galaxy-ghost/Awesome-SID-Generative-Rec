# MMQ

*Multimodal Mixture-of-Quantization Tokenization for Semantic ID Generation and User Behavioral Adaptation* — Xu et al. · WSDM’26

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2508.15281) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | **`MoE-VQ`** | `HeterRec` | `Joint / MTP` | `–` |

- `HeterRec`: HeterRec, the named recommendation backbone used in the paper.
- `Joint`: The generator loss updates the tokenizer directly.
- `MTP`: Predicts several codes in parallel at once.
- `–`: Not reported in the paper.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
