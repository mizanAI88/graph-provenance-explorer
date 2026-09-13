"""In-repo BM25 over passages. No external ranking dependency."""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from typing import Sequence

from .corpus import Passage

TOKEN_RE = re.compile(r"[a-z0-9]+")
STOPWORDS: frozenset[str] = frozenset(
    (
        "a an and are as at be by for from has have in is it its of on or that the this to was were with "
        "what which who whom when where why how does do did may can could would should many much "
        "not there their they them any all if then than into onto"
    ).split()
)


def tokenize(text: str) -> list[str]:
    """Lowercase alphanumeric tokens with a short stopword list removed."""
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS]


@dataclass(frozen=True)
class ScoredPassage:
    passage_id: str
    score: float


class BM25Index:
    """Okapi BM25 with the non-negative idf variant ``log(1 + (N - n + 0.5) / (n + 0.5))``."""

    def __init__(self, passages: Sequence[Passage], k1: float = 1.5, b: float = 0.75) -> None:
        if not passages:
            raise ValueError("BM25Index needs at least one passage")
        self.k1 = float(k1)
        self.b = float(b)
        self._ids = tuple(p.id for p in passages)
        self._tf = tuple(Counter(tokenize(p.text)) for p in passages)
        self._len = tuple(sum(tf.values()) for tf in self._tf)
        self._avg_len = sum(self._len) / len(self._len)
        df: Counter[str] = Counter()
        for tf in self._tf:
            df.update(tf.keys())
        n_docs = len(self._tf)
        self._idf = {term: math.log(1.0 + (n_docs - n + 0.5) / (n + 0.5)) for term, n in df.items()}

    @property
    def passage_ids(self) -> tuple[str, ...]:
        return self._ids

    def score_all(self, query: str) -> dict[str, float]:
        """Return BM25 scores for every passage, including zeros."""
        terms = tokenize(query)
        scores: dict[str, float] = {}
        for pid, tf, length in zip(self._ids, self._tf, self._len):
            total = 0.0
            norm = self.k1 * (1.0 - self.b + self.b * length / self._avg_len)
            for term in terms:
                freq = tf.get(term, 0)
                if freq == 0:
                    continue
                total += self._idf[term] * freq * (self.k1 + 1.0) / (freq + norm)
            scores[pid] = total
        return scores

    def search(self, query: str, k: int) -> tuple[ScoredPassage, ...]:
        """Top-k passages with a positive score, ties broken by passage id."""
        scores = self.score_all(query)
        ranked = sorted(((pid, s) for pid, s in scores.items() if s > 0.0), key=lambda x: (-x[1], x[0]))
        return tuple(ScoredPassage(pid, s) for pid, s in ranked[:k])
