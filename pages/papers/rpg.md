# RPG: Generating long semantic ids in parallel for recommendation

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2506.05781`)](https://arxiv.org/abs/2506.05781) · [Source Record (`data/papers/rpg.yaml`)](../../data/papers/rpg.yaml)

> **Summary**: Abstract: "they often suffer from inefficient inference due to the reliance on resource-intensive beam search".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Hou et al. (2025) | Published / posted in `KDD’25` |
| **Problem Band** | `V. Efficiency` | Can it be trained and served within latency and cost budgets? |
| **Primary Stage** | `Backbone` | The primary design change sits in the Generative Backbone stage. |
| **Representation** | `Text+Img` |  |
| **Tokenization** | `Par. OPQ` |  |
| **Backbone** | `Non-AR` | Non-autoregressive. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `MTP` | Predicts several codes in parallel at once. |
| **Inference Decoding** | `Graph` |  |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | Not reported | Official or public implementation link |

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "they often suffer from inefficient inference due to the reliance on resource-intensive beam search".

## Positioning in the Problem × Stage Matrix

- **Matrix Cell**: **V. Efficiency** $\times$ **Backbone** (`problem: V`, `stage: Backbone`).
- **Why Here**: Longer Semantic IDs ($M \in \{16, 32, 64\}$ sub-tokens) eliminate collisions and capture fine-grained item semantics, but autoregressive decoding over $M$ steps incurs prohibitive latency and cascading prefix errors. RPG replaces sequential token-by-token generation with a **non-autoregressive (`Non-AR`) parallel multi-token prediction (`MTP`) backbone** coupled with **Optimized Product Quantization (`Par. OPQ`)** and **graph-guided decoding (`Graph`)**.

```
Dense Item Embedding x_i ∈ ℝ^d
  │
  ▼  [1. Tokenization: Par. OPQ (orthogonal rotation R + M parallel subspace codebooks)]
Unordered Long Semantic ID c_i = (c_{i,1}, ..., c_{i,M})   (M up to 64)
  │
  ▼  [2. Backbone & 3. Training: Non-AR Transformer + M parallel heads trained with MTP]
Independent per-subspace logits { P_θ^(m)(c_m | h_u) }_{m=1}^M in a single forward pass
  │
  ▼  [4. Inference: Graph-constrained iterative propagation over item similarity graph G]
Top-K valid long-SID items
```

---

## Core Mechanism & Annotated Walkthrough

### Step 1: Parallel Subspace Tokenization via `Par. OPQ`

Whereas `RQ-VAE` quantizes residuals sequentially (creating strict order dependencies $c_1 \rightarrow c_2 \rightarrow \dots \rightarrow c_M$), RPG learns an orthogonal rotation matrix $\mathbf{R} \in \mathbb{R}^{d \times d}$ ($\mathbf{R}^\top \mathbf{R} = \mathbf{I}$) that decomposes the item representation $\mathbf{x}_i \in \mathbb{R}^d$ into $M$ orthogonal subspaces of dimension $d/M$:

$$\tilde{\mathbf{x}}_i = \mathbf{R}\mathbf{x}_i = \left[\tilde{\mathbf{x}}_i^{(1)} \,\|\, \tilde{\mathbf{x}}_i^{(2)} \,\|\, \dots \,\|\, \tilde{\mathbf{x}}_i^{(M)}\right], \qquad c_{i,m} = \arg\min_{k \in \{1,\dots,K\}} \left\| \tilde{\mathbf{x}}_i^{(m)} - \mathbf{e}_k^{(m)} \right\|_2^2$$

where:
- $\tilde{\mathbf{x}}_i^{(m)} \in \mathbb{R}^{d/M}$ is the $m$-th subspace projection of item $i$;
- $\mathcal{C}^{(m)} = \{\mathbf{e}_k^{(m)}\}_{k=1}^{K}$ is the $m$-th subspace codebook;
- $c_{i,m} \in \{1, \dots, K\}$ is the $m$-th token of item $i$'s unordered Semantic ID tuple $\mathbf{c}_i = (c_{i,1}, \dots, c_{i,M})$.

### Step 2: Non-Autoregressive Multi-Token Prediction (`Non-AR` + `MTP`)

Given the user interaction sequence $S_u = (i_1, \dots, i_{t-1})$, RPG aggregates each history item's $M$ sub-token embeddings into a single item-level vector so the sequence length fed into the Transformer backbone remains $t-1$ rather than $M(t-1)$. From the final hidden state $\mathbf{h}_u \in \mathbb{R}^d$, $M$ parallel projection heads $\mathbf{W}^{(1)}, \dots, \mathbf{W}^{(M)}$ predict all $M$ target code positions in a single forward pass:

$$P_\theta^{(m)}(c_{t,m} = k \mid S_u) = \frac{\exp\!\left(\mathbf{e}_k^{(m)\top} \mathbf{W}^{(m)} \mathbf{h}_u / \tau\right)}{\sum_{k'=1}^{K} \exp\!\left(\mathbf{e}_{k'}^{(m)\top} \mathbf{W}^{(m)} \mathbf{h}_u / \tau\right)}, \qquad \mathcal{L}_{\text{MTP}} = -\frac{1}{M}\sum_{m=1}^{M} \log P_\theta^{(m)}(c_{t,m} \mid S_u)$$

where $\tau > 0$ is a temperature hyperparameter.

```python
# Annotated PyTorch walkthrough of RPG's Non-AR MTP forward + Graph propagation decoding
# Reference: Hou et al. (KDD 2025), §2.2-2.3
def rpg_mtp_and_graph_decode(h_u, heads, codebooks, item_codes, adj_neighbors, tau=0.07, steps=2, beam_size=50):
    """
    h_u:           [B, d] user sequence representation from Transformer encoder
    heads:         M linear projections, stacked as [M, d, d_sub]
    codebooks:     [M, K, d_sub] OPQ subspace codebooks
    item_codes:    [N_items, M] precomputed long OPQ SIDs for all catalog items
    adj_neighbors: [N_items, deg] k-NN graph built over quantized item representations
    """
    # 1. Single-pass parallel multi-token log-probabilities across all M subspaces
    proj = torch.einsum("bd,mde->bme", h_u, heads)                 # [B, M, d_sub]
    logits = torch.einsum("bme,mke->bmk", proj, codebooks) / tau   # [B, M, K]
    log_probs = logits.log_softmax(dim=-1)                         # [B, M, K]

    # 2. Score initial seed items & propagate on the SID similarity graph G
    # Gather per-item log-likelihoods sum_{m=1}^M log P^(m)(c_{i,m} | h_u)
    seed_scores = log_probs[:, torch.arange( item_codes.size(1) ), item_codes].sum(dim=-1)  # [B, N_items]
    _, frontier = torch.topk(seed_scores, k=beam_size, dim=-1)                              # [B, beam_size]

    for _ in range(steps):
        # Expand frontier along graph edges and retain top-scoring valid items
        expanded = adj_neighbors[frontier].reshape(h_u.size(0), -1)
        candidates = torch.cat([frontier, expanded], dim=-1)
        cand_scores = seed_scores.gather(1, candidates)
        _, top_idx = torch.topk(cand_scores, k=beam_size, dim=-1)
        frontier = candidates.gather(1, top_idx)

    return frontier
