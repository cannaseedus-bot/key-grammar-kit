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


## Core algebra

The JSON key-grammar is not the graph itself. It is the compressed symbolic source from which the query-local graph is unfolded.

```text
k -> Book(k)
Book(k) = N(k) = {k1, k2, ..., kn}
B_Q = {k1, k2, ..., km}
U(B_Q) = union(Book(k) for k in B_Q)
U(B_Q, theta) -> G_Q
```

`B_Q` is the runtime **Bag of Key-Words** extracted from tokens, ngrams, aliases, relation tags, phase markers, classes, and XCFE operators. `resolve_manifest` performs the unfold, but the unfold is phase-constrained: resolved objects can carry C6 authority `theta(k) in {Pop, Wo, Yax, Sek, Ch'en, Xul}`.

The runtime graph can be read as a product graph:

```text
G_runtime = G_semantic □ G_phase
v = (k, theta)
```

A horizontal fold changes semantic position while preserving phase. A vertical fold preserves semantic identity while changing phase. Geometry comes after that as a projection:

```text
P: G_Q -> F
F = vector space | coordinate field | SVG-3D geometry | tensor layout | GML graph | GPU field representation
```

Invariant: **Manifest authority > Graph realization > Geometric projection**. Meaning is not coordinates. A projection can represent, measure, search, render, or execute against semantic authority, but it cannot redefine it. Symbolic key scoring also belongs before geometry: `S(k) = W_k + H_N(k)` can operate directly over manifest topology.



## Surface forms and sense keys

A surface word is not automatically the final semantic key. A word like `bank` enters as a surface form, then context, ngrams, aliases, intents, and classes resolve it into one or more candidate sense keys.

```text
surface:bank
  -> bank:river_edge
  -> bank:financial_institution
  -> bank:seed_repository
  -> bank:central_bank
  -> bank:nearby_financial_search
  -> bank:blood_repository
```

Example sense-key names below are illustrative canonical-style keys; a production manifest can use the registry names adopted by the runtime.

Examples:

| Surface evidence | Candidate sense key | Notes |
|------------------|---------------------|-------|
| `river bank` | `bank:river_edge` | landform / geography neighborhood |
| `seed bank` | `bank:seed_repository` | biological/genetic storage neighborhood |
| `central bank` | `bank:central_bank` | monetary authority neighborhood |
| `bank closest to me` | `bank:nearby_financial_search` | financial institution plus location/search intent |
| `blood bank` | `bank:blood_repository` | medical storage neighborhood |

After disambiguation, the selected sense key receives the normal treatment: `Book(k)=N(k)`, symbolic score `S(k)=W_k+H_N(k)`, and phase face `Theta(k)`. This keeps polysemy out of the static key identity: `bank` is a surface handle; `bank:river_edge` and `bank:financial_institution` are different semantic addresses.


### Joke/pun sense routing

A joke request can deliberately route across senses. In the vampire example, the answer text is `Blood Bank`, but the normalized semantic key is the blood-repository sense of `bank`, not the financial-institution sense.

```xml
<template>What do you call a fast food restaurant for a vampire?</template>
<semantics>key-word: bank:blood_repository; answer: Blood Bank</semantics>
<ngrams>vampire, blood_sucker, food_source, physical_location, joke, bankers</ngrams>
```

The joke frame admits a pun bridge: `vampire + blood_sucker + food_source` supplies blood semantics, `physical_location + restaurant + bank` supplies place semantics, and `joke + bankers` keeps the financial surface available as wordplay without selecting it as the primary sense.

## Symbolic key score

A resolved key can be scored before any vector or tensor projection by combining its static intrinsic weight with horizontal neighborhood evidence from its declared key-book:

```text
S(k) = W_k + H_N(k)
H_N(k) = sum(W_u * R(k, u) for u in N(k))
Book(k) = N(k)
```

`W_k` is the static/canonical weight attached to the key. `H_N(k)` is the evidence contributed by horizontally traversing the declared neighborhood behind the key. `R(k, u)` can be symbolic at this layer, such as relation-family match, phase compatibility, manifest edge type, or declared association strength. A geometric projection may later provide richer similarity, but it is not required for the basic key-book score.

The compressed primitive is:

```text
Key = Static Weight + Horizontal N
```

Vertical phase movement is separate. Horizontal evidence stays within the current phase position; vertical folds move the resolved semantic state through C6 phase authority and expose alternate phase semantics for the same key.


## Horizontal and vertical semantics

A resolved node has two coordinates:

```text
v = (k, theta)
```

Horizontal movement explores related semantics in the key-book while preserving phase:

```text
(k, theta) -> (k_prime, theta)
(k, theta) -> (N(k), theta)
```

Vertical movement keeps the key fixed and changes the phase-semantic interpretation of that same key:

```text
(k, theta_i) -> (k, theta_j)
```

Phase is therefore more than execution timing. It is the semantic face through which the same key is interpreted: Pop may read `CAUSE` as trigger, Wo as condition, Yax as candidate, Sek as operation, Ch'en as observed relation, and Xul as collapsed meaning.

The resolved semantic state is:

```text
Semantic state = W(k) + N(k) + Theta(k)
```

Horizontal asks: what is connected to this meaning? Vertical asks: what else can this same thing mean under another phase?

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

The runtime input is a **Bag of Key-Words** derived from tokens, ngrams, classes, aliases, relation tags, phase markers, operator tags, and disambiguated sense keys. `resolve_manifest` / `resolve_manifest_key` is the shared traversal engine; each manifest supplies the domain grammar.

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
| `docs/key-grammar-book-algebra.md` | Formal Semantic Fold Compression Grammar spec: manifests as compressed semantic addresses, Bag of Key-Words algebra, symbolic key scoring, phase-constrained unfold into graph topology, projection authority boundaries, manifest-driven `L_A`, and `FoldDelta`/`DirectionStore`/`FoldDirection` cardinalities. |
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
