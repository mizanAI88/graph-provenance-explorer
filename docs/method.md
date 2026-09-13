# Method

The pipeline is: corpus -> typed graph -> retrieval (three modes) -> renderer.
Every stage is deterministic and offline. The figure
`docs/figures/graph_retrieval.svg` (drawn by `tools/render_figure.py`) shows the
graph mode.

## 1. Ingestion and graph

`corpus.load_corpus` parses the markdown notes and `relations.yaml` into frozen
dataclasses. `graph.build_graph` creates a `networkx.DiGraph` with node
attribute `type` in `{document, passage, concept, assertion, source}` and edge
attributes `type` and `provenance`. Nodes are inserted in sorted id order and
edges in sorted `(source, target, type)` order so that two builds are
identical, which is what makes the seeded spring layout reproducible.

`graph.compute_layout` calls `networkx.spring_layout(graph, seed=7,
iterations=100)` and rounds coordinates to six decimals. `export-graph`
writes the layout twice: inside `graph_export.json` next to nodes, edges,
passages and provenance, and alone in `graph_layout.json`. A test asserts that
two runs are byte-identical and that the committed layout matches a fresh
run.

## 2. Lexical baseline (BM25)

`lexical.BM25Index` is a plain Okapi BM25 over passage text with the
non-negative idf variant `log(1 + (N - n + 0.5) / (n + 0.5))`. Tokens are
lowercase alphanumeric runs with a short stopword list that includes question
words (`what`, `which`, `how`, `many`, ...) because they carry no signal in a
question-answering index and, left in, matched unanswerable questions to
passages that happen to contain them. There is no external ranking
dependency.

## 3. Vector baseline (optional)

`vector.HashedVectorIndex` hashes each token with SHA-1 into one of
`vector.dims` buckets, builds an L2-normalised count vector per passage, and
scores a query by cosine similarity. It is a baseline for comparison only; it
uses no learned model.

## 4. Graph-neighbourhood retrieval

`retrieval.Retriever._graph`:

1. Score every passage with BM25. Take the top `retrieval.seed_k` with a
   positive score as **seeds**. A seed's initial score is its lexical score
   and its path is empty.
2. From each seed, walk `retrieval.hops` passage-level hops along typed
   edges in both directions (each edge is recorded in its stored direction).
   Crossing a node whose type is in `retrieval.bridge_via` (concept,
   assertion, source) does not consume a hop: the walk continues through it
   to the passages on its other side, and both edges appear in the path.
   Document nodes are never bridged, so passages of the same document are not
   neighbours merely by being in the same file.
3. Every reached passage becomes a candidate with
   `score = lexical(passage) + mean(edge_weights[type] for each edge on the path)`,
   using the weights in `retrieval.edge_weights`. The candidate keeps the
   highest-scoring path (shorter path wins ties). A seed that is also reached
   over an edge keeps `origin = "seed"` and may gain the bonus; this is what
   lets two seeds that are linked to each other rise together.
4. Rank by score, tie-break by passage id, return the top `retrieval.top_k`.

Each returned `Hit` carries `passage_id`, `score`, `lexical_score`, `origin`
(`seed` or `expanded`) and `path`, a tuple of `PathStep(source, edge_type,
target)`. `retrieval.validate_hits` re-checks every hit and every path step
against the corpus and graph, and the evaluation reports a path-step validity
rate as well as a citation validity rate.

The `contradicts` edge type has a positive but low weight so that a passage
that disagrees with a seed is surfaced next to it, which is the point of
recording contradictions, rather than hidden.

## 5. Renderer and abstention

`renderer.TemplateRenderer.render` returns an `Answer`. If there are no hits
or the top score is below the mode's threshold in `abstention`, the answer is
the single sentence `No supporting passage found in the approved corpus.` with
no citations. Otherwise it lists every hit as `[DOC-A1#p3] (score; path)`
followed by the passage text verbatim, and ends with a `Sources:` line.

Before any text is produced, `assert_citations_resolve` raises
`CitationError` if a citation is not a passage id of the loaded corpus. This
is a raised exception, not an `assert` statement, so it survives `python -O`.

`renderer.LLMRenderer` is a `typing.Protocol` describing the same `render`
signature. No provider implementation exists in the package; a test walks
every module and fails if one appears.

## 6. Settings taken from the source description

None. The retrieval weights, seed and top-k counts, hop count, BM25
parameters and abstention thresholds in `configs/default.yaml` are
implementation settings chosen on the authored fixture for this repository.
The thresholds were set by one rule: the lowest value at which no answerable
fixture question abstains (see `docs/evaluation.md`).
