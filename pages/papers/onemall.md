# OneMall

*One Architecture, More Scenarios -- End-to-End Generative Recommender Family at Kuaishou E-Commerce* — Zhang et al., CIKM’26

[arXiv](https://arxiv.org/abs/2601.21770) · [Record](../../data/papers/onemall.yaml) · [← Catalog](../../README.md#paradigms-systems-and-benchmarks)

> End-to-end paradigm or benchmark using R-KM+FSQ tokenization and Enc-Dec backbone.

| Group | Stage it changes |
| :-- | :-- |
| **Paradigms, Systems and Benchmarks**: Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. | No single stage |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | `R-KM+FSQ` | `Enc-Dec` | `Fixed / (NTP + Ctr.) → RL` | `Beam` |

- `R-KM+FSQ`: 前两层残差 k-means，末层有限标量量化消歧。
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `(NTP + Ctr.) → RL`: 先联合 NTP 与 in-batch contrastive，随后加入 RL。RL 阶段仍联合原两损失；箭头右侧只标新增 RL，不重复写保留的 NTP/Ctr.。

## Same cell: Paradigms, Systems and Benchmarks (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [TIGER](tiger.md) | NeurIPS’23 | `Text` → `RQ-VAE` → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [FORGE](forge.md) | KDD’26 | `Text+Img` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → `Dyn. Beam` |
| [GRID](grid.md) | CIKM’25 | `Text` → `R-KM` → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [MiniOneRec](minionerec.md) | arXiv’25 | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP → RL` → `Beam` |
| [OneRec](onerec.md) | arXiv’25 | `Text+CF` → `R-KM` → `Enc-Dec` → `Fixed / NTP → DPO` → `Sess. Beam` |
| [GR-Generalize](gr-generalize.md) | arXiv’26 | `Text+SID` → `RQ-VAE` → `Enc-Dec` → `Fixed† / NTP†` → `Hybrid` |
| [NEO](neo.md) | arXiv’26 | `Text / Audio` → `R-KM` → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam` |
| [Netflix-SID-Comparison](netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | `–` → `RQ-VAE` → `Dec-Only / Non-AR` → `Fixed / Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT` → `C-Beam / Scoring` |
| [PLUM](plum.md) | WWW’26 | `Text+Img+CF` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [ReRankID](rerankid.md) | arXiv’26 | `Text` → `R-KM†` → `Dec-Only` → `Fixed / NTP → RL` → `CoT+Greedy` |
| [SIDScope](sidscope.md) | arXiv’26 | `–` → `–` → `–` → `– / –` → `–` |
