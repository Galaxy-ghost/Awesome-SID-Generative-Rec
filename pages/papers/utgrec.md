# UTGRec

*Universal Item Tokenization for Transferable Generative Recommendation* — Zheng et al., arXiv’25

[arXiv](https://arxiv.org/abs/2504.04405) · [Record](../../data/papers/utgrec.yaml) · [← Catalog](../../README.md#vi--tokenization)

> Abstract: "typically domain-specific, limiting their ability for effective transfer or adaptation to new domains".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Multi-Dom` | **`Tree`** | `Enc-Dec` | `Fixed / NTP` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "typically domain-specific, limiting their ability for effective transfer or adaptation to new domains".

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用多模态大模型和树状码本构造跨领域通用的物品标识。

## Same cell: VI × Tokenization (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` → **`OPQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring` |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` → **`Unified RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [DACT](dact.md) | SIGIR’26 | `Text+CF` → **`RQ-VAE`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `–` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` → **`CART`** → `Dec-Only` → `Altern. / NTP + Aux.` → `C-Beam` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` → **`RQ+LoRA`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [MBGR](mbgr.md) | arXiv’26 | `Text+CF` → **`RQ`** → `Dec-Only` → `Fixed† / NTP + Aux.` → `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` → **`R-KM`** → `Lazy Dec-Only` → `Fixed / NTP → RL` → `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` → **`TokenMoE`** → `Enc-Dec` → `Fixed / NTP` → `Beam†` |
