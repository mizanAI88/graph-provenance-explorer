"""Template renderer: verbatim citations, abstention, and the citation guard."""

from __future__ import annotations

import pytest

from graph_provenance_explorer.commands import open_session, query
from graph_provenance_explorer.renderer import ABSTAIN_TEXT, CitationError, LLMRenderer, TemplateRenderer
from graph_provenance_explorer.retrieval import Hit


def test_rendered_answer_quotes_passages_verbatim_with_citations(session):
    answer = query(session, "When is the Marlow Index recomputed?", "graph")
    assert not answer.abstained
    assert answer.citations
    for cid in answer.citations:
        assert f"[{cid}]" in answer.text
        assert session.corpus.get_passage(cid).text in answer.text


def test_every_displayed_source_resolves_for_every_fixture_question(session, questions):
    for q in questions:
        for mode in ("lexical", "graph", "vector"):
            answer = query(session, q.text, mode)
            for cid in answer.citations:
                assert cid in session.corpus.passage_ids, (q.id, mode, cid)


def test_abstention_triggers_on_off_corpus_query(session):
    answer = query(session, "zeppelin cartography pastry", "graph")
    assert answer.abstained
    assert answer.text == ABSTAIN_TEXT
    assert answer.citations == ()


def test_abstention_triggers_when_top_score_is_below_threshold(session):
    hits = session.retriever.retrieve("When is the Marlow Index recomputed?", "graph")
    strict = TemplateRenderer(threshold=hits[0].score + 1.0)
    assert strict.render("q", hits, session.corpus, "graph").abstained
    lenient = TemplateRenderer(threshold=hits[0].score)
    assert not lenient.render("q", hits, session.corpus, "graph").abstained


def test_renderer_refuses_citation_outside_corpus(session):
    fake = (Hit("DOC-Z9#p1", 99.0, 99.0, "seed", ()),)
    with pytest.raises(CitationError, match="DOC-Z9#p1"):
        TemplateRenderer(threshold=0.0).render("q", fake, session.corpus, "lexical")


def test_llm_renderer_is_a_protocol_with_no_implementation_in_package():
    import graph_provenance_explorer as pkg
    import importlib
    import pkgutil

    assert isinstance(TemplateRenderer(0.0), LLMRenderer)
    implementations = []
    for info in pkgutil.iter_modules(pkg.__path__):
        module = importlib.import_module(f"{pkg.__name__}.{info.name}")
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, type) and obj is not TemplateRenderer and obj is not LLMRenderer:
                if getattr(obj, "__module__", "").startswith(pkg.__name__) and hasattr(obj, "render") and not name.startswith("_"):
                    implementations.append(f"{module.__name__}.{name}")
    assert implementations == [], f"unexpected renderer implementations: {implementations}"


def test_deleting_a_passage_removes_its_support(corpus_copy):
    question = "What happens to a summary line with Kestrel score K0?"
    before = query(open_session(corpus_copy), question, "graph")
    assert "DOC-B1#p3" in before.citations
    doc = corpus_copy / "DOC-B1.md"
    text = doc.read_text(encoding="utf-8")
    doc.write_text(text[: text.index("[p3]")], encoding="utf-8")
    rel = corpus_copy / "relations.yaml"
    lines = [ln for ln in rel.read_text(encoding="utf-8").splitlines() if "DOC-B1#p3" not in ln]
    rel.write_text("\n".join(lines) + "\n", encoding="utf-8")
    reopened = open_session(corpus_copy)
    assert "DOC-B1#p3" not in reopened.corpus.passage_ids
    after = query(reopened, question, "graph")
    assert after.abstained or ("DOC-B1#p3" not in after.citations and after.citations)
    assert all(c in reopened.corpus.passage_ids for c in after.citations)
