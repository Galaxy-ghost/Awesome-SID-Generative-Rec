# IDGenRec: Idgenrec: Llm-recsys alignment with textual id learning

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2403.19021`)](https://arxiv.org/abs/2403.19021) · [Source Record (`data/papers/idgenrec.yaml`)](../../data/papers/idgenrec.yaml)

> **Summary**: Abstract: "struggles to effectively encode recommendation items within the text-to-text framework".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Tan et al. (2024) | Published / posted in `SIGIR’24` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `LLM-Vocab` |  |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Altern.` | Tokenizer and generator are updated in turns. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "struggles to effectively encode recommendation items within the text-to-text framework".
- **`tokenizer`** (p4): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p4): Location from the 10-26 'Training split' table in the appendix.

## Peer Methods in `III. SID–Model Alignment` × `Tokenization` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [SIIT](siit.md) | arXiv’24 | `Text` | `Self-Imp.` | `Enc-Dec` | `Altern.` | `Multi-task NTP` | `C-Beam` |
| [SemConv](semconv.md) | AAAI’25 | `Text+CF` | `Align. RQ` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` | `Dual RQ` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Beam` |
| [CogRec](cogrec.md) | arXiv’26 | `Text` | `R-KM+Graph` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `CoT+C-Beam` |
| [DOS](dos.md) | WWW’26 Short | `Text+CF` | `Orth. RQ` | `Dec-Only†` | `Fixed†` | `NTP` | `–` |
| [GR4AD-X](gr4ad-x.md) | arXiv’26 | `–` | `Multi-Path R-KM+Hash` | `Enc-Dec` | `–` | `NTP + PV-RSPO + Rank + Aux.` | `PV-Beam+Rerank` |
| [GRLM](grlm.md) | arXiv’26 | `Text` | `Term-ID` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [HoloRec](holorec.md) | arXiv’26 | `–` | `Nested RQ` | `Enc-Dec` | `Fixed` | `NTP + Aux.` | `–` |
| [SST](sst.md) | CIKM’26 | `Text` | `RQ+IST` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` | `BDQ` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring+Rerank` |
