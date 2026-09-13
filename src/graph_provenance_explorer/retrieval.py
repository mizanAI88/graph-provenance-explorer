"""Lexical, vector and graph-neighbourhood retrieval returning passages with their paths."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

import networkx as nx

from .corpus import Corpus
from .lexical import BM25Index
from .vector import HashedVectorIndex

MODES: tuple[str, ...] = ("lexical", "graph", "vector")


class RetrievalError(ValueError):
    """Raised for an unknown mode or an unusable request."""


@dataclass(frozen=True)
class PathStep:
    """One traversed edge, recorded in its stored direction."""

    source: str
    edge_type: str
    target: str

    def as_tuple(self) -> tuple[str, str, str]:
        return (self.source, self.edge_type, self.target)


@dataclass(frozen=True)
class Hit:
    """A retrieved passage with its score decomposition and the path that reached it."""

    passage_id: str
    score: float
    lexical_score: float
    origin: str
    path: tuple[PathStep, ...]

    @property
    def seed_id(self) -> str:
        return self.path[0].source if self.path else self.passage_id


class Retriever:
    """Holds the indexes for one corpus and answers queries in any of the three modes."""

    def __init__(self, corpus: Corpus, graph: nx.DiGraph, config: Mapping[str, Any]) -> None:
        self.corpus = corpus
        self.graph = graph
        self.config = config
        bm25 = config["bm25"]
        self.bm25 = BM25Index(corpus.passages, k1=bm25["k1"], b=bm25["b"])
        self.vectors = HashedVectorIndex(corpus.passages, dims=config["vector"]["dims"])
        self._passage_ids = corpus.passage_ids

    def retrieve(self, query: str, mode: str, k: int | None = None) -> tuple[Hit, ...]:
        if mode not in MODES:
            raise RetrievalError(f"Unknown retrieval mode {mode!r}; choose one of {MODES}")
        if not query or not query.strip():
            raise RetrievalError("Query is empty")
        top_k = int(k if k is not None else self.config["retrieval"]["top_k"])
        if top_k < 1:
            raise RetrievalError("k must be at least 1")
        if mode == "lexical":
            return self._flat(self.bm25.score_all(query), top_k)
        if mode == "vector":
            return self._flat(self.vectors.score_all(query), top_k)
        return self._graph(query, top_k)

    @staticmethod
    def _flat(scores: Mapping[str, float], top_k: int) -> tuple[Hit, ...]:
        ranked = sorted(((pid, s) for pid, s in scores.items() if s > 0.0), key=lambda x: (-x[1], x[0]))
        return tuple(Hit(pid, s, s, "seed", ()) for pid, s in ranked[:top_k])

    def _graph(self, query: str, top_k: int) -> tuple[Hit, ...]:
        rcfg = self.config["retrieval"]
        weights: Mapping[str, float] = rcfg["edge_weights"]
        bridge_via = set(rcfg.get("bridge_via", ()))
        lexical = self.bm25.score_all(query)
        seeds = self._flat(lexical, int(rcfg["seed_k"]))
        seed_ids = {s.passage_id for s in seeds}
        best: dict[str, Hit] = {s.passage_id: s for s in seeds}
        for seed in seeds:
            for steps, node in self._neighbourhood(seed.passage_id, int(rcfg["hops"]), bridge_via):
                if node == seed.passage_id or self.graph.nodes[node]["type"] != "passage":
                    continue
                bonus = sum(weights[st.edge_type] for st in steps) / len(steps)
                score = lexical.get(node, 0.0) + bonus
                origin = "seed" if node in seed_ids else "expanded"
                candidate = Hit(node, score, lexical.get(node, 0.0), origin, steps)
                current = best.get(node)
                if current is None or (candidate.score, -len(steps)) > (current.score, -len(current.path)):
                    best[node] = candidate
        ranked = sorted(best.values(), key=lambda h: (-h.score, h.passage_id))
        return tuple(ranked[:top_k])

    def _neighbourhood(self, start: str, hops: int, bridge_via: set[str]):
        """Yield (path, node) for every node within ``hops`` passage-level hops of ``start``.

        Crossing a non-passage node listed in ``bridge_via`` (concept, assertion,
        source) does not consume a hop: the bridge node is traversed and the next
        edge is followed in the same hop. Document nodes are never bridged.
        """
        frontier: list[tuple[tuple[PathStep, ...], str, int]] = [((), start, 0)]
        seen: set[str] = {start}
        while frontier:
            path, node, used = frontier.pop(0)
            if used >= hops:
                continue
            for step, nxt in self._adjacent(node):
                if nxt in seen:
                    continue
                new_path = path + (step,)
                ntype = self.graph.nodes[nxt]["type"]
                if ntype == "passage":
                    seen.add(nxt)
                    yield new_path, nxt
                    frontier.append((new_path, nxt, used + 1))
                elif ntype in bridge_via:
                    for step2, nxt2 in self._adjacent(nxt):
                        if nxt2 in seen or self.graph.nodes[nxt2]["type"] != "passage":
                            continue
                        seen.add(nxt2)
                        full = new_path + (step2,)
                        yield full, nxt2
                        frontier.append((full, nxt2, used + 1))

    def _adjacent(self, node: str):
        """Both edge directions, each reported in its stored direction."""
        for _, tgt, attrs in self.graph.out_edges(node, data=True):
            yield PathStep(node, attrs["type"], tgt), tgt
        for src, _, attrs in self.graph.in_edges(node, data=True):
            yield PathStep(src, attrs["type"], node), src


def validate_hits(hits: tuple[Hit, ...], corpus: Corpus, graph: nx.DiGraph) -> None:
    """Raise RetrievalError if any hit or any path step fails to resolve in corpus and graph."""
    for hit in hits:
        if hit.passage_id not in corpus.passage_ids:
            raise RetrievalError(f"Hit {hit.passage_id!r} does not resolve to a corpus passage")
        for step in hit.path:
            if not graph.has_edge(step.source, step.target):
                raise RetrievalError(f"Path step {step.as_tuple()} is not an edge in the graph")
            if graph.edges[step.source, step.target]["type"] != step.edge_type:
                raise RetrievalError(f"Path step {step.as_tuple()} reports the wrong edge type")
