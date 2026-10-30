# FORGE: Forge: Forming semantic identifiers for generative retrieval in industrial datasets

[Back to Catalog](../../README.md) · [Paper (`https://arxiv.org/abs/2509.20904`)](https://arxiv.org/abs/2509.20904) · [Source Record (`data/papers/forge.yaml`)](../../data/papers/forge.yaml)

> **Summary**: Abstract: "their SID assessment typically relies on costly GR training".

## Taxonomy & Table 1 Specification

| Field | Value | Vocabulary Definition |
| :--- | :--- | :--- |
| **Authors & Year** | Fu et al. (2025) | Published / posted in `KDD’26` |
| **Problem Band** | `Paradigms, Systems and Benchmarks` | Baseline (TIGER), end-to-end multi-stage paradigms, open-source frameworks, benchmarks, and diagnostic resources. |
| **Primary Stage** | `n/a` | Used for Paradigms, Systems and Benchmarks (psb) rows that are not assigned to a single stage. |
| **Representation** | `Text+Img` |  |
| **Tokenization** | `RQ-VAE` |  |
| **Backbone** | `Dec-Only` | Decoder-only. |
| **Tokenizer Training** | `Fixed` | SIDs are built first and not changed while the generator trains. |
| **Training Objective** | `NTP` | Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP. |
| **Inference Decoding** | `Dyn. Beam` | Dynamic beam search. |
| **POI / Local-Life** | `false` | Point-of-interest / geographic recommendation indicator |
| **Code Repository** | [`https://huggingface.co/AL-GR`](https://huggingface.co/AL-GR) | Official or public implementation link |

## Architecture

![FORGE architecture diagram](../../architectures/forge.png)

## Verbatim Evidence & Rationale

- **`problem`** (arXiv abstract): Abstract: "their SID assessment typically relies on costly GR training".
- **`stage`** (arXiv abstract): Appendix tentatively places the new design in Tokenization.

## 旧卡片说明

迁自 `d61aa6c:papers/forge.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### FORGE：工业数据集语义标识构建

> FORGE 面向大规模工业交互数据，融合多模态内容和协同关系构造、清洗并评估生成式检索所需的语义标识。

### 研究动机与问题定义

小规模公开数据集难以反映工业生成式检索中的多模态、长尾和标识碰撞问题。FORGE 提供大规模数据、SID 构建流程、碰撞后处理和生成式检索评估，重点考察标识质量对推荐的影响。

### TL;DR（核心摘要）

`多模态内容与协同关系 → RQ-VAE SID → 碰撞消解 → 生成式检索 → 推荐物品`

文本和图像编码器提取内容表示，并以最相关的物品关系补充协同信息；RQ-VAE 生成多级 SID，随后使用碰撞处理和质量指标筛选。下游生成式检索模型直接生成 SID，SID 再映射到物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 文本、图像、物品关系和用户交互 |
| 信息融入位置 | SID 构建与生成式检索训练 |
| 语义标识结构 | 多级离散序列 |
| 适用场景 | 大规模工业生成式检索 |

### 方法设计

#### 3.1 SID 生成（SID Generation）
FORGE 使用文本和图像语言模型提取物品多模态内容，并结合最具协同关系的物品信息。融合表示经过 RQ-VAE 量化为多级 SID，既保留内容语义，也纳入工业交互中的相似关系。

#### 3.2 标识碰撞缓解（Alleviating ID Collisions）
论文分析多个物品获得相同 SID 的情况，并通过碰撞后处理、码本分配和质量指标评估标识可用性。相关指标包括碰撞、分布均衡、生成命中和代码升级收敛等。

#### 3.3 生成式检索（Generative Retrieval）
SID 被作为生成式检索的目标序列，推荐模型直接预测 SID。论文同时讨论训练阶段和动态推理阶段，考察大规模工业交互下生成结果的有效性与泛化。

#### 3.4 评估与工业分析
实验把 SID 直接指标和下游推荐指标结合，并分析数据规模、模态组合、代码本升级和线上可用性。FORGE 的重点也包括工业数据资源与评估基准。

### 实验结论

- FORGE 的工业数据规模和交互密度显著高于常见公开基准。
- SID 质量指标与生成式检索效果存在关联，碰撞处理能改善可用性。

### 局限性与研究定位

#### 局限性
- 工业数据和线上结果的可复现程度受数据开放范围限制。
- 具体下游模型与完整线上延迟比较未统一报告。

#### 研究定位
FORGE 的价值在于把 SID 学习从小规模基准推进到工业数据工程与评估。它适合放在“工业生成式检索与语义标识质量”章节。

### 相关资源

- [项目与数据资源](https://huggingface.co/AL-GR)

### 标签

`工业数据` · `多模态` · `SID优化` · `生成式检索`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：提供工业SID构建与评估流程。
- 使用场景：工业生成式检索。

## Peer Methods in `Paradigms, Systems and Benchmarks` × `n/a` (11 peers)

| Method | Venue | Representation | Tokenization | Backbone | Tokenizer | Objective | Inference |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [TIGER](tiger.md) | NeurIPS’23 | `Text` | `RQ-VAE` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [GRID](grid.md) | CIKM’25 | `Text` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP` | `Beam` |
| [MiniOneRec](minionerec.md) | arXiv’25 | `Text` | `RQ-VAE` | `Dec-Only` | `Fixed` | `NTP → RL` | `Beam` |
| [OneRec](onerec.md) | arXiv’25 | `Text+CF` | `R-KM` | `Enc-Dec` | `Fixed` | `NTP → DPO` | `Sess. Beam` |
| [GR-Generalize](gr-generalize.md) | arXiv’26 | `Text+SID` | `RQ-VAE` | `Enc-Dec` | `Fixed†` | `NTP†` | `Hybrid` |
| [NEO](neo.md) | arXiv’26 | `Text / Audio` | `R-KM` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `C-Beam` |
| [Netflix-SID-Comparison](netflix-sid-comparison.md) | NeurIPS’26 PALM Workshop | `–` | `RQ-VAE` | `Dec-Only / Non-AR` | `Fixed` | `Multi-task NTP / (Text NTP + MTP + Rank); Lang. RL after SFT` | `C-Beam / Scoring` |
| [OneMall](onemall.md) | CIKM’26 | `Text+Img+CF` | `R-KM+FSQ` | `Enc-Dec` | `Fixed` | `(NTP + Ctr.) → RL` | `Beam` |
| [PLUM](plum.md) | WWW’26 | `Text+Img+CF` | `RQ-VAE` | `Dec-Only` | `Fixed` | `Multi-task NTP` | `Beam` |
| [ReRankID](rerankid.md) | arXiv’26 | `Text` | `R-KM†` | `Dec-Only` | `Fixed` | `NTP → RL` | `CoT+Greedy` |
| [SIDScope](sidscope.md) | arXiv’26 | `–` | `–` | `–` | `–` | `–` | `–` |
