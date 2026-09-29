# Key-Grammar Key-Book Algebra

This document defines the missing layer behind the KHANARY key-grammar manifests.

The short form is:

```text
key_word : singular address inside a key_book
key_book : plural declared-neighborhood of key_words
manifest : key_book encoded as key_word -> expansion[]
grammar  : constrained traversal over one or more key_books
engine   : resolve_manifest / resolve_manifest_key
phase    : Wo binds, Yax selects, Ch'en validates
```

`words.manifest.json` is the canonical vocabulary key-book: one plural book containing many singular key-words. It is not an AIML pattern file, a plain dictionary, or a word list. It is a key expansion grammar where each key-word maps to an ordered expansion array containing other keys, relation tags, phase hints, intent tags, domain operators, topology names, and typed declarative conditionals.



## Layer classification

This layer is best named **Semantic Fold Compression Grammar**. It is the source grammar that compresses semantic fold neighborhoods into manifest key-words and defines how those key-words unfold.

```text
Semantic Fold Compression Grammar
  -> expands into Semantic Fold Graph Topology
  -> projects into Geometric Node Field Class
```

The three names refer to different layers, not competing names for the same object.

| Layer | Role | Canonical reading |
|-------|------|-------------------|
| Semantic Fold Compression Grammar | Source grammar. Declares compressed addresses and unfold rules. | `key-word -> key-book expansion -> semantic neighborhood` |
| Semantic Fold Graph Topology | Expanded graph. Contains atoms, relations, books, candidates, folds, and phase edges. | `Book(k) = N(k)` and fold graph laws |
| Geometric Node Field Class | Projection. Maps the graph into vectors, coordinates, fields, tensors, or render/runtime geometry. | `node/relation/fold graph -> vector field / tensor view` |

Formal definition:

```text
Semantic Fold Compression Grammar =
  manifest-backed key-book grammar
  that compresses semantic fold neighborhoods into addressable key-words,
  unfolds them into graph topology,
  and permits geometric node-field projections without making geometry the source of truth.
```

So this kit should be classified as a grammar package first. `fold_graph.xml` and SGSFG are the topology view produced by expansion. `field.xml`, vector metadata, GML, SVG-3D, and tensors are geometric or runtime projections over that topology.


## Core algebra and authority

The JSON key-grammar is not the graph itself. It is the compressed symbolic source from which the graph is unfolded.

A manifest key is a compressed semantic address:

```text
k -> Book(k)
Book(k) = N(k) = {k_1, k_2, ..., k_n}
```

`⟁CAUSE` is a key-word/address. Its manifest value is the key-book containing the declared semantic neighborhood behind that address. A query produces a Bag of Key-Words:

```text
B_Q = {k_1, k_2, ..., k_m}
```

`resolve_manifest` performs the unfold:

```text
U(B_Q) = union(Book(k) for k in B_Q)
```

The unfold is phase-constrained. Resolved objects can carry C6 authorization:

```text
theta(k) in {Pop, Wo, Yax, Sek, Ch'en, Xul}
U(B_Q, theta) -> G_Q
```

`G_Q` is the query-local Semantic Fold Graph Topology. The manifest/key-book system supplies the semantic adjacency dimension, while C6 supplies phase position. The runtime graph can be read as a product graph:

```text
G_runtime = G_semantic □ G_phase
v = (k, theta)
```

A horizontal fold changes semantic position while preserving phase:

```text
(k_i, theta) -> (k_j, theta)
```

A vertical fold preserves semantic identity while changing phase:

```text
(k, theta_i) -> (k, theta_j)
```

The JSON grammar defines the material from which the semantic axis is constructed. It does not collapse the semantic axis, phase axis, and geometric projection into one object.

Geometry comes after topology. `field.xml`, GML, SVG-3D, vectors, tensors, and GPU field layouts do not define the meaning of a key-word such as `⟁CAUSE`. They project the already-resolved topology:

```text
P: G_Q -> F
F = vector space | coordinate field | SVG-3D geometry | tensor layout | GML graph | GPU field representation
```

