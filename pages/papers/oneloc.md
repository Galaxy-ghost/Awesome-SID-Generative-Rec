# OneLoc: OneLoc: Geo-Aware Generative Recommender Systems for Local Life Service

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2508.14646`)](https://arxiv.org/abs/2508.14646) · [Source Record (`data/papers/oneloc.yaml`)](../../data/papers/oneloc.yaml)

> **Summary**: Abstract: "how to make full use of geographic information"; "how to balance multiple objectives, including user interests, the distance between user and stores, and some other business objectives". Three designs fix I (geo-aware SID, geo-aware self-attention, neighbor-aware prompt) against two rewards for IV. The complaints fit the six problems, so the paper is not in the top block (unlike OneRec).

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Wei et al. (2025) | Published / posted in `arXiv’25` |
| **Problem Band** | `I. Informativeness` | Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| **Primary Stage** | `Representation` | The primary design change sits in the Representation stage. |
| **Representation** | `Text+Img+Geo†` |  |
| **Tokenization** | `R-KM` | Residual k-means. |
| **Backbone** | `Enc-Dec` | Encoder-decoder. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP → DPO` | NTP, then preference optimization. |
| **Inference Decoding** | `Beam` |  |
| **POI / Local-Life** | `true` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (abstract, p1): Abstract: "how to make full use of geographic information"; "how to balance multiple objectives, including user interests, the distance between user and stores, and some other business objectives". Three designs fix I (geo-aware SID, geo-aware self-attention, neighbor-aware prompt) against two rewards for IV. The complaints fit the six problems, so the paper is not in the top block (unlike OneRec).
- **`stage`** (contribution list, p3; §2.2, p3): The three designs for I sit in Representation and Backbone; the first contribution, the geo-aware SID, decides. Its quantizer follows OneRec; only the input embedding adds location context.
- **`representation`** (§2.1, §2.2, p3): No collaborative signal enters the SIDs. Img is inferred from "video content and location context information, extracted by a multimodal large language model". Table 2 had Text+Img+Geo+CF.

## Positioning in the Problem × Stage Matrix

- **Matrix Cell**: **I. Informativeness** $\times$ **Representation** (`problem: I`, `stage: Representation`, `poi: true`).
- **Why Here**: In local-life and point-of-interest (POI) recommendation, item semantics depend jointly on multimodal content and physical geography. OneLoc enriches the **Representation** stage (`Text+Img+Geo†`) before residual $k$-means (`R-KM`) tokenization, and couples it with geo-aware encoder self-attention, neighbor-aware decoder prompts, and two-stage `NTP → DPO` optimization with geographic distance and GMV rewards.

```
Short Video + Store Metadata + Location Context (lat/lon, geohash, district)
  │
  ▼  [1. Representation: Multimodal LLM extracts fused Text+Img+Geo† embedding e_i]
Geo-aware item representation e_i ∈ ℝ^d
  │
  ▼  [2. Tokenization: L-level Residual K-Means (R-KM) with Fixed codebooks]
Discrete Geo-Aware Semantic ID s_i = (s_{i,1}, ..., s_{i,L})
  │
  ▼  [3. Backbone: Encoder (Geo-Aware Self-Attention) + Decoder (Neighbor-Aware Prompt)]
Autoregressive policy π_θ(s_target | u, loc_u, H_u)
  │
  ▼  [4. Training: Supervised NTP pre-training → DPO with Geo + GMV rewards]
  │
  ▼  [5. Inference: Beam Search]
Top-K local-life stores / videos
```

---

## Core Mechanism & Annotated Walkthrough

### Step 1: Geo-Aware Multimodal Representation & `R-KM` Tokenization

For each local-life item $i$ (a short video linked to a physical store), OneLoc prompts a multimodal large language model (MLLM) with the video frames, textual description, and structured geographic context (city, business district, coordinates) to extract a unified dense representation $\mathbf{e}_i \in \mathbb{R}^d$ (`Text+Img+Geo†`).

Following OneRec, OneLoc quantizes $\mathbf{e}_i$ into an $L$-level discrete Semantic ID $\mathbf{s}_i = (s_{i,1}, \dots, s_{i,L})$ via Residual K-Means (`R-KM`, §2.2, Eq. 1–3):

