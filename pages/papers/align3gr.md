# Align3GR

*Align$^3$GR: Unified Multi-Level Alignment for LLM-based Generative Recommendation* — Ye et al. · AAAI’26

`III. SID–Model Alignment` · `Tokenization`

[Paper](https://arxiv.org/abs/2511.11255) · [Matrix](../../README.md#iii--tokenization)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [3. Experimental Findings](#3-experimental-findings) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+CF` | **`Dual RQ`** | `Dec-Only` | `Fixed / NTP → DPO` | `Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → DPO`: NTP, then preference optimization.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | III. SID–Model Alignment: Can the generator read, write, and reason over SIDs, and do the tokenizer and generator work toward the same goal? |
| Modified Stage | Tokenization |

### 2. How It Works

![Align3GR architecture diagram](../../architectures/align3gr.png)

### 3. Experimental Findings

**Experimental setup**

- **Datasets**: Amazon Instruments, Amazon Beauty, and Yelp; users and items with fewer than 5 interactions are filtered. Retained corpus sizes: not reported in the body. Industrial: internal data from a large-scale advertising recommendation platform; filtering not reported.
  - Source: Datasets, 5-interaction filter, leave-one-out, history cap: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p1; industrial platform: https://arxiv.org/html/2511.11255v2#Sx4.SSx3.p1.
- **Split**: Leave-one-out into training, validation, and test; histories capped at the 20 most recent items. The exact position allocation is not reported beyond the leave-one-out label. Online: 10% of traffic (about 40+ million users) over multiple weeks.
  - Source: Leave-one-out and 20-item cap: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p1 and https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p3; online traffic: https://arxiv.org/html/2511.11255v2#Sx4.SSx3.p1.
- **Candidates**: not reported (full catalog versus sampled evaluation candidates); industrial retrieval reports Recall@100.
  - Source: Metrics and beam width only: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p3.
- **Visibility**: warm; no unseen-item protocol is defined.
  - Source: Standard leave-one-out with no cold-start experiment: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p1.
- **SID**: Item SCID: 3-level RQ-VAE x 256 codewords (dimension 32) over concatenated semantic (T5) and collaborative (DIN) embeddings; users receive their own SCIDs from a separate user RQ-VAE. Both are added to the LLM vocabulary. Collision handling: not reported.
  - Source: 3-level RQ-VAE x 256 codes of dimension 32, user and item SCIDs added to the vocabulary: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p4; dual user/item tokenizer: https://arxiv.org/html/2511.11255v2#Sx3.SSx2.p2 and https://arxiv.org/html/2511.11255v2#Sx3.SSx2.p4.
- **Inference budget**: Beam search with beam width 20 for generative methods (following EAGER-LLM); Recall and NDCG at K=5 and 10. All experiments use 4 NVIDIA GPUs (model not stated); inference batch size and latency: not reported. Backbone: Llama2-7B with LoRA.
  - Source: Beam width 20 following EAGER-LLM: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p3; 4 GPUs for all experiments: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p4.
- **Results from**: Table 1 (Instruments, Beauty, Yelp; averages over five seeds); Table 2 (industrial Recall@100 and online revenue versus a two-tower baseline and TIGER); Tables 3-5 and Figure 4 (tokenization, SFT-task, and DPO ablations).
  - Source: Main table: https://arxiv.org/html/2511.11255v2#Sx3.T1; industrial: https://arxiv.org/html/2511.11255v2#Sx4.T2; ablations: https://arxiv.org/html/2511.11255v2#Sx4.T3, https://arxiv.org/html/2511.11255v2#Sx4.T4, https://arxiv.org/html/2511.11255v2#Sx4.T5; five seeds: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p4.

## 旧卡片说明

迁自 `d61aa6c:papers/align3gr.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### Align3GR：多层统一对齐生成式推荐

> Align3GR 在 token、行为建模和偏好三个层面联合对齐语义与协同信息，使 LLM 直接生成结构化协同语义标识。

### 研究动机与问题定义

既有方法往往只在输入或输出层面对齐语义和协同信号，难以同时保持标识可解释性与行为偏好。Align3GR 将对齐拆为三个相互衔接的层面，并以渐进式偏好优化完成训练。

### TL;DR（核心摘要）

`用户/物品信息 → SCID与协同表示 → 三层对齐 → LLM生成SCID → 推荐物品`

模型先用语义和协同编码器构造层次化 SCID，再进行 token-level alignment；行为建模层加入用户/物品协同损失与索引-语言任务；最后用自博弈式渐进 DPO 注入真实反馈偏好。生成 SCID 直接确定物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 用户交互、物品文本语义和协同表示 |
| 信息融入位置 | SCID 构建、行为目标和偏好优化 |
| 语义标识结构 | 层次化序列 |
| 适用场景 | 公共数据集与工业数据集推荐 |

### 方法设计

#### 3.1 层次化 SCID 构建
Align3GR 为用户和物品分别构造语义-协同标识。语义编码器提供内容信息，协同编码器提供行为信息，RQ-VAE 将两者转为层次化 SCID，并以 token-level alignment 约束对应表示。

#### 3.2 行为建模层对齐
在基础 next-item 生成之外，模型加入用户/物品重构、行为建模和显式索引-语言对齐任务。SCID 被放入任务提示和生成序列，使语言模型学习标识 token 与推荐行为之间的对应关系。

#### 3.3 偏好层对齐
论文采用 Progressive DPO，从较容易的偏好样本逐步过渡到更困难样本。SP-DPO 使用自博弈生成偏好对，RF-DPO 再结合真实反馈校正模型，使优化目标从离线生成质量逐渐接近真实推荐偏好。

#### 3.4 训练与推理
模型先进行多任务监督微调，再执行渐进式偏好优化。在线阶段直接自回归生成完整 SCID，并通过标识词表解析为物品。

### 实验结论

- 多层对齐整体优于只做单层对齐的设置。
- 论文报告了公共和工业数据上的一致收益，并验证了渐进式偏好优化。

### 局限性与研究定位

#### 局限性
- 训练流程较复杂，依赖多种对齐数据和反馈构造。
- 线上部署成本、动态物品和更开放物品空间仍缺少充分验证。

#### 研究定位
Align3GR 的贡献是把语义-协同对齐从单点扩展为多层训练协议。它适合放在“生成式推荐对齐与偏好优化”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2511.11255)

### 标签

`多层对齐` · `SCID` · `渐进式DPO` · `生成式推荐`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：在三层面统一对齐。
- 使用场景：公共与工业推荐。

### 5. Connections to Related Work

- **Competitor** · [EAGER-LLM](eager-llm.md): EAGER-LLM aligns item tokens with collaborative signals; Align3GR also tokenizes users and adds progressive self-play and real-feedback DPO.
  - Source: Align3GR v2, Experimental Settings baselines (13) and beam-width protocol: https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p2 and https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p3; Table 1: https://arxiv.org/html/2511.11255v2#Sx3.T1.
- **Competitor** · [LC-Rec](lc-rec.md): LC-Rec aligns LLMs to item codes with auxiliary tasks; Align3GR adds dual user-item SCIDs and preference-level DPO on top of multi-task SFT.
  - Source: Align3GR v2, baselines (11): https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p2; Table 1: https://arxiv.org/html/2511.11255v2#Sx3.T1.
- **Competitor** · [LETTER](letter.md): LETTER learns a regularized item tokenizer; Align3GR fuses semantic and collaborative features for both users and items through a U2I loss.
  - Source: Align3GR v2, baselines (12): https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p2; Table 1: https://arxiv.org/html/2511.11255v2#Sx3.T1.
- **Competitor** · [TIGER](tiger.md): TIGER uses content-only RQ-VAE item codes with a small Transformer; Align3GR uses an LLM backbone with dual SCIDs and DPO.
  - Source: Align3GR v2, baselines (10): https://arxiv.org/html/2511.11255v2#Sx4.SSx1.p2; Table 1: https://arxiv.org/html/2511.11255v2#Sx3.T1; industrial Table 2: https://arxiv.org/html/2511.11255v2#Sx4.T2.

[View all papers in this cell](../../README.md#iii--tokenization)
