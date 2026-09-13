# graph-provenance-explorer

A summary built from retrieved passages is only trustworthy if every sentence can be traced back to a source that actually exists and a reader can see how it was reached. This repository implements source-preserving graph retrieval over a small authored corpus and renders inspectable, citation-linked answers that abstain when nothing in the corpus supports them.

**Status:** `demo_ready` - runs end to end on authored synthetic fixtures. No
real-data evaluation has been performed in this repository.

## Relationship to research

`coauthored_research`

Newly built companion explorer for the published article *ClinicGraphRAG: knowledge graph and LLM retrieval-augmented generation for reliable clinical decision support summaries* (Discover Artificial Intelligence, 2026, DOI 10.1007/s44163-026-01492-w), on which MD Mizanur Rahman is a coauthor. This repository is not the article's original code. The article's reported classifier result is not reproduced here, and retrieval quality on this synthetic corpus says nothing about the article's system. Coauthor names are not listed here; see the publisher record.

## What is implemented

- **Authored synthetic corpus** (`examples/corpus/v1`): twelve short fictional guidance notes, `DOC-A1` to `DOC-L1`, about invented workflow terms (Marlow Index, Kestrel score, Thornbury ladder, and so on). Each has numbered passages addressed as `DOC-A1#p3`. `relations.yaml` defines typed edges (`supports`, `cites`, `defines`, `contradicts`, `refines`), every one with `provenance: authored-v1`. See `docs/data.md`.
- **Typed graph** (networkx): document, passage, concept, assertion and source nodes; document-to-passage `contains` edges added at ingestion with their own provenance label. Spring layout with seed 7, exported so a web explorer renders the identical arrangement.
- **Retrieval**: an in-repo BM25 (no ranking dependency), a hashed bag-of-words cosine baseline, and graph-neighbourhood retrieval that seeds from the top lexical passages, expands one hop along typed edges, reranks by lexical score plus a configured edge-type weight, and returns every passage **with the path** (list of `(node, edge_type, node)`) that reached it. See `docs/method.md`.
- **Deterministic renderer**: lists retrieved passages verbatim with `[DOC-A1#p3]` citations; abstains with `No supporting passage found in the approved corpus.` when the top score is below the configured threshold; raises `CitationError` in code if any citation would not resolve. An `LLMRenderer` Protocol is declared with no provider implementation.
- **Evaluation**: recall@1/3/5, MRR, source-path validity rate, unsupported-citation rate, abstention accuracy on unanswerable questions, over a 25-question fixture. Writes `metrics.json` plus a run manifest with `mode: demo` or `mode: smoke`. See `docs/evaluation.md`.
- **CLI**: `ingest`, `query`, `evaluate`, `export-graph`, `smoke`, `demo`.

## Quickstart (offline, CPU, < 1 minute)

```
pip install -e .            # or: pip install -r requirements.txt and set PYTHONPATH=src
python -m graph_provenance_explorer smoke
python -m graph_provenance_explorer query "When is the Marlow Index recomputed?" --mode graph --show-paths
python -m graph_provenance_explorer query "When is the Marlow Index recomputed?" --mode lexical
python -m graph_provenance_explorer evaluate --mode all
python -m graph_provenance_explorer export-graph
python -m graph_provenance_explorer demo
python -m pytest -q
```

`make smoke`, `make demo`, `make test`, `make evaluate` and `make export-graph` wrap the same commands. Nothing downloads anything, nothing needs a GPU, a key or a model service.

## Demonstration output

`make demo` writes:

- `examples/output/demo/metrics.json` - metrics for the `lexical`, `graph` and `vector` modes.
- `examples/output/demo/answers.jsonl` and `answers.md` - every fixture question rendered in every mode, with citations and paths.
- `examples/output/demo/manifest.yaml` - run manifest, `mode: demo`.
- `examples/output/graph_export.json` - nodes, edges, layout, passages and provenance for a web explorer.
- `examples/output/graph_layout.json` - the seed-7 spring layout on its own.

The committed `metrics.json` was computed by `make demo` on the authored synthetic fixture `examples/corpus/v1` with the question fixture `examples/questions/v1.jsonl`, seed 42. It is not a benchmark result and it says nothing about any real corpus. Two things the demo shows that are worth reading in `docs/evaluation.md`: lexical and graph retrieval rank passages differently on most fixture questions (documented, not claimed better), and a score threshold does not separate an on-topic unanswerable question from an answerable one.

## Data access

There is no real dataset. The corpus is hand-authored fiction and ships in the repository; `docs/data.md` describes its format, its validation (`tools/check_corpus.py`), and how to point the CLI at a corpus of your own with `--corpus`. Nothing is downloaded.

## Evaluation protocol

Described in `docs/evaluation.md`: the question fixture, metric definitions, the abstention threshold rule, and the local test run summary line.

## Limitations

- The corpus is 12 fictional notes. Every number in `metrics.json` is a property of that fixture and the configuration, not of the method.
- Abstention is a score threshold. It catches off-corpus questions and does not catch questions that reuse corpus vocabulary but have no answer (see `U04` in the fixture).
- Graph retrieval expands one hop from lexical seeds; a passage with no lexical overlap and no edge to a seed cannot be reached.
- The vector baseline is a hashed bag of words, not a learned embedding.
- The template renderer quotes passages; it does not compose a summary. Any model-backed renderer is out of scope for this repository.
- The graph has more nodes than the range given in the original brief (see `docs/data.md`, "Node count").

## Related work

- ClinicGraphRAG: knowledge graph and LLM retrieval-augmented generation for reliable clinical decision support summaries. Discover Artificial Intelligence, 2026. DOI 10.1007/s44163-026-01492-w.

## Contribution and provenance

See `NOTICE.md`. The implementation was produced on commission with AI-assisted code generation and reviewed before release; the owner's role is commissioning, review and publication.

## License

MIT. See `LICENSE`.
