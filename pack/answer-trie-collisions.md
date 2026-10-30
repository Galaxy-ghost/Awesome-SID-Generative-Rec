# 回答页：Trie 能消除出词表 ID，但不能消除同码碰撞

## 条件化决策规则（Decision Rules）
| 规则 ID | 适用条件 | 处置建议 | 证据等级 | 原文锚点 | 边界说明 |
| --- | --- | --- | --- | --- | --- |
| `rule-trie-not-resolver` | 解码器挂前缀树（Trie）或合法前缀掩码约束 | Trie 只能保证生成的码序列落在目录合法前缀集合内（消除出词表 ID），不能区分落入同一叶节点的多个碰撞物品。 | `Deduction` | `2508.04618v2#S4.SS1.p6.1` | HiD-VAE 4.1 节明确说明 prefix tree 仅约束生成已知物品的合法 ID。 |
| `rule-change-code` | 允许修改或重训分词器与码本分配策略 | 优先在 Tokenization 阶段压低同码碰撞率：可采用分层监督与解耦均匀损失（HiD-VAE）、精确弹性匹配或重分配（PSI）、分布对齐正则（DIGER）或对比残差量化（CARD）。 | `Reported` | `2508.04618v2#abstract1.1`, `2509.16446v1#abstract1.1`, `2601.19711v3#abstract1.1`, `2604.26427v1#abstract1.1` | 四篇工作均在各自协议下报告了碰撞率下降或下游检索指标提升，但评测协议不同，不可直接跨文混排数值。 |
| `rule-keep-code` | 当碰撞率较低且工程上不重训分词器时 | 保留现有碰撞码位，在解码器到达末层码桶后追加轻量桶内消歧头、候选重排器或 item-level 二次检索。 | `Deduction` | 无（纯流水线接口推断） | 该条为基于流水线接口的工程条件推断（Deduction），不绑定原文引文；注意 TIGER 原文 3.1 节追加额外位属于码本构造期的静态去重，而非推理期桶内消歧。 |
| `rule-poi-candidate` | 面向地理敏感 POI 推荐且存在空间网格聚集与细粒度区分冲突 | 将地理空间层次或软残差对比分配显式编码进 SID（如 GWhere），缓解高密度商圈内的前缀碰撞。 | `Reported` | `2607.26073v1#abstract1.1`, `2607.26073v1#S3.SS2.SSS2.p1.1` | 当 Problem II 有效记录集合包含 POI 领域论文时自动激活该条候选建议。 |

## 协议对齐的同桶可比指标（Comparable Metric Groups）

### 协议桶：`dataset=amazon-beauty, split=static-catalog, level=static-code-item-share, resolver=not_applicable, metric=id-collision-rate-pct`
| 记录 | 变体 | 数值 | 原文单元格 | 表格坐标 | 原文版本 |
| --- | --- | --- | --- | --- | --- |
| `hid-vae` | `HiD-VAE (Full)` | `2.1%` | `2.1%` | `Table 3 (S4.T3) [HiD-VAE (Full), Beauty]` | `2508.04618v2` |
| `hid-vae` | `w/o HS` | `5.8%` | `5.8%` | `Table 3 (S4.T3) [w/o HS, Beauty]` | `2508.04618v2` |
| `hid-vae` | `w/o DUL` | `17.5%` | `17.5%` | `Table 3 (S4.T3) [w/o DUL, Beauty]` | `2508.04618v2` |
| `hid-vae` | `RQ-VAE (reported in HiD-VAE Table 3)` | `18.7%` | `18.7%` | `Table 3 (S4.T3) [RQ-VAE, Beauty]` | `2508.04618v2` |

## 协议不完备或不可混排的独立指标（Isolated Non-Comparable Metrics）
| 记录 | 变体 | 指标与数值 | 协议五元组 | 原文单元格与坐标 | 禁止混排原因 |
| --- | --- | --- | --- | --- | --- |
| `psi` | `RQ-VAE-ECM` | `recall@5=0.0191 (ratio)` | `ds=amazon-beauty, split=leave-last-out, level=item-level-next-item, resolver=unknown` | `0.0191*` (`Table 5 #Sx4.T5 [RQ-VAE-ECM, Amazon-Beauty / Recall@5]`) | resolver is unknown (post-collision item resolution protocol unspecified) |
| `psi` | `RQ-VAE-RRS` | `recall@5=0.0187 (ratio)` | `ds=amazon-beauty, split=leave-last-out, level=item-level-next-item, resolver=unknown` | `0.0187*` (`Table 5 #Sx4.T5 [RQ-VAE-RRS, Amazon-Beauty / Recall@5]`) | resolver is unknown (post-collision item resolution protocol unspecified) |