Invariant:

```text
Manifest authority > Graph realization > Geometric projection
meaning != coordinates
```

A projection can represent, measure, search, render, or execute against semantic authority. It cannot redefine semantic authority. The symbolic score `S(k) = W_k + H_N(k)` operates at the manifest/topology layer before projection.



## Surface forms, polysemy, and sense keys

A surface form is not the same thing as a semantic key. The raw token `bank` is an ambiguous handle. It must be resolved through context, ngrams, aliases, intents, relation tags, and class evidence before the runtime treats it as a stable semantic address.

```text
surface:bank
  -> bank:river_edge
  -> bank:financial_institution
  -> bank:seed_repository
  -> bank:central_bank
  -> bank:nearby_financial_search
  -> bank:blood_repository
```

The names below are illustrative canonical-style sense keys. A production manifest can adopt these names or bind the same senses under its registered naming convention. The ngram or context often supplies the deciding evidence:

| Evidence | Sense key | Semantic neighborhood |
|----------|-----------|-----------------------|
| `river bank` | `bank:river_edge` | river, shore, landform, erosion, water-edge |
| `seed bank` | `bank:seed_repository` | seed, vault, biodiversity, preservation, germplasm |
| `central bank` | `bank:central_bank` | monetary policy, currency, reserves, interest rates |
| `bank closest to me` | `bank:nearby_financial_search` | financial institution, local search, geolocation, route |
| `blood bank` | `bank:blood_repository` | blood, donor, storage, transfusion, medical inventory |

Formal route:

```text
surface token / ngram / context
  -> candidate sense keys
  -> selected semantic key k
  -> Book(k) = N(k)
  -> S(k) = W_k + H_N(k)
  -> phase face Theta(k)
```

This matters because horizontal and vertical semantics operate after sense selection. `bank:river_edge` and `bank:financial_institution` should not share one key just because their surface spelling is identical. They may share a surface alias, but they unfold into different key-books.

The rule is:

```text
surface form != final semantic key
same spelling != same Book(k)
polysemy resolves before horizontal N and vertical Theta
```

Location or action language can create intent-shaped sense keys. `bank closest to me` is not merely the financial-institution sense; it also activates search/locality constraints such as `intent:local_search`, `constraint:nearby`, and `context:geolocation`.


### Joke and pun sense routing

A joke request can intentionally keep multiple senses active while still selecting a primary semantic key. For example:

```xml
<template>What do you call a fast food restaurant for a vampire?</template>
<semantics>key-word: bank:blood_repository; answer: Blood Bank</semantics>
<ngrams>vampire, blood_sucker, food_source, physical_location, joke, bankers</ngrams>
```

The visible punchline is `Blood Bank`. The semantic key is `bank:blood_repository`. The route is:

```text
intent:joke
  + vampire
  + blood_sucker
  + food_source
  + physical_location
  + bankers
  -> candidate senses {bank:blood_repository, bank:financial_institution}
  -> selected punchline sense bank:blood_repository
  -> surface answer "Blood Bank"
```

The joke frame changes the admission policy. `bankers` and `bank:financial_institution` can remain as wordplay evidence, but they do not override the selected blood-repository sense. The pun works because the surface answer carries two readings while the semantic route records which sense solved the prompt.

`vampire` is also an association-field activator, not only a literal monster key. It contributes both a literal entity and a contextual field:

```text
vampire
  -> literal:vampire
  -> assoc:blood_sucker
  -> assoc:blood
  -> assoc:parasite
  -> assoc:extractor
  -> assoc:banker
  -> assoc:lawyer
  -> assoc:politician
```

Those associations are candidate evidence. They widen the humor/metaphor field and can support alternate jokes, but they do not automatically become the selected answer. For this prompt, the selected bridge is:

```text
fast_food_restaurant + vampire + blood + bank
  -> bank:blood_repository
  -> surface answer "Blood Bank"
```

The rule is:

```text
surface token -> literal key + association field
association field -> candidate sense keys
joke frame -> selects punchline-compatible path
```

