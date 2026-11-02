### 1. 为什么重要

各家生成式推荐（GR）方案的建模技巧、超参数和实验设置各不相同，很难直接比较（Abstract）。GRID 把这些方案放进一个模块化框架，组件可以替换，也可以逐个消融。

> "Our comprehensive experiments with GRID reveal that many overlooked architectural components in GR models with SIDs substantially impact performance."（Abstract）（许多被忽视的结构组件对效果影响很大。）

### 2. 方法

```mermaid
flowchart LR
    A[物品内容] --> B[语义编码器]
    B --> C[SID 编号器]
    C --> D[生成器]
    D --> E[束搜索]
```

#### 先编号，再生成

GRID 把基于语义 ID（Semantic ID，SID）的 GR 分成编号和生成两个阶段（Sec. 3.1）。

#### 编号阶段的消融

研究改变编号算法、语义编码器的大小、残差层数 $`L`$ 和每层 token 数 $`W`$（Sec. 4.1）。

> "Unless otherwise noted, we use RK-Means with (L,W)=(3,256) and Flan-T5-XL."（Sec. 4.1）（默认配置是 RK-Means、(L,W)=(3,256) 和 Flan-T5-XL。）

#### 生成阶段的消融

研究改变用户 token 数、编码器-解码器与仅解码器、数据增强、去重 ID，以及约束与不约束的束搜索（Sec. 4.2）。

### 3. 实验发现

- 主要结论：几个被当作必需、往往还费算力或工程量的组件，可以换成更省的做法而效果不降（Sec. 5）。

  > "Conversely, other, often overlooked design choices prove to be vital, such as encoder-decoder architectures and data augmentation."（Sec. 5）（反过来，编码器-解码器结构和数据增强这类常被忽视的选择很关键。）

### 4. 局限与分析

**Our analysis.**

- 消融每次只在默认配置上改一个组件（Sec. 4.1）。由此推断，组件之间的交互没有覆盖到。
- TIGER 用 `RQ-VAE` 码；GRID 默认用 `R-KM` 码，和 OneRec 的编号方式相同。
