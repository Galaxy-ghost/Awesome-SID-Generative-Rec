# OneRec-V2-Quantized

*Quantized Inference for OneRec-V2* — Su et al., arXiv’26

[arXiv](https://arxiv.org/abs/2603.11486) · [Record](../../data/papers/onerec-v2-quantized.yaml) · [← Catalog](../../README.md#v--inference)

> 新增可区分的 FP8 PTQ 与执行栈/算子设计，适合单独 V × Inference 条目，而非只重复 OneRec-V2。

| Problem it fixes | Stage it changes |
| :-- | :-- |
| **V. Efficiency**: Can it be trained and served within latency and cost budgets? | **Inference** |

## Pipeline

| Representation | Tokenization | Backbone | Training | Inference |
| :-: | :-: | :-: | :-: | :-: |
| `Text+Img+CF†` | `R-KM†` | `Lazy Dec-Only†` | `Fixed† / NTP → RL†` | **`FP8+RecoGEM`** |

- `Lazy Dec-Only†`: 主生成模块以lazy decoder-only处理长历史，后两码用轻量顺序条件模块。
- `FP8+RecoGEM`: FP8 权重/激活 PTQ 加直接构建 TensorRT 图及专门 TopK、attention、MoE 算子。

## Same cell: V × Inference (5 more)

| Paper | Venue | Pipeline |
| :-- | :-- | :-- |
| [AtSpeed](atspeed.md) | ICLR’25 | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Spec. Dec.`** |
| [NEZHA](nezha.md) | WWW’26 Industry | `Text` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Self-Draft+Hash`** |
| [PAD-Rec](pad-rec.md) | arXiv’26 | `Text+SID` → `RQ-VAE` → `Dec-Only` → `Fixed / Multi-task NTP†` → **`Spec. Dec.`** |
| [PFA](pfa.md) | arXiv’26 | `–` → `–` → `Enc-Dec` → `– / –` → **`Beam`** |
| [STATIC](static.md) | KDD’26 ADS | `–` → `RQ-VAE` → `Dec-Only` → `Fixed / NTP` → **`Vec. C-Beam`** |
