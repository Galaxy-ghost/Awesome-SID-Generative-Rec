# Merge-and-Branch

*Merge and Branch: Efficient Tree-Structured Supervised Fine-Tuning of LLMs for Recommendation* — Zhu et al. · arXiv’26

`V. Efficiency` · `Backbone`

[Paper](https://arxiv.org/abs/2610.37973) · [Matrix](../../README.md#v--backbone)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | **`Dec-Only`** | `Fixed / NTP` | `C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | V. Efficiency: Can it be trained and served within latency and cost budgets? |
| Modified Stage | Backbone |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#v--backbone)
