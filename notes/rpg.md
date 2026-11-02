## At a Glance

Key Findings: With 64-token IDs, RPG outperforms generative baselines by an average of 12.6% on NDCG@10 and also improves inference efficiency (Abstract).
Limitation: The authors assume that the tokens of an SID are conditionally independent given the input sequence, and the decoding graph must be rebuilt when the model is retrained or items are re-tokenized (Sec. 2.2.1, Sec. 2.3.1).

### 1. Why This Paper Matters

Generative recommenders such as TIGER decode a Semantic ID (SID) token by token with beam search, which needs several forward passes of the generator per recommendation. As a result, existing models keep SIDs short, often 4 tokens (Abstract). RPG instead predicts every token of a long, unordered SID in one forward pass and searches a graph of valid SIDs at inference. ACERec and SPRINT, later papers in the same matrix cell, use the same `Par. OPQ` tokenization and `Non-AR` backbone.

> "Running beam search for 32 steps would be computationally prohibitive." (Sec. 1)

### 2. How It Works

#### Overview

```
Item features → semantic encoder → item embedding
  │
  ▼  OPQ: one codebook per subvector
Unordered SID (c1, ..., cm), m up to 64
  │
  ▼  token embeddings pooled per item; Transformer decoder over the history
Sequence representation s
  │
  ▼  m MLP heads, one softmax per codebook (MTP loss in training)
Cached token log-probabilities p(1), ..., p(m)
  │
  ▼  graph-constrained decoding: sample b items, add graph neighbors, keep the best b, repeat q times
Top-K items
```

#### Step 1: Long SIDs from OPQ

RPG replaces residual quantization with optimized product quantization (OPQ), so that the tokens can be predicted in parallel rather than one after another (Sec. 2.1.1).

> "To align with parallel decoding, we tokenize each item into an unordered long semantic ID (up to 64 tokens per item) using optimized product quantization (Jégou et al., 2011; Ge et al., 2014)." (Sec. 1)

OPQ splits the item's semantic embedding into $`m`$ subvectors and quantizes each subvector with its own codebook of size $`M`$ (Sec. 2.1.1). The paper cites OPQ and does not restate its rotation or codebook training. The standard product-quantization assignment is:

```math
\mathbf{x}_i = \left[\mathbf{x}_i^{(1)}; \dots; \mathbf{x}_i^{(m)}\right], \qquad c_{i,j} = \arg\min_{c \in \mathcal{C}^{(j)}} \left\| \mathbf{x}_i^{(j)} - \mathbf{a}_c^{(j)} \right\|_2^2
```

where:
- $`\mathbf{x}_i`$ is the semantic embedding of item $`i`$ after the OPQ rotation;
- $`\mathbf{x}_i^{(j)}`$ is its $`j`$-th subvector;
- $`\mathcal{C}^{(j)}`$ is the $`j`$-th codebook with $`M`$ codewords $`\mathbf{a}_c^{(j)}`$;
- $`c_{i,j}`$ is the $`j`$-th token of the SID of item $`i`$.

"Unordered" means that no token is predicted from the tokens before it. Position $`j`$ still belongs to codebook $`j`$ (Sec. 2.1.1). Different items can share the same token set. Each item keeps its own node in the decoding graph, and the authors describe such collisions as very unlikely with 64-token IDs (Appendix C).

#### Step 2: Item-Level Input

A 64-token SID per history item would make the input sequence too long (Sec. 2.1.2). RPG gives each codebook a learnable token embedding table $`\mathbf{E}_j \in \mathbb{R}^{M \times d}`$ and pools the $`m`$ token embeddings of an item into one vector $`\mathbf{v}_i = \mathrm{Aggr}(\mathbf{e}_{1,c_{i,1}}, \dots, \mathbf{e}_{m,c_{i,m}})`$ with mean or max pooling (Sec. 2.1.2). A Transformer decoder reads the sequence $`\mathbf{v}_1, \dots, \mathbf{v}_{t-1}`$ and outputs a sequence representation $`\mathbf{s} \in \mathbb{R}^{d}`$ (Sec. 2.2.1).

#### Step 3: Parallel Prediction with the MTP Loss

RPG predicts each token of the next SID with its own head and trains all heads with a multi-token prediction (MTP) loss.

> "Since each token produced by OPQ encodes a separate subvector of the target item's semantic representation, we assume that tokens in the tuple are conditionally independent given the input sequence s." (Sec. 2.2.1)

```math
\mathcal{L} = -\sum_{j=1}^{m} \log \mathbb{P}^{(j)}(c_{t,j} \mid s) = -\sum_{j=1}^{m} \log \frac{\exp\left(\mathbf{e}_{c_{t,j}}^{\top} g_j(\mathbf{s}) / \tau\right)}{\sum_{c \in \mathcal{C}^{(j)}} \exp\left(\mathbf{e}_{c}^{\top} g_j(\mathbf{s}) / \tau\right)}
```

where:
- $`c_{t,j}`$ is the $`j`$-th token of the target item's SID;
- $`g_j`$ is an MLP projection head for codebook $`j`$;
- $`\mathbf{e}_c`$ is the token embedding of token $`c`$;
- $`\tau`$ is a temperature (Eq. 1).

#### Step 4: Cached Token Scores

For one input sequence, RPG computes each codebook's token distribution once and caches it (Eq. 2). The score of any candidate SID is then a sum of cached values (Eq. 3):

```math
\mathbf{p}^{(j)} = \mathrm{softmax}\left(\mathbf{E}_j\, g_j(\mathbf{s}) / \tau\right) \in \mathbb{R}^{M}, \qquad \mathrm{score}(c_1, \dots, c_m) = \sum_{j=1}^{m} \log p^{(j)}_{c_j}
```

