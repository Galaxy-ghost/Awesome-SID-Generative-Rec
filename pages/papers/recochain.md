# RecoChain

*Harmonizing Generative Retrieval and Ranking in Chain-of-Recommendation* — Liu and Cao, arXiv’26

[arXiv](https://arxiv.org/abs/2604.25787) · [Record](../../data/papers/recochain.yaml) · [← Catalog](../../README.md#iv--backbone)

> Abstract: "leading to a gap between generation and ranking performance". Candidates: IV / III (rule: IV threshold: a flawed training objective counts).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **IV. Utility**: Are training and search aimed at what users and the platform value, rather than at token likelihood? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | `RQ` | **`Dec-Only`** | `Fixed / NTP + Rank` | `Hybrid` |

- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Rank`: NTP plus a ranking loss.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "leading to a gap between generation and ranking performance". Candidates: IV / III (rule: IV threshold: a flawed training objective counts).
- **`tokenizer`** (p3): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p3): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

束搜索生成候选 SID 后，再由排序头对候选打分重排。

## Same cell: IV × Backbone (2 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [DiGR](digr.md) | arXiv’26 | `–` → `RQ-VAE` → **`Dec-Only`** → `Fixed / Discrim.` → `Scoring` |
| [Gryphon](gryphon.md) | CIKM’26 Short | `–` → `R-KM` → **`Enc-Dec`** → `Fixed / NTP + Rank` → `Hybrid` |
