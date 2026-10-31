## Positioning in the Problem × Stage Matrix

- **Matrix Cell**: **I. Informativeness** $`\times`$ **Representation** (`problem: I`, `stage: Representation`, `poi: true`).
- **Why Here**: In local-life and point-of-interest (POI) recommendation, item semantics depend jointly on multimodal content and physical geography. OneLoc enriches the **Representation** stage (`Text+Img+Geo†`) before residual $`k`$-means (`R-KM`) tokenization, and couples it with geo-aware encoder self-attention, neighbor-aware decoder prompts, and two-stage `NTP → DPO` optimization with geographic distance and GMV rewards.

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

For each local-life item $`i`$ (a short video linked to a physical store), OneLoc prompts a multimodal large language model (MLLM) with the video frames, textual description, and structured geographic context (city, business district, coordinates) to extract a unified dense representation $`\mathbf{e}_i \in \mathbb{R}^d`$ (`Text+Img+Geo†`).

Following OneRec, OneLoc quantizes $`\mathbf{e}_i`$ into an $`L`$-level discrete Semantic ID $`\mathbf{s}_i = (s_{i,1}, \dots, s_{i,L})`$ via Residual K-Means (`R-KM`, §2.2, Eq. 1–3):

```math
\mathbf{r}_i^{(1)} = \mathbf{e}_i, \qquad s_{i,l} = \arg\min_{k \in \{1,\dots,K\}} \left\| \mathbf{r}_i^{(l)} - \mathbf{c}_k^{(l)} \right\|_2^2, \qquad \mathbf{r}_i^{(l+1)} = \mathbf{r}_i^{(l)} - \mathbf{c}_{s_{i,l}}^{(l)}
```

where $`\mathcal{C}^{(l)} = \{\mathbf{c}_k^{(l)}\}_{k=1}^{K}`$ is the level-$`l`$ centroid matrix trained offline and kept `Fixed` during recommender training.

### Step 2: Geo-Aware Self-Attention & Neighbor-Aware Decoder Prompt

In the encoder (§2.3), given user history items with locations $`\{(\mathbf{h}_j, \ell_j)\}_{j=1}^{T}`$ and the user's real-time location $`\ell_u`$, OneLoc modulates self-attention logits with a gated spatial bias $`\mathbf{B}^{\text{geo}} \in \mathbb{R}^{T \times T}`$ derived from pairwise Haversine distances $`d(\ell_j, \ell_{j'})`$ and user-to-store distances $`d(\ell_u, \ell_j)`$:

```math
\mathrm{Attn}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \mathrm{softmax}\!\left(\frac{\mathbf{Q}\mathbf{K}^\top}{\sqrt{d_k}} + g_u \odot \mathbf{B}^{\text{geo}}\right)\mathbf{V}
```

In the decoder (§2.4), a **Neighbor-Aware Prompt** injects the Semantic IDs of stores within the user's current geohash cell $`\mathcal{N}(\ell_u)`$ as prefix context so the decoder attends directly to physically reachable candidates.

### Step 3: Two-Stage `NTP → DPO` with Geographic and Commercial Rewards

After supervised next-token prediction (`NTP`) pre-training (§2.5, Eq. 20–21), OneLoc samples $`G`$ candidate Semantic IDs $`\{\mathbf{s}^{(1)}, \dots, \mathbf{s}^{(G)}\}`$ via beam search for each user request $`(u, \ell_u)`$ and scores each valid store using a composite reward combining spatial proximity $`R_{\text{geo}}`$ and expected Gross Merchandise Volume $`R_{\text{GMV}}`$:

```math
R(\mathbf{s}, u, \ell_u) = \lambda_{\text{geo}}\, R_{\text{geo}}\!\left(d(\ell_u, \ell_{\mathbf{s}})\right) + \lambda_{\text{GMV}}\, R_{\text{GMV}}(\mathbf{s}, u)
```

Winning-losing pairs $`(\mathbf{s}_w, \mathbf{s}_l)`$ with $`R(\mathbf{s}_w) \gt R(\mathbf{s}_l)`$ optimize the Direct Preference Optimization (`DPO`, §2.5, Eq. 24) objective relative to the reference NTP policy $`\pi_{\text{ref}}`$:

```math
\mathcal{L}_{\text{DPO}}(\theta) = -\mathbb{E}_{(x, \mathbf{s}_w, \mathbf{s}_l)} \left[ \log \sigma\!\left( \beta \log \frac{\pi_\theta(\mathbf{s}_w \mid x)}{\pi_{\text{ref}}(\mathbf{s}_w \mid x)} - \beta \log \frac{\pi_\theta(\mathbf{s}_l \mid x)}{\pi_{\text{ref}}(\mathbf{s}_l \mid x)} \right) \right]
```

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

- **Datasets & Deployment**: Evaluated on industrial Kuaishou local-life service logs and deployed in online A/B testing serving $`\sim 400\text{M}`$ daily active users.
- **Reported Gains** (§3.2–3.4 of the paper):
  - **Online A/B Test**: Reports **+21.016% GMV** and **+17.891% order volume** over the production multi-stage local-life ranking baseline.
  - **Module Ablations**: Removing geo-aware SIDs, geo-aware self-attention, neighbor-aware prompts, or either DPO reward (`Geo` / `GMV`) degrades both offline hit rate and distance compliance.

---

## Limitations & Comparison with Peer POI Methods in `I. Informativeness`

1. **Implicit vs. explicit spatial prefix in SIDs**: OneLoc injects location context into the MLLM embedding before `R-KM` (`Text+Img+Geo†`), so spatial hierarchy is not guaranteed to align with individual code positions. Within the same cell (`I. Informativeness` $`\times`$ `Representation`), **`LGSID`** (`Geo-Idx+RQ`) and **`GeoGR`** (`R-KM+EM`) explicitly couple spatial/grid structure or EM-updated geographic alignment with collaborative signals (`Text+Geo+CF`), while **`LGRID`** (`DSRQ`) disentangles semantic and geographic latent spaces.
2. **Closed industrial evaluation**: Evaluation relies on proprietary short-video local-life logs and business GMV estimators without a public reproducibility benchmark.

---

## 旧卡片说明

迁自 `d61aa6c:papers/oneloc.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### OneLoc：面向本地生活服务的地理感知生成式推荐

