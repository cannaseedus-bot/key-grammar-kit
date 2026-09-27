# K'UHUL JSON Key-Grammar Kit

EBNF v3 runtime grammar for the **K'UHUL key-grammar JSON** format, plus corpus records used by the K'UHUL runtime.

The key-grammar defines how structured JSON records are addressed, phase-bound, and validated against the K'UHUL semantic algebra. Every record in the gram store is an instance of one of the row types described by `key-grammar-json.runtime.ebnf`.

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

## Files

| File | Description |
|------|-------------|
| `key-grammar-json.runtime.ebnf` | Full EBNF v3 with SC-1..SC-13 side constraints |
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

## Record format

Every key-grammar record is a JSON object on a single line (JSONL). Minimal shape:

```json
{"schema": "key.grammar.<type>.v1", "key": "<prefix>:<value>", "phase": "<C6 phase>", "channel": "<channel>", "authority": "<corpus>"}
```

The `schema` field identifies the row type and version. The `key` field is the gram store address. `phase` binds the record to a C6 phase for fold authorization.

## Part of

[KHANARY.CPP](https://github.com/cannaseedus-bot) — K'UHUL semantic runtime stack.
