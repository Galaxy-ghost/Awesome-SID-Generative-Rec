### 1. 为什么重要

现有的生成式推荐（GR）模型对每个行为单独编号，同一个行为在任何序列里都得到相同的 token（Abstract）。作者认为，同一个行为放在不同的上下文里，意思可以不同（Abstract）。ActionPiece 让前后的行为决定一个行为怎样被编号。

> "However, existing GR models tokenize each action independently, assigning the same fixed tokens to identical actions across all sequences without considering contextual relationships."（Abstract）（现有 GR 模型孤立地给每个行为编号，不看上下文。）

### 2. 方法

```mermaid
flowchart LR
    A[行为序列] --> B[共现计数]
    B --> C[词表]
    C --> D[多种切分]
    D --> E[生成器]
```

#### 行为即特征集合

每个行为是一组无序的物品特征，用户历史就是一串特征集合（Abstract）。

#### 构建词表

合并计数既在单个集合内部做，也在相邻集合之间做（Abstract）。两类 token 对的权重不同（Sec. 1）。

> "Considering the structural differences between token pairs, e.g., whether they occur within a single set or between two adjacent sets, we assign different weights to different pairs."（Sec. 1）（集合内和跨集合的 token 对权重不同。）

#### 集合置换正则

特征集合没有顺序，所以集合置换正则可以把同一条行为序列切成多种语义相同的切分（Abstract）。这些切分在训练时用作数据增强，在推理时做集成（Sec. 3.2.2）。

### 3. 实验发现

- 词表大小：词表越大，推荐效果越好，归一化序列长度（NSL）越短（Sec. 4.4.1，Fig. 4）。作者把词表大小看作效果、序列长度和内存之间的权衡（Sec. 4.4.1）。
- 消融：提升不只来自词表变大（Sec. 4.3，Table 5）。

  > "These results suggest that the performance improvement of ActionPiece is not simply due to scaling the vocabulary size up or down."（Sec. 4.3）（提升不是单纯调大或调小词表带来的。）

- token 使用：同一物品按邻居得到不同的 token，提高了 token 的使用率，也起到数据增强的作用（Sec. 4.3）。
- 其他分析：论文还研究了 token 使用（Sec. 4.4.2）、集成数（Fig. 6）和案例（Sec. 4.5）。

### 4. 局限与分析

**Our analysis.**

- 推理时要对多种切分分别排序再平均分数。由此推断，除非并行处理，解码开销会随集成数增长。
- VQ-Rec 在 `Encoder` 上用 `OPQ` 码做 `Scoring`；ActionPiece 从同类的码出发，但用 `Enc-Dec` 生成器生成合并后的 token。
