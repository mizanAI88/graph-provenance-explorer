# FIXTURE

Authored synthetic demonstration data. Fictional identifiers. Not derived from
any patient, dataset, or person. Hand-authored prose (no generator script, no
seed); validated by `tools/check_corpus.py`, fixture version `v1`.

Every document names an invented workflow term (Marlow Index, Kestrel score,
Thornbury ladder, Osprey window, Brindle flag, Quillon handoff, Sable
checkpoint, Wren ledger, Ferris loop, Lantern review, Corvid audit, Halden
tier). None of them exists outside this repository. The text contains no real
drug names, no real guidelines, and no disease-specific advice.

## Counts (computed by tools/check_corpus.py)

- Documents: 12
- Passages: 36
- Word budget per document: 150 to 300
- Relations in relations.yaml: 38
- Graph nodes after ingestion: 61 {'document': 12, 'passage': 36, 'concept': 6, 'assertion': 4, 'source': 3}
- Graph edges after ingestion: 74 {'cites': 7, 'contains': 36, 'contradicts': 1, 'defines': 6, 'refines': 10, 'supports': 14}

| Document | Title | Words | Passages |
|---|---|---|---|
| DOC-A1 | Protocol for the fictional Marlow Index | 235 | 3 |
| DOC-B1 | Handling of the invented Kestrel score | 208 | 3 |
| DOC-C1 | The Thornbury ladder for disputed summary lines | 225 | 3 |
| DOC-D1 | The Osprey window | 212 | 3 |
| DOC-E1 | The Brindle flag | 212 | 3 |
| DOC-F1 | The Quillon handoff | 185 | 3 |
| DOC-G1 | The Sable checkpoint | 190 | 3 |
| DOC-H1 | The Wren ledger | 196 | 3 |
| DOC-I1 | The Ferris loop | 194 | 3 |
| DOC-J1 | The Lantern review | 196 | 3 |
| DOC-K1 | The Corvid audit | 180 | 3 |
| DOC-L1 | The Halden tier of source reliability | 203 | 3 |
