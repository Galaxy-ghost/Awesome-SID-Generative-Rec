# MBGR

*Multi-Business Prediction for Generative Recommendation at Meituan* — Li et al., arXiv’26

[arXiv](https://arxiv.org/abs/2604.02684) · [Record](../../data/papers/mbgr.yaml) · [← Catalog](../../README.md#vi--tokenization)

> Abstract: "a seesaw phenomenon in multi-business scenarios"; "a unified SID space causes". Candidates: VI / II (rule: judged by the abstract's complaint first).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`RQ`** | `Dec-Only` | `Fixed† / NTP + Aux.` | `C-Beam` |

- `RQ`: Residual quantization.
- `Dec-Only`: Decoder-only.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `C-Beam`: Constrained beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "a seesaw phenomenon in multi-business scenarios"; "a unified SID space causes". Candidates: VI / II (rule: judged by the abstract's complaint first).
- **`tokenizer`** (p4): SID construction not described; Fixed is inferred. Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p4): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用业务感知 SID 和多业务预测结构缓解多业务场景的跷跷板问题。

## Same cell: VI × Tokenization (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` → **`OPQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring` |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` → **`Unified RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [UTGRec](utgrec.md) | arXiv’25 | `Multi-Dom` → **`Tree`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [DACT](dact.md) | SIGIR’26 | `Text+CF` → **`RQ-VAE`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `–` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` → **`CART`** → `Dec-Only` → `Altern. / NTP + Aux.` → `C-Beam` |
| [GenCDR](gencdr.md) | AAAI’26 | `Cross-Dom` → **`RQ+LoRA`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` → **`R-KM`** → `Lazy Dec-Only` → `Fixed / NTP → RL` → `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` → **`TokenMoE`** → `Enc-Dec` → `Fixed / NTP` → `Beam†` |
