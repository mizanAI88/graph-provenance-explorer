"""Deterministic answer rendering with abstention and a citation guard.

The default renderer is a template: it lists retrieved passages verbatim with
``[DOC-A1#p3]`` citations. It never emits an id that is not in the corpus; that
is enforced by ``CitationError`` in code, not by convention. ``LLMRenderer`` is a
Protocol only. No provider implementation is included in this repository.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence, runtime_checkable

from .corpus import Corpus
from .retrieval import Hit

ABSTAIN_TEXT = "No supporting passage found in the approved corpus."


class CitationError(RuntimeError):
    """Raised when a renderer would emit a citation that does not resolve in the corpus."""


@dataclass(frozen=True)
class Answer:
    question: str
    mode: str
    abstained: bool
    text: str
    citations: tuple[str, ...]
    hits: tuple[Hit, ...]


@runtime_checkable
class LLMRenderer(Protocol):
    """Interface an optional model-backed renderer would satisfy. Not implemented here."""

    def render(self, question: str, hits: Sequence[Hit], corpus: Corpus, mode: str) -> Answer: ...


def assert_citations_resolve(citations: Sequence[str], corpus: Corpus) -> None:
    """Guard shared by every renderer: every cited id must be a corpus passage."""
    known = corpus.passage_ids
    bad = [c for c in citations if c not in known]
    if bad:
        raise CitationError(f"Refusing to emit citations that do not resolve in the approved corpus: {bad}")


def format_path(hit: Hit) -> str:
    if not hit.path:
        return "direct lexical match"
    return " -> ".join(f"{s.source} -[{s.edge_type}]-> {s.target}" for s in hit.path)


class TemplateRenderer:
    """Verbatim, citation-linked rendering with score-threshold abstention."""

    def __init__(self, threshold: float) -> None:
        self.threshold = float(threshold)

    def render(self, question: str, hits: Sequence[Hit], corpus: Corpus, mode: str) -> Answer:
        ordered = tuple(hits)
        if not ordered or ordered[0].score < self.threshold:
            return Answer(question, mode, True, ABSTAIN_TEXT, (), ordered)
        citations = tuple(h.passage_id for h in ordered)
        assert_citations_resolve(citations, corpus)
        lines = [f"Question: {question}", f"Mode: {mode}", ""]
        for h in ordered:
            passage = corpus.get_passage(h.passage_id)
            lines.append(f"[{h.passage_id}] (score {h.score:.3f}; {format_path(h)})")
            lines.append(passage.text)
            lines.append("")
        lines.append("Sources: " + ", ".join(f"[{c}]" for c in citations))
        return Answer(question, mode, False, "\n".join(lines).rstrip(), citations, ordered)
