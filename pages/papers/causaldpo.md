# CausalDPO

*Causal Direct Preference Optimization for Distributionally Robust Generative Recommendation* — Zhao et al., ICML’26

[arXiv](https://arxiv.org/abs/2603.22335) · [Record](../../data/papers/causaldpo.yaml) · [← Catalog](../../README.md#vi--training)

> Abstract: "significantly undermining the generalization capability of LLM-based generative recommendation methods in out of distribution (OOD) scenarios".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `LLM-Vocab` | `Dec-Only` | **`Fixed / NTP → DPO`** | `Scoring` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "significantly undermining the generalization capability of LLM-based generative recommendation methods in out of distribution (OOD) scenarios".

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

生成物品标题文本，再对全物品打分映射到物品；当前记录将标题标识归为 LLM-Vocab。

## Same cell: VI × Training (3 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [RecBase](recbase.md) | EMNLP’25 | `Text` → `Curr. RQ` → `Dec-Only` → **`Fixed / NTP`** → `Beam` |
| [AWARE](aware.md) | arXiv’26 | `Text+Geo` → `Geo-Prefix+HClus` → `Dec-Only` → **`Fixed / NTP`** → `–` |
| [CMRec](cmrec.md) | CIKM’26 Short | `Text+Img+CF` → `RQ-VAE` → `Dec-Only†` → **`– / NTP`** → `–` |
