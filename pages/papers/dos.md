# DOS: DOS: Dual-Flow Orthogonal Semantic IDs for Recommendation in Meituan

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2602.04460`)](https://arxiv.org/abs/2602.04460) · [Source Record (`data/papers/dos.yaml`)](../../data/papers/dos.yaml)

> **Summary**: The abstract identifies the codebook-generation gap (III) and semantic loss during quantization (I), addressed by DFI and ORQ respectively. The designs and title cover both equally; the first contribution, DFI, breaks the tie in favor of alignment.

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Yin et al. (2026) | Published / posted in `WWW’26 Short` |
| **Problem Band** | `III. SID–Model Alignment` | Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| **Primary Stage** | `Tokenization` | The primary design change sits in the Tokenization stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `Orth. RQ` | Orthogonal residual quantization with task-relevant dimension selection and layer-wise residual coding (DOS; ORQ in the paper). |
| **Backbone** | `Dec-Only†` |  |
| **Tokenizer Training** | `Fixed†` |  |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `–` | Not reported in the paper. |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (abstract, p1; contribution list, p2): The abstract identifies the codebook-generation gap (III) and semantic loss during quantization (I), addressed by DFI and ORQ respectively. The designs and title cover both equally; the first contribution, DFI, breaks the tie in favor of alignment.
- **`stage`** (contribution 1, p2; §2.1, p2; Fig. 1(a), p3): The first contribution is Dual-Flow Integration (DFI), which incorporates user-item collaborative information directly into quantization through two flows and a shared codebook. It changes SID construction, not the generation backbone.
- **`representation`** (§2.1, Eq. (1)–(5), p2): Qwen3-0.6B-embedding encodes restaurant names, categories, dishes and prices. DFI adds collaborative signals from click sequences and target items during SID construction. No explicit geographic field is reported in the prompt template.

## Peer Methods in `III. SID–Model Alignment` × `Tokenization` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [IDGenRec](idgenrec.md) | SIGIR’24 | `Text` | `LLM-Vocab` | `Enc-Dec` | `Altern.` | `NTP` | `C-Beam` |
| [SIIT](siit.md) | arXiv’24 | `Text` | `Self-Imp.` | `Enc-Dec` | `Altern.` | `Multi-task NTP` | `C-Beam` |
| [SemConv](semconv.md) | AAAI’25 | `Text+CF` | `Align. RQ` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [Align3GR](align3gr.md) | AAAI’26 | `Text+CF` | `Dual RQ` | `Dec-Only` | `Fixed` | `NTP → DPO` | `Beam` |
| [CogRec](cogrec.md) | arXiv’26 | `Text` | `R-KM+Graph` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `CoT+C-Beam` |
| [GR4AD-X](gr4ad-x.md) | arXiv’26 | `–` | `Multi-Path R-KM+Hash` | `Enc-Dec` | `Fixed` | `NTP + PV-RSPO + Rank + Aux.` | `PV-Beam+Rerank` |
| [GRLM](grlm.md) | arXiv’26 | `Text` | `Term-ID` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [HoloRec](holorec.md) | arXiv’26 | `–` | `Nested RQ` | `Enc-Dec` | `Fixed` | `NTP + Aux.` | `–` |
| [SST](sst.md) | CIKM’26 | `Text` | `RQ+IST` | `Enc-Dec` | `Fixed` | `NTP` | `C-Beam` |
| [TopoGR](topogr.md) | arXiv’26 | `Text` | `BDQ` | `Non-AR` | `Fixed` | `MTP + Aux.` | `Scoring+Rerank` |
