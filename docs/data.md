# Data

## What ships

Only an authored, synthetic corpus. There is no real dataset, no download, no
patient record, no guideline text. Everything under `examples/corpus/v1` was
written for this repository and describes invented workflow terms in a
fictional review desk. `examples/corpus/v1/FIXTURE.md` carries the fixture
label and counts computed by `tools/check_corpus.py`.

## Corpus format

```
examples/corpus/v1/
  DOC-A1.md ... DOC-L1.md   twelve guidance notes
  relations.yaml            typed edges plus concept, assertion and source nodes
  FIXTURE.md                fixture label, written by tools/check_corpus.py
```

Each note is a markdown file with YAML front matter (`id`, `title`, `corpus`), a
blockquote stating that the material is synthetic, and passages that start
with `[p1]`, `[p2]`, ... on their own paragraphs. A passage is addressed as
`DOC-A1#p3`. The loader (`graph_provenance_explorer.corpus`) rejects a file
whose filename does not match its `id`, whose passage numbers are not
consecutive from 1, or whose body lacks the phrase `Authored synthetic
material`.

`relations.yaml` has four lists:

| Key | Node id pattern | Purpose |
|---|---|---|
| `concepts` | `CON-NAME` | the invented terms a passage defines |
| `assertions` | `AST-01` | one-sentence claims that passages support |
| `sources` | `SRC-01` | fictional notes and minutes that passages cite |
| `edges` | | `source`, `target`, `type`, `provenance` |

Edge types are exactly `supports`, `cites`, `defines`, `contradicts`,
`refines`. Every edge in the shipped file has `provenance: authored-v1`. The
loader rejects an unknown type, a missing provenance, an endpoint that does not
resolve, a self-loop, or a duplicate edge. Ingestion adds one `contains` edge
from each document node to each of its passages with provenance
`ingest-structural-v1`; those edges are not in the YAML because they are
derived from the files.

## What the corpus contains

Twelve notes, three passages each, each note between 150 and 300 words. The
topics are invented: the Marlow Index (queue ordering), the Kestrel score
(agreement bands), the Thornbury ladder (escalation), the Osprey window
(timing), the Brindle flag (disagreement marker), the Quillon handoff, the
Sable checkpoint (release gate), the Wren ledger (append-only record), the
Ferris loop (correction cycle), the Lantern review (second reading), the
Corvid audit and the Halden tier (source reliability). One disagreement is
authored on purpose: `DOC-B1#p2` states a four-cycle recomputation interval for
the Kestrel score and `DOC-E1#p3` states six; the `contradicts` edge records
it and the fixture question `Q05` has both as gold.

None of this is clinical guidance and no real drug, guideline or condition is
named. `tools/check_corpus.py` also refuses a small list of terms that would
suggest otherwise.

## Node count

The brief for this repository asked for 20 to 40 nodes after ingestion. With
12 documents, three passages each (so that `#p3` addresses exist) and all five
node types populated, the graph has 61 nodes and 74 edges (12 document, 36
passage, 6 concept, 4 assertion, 3 source; counts computed by
`tools/check_corpus.py` and by `python -m graph_provenance_explorer ingest`).
The range could only be met by dropping to two passages per document or by
leaving node types empty. Passage addressing and full type coverage were kept
and the deviation is recorded here.

## Question fixture

`examples/questions/v1.jsonl`: 25 lines, one JSON object each with `id`,
`question`, `gold` (list of passage ids) and `answerable`. Twenty are
answerable with one or two gold passages; five (`U01` to `U05`) are
unanswerable with empty gold. `U04` deliberately reuses a corpus term
(Marlow Index) so that the evaluation shows what a score threshold cannot do.
The loader rejects an answerable question with no gold, an unanswerable one
with gold, a gold id that does not resolve, and malformed JSON.

## Using your own corpus

Point any subcommand at a directory with the same layout:

```
python -m graph_provenance_explorer ingest --corpus path/to/corpus
python -m graph_provenance_explorer evaluate --corpus path/to/corpus --questions path/to/questions.jsonl --out out/
```

The loader validates the directory and exits with code 2 and a message naming
the problem if it does not match. Nothing is fetched from anywhere.