where $`p^{(j)}_{c_j}`$ is the entry of $`\mathbf{p}^{(j)}`$ for token $`c_j`$ (Sec. 2.2.2).

#### Step 5: Graph-Constrained Decoding

After training, RPG builds a graph whose nodes are the SIDs of catalog items (Sec. 2.3.1). The similarity of two SIDs is the sum of the inner products of their token embeddings:

```math
\mathrm{sim}(i, i') = \sum_{j=1}^{m} \mathbf{e}_{j,c_{i,j}}^{\top}\, \mathbf{e}_{j,c_{i',j}}
```

Each node keeps its $`k`$ most similar neighbors and an edge to itself. The graph is reused until the model is retrained or the items are re-tokenized (Sec. 2.3.1). Decoding then runs four steps (Sec. 2.3.2):

1. Sample $`b`$ SIDs from the catalog as the initial beam.
2. Add all $`b \times k`$ graph neighbors of the beam to a candidate set.
3. Score the candidates with the cached values and keep the best $`b`$.
4. Repeat steps 2 and 3 for $`q`$ iterations and return the final beam as the top-$`K`$ items.

> "Since neighboring nodes in the graph tend to have similar logits, we expand the beam by propagating through the graph, including all b×k neighbors of the current beam into a temporary set." (Sec. 2.3.2)

```python
import torch

def rpg_decode(s, heads, token_emb, item_codes, neighbors, b=10, q=2, tau=0.05):
    """
    s:          [d] sequence representation of one user
    heads:      list of m projection heads g_j, each mapping [d] -> [d]
    token_emb:  [m, M, d] token embedding tables E_j
    item_codes: [N, m] SID of every catalog item; entry j indexes codebook j
    neighbors:  [N, k] graph neighbors of every item, including the item itself
    """
    m = item_codes.size(1)
    # Eq. 2: one softmax per codebook, cached for this user
    proj = torch.stack([g(s) for g in heads])                                         # [m, d]
    log_p = torch.log_softmax(torch.einsum("jcd,jd->jc", token_emb, proj) / tau, -1)  # [m, M]
    # Eq. 3 for the whole catalog; the paper scores only the visited nodes (Sec. 2.3)
    scores = log_p[torch.arange(m), item_codes].sum(dim=-1)                          # [N]
    # step 1: random initial beam of b valid SIDs
    beam = torch.randperm(item_codes.size(0))[:b]                                     # [b]
    for _ in range(q):
        # step 2: beam plus graph neighbors, without duplicates
        cand = torch.unique(neighbors[beam].reshape(-1))                              # [<= b*k]
        # step 3: keep the b best candidates
        beam = cand[torch.topk(scores[cand], k=min(b, cand.numel())).indices]
    return beam                                                                       # item indices
```

Simplifications: The code scores every item in the catalog (`scores` covers the whole catalog) before the graph search. It therefore does not implement the Sec. 2.3 path that starts from a few sampled seeds and scores only the items reached along graph edges, and it does not reproduce the paper's inference efficiency. It also takes the heads, token embeddings, and graph as inputs, and omits OPQ, the Transformer decoder, MTP training, and graph construction.

> "Compared to generative models like TIGER (Rajput et al., 2023), RPG reduces the number of sequence encoder forward passes per input instance from approximately O(bm) to just O(1), greatly improving inference efficiency (Section 3.3)." (Sec. 2.4.2)

### 3. Experimental Findings

- Overall: with 64-token IDs, RPG outperforms the generative baselines by an average of 12.6% on NDCG@10 (Abstract). Table 2 gives the full comparison (Table 2).
- Efficiency: on Sports, RPG uses less runtime memory and less inference time than TIGER (Sec. 3.3, Fig. 3).

  > "Moreover, RPG reduces runtime memory consumption by nearly 25× and achieves an inference speedup of almost 15× compared to TIGER." (Sec. 3.3)

- ID length: performance does not rise with every increase in length. The best lengths are 16 on Sports, 32 on Beauty, 16 on Toys, and 64 on CDs (Sec. 3.5.1, Fig. 4).

  > "From Figure 4, we observe that, in general, longer OPQ-based semantic IDs lead to better performance. However, for smaller datasets, they may converge earlier." (Sec. 3.5.1)

- Semantic encoder: the main runs use OpenAI text-embedding-3-large, and Table 4 repeats the comparison with sentence-t5-base for parity with benchmark results (Sec. 3.1, Sec. 3.5.2).
- Long-tail items: on Sports, the authors report that RPG achieves the best overall performance across the training-frequency groups (Sec. 3.5.3, Fig. 5).

### 4. Limitations & Critical Analysis

**Stated by the authors.** The parallel heads rest on an assumption: the tokens of an SID are conditionally independent given the input sequence (Sec. 2.2.1). The authors state that different items can share the same token set (Appendix C). They also state that the efficiency study uses one fixed set of hyperparameters, and that its runtime memory covers the GPU memory for computing logits, not the storage of model parameters (Sec. 3.3).

**Our analysis.**

- The score of an SID is a sum of per-token scores (Eq. 3), so the model cannot express dependencies between tokens of one SID. In the same cell, ACERec adds contrastive and auxiliary objectives (`MTP + Ctr. + Aux.`), and SPRINT replaces the objective with `Dual-level Flow Ctr.`; both keep `Par. OPQ` and `Non-AR`.
- The decoding graph is an index outside the model. It has one node per catalog item and must be rebuilt after retraining or re-tokenization (Sec. 2.3.1).
- The evaluation covers four Amazon datasets. The paper reports no online or industrial test.
