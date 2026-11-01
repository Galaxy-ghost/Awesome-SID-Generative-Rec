# HoloRec

*Holistic Encoding and Interleaved Reasoning for Generative Recommendation* — Zhao et al., arXiv’26

[arXiv](https://arxiv.org/abs/2606.15331) · [Record](../../data/papers/holorec.yaml) · [← Catalog](../../README.md#iii--tokenization)

> 构造多粒度语义码并交错推理，使编号结构支持推荐推理。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **III. SID–Model Alignment**: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | **`Nested RQ`** | `Enc-Dec` | `Fixed / NTP + Aux.` | `–` |

- `–`: Not reported in the paper, or not applicable.
- `Nested RQ`: Residual quantization across nested representation granularities.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `–`: Not reported in the paper.

## Same cell: III × Tokenization (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [IDGenRec](idgenrec.md) | SIGIR’24 | `Text` → **`LLM-Vocab`** → `Enc-Dec` → `Altern. / NTP` → `C-Beam` |
| [SIIT](siit.md) | arXiv’24 | `Text` → **`Self-Imp.`** → `Enc-Dec` → `Altern. / Multi-task NTP` → `C-Beam` |
| [SemConv](semconv.md) | AAAI’25 | `Text+CF` → **`Align. RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` → **`Dual RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `Beam` |
| [CogRec](cogrec.md) | arXiv’26 | `Text` → **`R-KM+Graph`** → `Dec-Only` → `Fixed / Multi-task NTP` → `CoT+C-Beam` |
| [DOS](dos.md) | WWW’26 Short | `Text+CF` → **`Orth. RQ`** → `Dec-Only†` → `Fixed† / NTP` → `–` |
| [GR4AD-X](gr4ad-x.md) | arXiv’26 | `–` → **`Multi-Path R-KM+Hash`** → `Enc-Dec` → `Fixed / NTP + PV-RSPO + Rank + Aux.` → `PV-Beam+Rerank` |
| [GRLM](grlm.md) | arXiv’26 | `Text` → **`Term-ID`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [SST](sst.md) | CIKM’26 | `Text` → **`RQ+IST`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` → **`BDQ`** → `Non-AR` → `Fixed / MTP + Aux.` → `Scoring+Rerank` |
