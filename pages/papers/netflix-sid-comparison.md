# Netflix-SID-Comparison

*Personalized LLM Recommendation with Semantic IDs: Autoregressive Beam Search vs. Multi-Token Prediction* — Oh et al. · NeurIPS’26 PALM Workshop

`Paradigms, Systems and Benchmarks` · `No single stage`

[Paper](https://arxiv.org/abs/2610.15864) · [Matrix](../../README.md#paradigms-systems-and-benchmarks)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | `Dec-Only / Non-AR` | `Fixed / Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT` | `C-Beam / Scoring` |

- `–`: Not reported in the paper.
- `Dec-Only / Non-AR`: Decoder-only autoregressive and non-autoregressive prediction variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT`: Multi-task next-token prediction, or text next-token prediction with multi-token and ranking objectives; language-task reinforcement learning follows supervised fine-tuning.
- `C-Beam / Scoring`: Constrained beam search or direct item scoring, depending on the configuration.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | Paradigms, Systems and Benchmarks: Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| Modified Stage | No single stage |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#paradigms-systems-and-benchmarks)