This is the same polysemy rule with an extra frame:

```text
surface joke prompt -> ngram evidence -> candidate sense keys -> selected semantic key -> punchline surface
```

A runtime should preserve both pieces: the selected `key-word` for semantic authority and the rendered `template`/answer text for user-facing humor.

### Association fields vs action frames

Association tokens and action predicates are different semantic objects. `vampire` can open an association field, but `withdrawals` is an action/predicate fold. In plain terms: withdrawals is an action/predicate fold. The action does not merely add another related word; it creates role slots that must be bound by context.

```text
action:withdraw
  role:actor
  role:object
  role:source
  role:account_or_repository
```

For the prompt:

```text
Where does a vampire make his withdrawals from?
```

the route is:

```text
intent:joke
  + entity:vampire
  + action:withdraw
  + role:object <= assoc:blood
  + role:source <= bank/repository candidate
  -> bank:blood_repository
  -> surface answer "Blood Bank"
```

The action fold `withdraw` asks for a source/account/repository. The vampire association field supplies `blood` as the object/need. The joke frame then selects the `bank:blood_repository` sense because it satisfies both the action frame and the vampire context.

For the fast-food prompt, the opened frame is different:

```text
What do you call a fast food restaurant for a vampire?
```

```text
intent:joke
  + entity:vampire
  + frame:food_venue
  + role:consumer <= vampire
  + role:food <= blood
  + role:place <= repository/bank
  -> bank:blood_repository
  -> surface answer "Blood Bank"
```

`fast_food_restaurant` opens a venue/place frame where food is obtained quickly. `vampire` supplies the food class through `blood`. The shared answer is still `Blood Bank`, but the path differs from the withdrawal joke: one route is `action:withdraw -> role:source`, and the other is `frame:food_venue -> role:place`.

This is not just word association; it is frame binding over the association field.

### Recursive fold-unfold

This example also shows folds unfolding to new folds that unfold. In the compression grammar, a manifest expansion entry can terminate as evidence or point at another fold/key-book address. That means an unfold can produce child fold addresses, and those child folds can unfold in turn.

```text
key-word -> Fold(k)
Fold(k) -> {terminal evidence, child fold addresses}
child fold address -> Fold(child)
```

Depth-indexed expansion makes the boundary explicit:

```text
Unfold_0(k) = Book(k)
Unfold_{d+1}(k) = union(Book(u) for u in Unfold_d(k) if u is fold-address)
```

A runtime must keep recursive unfold bounded, cycle-aware, and phase-constrained. The traversal should remember opened fold addresses, enforce a maximum depth, and apply the current C6 phase authority before opening another book.

The vampire joke route is a concrete recursive unfold:

```text
fold:joke_prompt
  -> fold:vampire_context
       -> assoc:blood_sucker
       -> assoc:blood
       -> assoc:banker
       -> assoc:lawyer
       -> assoc:politician
  -> fold:bank_polysemy
       -> bank:blood_repository
       -> bank:financial_institution
  -> fold:blood_bank_punchline
       -> selected semantic key bank:blood_repository
       -> surface answer "Blood Bank"
```

This preserves the layer boundary: the key-grammar declares which fold addresses can open; the Semantic Fold Graph Topology realizes the unfolded route; a geometric field can later project it, but the projection does not decide which fold was semantically authorized.

## Static weight and horizontal neighborhood evidence

A key carries static intrinsic weight plus horizontal evidence from its declared neighborhood:

```text
S(k) = W_k + H_N(k)
```

Since `Book(k) = N(k)`, the horizontal contribution can be written as:

```text
H_N(k) = sum(W_u * R(k, u) for u in N(k))
S(k) = W_k + sum(W_u * R(k, u) for u in N(k))
```

`W_k` is the static or canonical weight attached to the key. `H_N(k)` is what the key-book contributes in the current semantic context by traversing declared same-phase neighbors.

```text
              N(k)
       -------+-------
       v      v      v
      k1     k2     k3
       \      |      /
        horizontal evidence
               v
        [ k | static W(k) ]
               v
          combined S(k)
```

