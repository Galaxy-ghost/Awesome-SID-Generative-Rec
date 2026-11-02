## At a Glance

Limitation: 编号器只读协同嵌入，没有交互的物品就没有可编号的输入（Sec. 3.2.1）。

### 1. 为什么重要

现有做法通常把物品编号和生成式推荐分开训练（Abstract）。ETEGRec 用一个双编码器-解码器框架把两者连在一起（Abstract）。

> "To enable synergistic interaction between these components, we propose a recommendation-oriented alignment strategy, which includes two key optimization objectives: sequence-item alignment and preference-semantic alignment."（Abstract）（面向推荐的对齐包括序列-物品对齐和偏好-语义对齐两个目标。）

### 2. 方法

```mermaid
flowchart LR
    A[协同嵌入] --> B[RQ-VAE 编号器]
    B --> C[物品 token]
    C --> D[生成器]
    D --> E[对齐损失]
    E --> B
```

#### 物品编号器

编号器读入每个物品的协同嵌入（例如来自 SASRec），再做层级量化（Sec. 3.2.1）。

> "By taking a hierarchical scheme, we essentially organize the items in a tree-structured way, which is particularly suitable for generative tasks."（Sec. 3.2.1）（层级方案把物品组织成树，适合生成任务。）

#### 面向推荐的对齐

序列-物品对齐让编码器序列状态和目标物品嵌入量化后的 token 分布一致（Sec. 1，Eq. 15）。偏好-语义对齐把解码器给出的用户偏好和 RQ-VAE 重建的目标物品语义做对比（Sec. 1，Eq. 16）。

#### 交替优化

在编号器阶段，量化损失和两个对齐损失更新编号器，生成器保持不动（Sec. 3.4）。

> "In order to improve the training stability, we propose an alternating optimization strategy to mutually train the item tokenizer and the generative recommender."（Sec. 3.4）（用交替优化提高训练稳定性。）

### 3. 实验发现

- 主实验：ETEGRec 好于序列推荐基线和生成式基线（Abstract）。
- 新老用户：在 Instrument 和 Scientific 上，把交互最少的 5% 用户留作新用户，ETEGRec 在两组上都好于 LETTER 和 TIGER（Sec. 4.4.1，Fig. 2）。

### 4. 局限与分析

**Our analysis.**

- 更新编号器会在训练中改变物品的 token 序列。交替训练是论文对这种不稳定的处理办法。
- LETTER 也用 `Learn. RQ` 码，但在训练生成器之前就训练好；ETEGRec 把码和生成器一起训练。
