# REGER

*Modeling inter-item Relations with Semantic IDs for Generative Recommendation* — Huang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.37584) · [Record](../../data/papers/reger.yaml) · [← Catalog](../../README.md#i--training)

> Personalized recommendation depends on learning semantic and collaborative relations among items from online content and user interactions. Generative recommendation (GR) offers a promising paradigm by autoregressively generating discrete semantic IDs (SIDs) of items. However, randomly initialized SID token embeddings and GR models trained from scratch do not directly inherit the semantic relations inherent in items, while inter-item collaborative relations are learned largely implicitly through token-level attention and next-token supervision. To address this limitation, we propose REGER, a unified framework that explicitly incorporates inter-item relations into semantic pretraining, history encoding, and SID generation. We pretrain the GR model through generative semantic retrieval, enabling it to inherit inter-item semantic similarity by learning to generate semantic neighbors' SIDs. We combine global attention with local attention aligned with SID boundaries to capture historical context and directed transitions between adjacent items. We further develop a theoretical framework for hierarchical preference decomposition over the SID prefix tree, proving an exact factorization of collaborative preference distributions and a weighted decomposition of item-level KL divergence into prefix-conditional KL divergences. Building on this analysis, we distill a discriminative teacher's full conditional distributions over all legal next tokens at ground-truth prefixes along the target SID path, jointly optimizing this objective with cross-entropy. Extensive experiments on real-world datasets demonstrate consistent improvements over existing GR baselines and support the effectiveness of the proposed preference distillation.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Training** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | `RQ-VAE` | `Enc-Dec` | **`Fixed / NTP → (NTP + Aux.)`** | `Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → (NTP + Aux.)`: Next-token prediction, followed by joint optimization of next-token prediction and auxiliary objectives.

## Same cell: I × Training (3 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [MBGen](mbgen.md) | CIKM’24 | `CF` → `Bal. VQ+KM` → `Enc-Dec` → **`Fixed / NTP`** → `Beam` |
| [RAGR](ragr.md) | arXiv’26 | `Text` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP → DPO`** → `Beam† / –` |
| [SynGR](syngr.md) | ICML’26 | `Text+Img` → `RQ-VAE` → `Enc-Dec` → **`Fixed / NTP + Ctr.`** → `C-Beam` |
