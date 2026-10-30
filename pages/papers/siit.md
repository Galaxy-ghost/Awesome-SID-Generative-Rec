# SIIT: Enhancing item tokenization for generative recommendation through self-improvement

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2412.17171`)](https://arxiv.org/abs/2412.17171) · [Source Record (`data/papers/siit.yaml`)](../../data/papers/siit.yaml)

> **Summary**: Abstract: "may not align with the LLM's internal pretrained tokenization schema".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Chen et al. (2024) | Published / posted in `arXiv’24` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Self-Imp.` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Altern.` | Tokenizer and generator are updated in turns. |
| **Training Objective** | `Multi-task NTP` | The same NTP loss over several tasks. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "may not align with the LLM's internal pretrained tokenization schema".

## Peer Methods in `III. SID–Model Alignment` × `Tokenization` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [IDGenRec](idgenrec.md) | SIGIR’24 | `Text` | `LLM-Vocab` | `Enc-Dec` | `Altern.` | `NTP` | `C-Beam` |
| [SemConv](semconv.md) | AAAI’25 | `Text+CF` | `Align. RQ` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` | `Dual RQ` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Beam` |
| [CogRec](cogrec.md) | arXiv’26 | `Text` | `R-KM+Graph` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `CoT+C-Beam` |
| [DOS](dos.md) | WWW’26 Short | `Text+CF` | `Orth. RQ` | `Dec-Only†` | `Fixed†` | `NTP` | `–` |
| [GR4AD-X](gr4ad-x.md) | arXiv’26 | `–` | `Multi-Path R-KM+Hash` | `Enc-Dec` | `–` | `NTP + PV-RSPO + Rank + Aux.` | `PV-Beam+Rerank` |
| [GRLM](grlm.md) | arXiv’26 | `Text` | `Term-ID` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [HoloRec](holorec.md) | arXiv’26 | `–` | `Nested RQ` | `Enc-Dec` | `Fixed` | `NTP + Aux.` | `–` |
| [SST](sst.md) | CIKM’26 | `Text` | `RQ+IST` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` | `BDQ` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring+Rerank` |
