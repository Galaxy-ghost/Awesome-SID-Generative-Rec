# GRC

*Learning to Reflect and Correct: Towards Better Decoding Trajectories for Large-Scale Generative Recommendation* — Xing et al. · CIKM’26

`III. SID–Model Alignment` · `Inference`

[Paper](https://arxiv.org/abs/2602.23639) · [Matrix](../../README.md#iii--inference)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | `Enc-Dec` | `Fixed / NTP → RL` | **`GRC+Beam`** |

- `–`: Not reported in the paper.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `GRC+Beam`: Generation, reflection and correction combined with beam search.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Inference |

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#iii--inference)
