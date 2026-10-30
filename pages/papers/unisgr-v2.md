# UniSGR-V2

*Stepwise Target-Side Feature Anticipation and Crossing for Generative Recommendation* — Yang et al., arXiv’26

[arXiv](https://arxiv.org/abs/2610.16132) · [Record](../../data/papers/unisgr-v2.yaml) · [← Catalog](../../README.md#i--backbone)

> Semantic-ID-based generative recommendation unifies retrieval and ranking through autoregressive decoding but differs structurally from discriminative models, which can directly access rich target-item side features. The attributes are compressed into a finite codebook during quantization, while the target item remains undetermined during decoding and its features cannot be looked up. This target-side feature vacuum weakens generation at each semantic-ID level through high conditional entropy and cascading errors, and final ranking through missing target-side feature crossing. Existing methods interact with candidate representations or generate discrete attribute tokens, but none reconstructs a continuous target-side representation inside decoding to support both stepwise generation and ranking. We propose TacGR (Stepwise Target-Side Feature Anticipation and Crossing for Generative Recommendation). Before decoding each codeword, TacGR anticipates a continuous target-side feature vector and crosses it with the semantic prefix and user behavior sequence inside the decoder. The crossed representation conditions current-level generation and is directly used for ranking. Continuous-vector regression risks a learnable target collapsing with its prediction and prediction noise propagating into generation through attention. TacGR addresses these challenges with a semantic-anchoring auxiliary tower and a unidirectional visibility mask, respectively. For extremely long industrial behavior histories, it introduces gated convolutional denoising to suppress noise and adapts the pyramid memory funnel to reduce inference cost. Offline experiments on a large-scale Lazada dataset show significant gains over OneRec, UniRec, and UniSGR. Online A/B testing improves IPV, Order, and GMV by 0.79%, 5.55%, and 3.09%, respectively.

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `–` | `–` | **`Enc-Dec`** | `– / NTP + Rank` | `Beam` |

- `–`: Not reported in the paper, or not applicable.
- `–`: No item SID is built, or not reported.
- `Enc-Dec`: Encoder-decoder.
- `–`: No SID is built.
- `NTP + Rank`: NTP plus a ranking loss.

## Same cell: I × Backbone (6 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [ColaRec](colarec.md) | CIKM’24 | `Text+CF` → `H-KM` → **`Enc-Dec`** → `Fixed / NTP + Ctr.` → `C-Beam` |
| [EAGER](eager.md) | KDD’24 | `Text+CF` → `Dual H-KM` → **`Dual Enc-Dec`** → `Fixed / NTP + Ctr.` → `Fusion` |
| [COBRA](cobra.md) | NeurIPS’25 | `Text+SID` → `Casc. RQ` → **`Dec-Only`** → `Fixed / NTP + Dense` → `BeamFusion` |
| [DiscRec](discrec.md) | arXiv’25 | `Text+CF` → `RQ-VAE / Learn. RQ` → **`Enc-Dec`** → `Fixed / NTP` → `C-Beam` |
| [Spacetime-GR](spacetime-gr.md) | arXiv’25 | `Geo` → `Geo-Idx` → **`Dec-Only`** → `Fixed / NTP → DPO` → `Beam` |
| [SPAR-Youku](spar-youku.md) | arXiv’26 | `–` → `RQ-PIB` → **`Dec-Only`** → `Fixed / NTP → DPO` → `C-Beam` |
