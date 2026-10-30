# ReSID: Rethinking Generative Recommender Tokenizer: Recsys-Native Encoding and Semantic Quantization Beyond LLMs

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2602.02338`)](https://arxiv.org/abs/2602.02338) · [Source Record (`data/papers/resid.yaml`)](../../data/papers/resid.yaml)

> **Summary**: 提出完整 SID 构造方法并在统一生成推荐器上验证。

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Liang et al. (2026) | Published / posted in `arXiv’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Representation` | The primary design change sits in the Representation stage. |
| **Representation** | `Attr+CF` | Structured item attributes plus collaborative filtering signals (ReSID). |
| **Tokenization** | `GAOQ` | Globally Aligned Orthogonal Quantization，全局对齐正交量化。 |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Peer Methods in `I. Informativeness` × `Representation` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Molar](molar.md) | arXiv’24 | `Text+Img+CF` | `–` | `Dec-Only` | `–` | `Discrim.` | `Scoring` |
| [OneLoc](oneloc.md) | arXiv’25 | `Text+Img+Geo†` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP → DPO` | `Beam` |
| [Q-BERT4Rec](q-bert4rec.md) | arXiv’25 | `Text+Img+CF` | `RQ-VAE` | `Encoder (Non-AR)` | `Fixed` | `Masked` | `Non-AR` |
| [UNGER](unger.md) | TOIS’25 | `Text+CF` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [GeoGR](geogr.md) | arXiv’26 | `Text+Geo+CF` | `R-KM+EM` | `Dec-Only` | `Altern.†` | `Multi-task NTP` | `Beam` |
| [HF-SID](hf-sid.md) | arXiv’26 | `Text+Attr+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [LGRID](lgrid.md) | arXiv’26 | `Text+Geo` | `DSRQ` | `Disc.` | `Fixed` | `Discrim.` | `Scoring` |
| [LGSID](lgsid.md) | AAAI’26 | `Text+Geo+CF` | `Geo-Idx+RQ` | `Disc. / Enc-Dec` | `Fixed` | `Discrim. / NTP` | `Scoring / Beam†` |
| [SCRec](screc.md) | RecSys’26 | `Text+CF` | `RQ-VAE` | `Non-AR / Enc-Dec` | `Fixed` | `MTP + Ctr.` | `Scoring / Beam†` |
| [SPAR](spar.md) | arXiv’26 | `Text+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [TriAlignGR](trialigngr.md) | arXiv’26 | `Text+Img` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
