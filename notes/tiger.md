## Positioning in the Problem × Stage Matrix

- **Matrix Cell**: **Paradigms, Systems and Benchmarks** (`problem: psb`, `stage: n/a`).
- **Why Here**: TIGER defines the canonical five-stage pipeline for Semantic ID-based generative recommendation rather than patching a single failure mode. Subsequent methods in bands `I`–`VI` modify one or more of TIGER's five stages (`Text` representation $\rightarrow$ `RQ-VAE` tokenization $\rightarrow$ `Enc-Dec` backbone $\rightarrow$ `Fixed` / `NTP` training $\rightarrow$ `Beam` inference).

```
Item Text (title, brand, price, category)
  │
  ▼  [1. Representation: frozen Sentence-T5]
Dense content embedding x ∈ ℝ^d (d = 768)
  │
  ▼  [2. Tokenization: 3-level RQ-VAE + collision suffix c_4]
Discrete Semantic ID c_i = (c_{i,1}, c_{i,2}, c_{i,3}, c_{i,4}) ∈ {0..255}^3 × {0..N_coll}
  │
  ▼  [3. Backbone & 4. Training: T5 Encoder-Decoder with Fixed SIDs & NTP]
Autoregressive sequence model P_θ(c_{t,m} | c_{<t}, c_{t,<m})
  │
  ▼  [5. Inference: autoregressive Beam Search + lookup table]
Top-K recommended items
```

---

## Core Mechanism & Annotated Walkthrough

### Step 1: Content Encoding and Residual Vector Quantization (`RQ-VAE`)

For each item $i$, its textual metadata (title, brand, price, and category) is encoded by a frozen pre-trained Sentence-T5 encoder into a dense vector $\mathbf{x} \in \mathbb{R}^{768}$, which an MLP encoder $E(\cdot)$ projects to a latent vector $\mathbf{z} := E(\mathbf{x}) \in \mathbb{R}^{d_z}$ ($d_z = 32$).

At quantization depth $m \in \{1, \dots, M\}$ ($M = 3$) with level-specific codebook $\mathcal{C}^{(m)} = \{\mathbf{e}_k^{(m)}\}_{k=1}^{K}$ ($K = 256$), RQ-VAE quantizes the residual $\mathbf{r}_m$ greedily from coarse to fine:

$$\mathbf{r}_1 = \mathbf{z}, \qquad c_m = \arg\min_{k \in \{1,\dots,K\}} \left\| \mathbf{r}_m - \mathbf{e}_k^{(m)} \right\|_2^2, \qquad \mathbf{r}_{m+1} = \mathbf{r}_m - \mathbf{e}_{c_m}^{(m)}$$

where:
- $\mathbf{r}_m \in \mathbb{R}^{d_z}$ is the residual vector entering level $m$;
- $c_m \in \{0, \dots, K-1\}$ is the discrete codeword index at depth $m$;
- $\mathbf{e}_{c_m}^{(m)} \in \mathbb{R}^{d_z}$ is the selected centroid at level $m$.

```python
# Annotated PyTorch walkthrough of TIGER's RQ-VAE residual loop
# Reference: Rajput et al. (NeurIPS 2023), §3.1 Eq. (1)-(3)
def rqvae_quantize(z, codebooks, beta=0.25):
    """
    z:         [B, d_z] latent vectors from MLP encoder E(x)
    codebooks: list of M parameters, each [K, d_z] (M=3, K=256)
    """
    r = z
    z_hat = torch.zeros_like(z)
    codes = []
    vq_loss = 0.0

    for m, E_m in enumerate(codebooks):
        # 1. Nearest centroid lookup in level-m codebook
        dists = torch.cdist(r, E_m, p=2.0) ** 2          # [B, K]
        c_m = torch.argmin(dists, dim=-1)                # [B]
        e_m = E_m[c_m]                                   # [B, d_z]

        # 2. Codebook + commitment loss (straight-through estimator)
        vq_loss = vq_loss + (e_m - r.detach()).pow(2).mean() + beta * (r - e_m.detach()).pow(2).mean()
        e_m_st = r + (e_m - r).detach()

        # 3. Accumulate quantized representation and update residual
        z_hat = z_hat + e_m_st
        r = r - e_m.detach()
        codes.append(c_m)

    return torch.stack(codes, dim=-1), z_hat, vq_loss
```

### Step 2: Training Objective of the Tokenizer

The quantized vector $\hat{\mathbf{z}} = \sum_{m=1}^{M} \mathbf{e}_{c_m}^{(m)}$ is passed through an MLP decoder $D(\cdot)$ to reconstruct $\hat{\mathbf{x}} = D(\hat{\mathbf{z}})$. The total RQ-VAE loss is:

$$\mathcal{L}_{\text{RQ-VAE}}(\mathbf{x}) = \|\mathbf{x} - \hat{\mathbf{x}}\|_2^2 + \sum_{m=1}^{M} \left( \left\|\operatorname{sg}[\mathbf{r}_m] - \mathbf{e}_{c_m}^{(m)}\right\|_2^2 + \beta \left\|\mathbf{r}_m - \operatorname{sg}[\mathbf{e}_{c_m}^{(m)}]\right\|_2^2 \right)$$

