# MBGen

*Multi-Behavior Generative Recommendation* — Liu et al., CIKM’24

[arXiv](https://arxiv.org/abs/2405.16871) · [Record](../../data/papers/mbgen.yaml) · [← Catalog](../../README.md#i--training)

> Abstract: "neglecting the value of integrating the target behavior type into the learning objective".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `CF` | `Bal. VQ+KM` | `Enc-Dec` | **`Fixed / NTP`** | `Beam` |

- `CF`: Collaborative filtering signal.
- `Bal. VQ+KM`: Balanced SID: single-layer VQ plus per-prefix k-means (MBGen).
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "neglecting the value of integrating the target behavior type into the learning objective".
- **`tokenizer`** (§3.1–3.3, p3–5): Location from the pre-10-26 Training evidence in the appendix.
- **`objective`** (§3.1–3.3, p3–5): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: I × Training (3 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [RAGR](ragr.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP → DPO`** → `Beam† / –` |
| [REGER](reger.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP → (NTP + Aux.)`** → `Beam` |
| [SynGR](syngr.md) | ICML’26 | `Text+Img` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP + Ctr.`** → `C-Beam` |