$$\mathbf{r}_i^{(1)} = \mathbf{e}_i, \qquad s_{i,l} = \arg\min_{k \in \{1,\dots,K\}} \left\| \mathbf{r}_i^{(l)} - \mathbf{c}_k^{(l)} \right\|_2^2, \qquad \mathbf{r}_i^{(l+1)} = \mathbf{r}_i^{(l)} - \mathbf{c}_{s_{i,l}}^{(l)}$$

where $\mathcal{C}^{(l)} = \{\mathbf{c}_k^{(l)}\}_{k=1}^{K}$ is the level-$l$ centroid matrix trained offline and kept `Fixed` during recommender training.

### Step 2: Geo-Aware Self-Attention & Neighbor-Aware Decoder Prompt

In the encoder (§2.3), given user history items with locations $\{(\mathbf{h}_j, \ell_j)\}_{j=1}^{T}$ and the user's real-time location $\ell_u$, OneLoc modulates self-attention logits with a gated spatial bias $\mathbf{B}^{\text{geo}} \in \mathbb{R}^{T \times T}$ derived from pairwise Haversine distances $d(\ell_j, \ell_{j'})$ and user-to-store distances $d(\ell_u, \ell_j)$:

$$\operatorname{Attn}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \operatorname{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + g_u \odot \mathbf{B}^{\text{geo}}\right)\mathbf{V}$$

In the decoder (§2.4), a **Neighbor-Aware Prompt** injects the Semantic IDs of stores within the user's current geohash cell $\mathcal{N}(\ell_u)$ as prefix context so the decoder attends directly to physically reachable candidates.

### Step 3: Two-Stage `NTP → DPO` with Geographic and Commercial Rewards

After supervised next-token prediction (`NTP`) pre-training (§2.5, Eq. 20–21), OneLoc samples $G$ candidate Semantic IDs $\{\mathbf{s}^{(1)}, \dots, \mathbf{s}^{(G)}\}$ via beam search for each user request $(u, \ell_u)$ and scores each valid store using a composite reward combining spatial proximity $R_{\text{geo}}$ and expected Gross Merchandise Volume $R_{\text{GMV}}$:

$$R(\mathbf{s}, u, \ell_u) = \lambda_{\text{geo}}\, R_{\text{geo}}\!\left(d(\ell_u, \ell_{\mathbf{s}})\right) + \lambda_{\text{GMV}}\, R_{\text{GMV}}(\mathbf{s}, u)$$

Winning-losing pairs $(\mathbf{s}_w, \mathbf{s}_l)$ with $R(\mathbf{s}_w) > R(\mathbf{s}_l)$ optimize the Direct Preference Optimization (`DPO`, §2.5, Eq. 24) objective relative to the reference NTP policy $\pi_{\text{ref}}$:

$$\mathcal{L}_{\text{DPO}}(\theta) = -\mathbb{E}_{(x, \mathbf{s}_w, \mathbf{s}_l)} \left[ \log \sigma\!\left( \beta \log \frac{\pi_\theta(\mathbf{s}_w \mid x)}{\pi_{\text{ref}}(\mathbf{s}_w \mid x)} - \beta \log \frac{\pi_\theta(\mathbf{s}_l \mid x)}{\pi_{\text{ref}}(\mathbf{s}_l \mid x)} \right) \right]$$

```python
# Annotated PyTorch walkthrough of OneLoc's Geo-Aware Attention + DPO loss
# Reference: Wei et al. (arXiv:2508.14646), §2.3 & §2.5 Eq. (20)-(24)
def oneloc_geo_dpo_step(q, k, v, dist_matrix, geo_bucket_emb, gate,
                        logp_theta_w, logp_theta_l, logp_ref_w, logp_ref_l, beta=0.1):
    """
    q, k, v:       [B, H, T, d_k] encoder query/key/value tensors
    dist_matrix:   [B, T, T] bucketed pairwise spatial distance indices
    gate:          [B, H, 1, 1] learnable sigmoid gate g_u
    logp_*:        [B] sequence log-probabilities sum_{l=1}^L log pi(s_l | s_<l, x)
    """
    # 1. Geo-aware self-attention with gated spatial distance bias (§2.3)
    geo_bias = geo_bucket_emb(dist_matrix).permute(0, 3, 1, 2)  # [B, H, T, T]
    scores = (q @ k.transpose(-2, -1)) / (q.size(-1) ** 0.5) + torch.sigmoid(gate) * geo_bias
    attn_out = scores.softmax(dim=-1) @ v

    # 2. DPO preference alignment over Geo + GMV ranked beam pairs (§2.5 Eq. 24)
    delta_w = logp_theta_w - logp_ref_w
    delta_l = logp_theta_l - logp_ref_l
    dpo_loss = -torch.nn.functional.logsigmoid(beta * (delta_w - delta_l)).mean()
    return attn_out, dpo_loss
```

