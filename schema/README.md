# Paper records

Neutral storage for the papers behind Table 1. Each record holds fields only;
README pages, tables and other views are generated from the records, so a
change of presentation does not touch the data.

| Path | Content |
| --- | --- |
| `data/papers/<id>.yaml` | one record per paper |
| `data/vocab.yaml` | allowed values for every label field |
| `schema/paper.schema.json` | JSON Schema of a record |
| `scripts/validate.py` | checks every record against the schema and the vocabulary |
| `scripts/export_table1_md.py` | regenerates Table 1 as Markdown and compares it with the source table |

Dependencies: Python 3 standard library and PyYAML.

```sh
python3 scripts/validate.py
python3 scripts/export_table1_md.py --check ~/Project/SID-Survey/材料/Table1_扩展版.md
```

Until the repository goes live, `材料/Table1_扩展版.md` in the SID-Survey project
stays the editing source of Table 1. The records were migrated from it and from
`材料/Table2_按仓库分类.md` on 2026-10-28.

## Primary key

`id` is the stable internal key and equals the file name.

1. Take the method name as written in Table 1, lower-case it, and replace every
   run of characters other than `a–z` and `0–9` with `-`; trim leading and
   trailing `-`. `HiD-VAE` → `hid-vae`, `Q-BERT4Rec` → `q-bert4rec`.
2. If that ID is taken, append `-<year>` (the venue year).
3. An ID never changes after it is assigned. When a method is renamed, keep the
   ID and put the old name in `aliases` (`adc-sid` keeps `MMQ-v2`).

arXiv ID, DOI, title, year, venue and links are external identifiers under
`external`; none of them is a key. The arXiv link is
`https://arxiv.org/abs/<external.arxiv>`.

## Record fields

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | yes | primary key, see above |
| `name` | yes | method name as in Table 1 |
| `aliases` | no | other names of the same paper |
| `record_type` | yes | `method` or `paradigm-system-benchmark` (the top block of Table 1) |
| `psb_kind` | for `paradigm-system-benchmark` only | `baseline` (TIGER), `paradigm` (all five stages replaced at once), `framework` (open-source framework, benchmark or analysis paper) |
| `citation` | when `in_table1` | short citation exactly as in Table 1, e.g. `Wang et al., 2024a` |
| `survey` | yes | presence in the original survey: `table1`, `text` (cited in the text only, ★‡) or `none` (★) |
| `in_repo_cards` | yes | the paper has a card under `papers/` (commit 705a11e) |
| `in_table1` | yes | the paper is a row of the current Table 1 |
| `external` | yes | `arxiv`, `doi`, `title` (optional); `year`, `venue` (required). `venue` keeps the track suffix, e.g. `KDD’26 ADS` |
| `labels` | yes | the eight labels below |
| `training_change` | when `labels.stage.value` is `Training` | `tokenizer` or `objective`: which split column the change is in |
| `settings` | when a label has per-setting values | names of the A / B settings, in order |
| `legacy_training` | no | the pre-10-26 single Training value from Table 2, kept while `tokenizer`/`objective` are `pending` |
| `note` | yes (may be empty) | free text |

The record type is stored apart from the problem label: `record_type` says what
kind of paper it is, `labels.problem` says which problem it fixes.

## Labels

| Label | Values |
| --- | --- |
| `problem` | `I`–`VI`, `n/a`, `pending` |
| `stage` | `Representation`, `Tokenization`, `Backbone`, `Training`, `Inference`, `n/a`, `pending` |
| `representation`, `tokenization`, `backbone`, `tokenizer`, `objective`, `inference` | the Table 1 columns of the same names; see `data/vocab.yaml` |

Every label is a mapping:

```yaml
inference:
  value: Beam            # a vocabulary value; a list for A / B rows
  inferred: true         # optional; Table 1 shows it as †
  source: §3.4, p6       # location in the paper or code, or the word missing
  status: verified       # verified | unverified
  note: ""
```

- `value` takes the exact Table 1 spelling, without `†`. Rows that run two
  setups (Table 1 writes `A / B`) store a list in the order of `settings`.
- `inferred` marks a value the paper does not state directly (`†` in Table 1).
  For list values it may be a list of booleans, one per setting.
- `source` gives the paper location (section, figure, equation, page, or a code
  path) that the appendices of `Table1_扩展版.md` attach to that cell; `missing`
  when the appendices give none. Sources are never filled in by guessing.
- `status` is `verified` when the appendices give a location, `unverified`
  otherwise. `verified` with `source: missing` is invalid.

Special values:

- `n/a`: no label by rule. `paradigm-system-benchmark` records carry
  `n/a` for `problem` and `stage`; so do records merged into another record.
- `pending`: not labeled yet. Not allowed in a Table 1 row.
- `–`: written in Table 1 for "not reported in the paper" or "not applicable"
  (e.g. `tokenizer: –` means no SID is built).

## Validation

`scripts/validate.py` reads the schema and the vocabulary and reports each error
with a category:

| Category | Check |
| --- | --- |
| `required` | required fields present, no unknown fields |
| `vocab` | every label value is in `data/vocab.yaml` |
| `id` | ID well-formed and equal to the file name; IDs, names/aliases and arXiv IDs unique |
| `source` | every label has a non-empty `source` (`missing` counts) |
| `status` | `status` is `verified` or `unverified`; `verified` needs a source |
| `rule` | `psb_kind`, `citation`, `training_change`, `settings` and `legacy_training` appear exactly when required; list lengths match `settings`; `paradigm-system-benchmark` records use `n/a`; no `pending` in Table 1 rows |

## Table 1 view

`scripts/export_table1_md.py` builds Table 1 from the records with
`in_table1: true`:

- Bands: the top block (`paradigm-system-benchmark`), then problems I–VI.
  Band titles come from `name` in `data/vocab.yaml`.
- Order inside the top block: `baseline`, `paradigm`, `framework`, each by
  arXiv ID. Inside a problem band: by stage (Representation → Inference), then
  by arXiv ID, which follows first posting.
- Bold: the column of the stage; for `Training`, the column named by
  `training_change`. The top block has no bold cells.
- Method cell: `★` / `★‡` and an arXiv link for papers not in the survey's
  Table 1, then `name (citation)`; TIGER gets the baseline mark.
