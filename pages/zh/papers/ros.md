# ROS

*Reasoning Over Space: Enabling Geographic Reasoning for LLM-Based Generative Next POI Recommendation* — Lv et al. · ACL’26

`I. 信息量` · `Tokenization` · `POI` · [论文](https://arxiv.org/abs/2601.04562) · [代码](https://github.com/amap-cvlab/Reasoning-Over-Space) · [矩阵](../../../README.zh.md#i--tokenization) · [English](../../papers/ros.md)

阅读级别：阅读笔记（第 2 级） · 本页目录：[TL;DR](#tldr) · [速览](#速览) · [1. 为什么重要](#1-为什么重要) · [2. 方法](#2-方法) · [3. 实验发现](#3-实验发现) · [4. 局限与分析](#4-局限与分析) · [5. 相关工作](#5-相关工作)

```mermaid
flowchart LR
    R["Representation<br/>Text+Geo"] --> T["Tokenization<br/>Geo-Prefix+RQ-VAE"] --> B["Backbone<br/>Dec-Only"] --> TR["Training<br/>Fixed / NTP → RL"] --> I["Inference<br/>CoT+C-Beam"]
    classDef main fill:#eaf2fb,stroke:#6b8fc7
    class T main
```

- `Geo-Prefix+RQ-VAE`: Geographic prefixes combined with residual-quantized variational codes.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `CoT+C-Beam`: Reasoning followed by constrained beam-search decoding.

### TL;DR

> [!NOTE]
> ROS 为基于 LLM 的下一 POI 生成加入层级空间 SID、带局部性剪枝的移动思维链以及空间引导强化学习。

### 速览

| 维度 | 摘要 |
| :-- | :-- |
| 研究问题 | I. 信息量：Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| 核心贡献 | ROS 为基于 LLM 的下一 POI 生成加入层级空间 SID、带局部性剪枝的移动思维链以及空间引导强化学习。 |
| 主要改动阶段 | Tokenization |
| 主要发现 | 在 NYC 上，ROS 的 HR@1 为 0.4478，CoAST 为 0.4027（+11.2%）；在 TKY 和 Gowalla-CA 上，比最强的 LLM 基线分别高 +11.0% 和 +15.7%（Table 1）。 |
| 局限 | 单调先验认为短时间内的远距离移动不太可能，所以 ROS 可能低估乘地铁或走高速的快速长途出行，交通枢纽附近尤其如此（Limitations）。 |

### 1. 为什么重要

基于 LLM 的生成式推荐器很少用地理信号，而在出行和本地服务场景里地理很重要（Abstract）。ROS 把下一次到访看作一串受时间、意图和地理约束的决策（Sec. 2.3）。它用层级空间语义 ID（Semantic ID，SID）表示每个 POI，SID 同时编码所在区域和 POI 语义（Abstract）。

> "We present ROS, a generative next POI recommendation framework that treats geography as an explicit decision variable."（Sec. 5）（ROS 把地理当作显式的决策变量。）

### 2. 方法

![ROS architecture diagram](../../../architectures/ros.png)

```mermaid
flowchart LR
    A[签到数据] --> B[空间 SID]
    B --> C[SID 落地]
    C --> D[出行思维链]
    D --> E[空间引导 RL]
    E --> F[下一个 POI]
```

#### 层级空间 SID

每个 POI 的 SID 由地理前缀、语义锚点和区分后缀三部分组成（Sec. 2.2.1）。地理前缀取 POI 的 S2 Cell ID，写成十六进制数字，去掉所有 POI 共有的前缀，再把剩下的数字分组成 token。语义锚点用 Qwen-0.6B 嵌入 POI 的品类描述，再用 RQ-VAE 量化。

#### SID 落地

双向对齐训练模型从文本预测 SID，也从 SID 生成文本（Sec. 2.2.2）。

> "This bidirectional alignment grounds SID tokens in functional semantics and fine-grained neighborhood cues."（Sec. 2.2.2）（双向对齐让 SID token 带上功能语义和细粒度的街区信息。）

之后的序列预训练在 SID 序列上做下一 POI 预测，模型学到近期性、品类重复和街区连续性。

#### 出行思维链

模型按三个确定的阶段推理：刻画用户；构建与意图一致的候选空间；剪枝候选（Sec. 2.3）。剪枝依据时间一致性、语义匹配，以及由街道地址和转移距离判断的空间可达性。

#### 空间引导的强化学习

GRPO 优化一个统一奖励（Sec. 2.4.3）。奖励由三部分组成：预测 POI 与真实 POI 之间的 Haversine 距离（Sec. 2.4.1），带完全匹配奖励的层级 SID 匹配（Sec. 2.4.2），以及格式项。

### 3. 实验发现

<details>
<summary>实验设置</summary>

- **数据集**：Foursquare NYC and TKY, Gowalla CA, prepared with the LLM4POI pipeline: users and POIs with fewer than 10 check-ins removed, trajectories segmented by a 24-hour time-gap threshold, and street-level addresses added by reverse geocoding. Sizes after preprocessing (users / POIs / check-ins): NYC 1,048 / 4,981 / 103,941; TKY 2,282 / 7,833 / 405,000; CA 3,957 / 9,690 / 238,369.
  - 出处：Datasets and LLM4POI pipeline: [S3.SS1.p1](https://arxiv.org/html/2601.04562v2#S3.SS1.p1); 24-hour gap and sizes: [A1.T10](https://arxiv.org/html/2601.04562v2#A1.T10).
- **切分**：Temporal 80% / 10% / 10% train/validation/test split. Separate cross-city test: train on one city and evaluate on others.
  - 出处：Temporal 80/10/10 split keeping test users and POIs observed: [S3.SS1.p1](https://arxiv.org/html/2601.04562v2#S3.SS1.p1); cross-city: [S3.T6](https://arxiv.org/html/2601.04562v2#S3.T6).
- **候选集**：n/a for candidate ranking: the model outputs exactly one POI per request and is scored by HR@1.
  - 出处：One recommendation per request, HR@1: [S3.SS1.SSS0.Px2.p1](https://arxiv.org/html/2601.04562v2#S3.SS1.SSS0.Px2.p1).
- **可见性**：warm; validation and test users and POIs are kept only if observed in training. The cross-city test (Table 6) uses POIs of another city; their tokenizer exposure is not reported.
  - 出处：Test users and POIs observed in training: [S3.SS1.p1](https://arxiv.org/html/2601.04562v2#S3.SS1.p1).
- **SID 规格**：Hierarchical spatial SID [g; s; u]: two S2-cell locality tokens (after removing the dataset-wide common prefix), two semantic tokens from a 2-level residual quantizer with 28 codes per level over Qwen-0.6B category embeddings, and a sequential suffix token within each (g, s) pair that makes IDs unique (at most 8 suffix values observed).
  - 出处：HS-SID construction: [A1.SS3.SSS0.Px1.p1](https://arxiv.org/html/2601.04562v2#A1.SS3.SSS0.Px1.p1).
- **推理预算**：Generates a mobility chain-of-thought and then one POI SID per request (three inference runs averaged); decoding settings not reported. Qwen3-4B student on 8 NVIDIA H20 GPUs; inference batch size and latency: not reported.
  - 出处：One output per request, hardware: [S3.SS1.SSS0.Px2.p1](https://arxiv.org/html/2601.04562v2#S3.SS1.SSS0.Px2.p1) and [S3.SS1.SSS0.Px3.p1](https://arxiv.org/html/2601.04562v2#S3.SS1.SSS0.Px3.p1).
- **结果来源**：Table 1 (HR@1 on NYC, TKY, CA versus traditional, neural, and LLM-based baselines); Tables 2-5 and Figure 3 (SID design, CoT stages, geographic cues, reward weights); Table 6 (cross-city generalization).
  - 出处：Main: [S3.T1](https://arxiv.org/html/2601.04562v2#S3.T1); ablations: [S3.T2](https://arxiv.org/html/2601.04562v2#S3.T2), [S3.T3](https://arxiv.org/html/2601.04562v2#S3.T3), [S3.T4](https://arxiv.org/html/2601.04562v2#S3.T4), [S3.T5](https://arxiv.org/html/2601.04562v2#S3.T5); RL weights: [S3.F3](https://arxiv.org/html/2601.04562v2#S3.F3); cross-city: [S3.T6](https://arxiv.org/html/2601.04562v2#S3.T6).

</details>

- 思维链阶段：三个阶段全用才最好（Sec. 3.3，Table 3）。
- 跨城迁移：在一个城市训练，用到两个没见过的城市，ROS 的迁移效果好于 LLM4POI 和 GA-LLM（Sec. 3.4，Table 6）。

### 4. 局限与分析

**Our analysis.**

- GNPR-SID 用普通 `RQ-VAE` 量化 POI 特征；ROS 在语义码前面加了显式的 S2 cell 前缀（`Geo-Prefix+RQ-VAE`）。
- SpaceTime-GR 只用地理索引（`Geo`，`Geo-Idx`）；ROS 在 SID 中加入品类语义，并在解码前先推理（`CoT+C-Beam`）。

### 5. 相关工作

```mermaid
flowchart LR
    P["ROS"]
    P -->|competitor| A["GNPR-SID"]
    P -->|competitor| B["Spacetime-GR"]
    P -->|alternative| C["OneLoc"]
    P -->|alternative| D["LGSID"]
```

- **同期对比** · [GNPR-SID](gnpr-sid.md): GNPR-SID quantizes POI embeddings without explicit spatial structure; ROS builds S2-cell locality tokens plus semantic codes and adds mobility chain-of-thought and spatial RL.
  - 出处：ROS v2, LLM-based baselines: https://arxiv.org/html/2601.04562v2#S3.SS1.SSS0.Px1.p1; Table 1: https://arxiv.org/html/2601.04562v2#S3.T1.
- **同期对比** · [Spacetime-GR](spacetime-gr.md): SpaceTime-GR also generates next POIs with an LLM; ROS adds hierarchical spatial SIDs and explicit reasoning before the recommendation.
  - 出处：ROS v2, LLM-based baselines (ST-GR): https://arxiv.org/html/2601.04562v2#S3.SS1.SSS0.Px1.p1; Table 1: https://arxiv.org/html/2601.04562v2#S3.T1.
- **替代方案** · [OneLoc](oneloc.md): OneLoc injects geography into the SID input and rewards; ROS encodes geography directly as S2-cell prefix tokens.
  - 出处：ROS v2, Section 1 cites OneLoc: https://arxiv.org/html/2601.04562v2#S1.p3.
- **替代方案** · [LGSID](lgsid.md): LGSID aligns embeddings with geographic rewards before quantization; ROS separates geographic and semantic tokens inside the SID.
  - 出处：ROS v2, Section 1 cites LGSID: https://arxiv.org/html/2601.04562v2#S1.p3.

[查看同格全部论文](../../../README.zh.md#i--tokenization)
