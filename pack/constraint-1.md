# 牵制 1：码位依赖 ↔ 生成因子分解（总状态：`Open`）

- **核心命题**：码位条件依赖（H(c_t | c_<t)）与生成解码因子分解（自回归链式、并行多头、迭代掩码去噪）相互牵制：残差层级码承载条件依赖时适配前缀条件分解，而正交/局部敏感哈希无序码适配并行独立输出头。
- **分层状态说明**：固定码消融层（在固定分词器下移除前缀条件或改用并行解码）已有单侧实证（Reported）；但“码怎么分配决定码位条件互信息与并行可分解性”的跨阶段双向机制仍缺同一主干与协议下的 2×2 正交对照，总等级维持 Open。
- **维持 `Open` 的原因**：现有文献分别验证了固定 RQ 码下移除前缀条件的退化（SID-MLP）与固定并行解码器下切换 LSH/OPQ/RQ 的差异（FLASH、RPG），但尚无工作在同一主干、同一商品目录与切分协议下完成「可控码位互信息分词器 × 自回归/并行/掩码因子分解」的 2×2 正交对照实验。
- **升级门禁条件**：至少 1 组经独立复核的 2×2 正交对照实验（同一主干与评测协议下交叉改变码本依赖结构与生成因子分解），并提供可复核的原文元素与表格单元格锚点。

## 已核验单侧与局部证据（Reported Observations）
| 编号 | 来源 | 机制方向 | 等级 | 原文元素锚点 | 摘要 |
| --- | --- | --- | --- | --- | --- |
| `c1-ar-hierarchy` | `tiger` | Hierarchical RQ-VAE code -> autoregressive prefix factorization | `Reported` | `2305.05065v3#abstract1.1` | TIGER 将物品编码为语义层级残差码元组，并用 Transformer sequence-to-sequence 模型按从粗到细前缀自回归逐位预测。 |
| `c1-parallel-independence` | `rpg` | Unordered OPQ sub-tokens -> parallel MTP factorization | `Reported` | `2506.05781v1#S2.SS2.SSS1.p1.1` | RPG 采用 OPQ 将嵌入划分为多个无序子空间码位，并在单步解码中对全部码位的对数似然独立求和（MTP）。 |
| `c1-rq-counterexample` | `rpg` | Swapping OPQ -> RQ inside parallel MTP + graph decoding degrades accuracy | `Reported` | `2506.05781v1#S3.T3`, `2506.05781v1#S3.SS4.p2.1` | RPG 3.4 节（#S3.SS4.p2.1）与 Table 3（#S3.T3）在保持 MTP 并行预测与图解码不变时将 OPQ 替换为 RQ，Beauty NDCG@10 从 0.0464 降至 0.0421。 |
| `c1-masked-coupling` | `llada-rec` | Inter-token dependency -> bidirectional parallel masked diffusion | `Reported` | `2511.06254v1#abstract1.1` | LLaDA-Rec 指出固定自左向右自回归会限制多码位双向耦合建模，改用双向注意力掩码扩散迭代去噪生成完整 SID。 |
| `c1-sidmlp-prefix-ablation` | SID-MLP (arXiv:2605.12617v1) | Fixed RQ-VAE code + removing prefix conditioning in parallel heads -> severe degradation | `Reported` | `2605.12617v1#S4.SS3.p2.1` | SID-MLP 4.3 节（#S4.SS3.p2.1）在固定 RQ-VAE 码下移除并行预测头间的前缀嵌入条件（G1 w/o prefix conditioning），NDCG@10 下降 64–72%。 |
| `c1-flash-lsh-parallel` | FLASH (arXiv:2610.07402v1) | Unordered SimHash/LSH tokens align with parallel decoding (LSH > OPQ > RQ-VAE) | `Reported` | `2610.07402v1#S3.SS2.p3.1` | FLASH 3.2 节（#S3.SS2.p3.1）表明 SimHash 生成的无序独立码位天然适配并行解码，在固定并行解码主干下替换码本表现为 LSH > OPQ > RQ-VAE。 |
