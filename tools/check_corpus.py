"""Validate the authored corpus and (re)write its FIXTURE.md label from computed facts.

The corpus is hand-authored prose, so there is no generator script and no seed.
This tool is the fixture's validator: it loads the corpus through the same code
the package uses, checks the word budget and the fiction marker on every file,
and writes examples/corpus/v1/FIXTURE.md with counts it computed itself.

Usage: python tools/check_corpus.py [--corpus examples/corpus/v1] [--min-words 150] [--max-words 300]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from graph_provenance_explorer.corpus import FICTION_MARKER, load_corpus  # noqa: E402
from graph_provenance_explorer.graph import build_graph, edge_counts, node_counts  # noqa: E402

FORBIDDEN_TERMS = ("mg", "dose", "dosage", "patient record", "diagnosis", "prescri")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", default=str(ROOT / "examples" / "corpus" / "v1"))
    parser.add_argument("--min-words", type=int, default=150)
    parser.add_argument("--max-words", type=int, default=300)
    parser.add_argument("--no-write", action="store_true", help="validate only; do not rewrite FIXTURE.md")
    args = parser.parse_args(argv)
    corpus = load_corpus(args.corpus)
    problems: list[str] = []
    for doc in corpus.documents:
        if not (args.min_words <= doc.word_count <= args.max_words):
            problems.append(f"{doc.id}: {doc.word_count} words outside [{args.min_words}, {args.max_words}]")
        text = (Path(args.corpus) / doc.path).read_text(encoding="utf-8")
        if FICTION_MARKER not in text:
            problems.append(f"{doc.id}: missing fiction marker")
        lowered = " ".join(p.text.lower() for p in doc.passages)
        for term in FORBIDDEN_TERMS:
            if f" {term}" in f" {lowered}":
                problems.append(f"{doc.id}: contains forbidden term {term!r}")
    if problems:
        for line in problems:
            print(f"PROBLEM {line}")
        return 1
    graph = build_graph(corpus)
    lines = [
        "# FIXTURE",
        "",
        "Authored synthetic demonstration data. Fictional identifiers. Not derived from",
        "any patient, dataset, or person. Hand-authored prose (no generator script, no",
        "seed); validated by `tools/check_corpus.py`, fixture version `v1`.",
        "",
        "Every document names an invented workflow term (Marlow Index, Kestrel score,",
        "Thornbury ladder, Osprey window, Brindle flag, Quillon handoff, Sable",
        "checkpoint, Wren ledger, Ferris loop, Lantern review, Corvid audit, Halden",
        "tier). None of them exists outside this repository. The text contains no real",
        "drug names, no real guidelines, and no disease-specific advice.",
        "",
        "## Counts (computed by tools/check_corpus.py)",
        "",
        f"- Documents: {len(corpus.documents)}",
        f"- Passages: {len(corpus.passages)}",
        f"- Word budget per document: {args.min_words} to {args.max_words}",
        f"- Relations in relations.yaml: {len(corpus.relations.edges)}",
        f"- Graph nodes after ingestion: {graph.number_of_nodes()} {node_counts(graph)}",
        f"- Graph edges after ingestion: {graph.number_of_edges()} {edge_counts(graph)}",
        "",
        "| Document | Title | Words | Passages |",
        "|---|---|---|---|",
    ]
    lines += [f"| {d.id} | {d.title} | {d.word_count} | {len(d.passages)} |" for d in corpus.documents]
    lines.append("")
    if not args.no_write:
        (Path(args.corpus) / "FIXTURE.md").write_text("\n".join(lines), encoding="utf-8")
        print("wrote FIXTURE.md")
    print(f"ok: {len(corpus.documents)} documents, {len(corpus.passages)} passages, {len(corpus.relations.edges)} relations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
