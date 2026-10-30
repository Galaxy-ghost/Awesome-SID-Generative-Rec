# CID

*How to Index Item IDs for Recommendation Foundation Models* — Hua et al., SIGIR-AP’23

[arXiv](https://arxiv.org/abs/2305.06569) · [Record](../../data/papers/cid.yaml) · [← Catalog](../../README.md#ii--tokenization)

> Abstract: "To avoid generating excessively long text and hallucinated recommendations"; "creating LLM-compatible item IDs to uniquely identify each item is essential". Candidates: II / I (rule: judged by the abstract's complaint first).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **II. Uniqueness and Validity**: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `CF` | **`Spectral Clus.`** | `Enc-Dec` | `Fixed / NTP` | `C-Beam` |

- `CF`: Collaborative filtering signal.
- `Spectral Clus.`: Recursive spectral clustering on the co-occurrence graph (CID).
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "To avoid generating excessively long text and hallucinated recommendations"; "creating LLM-compatible item IDs to uniquely identify each item is essential". Candidates: II / I (rule: judged by the abstract's complaint first).
- **`tokenizer`** (p2; §5.2): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (p2; §5.2): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: II × Tokenization (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
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
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` → **`RQ-VAE+PPR`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
