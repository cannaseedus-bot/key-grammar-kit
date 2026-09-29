#!/usr/bin/env python3
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFESTS = {
    'words': ROOT / 'data/manifest/words.manifest.json',
    'css': ROOT / 'data/manifest/css.manifest.json',
    'folds': ROOT / 'data/manifest/folds.manifest.json',
    'gml': ROOT / 'data/manifest/gml.manifest.json',
    'aiml': ROOT / 'data/manifest/aiml.manifest.json',
    'eliza': ROOT / 'data/manifest/eliza.manifest.json',
    'kuhul': ROOT / 'data/manifest/kuhul.manifest.json',
}
REQUIRED = [
    ROOT / 'data/schema/manifest-map.schema.json',
    ROOT / 'data/schema/math-isa.json',
    ROOT / 'data/schema/episode.contract.json',
    ROOT / 'data/grammar/fold_graph.xml',
    ROOT / 'docs/key-grammar-book-algebra.md',
    ROOT / 'joke-bootstrap.json',
    ROOT / 'joke-bootstrap.key-grammar.jsonl',
    ROOT / 'src/kuhul/fold_delta.h',
    ROOT / 'src/kuhul/fold_direction.h',
    ROOT / 'src/kuhul/fold_direction.cpp',
]
errors = []

def rel(path):
    return path.relative_to(ROOT).as_posix()

