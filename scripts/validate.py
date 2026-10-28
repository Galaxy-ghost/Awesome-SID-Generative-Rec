#!/usr/bin/env python3
"""Validate data/papers/*.yaml.

Structure comes from schema/paper.schema.json and allowed label values from
data/vocab.yaml; this script keeps no copy of either. Checks:

  [required] required fields are present (and no unknown fields)
  [vocab]    every label value is in data/vocab.yaml
  [id]       IDs are well-formed, match the file name and are unique
             (names, aliases and arXiv IDs must be unique too)
  [source]   every label has a source, or the explicit value 'missing'
  [status]   status is valid; 'verified' needs a source
  [rule]     cross-field rules documented in schema/README.md

Usage: python3 scripts/validate.py [--root DIR]
Exit status: 0 when clean, 1 when any error is found.
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TYPES = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'integer': int}


def schema_errors(value, schema, root_schema, path):
    """Minimal JSON Schema (2020-12) subset: the keywords paper.schema.json uses."""
    if '$ref' in schema:
        schema = root_schema['$defs'][schema['$ref'].split('/')[-1]]
    errs = []
    t = schema.get('type')
    if t:
        ok = isinstance(value, TYPES[t]) and not (t == 'integer' and isinstance(value, bool))
        if not ok:
            return [('type', path, f'expected {t}, got {type(value).__name__}')]
    if 'const' in schema and value != schema['const']:
        errs.append(('enum', path, f'expected {schema["const"]!r}'))
    if 'enum' in schema and value not in schema['enum']:
        errs.append(('enum', path, f'{value!r} not in {schema["enum"]}'))
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0):
            errs.append(('empty', path, 'empty string'))
        if 'pattern' in schema and not re.search(schema['pattern'], value):
            errs.append(('pattern', path, f'{value!r} does not match {schema["pattern"]}'))
    if isinstance(value, int) and 'minimum' in schema and value < schema['minimum']:
        errs.append(('type', path, f'{value} < {schema["minimum"]}'))
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            errs.append(('type', path, f'needs at least {schema["minItems"]} items'))
        for i, item in enumerate(value):
            errs += schema_errors(item, schema.get('items', {}), root_schema, f'{path}[{i}]')
    if isinstance(value, dict):
        for key in schema.get('required', []):
            if key not in value:
                errs.append(('required', f'{path}.{key}', 'missing required field'))
        props = schema.get('properties', {})
        for key, sub in value.items():
            if key in props:
                errs += schema_errors(sub, props[key], root_schema, f'{path}.{key}')
            elif schema.get('additionalProperties') is False:
                errs.append(('unknown', f'{path}.{key}', 'unknown field'))
    if 'oneOf' in schema:
        matches = [s for s in schema['oneOf'] if not schema_errors(value, s, root_schema, path)]
        if len(matches) != 1:
            errs.append(('type', path, f'matches {len(matches)} of the allowed shapes, expected exactly 1'))
    for sub in schema.get('allOf', []):
        errs += schema_errors(value, sub, root_schema, path)
    if 'if' in schema:
        branch = 'else' if schema_errors(value, schema['if'], root_schema, path) else 'then'
        if branch in schema:
            errs += [('rule', p, m) for _, p, m in schema_errors(value, schema[branch], root_schema, path)]
    if 'not' in schema and not schema_errors(value, schema['not'], root_schema, path):
        errs.append(('rule', path, f'must not match {json.dumps(schema["not"])}'))
    return errs


def category(kind, path):
    if kind in ('required', 'unknown'):
        return 'required'
    if kind == 'rule':
        return 'rule'
    if path.endswith('.status'):
        return 'status'
    if path.endswith('.source'):
        return 'source'
    if path == '$.id':
        return 'id'
    return 'required' if kind == 'empty' else 'schema'


def as_list(v):
    return v if isinstance(v, list) else [v]


def record_errors(rec, stem, allowed):
    """Checks that need the vocabulary or several fields at once."""
    errs = []
    if rec.get('id') != stem:
        errs.append(('id', '$.id', f'id {rec.get("id")!r} does not match file name {stem!r}'))
    labels = rec.get('labels') if isinstance(rec.get('labels'), dict) else {}
    n_settings = len(rec['settings']) if isinstance(rec.get('settings'), list) else None
    has_list = False
    for name, lab in labels.items():
        if not isinstance(lab, dict) or 'value' not in lab:
            continue
        p = f'$.labels.{name}'
        for v in as_list(lab['value']):
            if name in allowed and v not in allowed[name]:
                errs.append(('vocab', f'{p}.value', f'{v!r} not in data/vocab.yaml [{name}]'))
        if lab.get('status') == 'verified' and lab.get('source') == 'missing':
            errs.append(('status', f'{p}.status', "'verified' needs a source other than 'missing'"))
        if isinstance(lab['value'], list):
            has_list = True
            if n_settings != len(lab['value']):
                errs.append(('rule', f'{p}.value', f'{len(lab["value"])} values but {n_settings} settings'))
        if isinstance(lab.get('inferred'), list) and (
                not isinstance(lab['value'], list) or len(lab['inferred']) != len(lab['value'])):
            errs.append(('rule', f'{p}.inferred', 'inferred list must match the value list'))
        if rec.get('in_table1') is True and 'pending' in as_list(lab['value']):
            errs.append(('rule', f'{p}.value', "'pending' is not allowed in a Table 1 row"))
    if n_settings is not None and not has_list:
        errs.append(('rule', '$.settings', 'settings given but no label has per-setting values'))
    ps = [labels.get(k, {}).get('value') for k in ('problem', 'stage')]
    if rec.get('record_type') == 'paradigm-system-benchmark' and ps != ['n/a', 'n/a']:
        errs.append(('rule', '$.labels', "paradigm-system-benchmark records take problem and stage 'n/a'"))
    if rec.get('record_type') == 'method' and rec.get('in_table1') is True and 'n/a' in ps:
        errs.append(('rule', '$.labels', "a method row of Table 1 needs a problem and a stage, not 'n/a'"))
    pending_split = any(labels.get(k, {}).get('value') == 'pending' for k in ('tokenizer', 'objective'))
    if 'legacy_training' in rec and not pending_split:
        errs.append(('rule', '$.legacy_training', 'only kept while tokenizer or objective is pending'))
    return errs


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--root', type=Path, default=ROOT, help='repository root (default: this repository)')
    args = ap.parse_args()

    schema = json.loads((args.root / 'schema/paper.schema.json').read_text(encoding='utf-8'))
    vocab = yaml.safe_load((args.root / 'data/vocab.yaml').read_text(encoding='utf-8'))
    allowed = {field: {e['value'] for e in entries} for field, entries in vocab.items()}
    unknown_fields = set(allowed) - set(schema['properties']['labels']['properties'])
    errors = [('data/vocab.yaml', 'vocab', '$', f'fields not in the schema: {sorted(unknown_fields)}')] \
        if unknown_fields else []

    paths = sorted((args.root / 'data/papers').glob('*.yaml'))
    seen = {}  # (kind, key) -> file name
    for path in paths:
        try:
            rec = yaml.safe_load(path.read_text(encoding='utf-8'))
        except yaml.YAMLError as e:
            errors.append((path.name, 'schema', '$', f'YAML error: {e}'))
            continue
        if not isinstance(rec, dict):
            errors.append((path.name, 'schema', '$', 'top level must be a mapping'))
            continue
        found = [(category(k, p), p, m) for k, p, m in schema_errors(rec, schema, schema, '$')]
        found += record_errors(rec, path.stem, allowed)
        keys = [('id', rec.get('id'))] + [('name', n.lower()) for n in [rec.get('name')] + rec.get('aliases', [])
                                          if isinstance(n, str)]
        ext = rec.get('external') if isinstance(rec.get('external'), dict) else {}
        if ext.get('arxiv'):
            keys.append(('arxiv', ext['arxiv']))
        for key in keys:
            if key in seen:
                found.append(('id', '$', f'duplicate {key[0]} {key[1]!r} (also in {seen[key]})'))
            else:
                seen[key] = path.name
        errors += [(path.name, c, p, m) for c, p, m in found]

    for fname, cat, p, msg in errors:
        print(f'{fname}: [{cat}] {p}: {msg}')
    print(f'{len(paths)} records, {len(errors)} errors')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
