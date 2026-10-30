# MACRec

*Multi-aspect cross-modal quantization for generative recommendation* — Zhang et al., AAAI’26

[arXiv](https://arxiv.org/abs/2511.15122) · [Record](../../data/papers/macrec.yaml) · [← Catalog](../../README.md#i--tokenization)

> Abstract: "remain limited in their ability to harness multimodal information".

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **I. Informativeness**: Do the SIDs, or the model reading them, carry the collaborative and multimodal signals recommendation needs? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img` | **`Cross RQ`** | `Enc-Dec` | `Fixed / NTP + Ctr.` | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP + Ctr.`: NTP plus a contrastive loss.
- `C-Beam`: Constrained beam search.

## Architecture

![MACRec architecture diagram](../../architectures/macrec.png)

## Evidence

- **`problem`** (arXiv abstract): Abstract: "remain limited in their ability to harness multimodal information".
- **`tokenizer`** (p5; Conclusion, p7; code: zhangfw123/MACRec README and data.py): Location from the pre-10-26 Training evidence in the appendix.

## 旧卡片说明

迁自 `d61aa6c:papers/macrec.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### MACRec：多方面跨模态量化生成式推荐

> MACRec 在 SID 量化和生成推荐训练中同时建模文本、图像及其交互，减少跨模态语义损失和标识碰撞。

### 研究动机与问题定义

已有多模态生成推荐常独立量化不同模态，难以利用互补信息。MACRec 将跨模态对比学习放入量化过程，并在生成阶段加入多方面对齐。

### TL;DR（核心摘要）

`文本/图像 → 跨模态量化 → 多模态SID → 生成模型 → 内部集成 → 推荐物品`

模型分别编码文本和图像，通过伪标签、跨模态残差量化和重构对齐学习语义标识；生成推荐阶段包含隐式表示对齐、显式 item/sequence 对齐和 Seq2Seq 目标。推理时对两种模态进行约束束搜索并在模型内部平均分数，得到最终物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 物品文本、图像和用户交互 |
| 信息融入位置 | 量化目标、对齐任务和生成输入 |
| 语义标识结构 | 文本/视觉多级离散序列 |
| 适用场景 | 多模态序列推荐 |

### 方法设计

#### 3.1 双模态伪标签
MACRec 分别用文本编码器和视觉编码器获得物品表示，再在两种模态上聚类生成伪标签。伪标签用于构造跨模态正样本，使文本和图像在量化过程中能够相互提供监督。

#### 3.2 跨模态量化与重构
文本、视觉表示分别经过 MLP 和多级残差量化。跨模态对比损失让一类模态的残差表示吸收另一类模态的相似性；重构损失和量化损失保证离散 code 能恢复原始表示。

#### 3.3 多方面生成对齐
生成推荐阶段包含同模态 next-item 生成、跨模态 item/sequence 对齐，以及隐式表示对齐。模型由一种模态的历史 SID 预测另一种模态的目标 SID，促进两套标识的协同。

#### 3.4 训练与推理
训练目标联合推荐损失和对齐损失。推理时两种模态分别进行约束束搜索，最后在模型内部平均候选分数并去重，得到推荐结果。

### 实验结论

- MACRec 在三个 Amazon 数据集上优于比较方法。
- 跨模态量化和多方面对齐均改善效果，并降低碰撞。

### 局限性与研究定位

#### 局限性
- 双模态生成和结果集成增加推理成本。
- 图像缺失、动态物品和线上服务效率仍需验证。

#### 研究定位
MACRec 的贡献是把跨模态交互前移到 SID 学习阶段，适合放在“多模态语义标识与生成推荐”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2511.15122)

### 标签

`跨模态量化` · `多方面对齐` · `多模态推荐` · `生成式推荐`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：在量化阶段建模跨模态交互。
- 使用场景：多模态推荐。

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
| [MMGRec](mmgrec.md) | TOMM’26 | `Text+Img+CF` → **`Graph RQ-VAE`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [MMQ](mmq.md) | WSDM’26 | `Text+Img` → **`MoE-VQ`** → `HeterRec` → `Joint / MTP` → `–` |
| [MSCGRec](mscgrec.md) | arXiv’26 | `Text+Img+CF` → **`RQ-VAE+DINO`** → `Enc-Dec` → `Fixed† / NTP` → `Trie/C-Beam` |
| [PCR-CA](pcr-ca.md) | KDD’26 | `Text+CF` → **`PC-AE`** → `Disc.` → `Joint / Discrim.` → `Scoring` |
| [Pctx](pctx.md) | CIKM’26 | `Text+CF` → **`RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam+Agg.` |
| [ProGEO](progeo.md) | arXiv’26 | `Text+Geo` → **`R-KM+Geo-CB`** → `Dec-Only` → `Fixed / NTP` → `Beam+Geo-Filter` |
| [RoFiGR](rofigr.md) | arXiv’26 | `Text+Img+CF` → **`CF-Aligned MM RQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `C-Beam` |
| [ROS](ros.md) | ACL’26 | `Text+Geo` → **`Geo-Prefix+RQ-VAE`** → `Dec-Only` → `Fixed / NTP → RL` → `CoT+C-Beam` |
| [SPRIG](sprig.md) | CIKM’26 Short | `Text / Audio` → **`R-KM`** → `Dec-Only` → `Fixed / NTP` → `Div. Beam` |
| [Tlow](tlow.md) | CIKM’26 Applied | `Text` → **`Flow+PQ`** → `Non-AR` → `Fixed / MTP + Rel.MSE` → `Scoring` |
| [UniRec](unirec.md) | arXiv’26 | `Text+CF` → **`RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `C-Beam` |
| [UniSID](unisid.md) | arXiv’26 | `Text+Img+Attr` → **`Direct SID Heads`** → `–` → `– / –` → `–` |
| [VarLenRec (TIGER)](varlenrec-tiger.md) | arXiv’26 | `Text` → **`HARQ`** → `Enc-Dec` → `Fixed / NTP + Aux.` → `C-Beam` |
