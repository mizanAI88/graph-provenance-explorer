# Evaluation

Everything on this page was computed by `python -m graph_provenance_explorer demo`
(equivalently `make demo`) on the authored synthetic fixture
`examples/corpus/v1` with the question fixture `examples/questions/v1.jsonl`,
seed 42, on 2026-09-13. None of it is a benchmark result. The fixture is 12
fictional notes and 25 authored questions; the values describe that fixture
and this configuration, and they say nothing about any real corpus or about
the article this repository accompanies.

## Protocol

For each retrieval mode (`lexical`, `graph`, `vector`) and each question:

1. Retrieve the top 5 passages (`retrieval.top_k`).
2. `retrieval.validate_hits` checks that every hit and every path step
   resolves in the corpus and graph (a failure raises; it is not counted).
3. The `TemplateRenderer` renders the answer or abstains.

Metrics, over the 20 answerable questions unless stated:

| Metric | Definition |
|---|---|
| `recall_at_k` (k = 1, 3, 5) | mean over answerable questions of the fraction of gold passages in the top k |
| `mrr` | mean reciprocal rank of the first gold passage |
| `source_path_validity_rate` | over every citation emitted in every answer: fraction that resolves to a corpus passage |
| `path_step_validity_rate` | over every path step of every hit (graph mode only): fraction that is an edge of the graph with the recorded type |
| `unsupported_citation_rate` | over citations emitted for answerable questions: fraction not in that question's gold set |
| `abstention_accuracy_unanswerable` | over the 5 unanswerable questions: fraction on which the renderer abstained |
| `false_abstention_rate_answerable` | over answerable questions: fraction on which the renderer abstained |

Because the template renderer cites every returned passage (up to 5) and most
questions have one gold passage, `unsupported_citation_rate` is dominated by
`top_k`; it is reported as a property of the rendering policy, not as a claim
about retrieval precision.

## Results on the fixture (computed, not a benchmark)

| metric | lexical | graph | vector |
|---|---|---|---|
| recall_at_1 | 0.65 | 0.6 | 0.475 |
| recall_at_3 | 0.95 | 1.0 | 0.9 |
| recall_at_5 | 0.95 | 1.0 | 0.975 |
| mrr | 0.85 | 0.841667 | 0.739167 |
| source_path_validity_rate | 1.0 | 1.0 | 1.0 |
| path_step_validity_rate | n/a | 1.0 | n/a |
| unsupported_citation_rate | 0.681416 | 0.648649 | 0.733333 |
| abstention_accuracy_unanswerable | 0.4 | 0.4 | 0.8 |
| false_abstention_rate_answerable | 0.0 | 0.0 | 0.0 |
| citations_emitted | 113 | 111 | 105 |
| abstention_threshold | 3.0 | 3.0 | 0.2 |

Source: `examples/output/demo/metrics.json`.

## Lexical versus graph rankings

The two modes return a different ranked list on 24 of the 25 fixture
questions (`questions_ranked_differently_from_lexical` in `metrics.json`;
the exception is `U02`, where neither mode finds any passage). This is
documented as a difference, not claimed as an improvement: on this fixture
graph mode reaches every gold passage within the top 3 where lexical misses
one (`Q18`), and lexical places the gold passage first more often (`Q01`,
where a passage that `refines` the definition outranks the definition after
the edge bonus). Whether either behaviour is desirable depends on the
corpus and cannot be settled on 25 authored questions.

## Abstention

The thresholds were set by one stated rule: the lowest round value at which
no answerable fixture question abstains (`false_abstention_rate_answerable`
is 0.0 in every mode). What that rule buys and what it does not:

| question | lexical | graph | vector |
|---|---|---|---|
| U01 (Pelican rate) | abstained | abstained | abstained |
| U02 (Bramble panel) | abstained | abstained | abstained |
| U03 (Gullwing uploader) | answered | answered | abstained |
| U04 (Marlow Index badge colour) | answered | answered | answered |
| U05 (overnight roster) | answered | answered | abstained |

`U04` reuses the term "Marlow Index" and scores exactly as high as the
answerable `Q01` in lexical mode, so no threshold can separate them; the
renderer quotes passages about the Marlow Index that do not mention any
badge. `U03` and `U05` score between 3.1 and 4.7 on incidental words
("file", "desk", "duty") that also occur in the corpus. A score threshold
detects vocabulary mismatch, not the absence of an answer. This is a limit of
the method as implemented and is reported rather than tuned away.

## Acceptance tests (all in `tests/`)

| Requirement | Test |
|---|---|
| every displayed source resolves | `test_every_displayed_source_resolves_for_every_fixture_question`, `test_source_path_validity_is_one_in_every_mode` |
| deleting a passage removes its support | `test_deleting_a_passage_removes_its_support`, `test_deleting_a_passage_invalidates_edges_that_reference_it` |
| every edge has a type and provenance | `test_every_edge_has_known_type_and_provenance`, `test_every_graph_edge_has_type_and_provenance` |
| invalid ids raise | `test_parse_passage_id_rejects_malformed_ids`, `test_get_passage_returns_text_and_rejects_unknown`, `test_edge_to_unknown_passage_raises`, `test_questions_with_unresolvable_gold_raise` |
| layout deterministic across two runs | `test_layout_is_deterministic_across_two_builds`, `test_export_graph_is_byte_identical_across_two_runs`, `test_committed_layout_matches_a_fresh_run` |
| abstention triggers | `test_abstention_triggers_on_off_corpus_query`, `test_abstention_triggers_when_top_score_is_below_threshold`, `test_query_abstains_on_nonsense` |
| lexical vs graph differ on at least one question | `test_lexical_and_graph_rankings_differ_on_at_least_one_fixture_question` |
| renderer never emits an id outside the corpus | `test_renderer_refuses_citation_outside_corpus` |
| no provider renderer in the package | `test_llm_renderer_is_a_protocol_with_no_implementation_in_package` |

## Local test run (2026-09-13)

```
$ python -m pytest -q
84 passed in 6.07s
```

Python 3.10, CPU only, no network. `python -m graph_provenance_explorer smoke`
exits 0 in about one second and validates the schema of its own
`metrics.json` and `manifest.yaml` before reporting success.
