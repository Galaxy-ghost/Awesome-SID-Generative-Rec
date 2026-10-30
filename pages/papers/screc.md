# SCRec: Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2609.13678`)](https://arxiv.org/abs/2609.13678) · [Source Record (`data/papers/screc.yaml`)](../../data/papers/screc.yaml)

> **Summary**: Abstract: "item tokenization is largely dominated by textual semantics with limited incorporation of collaborative signals"; "the generation stage tends to overlook the original semantic information".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Dan (2026) | Published / posted in `RecSys’26` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Representation` | The primary design change sits in the Representation stage. |
| **Representation** | `Text+CF` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Non-AR / Enc-Dec` | Parallel prediction heads (main setting) vs. Encoder-Decoder TIGER integration (SCRec). |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `MTP + Ctr.` | MTP plus a contrastive loss. |
| **Inference Decoding** | `Scoring / Beam†` | Discriminative candidate scoring vs. generative beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "item tokenization is largely dominated by textual semantics with limited incorporation of collaborative signals"; "the generation stage tends to overlook the original semantic information".
- **`tokenizer`** (§3.2–3.3, p4–5): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§3.2–3.3, p4–5): Location from the pre-10-26 Training evidence in the appendix.

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
| [ReSID](resid.md) | arXiv’26 | `Attr+CF` | `GAOQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [SPAR](spar.md) | arXiv’26 | `Text+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [TriAlignGR](trialigngr.md) | arXiv’26 | `Text+Img` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
