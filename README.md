# K'UHUL JSON Key-Grammar Kit

EBNF v3 runtime grammar for the **K'UHUL key-grammar JSON** format, plus corpus records used by the K'UHUL runtime.

The key-grammar defines how structured JSON records are addressed, phase-bound, and validated against the K'UHUL semantic algebra. Every record in the gram store is an instance of one of the row types described by `key-grammar-json.runtime.ebnf`.


## Layer classification

This kit defines the **Semantic Fold Compression Grammar**. The grammar is the source layer: manifest-backed key-books compress semantic fold neighborhoods into addressable key-words, then unfold those addresses into graph topology and optional geometric field projections.

```text
Semantic Fold Compression Grammar
  -> Semantic Fold Graph Topology
  -> Geometric Node Field Class
```

| Layer | Meaning | Kit/runtime surface |
|-------|---------|---------------------|
| Semantic Fold Compression Grammar | Declares compressed semantic addresses and unfold rules. | `*.manifest.json`, `⟁KEYGRAMMAR`, `resolve_manifest`, key-books, Bag of Key-Words |
| Semantic Fold Graph Topology | Expanded atoms, relations, books, candidates, folds, and phase edges. | `data/grammar/fold_graph.xml`, SGSFG, `Book(k) = N(k)` |
| Geometric Node Field Class | Projection of the graph into vectors, fields, coordinates, tensors, or rendering/runtime geometry. | `field.xml`, vector metadata, GML, SVG-3D, tensor projections |

Use the first name when describing this kit as a grammar package. Use the second when describing the unfolded graph. Use the third when describing a vector/field/tensor projection of that graph.

## Key record types

| Type | Key prefix | Phase | Description |
|------|-----------|-------|-------------|
| `lexicon_row` | `word:<term>` | any | Vocabulary entry with pos, definition, channel |
| `control_flow_row` | `control:<op>` | Wo/Yax/Sek | XCFE control operator binding |
| `relation_row` | `rel:<verb>` | Sek/Ch'en | Canonical relation verb record |
| `greeting_row` | `greeting:<id>` | Pop | Greeting/response seed |
| `lingo_blend_row` | `lingo:<id>` | Pop/Wo | Multilingual/register blend |
| `template_slot_row` | `template:slot:<name>` | any | Template slot binding (SC-13) |

## EBNF v3 additions over v2

- `control_op_fields` shared production — eliminates duplication across control row variants
- `greeting_phase` split — phase name is a separate terminal, not inlined
- `channel_contract` — documentation-only production capturing per-channel authority rules
- `template_slot_row` — new row type unifying template slots with gram store keys
- `lingo_blend_key` — explicit production for multilingual blend keys
- SC-1..SC-13 side-constraint block — cross-field invariants enforced by `mini_transpilers.py`

## Side constraints (SC-1..SC-13)

| SC | Rule |
|----|------|
| SC-1 | `lexicon_row` pos is one of the 9 canonical POS tags |
| SC-2 | `control_flow_row` xcfe_class ∈ 14-class closed set |
| SC-3 | `lexicon_row` type↔unit coupling (word/definition_token, etc.) |
| SC-4 | `relation_row` verb ∈ canonical RelationISA |
| SC-5 | `greeting_row` phase ∈ {Pop, Wo} |
| SC-6 | `gram_store_entry` channel ∈ declared channel set |
| SC-7 | `template_slot_row` phase ∈ C6 phase names |
| SC-8 | `control_flow_row` authority_phase = CanonicalPhase(xcfe_class) |
| SC-9 | `xcfe_class_authority` pair count = 14 |
| SC-10 | `lingo_blend_row` language_tag is BCP-47 |
| SC-11 | `key_store_key` matches the pattern for its row type |
| SC-12 | `string_object` values are JSON strings only |
| SC-13 | `template_slot_row` slot_type↔slot_unit coupling (mirrors SC-3) |


## Manifest key-books

The key-grammar layer is the Semantic Fold Compression Grammar and includes manifest-backed key-books. A **key-word** is the singular resolved address/evidence unit. A **key-book** is the plural declared neighborhood that stores many key-words and their expansion edges. This avoids confusing KHANARY key-books with generic graph-theory book terminology.

The runtime input is a **Bag of Key-Words** derived from tokens, ngrams, classes, aliases, relation tags, phase markers, and operator tags. `resolve_manifest` / `resolve_manifest_key` is the shared traversal engine; each manifest supplies the domain grammar.

| Key-book | Role |
|----------|------|
| `data/manifest/words.manifest.json` | Canonical vocabulary key-book: lexical aliases, intents, relation families, phase anchors, dispatch keys, and conditionals. |
| `data/manifest/css.manifest.json` | Atomic CSS/UI key-book; declares `⟁KEYGRAMMAR`, style atoms, composed blocks, components, layouts, and app-level UI keys. |
| `data/manifest/folds.manifest.json` | K'UHUL phase-fold/topology key-book: activation fold, horizontal/vertical phase folds, association channels, and syntax books. |
| `data/manifest/gml.manifest.json` | Graph topology key-book: GML loader, validators, Q3/Q4 hypercubes, CCC_n graphs, projection ABI, and gyro ABI. |
| `data/manifest/aiml.manifest.json` | AIML structure key-book: pattern, template, wildcard, topic, that, graph, relation, and advisor routing keys. |
| `data/manifest/eliza.manifest.json` | ELIZA operator key-book: 16 ELIZA-1 operators mapped to relation families and phases. |
| `data/manifest/kuhul.manifest.json` | Runtime authority key-book linking fold deltas, DirectionStore, episode contracts, fold graph laws, and key-query routes. |
| `data/schema/math-isa.json` | Math GraphPlan ISA extension for manifest-driven `L_A` lowering. |

