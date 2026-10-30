# SnapLGR

*LLM-Based Generative Retrieval for Snapchat Content Recommendation* — Collins et al., arXiv’26

[arXiv](https://arxiv.org/abs/2607.28895) · [Record](../../data/papers/snaplgr.yaml) · [← Catalog](../../README.md#ii--tokenization)

> 明确完整端到端工业系统且多组件共同构成贡献；SID 为语义簇，再由 materialization 映射具体视频。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **II. Uniqueness and Validity**: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF` | **`RQ-VAE+PPR`** | `Dec-Only` | `Fixed / Multi-task NTP` | `Beam` |

- `RQ-VAE+PPR`: RQ-VAE 构码时加基于 Personalized PageRank 共参与关系的对比监督。
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `Multi-task NTP`: The same NTP loss over several tasks.

## Same cell: II × Tokenization (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [CID](cid.md) | SIGIR-AP’23 | `CF` → **`Spectral Clus.`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TransRec](transrec.md) | KDD’24 | `Text` → **`Multi-Facet ID`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `FM-Index+Agg.` |
| [HiD-VAE](hid-vae.md) | arXiv’25 | `Text` → **`Hier. RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [PSI](psi.md) | arXiv’25 | `Text` → **`Post-hoc RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [AdaSID](adasid.md) | arXiv’26 | `Text+Img` → **`RQ`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [API](api.md) | arXiv’26 | `Text` → **`PID (P-SAE)`** → `Enc-Dec / Dec-Only (AR); Non-AR (PR)` → `Fixed / NTP + Rank + Aux. / MTP + Rank + Aux.` → `C-Beam / Scoring` |
| [CARD](card.md) | arXiv’26 | `Text+Img+CF` → **`NU-RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [DIGER](diger.md) | SIGIR’26 | `Text` → **`Learn. RQ`** → `Enc-Dec` → `Joint / NTP` → `Beam†` |
| [Gwhere](gwhere.md) | RecSys’26 | `Text+Img+Geo+CF` → **`Contr. RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `–` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` → **`QA-RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` → **`Ref.-RQ`** → `–` → `Fixed / NTP` → `Beam` |
