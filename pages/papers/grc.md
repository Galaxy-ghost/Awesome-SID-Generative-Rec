# GRC

*Learning to Reflect and Correct: Towards Better Decoding Trajectories for Large-Scale Generative Recommendation* — Xing et al., CIKM’26

[arXiv](https://arxiv.org/abs/2602.23639) · [Record](../../data/papers/grc.yaml) · [← Catalog](../../README.md#iii--inference)

> §5.1仅称Qwen3-8B encode item embeddings，未列构码原始输入模态；没有点名继承文本输入配置，不能把常见Qwen文本编码经验写Text†。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `RQ-VAE` | `Enc-Dec` | `Fixed / NTP → RL` | **`GRC+Beam`** |

- `–`: Not reported in the paper, or not applicable.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `GRC+Beam`: Generation, reflection and correction combined with beam search.

## Same cell: III × Inference (1 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [PROMISE](promise.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → `Fixed† / NTP + Aux.` → **`PRM-Beam`** |
