# SCRec

*Addressing Cross-Stage Decoupling of Semantic and Collaborative Signals in Generative Recommendation* — Dan, RecSys’26

[arXiv](https://arxiv.org/abs/2609.13678) · [Record](../../data/papers/screc.yaml) · [← Catalog](../../README.md#i--representation)

> Abstract: "item tokenization is largely dominated by textual semantics with limited incorporation of collaborative signals"; "the generation stage tends to overlook the original semantic information".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Representation** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+CF`** | `RQ-VAE` | `Non-AR / Enc-Dec` | `Fixed / MTP + Ctr.` | `Scoring / Beam†` |

- `Non-AR / Enc-Dec`: Non-autoregressive and encoder–decoder backbone variants.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP + Ctr.`: MTP plus a contrastive loss.
- `Scoring / Beam†`: Discriminative candidate scoring vs. generative beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "item tokenization is largely dominated by textual semantics with limited incorporation of collaborative signals"; "the generation stage tends to overlook the original semantic information".
- **`tokenizer`** (§3.2–3.3, p4–5): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§3.2–3.3, p4–5): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: I × Representation (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [Molar](molar.md) | arXiv’24 | **`Text+Img+CF`** → `n/a` → `Dec-Only` → `n/a / Discrim.` → `Scoring` |
| [OneLoc](oneloc.md) | arXiv’25 | **`Text+Img+Geo†`** → `R-KM` → `Enc-Dec` → `Fixed / NTP → DPO` → `Beam` |
| [Q-BERT4Rec](q-bert4rec.md) | arXiv’25 | **`Text+Img+CF`** → `RQ-VAE` → `Encoder (Non-AR)` → `Fixed / Masked` → `Non-AR` |
| [UNGER](unger.md) | TOIS’25 | **`Text+CF`** → `R-KM` → `Enc-Dec` → `Fixed / NTP + Ctr.` → `Beam` |
| [GeoGR](geogr.md) | arXiv’26 | **`Text+Geo+CF`** → `R-KM+EM` → `Dec-Only` → `Altern.† / Multi-task NTP` → `Beam` |
| [HF-SID](hf-sid.md) | arXiv’26 | **`Text+Attr+Geo`** → `R-KM` → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [LGRID](lgrid.md) | arXiv’26 | **`Text+Geo`** → `DSRQ` → `Disc.` → `Fixed / Discrim.` → `Scoring` |
| [LGSID](lgsid.md) | AAAI’26 | **`Text+Geo+CF`** → `Geo-Idx+RQ` → `Disc. / Enc-Dec` → `Fixed / Discrim. / NTP` → `Scoring / Beam†` |
| [ReSID](resid.md) | arXiv’26 | **`Attr+CF`** → `GAOQ` → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [SPAR](spar.md) | arXiv’26 | **`Text+Geo`** → `R-KM` → `Dec-Only` → `Fixed / Multi-task NTP` → `–` |
| [TriAlignGR](trialigngr.md) | arXiv’26 | **`Text+Img`** → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam` |
