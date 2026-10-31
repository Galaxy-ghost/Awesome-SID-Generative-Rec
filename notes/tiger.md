## Positioning in the Problem × Stage Matrix

- **Matrix Cell**: **Paradigms, Systems and Benchmarks** (`problem: psb`, `stage: n/a`).
- **Why Here**: TIGER defines the canonical five-stage pipeline for Semantic ID-based generative recommendation rather than patching a single failure mode. Subsequent methods in bands `I`–`VI` modify one or more of TIGER's five stages (`Text` representation $`\rightarrow`$ `RQ-VAE` tokenization $`\rightarrow`$ `Enc-Dec` backbone $`\rightarrow`$ `Fixed` / `NTP` training $`\rightarrow`$ `Beam` inference).

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

For each item $`i`$, its textual metadata (title, brand, price, and category) is encoded by a frozen pre-trained Sentence-T5 encoder into a dense vector $`\mathbf{x} \in \mathbb{R}^{768}`$, which an MLP encoder $`E(\cdot)`$ projects to a latent vector $`\mathbf{z} := E(\mathbf{x}) \in \mathbb{R}^{d_z}`$ ($`d_z = 32`$).

At quantization depth $`m \in \{1, \dots, M\}`$ ($`M = 3`$) with level-specific codebook $`\mathcal{C}^{(m)} = \{\mathbf{e}_k^{(m)}\}_{k=1}^{K}`$ ($`K = 256`$), RQ-VAE quantizes the residual $`\mathbf{r}_m`$ greedily from coarse to fine:

```math
\mathbf{r}_1 = \mathbf{z}, \qquad c_m = \arg\min_{k \in \{1,\dots,K\}} \left\| \mathbf{r}_m - \mathbf{e}_k^{(m)} \right\|_2^2, \qquad \mathbf{r}_{m+1} = \mathbf{r}_m - \mathbf{e}_{c_m}^{(m)}
```

where:
- $`\mathbf{r}_m \in \mathbb{R}^{d_z}`$ is the residual vector entering level $`m`$;
- $`c_m \in \{0, \dots, K-1\}`$ is the discrete codeword index at depth $`m`$;
- $`\mathbf{e}_{c_m}^{(m)} \in \mathbb{R}^{d_z}`$ is the selected centroid at level $`m`$.

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

The quantized vector $`\hat{\mathbf{z}} = \sum_{m=1}^{M} \mathbf{e}_{c_m}^{(m)}`$ is passed through an MLP decoder $`D(\cdot)`$ to reconstruct $`\hat{\mathbf{x}} = D(\hat{\mathbf{z}})`$. The total RQ-VAE loss is:

```math
\mathcal{L}_{\text{RQ-VAE}}(\mathbf{x}) = \|\mathbf{x} - \hat{\mathbf{x}}\|_2^2 + \sum_{m=1}^{M} \left( \left\|\mathrm{sg}[\mathbf{r}_m] - \mathbf{e}_{c_m}^{(m)}\right\|_2^2 + \beta \left\|\mathbf{r}_m - \mathrm{sg}[\mathbf{e}_{c_m}^{(m)}]\right\|_2^2 \right)
```

where $`\mathrm{sg}[\cdot]`$ is the stop-gradient operator and $`\beta = 0.25`$ balances commitment to the chosen centroids. To prevent codebook collapse on the first batch, TIGER initializes $`\mathcal{C}^{(m)}`$ via $`k`$-means on the residuals $`\mathbf{r}_m`$.

### Step 3: Collision Resolution Suffix and Sequence-to-Sequence NTP

If $`N_{\text{coll}}`$ items share the same 3-tuple $`(c_1, c_2, c_3)`$, TIGER appends a fourth disambiguating token $`c_4 \in \{0, 1, \dots, N_{\text{coll}}-1\}`$ assigned in arbitrary order:

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