This calculation is symbolic. It does not require a vector space. `N(k)` comes directly from the manifest topology, and `R(k, u)` may be supplied by relation-family match, declared edge type, phase compatibility, association strength, or another symbolic relevance provider. Geometry, tensors, or embeddings may later provide richer `R(k, u)`, but they are projections over the semantic topology rather than the source of the score.

The compressed primitive is:

```text
Key = Static Weight + Horizontal N
```

Vertical phase movement is a separate operation over the resolved semantic state. Horizontal evidence answers what the current key-book contributes within the current phase. Vertical fold movement answers which alternate phase-semantic face of the same key may receive or transform that state next.


## Horizontal neighborhood and vertical phase semantics

Horizontal and vertical movements answer different semantic questions.

```text
Horizontal N = related semantics
Vertical phase = alternate semantics of the same key
```

A resolved node has two coordinates:

```text
v = (k, theta)
```

The horizontal operation explores the key-book while preserving phase:

```text
(k, theta) -> (N(k), theta)
(k, theta) -> (k_prime, theta)
```

This keeps the same phase and moves to neighboring concepts. It asks: what is connected to this meaning?

The vertical operation keeps the key fixed and changes phase:

```text
(k, theta_i) -> (k, theta_j)
```

This changes the semantic face through which the same key is interpreted. It asks: what else can this same thing mean under another phase?

For a key such as `CAUSE`, the phase stack can be read as alternate semantics of the same compressed address:

```text
Pop    : CAUSE as trigger
Wo     : CAUSE as condition
Yax    : CAUSE as candidate
Sek    : CAUSE as operation
Ch'en  : CAUSE as observed relation
Xul    : CAUSE as collapsed meaning
```

Phase is therefore not merely execution timing. It is part of semantic interpretation.

The semantic state can be summarized as:

```text
Semantic state = W(k) + N(k) + Theta(k)
```

`W(k)` is static identity/weight. `N(k)` supplies horizontal contextual semantics. `Theta(k)` supplies alternate phase-semantic interpretation for the same key.

## FoldDelta is semantic, not vectorial

`FoldDelta != VecDelta`. A `FoldDelta` describes verified semantic displacement in the unfolded topology:

```text
Delta_F: v_a -> v_b
```

A vector delta is only the displacement produced by one projection:

```text
Delta_vec = P(v_b) - P(v_a)
```

Therefore:

```text
Delta_F is semantic
Delta_vec is representational
```

`DirectionStore` can accumulate verified semantic displacements without requiring a specific embedding, vector, tensor, or geometry engine. Projection indexes can accelerate retrieval, but they are not the semantic source of truth.

## Layer responsibilities

| Layer | Fundamental object | Operation | Authority |
|-------|--------------------|-----------|-----------|
| Semantic Fold Compression Grammar | key-word / key-book | declare + unfold + symbolic score | manifest authority |
| Semantic Fold Graph Topology | node / edge / fold / phase-face | traverse horizontal N and vertical Theta | graph realization |
| Geometric Node Field | vector / coordinate / tensor | project | representation only |

Calling the manifests themselves the Semantic Fold Graph would collapse the compressed source layer into its unfolded graph realization. This kit keeps those stages separate.

## Terminology note: overloaded graph words

`book` and `fold` are common words in graph theory and graph-processing literature, so this kit uses qualified meanings.

| Word | KHANARY key-grammar meaning | Avoid confusing with |
|------|-----------------------------|---------------------|
| `book` | A manifest-backed declared neighborhood of key-words. In files, this is a `*.manifest.json` key-expansion map. | Graph book embeddings, book thickness, pages/spines in topological graph theory, or ordinary documentation books. |
| `fold` | A phase-aware traversal/composition operation in the K'UHUL/XCFE runtime. Horizontal fold means same-phase composition; vertical fold means phase transition. | Generic graph folding, quotient graphs, protein folding, or arbitrary reduction/fold functions. |
| key-word | A singular resolved key-word/evidence unit, usually produced from one token, ngram, class, alias, relation, or phase marker. | Ordinary word tokens without manifest identity. |
| key-book | A plural declared neighborhood containing many key-words and their expansion edges. | Graph book embeddings, book thickness, pages/spines in topological graph theory, or ordinary documentation books. |
| Bag of Key-Words | A multiset of singular resolved key-words derived from tokens, ngrams, and classes. | Bag-of-words without manifest-backed key identity. |

