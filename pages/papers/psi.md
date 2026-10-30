# PSI

*Purely Semantic Indexing for LLM-based Generative Recommendation and Retrieval* — Zhang et al., arXiv’25

[arXiv](https://arxiv.org/abs/2509.16446) · [Record](../../data/papers/psi.yaml) · [← Catalog](../../README.md#ii--tokenization)

> 已有不收判定，按任务书维持；原理由见Table1收录筛选对应行。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **II. Uniqueness and Validity**: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Post-hoc RQ`** | `Enc-Dec` | `Fixed / NTP` | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "suffer from semantic ID conflicts".

## 旧目录说明

迁自 `d61aa6c:README.md` 的条目说明，未沿用旧目录的收录分类。

放宽最近质心分配，不追加非语义 token 也能得到唯一 SID。

## Same cell: II × Tokenization (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [CID](cid.md) | SIGIR-AP’23 | `CF` → **`Spectral Clus.`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TransRec](transrec.md) | KDD’24 | `Text` → **`Multi-Facet ID`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `FM-Index+Agg.` |
| [HiD-VAE](hid-vae.md) | arXiv’25 | `Text` → **`Hier. RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [AdaSID](adasid.md) | arXiv’26 | `Text+Img` → **`RQ`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [API](api.md) | arXiv’26 | `Text` → **`PID (P-SAE)`** → `Enc-Dec / Dec-Only (AR); Non-AR (PR)` → `Fixed / NTP + Rank + Aux. / MTP + Rank + Aux.` → `C-Beam / Scoring` |
| [CARD](card.md) | arXiv’26 | `Text+Img+CF` → **`NU-RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [DIGER](diger.md) | SIGIR’26 | `Text` → **`Learn. RQ`** → `Enc-Dec` → `Joint / NTP` → `Beam†` |
| [Gwhere](gwhere.md) | RecSys’26 | `Text+Img+Geo+CF` → **`Contr. RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `–` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` → **`QA-RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` → **`Ref.-RQ`** → `–` → `Fixed / NTP` → `Beam` |
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` → **`RQ-VAE+PPR`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
