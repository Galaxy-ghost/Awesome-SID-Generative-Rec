# LGSID: LLM-Aligned Geographic Item Tokenization for Local-Life Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2511.14221`)](https://arxiv.org/abs/2511.14221) · [Source Record (`data/papers/lgsid.yaml`)](../../data/papers/lgsid.yaml)

> **Summary**: Abstract: "simply injecting location information into prompts fails to capture fine-grained spatial characteristics and real-world distance awareness among items".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Jiang et al. (2026) | Published / posted in `AAAI’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Representation` | The primary design change sits in the Representation stage. |
| **Representation** | `Text+Geo+CF` |  |
| **Tokenization** | `Geo-Idx+RQ` | Geographic attribute index plus residual quantization (LGSID). |
| **Backbone** | `Disc. / Enc-Dec` | Evaluated on both discriminative rankers (DIN, etc.) and Encoder-Decoder generative models (LGSID). |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `Discrim. / NTP` | Discriminative scoring objective vs. generative next-token prediction objective (LGSID). |
| **Inference Decoding** | `Scoring / Beam†` | Discriminative candidate scoring vs. generative beam search. |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (abstract, p1): Abstract: "simply injecting location information into prompts fails to capture fine-grained spatial characteristics and real-world distance awareness among items".
- **`stage`** (contribution list, p2; p4): Both designs (RL-based geographic alignment, hierarchical geographic tokenization) fix the same problem; the first contribution, aligning the item-encoding LLM (G-DPO), decides.
- **`backbone`** (Table 1, Table 2, p5–6): Discriminative models DIN, TWIN, ETA etc. (Table 1 of the paper); generative experiments on TIGER and OneRec (Table 2 of the paper), both Enc-Dec in Table 1.

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
| [ReSID](resid.md) | arXiv’26 | `Attr+CF` | `GAOQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [SCRec](screc.md) | RecSys’26 | `Text+CF` | `RQ-VAE` | `Non-AR / Enc-Dec` | `Fixed` | `MTP + Ctr.` | `Scoring / Beam†` |
| [SPAR](spar.md) | arXiv’26 | `Text+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [TriAlignGR](trialigngr.md) | arXiv’26 | `Text+Img` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
