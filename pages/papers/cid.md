# CID

*How to Index Item IDs for Recommendation Foundation Models* — Hua et al. · SIGIR-AP’23

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2305.06569) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `CF` | **`Spectral Clus.`** | `Enc-Dec` | `Fixed / NTP` | `C-Beam` |

- `CF`: Collaborative filtering signal.
- `Spectral Clus.`: Spectral clustering-based tokenization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#ii--tokenization)
