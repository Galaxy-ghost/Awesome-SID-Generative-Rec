# RPG

*Generating long semantic ids in parallel for recommendation* — Hou et al., KDD’25

[arXiv](https://arxiv.org/abs/2506.05781) · [Record](../../data/papers/rpg.yaml) · [← Catalog](../../README.md#v--backbone)

> Abstract: "they often suffer from inefficient inference due to the reliance on resource-intensive beam search".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Backbone** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | `Par. OPQ` | **`Non-AR`** | `Fixed / MTP` | `Graph` |

- `Non-AR`: Non-autoregressive.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `MTP`: Predicts several codes in parallel at once.

## Architecture

![RPG architecture diagram](../../architectures/rpg.png)

## Evidence

- **`problem`** (arXiv abstract): Abstract: "they often suffer from inefficient inference due to the reliance on resource-intensive beam search".

## Positioning in the Problem × Stage Matrix

- **Matrix Cell**: **V. Efficiency** $`\times`$ **Backbone** (`problem: V`, `stage: Backbone`).
- **Why Here**: Longer Semantic IDs ($`M \in \{16, 32, 64\}`$ sub-tokens) eliminate collisions and capture fine-grained item semantics, but autoregressive decoding over $`M`$ steps incurs prohibitive latency and cascading prefix errors. RPG replaces sequential token-by-token generation with a **non-autoregressive (`Non-AR`) parallel multi-token prediction (`MTP`) backbone** coupled with **Optimized Product Quantization (`Par. OPQ`)** and **graph-guided decoding (`Graph`)**.

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

Whereas `RQ-VAE` quantizes residuals sequentially (creating strict order dependencies $`c_1 \rightarrow c_2 \rightarrow \dots \rightarrow c_M`$), RPG learns an orthogonal rotation matrix $`\mathbf{R} \in \mathbb{R}^{d \times d}`$ ($`\mathbf{R}^\top \mathbf{R} = \mathbf{I}`$) that decomposes the item representation $`\mathbf{x}_i \in \mathbb{R}^d`$ into $`M`$ orthogonal subspaces of dimension $`d/M`$:

```math
\tilde{\mathbf{x}}_i = \mathbf{R}\mathbf{x}_i = \left[\tilde{\mathbf{x}}_i^{(1)} \,\|\, \tilde{\mathbf{x}}_i^{(2)} \,\|\, \dots \,\|\, \tilde{\mathbf{x}}_i^{(M)}\right], \qquad c_{i,m} = \arg\min_{k \in \{1,\dots,K\}} \left\| \tilde{\mathbf{x}}_i^{(m)} - \mathbf{e}_k^{(m)} \right\|_2^2
```

where:
- $`\tilde{\mathbf{x}}_i^{(m)} \in \mathbb{R}^{d/M}`$ is the $`m`$-th subspace projection of item $`i`$;
- $`\mathcal{C}^{(m)} = \{\mathbf{e}_k^{(m)}\}_{k=1}^{K}`$ is the $`m`$-th subspace codebook;
- $`c_{i,m} \in \{1, \dots, K\}`$ is the $`m`$-th token of item $`i`$'s unordered Semantic ID tuple $`\mathbf{c}_i = (c_{i,1}, \dots, c_{i,M})`$.

### Step 2: Non-Autoregressive Multi-Token Prediction (`Non-AR` + `MTP`)

Given the user interaction sequence $`S_u = (i_1, \dots, i_{t-1})`$, RPG aggregates each history item's $`M`$ sub-token embeddings into a single item-level vector so the sequence length fed into the Transformer backbone remains $`t-1`$ rather than $`M(t-1)`$. From the final hidden state $`\mathbf{h}_u \in \mathbb{R}^d`$, $`M`$ parallel projection heads $`\mathbf{W}^{(1)}, \dots, \mathbf{W}^{(M)}`$ predict all $`M`$ target code positions in a single forward pass:

```math
P_\theta^{(m)}(c_{t,m} = k \mid S_u) = \frac{\exp\!\left(\mathbf{e}_k^{(m)\top} \mathbf{W}^{(m)} \mathbf{h}_u / \tau\right)}{\sum_{k'=1}^{K} \exp\!\left(\mathbf{e}_{k'}^{(m)\top} \mathbf{W}^{(m)} \mathbf{h}_u / \tau\right)}, \qquad \mathcal{L}_{\text{MTP}} = -\frac{1}{M}\sum_{m=1}^{M} \log P_\theta^{(m)}(c_{t,m} \mid S_u)
```

where $`\tau \gt 0`$ is a temperature hyperparameter.

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

Because the $`M`$ heads predict marginal distributions independently, naively picking $`\arg\max_k P_\theta^{(m)}(k \mid S_u)`$ for each $`m`$ rarely lands on a valid catalog item when $`K^M \gg |\mathcal{I}|`$, while scoring all $`|\mathcal{I}|`$ items scales linearly with catalog size. RPG constructs a sparse $`k`$-NN graph $`\mathcal{G} = (\mathcal{I}, \mathcal{E})`$ over the catalog items based on their quantized OPQ representations, scores a small seed set using $`\sum_{m=1}^{M} \log P_\theta^{(m)}(c_{i,m} \mid S_u)`$, and iteratively expands neighbors on $`\mathcal{G}`$ to retrieve the highest-scoring valid items in sub-linear time.

---

## Verbatim Quotes from the Paper

- **Motivation for parallel long SIDs** (§1, p.1): *"We propose a paradigm that generates long Semantic IDs in parallel for recommendation (RPG)."*
- **Order-agnostic subspace tokenization** (§2.1, p.3): *"Instead of residual quantization that enforces a coarse-to-fine sequential dependency, we adopt product quantization over orthogonal subspaces so that tokens at different positions can be predicted in parallel."*
- **Graph-guided decoding** (§2.3, p.4): *"During inference, we leverage a semantic similarity graph over item IDs to iteratively propagate and refine candidate IDs using the parallelly predicted token distributions."*

---

## Experimental Protocol & Key Results

- **Datasets & Split**: Amazon Reviews (`Beauty`, `Sports and Outdoors`, `Toys and Games`, `CDs and Vinyl`), 5-core leave-one-out split.
- **Reported Findings** (§3, Tables 1–3 of the paper):
  - **Scaling SID length $`M`$**: Increasing $`M`$ from $`4`$ to $`16`$–$`64`$ in RPG consistently improves Recall@10 and NDCG@10 while eliminating SID collisions without needing an arbitrary trailing collision token.
  - **Inference Speedup**: Because all $`M`$ positions are predicted in one forward pass followed by lightweight graph propagation, RPG reduces decoding latency and GPU memory by an order of magnitude compared to autoregressive beam search over long SIDs.

---

## Limitations & Comparison with Peer Methods in `V. Efficiency`

1. **Marginal factorizability vs. intra-code dependencies**: Independent subspace heads assume conditional independence across the $`M`$ sub-tokens given $`\mathbf{h}_u`$. Within the same cell (`V. Efficiency` $`\times`$ `Backbone`), **`ACERec`** adds contrastive and auxiliary alignment regularizers to `Par. OPQ` + `Non-AR`, while **`SPRINT`** replaces independent token cross-entropy with a dual-level flow contrastive objective (`Dual-level Flow Ctr.`) that jointly optimizes token-product scores and whole-SID similarity.
2. **Graph maintenance overhead**: Maintaining the item similarity graph $`\mathcal{G}`$ adds an index structure alongside the generator parameters, whereas **`SID-MLP`** (`Enc-MLP`) and **`OneRec-V2`** (`Lazy Dec-Only`) accelerate autoregressive decoding without an external graph.

---

## 旧卡片说明

迁自 `d61aa6c:papers/rpg.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### RPG：并行生成长语义标识

> RPG 面向长语义标识的生成效率与质量问题，结合多 token 预测和标识图传播，实现更高效的推荐生成。

### 研究动机与问题定义

更长的 SID 能承载更细粒度语义，但自回归逐 token 生成会显著增加成本，且长序列误差更易累积。RPG 研究如何在保留长 SID 表达能力的同时进行并行预测和结构化解码。

### TL;DR（核心摘要）

`物品信息 → 长SID与相似图 → 多token训练 → 并行生成/图传播 → 推荐物品`

RPG 为物品学习长语义标识，使用 multi-token prediction 同时学习多个位置，并根据 SID 相似关系构建图。推理时结合候选标识的图结构进行迭代传播，最后生成完整 SID 并映射物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 交互历史、物品语义和 SID 相似关系 |
| 信息融入位置 | SID 构建、并行预测目标和解码图 |
| 语义标识结构 | 长定长序列 |
| 适用场景 | 长标识生成式推荐 |

### 方法设计

#### 2.1 长语义标识物品表示
RPG 将物品表示为较长的层次化 SID，使不同 code 位置能够表达更细粒度的语义。长标识提升表达能力，但也带来序列长度、内存和自回归误差累积问题。

#### 2.2 并行学习 SID 生成
模型采用 multi-token prediction，同时预测多个 SID 位置，减少严格逐 token 训练的依赖。训练目标仍要求生成结果与目标 SID 一致，并通过语义表示和协同关系维持标识质量。

#### 2.3 图结构辅助解码
论文根据 SID 或物品相似关系构建图，在候选生成过程中传播相邻标识的信息。推理阶段先产生部分/并行候选，再利用图结构迭代补全和筛选，输出完整 SID。

#### 2.4 讨论
论文进一步讨论 SID 长度、运行内存、推理速度和冷启动。RPG 的核心是让长 SID 的表达收益不被自回归成本抵消。

### 实验结论

- RPG 在延长 SID 后仍能保持或提升推荐效果。
- 并行生成降低了长标识带来的推理开销。
- 冷启动分析显示语义标识对未见物品具有一定帮助。

### 局限性与研究定位

#### 局限性
- 图构建和迭代传播增加了系统组件。
- 长 SID 的词表、图规模与在线内存成本仍需更多工业验证。

#### 研究定位
RPG 的主要贡献是把长 SID 的表达能力与并行生成结合起来，适合放在“长语义标识与高效解码”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2506.05781)

### 标签

`长SID` · `并行生成` · `图传播` · `生成式推荐`

### 架构图来源

*图源：原论文，图1。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：并行生成长语义标识。
- 使用场景：长SID推荐。

## Same cell: V × Backbone (10 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [OneRec-V2](onerec-v2.md) | arXiv’25 | `Text+Img+CF†` → `R-KM†` → **`Lazy Dec-Only`** → `Fixed / NTP → RL` → `Beam` |
| [ACERec](acerec.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / MTP + Ctr. + Aux.` → `Scoring` |
| [Deco](deco.md) | arXiv’26 | `Text / –` → `R-KM` → **`Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [IBA](iba.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP → (NTP + Aux.)` → `C-Beam` |
| [LoopGR](loopgr.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec`** → `Fixed / NTP / NTP + Aux.` → `–` |
| [Merge-and-Branch](merge-and-branch.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Dec-Only`** → `Fixed / NTP` → `C-Beam` |
| [PinGER](pinger.md) | arXiv’26 | `Text+Img+CF` → `RQ-VAE` → **`Dec-Only`** → `– / NTP → DPO` → `Div. C-Beam` |
| [SID-MLP](sid-mlp.md) | arXiv’26 | `Text` → `RQ-VAE†` → **`Enc-MLP`** → `Fixed / NTP + Aux.` → `C-Beam` |
| [SPRINT](sprint.md) | arXiv’26 | `Text` → `Par. OPQ` → **`Non-AR`** → `Fixed / Dual-level Flow Ctr.` → `Scoring` |
| [STAMP](stamp.md) | arXiv’26 | `Text` → `RQ-VAE` → **`Enc-Dec / Dec-Only`** → `Fixed / NTP + Aux.` → `C-Beam` |