```

### Step 3: Graph-Guided Decoding (`Graph`)

Because the $M$ heads predict marginal distributions independently, naively picking $\arg\max_k P_\theta^{(m)}(k \mid S_u)$ for each $m$ rarely lands on a valid catalog item when $K^M \gg |\mathcal{I}|$, while scoring all $|\mathcal{I}|$ items scales linearly with catalog size. RPG constructs a sparse $k$-NN graph $\mathcal{G} = (\mathcal{I}, \mathcal{E})$ over the catalog items based on their quantized OPQ representations, scores a small seed set using $\sum_{m=1}^{M} \log P_\theta^{(m)}(c_{i,m} \mid S_u)$, and iteratively expands neighbors on $\mathcal{G}$ to retrieve the highest-scoring valid items in sub-linear time.

---

## Verbatim Quotes from the Paper

- **Motivation for parallel long SIDs** (§1, p.1): *"We propose a paradigm that generates long Semantic IDs in parallel for recommendation (RPG)."*
- **Order-agnostic subspace tokenization** (§2.1, p.3): *"Instead of residual quantization that enforces a coarse-to-fine sequential dependency, we adopt product quantization over orthogonal subspaces so that tokens at different positions can be predicted in parallel."*
- **Graph-guided decoding** (§2.3, p.4): *"During inference, we leverage a semantic similarity graph over item IDs to iteratively propagate and refine candidate IDs using the parallelly predicted token distributions."*

---

## Experimental Protocol & Key Results

- **Datasets & Split**: Amazon Reviews (`Beauty`, `Sports and Outdoors`, `Toys and Games`, `CDs and Vinyl`), 5-core leave-one-out split.
- **Reported Findings** (§3, Tables 1–3 of the paper):
  - **Scaling SID length $M$**: Increasing $M$ from $4$ to $16$–$64$ in RPG consistently improves Recall@10 and NDCG@10 while eliminating SID collisions without needing an arbitrary trailing collision token.
  - **Inference Speedup**: Because all $M$ positions are predicted in one forward pass followed by lightweight graph propagation, RPG reduces decoding latency and GPU memory by an order of magnitude compared to autoregressive beam search over long SIDs.

---

## Limitations & Comparison with Peer Methods in `V. Efficiency`

1. **Marginal factorizability vs. intra-code dependencies**: Independent subspace heads assume conditional independence across the $M$ sub-tokens given $\mathbf{h}_u$. Within the same cell (`V. Efficiency` $\times$ `Backbone`), **`ACERec`** adds contrastive and auxiliary alignment regularizers to `Par. OPQ` + `Non-AR`, while **`SPRINT`** replaces independent token cross-entropy with a dual-level flow contrastive objective (`Dual-level Flow Ctr.`) that jointly optimizes token-product scores and whole-SID similarity.
2. **Graph maintenance overhead**: Maintaining the item similarity graph $\mathcal{G}$ adds an index structure alongside the generator parameters, whereas **`SID-MLP`** (`Enc-MLP`) and **`OneRec-V2`** (`Lazy Dec-Only`) accelerate autoregressive decoding without an external graph.

## Peer Methods in `V. Efficiency` × `Backbone` (10 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [ACERec](acerec.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `MTP + Ctr. + Aux.` | `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` | `R-KM` | `Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP → (NTP + Aux.)` | `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec` | `–` | `NTP / NTP + Aux.` | `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP` | `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `–` | `NTP → (NTP + DPO)` | `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` | `RQ-VAE†` | `Enc-MLP` | `Fixed` | `NTP + Aux.` | `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` | `Par. OPQ` | `Non-AR` | `Fixed` | `Dual-level Flow Ctr.` | `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` | `RQ-VAE` | `Enc-Dec / Dec-Only` | `Fixed` | `NTP + Aux.` | `C-Beam` |