def load_json(path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{rel(path)} invalid JSON: {exc}')
        return None

def validate_token(token, relname, key, trail):
    if isinstance(token, str):
        return
    if isinstance(token, dict):
        if '@if' not in token or '@then' not in token:
            errors.append(f'{relname}:{key} conditional missing @if/@then at {trail}')
            return
        allowed = {'@if', '@then', '@else'}
        extra = set(token) - allowed
        if extra:
            errors.append(f'{relname}:{key} conditional has extra keys {sorted(extra)} at {trail}')
        if not isinstance(token['@if'], (str, bool)):
            errors.append(f'{relname}:{key} @if must be string/bool at {trail}')
        for branch in ['@then', '@else']:
            if branch in token:
                if not isinstance(token[branch], list):
                    errors.append(f'{relname}:{key} {branch} must be array at {trail}')
                else:
                    for i, item in enumerate(token[branch]):
                        validate_token(item, relname, key, f'{trail}.{branch}[{i}]')
        return
    errors.append(f'{relname}:{key} expansion token must be string or conditional object at {trail}')

for path in REQUIRED:
    if not path.exists():
        errors.append(f'missing {rel(path)}')

books = {}
for name, path in MANIFESTS.items():
    if not path.exists():
        errors.append(f'missing {rel(path)}')
        continue
    data = load_json(path)
    if data is None:
        continue
    if not isinstance(data, dict):
        errors.append(f'{rel(path)} must be object')
        continue
    books[name] = data
    for key, expansion in data.items():
        if not isinstance(key, str) or not key:
            errors.append(f'{name}: empty/non-string key')
        if not isinstance(expansion, list):
            errors.append(f'{name}:{key} expansion must be array')
            continue
        for i, token in enumerate(expansion):
            validate_token(token, name, key, f'expansion[{i}]')

css = books.get('css', {})
keygrammar = css.get('⟁KEYGRAMMAR')
if not isinstance(keygrammar, list):
    errors.append('css manifest missing ⟁KEYGRAMMAR list')
else:
    for token in ['key:address(book)', 'book:declared-neighborhood', 'grammar:constrained-book-traversal', 'phase:Wo', 'phase:Yax', "phase:Ch'en"]:
        if token not in keygrammar:
            errors.append(f'⟁KEYGRAMMAR missing {token}')

words = books.get('words', {})
for key in ['hello', 'hi', 'help', 'cause', 'manifest', 'key_references', 'ngram_references', 'MANIFEST:', '@manifest_query', 'JOKE:', '@joke', 'joke', 'pun', 'wordplay']:
    if key not in words:
        errors.append(f'words manifest missing {key}')
if words.get('hello') and 'intent:salutation' not in words['hello']:
    errors.append('hello expansion missing intent:salutation')
if words.get('help') and not any(isinstance(x, dict) and '@if' in x for x in words['help']):
    errors.append('help expansion should include typed conditional')

folds = books.get('folds', {})
for key in ['fold:activation', 'fold:horizontal', 'fold:vertical']:
    if key not in folds:
        errors.append(f'folds manifest missing {key}')

eliza = books.get('eliza', {})
operator_pack = eliza.get('eliza:operator-pack', [])
if isinstance(operator_pack, list) and len([x for x in operator_pack if isinstance(x, str) and x.startswith('ELIZA-1:')]) < 16:
    errors.append('eliza operator pack should declare 16 ELIZA-1 operators')

kuhul = books.get('kuhul', {})
for key in ['fold_delta:impl', 'direction_store:impl', 'schema:episode', 'fold_graph:spec']:
    if key not in kuhul:
        errors.append(f'kuhul manifest missing {key}')
if kuhul.get('direction_store:impl'):
    for token in ['class:DirectionStore', 'retrieval:R=Jaccard(query_caps,capability_key)', 'wire:direction_store.ingest(delta)@factory_advisor_commit']:
        if token not in kuhul['direction_store:impl']:
            errors.append(f'direction_store:impl missing {token}')

for key in ['JOKE-µ', 'joke.aiml', 'joke:frame', 'joke:pun_bridge', 'joke:answer_surface']:
    if key not in books.get('aiml', {}):
        errors.append(f'aiml manifest missing {key}')
if 'JOKE-µ' in books.get('aiml', {}):
    for token in ['not:joke-authoring', 'first-class-µ-track', 'peer:PLAN-µ', 'peer:ADVISOR-µ', 'availability:all-domains']:
        if token not in books['aiml']['JOKE-µ']:
            errors.append(f'JOKE-µ must declare {token}')

joke_bootstrap = load_json(ROOT / 'joke-bootstrap.json') if (ROOT / 'joke-bootstrap.json').exists() else None
if joke_bootstrap:
    if joke_bootstrap.get('track') != 'JOKE-µ':
        errors.append('joke bootstrap track must be JOKE-µ')
    if joke_bootstrap.get('first_class') is not True or joke_bootstrap.get('availability') != 'all_domains':
        errors.append('joke bootstrap must declare first-class all-domain availability')
    for peer in ['PLAN-µ', 'ADVISOR-µ']:
        if peer not in joke_bootstrap.get('peers', []):
            errors.append(f'joke bootstrap missing peer {peer}')
    policy = joke_bootstrap.get('policy', {})
    for token in ['pun_bridge', 'surface_ambiguity', 'multiple_senses_active', 'punchline_compression']:
        if token not in policy.get('admit', []):
            errors.append(f'joke bootstrap policy missing {token}')
    if policy.get('not_purpose') != 'telling jokes as freeform generation':
        errors.append('joke bootstrap must declare not_purpose')
    routes = joke_bootstrap.get('routes', [])
    if len(routes) < 5:
        errors.append('joke bootstrap should declare at least five routes')

joke_jsonl = ROOT / 'joke-bootstrap.key-grammar.jsonl'
if joke_jsonl.exists():
    rows = []
    for line_no, line in enumerate(joke_jsonl.read_text(encoding='utf-8').splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except Exception as exc:
            errors.append(f'joke-bootstrap.key-grammar.jsonl line {line_no} invalid JSON: {exc}')
    if len(rows) < 5:
        errors.append('joke-bootstrap.key-grammar.jsonl should contain at least five records')
    for row in rows:
        if row.get('class') != 'JOKE' or 'JOKE-µ' not in row.get('definition', ''):
            errors.append(f'joke JSONL row missing JOKE class/definition: {row.get("key")}')
        if 'first-class reusable humor-frame routing track' not in row.get('semantic_note', ''):
            errors.append(f'joke JSONL row missing semantic note: {row.get("key")}')

math_isa = load_json(ROOT / 'data/schema/math-isa.json') if (ROOT / 'data/schema/math-isa.json').exists() else None
if math_isa:
    if math_isa.get('compiler') != 'L_A':
        errors.append('math-isa compiler must be L_A')
    ops = math_isa.get('graphplan_ops', [])
    if not isinstance(ops, list) or not ops:
        errors.append('math-isa graphplan_ops must be non-empty list')
    else:
        for op in ops:
            for field in ['op', 'mathml', 'resolver_capability', 'resolver_primitive']:
                if field not in op:
                    errors.append(f'math-isa op missing {field}: {op}')

episode = load_json(ROOT / 'data/schema/episode.contract.json') if (ROOT / 'data/schema/episode.contract.json').exists() else None
if episode:
    direction = episode.get('fold_direction', {})
    if not isinstance(direction, dict):
        errors.append('episode contract missing fold_direction object')
    else:
        principal = direction.get('principal_direction', {})
        if 'PrincipalDirection' not in str(principal):
            errors.append('episode fold_direction missing PrincipalDirection definition')
        direction_text = json.dumps(episode, ensure_ascii=False)
        for token in ['Journal', 'FoldDelta', 'DirectionLibrary', 'Projection_Index']:
            if token not in direction_text:
                errors.append(f'episode fold_direction text missing {token}')

fold_graph = (ROOT / 'data/grammar/fold_graph.xml').read_text(encoding='utf-8', errors='replace') if (ROOT / 'data/grammar/fold_graph.xml').exists() else ''
for token in ['journal-is-direction-library', 'fold-delta-composition', 'fold-delta-not-vec-delta', 'apply-field-not-commit-topology']:
    if token not in fold_graph:
        errors.append(f'fold_graph.xml missing law {token}')

source_checks = {
    'src/kuhul/fold_delta.h': ['struct FoldDelta', 'std::string  verdict', 'jrom_seq', 'GOOD'],
    'src/kuhul/fold_direction.h': ['struct FoldDirection', 'class DirectionStore', 'capability_key', 'governs_key', 'query('],
    'src/kuhul/fold_direction.cpp': ['store_[delta.micronaut_id]', 'delta.verdict != "GOOD"', 'jaccard(query_caps, dir.capability_key)', 'dir.W * dir.C * R'],
}
for relpath, needles in source_checks.items():
    path = ROOT / relpath
    text = path.read_text(encoding='utf-8', errors='replace') if path.exists() else ''
    for needle in needles:
        if needle not in text:
            errors.append(f'{relpath} missing {needle}')

spec = (ROOT / 'docs/key-grammar-book-algebra.md').read_text(encoding='utf-8', errors='replace') if (ROOT / 'docs/key-grammar-book-algebra.md').exists() else ''
for token in [
    'Bag of Key-Words',
    'Terminology note',
    'key-word',
    'key-book',
    'resolve_manifest',
    'manifest-driven',
    'Semantic Fold Compression Grammar',
    'Semantic Fold Graph Topology',
    'Geometric Node Field Class',
    'P: G_Q -> F',
    'G_runtime = G_semantic □ G_phase',
    'U(B_Q, theta) -> G_Q',
    'Delta_vec is representational',
    'FoldDelta is semantic',
    'meaning != coordinates',
    'Manifest authority > Graph realization > Geometric projection',
    'Vertical phase movement is a separate operation',
    'Key = Static Weight + Horizontal N',
    'H_N(k) = sum(W_u * R(k, u) for u in N(k))',
    'S(k) = W_k + H_N(k)',
    'Static weight and horizontal neighborhood evidence',
    'CAUSE as collapsed meaning',
    'CAUSE as trigger',
    'Semantic state = W(k) + N(k) + Theta(k)',
    'Vertical phase = alternate semantics of the same key',
    'Horizontal N = related semantics',
    'Horizontal neighborhood and vertical phase semantics',
    'bank:blood_repository',
    'bank:nearby_financial_search',
    'bank:central_bank',
    'bank:seed_repository',
    'bank:financial_institution',
    'bank:river_edge',
    'polysemy resolves before horizontal N and vertical Theta',
    'same spelling != same Book(k)',
    'surface form != final semantic key',
    'Surface forms, polysemy, and sense keys',
    'surface joke prompt -> ngram evidence -> candidate sense keys -> selected semantic key -> punchline surface',
    'selected punchline sense bank:blood_repository',
    'bankers',
    'physical_location',
    'food_source',
    'blood_sucker',
    'intent:joke',
    'answer: Blood Bank',
    'What do you call a fast food restaurant for a vampire?',
    'Joke and pun sense routing',
    'JOKE route surfaces are routing policy',
    'JOKE-µ != freeform joke authoring',
    'JOKE-µ = first-class humor-frame semantic routing',
    'first-class reusable µ-track like `PLAN-µ` and `ADVISOR-µ`',
    'available to all domains',
    'joke.aiml = surface trigger projection',
    'joke key-book = admissible ambiguity/pun moves',
    'JOKE track = runtime policy application',
    'allow:pun_bridge',
    'keep:multiple_senses_active',
    'admit:surface_ambiguity',
    'prefer:punchline_compatible_sense_selection',
    'preserve:selected_semantic_key + surface_answer_text',
    'fast_food_restaurant + vampire + blood + bank',
    'joke frame -> selects punchline-compatible path',
    'association field -> candidate sense keys',
    'surface token -> literal key + association field',
    'assoc:politician',
    'assoc:lawyer',
    'assoc:extractor',
    'assoc:parasite',
    'literal:vampire',
    'association-field activator',
    'Association fields vs action frames',
    'withdrawals is an action/predicate fold',
    'action:withdraw',
    'role:source',
    'role:object',
    'role:account_or_repository',
    'Where does a vampire make his withdrawals from?',
    'frame:food_venue',
    'role:food <= blood',
    'role:place <= repository/bank',
    'action:withdraw -> role:source',
    'frame:food_venue -> role:place',
    'not just word association; it is frame binding over the association field',
    'Recursive fold-unfold',
    'folds unfolding to new folds that unfold',
    'bounded, cycle-aware, and phase-constrained',
    'key-word -> Fold(k)',
    'child fold address -> Fold(child)',
    'Unfold_{d+1}(k)',
    'fold:joke_prompt',
    'fold:vampire_context',
    'fold:bank_polysemy',
    'fold:blood_bank_punchline',
    'Singular/plural semantic context',
    'DirectionStore aggregation boundary',
    '1 Episode -> 1 FoldDelta',
    'N compatible FoldDelta -> 1 FoldDirection',
    'Compatible(F_i, F_Q)',
]:
    if token not in spec:
        errors.append(f'book algebra spec missing {token}')

for bad in ['.exe', '.dll', '.obj', '.cso', '.pyc']:
    hits = [p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*' + bad)]
    if hits:
        errors.append(f'forbidden {bad}: {hits[:5]}')

if errors:
    for error in errors:
        print('FAIL |', error)
    sys.exit(1)

print(f'PASS | key-book grammar: {len(books)} manifest books, {sum(len(b) for b in books.values())} declared keys; DirectionStore boundary verified')