where $\operatorname{sg}[\cdot]$ is the stop-gradient operator and $\beta = 0.25$ balances commitment to the chosen centroids. To prevent codebook collapse on the first batch, TIGER initializes $\mathcal{C}^{(m)}$ via $k$-means on the residuals $\mathbf{r}_m$.

### Step 3: Collision Resolution Suffix and Sequence-to-Sequence NTP

If $N_{\text{coll}}$ items share the same 3-tuple $(c_1, c_2, c_3)$, TIGER appends a fourth disambiguating token $c_4 \in \{0, 1, \dots, N_{\text{coll}}-1\}$ assigned in arbitrary order:

```python
# Collision resolution via trailing integer token c_4 (§3.1, p.4)
from collections import defaultdict

def append_collision_suffix(raw_tuples):
    bucket_counts = defaultdict(int)
    semantic_ids = []
    for tup in raw_tuples:
        c4 = bucket_counts[tup]
        bucket_counts[tup] += 1
        semantic_ids.append((*tup, c4))
    return semantic_ids
```

Given a user interaction history $(i_1, \dots, i_{t-1})$ flattened into a sequence of Semantic ID tokens (prepended with a hashed user token), a T5-style Encoder-Decoder maximizes the token-level next-token prediction (`NTP`) log-likelihood over the target item's 4-token code $\mathbf{c}_t = (c_{t,1}, c_{t,2}, c_{t,3}, c_{t,4})$:

$$\mathcal{L}_{\text{NTP}} = -\sum_{m=1}^{4} \log P_\theta\!\left(c_{t,m} \;\middle|\; \mathbf{c}_{1:t-1},\, c_{t,1:m-1}\right)$$

---

## Verbatim Quotes from the Paper

- **Generative retrieval paradigm** (§1, p.1): *"We propose a new paradigm, generative retrieval, where a recommender model autoregressively decodes the identifiers of the target candidates."*
- **Residual quantization for Semantic IDs** (§3.1, p.3): *"RQ-VAE is a multi-level vector quantizer that applies quantization on residuals to generate a tuple of codewords (i.e., Semantic IDs)."*
- **Suffix-based collision handling** (§3.1, p.4): *"To handle collisions, we append an extra token at the end of the codewords to make them unique."*

---

## Experimental Protocol & Key Results

- **Datasets & Split**: Amazon Product Reviews (`Beauty`, `Sports and Outdoors`, `Toys and Games`), 5-core filtering, standard leave-one-out split (last item for test, second-to-last for validation).
- **Reported Metrics** (Table 1 of the paper, 4-layer T5 encoder + 4-layer T5 decoder, $M=3, K=256$):
  - **Beauty**: Recall@5 = `0.0454`, NDCG@5 = `0.0321`, Recall@10 = `0.0648`, NDCG@10 = `0.0384` (vs. SASRec Recall@5 = `0.0387`, NDCG@5 = `0.0249`).
  - **Sports and Outdoors**: Recall@5 = `0.0264`, NDCG@5 = `0.0181`, Recall@10 = `0.0400`, NDCG@10 = `0.0225` (vs. SASRec Recall@5 = `0.0233`, NDCG@5 = `0.0154`).
  - **Toys and Games**: Recall@5 = `0.0521`, NDCG@5 = `0.0371`, Recall@10 = `0.0712`, NDCG@10 = `0.0432` (vs. SASRec Recall@5 = `0.0463`, NDCG@5 = `0.0306`).
- **Tokenization Ablation** (Table 2 of the paper): `RQ-VAE` SIDs consistently outperform `Random ID` and `LSH` IDs across all three Amazon subsets.

---

## Limitations & Follow-up Work in the Matrix

1. **Content-only representation (`I. Informativeness`)**: Frozen Sentence-T5 embeddings ignore collaborative co-occurrence; addressed by `LETTER`, `CoST`, `EAGER-LLM`, and `UNGER`.
2. **Non-semantic collision suffix and invalid beams (`II. Uniqueness and Validity`)**: The trailing integer $c_4$ introduces an arbitrary suffix token and unconstrained beam search can emit unassigned 4-tuples; addressed by Sinkhorn/uniformity regularizers (`LETTER`, `MME-SID`) and prefix-tree constrained decoding (`C-Beam`).
3. **Two-stage objective mismatch (`III. SID–Model Alignment`)**: The tokenizer is frozen (`Fixed`) before generator training; addressed by alternating or joint optimization (`ETEGRec`, `Align3GR`).
4. **Sequential beam cost on long codes (`V. Efficiency`)**: Autoregressive decoding scales linearly with code length $M$ and beam width $B$; addressed by parallel multi-token prediction (`RPG`, `ACERec`, `SPRINT`) and speculative decoding (`AtSpeed`, `NEZHA`).
