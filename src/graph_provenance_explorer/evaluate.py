"""Question fixture loading and retrieval/abstention metrics."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Sequence

from .corpus import Corpus
from .renderer import Answer, TemplateRenderer
from .retrieval import Hit, Retriever, validate_hits


class QuestionError(ValueError):
    """Raised when the questions fixture is missing or malformed."""


@dataclass(frozen=True)
class Question:
    id: str
    text: str
    gold: tuple[str, ...]
    answerable: bool


def load_questions(path: str | Path, corpus: Corpus | None = None) -> tuple[Question, ...]:
    """Read a JSONL questions fixture; when ``corpus`` is given, gold ids must resolve."""
    p = Path(path)
    if not p.exists():
        raise QuestionError(f"Questions file not found: {p}. Expected examples/questions/v1.jsonl or --questions PATH")
    questions: list[Question] = []
    for lineno, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        try:
            raw = json.loads(line)
        except json.JSONDecodeError as exc:
            raise QuestionError(f"{p.name}:{lineno}: invalid JSON ({exc.msg})") from exc
        for key in ("id", "question", "gold", "answerable"):
            if key not in raw:
                raise QuestionError(f"{p.name}:{lineno}: missing field {key!r}")
        gold = tuple(str(g) for g in raw["gold"])
        answerable = bool(raw["answerable"])
        if answerable and not gold:
            raise QuestionError(f"{p.name}:{lineno}: answerable question {raw['id']} has no gold passages")
        if not answerable and gold:
            raise QuestionError(f"{p.name}:{lineno}: unanswerable question {raw['id']} must have empty gold")
        if corpus is not None:
            unknown = [g for g in gold if g not in corpus.passage_ids]
            if unknown:
                raise QuestionError(f"{p.name}:{lineno}: gold ids do not resolve in corpus: {unknown}")
        questions.append(Question(str(raw["id"]), str(raw["question"]), gold, answerable))
    if not questions:
        raise QuestionError(f"{p.name}: no questions found")
    ids = [q.id for q in questions]
    if len(set(ids)) != len(ids):
        raise QuestionError(f"{p.name}: duplicate question ids")
    return tuple(questions)


def recall_at_k(ranked: Sequence[str], gold: Sequence[str], k: int) -> float:
    gold_set = set(gold)
    if not gold_set:
        return 0.0
    return len(gold_set.intersection(ranked[:k])) / len(gold_set)


def reciprocal_rank(ranked: Sequence[str], gold: Sequence[str]) -> float:
    gold_set = set(gold)
    for i, pid in enumerate(ranked, start=1):
        if pid in gold_set:
            return 1.0 / i
    return 0.0


@dataclass(frozen=True)
class QuestionResult:
    question_id: str
    mode: str
    answerable: bool
    abstained: bool
    ranked: tuple[str, ...]
    citations: tuple[str, ...]
    paths: tuple[tuple[tuple[str, str, str], ...], ...]
    top_score: float | None


def _mean(values: Sequence[float]) -> float | None:
    return round(sum(values) / len(values), 6) if values else None


def evaluate_mode(
    retriever: Retriever,
    renderer: TemplateRenderer,
    questions: Sequence[Question],
    mode: str,
    k_values: Sequence[int] = (1, 3, 5),
) -> tuple[dict[str, Any], tuple[QuestionResult, ...]]:
    """Run every question in one mode; return metrics plus per-question results."""
    corpus = retriever.corpus
    max_k = max(k_values)
    results: list[QuestionResult] = []
    recalls: dict[int, list[float]] = {k: [] for k in k_values}
    rr: list[float] = []
    cited_total = 0
    cited_resolving = 0
    cited_unsupported = 0
    path_steps_total = 0
    path_steps_valid = 0
    abstain_unanswerable: list[float] = []
    abstain_answerable: list[float] = []
    for q in questions:
        hits: tuple[Hit, ...] = retriever.retrieve(q.text, mode, k=max_k)
        validate_hits(hits, corpus, retriever.graph)
        answer: Answer = renderer.render(q.text, hits, corpus, mode)
        ranked = tuple(h.passage_id for h in hits)
        for k in k_values:
            if q.answerable:
                recalls[k].append(recall_at_k(ranked, q.gold, k))
        if q.answerable:
            rr.append(reciprocal_rank(ranked, q.gold))
            abstain_answerable.append(1.0 if answer.abstained else 0.0)
        else:
            abstain_unanswerable.append(1.0 if answer.abstained else 0.0)
        for c in answer.citations:
            cited_total += 1
            cited_resolving += 1 if c in corpus.passage_ids else 0
            if q.answerable and c not in q.gold:
                cited_unsupported += 1
        for h in hits:
            for step in h.path:
                path_steps_total += 1
                path_steps_valid += 1 if retriever.graph.has_edge(step.source, step.target) else 0
        results.append(
            QuestionResult(
                q.id,
                mode,
                q.answerable,
                answer.abstained,
                ranked,
                answer.citations,
                tuple(tuple(s.as_tuple() for s in h.path) for h in hits),
                hits[0].score if hits else None,
            )
        )
    metrics: dict[str, Any] = {
        "mode": mode,
        "n_questions": len(questions),
        "n_answerable": sum(1 for q in questions if q.answerable),
        "n_unanswerable": sum(1 for q in questions if not q.answerable),
        "abstention_threshold": renderer.threshold,
        "mrr": _mean(rr),
        "citations_emitted": cited_total,
        "source_path_validity_rate": round(cited_resolving / cited_total, 6) if cited_total else None,
        "path_step_validity_rate": round(path_steps_valid / path_steps_total, 6) if path_steps_total else None,
        "unsupported_citation_rate": round(cited_unsupported / cited_total, 6) if cited_total else None,
        "abstention_accuracy_unanswerable": _mean(abstain_unanswerable),
        "false_abstention_rate_answerable": _mean(abstain_answerable),
    }
    for k in k_values:
        metrics[f"recall_at_{k}"] = _mean(recalls[k])
    return metrics, tuple(results)


def ranking_differences(results_a: Sequence[QuestionResult], results_b: Sequence[QuestionResult]) -> tuple[str, ...]:
    """Ids of questions whose ranked passage lists differ between two result sets."""
    by_id = {r.question_id: r.ranked for r in results_b}
    return tuple(r.question_id for r in results_a if by_id.get(r.question_id) != r.ranked)


def result_to_dict(result: QuestionResult) -> dict[str, Any]:
    return asdict(result)
