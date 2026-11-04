# Paper Records Schema

Each paper is stored as a single YAML file under `data/papers/<id>.yaml`.
Field names are defined once in [`schema/paper.schema.json`](paper.schema.json) and checked against [`data/vocab.yaml`](../data/vocab.yaml) by `scripts/check.py`.

## Commands

```sh
python3 scripts/check.py --write-i18n  # Record bilingual section hashes in data/i18n.yaml after editing paired docs
make build                             # Build English and Chinese READMEs, paper pages, indexes, comparisons, glossaries, and llms*.txt
make check                             # Validate records, Table 1 round-trip, links, updates, bilingual pairing, and awesome-lint
```

`make build` reads the YAML records and never synchronizes Table 1 automatically.
To import Table 1 columns explicitly, run `python3 scripts/build.py --sync-table1 path/to/main.tex path/to/supplementary.tex`.
Alternatively, set `TABLE1="path/to/main.tex path/to/supplementary.tex"` and run `python3 scripts/build.py --sync-table1`.
A synchronization with no source or a missing file fails.
Records are matched by `name`. A Table 1 row with no record fails; a record with no Table 1 row is kept with a warning.
Synchronization updates `venue`, `problem`, `stage`, and the six technical columns, and keeps the other fields.

For the Table 1 round-trip check, run `TABLE1="path/to/main.tex path/to/supplementary.tex" make check` or
`python3 scripts/check.py --table1 path/to/main.tex path/to/supplementary.tex`. An explicit path overrides `TABLE1`.
Without a source, the check prints `SKIP` for the Table 1 comparison and runs the other checks.

## Record Format

```yaml
id: tiger
name: TIGER
title: Recommender Systems with Generative Retrieval
authors: Rajput et al.
year: 2023
venue: NeurIPS’23
links:
  arxiv: https://arxiv.org/abs/2305.05065
  code: null
  code_third_party: https://github.com/baiyimeng/TIGER
problem: psb
stage: n/a
representation: Text
tokenization: RQ-VAE
backbone: Enc-Dec
tokenizer: Fixed
objective: NTP
inference: Beam
poi: false
tldr: TIGER encodes item text into RQ-VAE Semantic IDs and trains a Transformer encoder-decoder to decode the next item's
  ID, instead of retrieving items by approximate nearest neighbor search.
tldr_zh: TIGER 用 RQ-VAE 将物品文本编码为语义 ID（SID），并训练 Transformer 编码器-解码器自回归解码下一物品的 SID，替代近似最近邻检索。
setup:
  ...
  inference_budget: 'Autoregressive beam search; numerical beam width not reported. ...'
  ...
setup_where:
  ...
  inference_budget: 'Autoregressive beam search: https://arxiv.org/html/2305.05065v3#A5.p3; ...'
  ...
related:
- id: rpg
  relation: alternative
  note: RPG predicts long OPQ IDs in parallel and uses graph-constrained decoding, while TIGER generates RQ-VAE IDs autoregressively.
  where: 'Evidence is from the later RPG paper: Section 2 overview, https://arxiv.org/html/2506.05781v1#S2.p1; ...'
changes:
  representation: none
  tokenization:
    value: other
    quote: '...'
    where: '...'
  backbone:
    value: other
    quote: '...'
    where: '...'
  tokenizer: none
  objective: none
  inference:
    value: other
    quote: '...'
    where: '...'
modality:
- Text
domain:
- E-commerce
settings:
- value: cold-start
  scope: item
  quote: '...'
  where: '...'
```

- `problem`: `psb` (`Paradigms, Systems and Benchmarks`) or `I`–`VI` (`Informativeness`, `Uniqueness and Validity`, `SID–Model Alignment`, `Utility`, `Efficiency`, `Generalization`).
- `stage`: `n/a` (for `psb`) or one of `Representation`, `Tokenization`, `Backbone`, `Training`, `Inference`.
- Technical columns (`representation`, `tokenization`, `backbone`, `tokenizer`, `objective`, `inference`) are stored verbatim as in Table 1, including `†` (inferred) and `A / B` (dual-branch setups). Every value is defined in English (`description`) and Chinese (`description_zh`) in `data/vocab.yaml`.
- `poi`: `true` when the paper targets POI, local-life, or spatial recommendation.
- `links.code` is the authors' repository or `null`; `links.code_third_party` is an optional implementation by others.
- `tldr`: one English sentence that `README.md`, the English paper page, and `llms.txt` copy verbatim.
- `tldr_zh`: one Chinese sentence corresponding to `tldr`, used in `README.zh.md` and the Chinese paper page.
- `setup`: the setup card with seven fixed keys in this order: `datasets`, `split`, `candidates`, `visibility`, `sid`, `inference_budget`, `results_from`.
- `setup_where`: the paper location for each `setup` key; it appears only with `setup`.
- `related`: 1–5 links to other records, each with `id`, `relation` (`predecessor`, `successor`, `competitor`, or `alternative`), `note`, and `where`.
- `evidence`: an optional list of `{field, where, quote?, reason?}` items; each item has at least one of `quote` and `reason`.
- `changes`: mapping over the six technical columns (`representation`, `tokenization`, `backbone`, `tokenizer`, `objective`, `inference`). Each value is `primary`, `none`, or `{value: other, quote, where}`. Non-`psb` papers have exactly one `primary` matching `stage` (and the bolded cell in Table 1); `psb` papers have no `primary`.
- `modality`: SID tokenizer input modalities as a list of values from `data/vocab.yaml` (e.g. `[Text, CF]`) or a branch-name-to-list mapping (e.g. `{A: [Text], B: [Audio]}`). Optional companion fields: `modality_open` (list of open signals when `unknown` is present), `modality_where` (`{quote, where}`), and `note` (string).
- `domain`: non-empty list of application domains from `data/vocab.yaml`.
- `settings`: list of special evaluation settings (`{value, scope?, quote, where}`), where `value` is `cold-start` (requiring `scope: user` or `scope: item`), `cross-domain`, or `catalog-change`.
- Optional reading notes are stored in `notes/<id>.md` and `notes/zh/<id>.md`, paired section-by-section via `data/i18n.yaml`, and embedded into `pages/papers/<id>.md` and `pages/zh/papers/<id>.md` during `make build`.
- Optional architecture diagrams are stored as `architectures/<id>.png`, matching the record ID exactly. `make build` embeds each existing diagram into its paper page; no YAML field is needed.