> OneLoc 将地理感知 SID、位置自注意力和邻域提示结合到端到端生成式推荐中，并用地理与 GMV 奖励平衡兴趣和距离目标。

### 研究动机与问题定义

本地生活推荐既要满足用户兴趣，也要考虑用户实时位置、商户距离和业务价值。传统模型通常将地理特征作为额外输入，难以在端到端生成中同时控制这些目标。OneLoc 直接生成本地生活 POI/商户的语义 token，并研究其在 Kuaishou 本地生活场景中的部署方式。

### TL;DR（核心摘要）

`用户行为/视频/位置 → 地理感知SID → 地理自注意力编码 → 邻域提示解码 → 商户推荐`

OneLoc 用视频和地理信息构造语义 token，在编码器中利用历史商户位置与实时位置调节注意力，在解码器中加入周边商户提示。监督训练后，模型通过地理奖励和 GMV 奖励构造偏好对并进行 DPO 式强化学习，生成 token 直接对应推荐商户。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户行为、视频内容、历史位置、实时位置、邻域商户和 GMV |
| 信息融入位置 | SID、编码器注意力、解码提示和强化学习奖励 |
| 语义标识结构 | 多 token 离散序列 |
| 适用场景 | 本地生活服务推荐和工业部署 |

### 方法设计

#### 2.2 地理感知语义标识
OneLoc 将视频内容 token 与地理 token 共同用于商户/内容表示，使生成器看到的离散标识同时包含语义和位置线索。论文强调，位置并非简单拼接的连续特征，而是参与物品 token 化。

#### 2.3 编码器
编码器接收用户历史行为、历史商户位置和实时位置。Geo-aware Self-Attention 根据行为内容相似性、历史位置关系以及用户当前地点计算注意力，并以门控方式调节位置上下文的影响。

#### 2.4 解码器与邻域提示
解码器采用带因果自注意力和交叉注意力的生成结构。Neighbor-aware Prompt 将用户实时位置周围的地理网格、邻近商户和位置提示加入解码过程，使生成结果更符合本地可达性。

#### 2.5 强化学习
监督训练得到初始模型后，OneLoc 从模型分布采样多个视频/商户结果。地理奖励衡量距离约束，GMV 奖励反映业务价值，再按奖励排序构造偏好对，用 DPO 更新模型。

### 实验结论

- 离线实验和在线 A/B 测试均报告了相对生产基线的收益；论文报告日活约 4 亿用户场景下 GMV 和订单数分别提升 21.016% 与 17.891%。
- 地理自注意力、邻域提示以及两类奖励的消融结果支持这些模块对效果的贡献。
- 论文展示了系统部署框架，但稿件中的会议元数据仍为占位文本，正式发表信息未确认。

### 局限性与研究定位

#### 局限性

- 多目标奖励权重和偏好数据构造依赖具体业务，跨平台复现难度较高。
- POI 动态更新、生成非法商户以及候选覆盖率的处理细节未充分报告。

#### 研究定位

OneLoc 代表将 Semantic ID 生成式推荐推进到本地生活工业场景的路线，适合放在“地理约束与多目标生成推荐”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2508.14646)

### 标签

`本地生活` · `地理感知` · `邻域提示` · `强化学习`

### 架构图来源

*图源：原论文，图2。论文页面信息未完整报告，图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：用地理感知生成和偏好优化统一本地生活目标。
- 使用场景：本地生活推荐。
