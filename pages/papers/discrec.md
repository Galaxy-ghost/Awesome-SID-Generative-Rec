# DiscRec

*Disentangled Semantic-Collaborative Modeling for Generative Recommendation* — Liu et al., arXiv’25

[arXiv](https://arxiv.org/abs/2506.15576) · [Record](../../data/papers/discrec.yaml) · [← Catalog](../../README.md#i--backbone)

> Abstract: "token-item misalignment"; "semantic-collaborative signal entanglement". Candidates: I / III (rule: tie broken by the title).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `RQ-VAE / Learn. RQ` | **`Enc-Dec`** | `Fixed / NTP` | `C-Beam` |

- `RQ-VAE / Learn. RQ`: Residual-quantized variational codes or learnable residual-quantization codes in different configurations.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

## Evidence

- **`problem`** (arXiv abstract): Abstract: "token-item misalignment"; "semantic-collaborative signal entanglement". Candidates: I / III (rule: tie broken by the title).
- **`tokenization`** (§I, p2; §IV-A, p7): Settings A/B take the TIGER and LETTER rows of Table 1.
- **`tokenizer`** (§II-A–B, p3): Location from the pre-10-26 Training evidence in the appendix.

## Same cell: I × Backbone (6 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` → `H-KM` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` → `Dual H-KM` → **`Dual Enc-Dec`** → `Fixed / NTP + Ctr.` → `Fusion` |
| [COBRA](cobra.md) | NeurIPS’25 | `Text+SID` → `Casc. RQ` → **`Dec-Only`** → `Fixed / NTP + Dense` → `BeamFusion` |
| [Spacetime-GR](spacetime-gr.md) | arXiv’25 | `Geo` → `Geo-Idx` → **`Dec-Only`** → `Fixed / NTP → DPO` → `Beam` |
| [SPAR-Youku](spar-youku.md) | arXiv’26 | `–` → `RQ-PIB` → **`Dec-Only`** → `Fixed / NTP → DPO` → `C-Beam` |
| [UniSGR-V2](unisgr-v2.md) | arXiv’26 | `–` → `–` → **`Enc-Dec`** → `– / NTP + Rank` → `Beam` |
