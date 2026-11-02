# SPRIG

*Semantic-ID-enhanced Paths for Knowledge Graph-based Generative Recommendation* — Hangoebl et al. · CIKM’26 Short

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2610.06590) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text / Audio` | **`R-KM`** | `Dec-Only` | `Fixed / NTP` | `Div. Beam` |

- `Text / Audio`: Text or audio representations in different branches or evaluation settings.
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `Div. Beam`: Beam search with an explicit diversity mechanism.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
