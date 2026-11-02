# OneRec

*Unifying retrieve and rank with generative recommender and iterative preference alignment* — Deng et al. · arXiv’25

`Paradigms, Systems and Benchmarks` · `No single stage`

[Paper](https://arxiv.org/abs/2502.18965) · [Matrix](../../README.md#paradigms-systems-and-benchmarks)

Reading level: Overview (Level 1) · On this page: [TL;DR](#tldr) · [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | `R-KM` | `Enc-Dec` | `Fixed / NTP → DPO` | `Sess. Beam` |

- `R-KM`: Residual k-means.
- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.

### TL;DR

OneRec replaces the retrieve-and-rank cascade with one encoder-decoder generator using sparse MoE, generates whole sessions of videos, and aligns preferences by iterative DPO with a reward model.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | Paradigms, Systems and Benchmarks: Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| Key Contribution | OneRec replaces the retrieve-and-rank cascade with one encoder-decoder generator using sparse MoE, generates whole sessions of videos, and aligns preferences by iterative DPO with a reward model. |
| Modified Stage | No single stage |

### 2. How It Works

![OneRec architecture diagram](../../architectures/onerec.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Kuaishou short-video interaction logs; training sessions are built from high-quality user sessions (a session is 5-10 videos per request; the listed criteria include at least 5 videos actually watched, total watch time above a threshold whose value is not given, and interactions such as liking, collecting, or sharing). Dataset size: not reported.
  - Source: Industrial Kuaishou data and session construction: https://arxiv.org/html/2502.18965v1#S3.SS2.p1 and https://arxiv.org/html/2502.18965v1#S4.p1; no dataset statistics found.
- **Split**: Offline: evaluation on a randomly sampled set of test cases in each iteration; the train/test construction is not reported. Online: A/B test on Kuaishou's main-page video scenarios with 1% of main traffic.
  - Source: Offline evaluation on randomly sampled test cases: https://arxiv.org/html/2502.18965v1#S5.SS1.SSS3.p1; online: https://arxiv.org/html/2502.18965v1#S5.SS5.p1.
- **Candidates**: n/a for ranking metrics: generated sessions are scored by a pre-trained reward model (session watch time, view, follow, and like probabilities), not ranked against a candidate set.
  - Source: Reward-model evaluation of generated sessions: https://arxiv.org/html/2502.18965v1#S5.SS1.SSS3.p1.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: No unseen-item protocol: https://arxiv.org/html/2502.18965v1#S5.SS1.SSS3.p1.
- **SID**: 3 levels x 8,192 codes from multi-level balanced residual K-means over multimodal video embeddings aligned with user behavior; balanced K-means equalizes cluster sizes. Collision handling: not reported.
  - Source: Balanced residual K-means, L=3 x K=8192: https://arxiv.org/html/2502.18965v1#S3.SS1.p2, https://arxiv.org/html/2502.18965v1#S3.SS1.p3, https://arxiv.org/html/2502.18965v1#S5.SS1.SSS1.p1; no collision rule found.
- **Inference budget**: Beam search with beam size 128 (also used to generate 128 responses per user for DPO); KV-cache decoding with float16 quantization; MoE with 24 experts, 2 active (about 13% of parameters active at inference). Training on NVIDIA A800 GPUs; serving hardware, batch size, and latency: not reported.
  - Source: Beam size 128 online and for DPO sampling; KV cache and float16: https://arxiv.org/html/2502.18965v1#S4.p1 and https://arxiv.org/html/2502.18965v1#S5.SS1.SSS1.p1.
- **Results from**: Table 1 (offline reward-model metrics versus pointwise, listwise, and preference-alignment baselines); Figure 4 (DPO sample ratio); Table 2 (online A/B: OneRec-1B+IPA +1.68% total watch time, +6.56% average view duration).
  - Source: Offline: https://arxiv.org/html/2502.18965v1#S3.T1; DPO ratio: https://arxiv.org/html/2502.18965v1#S5.F4; online: https://arxiv.org/html/2502.18965v1#S5.T2.

## 旧卡片说明

迁自 `d61aa6c:papers/onerec.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### OneRec：检索排序一体化生成式推荐

> OneRec 用生成模型直接产生推荐列表，并通过迭代偏好对齐替代传统的召回-排序级联。

### 研究动机与问题定义

级联系统把召回和排序拆开，模块目标不一致且存在信息损失。OneRec 将会话建模、候选选择和排序统一为列表生成，并研究如何使生成结果贴近真实偏好。

### TL;DR（核心摘要）

`会话历史 → SID列表目标 → 生成模型 → 推荐列表 → 偏好对齐`

模型以会话级物品列表作为训练目标，使用平衡聚类构造物品语义标识，并直接生成列表。训练后通过奖励反馈和迭代 DPO 逐步对齐列表质量；在线阶段生成的 SID 直接对应推荐物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 会话交互、物品标识和偏好反馈 |
| 信息融入位置 | 列表目标、生成输入和偏好训练 |
| 语义标识结构 | 列表中的多 token 序列 |
| 适用场景 | 工业会话推荐 |

### 方法设计

#### 3.1 会话级列表生成
OneRec 把单物品 next-item 目标扩展为 session-wise list generation。训练样本包含会话上下文和目标推荐列表，生成器按统一序列格式输出多个物品 SID，并在列表内部处理顺序与重复。

#### 3.2 生成器训练
模型采用编码器-解码器结构，以会话行为和物品标识作为条件。标识由平衡聚类构造，使不同物品在生成词表中具有较好的覆盖和可区分性。

#### 3.3 迭代偏好对齐
训练后使用奖励模型产生偏好信号，构造列表级偏好样本并进行 DPO。迭代过程不断用更新后的模型生成新样本，使生成列表逐步靠近业务偏好。

#### 3.4 系统部署
论文进一步设计线上生成、去重和服务流程，目标是用一个生成模型连接原本分离的召回与排序阶段。

### 实验结论

- OneRec 在论文报告的公开和工业设置中改善了生成式推荐效果。
- 列表级训练和偏好对齐均带来额外收益。

### 局限性与研究定位

#### 局限性
- 列表生成、去重和约束会增加推理工程复杂度。
- 动态物品、极端长尾和跨场景迁移仍需更多验证。

#### 研究定位
OneRec 的主要贡献是以生成列表统一召回与排序，适合放在“端到端工业生成式推荐”章节。

### 标签

`召回排序一体化` · `列表生成` · `偏好对齐` · `工业推荐`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：统一召回与排序。
- 使用场景：工业会话推荐。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER generates one next item from RQ-VAE semantic IDs; OneRec generates whole sessions with balanced residual K-means IDs, an MoE encoder-decoder, and iterative DPO.
  - Source: OneRec v1, baselines: https://arxiv.org/html/2502.18965v1#S5.I1.i4.p1; Table 1: https://arxiv.org/html/2502.18965v1#S3.T1; tokenizer contrast with RQ-VAE: https://arxiv.org/html/2502.18965v1#S3.SS1.p2.
- **Successor** · [MiniOneRec](minionerec.md): MiniOneRec later reproduces the OneRec-style SID, SFT, and RL pipeline in open source on public data.
  - Source: Evidence is from the later MiniOneRec paper, Section 1: https://arxiv.org/html/2510.24431v1#S1.p1 and https://arxiv.org/html/2510.24431v1#S1.p3.
- **Alternative** · [GFlowGR](gflowgr.md): GFlowGR later compares against OneRec's IPA alignment and replaces it with a GFlowNet objective over reward-weighted trajectories.
  - Source: Evidence is from the later GFlowGR paper: IPA baseline and Table 2: https://arxiv.org/html/2506.16114v3#S4.I2.i6.p1 and https://arxiv.org/html/2506.16114v3#S4.T2.

[View all papers in this cell](../../README.md#paradigms-systems-and-benchmarks)
