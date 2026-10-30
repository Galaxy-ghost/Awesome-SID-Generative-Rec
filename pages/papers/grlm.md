# GRLM: Unleashing the Native Recommendation Potential: LLM-Based Generative Recommendation via Structured Term Identifiers

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2601.06798`)](https://arxiv.org/abs/2601.06798) · [Source Record (`data/papers/grlm.yaml`)](../../data/papers/grlm.yaml)

> **Summary**: Abstract: "Text-based methods introduce LLMs' vast output space, leading to hallucination"; "encounter a semantic gap between SIDs and LLMs' native vocabulary". Candidates: II / III (rule: tie broken by the majority of new designs).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Zhang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text` |  |
| **Tokenization** | `Term-ID` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Multi-task NTP` | The same NTP loss over several tasks. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "Text-based methods introduce LLMs' vast output space, leading to hallucination"; "encounter a semantic gap between SIDs and LLMs' native vocabulary". Candidates: II / III (rule: tie broken by the majority of new designs).

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
| [HoloRec](holorec.md) | arXiv’26 | `–` | `Nested RQ` | `Enc-Dec` | `Fixed` | `NTP + Aux.` | `–` |
| [SST](sst.md) | CIKM’26 | `Text` | `RQ+IST` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` | `BDQ` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring+Rerank` |
