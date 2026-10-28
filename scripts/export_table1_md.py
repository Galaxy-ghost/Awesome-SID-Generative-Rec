#!/usr/bin/env python3
"""Generate Table 1 as a Markdown table from data/papers/*.yaml.

Rows are the records with in_table1: true; layout rules are in schema/README.md
("Table 1 view"). With --check, the generated table is compared cell by cell
with the table under "## Table 1" in the given Markdown file.

Usage:
  python3 scripts/export_table1_md.py [--root DIR] [--out FILE]
  python3 scripts/export_table1_md.py --check PATH/TO/Table1_扩展版.md
Exit status with --check: 0 when every cell matches, 1 otherwise.
"""
import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
COLUMNS = [('Representation', 'representation'), ('Tokenization', 'tokenization'),
           ('Backbone', 'backbone'), ('Tokenizer', 'tokenizer'),
           ('Objective', 'objective'), ('Inference', 'inference')]
HEADER = ['Method', 'Venue'] + [title for title, _ in COLUMNS]
TOP_BLOCK_TITLE = 'Paradigms, Systems and Benchmarks'
PSB_ORDER = ['baseline', 'paradigm', 'framework']
BASELINE_MARK = '（基线）'  # literal used by the source table
SURVEY_MARK = {'table1': '', 'text': '★‡ ', 'none': '★ '}


def load(root):
    vocab = yaml.safe_load((root / 'data/vocab.yaml').read_text(encoding='utf-8'))
    records = [yaml.safe_load(p.read_text(encoding='utf-8'))
               for p in sorted((root / 'data/papers').glob('*.yaml'))]
    return vocab, [r for r in records if r['in_table1']]


def arxiv_key(rec):
    ax = rec['external'].get('arxiv')
    if not ax:
        return (1, 0, 0, rec['name'])
    yymm, num = ax.split('.')
    return (0, int(yymm), int(num), rec['name'])


def render_label(label, bold):
    values = label['value'] if isinstance(label['value'], list) else [label['value']]
    inferred = label.get('inferred', False)
    if not isinstance(inferred, list):
        inferred = [inferred] * len(values)
    text = ' / '.join(v + ('†' if i else '') for v, i in zip(values, inferred))
    return f'**{text}**' if bold else text


def render_row(rec):
    name = rec['name']
    if rec['survey'] != 'table1':
        name = f'{SURVEY_MARK[rec["survey"]]}[{name}](https://arxiv.org/abs/{rec["external"]["arxiv"]})'
    method = f'{name} ({rec["citation"]})'
    if rec.get('psb_kind') == 'baseline':
        method += BASELINE_MARK
    stage = rec['labels']['stage']['value']
    bold_label = {'Representation': 'representation', 'Tokenization': 'tokenization',
                  'Backbone': 'backbone', 'Training': rec.get('training_change'),
                  'Inference': 'inference'}.get(stage) if rec['record_type'] == 'method' else None
    cells = [method, rec['external']['venue']]
    cells += [render_label(rec['labels'][key], key == bold_label) for _, key in COLUMNS]
    return cells


def build_rows(vocab, records):
    """Return the table body as lists of cells, band rows included."""
    stage_rank = {e['value']: i for i, e in enumerate(vocab['stage'])}
    blank = [''] * (len(HEADER) - 1)
    rows = [[f'**{TOP_BLOCK_TITLE}**'] + blank]
    top = [r for r in records if r['record_type'] == 'paradigm-system-benchmark']
    rows += [render_row(r) for r in sorted(top, key=lambda r: (PSB_ORDER.index(r['psb_kind']), arxiv_key(r)))]
    for entry in vocab['problem']:
        if 'name' not in entry:
            continue  # n/a, pending
        band = [r for r in records
                if r['record_type'] == 'method' and r['labels']['problem']['value'] == entry['value']]
        rows.append([f'**{entry["value"]}. {entry["name"]}**'] + blank)
        band.sort(key=lambda r: (stage_rank[r['labels']['stage']['value']], arxiv_key(r)))
        rows += [render_row(r) for r in band]
    return rows


def to_markdown(rows):
    lines = [HEADER, ['---'] * len(HEADER)] + rows
    return '\n'.join('| ' + ' | '.join(cells) + ' |' for cells in lines) + '\n'


def read_source_table(path):
    """Lines of the Markdown table under '## Table 1'."""
    lines = path.read_text(encoding='utf-8').split('\n')
    start = lines.index('## Table 1')
    table = []
    for ln in lines[start + 1:]:
        if ln.startswith('|'):
            table.append(ln)
        elif table:
            break
    return table


def split_cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def check(generated_md, source_path):
    gen_lines = generated_md.rstrip('\n').split('\n')
    src_lines = read_source_table(source_path)
    gen = [split_cells(ln) for ln in gen_lines]
    src = [split_cells(ln) for ln in src_lines]
    print(f'source: {len(src) - 2} body rows; generated: {len(gen) - 2} body rows')
    problems = 0
    if gen[:2] != src[:2]:
        print('header differs:', gen[:2], src[:2])
        problems += 1
    gen_body, src_body = gen[2:], src[2:]
    gen_pos = {cells[0]: i for i, cells in enumerate(gen_body)}
    src_pos = {cells[0]: i for i, cells in enumerate(src_body)}
    for key in sorted(src_pos.keys() - gen_pos.keys(), key=src_pos.get):
        print(f'row only in source: {key}')
        problems += 1
    for key in sorted(gen_pos.keys() - src_pos.keys(), key=gen_pos.get):
        print(f'row only in generated: {key}')
        problems += 1
    cell_diffs = 0
    common = sorted(src_pos.keys() & gen_pos.keys(), key=src_pos.get)
    for key in common:
        s, g = src_body[src_pos[key]], gen_body[gen_pos[key]]
        if src_pos[key] != gen_pos[key]:
            print(f'row position differs: {key}: source {src_pos[key] + 1}, generated {gen_pos[key] + 1}')
            problems += 1
        for col, (sc, gc) in enumerate(zip(s, g)):
            if sc != gc:
                print(f'cell differs: {key} / {HEADER[col]}: source {sc!r}, generated {gc!r}')
                cell_diffs += 1
        if len(s) != len(g):
            print(f'cell count differs: {key}: source {len(s)}, generated {len(g)}')
            problems += 1
    compared = sum(len(src_body[src_pos[k]]) for k in common)
    print(f'cells compared: {compared}; differing cells: {cell_diffs}')
    identical = [ln.rstrip() for ln in gen_lines] == [ln.rstrip() for ln in src_lines]
    print(f'lines identical (ignoring trailing spaces): {"yes" if identical else "no"}')
    return problems + cell_diffs


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--root', type=Path, default=ROOT, help='repository root (default: this repository)')
    ap.add_argument('--out', type=Path, help='write the table here instead of stdout')
    ap.add_argument('--check', type=Path, metavar='MD', help='compare with the Table 1 in this Markdown file')
    args = ap.parse_args()
    vocab, records = load(args.root)
    md = to_markdown(build_rows(vocab, records))
    if args.check:
        return 1 if check(md, args.check) else 0
    if args.out:
        args.out.write_text(md, encoding='utf-8')
    else:
        sys.stdout.write(md)
    return 0


if __name__ == '__main__':
    sys.exit(main())
