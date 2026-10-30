# Molar

*Multimodal llms with collaborative filtering alignment for enhanced sequential recommendation* — Luo et al., arXiv’24

[arXiv](https://arxiv.org/abs/2412.18176) · [Record](../../data/papers/molar.yaml) · [← Catalog](../../README.md#i--representation)

> Abstract: "inherently lack collaborative filtering information, relying primarily on textual content data neglecting other modalities".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Representation** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Img+CF`** | `–` | `Dec-Only` | `– / Discrim.` | `Scoring` |

- `–`: No item SID is built, or not reported.
- `Dec-Only`: Decoder-only.
- `–`: No SID is built.
- `Discrim.`: Scores items; does not generate SIDs.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "inherently lack collaborative filtering information, relying primarily on textual content data neglecting other modalities".
- **`tokenizer`** (p3): Location from the 10-26 'Training split' table in the appendix.
- **`objective`** (p3): Location from the 10-26 'Training split' table in the appendix.

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

用多模态 LLM 产出用户和物品嵌入，按相似度推荐，不使用 SID。

## Same cell: I × Representation (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
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
| [TriAlignGR](trialigngr.md) | arXiv’26 | **`Text+Img`** → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam` |
