# RecBase

*Generative foundation model pretraining for zero-shot recommendation* — Zhou et al., EMNLP’25

[arXiv](https://arxiv.org/abs/2509.03131) · [Record](../../data/papers/recbase.yaml) · [← Catalog](../../README.md#vi--training)

> Abstract: "cross-domain generalization is hindered by a fundamental mismatch between language-centric pretraining and the recommendation task".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `Curr. RQ` | `Dec-Only` | **`Fixed / NTP`** | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "cross-domain generalization is hindered by a fundamental mismatch between language-centric pretraining and the recommendation task".

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

推理时可逐位生成概念 ID，但实验按 AUC 对候选物品打分排序。

## Same cell: VI × Training (3 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [AWARE](aware.md) | arXiv’26 | `Text+Geo` → `Geo-Prefix+HClus` → `Dec-Only` → **`Fixed / NTP`** → `–` |
| [CausalDPO](causaldpo.md) | ICML’26 | `Text` → `LLM-Vocab` → `Dec-Only` → **`Fixed / NTP → DPO`** → `Scoring` |
| [CMRec](cmrec.md) | CIKM’26 Short | `Text+Img+CF` → `RQ-VAE` → `Dec-Only†` → **`– / NTP`** → `–` |