Singular/plural convention: **key-word** is the singular evidence/address unit; **key-book** is the plural manifest neighborhood that stores many key-words and their expansion edges.

When this document says **book**, read **key-book** or **manifest book**. When it says **fold**, read **K'UHUL fold** or **phase fold**. Unqualified uses are shorthand only inside this kit.

## The `⟁KEYGRAMMAR` type signature

`data/manifest/css.manifest.json` declares the system signature:

```json
"⟁KEYGRAMMAR": [
  "key:address(book)",
  "book:declared-neighborhood",
  "grammar:constrained-book-traversal",
  "phase:Wo",
  "phase:Yax",
  "phase:Ch'en"
]
```

This is the type signature for the manifest layer.

- A **key-word** is a singular key address inside a key-book.
- A **key-book** is a manifest-backed declared neighborhood of key-words, not a graph-theory book embedding.
- A **manifest** is the serialized key-book.
- A **grammar** is constrained traversal over key-book neighborhoods.
- The traversal has phase discipline: Wo binds a token/ngram to an address, Yax chooses and traverses expansions, and Ch'en validates the result before downstream commit.

## Bag of Key-Words

The runtime input is closer to a **Bag of Key-Words** than a plain bag of words, and ambiguous surface forms must first resolve into candidate sense keys.

A natural-language query produces tokens and ngrams. Each token/ngram can map to one or more candidate sense keys, and each selected sense key is a key-word. Those key-words are the semantic evidence units used by later ranking, graph planning, and fold admission.

```text
query text
  -> tokens + ngrams + classes
  -> candidate key-words
  -> manifest expansion graph
  -> phase/intent/relation/operator/topology evidence
  -> GraphPlan / SGSFG / XCFE / K'UHUL projections
```

This is why the key grammar is highly related to ngram types and classes. Ngrams are not only lexical spans; they are candidate handles into a manifest-backed keyspace. `key_references` and `ngram_references` carry those handles with `source_kind`, `source_value`, resolved key, and expansion.

## Manifest key-books

All of these manifest key-books share the same shape: `key-word -> expansion[]`.

| Key-book | Role |
|------|------|
| `data/manifest/words.manifest.json` | Canonical lexical and semantic vocabulary: words, aliases, relation families, phase markers, intents, dispatch keys, and conditional expansions. |
| `data/manifest/css.manifest.json` | Atomic style keys and composed UI/style blocks such as `⟁BGpanel`, `⟁CARD`, and `⟁WIDGETCARD`; also declares `⟁KEYGRAMMAR`. |
| `data/manifest/folds.manifest.json` | Fold topology and activation channels: horizontal/vertical folds, association channels, syntax books, and fold graph parsing. |
| `data/manifest/gml.manifest.json` | Graph topology and ABI references: Q3/Q4 hypercubes, CCC_n graphs, projection/gyro schemas, validators, and GML loader keys. |
| `data/manifest/aiml.manifest.json` | AIML structural keys: pattern, template, wildcard, topic, that, graph, relation, and advisor entries. |
| `data/manifest/eliza.manifest.json` | ELIZA operator pack: 16 operators mapped to relation families and phase hints. |
| `data/schema/math-isa.json` | Math-domain GraphPlan ISA extension plugged into `L_A`; it declares closed-world math ops and resolver requirements. |

## Expansion graph

A manifest is a directed expansion graph:

```text
key-word -> expansion[0]
key-word -> expansion[1]
key-word -> expansion[n]
```

An expansion element may be:

