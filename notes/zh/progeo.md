## At a Glance

Key Findings: 在工业数据集上，ProGEO 的 Hit@50 为 0.4243，RQ-Kmeans 为 0.4056；平均地理聚类距离为 25.41 km，RQ-OPQ 为 46.71 km（Table 1）。

### 1. 为什么重要

本地服务平台的推荐既要相关，也要在地理上去得了（Abstract）。语义码本只按内容给物品聚类。

> "existing semantic codebooks neglect geographic constraints, often resulting in recommendations that are semantically relevant yet geographically unreachable."（Abstract）（现有语义码本忽略地理约束，推荐结果语义相关却去不了。）

ProGEO 保留标准的语义码字，再加一个地理码字，编码每个 POI 相对其语义簇的位置。地理由此成为语义 ID（Semantic ID，SID）的一部分，而不是一个弱的辅助特征（Abstract，Sec. 1）。

### 2. 方法

```mermaid
flowchart LR
    A[POI 特征] --> B[两层语义码本]
    B --> C[地理质心坐标]
    C --> D[Geo-RoPE 层]
    D --> E[SID]
    E --> F[微调后的 LLM]
    F --> G[附近的 POI]
```

#### 语义层

前两层码本以余弦相似度为度量，对混合特征向量聚类，并把投影残差传给下一层（Sec. 3.1）。SID 由两层标准码本和一层地理码本组成（Fig. 2）。

#### 地理质心局部坐标

前两层 SID 相同的 POI 组成一个子集。这些 POI 的实际经纬度确定一个地理质心，每个 POI 的全局位置换算成围绕这个质心的极坐标（Sec. 1，Sec. 3.2）。

#### Geo-RoPE

Geo-RoPE 把每个 POI 相对质心的偏移，编码为对第二层残差的复数旋转（Sec. 1，Sec. 3.3）。两个旋转后向量的相似度因此同时取决于语义因素和空间关系。

> "We extend RoPE to the spatial domain, formalizing geographic proximity as rotary operations in high-dimensional feature space."（Sec. 3.3）（把 RoPE 推广到空间域，把地理邻近写成高维特征空间里的旋转。）

#### 生成

在工业场景中，LLM 的提示包含搜索词、城市和用户位置的 GeoHash（Table 4）。

### 3. 实验发现

- Geo-RoPE 放在哪一层：只在第三层聚类上用 Geo-RoPE，CUR（7.67%）和 ICR（57.08%）在所试的位置中最高（Sec. 4.3.2，Fig. 5）。
- 案例：用了 Geo-RoPE，推荐的 POI 离用户近；不用的变体会推荐另一个城市的 POI（Sec. 4.5.2）。

  > "when Geo-RoPE is introduced, the recommended POIs are concentrated much closer to the user, typically within a 6-kilometer radius."（Sec. 4.5.2）（推荐的 POI 通常在用户 6 公里范围内。）

### 4. 局限与分析

**Our analysis.**

- 地理信号只进入 SID 的第三个 token。由此推断，生成器在用到任何空间信息之前，已经先选定了语义簇。
- OneLoc 用普通 `R-KM` 码；ProGEO 在同类编号器上加了一层地理码本（`R-KM+Geo-CB`）。
- GNPR-SID 也在 POI SID 中编码地理（`Attr+Geo+CF`），但用普通 `RQ-VAE`，没有专门的地理码本层。
