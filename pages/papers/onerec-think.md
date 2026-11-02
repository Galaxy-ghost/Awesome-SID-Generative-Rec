# OneRec-Think

*In-text reasoning for generative recommendation* — Liu et al. · arXiv’25

`III. SID–Model Alignment` · `Training`

[Paper](https://arxiv.org/abs/2510.11639) · [Code](https://github.com/wangshy31/OneRec-Think) · [Matrix](../../README.md#iii--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF†` | `R-KM†` | `Dec-Only` | **`Fixed / NTP → RL`** | `CoT` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `CoT`: Chain-of-thought before the SID.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Training |

### 2. How It Works

![OneRec-Think architecture diagram](../../architectures/onerec-think.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Beauty, Toys, and Sports; users and items with fewer than 5 interactions are discarded. Industrial: Kuaishou short-video data with daily incremental training on about 20B tokens per day. Retained corpus sizes: not reported.
  - Source: Public datasets: https://arxiv.org/html/2510.11639v2#S5.SS1.p2; filtering and split: https://arxiv.org/html/2510.11639v2#A1.SS1.SSS0.Px2.p1; industrial deployment: https://arxiv.org/html/2510.11639v2#S5.SS4.SSS2.Px1.p1.
- **Split**: Public: leave-one-out (allocation not restated beyond the label); training histories capped at 50 items. Online: one-week A/B test with a 1.29% traffic group.
  - Source: Leave-one-out and history cap: https://arxiv.org/html/2510.11639v2#A1.SS1.SSS0.Px2.p1; online test: https://arxiv.org/html/2510.11639v2#S5.SS4.SSS2.Px1.p1.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); top-K lists from beam search with width 10.
  - Source: Metrics only: https://arxiv.org/html/2510.11639v2#S5.SS1.p2.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2510.11639v2#A1.SS1.SSS0.Px2.p1.
- **SID**: Public: four-level hierarchical semantic IDs with 256 tokens per level (1,024 new tokens). Industrial: three levels x 8,192 itemic tokens (24,576 new tokens), plus item boundary tokens. The tokenizer algorithm is not restated; collision handling: not reported.
  - Source: Public 4 levels x 256; industrial 3 levels x 8,192: https://arxiv.org/html/2510.11639v2#A1.SS1.SSS0.Px2.p1 and https://arxiv.org/html/2510.11639v2#S5.SS4.SSS1.p1; no collision rule found.
- **Inference budget**: Public: beam search with width 10 after the reasoning text (Qwen3-1.7B). Industrial: Think-Ahead serving generates the reasoning and the first two itemic tokens offline with Qwen-8B, then a real-time OneRec model completes the last token online; latency numbers: not reported. Daily training on a cluster of 80 GPUs.
  - Source: Beam width 10 for public evaluation: https://arxiv.org/html/2510.11639v2#A1.SS1.SSS0.Px2.p1; Rollout-Beam reward with width K: https://arxiv.org/html/2510.11639v2#S4.SS3.p2; two-stage serving: https://arxiv.org/html/2510.11639v2#S4.SS4.p2; training cluster: https://arxiv.org/html/2510.11639v2#S5.SS4.SSS1.p1.
- **Results from**: Table 1 (Beauty, Toys, Sports versus sequential and generative baselines); Table 2 (alignment and reasoning ablation on Beauty); Table 3 (online A/B); Table 4 (user and video understanding BertScore).
  - Source: Public: https://arxiv.org/html/2510.11639v2#S4.T1; ablation: https://arxiv.org/html/2510.11639v2#S5.T2; online: https://arxiv.org/html/2510.11639v2#S5.T3; understanding benchmarks: https://arxiv.org/html/2510.11639v2#S5.T4.

## 旧卡片说明

迁自 `d61aa6c:papers/onerecthink.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### OneRec-Think：文本内推理生成式推荐

> OneRec-Think 在物品标识生成前加入用户偏好推理，并用多任务对齐和强化学习提升推荐质量与可解释性。

### 研究动机与问题定义

生成式推荐能够直接预测物品标识，但通常缺少可观察的偏好推理。OneRec-Think 试图让 LLM 在同一自回归过程中先形成理由，再生成目标 itemic token，同时兼顾工业响应速度。

### TL;DR（核心摘要）

`用户历史与itemic token → 多任务对齐 → 偏好理由 → 生成itemic token → 推荐物品`

框架包含 itemic alignment、reasoning activation 和 reasoning enhancement 三阶段。多任务预训练融合用户画像、序列偏好、物品描述生成和通用语言建模；随后从裁剪历史中引导理由生成，并用推荐奖励强化推理路径。Think-Ahead 架构将部分推理前置，最终 token 直接对应物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户行为、用户画像、物品文本和偏好反馈 |
| 信息融入位置 | itemic token 对齐、推理文本和奖励目标 |
| 语义标识结构 | 推理序列后接 itemic token 序列 |
| 适用场景 | 工业序列推荐和可解释推荐 |

### 方法设计

#### 4.1 多任务 Itemic 对齐预训练
OneRec-Think 将 itemic token 与文本 token 放进同一语言空间，训练用户画像、序列偏好、itemic dense captioning 和通用语言建模四类任务。Token warm-up 先学习 itemic embedding，再进行多任务联合整合。

#### 4.2 推理激活
为应对工业行为序列噪声，模型先从裁剪后的相关历史中生成偏好理由，再把这些理由蒸馏到原始行为上下文。推理目标不是独立解释，而是为后续 itemic token 生成提供中间偏好结构。

#### 4.3 推理增强
模型生成多条 reasoning rollout，并用推荐特定奖励比较目标一致性、路径质量和结果可靠性。强化学习进一步筛选能够导向有效 itemic token 的推理路径。

#### 4.4 Think-Ahead 部署架构
论文将部分推理工作前置或离线化，在线阶段快速读取增强后的上下文并生成目标 itemic token，从而在可解释性和工业响应时间之间折中。

### 实验结论

- OneRec-Think 在多个公开基准上报告了较强推荐表现。
- 三阶段训练分别改善语义对齐、推理激活和偏好一致性。
- Think-Ahead 在工业部署中报告了停留时长收益。

### 局限性与研究定位

#### 局限性
- 文本推理增加 token 数量和训练、推理成本。
- 推理奖励依赖用户行为代理信号，可能存在偏差。
- 复杂场景下的实时推理稳定性仍需更多公开验证。

#### 研究定位
OneRec-Think 将显式文本推理嵌入直接 itemic token 生成，适合放在“推理增强生成式推荐”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2510.11639)

### 标签

`文本内推理` · `多任务预训练` · `Think-Ahead` · `偏好强化学习`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：在生成物品标识前加入文本内推理。
- 使用场景：工业推荐。

### 5. Connections to Related Work

- **Competitor** · [TIGER](tiger.md): TIGER generates the next itemic tokens directly; OneRec-Think first generates interleaved text-and-item reasoning and is rewarded with a beam-based signal.
  - Source: OneRec-Think v2, baselines: https://arxiv.org/html/2510.11639v2#S5.SS1.p2 and https://arxiv.org/html/2510.11639v2#A1.SS1.SSS0.Px1.p1; Table 1: https://arxiv.org/html/2510.11639v2#S4.T1.
- **Alternative** · [LC-Rec](lc-rec.md): LC-Rec aligns LLMs to item indices with auxiliary tasks; OneRec-Think adds itemic-textual alignment followed by reasoning activation and RL.
  - Source: OneRec-Think v2, Section 3 and Appendix A.1 cite Zheng et al. (2024): https://arxiv.org/html/2510.11639v2#S3.SS0.SSS0.Px2.p2 and https://arxiv.org/html/2510.11639v2#A1.SS1.SSS0.Px2.p1; not a baseline in Table 1.
- **Alternative** · [GRLM](grlm.md): GRLM later compares against OneRec-Think and replaces numeric itemic tokens with natural-language term IDs.
  - Source: Evidence is from the later GRLM paper: LLM-based baselines and Table 2: https://arxiv.org/html/2601.06798v1#S4.I1.i3.p1 and https://arxiv.org/html/2601.06798v1#S5.T2.

[View all papers in this cell](../../README.md#iii--training)