- another key (`hi -> hello`)
- a relation (`ELIZA-1:CAUSE -> @causes`)
- an intent (`intent:salutation`)
- a phase marker (`⟁Pop`, `phase:Wo`)
- a domain operator (`Factory:create`, `SOLVE_LINEAR`)
- a topology reference (`fold:horizontal`, `gml:hypercube_q3`)
- a typed conditional object (`{"@if": ..., "@then": [...], "@else": [...]}`)

The schema for this book shape is `data/schema/manifest-map.schema.json`. It allows string tokens and typed declarative conditionals. Loading must never execute conditionals; it only preserves them as declarative XCFE data for later lowering.

## Shared transpiler engine

The engine is shared. The domain-specific grammar lives in the manifest contents.

```text
css.manifest.json   + resolve_manifest -> CSS-key transpiler
words.manifest.json + resolve_manifest -> lexical-key transpiler
folds.manifest.json + resolve_manifest -> fold-topology transpiler
gml.manifest.json   + resolve_manifest -> graph-topology transpiler
aiml.manifest.json  + resolve_manifest -> AIML-structure transpiler
eliza.manifest.json + resolve_manifest -> relation/operator transpiler
```

The same engine reads every book. Adding a domain means adding new declared keys and expansions, not changing the traversal engine.

## Lookup cascade

`Factory::lookup_key` and the ngram payload builder should be read as manifest-backed lookup, not plain key-value lookup.

```text
query token or ngram
  -> manifest_reg.has(token)?
       yes -> manifest_reg.resolve(token) -> expansion array
              -> recursively inspect expansion entries that are keys
       no  -> normalize/candidate-match/fall through to stored keys
```

The runtime evidence surface is `key_references`:

```json
{
  "source_kind": "token|ngram|meaning|control",
  "source_value": "hello",
  "resolved_key": "hello",
  "expansion": ["greeting", "intent:salutation", "⟁Pop"]
}
```

That evidence is what later components can use for incidence fingerprints, relevance scores, graph planning, and fold admission.

## Phase discipline

Key traversal follows a mini-fold:

| Phase | Traversal responsibility |
|-------|--------------------------|
| Wo | Bind raw query evidence to candidate key-words in the active book. |
| Yax | Select expansion paths, traverse aliases/compositions, and choose candidate relation/operator/topology evidence. |
| Ch'en | Validate the expansion result against schema, phase constraints, and closed-world domain rules. |

`folds.manifest.json` names the activation fold:

```text
Text -> Grams -> Associations -> Books -> Atoms -> Relations -> FoldGraph
```

That is the route from surface text to key-words.

## Singular/plural semantic context

The C++ layer already carries the class boundary, so this kit does not invent `DirectionStore2`, `FoldDirectionStore`, or another context class.

```text
FoldDelta      = one observed/verified semantic displacement
DirectionStore = collection and aggregation boundary
FoldDirection  = derived reusable direction
```

The lifecycle is:

```text
E_i^GOOD
  -> FoldDelta_i
  -> DirectionStore{FoldDelta_i}
  -> PrincipalDirection
  -> FoldDirection
```

The cardinalities are:

```text
1 Episode -> 1 FoldDelta
N compatible FoldDelta -> 1 FoldDirection
N FoldDirection -- WCR/Yax --> 1 or bounded set of applicable directions
```

The semantic-context decision belongs at the **DirectionStore aggregation boundary**. It should not mean "all GOOD deltas." It means the store decides which verified displacements are compatible enough to participate in the same derived direction.

Formally:

```text
D_Q = PrincipalDirection(Deltas_Q)
Deltas_Q = { DeltaF_i | Compatible(F_i, F_Q) }
```

The current implementation is narrower and concrete:

