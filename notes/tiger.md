## At a Glance

Key Findings: On Amazon Beauty, TIGER reports Recall@5 of 0.0454 against 0.0387 for SASRec, and RQ-VAE Semantic IDs outperform LSH and random IDs (Tables 1 and 2).
Limitation: The authors state that beam search can make TIGER more expensive than ANN-based retrieval at inference, and the paper does not report a beam width or latency (Appendix E).

### 1. Why This Paper Matters

Large-scale recommenders usually embed users and items in one space and select candidates by approximate nearest neighbor (ANN) search (Abstract). TIGER instead trains a sequence-to-sequence model to decode the Semantic ID (SID) of the next item. The authors describe it as the first Semantic ID-based generative model for recommendation (Abstract). Many later papers in this list keep this pipeline and change one of its stages.

> "We propose a new paradigm of building generative retrieval models for sequential recommendation." (Sec. 1)

### 2. How It Works

#### Overview

```
Item text (title, price, brand, category)
  │
  ▼  pre-trained Sentence-T5
Content embedding x (768 dimensions)
  │
  ▼  DNN encoder, 3-level RQ-VAE, collision token
SID (c1, c2, c3, c4): three codes from 256-entry codebooks plus one collision token
  │
  ▼  Transformer encoder-decoder (T5X), next-token prediction
Next-item SID, decoded by beam search
  │
  ▼  frozen lookup table
Recommended items
```

#### Step 1: Item Text to a Latent Vector

TIGER builds a sentence from each item's title, price, brand, and category, and the pre-trained Sentence-T5 model encodes it into a 768-dimensional embedding $`\mathbf{x}`$ (Sec. 4). A DNN encoder $`E`$ with intermediate layers of size 512, 256, and 128 and ReLU activations maps $`\mathbf{x}`$ to a 32-dimensional latent vector $`\mathbf{z} = E(\mathbf{x})`$ (Sec. 4).

#### Step 2: Residual Quantization into Codes

RQ-VAE quantizes the residual left by the previous level, so each level refines the code of the level before it.

> "Residual-Quantized Variational AutoEncoder (RQ-VAE) [40] is a multi-level vector quantizer that applies quantization on residuals to generate a tuple of codewords (aka Semantic IDs)." (Sec. 3.1)

TIGER uses $`M = 3`$ levels, each with a codebook of $`K = 256`$ codewords of dimension 32 (Sec. 4). At level $`m`$:

```math
\mathbf{r}_1 = \mathbf{z}, \qquad c_m = \arg\min_{k \in \{0, \dots, K-1\}} \left\| \mathbf{r}_m - \mathbf{e}_k^{(m)} \right\|_2^2, \qquad \mathbf{r}_{m+1} = \mathbf{r}_m - \mathbf{e}_{c_m}^{(m)}
```

where:
- $`\mathbf{r}_m \in \mathbb{R}^{32}`$ is the residual that enters level $`m`$;
- $`\mathbf{e}_k^{(m)}`$ is codeword $`k`$ of the level-$`m`$ codebook;
- $`c_m`$ is the code chosen at level $`m`$.

```python
import torch

def rqvae_quantize(z, codebooks, beta=0.25):
    """
    z:         [B, 32] latent vectors from the encoder E(x)
    codebooks: list of M tensors, each [K, 32] (M = 3, K = 256)
    """
    r = z
    z_hat = torch.zeros_like(z)
    codes, vq_loss = [], 0.0
    for E_m in codebooks:
        # nearest codeword at this level
        c_m = torch.cdist(r, E_m).pow(2).argmin(dim=-1)                     # [B]
        e_m = E_m[c_m]                                                       # [B, 32]
        # codebook and commitment terms of the quantization loss
        vq_loss = vq_loss + (e_m - r.detach()).pow(2).mean() + beta * (r - e_m.detach()).pow(2).mean()
        # straight-through estimate, then the residual for the next level
        z_hat = z_hat + r + (e_m - r).detach()
        r = r - e_m.detach()
        codes.append(c_m)
    return torch.stack(codes, dim=-1), z_hat, vq_loss                        # [B, M], [B, 32], scalar
```

Simplifications: The code shows only the quantization loop and the quantization loss. It omits the DNN encoder and decoder, the reconstruction loss, and the k-means codebook initialization.

#### Step 3: Tokenizer Training

A decoder $`D`$ reconstructs $`\hat{\mathbf{x}} = D(\hat{\mathbf{z}})`$ from the sum of the selected codewords $`\hat{\mathbf{z}} = \sum_{m=1}^{M} \mathbf{e}_{c_m}^{(m)}`$. RQ-VAE trains the encoder, decoder, and codebooks with a reconstruction loss and a quantization loss:

```math
\mathcal{L}(\mathbf{x}) = \|\mathbf{x} - \hat{\mathbf{x}}\|_2^2 + \sum_{m=1}^{M} \left( \left\|\mathrm{sg}[\mathbf{r}_m] - \mathbf{e}_{c_m}^{(m)}\right\|_2^2 + \beta \left\|\mathbf{r}_m - \mathrm{sg}[\mathbf{e}_{c_m}^{(m)}]\right\|_2^2 \right)
```

