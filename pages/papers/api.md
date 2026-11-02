# API

*The Vocabulary Is Already Here: Adapting Pretrained Interpretable Features for Generative Recommendation* — Luo et al. · arXiv’26

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2610.36763) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`PID (P-SAE)`** | `Enc-Dec / Dec-Only (AR); Non-AR (PR)` | `Fixed / NTP + Rank + Aux. / MTP + Rank + Aux.` | `C-Beam / Scoring` |

- `PID (P-SAE)`: Pretrained Interpretable ID (Pretrained Sparse Autoencoder).
- `Enc-Dec / Dec-Only (AR); Non-AR (PR)`: Encoder–decoder or decoder-only autoregressive variants, and parallel non-autoregressive variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank + Aux. / MTP + Rank + Aux.`: Autoregressive or parallel token prediction jointly optimized with ranking and auxiliary objectives.
- `C-Beam / Scoring`: Constrained beam search or direct item scoring, depending on the configuration.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#ii--tokenization)
