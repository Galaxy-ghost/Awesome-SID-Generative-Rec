# HiD-VAE

*Interpretable Generative Recommendation via Hierarchical and Disentangled Semantic IDs* — Fang et al., arXiv’25

[arXiv](https://arxiv.org/abs/2508.04618) · [Record](../../data/papers/hid-vae.yaml) · [← Catalog](../../README.md#ii--tokenization)

> Abstract: "semantically flat and uninterpretable, lacking a coherent hierarchy"; "prone to representation entanglement (i.e., ``ID collisions'')". Candidates: I / II (rule: tie broken by the majority of new designs).

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **II. Uniqueness and Validity**: Does every item get its own SID, every generated SID name a real item, and the codebook get used evenly? | **Tokenization** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text` | **`Hier. RQ`** | `Enc-Dec` | `Fixed / NTP` | `C-Beam` |

- `Enc-Dec`: Encoder-decoder.
- `Fixed`: SIDs are built first and not changed while the generator trains.
- `NTP`: Next-token prediction loss only; continuing from a pretrained LLM (SFT) also counts as NTP.
- `C-Beam`: Constrained beam search.

## Architecture

![HiD-VAE architecture diagram](../../architectures/hid-vae.png)

## Evidence

- **`problem`** (arXiv abstract): Abstract: "semantically flat and uninterpretable, lacking a coherent hierarchy"; "prone to representation entanglement (i.e., ``ID collisions'')". Candidates: I / II (rule: tie broken by the majority of new designs).
- **`tokenizer`** (§3.8, p5): Location from the pre-10-26 Training evidence in the appendix.

## 旧卡片说明

迁自 `d61aa6c:papers/hidvae.md`。保留方法说明、实验叙述与局限；本轮只对照现有记录处理明确冲突，未重新逐句核查原论文。分类和规格以页面上方由记录生成的表格为准。

### HiD-VAE：层次解耦语义标识可解释生成推荐

> HiD-VAE 通过层次标签监督和唯一性约束学习可解释、低碰撞的物品语义标识，并用于直接生成推荐。

### 研究动机与问题定义

现有 SID 往往缺乏可解释层次，且不同物品可能碰撞到相同标识。HiD-VAE 研究如何让标识的不同层级对应可理解类别，同时在潜空间中减少表示重叠。

### TL;DR（核心摘要）

`物品语义与层次标签 → HiD-VAE → 层次SID/标签ID → Transformer → 推荐物品`

离线阶段用文本表示和层次标签训练监督 VAE：标签对齐与标签预测约束各量化层的语义粒度，唯一性损失惩罚不同物品的潜表示重叠。在线阶段冻结 tokenizer，Transformer 根据用户历史自回归生成 SID，并用约束解码映射到物品。

### 输入与使用场景

| 方面 | 说明 |
|---|---|
| 使用信息 | 物品文本、类别层次和用户交互 |
| 信息融入位置 | VAE 监督目标与生成模型输入 |
| 语义标识结构 | 层次化序列，并附带标签 ID |
| 适用场景 | 可解释序列推荐与冷启动 |

### 方法设计

#### 3.3 框架总览
HiD-VAE 分为离线层次 ID 学习和在线可解释推荐两阶段。第一阶段学习冻结的物品 tokenizer，第二阶段用 Transformer 根据用户历史生成语义 ID，同时预测或展示对应的层次标签。

#### 3.4 层次标签生成
对于缺少人工类别的数据，论文先使用 LLM 从物品文本和候选标签中生成层次标签。标签从粗粒度类别逐步细化，为不同 VAE 层提供监督信号。

#### 3.5 层次表示学习
HiD-VAE 在 RQ-VAE 的多级量化基础上加入标签对齐损失和标签预测损失，使每一层承担特定语义粒度。重构和量化损失保证表示可恢复，标签监督保证层次可解释。

#### 3.6 解耦与唯一性损失
唯一性损失直接惩罚不同物品潜表示的重叠，减少 ID collision。训练后在线生成阶段采用约束解码，只保留码本中存在且能对应真实物品的标识。

### 实验结论

- HiD-VAE 在三个公开数据集上提升了推荐效果和标识可解释性。
- 层次监督改善了语义层次，唯一性损失降低了 ID 碰撞。
- 对缺少类别标签的数据，论文使用 LLM 生成层次标签。

### 局限性与研究定位

#### 局限性
- 依赖离线标签生成和 tokenizer 更新。
- 约束自回归解码仍存在延迟。
- 真实动态目录和线上效果未充分验证。

#### 研究定位
HiD-VAE 将“可解释层次”和“低碰撞”作为 SID 的联合目标，适合放在“可解释语义标识学习”章节。

### 相关资源

- [论文原文](https://arxiv.org/abs/2508.04618)

### 标签

`层次监督` · `解耦表示` · `唯一性损失` · `可解释推荐`

### 架构图来源

*图源：原论文，图2。图片使用许可待核实。*

---

### 旧总表补充

来源：`d61aa6c:tables/all-methods.md`。

- 核心贡献：学习可解释且低碰撞的SID。
- 使用场景：可解释推荐。

## Same cell: II × Tokenization (11 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [CID](cid.md) | SIGIR-AP’23 | `CF` → **`Spectral Clus.`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [TransRec](transrec.md) | KDD’24 | `Text` → **`Multi-Facet ID`** → `Enc-Dec / Dec-Only` → `Fixed / NTP` → `FM-Index+Agg.` |
| [PSI](psi.md) | arXiv’25 | `Text` → **`Post-hoc RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam` |
| [AdaSID](adasid.md) | arXiv’26 | `Text+Img` → **`RQ`** → `Dec-Only` → `Fixed / NTP` → `C-Beam` |
| [API](api.md) | arXiv’26 | `Text` → **`PID (P-SAE)`** → `Enc-Dec / Dec-Only (AR); Non-AR (PR)` → `Fixed / NTP + Rank + Aux. / MTP + Rank + Aux.` → `C-Beam / Scoring` |
| [CARD](card.md) | arXiv’26 | `Text+Img+CF` → **`NU-RQ`** → `Enc-Dec` → `Fixed / NTP` → `C-Beam` |
| [DIGER](diger.md) | SIGIR’26 | `Text` → **`Learn. RQ`** → `Enc-Dec` → `Joint / NTP` → `Beam†` |
| [Gwhere](gwhere.md) | RecSys’26 | `Text+Img+Geo+CF` → **`Contr. RQ`** → `Dec-Only` → `Fixed / NTP → DPO` → `–` |
| [QuaSID](quasid.md) | KDD’26 ADS | `Text+CF` → **`QA-RQ`** → `Enc-Dec` → `Fixed / NTP` → `Beam†` |
| [R3-VAE](r3-vae.md) | arXiv’26 | `Text` → **`Ref.-RQ`** → `–` → `Fixed / NTP` → `Beam` |
| [SnapLGR](snaplgr.md) | arXiv’26 | `Text+Img+CF` → **`RQ-VAE+PPR`** → `Dec-Only` → `Fixed / Multi-task NTP` → `Beam` |
