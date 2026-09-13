"""Lexical, vector and graph retrieval behaviour, including paths and failure cases."""

from __future__ import annotations

import pytest

from graph_provenance_explorer.config import ConfigError, validate_config
from graph_provenance_explorer.corpus import Passage
from graph_provenance_explorer.lexical import BM25Index, tokenize
from graph_provenance_explorer.retrieval import Hit, RetrievalError, validate_hits
from graph_provenance_explorer.vector import HashedVectorIndex, embed


def _toy():
    return (
        Passage("DOC-T1#p1", "DOC-T1", 1, "The Marlow Index orders the queue by window age."),
        Passage("DOC-T1#p2", "DOC-T1", 2, "The Kestrel score counts agreeing passages per line."),
        Passage("DOC-T1#p3", "DOC-T1", 3, "The ledger is append only and never edited."),
    )


def test_tokenize_lowercases_and_drops_stopwords():
    assert tokenize("The Marlow Index, is IT?") == ["marlow", "index"]


def test_bm25_ranks_passage_containing_query_terms_first():
    index = BM25Index(_toy())
    hits = index.search("Kestrel score", k=3)
    assert hits[0].passage_id == "DOC-T1#p2"
    assert all(h.score > 0 for h in hits)


def test_bm25_returns_nothing_for_terms_absent_from_corpus():
    index = BM25Index(_toy())
    assert index.search("zeppelin cartography", k=3) == ()


def test_bm25_rejects_empty_passage_list():
    with pytest.raises(ValueError):
        BM25Index(())


def test_vector_embedding_is_unit_length_and_stable():
    a = embed("Marlow Index queue", 64)
    b = embed("Marlow Index queue", 64)
    assert (a == b).all()
    assert abs(float((a * a).sum()) - 1.0) < 1e-9
    assert float(embed("", 64).sum()) == 0.0


def test_vector_index_prefers_lexically_overlapping_passage():
    index = HashedVectorIndex(_toy(), dims=128)
    assert index.search("append only ledger", k=1)[0].passage_id == "DOC-T1#p3"


def test_vector_index_rejects_tiny_dims():
    with pytest.raises(ValueError):
        HashedVectorIndex(_toy(), dims=2)


def test_unknown_mode_raises(session):
    with pytest.raises(RetrievalError, match="Unknown retrieval mode"):
        session.retriever.retrieve("Marlow Index", "hybrid")


def test_empty_query_raises(session):
    with pytest.raises(RetrievalError, match="empty"):
        session.retriever.retrieve("   ", "lexical")


def test_lexical_hits_have_no_path_and_origin_seed(session):
    hits = session.retriever.retrieve("When is the Marlow Index recomputed?", "lexical")
    assert hits and all(h.path == () and h.origin == "seed" for h in hits)


def test_graph_hits_carry_valid_paths(session):
    hits = session.retriever.retrieve("When is the Marlow Index recomputed?", "graph")
    validate_hits(hits, session.corpus, session.graph)
    expanded = [h for h in hits if h.origin == "expanded"]
    assert expanded, "graph mode should surface at least one expanded passage for this question"
    for h in expanded:
        assert h.path, "expanded hits must record how they were reached"
        for step in h.path:
            assert session.graph.has_edge(step.source, step.target)
            assert session.graph.edges[step.source, step.target]["type"] == step.edge_type


def test_neighbourhood_bridges_through_assertion_node(session):
    reached = {node: path for path, node in session.retriever._neighbourhood("DOC-H1#p3", 1, {"assertion"})}
    assert "DOC-G1#p1" in reached, sorted(reached)
    steps = [s.as_tuple() for s in reached["DOC-G1#p1"]]
    assert steps == [("DOC-H1#p3", "supports", "AST-01"), ("DOC-G1#p1", "supports", "AST-01")]


def test_neighbourhood_does_not_bridge_through_document_nodes(session):
    reached = {node for _, node in session.retriever._neighbourhood("DOC-K1#p3", 1, set())}
    assert "DOC-K1#p1" not in reached and "DOC-K1#p2" not in reached


def test_graph_score_is_lexical_plus_mean_edge_weight(session, config):
    weights = config["retrieval"]["edge_weights"]
    hits = session.retriever.retrieve("When is the Marlow Index recomputed?", "graph")
    assert any(h.path for h in hits)
    for h in hits:
        if h.path:
            expected = h.lexical_score + sum(weights[s.edge_type] for s in h.path) / len(h.path)
            assert abs(h.score - expected) < 1e-9
        else:
            assert h.score == h.lexical_score


def test_lexical_and_graph_rankings_differ_on_at_least_one_fixture_question(session, questions):
    differing = [
        q.id
        for q in questions
        if [h.passage_id for h in session.retriever.retrieve(q.text, "lexical")]
        != [h.passage_id for h in session.retriever.retrieve(q.text, "graph")]
    ]
    assert differing, "expected at least one question where the two modes rank passages differently"


def test_k_limits_number_of_hits(session):
    assert len(session.retriever.retrieve("Wren ledger entry", "graph", k=2)) == 2
    with pytest.raises(RetrievalError):
        session.retriever.retrieve("Wren ledger entry", "graph", k=0)


def test_validate_hits_rejects_foreign_passage(session):
    with pytest.raises(RetrievalError, match="does not resolve"):
        validate_hits((Hit("DOC-Z9#p1", 1.0, 1.0, "seed", ()),), session.corpus, session.graph)


def test_config_without_all_edge_weights_is_rejected(config):
    broken = {**config, "retrieval": {**config["retrieval"], "edge_weights": {"supports": 1.0}}}
    with pytest.raises(ConfigError, match="edge_weights"):
        validate_config(broken)