---

## Verbatim Quotes from the Paper

- **Problem statement** (Abstract, p.1): *"Two critical challenges remain in local life service recommendation: (1) how to make full use of geographic information, and (2) how to balance multiple objectives, including user interests, the distance between user and stores, and some other business objectives."*
- **Multimodal + geographic representation** (§2.1–2.2, p.3): *"We first extract item representations from video content and location context information, extracted by a multimodal large language model ... Following OneRec, we use res-kmeans to quantize the item representations into discrete semantic IDs."*
- **DPO alignment with dual rewards** (§2.5, p.5): *"We design a Geography Reward and a GMV Reward to construct preference pairs from beam search candidates, and apply Direct Preference Optimization (DPO) to align the generative model."*

---

## Experimental Protocol & Key Results

- **Datasets & Deployment**: Evaluated on industrial Kuaishou local-life service logs and deployed in online A/B testing serving $\sim 400\text{M}$ daily active users.
- **Reported Gains** (§3.2–3.4 of the paper):
  - **Online A/B Test**: Reports **+21.016% GMV** and **+17.891% order volume** over the production multi-stage local-life ranking baseline.
  - **Module Ablations**: Removing geo-aware SIDs, geo-aware self-attention, neighbor-aware prompts, or either DPO reward (`Geo` / `GMV`) degrades both offline hit rate and distance compliance.

---

## Limitations & Comparison with Peer POI Methods in `I. Informativeness`

1. **Implicit vs. explicit spatial prefix in SIDs**: OneLoc injects location context into the MLLM embedding before `R-KM` (`Text+Img+Geo†`), so spatial hierarchy is not guaranteed to align with individual code positions. Within the same cell (`I. Informativeness` $\times$ `Representation`), **`LGSID`** (`Geo-Idx+RQ`) and **`GeoGR`** (`R-KM+EM`) explicitly couple spatial/grid structure or EM-updated geographic alignment with collaborative signals (`Text+Geo+CF`), while **`LGRID`** (`DSRQ`) disentangles semantic and geographic latent spaces.
2. **Closed industrial evaluation**: Evaluation relies on proprietary short-video local-life logs and business GMV estimators without a public reproducibility benchmark.

## Peer Methods in `I. Informativeness` × `Representation` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [Molar](molar.md) | arXiv’24 | `Text+Img+CF` | `–` | `Dec-Only` | `–` | `Discrim.` | `Scoring` |
| [Q-BERT4Rec](q-bert4rec.md) | arXiv’25 | `Text+Img+CF` | `RQ-VAE` | `Encoder (Non-AR)` | `Fixed` | `Masked` | `Non-AR` |
| [UNGER](unger.md) | TOIS’25 | `Text+CF` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP + Ctr.` | `Beam` |
| [GeoGR](geogr.md) | arXiv’26 | `Text+Geo+CF` | `R-KM+EM` | `Dec-Only` | `Altern.†` | `Multi-task NTP` | `Beam` |
| [HF-SID](hf-sid.md) | arXiv’26 | `Text+Attr+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [LGRID](lgrid.md) | arXiv’26 | `Text+Geo` | `DSRQ` | `Disc.` | `Fixed` | `Discrim.` | `Scoring` |
| [LGSID](lgsid.md) | AAAI’26 | `Text+Geo+CF` | `Geo-Idx+RQ` | `Disc. / Enc-Dec` | `Fixed` | `Discrim. / NTP` | `Scoring / Beam†` |
| [ReSID](resid.md) | arXiv’26 | `Attr+CF` | `GAOQ` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [SCRec](screc.md) | RecSys’26 | `Text+CF` | `RQ-VAE` | `Non-AR / Enc-Dec` | `Fixed` | `MTP + Ctr.` | `Scoring / Beam†` |
| [SPAR](spar.md) | arXiv’26 | `Text+Geo` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `–` |
| [TriAlignGR](trialigngr.md) | arXiv’26 | `Text+Img` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
