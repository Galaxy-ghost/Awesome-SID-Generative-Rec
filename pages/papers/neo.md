# NEO

*A Unified Language Model for Large Scale Search, Recommendation, and Reasoning* — De Nadai et al., arXiv’26

[arXiv](https://arxiv.org/abs/2603.17533) · [Record](../../data/papers/neo.yaml) · [← Catalog](../../README.md#paradigms-systems-and-benchmarks)

> End-to-end paradigm or benchmark using R-KM tokenization and Dec-Only backbone.

| Group | Stage it changes |
| :-- | :-- |
| **Paradigms, Systems and Benchmarks**: Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. | No single stage |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text / Audio` | `R-KM` | `Dec-Only` | `Fixed / Multi-task NTP` | `C-Beam` |

- `Text / Audio`: 不同实体类型分别使用文本或音频嵌入与独立码本，不代表拼接两模态。
- `R-KM`: Residual k-means.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `C-Beam`: Constrained beam search.

## Same cell: Paradigms, Systems and Benchmarks (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [TIGER](tiger.md) | NeurIPS’23 | `Text` → `RQ-VAE` → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [FORGE](forge.md) | KDD’26 | `Text+Img` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → `Dyn. Beam` |
| [GRID](grid.md) | CIKM’25 | `Text` → `R-KM` → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [MiniOneRec](minionerec.md) | arXiv’25 | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP → RL` → `Beam` |
| [OneRec](onerec.md) | arXiv’25 | `Text+CF` → `R-KM` → `Enc-Dec` → `Fixed / NTP → DPO` → `Sess. Beam` |
| [GR-Generalize](gr-generalize.md) | arXiv’26 | `Text+SID` → `RQ-VAE` → `Enc-Dec` → `Fixed† / NTP†` → `Hybrid` |
| [Netflix-SID-Comparison](netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | `–` → `RQ-VAE` → `Dec-Only / Non-AR` → `Fixed / Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT` → `C-Beam / Scoring` |
| [OneMall](onemall.md) | CIKM’26 | `Text+Img+CF` → `R-KM+FSQ` → `Enc-Dec` → `Fixed / (NTP + Ctr.) → RL` → `Beam` |
| [PLUM](plum.md) | WWW’26 | `Text+Img+CF` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [ReRankID](rerankid.md) | arXiv’26 | `Text` → `R-KM†` → `Dec-Only` → `Fixed / NTP → RL` → `CoT+Greedy` |
| [SIDScope](sidscope.md) | arXiv’26 | `–` → `–` → `–` → `– / –` → `–` |
