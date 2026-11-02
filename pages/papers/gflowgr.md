# GFlowGR

*Fine-Tuning Generative Recommendation Frameworks with Generative Flow Networks* — Wang et al. · SIGIR’26

`IV. Utility` · `Training`

[Paper](https://arxiv.org/abs/2506.16114) · [Code](https://github.com/Applied-Machine-Learning-Lab/SIGIR26_GFlowGR) · [Matrix](../../README.md#iv--training)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text / Text+CF` | `RQ-VAE / Learn. RQ` | `Enc-Dec†` | **`Fixed / NTP + Aux.`** | `Beam† / C-Beam†` |

- `Text / Text+CF`: Text-only representations or text representations combined with collaborative signals.
- `RQ-VAE / Learn. RQ`: Residual-quantized variational codes or learnable residual-quantization codes in different configurations.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Aux.`: NTP plus another auxiliary loss.
- `Beam† / C-Beam†`: Beam search or constrained beam search in the respective inherited configurations.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | IV. Utility: Are training and search aimed at what users and the platform value, rather than at token likelihood? |
| Modified Stage | Training |

### 2. How It Works

![GFlowGR architecture diagram](../../architectures/gflowgr.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Yelp, Amazon Beauty, and Amazon Instruments, preprocessed following LETTER (filter thresholds not restated); 30,431 / 20,032, 22,362 / 12,101, and 24,772 / 9,922 users / items. Production: Taobao search advertising data with hundreds of millions of daily requests; filtering not reported.
  - Source: Datasets and LETTER preprocessing: https://arxiv.org/html/2506.16114v3#S4.SS1.p1; statistics: https://arxiv.org/html/2506.16114v3#S4.T1; production data: https://arxiv.org/html/2506.16114v3#S5.p2.
- **Split**: Per-user leave-one-out: last item for test, second-to-last for validation, the rest for training. Three random seeds. Online: 15-day A/B test on 10% of traffic (50/50).
  - Source: Leave-one-out allocation: https://arxiv.org/html/2506.16114v3#S4.SS1.p1; three seeds: https://arxiv.org/html/2506.16114v3#S4.SS1.p2; online test: https://arxiv.org/html/2506.16114v3#S5.p3.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); top-5 and top-10 lists. Training negatives for the flow objective come from a collaborative-model sampler or beam search, which is a training choice, not the evaluation candidate set.
  - Source: Metrics only: https://arxiv.org/html/2506.16114v3#S4.SS1.p2.
- **Visibility**: warm; no unseen-item protocol is defined. Online, newly listed items gain 4.0% revenue, but their tokenizer and generator visibility is not reported.
  - Source: Standard split with no unseen-item protocol: https://arxiv.org/html/2506.16114v3#S4.SS1.p1; online newly listed items without visibility definition: https://arxiv.org/html/2506.16114v3#S5.p3.
- **SID**: Uses the TIGER and LETTER tokenizers as backbones; layer count and codebook size for the experiments: not reported (Figure 1 illustrates L=3). Collision handling: not reported; the paper notes that intermediate states do not uniquely identify items.
  - Source: Backbones TIGER and LETTER, no own SID settings: https://arxiv.org/html/2506.16114v3#S4.SS1.p2; L=3 appears in the overview figure: https://arxiv.org/html/2506.16114v3#S1.F1.
- **Inference budget**: Decoding method and beam width for evaluation: not reported. All experiments run on the same GPU (model not stated). Table 7 reports training cost on production data (GFlowGR 2.1x SFT with 80x samples); inference latency and batch size: not reported.
  - Source: Hardware statement and cost: https://arxiv.org/html/2506.16114v3#S4.SS1.p3 and https://arxiv.org/html/2506.16114v3#S4.T7.
- **Results from**: Table 2 (Beauty, Instruments, Yelp; SFT, GRPO, DPO-family baselines on TIGER and LETTER backbones); Tables 3-6 (rewards, combination, sample selection, LLM reward); Figures 3-4 (parameter study); Table 7 and Section 5 (production offline and 15-day online A/B).
  - Source: Main: https://arxiv.org/html/2506.16114v3#S4.T2; ablations and strategies: https://arxiv.org/html/2506.16114v3#S4.T3, https://arxiv.org/html/2506.16114v3#S4.T4, https://arxiv.org/html/2506.16114v3#S4.T5, https://arxiv.org/html/2506.16114v3#S4.T6; production: https://arxiv.org/html/2506.16114v3#S4.T7 and https://arxiv.org/html/2506.16114v3#S5.p3.

## 旧卡片说明

迁自 `d61aa6c:papers/gflowgr.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### GFlowGR：生成流网络生成式推荐微调

> GFlowGR 将生成流网络用于生成式推荐微调，使模型从多条可能的生成轨迹中学习更符合推荐价值的物品标识。

### 研究动机与问题定义

最大似然训练倾向于复现日志中的单一路径，难以表达推荐结果的多样性和长期价值。GFlowGR 将 SID 生成过程视为轨迹采样问题，用奖励约束生成分布。

### TL;DR（核心摘要）

`用户历史 → SID生成轨迹 → 奖励模型 → GFlowNet微调 → 推荐物品`

框架从交互日志、随机采样、协同模型或在线策略获得轨迹，并训练奖励模型评估生成结果。GFlowNet 目标在训练阶段调整生成概率；在线仍由生成器直接产生完整 SID 并映射物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 交互日志、协同信号和生成轨迹 |
| 信息融入位置 | 奖励模型与轨迹采样 |
| 语义标识结构 | 多 token 序列 |
| 适用场景 | 偏好对齐与多样化推荐 |

### 方法设计

#### 3.1 轨迹采样器（Trajectory Sampler）
GFlowGR 把 SID 逐 token 生成看作从根节点到完整物品标识的轨迹。轨迹可以来自交互日志、随机策略、协同模型、组合采样或当前生成策略，用于覆盖单一监督路径之外的候选空间。

#### 3.2 奖励模型（Reward Model）
奖励模型评估完整生成结果或中间轨迹的推荐价值，将点击/偏好等信号转成训练奖励。它负责提供 GFlowNet 所需的终点价值，但不作为在线独立精排器。

#### 3.3 GFN 训练目标
模型学习前向生成概率与后向流之间的平衡，使不同高价值 SID 轨迹获得合理概率。该目标鼓励多条有效生成路径共存，缓解最大似然对单一日志目标的过拟合。

#### 3.4 训练与推理
训练阶段交替采样轨迹、计算奖励和更新生成器；推理阶段仍由生成器直接产生 SID。实验还分析不同轨迹来源、参数设置和部署成本。

### 实验结论

- GFlowNet 微调改善了生成推荐的排序表现。
- 不同轨迹来源对训练效果有影响，在线策略轨迹更贴近目标。

### 局限性与研究定位

#### 局限性
- 奖励模型和轨迹采样带来额外训练成本。
- 奖励偏差、探索范围与线上稳定性仍需验证。

#### 研究定位
GFlowGR 的贡献是把生成式推荐的偏好微调改写为生成流学习问题，适合放在“生成轨迹优化与偏好学习”章节。

### 标签

`生成流网络` · `偏好优化` · `SID生成` · `序列推荐`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：用生成流网络进行偏好微调。
- 使用场景：偏好对齐。

### 5. Connections to Related Work

- **Predecessor** · [TIGER](tiger.md): TIGER is one of the two generative backbones; GFlowGR updates the LLM with the sum of the SFT loss and a GFlowNets loss over augmented generation trajectories.
  - Source: GFlowGR v3, Section 4.1 installs GFlowGR on TIGER: https://arxiv.org/html/2506.16114v3#S4.SS1.p2; Table 2: https://arxiv.org/html/2506.16114v3#S4.T2; training objective: https://arxiv.org/html/2506.16114v3#S3.SS4.p1.
- **Predecessor** · [LETTER](letter.md): LETTER supplies the second backbone and the data preprocessing; GFlowGR changes only the fine-tuning objective.
  - Source: GFlowGR v3, Section 4.1 follows LETTER preprocessing and uses it as a backbone: https://arxiv.org/html/2506.16114v3#S4.SS1.p1 and https://arxiv.org/html/2506.16114v3#S4.SS1.p2; Table 2: https://arxiv.org/html/2506.16114v3#S4.T2.
- **Competitor** · [OneRec](onerec.md): OneRec's IPA aligns the model by iterative SFT and DPO with reward-selected rejected samples; GFlowGR learns probabilities proportional to rewards over many trajectories.
  - Source: GFlowGR v3, IPA baseline from OneRec, reimplemented with the same reward model: https://arxiv.org/html/2506.16114v3#S4.I2.i6.p1 and https://arxiv.org/html/2506.16114v3#S4.SS1.p3; Table 2: https://arxiv.org/html/2506.16114v3#S4.T2.

[View all papers in this cell](../../README.md#iv--training)
