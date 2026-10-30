# HoloRec: HoloRec: Holistic Encoding and Interleaved Reasoning for Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2606.15331`)](https://arxiv.org/abs/2606.15331) · [Source Record (`data/papers/holorec.yaml`)](../../data/papers/holorec.yaml)

> **Summary**: 构造多粒度语义码并交错推理，使编号结构支持推荐推理。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhao et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `–` | Not reported in the paper, or not applicable. |
| **Tokenization** | `Nested RQ` | 多粒度嵌套残差量化，共享各残差层码本。 |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP + Aux.` | NTP plus another auxiliary loss. |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `III. SID–Model Alignment` × `Tokenization` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [IDGenRec](idgenrec.md) | SIGIR’24 | `Text` | `LLM-Vocab` | `Enc-Dec` | `Altern.` | `NTP` | `C-Beam` |
| [SIIT](siit.md) | arXiv’24 | `Text` | `Self-Imp.` | `Enc-Dec` | `Altern.` | `Multi-task NTP` | `C-Beam` |
| [SemConv](semconv.md) | AAAI’25 | `Text+CF` | `Align. RQ` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` | `Dual RQ` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Beam` |
| [CogRec](cogrec.md) | arXiv’26 | `Text` | `R-KM+Graph` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `CoT+C-Beam` |
| [DOS](dos.md) | WWW’26 Short | `Text+CF` | `Orth. RQ` | `Dec-Only†` | `Fixed†` | `NTP` | `–` |
| [GR4AD-X](gr4ad-x.md) | arXiv’26 | `–` | `Multi-Path R-KM+Hash` | `Enc-Dec` | `–` | `NTP + PV-RSPO + Rank + Aux.` | `PV-Beam+Rerank` |
| [GRLM](grlm.md) | arXiv’26 | `Text` | `Term-ID` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [SST](sst.md) | CIKM’26 | `Text` | `RQ+IST` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` | `BDQ` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring+Rerank` |
