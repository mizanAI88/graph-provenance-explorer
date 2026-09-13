"""Optional vector baseline: hashed bag-of-words cosine similarity, no external model."""

from __future__ import annotations

import hashlib
from typing import Sequence

import numpy as np

from .corpus import Passage
from .lexical import ScoredPassage, tokenize


def _bucket(token: str, dims: int) -> int:
    digest = hashlib.sha1(token.encode("utf-8")).digest()
    return int.from_bytes(digest[:4], "big") % dims


def embed(text: str, dims: int) -> np.ndarray:
    """L2-normalised hashed term-count vector; the zero vector for empty text."""
    vec = np.zeros(dims, dtype=np.float64)
    for token in tokenize(text):
        vec[_bucket(token, dims)] += 1.0
    norm = float(np.linalg.norm(vec))
    return vec / norm if norm > 0 else vec


class HashedVectorIndex:
    """Cosine similarity over hashed bag-of-words passage vectors."""

    def __init__(self, passages: Sequence[Passage], dims: int = 512) -> None:
        if dims < 8:
            raise ValueError("vector.dims must be at least 8")
        if not passages:
            raise ValueError("HashedVectorIndex needs at least one passage")
        self.dims = int(dims)
        self._ids = tuple(p.id for p in passages)
        self._matrix = np.stack([embed(p.text, self.dims) for p in passages])

    def score_all(self, query: str) -> dict[str, float]:
        q = embed(query, self.dims)
        sims = self._matrix @ q
        return {pid: float(s) for pid, s in zip(self._ids, sims)}

    def search(self, query: str, k: int) -> tuple[ScoredPassage, ...]:
        scores = self.score_all(query)
        ranked = sorted(((pid, s) for pid, s in scores.items() if s > 0.0), key=lambda x: (-x[1], x[0]))
        return tuple(ScoredPassage(pid, s) for pid, s in ranked[:k])
