# ROS

*Reasoning Over Space: Enabling Geographic Reasoning for LLM-Based Generative Next POI Recommendation* — Lv et al., ACL’26 · `POI`

[arXiv](https://arxiv.org/abs/2601.04562) · [Record](../../data/papers/ros.yaml) · [← Catalog](../../README.md#i--tokenization)

> Abstract: "existing LLM-based recommenders remain limited in leveraging geographic signals". Alternative III: the introduction narrows the gap to not reasoning over geography (p1).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Geo` | **`Geo-Prefix+RQ-VAE`** | `Dec-Only` | `Fixed / NTP → RL` | `CoT+C-Beam` |

- `Geo-Prefix+RQ-VAE`: Geographic prefixes combined with residual-quantized variational codes.
- `Dec-Only`: Decoder-only.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP → RL`: NTP, then reinforcement learning (GRPO, GBPO, etc.).
- `CoT+C-Beam`: Reasoning followed by constrained beam-search decoding.

## Architecture

![ROS architecture diagram](../../architectures/ros.png)

## Evidence

- **`problem`** (abstract, p1): Abstract: "existing LLM-based recommenders remain limited in leveraging geographic signals". Alternative III: the introduction narrows the gap to not reasoning over geography (p1).
- **`stage`** (contribution (1), p2): Three designs fix the same problem: Hierarchical Spatial SID (Tokenization), Mobility CoT and spatial-guided RL (Training); the first contribution decides.
- **`tokenizer`** (§2.2, p2): SIDs are built before SID grounding pre-training.

## 旧卡片说明

迁自 `d61aa6c:papers/ros.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### ROS：空间推理增强的生成式下一兴趣点推荐

> ROS 将地理关系显式纳入下一 POI 推理过程，通过层次化空间 SID、移动思维链和空间引导强化学习生成可行地点。

### 研究动机与问题定义

下一 POI 不是普通的物品分类：用户兴趣、时间规律和空间可达性共同决定目的地。已有 LLM 推荐方法虽能生成 SID，却常把空间信息作为文本或单步条件，缺少显式的候选构造和可行性判断。ROS 将推荐建模为带空间约束的多阶段决策。

### TL;DR（核心摘要）

`坐标/网格/类别 → 空间SID → 用户画像与候选空间 → 移动CoT剪枝 → 生成POI SID`

ROS 把 POI SID 分成地理前缀、语义锚点和区分性后缀。模型先通过双向对齐和序列预训练学习 SID 与地址/类别的对应关系，再用三步 Mobility CoT 建立用户画像、构造意图候选并进行局部性剪枝，最后用空间、SID 和格式奖励进行强化学习。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | GPS、S2 网格、POI 类别、地址、用户历史和时间 |
| 信息融入位置 | SID 结构、预训练任务、思维链和强化学习奖励 |
| 语义标识结构 | 层次化、定长离散序列 |
| 适用场景 | 下一 POI、跨城市迁移和地理可行性推荐 |

### 方法设计

#### 2.1 问题形式化
给定用户历史轨迹、时间和上下文，模型需要生成下一 POI 的完整 SID。与只预测一个标签不同，ROS 将生成过程拆为画像分析、候选空间构造和局部性筛选等有顺序的决策。

#### 2.2 空间语义标识
地理前缀由 GPS 映射到 S2 网格，再转换为层次化六边形 token；语义锚点由 POI 类别等文本信息经过编码和 RQ-VAE 量化得到；后缀用于区分同一地理和语义区域内的不同 POI。三者拼接为 Hierarchical Spatial SID。

#### 2.2.2 SID 对齐预训练
模型使用双向 SID-文本/地址对齐任务，使 SID 能预测 POI 的类别和地址，也使文本能恢复 SID。另一个序列预训练任务让模型学习移动轨迹中的时间、类别重复和邻域连续性。

#### 2.3 Mobility CoT 推理
第一步从历史轨迹提炼用户移动画像；第二步根据画像和当前上下文形成候选 POI 空间；第三步依据访问频率、时间和空间邻近性对候选进行局部性剪枝，再生成目标 SID。这种流程把地理可行性变成显式推理条件。

#### 2.4 空间引导强化学习
训练时从策略模型采样推理轨迹，奖励由空间距离、SID 层次匹配和格式合法性组成，并通过 GRPO 优化。层级 SID 奖励使正确的地理前缀和语义部分获得分层反馈。

### 实验结论

- 在三个 LBSN 数据集上，ROS 相比 LLM 基线取得更高命中率，论文报告相对提升超过 10%。
- 移动 CoT 和空间奖励的消融支持显式候选构造与地理剪枝的作用。
- 跨城市实验显示模型具有较好的迁移能力，但论文指出短时间长距离移动的交通先验仍未充分建模。

### 局限性与研究定位

#### 局限性

- 当前地理可行性主要采用短时间内长距离移动不太可能的单调先验，可能低估地铁、高速等交通支持的远距离移动。
- 多阶段思维链会增加生成 token 和推理成本，在线延迟比较未充分展开。

#### 研究定位

ROS 代表把“空间推理”引入 Semantic ID 生成推荐的路线，适合放在“推理增强与地理约束生成推荐”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2601.04562)

### 标签

`空间推理` · `层次化SID` · `移动思维链` · `空间强化学习`

### 架构图来源

*图源：原论文，图2（[论文原文](https://arxiv.org/abs/2601.04562)）。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：用移动思维链和空间奖励显式执行地理推理。
- 使用场景：下一 POI、跨城市迁移。

## Same cell: I × Tokenization (33 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [CoST](cost.md) | RecSys’24 | `Text` → **`C-RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [LETTER](letter.md) | CIKM’24 | `Text+CF` → **`Learn. RQ`** → `Enc-Dec` → `Fixed / NTP + Rank` → `C-Beam` |
| [LMIndexer](lmindexer.md) | ICML’24 | `Text` → **`Self-Sup. ID`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [ActionPiece](actionpiece.md) | ICML’25 | `Text` → **`OPQ`** → `Enc-Dec` → `Fixed / NTP` → `Ensemble` |
| [ADC-SID](adc-sid.md) | arXiv’25 | `Text+Img+CF` → **`MoE-VQ`** → `Enc-Dec` → `Fixed† / NTP` → `–` |
| [DAS](das.md) | CIKM’25 | `Text+CF` → **`Dual RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [EAGER-LLM](eager-llm.md) | WWW’25 | `Text+CF` → **`Dual H-KM`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
| [FlexCode](flexcode.md) | arXiv’25 | `Text+CF` → **`Dual RQ-VAE`** → `–` → `Joint / NTP` → `–` |
| [GenSAR](gensar.md) | RecSys’25 | `Text+CF` → **`Shared/Spec. RQ`** → `Enc-Dec` → `Fixed / Multi-task NTP` → `C-Beam` |
| [GNPR-SID](gnpr-sid.md) | KDD’25 | `Attr+Geo+CF` → **`RQ-VAE`** → `Dec-Only` → `Fixed / NTP` → `–` |
| [GRAM](gram.md) | ACL’25 | `Text+CF` → **`H-KM`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [KGTB](kgtb.md) | arXiv’25 | `Attr+Geo+CF` → **`KG-RQ`** → `Dec-Only` → `Fixed / Multi-task NTP` → `–` |
| [MME-SID](mme-sid.md) | CIKM’25 | `Text+Img+CF` → **`MM-RQ`** → `Dec-Only` → `Fixed / NTP` → `Scoring` |
| [MQL4GRec](mql4grec.md) | ICLR’25 | `Text+Img` → **`Dual RQ`** → `Enc-Dec` → `Fixed / Multi-task NTP` → `Beam` |
| [PSRQ](psrq.md) | CIKM’25 | `Text+Img` → **`Prog. RQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring` |
| [QT-Mob](qt-mob.md) | KDD’25 | `Text+Geo` → **`RQ-VAE`** → `Dec-Only` → `Fixed / Multi-task NTP` → `C-Beam` |
| [TokenRec](tokenrec.md) | TKDE’25 | `CF` → **`Masked VQ`** → `Encoder` → `Fixed / Discrim.` → `Scoring` |
| [CapsID](capsid.md) | arXiv’26 | `Text+CF` → **`Soft-RQ`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [ChronoID](chronoid.md) | arXiv’26 | `Text+Time` → **`RQ-VAE / Par. VQ`** → `Dec-Only†` → `Fixed / NTP` → `Beam†` |
| [GrIS (RecDMoN / RQ-GAE)](gris-recdmon-rq-gae.md) | CIKM’26 | `Text+CF` → **`RecDMoN / RQ-VAE`** → `Enc-Dec` → `Fixed / –` → `–` |
| [MACRec](macrec.md) | AAAI’26 | `Text+Img` → **`Cross RQ`** → `Enc-Dec` → `Fixed / NTP + Ctr.` → `C-Beam` |
| [MMGRec](mmgrec.md) | TOMM’26 | `Text+Img+CF` → **`Graph RQ-VAE`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [MMQ](mmq.md) | WSDM’26 | `Text+Img` → **`MoE-VQ`** → `HeterRec` → `Joint / MTP` → `–` |
| [MSCGRec](mscgrec.md) | arXiv’26 | `Text+Img+CF` → **`RQ-VAE+DINO`** → `Enc-Dec` → `Fixed† / NTP` → `Trie/C-Beam` |
| [PCR-CA](pcr-ca.md) | KDD’26 | `Text+CF` → **`PC-AE`** → `Disc.` → `Joint / Discrim.` → `Scoring` |
| [Pctx](pctx.md) | CIKM’26 | `Text+CF` → **`RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam+Agg.` |
| [ProGEO](progeo.md) | arXiv’26 | `Text+Geo` → **`R-KM+Geo-CB`** → `Dec-Only` → `Fixed / NTP` → `Beam+Geo-Filter` |
| [RoFiGR](rofigr.md) | arXiv’26 | `Text+Img+CF` → **`CF-Aligned MM RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `C-Beam` |
| [SPRIG](sprig.md) | CIKM’26 Short | `Text / Audio` → **`R-KM`** → `Dec-Only` → `Fixed / NTP` → `Div. Beam` |
| [Tlow](tlow.md) | CIKM’26 Applied | `Text` → **`Flow+PQ`** → `Non-AR` → `Fixed / MTP + Rel.MSE` → `Scoring` |
| [UniRec](unirec.md) | arXiv’26 | `Text+CF` → **`RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `C-Beam` |
| [UniSID](unisid.md) | arXiv’26 | `Text+Img+Attr` → **`Direct SID Heads`** → `–` → `– / –` → `–` |
| [VarLenRec (TIGER)](varlenrec-tiger.md) | arXiv’26 | `Text` → **`HARQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `C-Beam` |
