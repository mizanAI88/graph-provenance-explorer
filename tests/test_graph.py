"""Graph construction, typed nodes and edges, deterministic layout, explorer export."""

from __future__ import annotations

import json

from graph_provenance_explorer.corpus import EDGE_TYPES
from graph_provenance_explorer.graph import (
    NODE_TYPES,
    STRUCTURAL_EDGE_TYPE,
    STRUCTURAL_PROVENANCE,
    build_graph,
    compute_layout,
    export_graph,
    node_counts,
)


def test_graph_uses_only_the_five_node_types_and_all_of_them(corpus):
    graph = build_graph(corpus)
    types = {a["type"] for _, a in graph.nodes(data=True)}
    assert types == set(NODE_TYPES)
    counts = node_counts(graph)
    assert counts["document"] == 12
    assert counts["passage"] == len(corpus.passages)


def test_every_graph_edge_has_type_and_provenance(corpus):
    graph = build_graph(corpus)
    allowed = EDGE_TYPES | {STRUCTURAL_EDGE_TYPE}
    for u, v, attrs in graph.edges(data=True):
        assert attrs["type"] in allowed, (u, v)
        assert attrs["provenance"] in {"authored-v1", STRUCTURAL_PROVENANCE}, (u, v)


def test_structural_edges_link_each_document_to_its_passages(corpus):
    graph = build_graph(corpus)
    for doc in corpus.documents:
        for p in doc.passages:
            assert graph.edges[doc.id, p.id]["type"] == STRUCTURAL_EDGE_TYPE


def test_authored_edge_count_matches_relations(corpus):
    graph = build_graph(corpus)
    authored = [1 for _, _, a in graph.edges(data=True) if a["provenance"] == "authored-v1"]
    assert len(authored) == len(corpus.relations.edges)


def test_layout_is_deterministic_across_two_builds(corpus):
    a = compute_layout(build_graph(corpus), seed=7)
    b = compute_layout(build_graph(corpus), seed=7)
    assert a == b
    assert json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def test_layout_changes_with_seed(corpus):
    graph = build_graph(corpus)
    assert compute_layout(graph, seed=7) != compute_layout(graph, seed=8)


def test_export_contains_nodes_edges_layout_passages_provenance(corpus):
    graph = build_graph(corpus)
    layout = compute_layout(graph, seed=7)
    payload = export_graph(corpus, graph, layout)
    for key in ("nodes", "edges", "layout", "passages", "provenance", "counts"):
        assert key in payload
    assert len(payload["nodes"]) == graph.number_of_nodes()
    assert len(payload["edges"]) == graph.number_of_edges()
    assert set(payload["layout"]) == set(graph.nodes)
    assert set(payload["passages"]) == corpus.passage_ids
    assert payload["provenance"]["relations"] == ["authored-v1"]
    json.dumps(payload)


def test_export_node_coordinates_match_layout(corpus):
    graph = build_graph(corpus)
    layout = compute_layout(graph, seed=7)
    payload = export_graph(corpus, graph, layout)
    for node in payload["nodes"]:
        assert [node["x"], node["y"]] == payload["layout"][node["id"]]