Given a user interaction history $`(i_1, \dots, i_{t-1})`$ flattened into a sequence of Semantic ID tokens (prepended with a hashed user token), a T5-style Encoder-Decoder maximizes the token-level next-token prediction (`NTP`) log-likelihood over the target item's 4-token code $`\mathbf{c}_t = (c_{t,1}, c_{t,2}, c_{t,3}, c_{t,4})`$:

```math
\mathcal{L}_{\text{NTP}} = -\sum_{m=1}^{4} \log P_\theta\!\left(c_{t,m} \;\middle|\; \mathbf{c}_{1:t-1},\, c_{t,1:m-1}\right)
```

---

## Verbatim Quotes from the Paper

- **Generative retrieval paradigm** (§1, p.1): *"We propose a new paradigm, generative retrieval, where a recommender model autoregressively decodes the identifiers of the target candidates."*
- **Residual quantization for Semantic IDs** (§3.1, p.3): *"RQ-VAE is a multi-level vector quantizer that applies quantization on residuals to generate a tuple of codewords (i.e., Semantic IDs)."*
- **Suffix-based collision handling** (§3.1, p.4): *"To handle collisions, we append an extra token at the end of the codewords to make them unique."*

---

## Experimental Protocol & Key Results

- **Datasets & Split**: Amazon Product Reviews (`Beauty`, `Sports and Outdoors`, `Toys and Games`), 5-core filtering, standard leave-one-out split (last item for test, second-to-last for validation).
- **Reported Metrics** (Table 1 of the paper, 4-layer T5 encoder + 4-layer T5 decoder, $`M=3, K=256`$):
  - **Beauty**: Recall@5 = `0.0454`, NDCG@5 = `0.0321`, Recall@10 = `0.0648`, NDCG@10 = `0.0384` (vs. SASRec Recall@5 = `0.0387`, NDCG@5 = `0.0249`).
  - **Sports and Outdoors**: Recall@5 = `0.0264`, NDCG@5 = `0.0181`, Recall@10 = `0.0400`, NDCG@10 = `0.0225` (vs. SASRec Recall@5 = `0.0233`, NDCG@5 = `0.0154`).
  - **Toys and Games**: Recall@5 = `0.0521`, NDCG@5 = `0.0371`, Recall@10 = `0.0712`, NDCG@10 = `0.0432` (vs. SASRec Recall@5 = `0.0463`, NDCG@5 = `0.0306`).
- **Tokenization Ablation** (Table 2 of the paper): `RQ-VAE` SIDs consistently outperform `Random ID` and `LSH` IDs across all three Amazon subsets.

---

## Limitations & Follow-up Work in the Matrix

1. **Content-only representation (`I. Informativeness`)**: Frozen Sentence-T5 embeddings ignore collaborative co-occurrence; addressed by `LETTER`, `CoST`, `EAGER-LLM`, and `UNGER`.
2. **Non-semantic collision suffix and invalid beams (`II. Uniqueness and Validity`)**: The trailing integer $`c_4`$ introduces an arbitrary suffix token and unconstrained beam search can emit unassigned 4-tuples; addressed by Sinkhorn/uniformity regularizers (`LETTER`, `MME-SID`) and prefix-tree constrained decoding (`C-Beam`).
3. **Two-stage objective mismatch (`III. SID–Model Alignment`)**: The tokenizer is frozen (`Fixed`) before generator training; addressed by alternating or joint optimization (`ETEGRec`, `Align3GR`).
4. **Sequential beam cost on long codes (`V. Efficiency`)**: Autoregressive decoding scales linearly with code length $`M`$ and beam width $`B`$; addressed by parallel multi-token prediction (`RPG`, `ACERec`, `SPRINT`) and speculative decoding (`AtSpeed`, `NEZHA`).

---

## 旧卡片说明

