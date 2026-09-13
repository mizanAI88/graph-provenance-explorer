"""Corpus loading, passage addressing, and relations validation (including failure cases)."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from graph_provenance_explorer.corpus import (
    EDGE_TYPES,
    FICTION_MARKER,
    CorpusError,
    load_corpus,
    parse_passage_id,
)


def test_loads_twelve_documents_with_consecutive_passages(corpus):
    assert len(corpus.documents) == 12
    assert [d.id for d in corpus.documents] == [f"DOC-{c}1" for c in "ABCDEFGHIJKL"]
    for doc in corpus.documents:
        assert [p.index for p in doc.passages] == list(range(1, len(doc.passages) + 1))
        assert all(p.id == f"{doc.id}#p{p.index}" for p in doc.passages)


def test_every_document_is_within_word_budget_and_marked_fictional(corpus, corpus_dir):
    for doc in corpus.documents:
        assert 150 <= doc.word_count <= 300, doc.id
        assert FICTION_MARKER in (corpus_dir / doc.path).read_text(encoding="utf-8")


def test_relations_statement_carries_fiction_marker(corpus):
    assert FICTION_MARKER in corpus.relations.statement


def test_every_edge_has_known_type_and_provenance(corpus):
    assert corpus.relations.edges
    for edge in corpus.relations.edges:
        assert edge.type in EDGE_TYPES
        assert edge.provenance == "authored-v1"
        assert edge.source in corpus.node_ids and edge.target in corpus.node_ids


def test_all_five_edge_types_are_used(corpus):
    assert {e.type for e in corpus.relations.edges} == set(EDGE_TYPES)


def test_get_passage_returns_text_and_rejects_unknown(corpus):
    p = corpus.get_passage("DOC-A1#p3")
    assert "Brindle flag" in p.text
    with pytest.raises(CorpusError, match="does not resolve"):
        corpus.get_passage("DOC-Z9#p1")


@pytest.mark.parametrize("bad", ["DOC-A1", "DOC-A1#3", "A1#p3", "DOC-A1#p", "doc-a1#p1"])
def test_parse_passage_id_rejects_malformed_ids(bad):
    with pytest.raises(CorpusError, match="Invalid passage id"):
        parse_passage_id(bad)


def test_parse_passage_id_accepts_well_formed():
    assert parse_passage_id("DOC-K1#p12") == ("DOC-K1", 12)


def test_without_passage_drops_passage_and_its_edges(corpus):
    before = len([e for e in corpus.relations.edges if "DOC-E1#p3" in (e.source, e.target)])
    assert before > 0
    reduced = corpus.without_passage("DOC-E1#p3")
    assert "DOC-E1#p3" not in reduced.passage_ids
    assert not any("DOC-E1#p3" in (e.source, e.target) for e in reduced.relations.edges)
    assert "DOC-E1#p3" in corpus.passage_ids, "original corpus must be unchanged"


def test_missing_corpus_directory_raises(tmp_path):
    with pytest.raises(CorpusError, match="Corpus directory not found"):
        load_corpus(tmp_path / "nope")


def test_unknown_edge_type_raises(corpus_copy: Path):
    rel = corpus_copy / "relations.yaml"
    data = yaml.safe_load(rel.read_text(encoding="utf-8"))
    data["edges"].append({"source": "DOC-A1#p1", "target": "DOC-B1#p1", "type": "mentions", "provenance": "authored-v1"})
    rel.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(CorpusError, match="edge type 'mentions'"):
        load_corpus(corpus_copy)


def test_edge_without_provenance_raises(corpus_copy: Path):
    rel = corpus_copy / "relations.yaml"
    data = yaml.safe_load(rel.read_text(encoding="utf-8"))
    data["edges"].append({"source": "DOC-A1#p1", "target": "DOC-B1#p1", "type": "supports"})
    rel.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(CorpusError, match="provenance"):
        load_corpus(corpus_copy)


def test_edge_to_unknown_passage_raises(corpus_copy: Path):
    rel = corpus_copy / "relations.yaml"
    data = yaml.safe_load(rel.read_text(encoding="utf-8"))
    data["edges"].append({"source": "DOC-A1#p1", "target": "DOC-Q7#p1", "type": "supports", "provenance": "authored-v1"})
    rel.write_text(yaml.safe_dump(data), encoding="utf-8")
    with pytest.raises(CorpusError, match="DOC-Q7#p1"):
        load_corpus(corpus_copy)


def test_document_without_fiction_marker_raises(corpus_copy: Path):
    doc = corpus_copy / "DOC-A1.md"
    doc.write_text(doc.read_text(encoding="utf-8").replace(FICTION_MARKER, "Ordinary material"), encoding="utf-8")
    with pytest.raises(CorpusError, match="marker"):
        load_corpus(corpus_copy)


def test_non_consecutive_passage_numbering_raises(corpus_copy: Path):
    doc = corpus_copy / "DOC-B1.md"
    doc.write_text(doc.read_text(encoding="utf-8").replace("[p3]", "[p4]"), encoding="utf-8")
    with pytest.raises(CorpusError, match="consecutive"):
        load_corpus(corpus_copy)


def test_deleting_a_passage_invalidates_edges_that_reference_it(corpus_copy: Path):
    doc = corpus_copy / "DOC-E1.md"
    text = doc.read_text(encoding="utf-8")
    cut = text[: text.index("[p3]")]
    doc.write_text(cut, encoding="utf-8")
    with pytest.raises(CorpusError, match="DOC-E1#p3"):
        load_corpus(corpus_copy)
