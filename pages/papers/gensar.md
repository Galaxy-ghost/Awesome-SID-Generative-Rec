# GenSAR

*Unified Generative Search and Recommendation* — Shi et al. · RecSys’25

`I. Informativeness` · `Tokenization`

[Paper](https://arxiv.org/abs/2504.05730) · [Matrix](../../README.md#i--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Shared/Spec. RQ`** | `Enc-Dec` | `Fixed / Multi-task NTP` | `C-Beam` |

- `Shared/Spec. RQ`: Residual quantization using shared and task-specific codebooks.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Tokenization |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--tokenization)