迁自 `d61aa6c:papers/tiger.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### TIGER：生成式检索推荐

> TIGER 将物品内容压缩为层次化语义标识，并让 Transformer 直接生成下一件物品的完整标识，从而把序列推荐中的候选检索转化为生成任务。

### 研究动机与问题定义

论文将传统序列推荐中的 ANN/MIPS 候选检索改写为语义标识生成：Transformer 参数充当生成式索引，直接预测下一件物品。TIGER 是这一方向的早期代表工作，但其冷启动结果来自模拟的未见物品设置，并非真实线上动态目录验证。

### TL;DR（核心摘要）

`用户历史 → 物品语义标识 → T5 编码器-解码器 → 完整语义标识 → 查表得到推荐物品`

首先，论文将物品标题、价格、品牌和类别输入 Sentence-T5，再用 RQ-VAE（残差量化变分自编码器）逐层量化内容向量，得到定长、层次化 Semantic ID；碰撞时追加后缀码字保证当前物品库中的唯一性。训练时将用户历史展开为语义标识序列，由 T5 风格编码器-解码器自回归生成下一物品的完整标识。在线使用束搜索生成候选，并通过冻结查表解析物品，不依赖独立召回器或精排器。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户交互历史，以及物品标题、价格、品牌和类别等文本化元数据 |
| 信息融入位置 | 内容信息进入语义标识构建；交互历史和用户标识进入生成模型输入 |
| 语义标识结构 | 定长、顺序化、层次化码字序列 |
| 适用场景 | 常规序列推荐，以及基于内容编码的模拟物品冷启动 |

### 方法设计

#### 3.1 生成式检索任务（Generative Retrieval）
TIGER 将下一物品预测改写为目标物品 Semantic ID 序列生成。用户历史先转换为对应 SID，T5 风格编码器读取历史序列，解码器逐 token 生成目标 SID；完整标识通过物品索引表解析为推荐物品。

#### 3.2 物品标识学习（Item Tokenization）
论文使用 RQ-VAE 将物品标题和描述的语义向量进行残差量化。不同量化层形成从粗到细的层次化 codeword，物品因此拥有固定长度的 SID。量化器通过重构损失和码本相关损失学习，训练完成后冻结用于推荐。

#### 3.3 生成模型与推理（Generative Recommender）
生成器以历史 SID 为输入进行自回归 next-item 训练。推理时使用束搜索，将生成的有效 SID 映射到物品形成 Top-K 结果。当前 Table 1 记录为 Beam。

#### 3.4 实验相关设计
论文进一步分析了 SID 长度、码本大小、无效标识和模拟冷启动。实验结果说明层次语义能帮助新物品表示，但动态物品更新并未成为完整在线方案。

### 实验结论

- 三个 Amazon 商品数据集上的 Recall/NDCG 均优于论文列出的比较基线。
- RQ-VAE 语义标识优于 LSH 标识和随机标识，支持内容码字共享有助于推荐。
- 模拟冷启动实验显示共享语义前缀可以推荐未见物品，温度采样可调节类别多样性。

### 局限性与研究定位

#### 局限性
- 唯一性后缀不一定具有语义，模型也会生成少量无效标识。
- 自回归束搜索可能比 ANN 检索更昂贵，论文未报告完整线上效率。
- 数据集和冷启动协议较有限，动态新增物品与真实时间切分仍未验证。

#### 研究定位
TIGER 展示了直接生成 Semantic ID 作为推荐检索的可行性，并将 RQ-VAE 内容语义引入离散标识。它适合放在“语义标识构建”和“生成式推荐架构”章节；后续工作主要改进约束解码、效率和动态目录泛化。

### 相关资源

- [论文原文](https://papers.neurips.cc/paper_files/paper/2023/hash/20dcab0f14046a5c6b02b61da9f13229-Abstract-Conference.html)
- [公开 PyTorch 实现（第三方）](https://github.com/baiyimeng/TIGER)

### 标签

`残差量化` · `语义标识` · `自回归生成` · `编码器-解码器` · `冷启动` · `束搜索`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：将内容表示转为可生成的层次化SID。
- 使用场景：序列推荐、冷启动。
