# DOS 打标裁决（leader，10-30）

两家各自独立打标：`claude-dos.md`、`codex-dos.md`。

| 列 | Claude | Codex | 裁决 | 理由 |
|---|---|---|---|---|
| 毛病 | III（备选 I） | III | **III** | 两家一致。DFI 修 III，ORQ 修 I，按第一项贡献 DFI 取 III |
| 阶段 | Tokenization | Tokenization | **Tokenization** | 一致 |
| Representation | Text+CF | Text+CF | **Text+CF** | 一致 |
| Tokenization | Orth. RQ | ORQ | **Orth. RQ**（加粗，新写法） | 跟表里 Hier. RQ、Learn. RQ、Ref.-RQ 的缩写方式一致 |
| Backbone | Dec-Only（备选 HSTU） | HSTU，或 Dec-Only† | **Dec-Only†** | 原文只写 HSTU，没有报告架构细节；按 HSTU 原作的因果自回归设置推定为 Dec-Only，按表里的惯例用 † 标"推定" |
| Tokenizer | Fixed | Fixed†（备选 Joint） | **Fixed†** | 两段式流程，原文没说 HSTU 训练时是否更新编号器，所以是推定 |
| Objective | NTP（问要不要加 †） | NTP | **NTP** | §3.2.2 明确写了 next-token prediction，不加 † |
| Inference | – | – | **–** | 一致，原文未报告 |
