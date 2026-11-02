# TransRec

*Bridging Items and Language: A Transition Paradigm for Large Language Model-Based Recommendation* — Lin et al. · KDD’24

`II. Uniqueness and Validity` · `Tokenization`

[Paper](https://arxiv.org/abs/2310.06491) · [Matrix](../../README.md#ii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Multi-Facet ID`** | `Enc-Dec / Dec-Only` | `Fixed / NTP` | `FM-Index+Agg.` |

- `Multi-Facet ID`: Identifiers representing multiple facets of an item.
- `Enc-Dec / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `FM-Index+Agg.`: FM-index-constrained generation followed by identifier-to-item score aggregation.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | II. Uniqueness and Validity: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#ii--tokenization)