See `docs/key-grammar-book-algebra.md` for the formal Semantic Fold Compression Grammar classification, book/key-word terminology, traversal phases, Bag of Key-Words model, DirectionStore singular/plural boundary, and open specs for `A(v)`, `L_A`, SGSFG edges, and key-book algebra.

## Files

| File | Description |
|------|-------------|
| `key-grammar-json.runtime.ebnf` | Full EBNF v3 with SC-1..SC-13 side constraints |
| `tools/grammar/mini_transpilers.py` | Source-side validator/transpiler referenced by the EBNF side constraints; defaults to the KHANARY.CPP repo layout. |
| `data/schema/math-isa.json` | Closed-world math GraphPlan ISA extension used by manifest-driven `L_A`. |
| `data/schema/manifest-map.schema.json` | Schema for key-word expansion maps, including typed declarative XCFE conditionals. |
| `data/schema/episode.contract.json` | Episode/FoldDelta/FoldDirection contract defining journal evidence, direction library, and PrincipalDirection rules. |
| `data/grammar/fold_graph.xml` | Fold graph laws, including journal-is-direction-library and fold-delta-not-vec-delta. |
| `data/manifest/*.manifest.json` | Manifest key-books for words, css, folds, gml, aiml, eliza, and kuhul runtime domains. |
| `src/kuhul/fold_delta.h` | Reference C++ boundary for one verified semantic displacement (`FoldDelta`). |
| `src/kuhul/fold_direction.h` | Reference C++ boundary for `DirectionStore` and derived `FoldDirection`. |
| `src/kuhul/fold_direction.cpp` | Current DirectionStore membership/retrieval implementation: GOOD gate, `micronaut_id` grouping, and Jaccard capability retrieval. |
| `tools/check_key_book_grammar.py` | Dependency-free validator for manifest key-book shape, `⟁KEYGRAMMAR`, conditionals, ELIZA operator pack, math ISA, and DirectionStore semantic boundary. |
| `docs/key-grammar-book-algebra.md` | Formal key-book/key-word algebra spec: manifests as declared neighborhoods, Bag of Key-Words, phase traversal, manifest-driven `L_A`, and `FoldDelta`/`DirectionStore`/`FoldDirection` cardinalities. |
| `control-flow.key-grammar.jsonl` | XCFE control operator bindings — one record per operator |
| `control-capability-gaps.jsonl` | Capability gap records for Ch'en miss classification |
| `greeting-bank.json` | Greeting/response seed data (raw) |
| `greeting-bank.key-grammar.jsonl` | Greeting seeds as key-grammar records |
| `english-dictionary.definition-relations.key-grammar.jsonl` | Relation records derived from dictionary definitions |
| `english-dictionary.key-grammar.meta.json` | Metadata for the dictionary corpus (stats, authority, channel) |
| `english-dictionary.lexicon.key-grammar.jsonl.zip` | Full English lexicon corpus — 9.3 MB compressed, 122 MB unzipped. **Unzip before use:** `unzip english-dictionary.lexicon.key-grammar.jsonl.zip` |
| `advisor-bootstrap.json` | Advisor delegation seed data (raw) |
| `advisor-bootstrap.key-grammar.jsonl` | Advisor seeds as key-grammar records |
| `plan-bootstrap.json` | Plan/proposal seed data (raw) |
| `plan-bootstrap.key-grammar.jsonl` | Plan seeds as key-grammar records |

> **Note:** `english-dictionary.lexicon.key-grammar.jsonl` (122 MB) exceeds GitHub's file size limit and is not included. It is available in the full KHANARY.CPP distribution.

## Validation

Run the manifest/key-book validator from the kit root:

```powershell
python tools\check_key_book_grammar.py
```

`tools/grammar/mini_transpilers.py validate` targets the full KHANARY.CPP `data/grammar` layout. This slim kit keeps the large key-grammar JSONL artifacts at the kit root, so use `check_key_book_grammar.py` for the bundled manifest, schema, and DirectionStore boundary checks.

## Record format

Every key-grammar record is a JSON object on a single line (JSONL). Minimal shape:

```json
{"schema": "key.grammar.<type>.v1", "key": "<prefix>:<value>", "phase": "<C6 phase>", "channel": "<channel>", "authority": "<corpus>"}
```

The `schema` field identifies the row type and version. The `key` field is the gram store address. `phase` binds the record to a C6 phase for fold authorization.

## Part of

[KHANARY.CPP](https://github.com/cannaseedus-bot) — K'UHUL semantic runtime stack.
