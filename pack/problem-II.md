# Problem II：静态码本崩塌与前缀碰撞

当前 `problem: II` 且 `in_table1: true` 共 **10** 篇（阶段分布：**Tokenization 10 篇**）。

| 方法 | 引文 | 领域 | 阶段 | 分词器 | 推理约束 | 子问题 | 核心机制 | 证据等级 | 原文锚点 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `AdaSID` (`adasid`) | Pan et al., 2026 | General | Tokenization | `RQ` | `C-Beam` | 碰撞/混淆 | 自适应调节重合排斥 | 设计已述；效果等级未核 | `2604.23522v1#abstract1.1` |
| `CARD` (`card`) | Wei et al., 2026 | General | Tokenization | `NU-RQ` | `C-Beam` | 码字不均/生成偏差 | 非均匀量化 | 设计已述；效果等级未核 | `2604.26427v1#abstract1.1` |
| `CID` (`cid`) | Hua et al., 2023 | General | Tokenization | `Spectral Clus.` | `C-Beam` | 完整标识区分性 | 协同层次索引 | 设计已述；效果等级未核 | `2305.06569v6#abstract1.1` |
| `DIGER` (`diger`) | Fu et al., 2026 | General | Tokenization | `Learn. RQ` | `Beam` | 码本塌缩 | 可微构码与探索 | 设计已述；效果等级未核 | `2601.19711v3#abstract1.1` |
| `Gwhere` (`gwhere`) | Zhai et al., 2026 | POI | Tokenization | `Contr. RQ` | `–` | 冗余/同码碰撞，备选 I | 对比残差量化 | 设计已述；撞号解析与直接效果待核 | `2607.26073v1#abstract1.1` |
| `HiD-VAE` (`hid-vae`) | Fang et al., 2025 | General | Tokenization | `Hier. RQ` | `C-Beam` | 同码碰撞 | 层次监督与唯一性损失 | Reported：Table 3 消融 | `2508.04618v2#abstract1.1` |
| `PSI` (`psi`) | Zhang et al., 2025a | General | Tokenization | `Post-hoc RQ` | `Beam` | 同码碰撞 | ECM/RRS 重分配，避免追加随机尾码 | 设计已述；效果等级未核 | `2509.16446v1#abstract1.1` |
| `QuaSID` (`quasid`) | Hu et al., 2026 | General | Tokenization | `QA-RQ` | `Beam` | 有害/无害碰撞 | 资格筛选后的排斥 | 设计已述；效果等级未核 | `2603.00632v1#abstract1.1` |
| `R3-VAE` (`r3-vae`) | Wan et al., 2026 | General | Tokenization | `Ref.-RQ` | `Beam` | 训练不稳/码本塌缩 | 参考向量与量化稳定化 | 设计已述；效果等级未核 | `2604.11440v3#abstract1` |
| `TransRec` (`transrec`) | Lin et al., 2024 | General | Tokenization | `Multi-Facet ID` | `FM-Index+Agg.` | 标识区分性/生成合法性 | 多面标识与生成 grounding | 设计已述；效果等级未核 | `2310.06491v2#abstract1.1` |

## 范围边界说明（Scope Boundary Notes）
- `lgsid`：LGSID 虽在实验分析中报告碰撞率下降，但其主方法针对层级语义失配与空间协同对齐，经双盲裁决归入 Problem III × Representation，故不计入 Problem II 主表。（裁决日期：`2026-10-28`）
- `dos`：DOS 采用正交残差量化（Orth. RQ）与 Wasserstein 分布对齐解决跨域 POI 空间割裂与分布偏移，经双盲裁决归入 Problem III × Tokenization。（裁决日期：`2026-10-30`）