- Source files: `src/kuhul/fold_delta.h`, `src/kuhul/fold_direction.h`, and `src/kuhul/fold_direction.cpp`.
- Ingest gate: `delta.verdict == "GOOD"`, `delta.micronaut_id` is non-empty, and `jrom_seq` gives idempotency.
- Current membership key for factory-evolution episodes: `store_[delta.micronaut_id]`. All GOOD capability/governs deltas for one micronaut contribute to that micronaut's `FoldDirection`.
- Current discrete `PrincipalDirection`: sorted union/consensus of `RelationDelta.added_capabilities` into `capability_key` and `RelationDelta.added_governs` into `governs_key`.
- Current retrieval primitive: `R = Jaccard(query_caps, capability_key)` and `S = W * C * R`.
- Current wiring: startup calls `direction_store.rebuild_from_jrom(jrom)` and `factory_advisor_commit` calls `direction_store.ingest(delta)` after GOOD verification. No runtime route currently calls `DirectionStore::query(...)`, so retrieval compatibility is implemented as a primitive but not yet connected to serving.

So `Compatible(F_i, F_Q)` currently means:

1. At ingest: same `micronaut_id` within the factory-advisor evolution path.
2. At retrieval primitive: overlap between query capability evidence and the derived direction's `capability_key`.
3. Never: arbitrary PCA over every GOOD episode.

This is a semantic-context boundary, not a grammatical plural marker. Singular/plural matters because singular `FoldDelta` preserves evidence and provenance, while plural `DirectionStore` defines the compatible neighborhood from which `FoldDirection` can emerge.

## AIML lowering is manifest-driven

`L_A` is manifest-driven. AIML patterns decide when to invoke a grammar route; manifests define what the route means.

```text
AIML pattern match
  -> tokenize captured input
  -> resolve tokens/ngrams against manifest books
  -> collect phase/intent/relation/operator evidence
  -> assemble GraphPlan operations from declared ISA/domain entries
  -> project to SGSFG / Yax / XCFE / K'UHUL
```

For math, `data/schema/math-isa.json` declares the closed-world GraphPlan ops and resolver capabilities. The assemble step must not invent runtime math operations that are absent from this declared ISA.

## Key-book operations

The formal operations over manifest key-books are:

| Operation | Meaning |
|-----------|---------|
| `has(book, key)` | True if the key-word is declared in the book. |
| `expand(book, key)` | Return the ordered expansion array for a declared key. |
| `resolve(bookset, evidence)` | Normalize evidence into a declared key and return its expansion. |
| `closure(bookset, key, depth)` | Recursively expand key-word expansion entries to a bounded depth. |
| `intersect(book_a, book_b)` | Return shared key-words or shared expansion tags across books. |
| `classify(expansion)` | Partition expansion tokens into phases, intents, relations, operators, topology refs, and literals. |
| `validate(expansion)` | Check schema shape, closed-world operator policy, allowed conditionals, and phase constraints. |

All recursive operations must be bounded and cycle-aware.

## Open specifications

The grammar layer locks the vocabulary model, but four specs still need explicit contracts:

1. `A(v)` components: especially relevance over expanded incidence fingerprints.
2. Full `L_A` assembly: manifest-resolve evidence to GraphPlan op construction.
3. SGSFG edge vocabulary: `REQUIRES`, `BLOCKS`, `PRODUCES`, `VERIFIES`, `DELEGATES_TO`, `RETURN_TO`, `RESUMES`, and miss classes.
4. Key-book algebra runtime: exact closure, intersection, cycle policy, phase constraints, and validation semantics.

## One-line contract

`words.manifest.json` is the key grammar. Every manifest file is a key-book. `resolve_manifest` is the phase-constrained unfold engine. `⟁KEYGRAMMAR` is the type signature. `L_A` is manifest-driven. Ngrams produce candidate sense keys and then a Bag of Key-Words; joke frames can keep pun senses active while selecting a primary semantic key; manifest key-books unfold that bag into query-local Semantic Fold Graph Topology; `S(k)=W_k+H_N(k)` scores keys from static weight plus horizontal neighborhood evidence before vectors; `Semantic state = W(k) + N(k) + Theta(k)` adds the vertical phase-semantic face of the same key; geometric fields project that topology without redefining semantic authority; and DirectionStore guards the plural semantic-context boundary for verified fold directions.
