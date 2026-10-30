#!/usr/bin/env python3
"""Verify pinned arXiv HTML evidence anchors, section/subject heuristics, and metric table cell bindings."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import tempfile
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / 'data'
DEFAULT_CACHE_DIR = ROOT / '.cache' / 'sources'
VOID = {
    'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
    'meta', 'param', 'source', 'track', 'wbr',
}
BASELINE_HEADING_RE = re.compile(
    r'\b(baselines?|related\s+work|prior\s+work|compared\s+methods?|competitors?|literature\s+review)\b',
    re.I,
)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def normalize(text):
    return ' '.join(text.split())


def expand_table_spans(raw_rows):
    """Expand rowspan and colspan into a rectangular grid of cell strings."""
    grid = []
    carry = {}
    for r_idx, row in enumerate(raw_rows):
        out_row = []
        c_idx = 0
        while (r_idx, c_idx) in carry:
            out_row.append(carry.pop((r_idx, c_idx)))
            c_idx += 1
        for text, rspan, cspan in row:
            while (r_idx, c_idx) in carry:
                out_row.append(carry.pop((r_idx, c_idx)))
                c_idx += 1
            for dc in range(cspan):
                out_row.append(text)
                for dr in range(1, rspan):
                    carry[(r_idx + dr, c_idx + dc)] = text
            c_idx += cspan
        while (r_idx, c_idx) in carry:
            out_row.append(carry.pop((r_idx, c_idx)))
            c_idx += 1
        if any(cell != '' for cell in out_row):
            grid.append(out_row)
    return grid


def extract_sentence(context, quote):
    idx = context.find(quote)
    if idx < 0:
        return ''
    masked = context
    for abbr in ('et al.', 'e.g.', 'i.e.', 'vs.', 'Fig.', 'Tab.', 'Sec.', 'Eq.', 'No.', 'Dr.', 'Prof.'):
        masked = re.sub(re.escape(abbr), lambda m: m.group(0)[:-1] + '_', masked, flags=re.I)
    masked = re.sub(r'(\d)\.(\d)', r'\1_\2', masked)
    masked = re.sub(r'(\d)\.(\d)', r'\1_\2', masked)
    start = idx
    while start > 0 and masked[start - 1] not in '.!?•':
        start -= 1
    end = idx + len(quote)
    while end < len(masked) and masked[end] not in '.!?•':
        end += 1
    if end < len(context) and context[end] in '.!?':
        end += 1
    return context[start:end].strip()


def parse_cell_numeric(cell_text):
    """Parse numeric value and inferred unit ('%' or 'ratio') from a table cell string."""
    cleaned = cell_text.strip()
    is_pct = '%' in cleaned
    m = re.search(r'[-+]?\d+(?:\.\d+)?', cleaned)
    if not m:
        return None, None
    return float(m.group(0)), ('%' if is_pct else 'ratio')


class RichElementsParser(HTMLParser):
    def __init__(self, wanted):
        super().__init__(convert_charrefs=True)
        self.wanted = set(wanted)
        self.stack = []
        self.active = []
        self.found = {}
        self.section_paths = {}
        self.tables = {}
        self.all_text = []
        self.headings = {}
        self.in_heading = None
        self.active_tables = []

    def current_section_path(self):
        return [self.headings[k] for k in sorted(self.headings) if self.headings[k]]

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in VOID:
            return
        self.stack.append(tag)
        depth = len(self.stack)
        if re.fullmatch(r'h[1-6]', tag):
            level = int(tag[1])
            for k in list(self.headings):
                if k >= level:
                    del self.headings[k]
            self.in_heading = (depth, level, [])
        eid = attrs.get('id')
        if eid in self.wanted:
            self.active.append((depth, eid, [], self.current_section_path()))
            self.active_tables.append([depth, eid, [], None, None, None])
        for t in self.active_tables:
            if tag == 'tr' and t[3] is None:
                t[3] = []
            elif tag in ('td', 'th') and t[3] is not None and t[4] is None:
                try:
                    rspan = max(1, int(attrs.get('rowspan', '1') or '1'))
                except ValueError:
                    rspan = 1
                try:
                    cspan = max(1, int(attrs.get('colspan', '1') or '1'))
                except ValueError:
                    cspan = 1
                t[4] = ([], rspan, cspan)
                t[5] = depth

    def handle_endtag(self, tag):
        if tag not in self.stack:
            return
        end = len(self.stack) - self.stack[::-1].index(tag)
        if self.in_heading and self.in_heading[0] >= end:
            _, level, chunks = self.in_heading
            htext = normalize(''.join(chunks))
            if htext:
                self.headings[level] = htext
            self.in_heading = None

        for t in self.active_tables:
            if t[4] is not None and end <= t[5]:
                chunks, rspan, cspan = t[4]
                cell_txt = normalize(''.join(chunks))
                t[3].append((cell_txt, rspan, cspan))
                t[4] = None
                t[5] = None
            if tag == 'tr' and t[3] is not None and end <= len(self.stack):
                if t[3]:
                    t[2].append(t[3])
                t[3] = None

        kept_tables = []
        for t in self.active_tables:
            if t[0] >= end:
                if t[2]:
                    self.tables[t[1]] = expand_table_spans(t[2])
            else:
                kept_tables.append(t)
        self.active_tables = kept_tables

        kept = []
        for depth, key, chunks, spath in self.active:
            if depth >= end:
                self.found[key] = normalize(''.join(chunks))
                self.section_paths[key] = spath
            else:
                kept.append((depth, key, chunks, spath))
        self.active = kept
        self.stack = self.stack[:end - 1]

    def handle_data(self, data):
        self.all_text.append(data)
        if self.in_heading is not None:
            self.in_heading[2].append(data)
        for _, _, chunks, _ in self.active:
            chunks.append(data)
        for t in self.active_tables:
            if t[4] is not None:
                t[4][0].append(data)


def parse_html(raw, wanted):
    parser = RichElementsParser(wanted)
    parser.feed(raw.decode('utf-8'))
    parser.close()
    return (
        parser.found,
        parser.section_paths,
        parser.tables,
        normalize(''.join(parser.all_text)),
    )


def load_known_method_names(papers_dir):
    names = {}
    if papers_dir.is_dir():
        for p in sorted(papers_dir.glob('*.yaml')):
            rec = yaml.safe_load(p.read_text(encoding='utf-8'))
            if isinstance(rec, dict) and rec.get('id') and rec.get('name'):
                names[rec['id']] = rec['name']
    return names


def verify_table_binding(metric_entry, evidence_map, anchor_lookup):
    tb = metric_entry.get('table_binding') or {}
    ev_id = tb.get('evidence_id')
    ev = evidence_map.get(ev_id, {})
    anchor = anchor_lookup.get(ev_id, {})
    grid = anchor.get('table_grid') or []
    col_idx = tb.get('column_index')
    row_label = tb.get('row_label')
    col_path = tb.get('column_path') or []
    expected_cell = tb.get('cell_text')
    expected_num = tb.get('numeric_value')
    expected_unit = tb.get('unit')

    matched_row = None
    for row in grid:
        if row and row[0] == row_label:
            matched_row = row
            break

    observed_cell = None
    if matched_row is not None and isinstance(col_idx, int) and 0 <= col_idx < len(matched_row):
        observed_cell = matched_row[col_idx]

    header_cells = []
    if grid and isinstance(col_idx, int):
        for r in grid[:max(1, len(col_path))]:
            if 0 <= col_idx < len(r):
                header_cells.append(r[col_idx])

    parsed_num, parsed_unit = parse_cell_numeric(observed_cell or '')
    checks = {
        'evidence_anchor_ok': bool(anchor.get('ok')),
        'version_matches': tb.get('source_version') == ev.get('version'),
        'element_matches': tb.get('table_element_id') == ev.get('element_id'),
        'header_path_matches': header_cells == col_path,
        'row_found': matched_row is not None,
        'cell_text_matches': observed_cell == expected_cell,
        'numeric_value_matches': (
            parsed_num is not None
            and expected_num is not None
            and abs(parsed_num - float(expected_num)) < 1e-9
            and abs(float(metric_entry.get('value', -999999.0)) - float(expected_num)) < 1e-9
        ),
        'unit_matches': parsed_unit == expected_unit == metric_entry.get('unit'),
    }
    return {
        'metric_id': metric_entry.get('id'),
        'record_id': metric_entry.get('record_id'),
        'evidence_id': ev_id,
        'table_element_id': tb.get('table_element_id'),
        'row_label': row_label,
        'column_path': col_path,
        'column_index': col_idx,
        'expected_cell_text': expected_cell,
        'observed_cell_text': observed_cell,
        'observed_header_path': header_cells,
        'parsed_numeric_value': parsed_num,
        'parsed_unit': parsed_unit,
        'ok': all(checks.values()),
        'checks': checks,
    }


def ensure_cached_source(source_dir, skey, entries, auto_download=True):
    """Locate cached HTML in source_dir or download by pinned arXiv version if missing."""
    primary = source_dir / f'{skey}.html'
    ver = entries[0][1].get('version', '') if entries else ''
    by_ver = source_dir / f'{ver}.html' if ver else None
    if primary.is_file():
        return primary
    if by_ver and by_ver.is_file():
        return by_ver
    if not auto_download or not ver:
        return primary
    source_dir.mkdir(parents=True, exist_ok=True)
    url = f'https://arxiv.org/html/{ver}'
    subprocess.run(
        [
            'curl', '-L', '--fail', '--silent', '--show-error',
            '--max-time', '45', url, '-o', str(primary),
        ],
        check=True,
    )
    if by_ver and by_ver != primary and not by_ver.exists():
        by_ver.write_bytes(primary.read_bytes())
    return primary


def verify(evidence, metrics, source_dir=None, evidence_path=None, metrics_path=None, papers_dir=None, auto_download=False):
    source_dir = Path(source_dir) if source_dir is not None else DEFAULT_CACHE_DIR
    evidence_path = Path(evidence_path) if evidence_path is not None else (DATA_DIR / 'evidence.json')
    metrics_path = Path(metrics_path) if metrics_path is not None else (DATA_DIR / 'metrics.json')
    papers_dir = papers_dir or (DATA_DIR / 'papers')
    record_names = load_known_method_names(papers_dir)
    all_method_names = sorted(
        set(record_names.values()) | {'VQ-Rec', 'TIGER', 'LC-Rec', 'SASRec', 'BERT4Rec', 'GRU4Rec'},
        key=len,
        reverse=True,
    )

    report = []
    by_source = {}
    for eid, entry in evidence.items():
        skey = entry.get('source_key') or entry.get('record_id')
        by_source.setdefault(skey, []).append((eid, entry))

    anchor_lookup = {}
    for skey, entries in sorted(by_source.items()):
        path = ensure_cached_source(source_dir, skey, entries, auto_download=auto_download)
        if not path.is_file():
            for eid, entry in entries:
                item = {
                    'id': eid,
                    'record_id': entry.get('record_id'),
                    'source_key': skey,
                    'ok': False,
                    'reason': 'source missing',
                }
                report.append(item)
                anchor_lookup[eid] = item
            continue
        raw = path.read_bytes()
        found, spaths, tables, text = parse_html(raw, [e['element_id'] for _, e in entries])
        version = re.search(r'arXiv:\s*(\d{4}\.\d{4,5}v\d+)', text)
        for eid, entry in entries:
            elem_id = entry['element_id']
            context = found.get(elem_id, '')
            spath = spaths.get(elem_id, [])
            sent = extract_sentence(context, entry['quote'])
            heading_hit = any(BASELINE_HEADING_RE.search(h) for h in spath)
            own_name = record_names.get(entry.get('record_id'), '')
            cleaned_sent = re.sub(r'^[\s•\-\d\)\(\.]+', '', sent)
            competing_subject = None
            for mname in all_method_names:
                if own_name and mname.lower() == own_name.lower():
                    continue
                if re.match(rf'^{re.escape(mname)}\b', cleaned_sent):
                    competing_subject = mname
                    break
            needs_subject_review = bool(heading_hit or competing_subject)
            checks = {
                'quote_present_in_element': entry['quote'] in context,
                'quote_hash': digest(entry['quote'].encode('utf-8')) == entry['quote_sha256'],
                'context_hash': digest(context.encode('utf-8')) == entry.get('context_sha256'),
                'version': bool(version and version.group(1) == entry['version']),
                'html_sha256': digest(raw) == entry.get('source_html_sha256'),
            }
            item = {
                'id': eid,
                'record_id': entry.get('record_id'),
                'source_key': skey,
                'ok': all(checks.values()),
                'checks': checks,
                'observed_html_sha256': digest(raw),
                'source': entry['url'],
                'element_id': elem_id,
                'section_path': spath,
                'sentence': sent,
                'subject_heuristics': {
                    'baseline_or_related_section_hit': heading_hit,
                    'competing_sentence_subject': competing_subject,
                    'needs_subject_review': needs_subject_review,
                },
            }
            if elem_id in tables:
                item['table_grid'] = tables[elem_id]
            report.append(item)
            anchor_lookup[eid] = item

    metric_reports = [verify_table_binding(m, evidence, anchor_lookup) for m in metrics]
    return {
        'scope': (
            'quote existence + pinned version + HTML/context hashes + section/sentence subject heuristics '
            '+ HTML table cell coordinate and numeric value verification'
        ),
        'evidence_sha256': digest(evidence_path.read_bytes()),
        'metrics_sha256': digest(metrics_path.read_bytes()),
        'passed': sum(r['ok'] for r in report),
        'total': len(report),
        'metrics_passed': sum(m['ok'] for m in metric_reports),
        'metrics_total': len(metric_reports),
        'checks': report,
        'metric_table_checks': metric_reports,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        '--source-dir',
        type=Path,
        default=DEFAULT_CACHE_DIR,
        help='directory for cached arXiv HTML sources (default: .cache/sources)',
    )
    ap.add_argument(
        '--fetch',
        action='store_true',
        help='force re-download of pinned arXiv HTML versions into a temporary directory',
    )
    ap.add_argument(
        '--no-download',
        action='store_true',
        help='do not download missing HTML files when reading from --source-dir',
    )
    ap.add_argument('--evidence', type=Path, default=DATA_DIR / 'evidence.json')
    ap.add_argument('--metrics', type=Path, default=DATA_DIR / 'metrics.json')
    ap.add_argument('--output', type=Path, default=DATA_DIR / 'source-verification.json')
    args = ap.parse_args()

    evidence = json.loads(args.evidence.read_text(encoding='utf-8'))
    metrics = json.loads(args.metrics.read_text(encoding='utf-8'))
    if args.fetch:
        with tempfile.TemporaryDirectory(prefix='sid-repo-source-') as temp:
            source_dir = Path(temp)
            result = verify(
                evidence,
                metrics,
                source_dir,
                args.evidence,
                args.metrics,
                auto_download=True,
            )
    else:
        result = verify(
            evidence,
            metrics,
            args.source_dir,
            args.evidence,
            args.metrics,
            auto_download=not args.no_download,
        )
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(
        f"Source anchors: {result['passed']}/{result['total']} passed; "
        f"metric table bindings: {result['metrics_passed']}/{result['metrics_total']} passed"
    )
    return 0 if (result['passed'] == result['total'] and result['metrics_passed'] == result['metrics_total']) else 1


if __name__ == '__main__':
    raise SystemExit(main())
