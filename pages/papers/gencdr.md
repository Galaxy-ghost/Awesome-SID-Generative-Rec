# GenCDR

*From ids to semantics: A generative framework for cross-domain recommendation with adaptive semantic tokenization* — Hu et al., AAAI’26

[arXiv](https://arxiv.org/abs/2511.08006) · [Record](../../data/papers/gencdr.yaml) · [← Catalog](../../README.md#vi--tokenization)

> Abstract: "item ID tokenization dilemma"; "insufficient domain-specific modeling". Candidates: VI / I (rule: tie broken by the majority of new designs).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **VI. Generalization**: Does it still work for new items, new domains, and shifting interests? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Cross-Dom` | **`RQ+LoRA`** | `Dec-Only` | `Fixed / NTP` | `C-Beam` |

- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

## Architecture

![GenCDR architecture diagram](../../architectures/gencdr.png)

## Evidence

- **`problem`** (arXiv abstract): Abstract: "item ID tokenization dilemma"; "insufficient domain-specific modeling". Candidates: VI / I (rule: tie broken by the majority of new designs).

## 旧卡片说明

迁自 `d61aa6c:papers/gencdr.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### GenCDR：带自适应语义分词的跨域生成推荐

> GenCDR 用共享语义空间和域特定适配器构造统一 SID，并以动态路由适配不同领域的推荐偏好。

### 研究动机与问题定义

跨域推荐既需要共享知识，也需要保留领域特征；固定的物品标识和静态融合容易造成负迁移。GenCDR 研究如何让 SID 和生成器同时具备跨域共享与域内适应能力。

### TL;DR（核心摘要）

`多域物品文本 → 通用SID → 域适配量化 → 统一生成器 → 域路由 → 推荐物品`

第一阶段用共享编码器和 RQ-VAE 学习通用 SID；第二阶段通过 LoRA 适配器学习域特定表示，并用 item-level 动态路由融合通用与域内表示。统一生成器先学习跨域兴趣，再进行域特定微调，使用前缀树约束生成完整 SID，直接得到物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 多域物品文本与用户交互 |
| 信息融入位置 | SID 构建、LoRA 适配和生成输入 |
| 语义标识结构 | 跨域共享的层次化序列 |
| 适用场景 | 跨域序列推荐 |

### 方法设计

#### 3.1 问题定义与总体流程
GenCDR 面向多个领域的跨域序列推荐，目标是使用共享 SID 建立可迁移的物品和用户兴趣空间。系统分为域自适应分词、跨域自回归推荐和域特定微调三部分。

#### 3.2 域自适应分词
通用编码器和 RQ-VAE 先从多域文本学习共享语义基础；每个领域再通过 LoRA 适配器补充领域特征。item-level 动态路由器以物品为单位融合通用表示和域特定表示，融合结果再量化为 SID。

#### 3.3 跨域自回归推荐
统一生成器把跨域历史 SID 作为输入，先学习域无关的兴趣模式。域特定适配阶段加入各领域 LoRA，使模型保留共享知识并适应领域差异。

#### 3.4 训练与推理
训练采用通用阶段和领域微调阶段。在线生成时使用前缀树约束，确保输出完整 SID 能对应目标领域中的真实物品。

### 实验结论

- GenCDR 在跨域推荐设置中改善了域内和迁移表现。
- 动态路由和域特定 LoRA 有助于缓解负迁移。

### 局限性与研究定位

#### 局限性
- 多适配器和路由网络增加部署管理成本。
- 前缀树与域特定 SID 更新流程仍需更多工业验证。

#### 研究定位
GenCDR 的贡献是把域适配从推荐器参数扩展到 SID 表示和路由，适合放在“跨域语义标识生成”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2511.08006)

### 标签

`跨域推荐` · `自适应分词` · `动态路由` · `LoRA`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：自适应融合通用与域特定语义。
- 使用场景：跨域推荐。

## Same cell: VI × Tokenization (8 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [VQ-Rec](vq-rec.md) | WWW’23 | `Multi-Dom` → **`OPQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring` |
| [GMC](gmc.md) | arXiv’25 | `Cross-Dom` → **`Unified RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [UTGRec](utgrec.md) | arXiv’25 | `Multi-Dom` → **`Tree`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [DACT](dact.md) | SIGIR’26 | `Text+CF` → **`RQ-VAE`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `–` |
| [DREAM](dream.md) | arXiv’26 | `Text+CF` → **`CART`** → `Dec-Only` → `Altern. / NTP + Aux.` → `C-Beam` |
| [MBGR](mbgr.md) | arXiv’26 | `Text+CF` → **`RQ`** → `Dec-Only` → `Fixed† / NTP + Aux.` → `C-Beam` |
| [OneLive](onelive.md) | KDD’26 ADS | `Text+Img+Audio+CF` → **`R-KM`** → `Lazy Dec-Only` → `Fixed / NTP → RL` → `Beam` |
| [UniTok](unitok.md) | AAAI’26 | `Multi-Dom` → **`TokenMoE`** → `Enc-Dec` → `Fixed / NTP` → `Beam†` |
