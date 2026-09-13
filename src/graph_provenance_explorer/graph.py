"""Typed corpus graph (networkx), deterministic layout, and explorer export."""

from __future__ import annotations

from typing import Any

import networkx as nx

from .corpus import Corpus

NODE_TYPES: tuple[str, ...] = ("document", "passage", "concept", "assertion", "source")
STRUCTURAL_EDGE_TYPE = "contains"
STRUCTURAL_PROVENANCE = "ingest-structural-v1"


class GraphError(ValueError):
    """Raised when the graph cannot be built or a node does not resolve."""


def build_graph(corpus: Corpus) -> nx.DiGraph:
    """Build the typed directed graph. Nodes are inserted in sorted id order for determinism."""
    graph = nx.DiGraph()
    nodes: list[tuple[str, dict[str, Any]]] = []
    for doc in corpus.documents:
        nodes.append((doc.id, {"type": "document", "label": doc.title, "doc": doc.id}))
        for p in doc.passages:
            nodes.append((p.id, {"type": "passage", "label": p.id, "doc": doc.id, "index": p.index, "text": p.text}))
    rel = corpus.relations
    nodes.extend((c.id, {"type": "concept", "label": c.label}) for c in rel.concepts)
    nodes.extend((a.id, {"type": "assertion", "label": a.text}) for a in rel.assertions)
    nodes.extend((s.id, {"type": "source", "label": s.label}) for s in rel.sources)
    for node_id, attrs in sorted(nodes, key=lambda n: n[0]):
        graph.add_node(node_id, **attrs)
    for doc in corpus.documents:
        for p in doc.passages:
            graph.add_edge(doc.id, p.id, type=STRUCTURAL_EDGE_TYPE, provenance=STRUCTURAL_PROVENANCE)
    for e in sorted(rel.edges, key=lambda e: (e.source, e.target, e.type)):
        if e.source not in graph or e.target not in graph:
            raise GraphError(f"Edge {e.source} -> {e.target} references a node that is not in the graph")
        graph.add_edge(e.source, e.target, type=e.type, provenance=e.provenance)
    return graph


def node_counts(graph: nx.DiGraph) -> dict[str, int]:
    counts = {t: 0 for t in NODE_TYPES}
    for _, attrs in graph.nodes(data=True):
        counts[attrs["type"]] += 1
    return counts


def edge_counts(graph: nx.DiGraph) -> dict[str, int]:
    counts: dict[str, int] = {}
    for _, _, attrs in graph.edges(data=True):
        counts[attrs["type"]] = counts.get(attrs["type"], 0) + 1
    return dict(sorted(counts.items()))


def compute_layout(graph: nx.DiGraph, seed: int = 7, iterations: int = 100) -> dict[str, tuple[float, float]]:
    """Spring layout with a fixed seed; coordinates rounded so two runs serialise identically."""
    positions = nx.spring_layout(graph, seed=seed, iterations=iterations)
    return {node: (round(float(x), 6), round(float(y), 6)) for node, (x, y) in sorted(positions.items())}


def export_graph(corpus: Corpus, graph: nx.DiGraph, layout: dict[str, tuple[float, float]]) -> dict[str, Any]:
    """JSON-ready explorer payload: nodes, edges, layout, passages and provenance."""
    nodes = [
        {
            "id": n,
            "type": a["type"],
            "label": a["label"],
            "doc": a.get("doc"),
            "x": layout[n][0],
            "y": layout[n][1],
        }
        for n, a in graph.nodes(data=True)
    ]
    edges = [
        {"source": u, "target": v, "type": a["type"], "provenance": a["provenance"]}
        for u, v, a in graph.edges(data=True)
    ]
    passages = {
        p.id: {"doc": p.doc_id, "index": p.index, "text": p.text}
        for p in corpus.passages
    }
    return {
        "schema_version": 1,
        "corpus": {
            "root": "examples/corpus/v1",
            "statement": corpus.relations.statement,
            "documents": [{"id": d.id, "title": d.title, "file": d.path} for d in corpus.documents],
        },
        "node_types": list(NODE_TYPES),
        "edge_types": sorted({e["type"] for e in edges}),
        "nodes": nodes,
        "edges": edges,
        "layout": {n: [x, y] for n, (x, y) in layout.items()},
        "passages": passages,
        "provenance": {
            "relations": sorted({e.provenance for e in corpus.relations.edges}),
            "structural": STRUCTURAL_PROVENANCE,
        },
        "counts": {"nodes": node_counts(graph), "edges": edge_counts(graph)},
    }
