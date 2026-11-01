# CogRec

*Structure-Cognitive Fast-and-Slow Reasoning for Generative Recommendation* — Liu et al., arXiv’26

[arXiv](https://arxiv.org/abs/2607.24402) · [Record](../../data/papers/cogrec.yaml) · [← Catalog](../../README.md#iii--tokenization)

> 用SID拓扑生成结构化推理轨迹，解决自然语言推理与标识空间脱节。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`R-KM+Graph`** | `Dec-Only` | `Fixed / Multi-task NTP` | `CoT+C-Beam` |

- `R-KM+Graph`: Residual k-means combined with a graph over semantic codes.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `CoT+C-Beam`: Reasoning followed by constrained beam-search decoding.

## Same cell: III × Tokenization (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [IDGenRec](idgenrec.md) | SIGIR’24 | `Text` → **`LLM-Vocab`** → `Enc-Dec` → `Altern. / NTP` → `C-Beam` |
| [SIIT](siit.md) | arXiv’24 | `Text` → **`Self-Imp.`** → `Enc-Dec` → `Altern. / Multi-task NTP` → `C-Beam` |
| [SemConv](semconv.md) | AAAI’25 | `Text+CF` → **`Align. RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` → **`Dual RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `Beam` |
| [DOS](dos.md) | WWW’26 Short | `Text+CF` → **`Orth. RQ`** → `Dec-Only†` → `Fixed† / NTP` → `–` |
| [GR4AD-X](gr4ad-x.md) | arXiv’26 | `–` → **`Multi-Path R-KM+Hash`** → `Enc-Dec` → `Fixed / NTP + PV-RSPO + Rank + Aux.` → `PV-Beam+Rerank` |
| [GRLM](grlm.md) | arXiv’26 | `Text` → **`Term-ID`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [HoloRec](holorec.md) | arXiv’26 | `–` → **`Nested RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `–` |
| [SST](sst.md) | CIKM’26 | `Text` → **`RQ+IST`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` → **`BDQ`** → `Non-AR` → `Fixed / MTP + Aux.` → `Scoring+Rerank` |
