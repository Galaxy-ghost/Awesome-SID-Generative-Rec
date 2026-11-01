# TriAlignGR

*Triangular Multitask Alignment with Multimodal Deep Interest Mining for Generative Recommendation* — Zeng et al., arXiv’26

[arXiv](https://arxiv.org/abs/2605.05249) · [Record](../../data/papers/trialigngr.yaml) · [← Catalog](../../README.md#i--representation)

> Abstract: "SID Content Degradation (SCD)"; "SID Semantic Opacity (SSO)". Candidates: I / III (rule: tie broken by the majority of new designs).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Representation** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Img`** | `RQ-VAE` | `Dec-Only` | `Fixed / Multi-task NTP` | `C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.
- `C-Beam`: Constrained beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "SID Content Degradation (SCD)"; "SID Semantic Opacity (SSO)". Candidates: I / III (rule: tie broken by the majority of new designs).
- **`tokenizer`** (p4): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p4): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

把视觉语义编进 SID，并用视觉描述等多任务让模型理解 SID 的含义。

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
| [SCRec](screc.md) | RecSys’26 | **`Text+CF`** → `RQ-VAE` → `Non-AR / Enc-Dec` → `Fixed / MTP + Ctr.` → `Scoring / Beam†` |
| [SPAR](spar.md) | arXiv’26 | **`Text+Geo`** → `R-KM` → `Dec-Only` → `Fixed / Multi-task NTP` → `–` |
