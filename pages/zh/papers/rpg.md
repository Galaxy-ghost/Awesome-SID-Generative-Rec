# RPG

[← 问题 × 阶段矩阵](../../../README.zh.md#v--backbone) · [按阶段索引](../index/stages.md) · [按模态找论文](../index/modality.md) · [按领域找论文](../index/domain.md) · [English](../../papers/rpg.md) | 中文

| **题目** | *Generating long semantic ids in parallel for recommendation* |
| :-- | :-- |
| **作者** | Hou et al. |
| **发表** | KDD’25 |
| **问题与阶段** | `V. 效率` · `生成骨干（Backbone）` |
| **改动** | ● 生成骨干 · ○ 训练目标 · ○ 推理 |
| **构码输入** | `Text` |
| **领域** | `电商` |
| **应用场景** | `一般物品推荐`；`公开数据` |
| **链接** | [论文](https://arxiv.org/abs/2506.05781) · [代码](https://github.com/facebookresearch/RPG_KDD2025) |
| **阅读级别** | 代码级精读（第 3 级） |

**本页目录**：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["物品表示 Representation<br/>Text"] --> T["构码 Tokenization<br/>Par. OPQ"] --> B["生成骨干 Backbone<br/>● Non-AR"] --> TR["训练 Training<br/>编号器更新: Fixed<br/>训练目标: ○ MTP"] --> I["推理 Inference<br/>○ Graph"]
    classDef base fill:#f8fafc,stroke:#cbd5e1
    class R,T,B,TR,I base
    classDef other fill:#f8fafc,stroke:#6b8fc7,stroke-width:1.5px,stroke-dasharray:5 3
    class TR,I other
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    class B main
```

- `Text`：物品文本元数据（标题、描述、类目或提示词）。
- `Par. OPQ`：并行优化乘积量化，生成无序多子空间码。
- `Non-AR`：非自回归（Non-autoregressive）并行预测架构。
- `Fixed`：先独立训练并冻结编号器，生成器训练期间 SID 保持不变。
- `MTP`：多 token 并行预测损失（Multi-Token Prediction），一次前向同时预测多个码位。
- `Graph`：在合法物品 SID 近邻图上做迭代图搜索解码。

### TL;DR

> [!NOTE]
> RPG 用多 token 预测损失并行预测长且无序的 OPQ SID，并在合法 ID 图上解码，替代短 ID 上的自回归束搜索。

---

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 主要发现 | 使用最长 64 个 token 的 ID 时，RPG 在 NDCG@10 上较生成式基线平均提升 12.6%，同时降低了推理开销（Abstract）。 |
| 局限 | 作者假设在给定输入序列的条件下，单个语义 ID（Semantic ID，SID）内的各个 token 彼此条件独立（Sec. 2.2.1）。 |

---

### 1. 为什么重要

TIGER 等自回归生成式推荐器通过束搜索逐位解码 SID，单次推荐请求需多次执行生成器前向传播。受此计算开销限制，已有模型通常将 SID 压缩得很短，常见长度为 4 个 token（Abstract）。

> "Running beam search for 32 steps would be computationally prohibitive."（Sec. 1）

RPG 用最长 64 个 token 的无序优化乘积量化（OPQ）ID、单次前向的并行多 token 预测，以及在物品 SID 相似图上的迭代传播解码，替代短残差码上的逐步束搜索。

---

### 2. 方法

![RPG architecture diagram](../../../architectures/rpg.png)

#### 概览

```mermaid
flowchart LR
    A("物品嵌入 x_i") --> B["OPQ 旋转与切分：x_i^(1) ... x_i^(m)"]
    B --> C["m 个子空间码本 C^(1) ... C^(m)"]
    C --> D("无序 m-token SID")
    D --> P["按物品池化 token Aggr -> v_1 ... v_{t-1}"]
    P --> E["Transformer 解码器 -> 序列状态 s"]
    E --> F["m 个并行预测头 g_1(s) ... g_m(s)"]:::key
    L1{{"多 token 预测（MTP）损失"}} -.-> F
    F --> G("缓存对数概率表 [m × M]")
    G --> H["q 轮图约束解码"]:::key
    H --> I("Top-K 物品库物品")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

#### 第 1 步：用 OPQ 构建长 SID

RPG 用优化乘积量化（OPQ）替代残差量化，使所有 SID 位置可以并行预测而非串行依赖（Sec. 2.1.1）。

> "To align with parallel decoding, we tokenize each item into an unordered long semantic ID (up to 64 tokens per item) using optimized product quantization (Jégou et al., 2011; Ge et al., 2014)."（Sec. 1）

OPQ 将旋转后的物品语义嵌入切分为 $`m`$ 个子向量，每个子向量在各自大小为 $`M`$ 的独立码本中完成最近邻量化（Sec. 2.1.1）：

```math
\mathbf{x}_i = \left[\mathbf{x}_i^{(1)}; \dots; \mathbf{x}_i^{(m)}\right], \qquad c_{i,j} = \arg\min_{c \in \mathcal{C}^{(j)}} \left\| \mathbf{x}_i^{(j)} - \mathbf{a}_c^{(j)} \right\|_2^2
```

其中：
- $`\mathbf{x}_i`$ 是物品 $`i`$ 经 OPQ 旋转后的语义嵌入；
- $`\mathbf{x}_i^{(j)}`$ 是其第 $`j`$ 个子向量；
- $`\mathcal{C}^{(j)}`$ 是第 $`j`$ 个子空间码本，含 $`M`$ 个码字 $`\mathbf{a}_c^{(j)}`$；
- $`c_{i,j}`$ 是物品 $`i`$ 的 SID 第 $`j`$ 位 token。

这里的“无序”（"Unordered"）指解码时任一 token 都不以前序位置的 token 为条件，但第 $`j`$ 位仍固定对应第 $`j`$ 个码本（Sec. 2.1.1）。即便不同物品落入同一组 token，它们在解码图中仍保留各自节点；在 64-token 长度下此类冲突极少发生（Appendix C）。

#### 第 2 步：物品级输入

若将每个历史物品展开为 64 个 token，上下文序列会急剧拉长（Sec. 2.1.2）。RPG 为每个码本维护可学习的 token 嵌入表 $`\mathbf{E}_j \in \mathbb{R}^{M \times d}`$，通过均值或最大池化将单个物品的 $`m`$ 个 token 嵌入聚合为单个物品向量 $`\mathbf{v}_i = \mathrm{Aggr}(\mathbf{e}_{1,c_{i,1}}, \dots, \mathbf{e}_{m,c_{i,m}})`$（Sec. 2.1.2）。Transformer 解码器读入历史序列 $`\mathbf{v}_1, \dots, \mathbf{v}_{t-1}`$ 并输出用户状态表示 $`\mathbf{s} \in \mathbb{R}^{d}`$（Sec. 2.2.1）。

#### 第 3 步：用 MTP 损失并行预测

RPG 为下一物品 SID 的每一位配置独立的投影头，并用多 token 预测（MTP）损失联合训练全部 $`m`$ 个预测头。

> "Since each token produced by OPQ encodes a separate subvector of the target item's semantic representation, we assume that tokens in the tuple are conditionally independent given the input sequence s."（Sec. 2.2.1）

```math
\mathcal{L} = -\sum_{j=1}^{m} \log \mathbb{P}^{(j)}(c_{t,j} \mid s) = -\sum_{j=1}^{m} \log \frac{\exp\left(\mathbf{e}_{c_{t,j}}^{\top} g_j(\mathbf{s}) / \tau\right)}{\sum_{c \in \mathcal{C}^{(j)}} \exp\left(\mathbf{e}_{c}^{\top} g_j(\mathbf{s}) / \tau\right)}
```

其中：
- $`c_{t,j}`$ 是目标物品 SID 的第 $`j`$ 个 token；
- $`g_j`$ 是第 $`j`$ 个码本对应的 MLP 投影头；
- $`\mathbf{e}_c`$ 是 token $`c`$ 的嵌入向量；
- $`\tau`$ 是温度系数（Eq. 1）。

#### 第 4 步：缓存 token 分数

推理时，RPG 只需一次前向传播即可算出全部 $`m`$ 个码本上的 token 概率分布并缓存（Eq. 2）。任意候选 SID 的总分随即简化为查表累加 $`m`$ 个缓存对数概率（Eq. 3）：

```math
\mathbf{p}^{(j)} = \mathrm{softmax}\left(\mathbf{E}_j\, g_j(\mathbf{s}) / \tau\right) \in \mathbb{R}^{M}, \qquad \mathrm{score}(c_1, \dots, c_m) = \sum_{j=1}^{m} \log p^{(j)}_{c_j}
```

其中 $`p^{(j)}_{c_j}`$ 是 $`\mathbf{p}^{(j)}`$ 中对应 token $`c_j`$ 的概率项（Sec. 2.2.2）。

#### 第 5 步：图约束解码

训练结束后，RPG 离线构建以物品库各物品为节点的有向 $`k`$ 近邻图（Sec. 2.3.1）。两物品间的相似度定义为各子空间 token 嵌入内积之和：

```math
\mathrm{sim}(i, i') = \sum_{j=1}^{m} \mathbf{e}_{j,c_{i,j}}^{\top}\, \mathbf{e}_{j,c_{i',j}}
```

每个节点保留相似度最高的 $`k`$ 个邻居（Sec. 2.3.1）并包含一条自环边（Sec. 2.3.2）。在线解码按四步迭代执行（Sec. 2.3.2）：

1. 从物品库随机采样 $`b`$ 个合法 SID 作为初始束。
2. 将当前束全部节点的 $`b \times k`$ 个图邻居加入临时候选集。
3. 查表累加缓存的对数概率为访问到的候选打分，保留得分最高的 $`b`$ 个节点。
4. 重复第 2、3 步共 $`q`$ 轮，返回最终束作为 top-$`K`$ 推荐结果。

> "Since neighboring nodes in the graph tend to have similar logits, we expand the beam by propagating through the graph, including all b×k neighbors of the current beam into a temporary set."（Sec. 2.3.2）

```python
import torch

def rpg_decode(s, heads, token_emb, item_codes, neighbors, b=10, q=2, tau=0.05):
    """
    s:          [d] sequence representation of one user
    heads:      list of m projection heads g_j, each mapping [d] -> [d]
    token_emb:  [m, M, d] token embedding tables E_j
    item_codes: [N, m] SID of every catalog item; entry j indexes codebook j
    neighbors:  [N, k] graph neighbors of every item; the item itself is included here
    """
    m = item_codes.size(1)
    # Eq. 2: one softmax per codebook, cached for this user
    proj = torch.stack([g(s) for g in heads])                                         # [m, d]
    log_p = torch.log_softmax(torch.einsum("jcd,jd->jc", token_emb, proj) / tau, -1)  # [m, M]
    # Eq. 3 for the whole catalog
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

简化说明：代码在图搜索前一次性算出了全量物品库分数；原论文仅对沿图边访问到的候选节点打分（Sec. 2.3.3）。此外，代码将预测头、token 嵌入表与近邻图作为已知输入传入，省略了 OPQ 量化、Transformer 解码器、MTP 训练与离线建图过程。

> "Compared to generative models like TIGER (Rajput et al., 2023), RPG reduces the number of sequence encoder forward passes per input instance from approximately O(bm) to just O(1), greatly improving inference efficiency (Section 3.3)."（Sec. 2.4.2）

```mermaid
flowchart LR
    G("离线 k-NN SID 近邻图（含自环）") --> S2
    S1["1. 随机采样 b 个合法 SID 作初始束"] --> S2["2. 沿图边扩展 b×k 个邻居候选"]
    C("缓存对数概率表 log p^(j)") --> S3["3. 累加 m 位缓存分数并剪枝保留 top-b"]:::key
    S2 --> S3
    S3 -->|"重复 q 轮"| S2
    S3 --> S4("4. 输出最终束作为 top-K 物品")
    classDef key fill:#eaf2fb,stroke:#6b8fc7
```

---

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Amazon Reviews: Sports and Outdoors, Beauty, Toys and Games, and CDs and Vinyl; filtering rules: not reported.
  - 出处：The four Amazon categories and chronological protocol are stated, but 5-core or other filtering rules are not stated in the body or appendix; [S3.SS1.p1](https://arxiv.org/html/2506.05781v1#S3.SS1.p1) and [S3.SS1.p2](https://arxiv.org/html/2506.05781v1#S3.SS1.p2), dataset counts in [S2.T1](https://arxiv.org/html/2506.05781v1#S2.T1).
- **切分**：Per-user chronological leave-last-out: last item for test, second-last for validation, earlier items for training.
  - 出处：The last interaction is test, the second-last validation, and the remaining earlier interactions form the training history; [S3.SS1.p2](https://arxiv.org/html/2506.05781v1#S3.SS1.p2).
- **候选集**：Evaluation candidate protocol: not reported (full catalog versus sampled-negative ranking). Inference searches a graph of valid catalog items and scores only visited nodes; per-user exclusion rules are not reported.
  - 出处：The evaluation description does not specify full-catalog versus sampled-negative ranking; [S3.SS1.p2](https://arxiv.org/html/2506.05781v1#S3.SS1.p2). The separate inference description builds a graph over valid catalog items and starts with b random valid nodes; this does not by itself establish the evaluation candidate protocol; [S2.SS3.SSS1.p1](https://arxiv.org/html/2506.05781v1#S2.SS3.SSS1.p1) and [S2.SS3.SSS2.p2](https://arxiv.org/html/2506.05781v1#S2.SS3.SSS2.p2).
- **可见性**：Tokenizer exposure of test-only items: not reported. The long-tail analysis groups items by training frequency [0,5], [6,10], [11,15], and [16,20]; it does not isolate strictly unseen items from low-frequency items.
  - 出处：Figure 5 combines zero-frequency and low-frequency targets, so it cannot establish separate strictly unseen-item performance; tokenizer exposure of those targets is not specified; [S3.SS5.SSS3.p1](https://arxiv.org/html/2506.05781v1#S3.SS5.SSS3.p1).
- **SID 规格**：Parallel OPQ subspaces, with best lengths Sports 16, Beauty 32, Toys 16, and CDs 64; per-subspace codebook size: not reported as an experimental setting. Colliding items retain separate graph nodes; no guaranteed collision-free identifier is claimed.
  - 出处：Best SID lengths are in Table 6; the 256-entry codebook in the introduction is an example, not an explicit main-experiment setting; item-based graph nodes permit collisions; [A2.T6](https://arxiv.org/html/2506.05781v1#A2.T6), [S1](https://arxiv.org/html/2506.05781v1#S1), and [A3.p2](https://arxiv.org/html/2506.05781v1#A3.p2).
- **推理预算**：Initial random seeds and retained beam b=10; best (neighbors k, iterations q): Sports (100,2), Beauty (100,3), Toys (50,5), CDs (500,3). One NVIDIA RTX 3090 24GB; inference batch size: not reported (training batch size is 256). Sports-only fixed-configuration scaling experiment reports approximately 15x faster inference and 25x lower runtime memory than TIGER; these are not total-storage reductions or per-request latency claims.
  - 出处：Table 6 supplies b/k/q; Appendix B supplies hardware and separates checkpoint selection from graph-budget tuning; the batch size 256 in Section 3.1 is a training setting, not an inference setting; [A2.T6](https://arxiv.org/html/2506.05781v1#A2.T6), [A2.p1](https://arxiv.org/html/2506.05781v1#A2.p1), [S3.SS1.p6](https://arxiv.org/html/2506.05781v1#S3.SS1.p6). Speed/memory scope: [S3.SS3.p1](https://arxiv.org/html/2506.05781v1#S3.SS3.p1) and [S3.SS3.p2](https://arxiv.org/html/2506.05781v1#S3.SS3.p2).
- **结果来源**：arXiv:2506.05781v1: Table 2 (main ranking results), Table 3 (ablations), Table 4 (semantic-encoder-controlled comparison), Figure 3 (Sports efficiency), Figure 5 (training-frequency analysis), and Tables 6 and 8 (best inference budgets and memory scope).
  - 出处：Overall ranking metrics, graph/architecture ablations, encoder-matched comparisons, and the bounded efficiency study are separate result locations; [S2.T2](https://arxiv.org/html/2506.05781v1#S2.T2), [S3.T3](https://arxiv.org/html/2506.05781v1#S3.T3), [S3.T4](https://arxiv.org/html/2506.05781v1#S3.T4), and [S3.F3](https://arxiv.org/html/2506.05781v1#S3.F3).

</details>

- 主排序对比：在 Sports and Outdoors、Beauty、Toys and Games 和 CDs and Vinyl 四个数据集上，采用长 OPQ SID 的 RPG 在 NDCG@10 上较 TIGER、VQ-Rec 等序列与生成式基线平均提升 12.6%（Abstract，Table 2）。
- 推理效率：在 Sports 上，RPG 的运行时显存占用与推理耗时均显著低于采用自回归束搜索的 TIGER（Sec. 3.3，Fig. 3）。

  > "Moreover, RPG reduces runtime memory consumption by nearly 25× and achieves an inference speedup of almost 15× compared to TIGER."（Sec. 3.3）

- ID 长度消融：排序指标并非随 SID 长度单调递增；Sports、Beauty、Toys 和 CDs 上的最优长度分别为 16、32、16 和 64（Sec. 3.5.1，Fig. 4）。

  > "From Figure 4, we observe that, in general, longer OPQ-based semantic IDs lead to better performance. However, for smaller datasets, they may converge earlier."（Sec. 3.5.1）

- 语义编码器对齐：主实验使用 OpenAI text-embedding-3-large 编码物品文本，Table 4 额外换用 sentence-t5-base 重做对比以对齐既往 TIGER 基准协议（Sec. 3.1，Sec. 3.5.2）。
- 长尾物品表现：在 Sports 按训练交互频次划分的各分组中，RPG 均优于 TIGER（Sec. 3.5.3，Fig. 5）。

---

### 4. 局限与分析

**Stated by the authors.** 效率对比实验仅采用单一固定超参数配置，且所报告的运行内存仅统计计算 logit 时的 GPU 显存，不包含模型参数本身的存储开销（Sec. 3.3）。

**Our analysis.**

- 候选 SID 的得分由各位边际对数概率直接相加得到（Eq. 3），因此生成器无法建模同一 SID 内部不同位置 token 之间的联合依赖。同一矩阵格内的 ACERec 引入对比与辅助目标（`MTP + Ctr. + Aux.`），SPRINT 将训练目标替换为 `Dual-level Flow Ctr.`；二者均保留 `Par. OPQ` 与 `Non-AR`。
- 解码近邻图是独立于生成器的外部索引，每个物品对应一个图节点；一旦物品重新编号或重训 token 嵌入，整张图都必须重建（Sec. 2.3.1）。

---

### 5. 相关工作

```mermaid
flowchart LR
    P["RPG"]
    P -->|"同期对比"| A["TIGER"]
    P -->|"前序工作"| B["VQ-Rec"]
    P -->|"替代方案"| C["LETTER"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7,stroke-width:2px
    classDef peer fill:#f8fafc,stroke:#cbd5e1
    class P main
    class A,B,C peer
```

- **同期对比** · [TIGER](tiger.md): RPG compares its parallel OPQ-token prediction and graph-constrained decoding with TIGER's autoregressive RQ-VAE-token generation.
  - 出处：RPG v1, Section 2.1.1 describes OPQ: [S2.SS1.SSS1.p1](https://arxiv.org/html/2506.05781v1#S2.SS1.SSS1.p1); Section 2.4.2 explicitly contrasts TIGER: [S2.SS4.SSS2.p1](https://arxiv.org/html/2506.05781v1#S2.SS4.SSS2.p1); Section 3.1 names the TIGER baseline and Table 2 compares results: [S3.SS1.p4](https://arxiv.org/html/2506.05781v1#S3.SS1.p4) and [S2.T2](https://arxiv.org/html/2506.05781v1#S2.T2).
- **前序工作** · [VQ-Rec](vq-rec.md): RPG follows VQ-Rec in using optimized product quantization, then predicts individual codes and searches an item graph instead of using VQ-Rec's retrieval model.
  - 出处：RPG v1, Section 2.1.1 explicitly follows Hou et al. (2023) for OPQ: [S2.SS1.SSS1.p1](https://arxiv.org/html/2506.05781v1#S2.SS1.SSS1.p1); Section 2.4.1 identifies the compared model as VQ-Rec: [S2.SS4.SSS1.p1](https://arxiv.org/html/2506.05781v1#S2.SS4.SSS1.p1); Table 2 includes VQ-Rec: [S2.T2](https://arxiv.org/html/2506.05781v1#S2.T2).
- **替代方案** · [LETTER](letter.md): LETTER regularizes a hierarchical RQ-VAE tokenizer for collaborative alignment and code diversity, whereas RPG uses long OPQ codes with parallel prediction to improve inference efficiency.
  - 出处：Manually compared mechanisms, not a head-to-head evaluation: RPG v1, Section 4 cites LETTER (Wang et al., 2024a) among quantization methods: [S4.p2](https://arxiv.org/html/2506.05781v1#S4.p2); Section 2.1.1 gives RPG's OPQ rationale: [S2.SS1.SSS1.p1](https://arxiv.org/html/2506.05781v1#S2.SS1.SSS1.p1); LETTER v1, Section 3.1 defines its regularized hierarchical RQ-VAE tokenizer: [S3.SS1.p1](https://arxiv.org/html/2405.07314v1#S3.SS1.p1) and [S3.SS1.p2](https://arxiv.org/html/2405.07314v1#S3.SS1.p2).

[查看同格全部论文](../../../README.zh.md#v--backbone)
