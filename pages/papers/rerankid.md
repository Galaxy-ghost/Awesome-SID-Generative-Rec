# ReRankID

*Reasoning Reranking with Semantic IDs as the Sole Item Representation* — Tang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.22797) · [Record](../../data/papers/rerankid.yaml) · [← Catalog](../../README.md#paradigms-systems-and-benchmarks)

> End-to-end paradigm or benchmark using R-KM† tokenization and Dec-Only backbone.

| Group | Stage it changes |
| :-- | :-- |
| **Paradigms, Systems and Benchmarks**: Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. | No single stage |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `R-KM†` | `Dec-Only` | `Fixed / NTP → RL` | `CoT+Greedy` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `CoT+Greedy`: 贪心生成自然语言推理与候选索引排序，失败时追加结构化抽取。

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
| [OneMall](onemall.md) | CIKM’26 | `Text+Img+CF` → `R-KM+FSQ` → `Enc-Dec` → `Fixed / (NTP + Ctr.) → RL` → `Beam` |
| [PLUM](plum.md) | WWW’26 | `Text+Img+CF` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [SIDScope](sidscope.md) | arXiv’26 | `–` → `–` → `–` → `– / –` → `–` |
