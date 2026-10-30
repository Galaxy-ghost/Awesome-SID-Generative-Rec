# SID 生成式推荐：确定性核验骨架（Living Review Skeleton）

## 覆盖回执（Coverage Receipt）
- 仓库有效记录总数：`96` 篇（其中 `in_table1: true` 共 `94` 篇，POI 领域共 `10` 篇）
- Problem II 主表收录：`10` 篇（阶段分布：`Tokenization 10 篇`；含 POI 论文 `1` 篇）
- 裁决档案条目数：`10` 条（全部通过 `submitted_by != reviewed_by` 独立复核与字段一致性校验）

## 核心页面与机器可读产物
- [Problem II：静态码本崩塌与前缀碰撞](problem-II.md)
- [牵制 1：码位依赖 ↔ 生成因子分解](constraint-1.md)
- [回答页：Trie 能消除出词表 ID，但不能消除同码碰撞](answer-trie-collisions.md)
- [answer-pack.json](answer-pack.json)：供检索与智能体消费的结构化答案包
- [effective-records.jsonl](effective-records.jsonl)：全量有效论文记录快照
