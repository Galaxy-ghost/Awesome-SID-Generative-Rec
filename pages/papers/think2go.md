# Think2Go

*Generative Next POI Recommendation with LLM Reasoning* — Zhuang et al. · KDD’26

`III. SID–Model Alignment` · `Training` · `POI`

[Paper](https://arxiv.org/abs/2607.28997) · [Code](https://doi.org/10.5281/zenodo.18206701) · [Matrix](../../README.md#iii--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Attr+Geo+CF†` | `RQ-VAE` | `Dec-Only` | **`Fixed / NTP → RL`** | `CoT+Beam` |

- `Attr+Geo+CF†`: Structured item attributes, geographic information, and collaborative signals (inferred).
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `CoT+Beam`: Reasoning followed by beam-search decoding.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Training |

### 2. How It Works

![Think2Go architecture diagram](../../architectures/think2go.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Foursquare NYC and TKY (April 2012-February 2013) and Gowalla CA (February 2009-October 2010), preprocessed as in GNPR-SID: POIs with fewer than 10 interactions and users with fewer than 10 check-ins removed. Sizes (users / POIs): NYC 1,083 / 5,135; TKY 2,293 / 7,873; CA 6,592 / 14,027.
  - Source: Datasets and GNPR preprocessing: https://arxiv.org/html/2607.28997v1#S5.SS1.p1; statistics: https://arxiv.org/html/2607.28997v1#S5.T1.
- **Split**: Records sorted chronologically and split 80% / 10% / 10% for training, validation, and test; for each user the last check-in is the answer. Separate cross-city transfer test (Table 5).
  - Source: Temporal 80/10/10 with last check-in as answer: https://arxiv.org/html/2607.28997v1#S5.SS1.p1; cross-domain: https://arxiv.org/html/2607.28997v1#S5.T5.
- **Candidates**: not reported (full catalog versus sampled); Acc@1, 5, 10 and MRR over the predicted top-K POIs.
  - Source: Acc@K and MRR over predicted lists: https://arxiv.org/html/2607.28997v1#S5.SS3.p1.
- **Visibility**: warm; users and POIs that do not appear in training are removed from the test set. The cross-city transfer (Table 5) tests POIs of another city; their tokenizer exposure is not reported.
  - Source: Test users and POIs absent from training removed: https://arxiv.org/html/2607.28997v1#S5.SS1.p1.
- **SID**: Listwise semantic IDs built with RQ-VAE, which the paper contrasts with the pointwise semantic IDs of GNPR; numerical levels, codebook sizes, and collision handling: not reported.
  - Source: Listwise semantic IDs whose correlations are learned through RQ-VAE, contrasted with GNPR's pointwise IDs: https://arxiv.org/html/2607.28997v1#S5.SS5.p2; numerical settings not found.
- **Inference budget**: Reasoning generated with vLLM (max length 1,024, temperature 1.3, 4 rollouts, beam search width 10) before the POI SID; LLaMA3.1-8B with LoRA. Five NVIDIA L40s GPUs (four for training, one for rollout inference); latency: not reported.
  - Source: Rollout and decoding settings, hardware: https://arxiv.org/html/2607.28997v1#A1.p1.
- **Results from**: Table 2 (NYC, TKY, CA versus traditional, sequence, GCN, LLM, and reasoning baselines); Table 3 (ablations); Table 4 (SID category prediction versus GNPR); Table 5 (cross-city generalization).
  - Source: Main: https://arxiv.org/html/2607.28997v1#S5.T2; ablation: https://arxiv.org/html/2607.28997v1#S5.T3; SID understanding: https://arxiv.org/html/2607.28997v1#S5.T4; cross-domain: https://arxiv.org/html/2607.28997v1#S5.T5.

## 旧卡片说明

迁自 `d61aa6c:papers/think2go.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### Think2Go：带大语言模型推理的生成式下一兴趣点推荐

> Think2Go 将监督微调和强化学习推理统一到自回归生成中，通过自纠错和自适应优势校准提升 LLM 对 POI SID 的理解。

### 研究动机与问题定义

用户移动轨迹具有稀疏、周期和多步空间规律，单步生成可能难以捕获深层意图。另一方面，独立训练的 SID 对 LLM 来说只是符号序列，模型未必理解 token 的类别和空间意义。Think2Go 研究如何让生成模型在输出下一 POI SID 前进行可控推理，并保持对行为模式的记忆。

### TL;DR（核心摘要）

`用户历史SID/时间 → Think → Self-Correct → Answer SID`

Think2Go 在一个自回归框架中同时训练推理轨迹和最终答案。监督微调先教模型生成思考与 SID，强化学习再用答案奖励更新推理过程；Prompt epistemic uncertainty（提示认知不确定性）鼓励难例探索，reward-informed advantage scaling（奖励感知优势缩放）调节不同难度样本的更新幅度。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户历史 SID、时间信息和 POI 生成结果 |
| 信息融入位置 | 推理提示、答案监督和奖励校准 |
| 语义标识结构 | 多级离散序列 |
| 适用场景 | 下一 POI、跨域泛化和推理增强推荐 |

### 方法设计

#### 4.1 模型架构
模型接收带时间的用户历史和目标上下文，输出 reasoning、Self-Correct 和 Answer 三类 token。Answer 是最终 POI SID，reasoning 用于表达用户偏好和时空判断，Self-Correct 连接推理阶段与监督答案阶段。

#### 4.2 自适应优势校准
作者指出只用普通优势估计可能造成不同难度样本更新幅度相同，或因估计偏差抑制探索。Think2Go 用核密度估计当前提示与用户历史的时空周期匹配程度，得到提示认知不确定性，并据此调节优势权重。

#### 4.2.2 奖励感知缩放
奖励被相对于同组样本最大值归一化，用于缩放策略梯度。高价值且难度合适的样本得到更有效更新，减少噪声奖励导致的过拟合和策略熵塌缩。

#### 4.2.3 规则奖励与训练目标
规则奖励综合答案 SID 正确性、格式合法性和时空行为匹配。模型在自回归推理轨迹上计算奖励，并用校准后的策略优化目标更新；这种设计形成隐式课程学习。

#### 附录：自纠错与零样本 SID 语义预测
附录给出 Self-Correct 提示格式和零样本类别预测任务。模型在答案错误时生成修正建议；类别预测实验用于检查微调和强化学习后，SID 是否承载可恢复的语义信息。

### 实验结论

- 三个真实数据集上的实验显示 Think2Go 能提升生成式下一 POI 推荐效果和 SID 语义理解。
- 优势校准、推理轨迹和自纠错的消融支持其对探索与训练稳定性的贡献。
- 相比基于完整文本提示的推理方法，论文报告 Think2Go 在训练时间、测试时间和显存占用上更高效。

### 局限性与研究定位

#### 局限性

- 推理轨迹增加输出长度和推理成本，效果与效率之间需要按场景权衡。
- 规则奖励和核密度不确定性估计依赖数据分布，跨城市和极少行为用户的可靠性仍需验证。

#### 研究定位

Think2Go 适合放在“推理增强的语义标识生成推荐”章节，重点体现将 SID 理解、显式推理和自适应强化学习结合起来。

### 相关资源

- [论文原文](https://arxiv.org/abs/2607.28997)

### 标签

`下一兴趣点推荐` · `推理增强` · `强化学习` · `自纠错`

### 架构图来源

*图源：原论文，图1（[论文原文](https://arxiv.org/abs/2607.28997)）。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：统一 SFT、推理、自纠错与自适应强化学习。
- 使用场景：下一 POI 推荐。

### 5. Connections to Related Work

- **Competitor** · [GNPR-SID](gnpr-sid.md): GNPR-SID trains SID knowledge by SFT alone; Think2Go adds reasoning tokens and advantage-calibrated GRPO over the same kind of POI semantic IDs and generalizes better across cities.
  - Source: Think2Go v1, LLM-based baselines and preprocessing: https://arxiv.org/html/2607.28997v1#S5.SS2.p4 and https://arxiv.org/html/2607.28997v1#S5.SS1.p1; Tables 2, 4, 5: https://arxiv.org/html/2607.28997v1#S5.T2, https://arxiv.org/html/2607.28997v1#S5.T4, https://arxiv.org/html/2607.28997v1#S5.T5.
- **Alternative** · [OneRec-Think](onerec-think.md): OneRec-Think adds reasoning to industrial video recommendation; Think2Go applies RL-trained reasoning to next-POI prediction with SIDs.
  - Source: Think2Go v1, Section 2.2 cites OneRec-Think: https://arxiv.org/html/2607.28997v1#S2.SS2.p1.
- **Alternative** · [OneLoc](oneloc.md): OneLoc is a geo-aware generative recommender trained without explicit reasoning; Think2Go relies on reasoning to use spatial context.
  - Source: Think2Go v1, Section 1 cites OneLoc: https://arxiv.org/html/2607.28997v1#S1.p4.

[View all papers in this cell](../../README.md#iii--training)
