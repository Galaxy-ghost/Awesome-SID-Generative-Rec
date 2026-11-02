# GeoGR

*Enabling Spatio-Temporal Aware Industrial-Scale Generative POI Recommendations* — Wang et al. · arXiv’26

`I. Informativeness` · `Representation` · `POI`

[Paper](https://arxiv.org/abs/2602.10411) · [Matrix](../../README.md#i--representation)

Reading level: Overview (Level 1) · On this page: [At a Glance](#at-a-glance) · [2. How It Works](#2-how-it-works) · [5. Connections to Related Work](#5-connections-to-related-work)

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| **`Text+Geo+CF`** | `R-KM+EM` | `Dec-Only` | `Altern.† / Multi-task NTP` | `Beam` |

- `R-KM+EM`: Residual k-means with expectation-maximization-style refinement.
- `Dec-Only`: Decoder-only.
- `Multi-task NTP`: The same NTP loss over several tasks.

### At a Glance

| Aspect | Summary |
| :-- | :-- |
| Research Problem | I. Informativeness: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? |
| Modified Stage | Representation |

### 2. How It Works

![GeoGR architecture diagram](../../architectures/geogr.png)

## 旧卡片说明

迁自 `d61aa6c:papers/geogr.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### GeoGR：面向工业规模生成式 POI 推荐的时空感知框架

> GeoGR 通过地理约束共访关系构造时空协同 SID，并用持续预训练和监督微调使 LLM 直接生成可服务的 POI 标识。

### 研究动机与问题定义

工业 POI 推荐同时面对稀疏行为、复杂地理关系和 LLM 不理解非原生 SID token 的问题。GeoGR 面向导航类本地服务，目标是在保留用户时空状态变化的同时，建立可生成、可扩展并能在线服务的 POI 标识。

### TL;DR（核心摘要）

`POI描述/地理/共访关系 → 对比表示学习 → RQ-KMeans SID → CPT → SFT生成 → 在线POI`

GeoGR 先利用地理约束的共访 POI 对学习时空协同表示，再通过层次化 RQ-KMeans 生成 SID，并用 EM 风格优化减少标识质量问题。推荐模型经过多模板持续预训练和监督微调，使 LLM 学会 SID、POI 描述与下一位置预测之间的对应关系。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | POI 描述、经纬度、地理约束共访关系和用户轨迹 |
| 信息融入位置 | SID 表示、量化优化、持续预训练和生成输入 |
| 语义标识结构 | 多级定长离散序列 |
| 适用场景 | 导航、本地生活和工业规模服务 |

### 方法设计

#### 4.1 地理感知 POI SID 构建
GeoGR 将 POI 文本、经纬度、地址和类别输入 LLM，构造初始语义表示。为避免只依赖文本相似性，作者从用户轨迹中挖掘地理接近且具有共访关系的 POI 对，并加入正负样本进行对比学习。

#### 4.1.1 时空协同语义表示
正样本来自轨迹中频繁共现且空间相近的 POI，负样本通过采样获得。对比目标使表示同时靠近行为相关和地理合理的 POI，减少“文本相似但行为无关”的错误关联。

#### 4.1.2 语义表示量化
模型使用层次化 RQ-KMeans 逐级量化 POI 表示。每层对当前残差聚类并生成 code，所有 code 拼成 POI SID；层次结构让前缀承载较粗粒度的时空语义。

#### 4.1.3 EM 风格 SID 优化
作者让 LLM 根据生成 SID 相关任务反向评估标识质量，再用 EM 风格过程交替细化 SID 和模型参数，改善 SID 与 POI 语义、地理关系的一致性。

#### 4.2 生成式 POI 推荐
在推荐训练前，GeoGR 用包含 SID 描述、用户轨迹和 POI 问答的多任务语料进行持续预训练，使 LLM 适应新增的非原生 token。之后使用下一 POI 监督模板进行 SFT，模型根据历史和当前上下文自回归生成目标 SID。

### 实验结论

- 公共数据集和工业数据集实验均报告 GeoGR 优于比较方法。
- 在线部署三个月的实验报告 WINRATE 提升 2.91%、PV_CTR 提升 5.55%，说明该框架具备生产可用性。
- 消融与表示可视化支持地理协同 SID、CPT 和 SFT 对效果的贡献；模型规模影响也被单独分析。

### 局限性与研究定位

#### 局限性

- SID 构建、EM 风格优化和多阶段 LLM 训练流程较复杂，复现实验需要较多工业数据与资源。
- 论文对动态新增 POI、标识碰撞在线修复和生成失败回退的细节报告有限。

#### 研究定位

GeoGR 适合放在“工业级地理生成式推荐”章节，体现时空协同 SID 与 LLM 任务对齐、线上部署相结合的路线。

### 相关资源

- [论文原文](https://arxiv.org/abs/2602.10411)

### 标签

`工业规模` · `时空协同` · `RQ-KMeans` · `在线部署`

### 架构图来源

*图源：原论文，图2（[论文原文](https://arxiv.org/abs/2602.10411)）。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：面向工业规模结合时空 SID 与多阶段 LLM 对齐。
- 使用场景：导航与工业 POI 推荐。

### 5. Connections to Related Work

[View all papers in this cell](../../README.md#i--representation)
