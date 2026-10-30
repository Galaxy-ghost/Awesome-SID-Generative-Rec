# DACT

*Drift-Aware Continual Tokenization for Generative Recommendation* — Feng et al., SIGIR’26

[arXiv](https://arxiv.org/abs/2603.29705) · [Record](../../data/papers/dact.yaml) · [← Catalog](../../README.md#vi--tokenization)

> 给完整 SID 生成模型提供持续更新编号器的新设计，在 TIGER 与 LC-Rec 验证。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`RQ-VAE`** | `Enc-Dec / Dec-Only` | `Fixed / NTP` | `–` |

- `Enc-Dec / Dec-Only`: Evaluated on both Encoder-Decoder and Decoder-Only backbones.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `–`: Not reported in the paper.

## Same cell: VI × Tokenization (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` → **`OPQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring` |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` → **`Unified RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [UTGRec](utgrec.md) | arXiv’25 | `Multi-Dom` → **`Tree`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` → **`CART`** → `Dec-Only` → `Altern. / NTP + Aux.` → `C-Beam` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` → **`RQ+LoRA`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [MBGR](mbgr.md) | arXiv’26 | `Text+CF` → **`RQ`** → `Dec-Only` → `Fixed† / NTP + Aux.` → `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` → **`R-KM`** → `Lazy Dec-Only` → `Fixed / NTP → RL` → `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` → **`TokenMoE`** → `Enc-Dec` → `Fixed / NTP` → `Beam†` |
