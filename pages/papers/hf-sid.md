# HF-SID: HF-SID: High-Fidelity Semantic IDs for Generative Retrieval in Location-Based Services

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2608.30479`)](https://arxiv.org/abs/2608.30479) · [Source Record (`data/papers/hf-sid.yaml`)](../../data/papers/hf-sid.yaml)

> **Summary**: 直接研究 POI SID 质量并用于下游 next-POI 生成，建议保留方法；完整码到多 POI 的物化仍须明确标未知。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Lin et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Representation` | The primary design change sits in the Representation stage. |
| **Representation** | `Text+Attr+Geo` | Attr 特指数值业务属性，Geo 包括连续坐标 |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `C-Beam` | Constrained beam search. |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `I. Informativeness` × `Representation` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Molar](molar.md) | arXiv’24 | `Text+Img+CF` | `–` | `Dec-Only` | `–` | `Discrim.` | `Scoring` |
| [OneLoc](oneloc.md) | arXiv’25 | `Text+Img+Geo†` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP → DPO` | `Beam` |
| [Q-BERT4Rec](q-bert4rec.md) | arXiv’25 | `Text+Img+CF` | `RQ-VAE` | `Encoder (Non-AR)` | `Fixed` | `Masked` | `Non-AR` |
| [UNGER](unger.md) | TOIS’25 | `Text+CF` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [GeoGR](geogr.md) | arXiv’26 | `Text+Geo+CF` | `R-KM+EM` | `Dec-Only` | `Altern.†` | `Multi-task NTP` | `Beam` |
| [LGRID](lgrid.md) | arXiv’26 | `Text+Geo` | `DSRQ` | `Disc.` | `Fixed` | `Discrim.` | `Scoring` |
| [LGSID](lgsid.md) | AAAI’26 | `Text+Geo+CF` | `Geo-Idx+RQ` | `Disc. / Enc-Dec` | `Fixed` | `Discrim. / NTP` | `Scoring / Beam†` |
| [ReSID](resid.md) | arXiv’26 | `Attr+CF` | `GAOQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [SCRec](screc.md) | RecSys’26 | `Text+CF` | `RQ-VAE` | `Non-AR / Enc-Dec` | `Fixed` | `MTP + Ctr.` | `Scoring / Beam†` |
| [SPAR](spar.md) | arXiv’26 | `Text+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [TriAlignGR](trialigngr.md) | arXiv’26 | `Text+Img` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
