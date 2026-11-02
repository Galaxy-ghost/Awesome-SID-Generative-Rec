# Tlow

*Flow-based Item Tokenizer for Recommendation* — Li et al. · CIKM’26 Applied

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2608.24176) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Flow+PQ`** | `Non-AR` | `Fixed / MTP + Rel.MSE` | `Scoring` |

- `Flow+PQ`: Flow-based representation transformation followed by product quantization.
- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP + Rel.MSE`: Multi-token prediction jointly optimized with a mean-squared-error objective on relations.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
