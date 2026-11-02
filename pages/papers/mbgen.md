# MBGen

*Multi-Behavior Generative Recommendation* — Liu et al. · CIKM’24

`I. Informativeness` · `Training`

[Paper](https://arxiv.org/abs/2405.16871) · [Matrix](../../README.md#i--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `CF` | `Bal. VQ+KM` | `Enc-Dec` | **`Fixed / NTP`** | `Beam` |

- `CF`: Collaborative filtering signal.
- `Bal. VQ+KM`: Balanced tokenization combining vector quantization and k-means clustering.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Training |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--training)