where:
- $`\mathrm{sg}[\cdot]`$ is the stop-gradient operator;
- $`\beta = 0.25`$ weights the commitment term (Sec. 4).

To prevent codebook collapse, TIGER runs k-means on the first training batch and uses the centroids to initialize the codebooks (Sec. 3.1).

#### Step 4: Collision Token

Several items can receive the same three codes. TIGER appends a fourth token so that every item has a unique SID: two items that share (12, 24, 52) become (12, 24, 52, 0) and (12, 24, 52, 1) (Sec. 3.1).

> "To remove the collisions, we append an extra token at the end of the ordered semantic codes to make them unique." (Sec. 3.1)

```python
from collections import defaultdict

def append_collision_token(code_tuples):
    """code_tuples: list of (c1, c2, c3), one per item."""
    seen = defaultdict(int)
    sids = []
    for t in code_tuples:
        sids.append((*t, seen[t]))   # 0 for the first item with this tuple, 1 for the second, ...
        seen[t] += 1
    return sids
```

The code assigns the fourth token in input order; the paper does not state how the order is chosen. The table that maps SIDs to items is built once after the tokenizer is trained and then frozen (Appendix E).

#### Step 5: Sequence-to-Sequence Generation

TIGER flattens a user's history into SID tokens and puts one user token in front. The raw user ID is hashed into one of 2,000 user tokens (Sec. 4). The generator is a Transformer encoder-decoder built with the T5X framework, with 4 layers each in the encoder and the decoder and 6 self-attention heads of dimension 64 (Sec. 4).

> "Given Semantic IDs for items in a user session, a Transformer-based sequence-to-sequence model is trained to predict the Semantic ID of the next item that the user will interact with." (Abstract)

The generator is trained with next-token prediction over the four tokens of the target SID:

```math
\mathcal{L}_{\mathrm{NTP}} = -\sum_{m=1}^{4} \log P_\theta\left(c_{t,m} \mid \mathbf{c}_{1:t-1},\, c_{t,1:m-1}\right)
```

where:
- $`\mathbf{c}_{1:t-1}`$ is the SID token sequence of the history items;
- $`c_{t,m}`$ is the $`m`$-th token of the target item's SID.

At inference, TIGER decodes SIDs with autoregressive beam search and maps each generated SID to an item through the frozen lookup table (Appendix E).

### 3. Experimental Findings

- Beauty: TIGER reports Recall@5 = 0.0454, NDCG@5 = 0.0321, Recall@10 = 0.0648, and NDCG@10 = 0.0384, against 0.0387, 0.0249, 0.0605, and 0.0318 for SASRec (Table 1).
- Sports and Outdoors: TIGER reports Recall@5 = 0.0264, NDCG@5 = 0.0181, Recall@10 = 0.0400, and NDCG@10 = 0.0225, against 0.0233, 0.0154, 0.0350, and 0.0192 for SASRec (Table 1).
- Toys and Games: TIGER reports Recall@5 = 0.0521, NDCG@5 = 0.0371, Recall@10 = 0.0712, and NDCG@10 = 0.0432, against 0.0463, 0.0306, 0.0675, and 0.0374 for SASRec (Table 1).
- ID ablation: Table 2 compares random IDs, LSH Semantic IDs, and RQ-VAE Semantic IDs. RQ-VAE IDs score highest and random IDs lowest in all twelve metric columns (Table 2).

  > "Our results show that RQ-VAE consistently outperforms LSH." (Sec. 4.2)

- Invalid IDs: for top-10 predictions, 0.1%–1.6% of generated IDs map to no item across the three datasets (Sec. 4.5, Fig. 6).
- Cold start: the authors state that SIDs improve retrieval of items with no prior interaction history (Abstract, Fig. 5).
- Diversity: temperature-based sampling during decoding controls the diversity of predictions (Sec. 4.3).
- ID length and codebook size: the authors also tried other settings, such as 6 codewords from codebooks of size 64.

  > "We noticed that the recommendation metrics for TIGER were robust to these changes." (Appendix E)

### 4. Limitations & Critical Analysis

**Stated by the authors.** The authors state that TIGER can be more expensive than ANN-based models at inference because of beam search (Appendix E).

> "we note that our model can be more computationally expensive than ANN-based models during inference due to the use of beam search for autoregressive decoding." (Appendix E)

**Our analysis.**

- TIGER's representation uses item text only (`Text`). LETTER uses text and collaborative signals (`Text+CF`) with a learnable RQ tokenizer (`Learn. RQ`).
- The tokenizer is fixed before the generator trains (`Fixed`). ETEGRec updates the tokenizer and the generator in turns (`Altern.`).
- The fourth token only separates items that share three codes; the paper derives it from the collision, not from item content (Sec. 3.1).
- Unconstrained beam search can produce IDs that map to no item (Sec. 4.5). LETTER decodes with constrained beam search (`C-Beam`).
- Beam search runs one generator step per SID token. RPG predicts all tokens of an SID in parallel (`Non-AR`) and decodes over a graph of valid IDs (`Graph`).
