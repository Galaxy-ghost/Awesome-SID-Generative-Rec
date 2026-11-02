# SST

*Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms to Semantic Subwords* — Miao et al. · CIKM’26

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2608.22734) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`RQ+IST`** | `Enc-Dec` | `Fixed / NTP` | `C-Beam` |

- `RQ+IST`: Residual quantization combined with item-level subword tokenization.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--tokenization)
