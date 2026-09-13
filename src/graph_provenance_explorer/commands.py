"""Command implementations. Each returns a result mapping; the CLI does the printing."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from . import PROJECT_ID
from .config import config_hash, default_corpus_dir, default_output_dir, default_questions_file, load_config
from .corpus import Corpus, load_corpus
from .evaluate import Question, evaluate_mode, load_questions, ranking_differences, result_to_dict
from .graph import build_graph, compute_layout, edge_counts, export_graph, node_counts
from .manifest import build_manifest, load_json, load_yaml, now_iso, sha256_file, validate_manifest, validate_metrics, write_manifest
from .renderer import Answer, TemplateRenderer
from .retrieval import MODES, Retriever


@dataclass(frozen=True)
class Session:
    """Everything a command needs: corpus, graph, retriever, resolved config."""

    corpus: Corpus
    graph: Any
    retriever: Retriever
    config: dict[str, Any]
    corpus_dir: Path

    def renderer(self, mode: str) -> TemplateRenderer:
        return TemplateRenderer(threshold=float(self.config["abstention"][mode]))


def open_session(corpus_dir: str | Path | None = None, config_path: str | Path | None = None) -> Session:
    """Load config and corpus, build graph and indexes. Raises on any structural problem."""
    config = load_config(config_path)
    cdir = Path(corpus_dir) if corpus_dir is not None else default_corpus_dir()
    corpus = load_corpus(cdir)
    graph = build_graph(corpus)
    return Session(corpus, graph, Retriever(corpus, graph, config), config, cdir)


def ingest(session: Session, out_file: str | Path | None = None) -> dict[str, Any]:
    """Validate the corpus and report graph composition; optionally write the summary as JSON."""
    summary = {
        "project_id": PROJECT_ID,
        "corpus_dir": "examples/corpus/v1" if session.corpus_dir == default_corpus_dir() else str(session.corpus_dir.name),
        "documents": len(session.corpus.documents),
        "passages": len(session.corpus.passages),
        "word_counts": {d.id: d.word_count for d in session.corpus.documents},
        "nodes": node_counts(session.graph),
        "nodes_total": session.graph.number_of_nodes(),
        "edges": edge_counts(session.graph),
        "edges_total": session.graph.number_of_edges(),
        "relations_provenance": sorted({e.provenance for e in session.corpus.relations.edges}),
    }
    if out_file is not None:
        p = Path(out_file)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        summary["written"] = str(p)
    return summary


def query(session: Session, question: str, mode: str, k: int | None = None) -> Answer:
    hits = session.retriever.retrieve(question, mode, k=k)
    return session.renderer(mode).render(question, hits, session.corpus, mode)


def _data_block(session: Session, questions_file: Path, questions: Sequence[Question]) -> dict[str, Any]:
    n_ans = sum(1 for q in questions if q.answerable)
    return {
        "source_id": session.config["corpus"]["source_id"],
        "version": session.config["corpus"]["version"],
        "split_manifest_hash": sha256_file(questions_file),
        "sample_counts": {"train": 0, "val": 0, "test": len(questions)},
        "questions": {"answerable": n_ans, "unanswerable": len(questions) - n_ans},
        "relations_hash": sha256_file(session.corpus_dir / "relations.yaml"),
        "documents": len(session.corpus.documents),
        "passages": len(session.corpus.passages),
    }


def evaluate(
    session: Session,
    out_dir: str | Path,
    modes: Sequence[str] = MODES,
    questions_file: str | Path | None = None,
    manifest_mode: str = "demo",
) -> dict[str, Any]:
    """Evaluate the requested modes; write metrics.json, answers.jsonl and manifest.yaml."""
    started = now_iso()
    qfile = Path(questions_file) if questions_file is not None else default_questions_file()
    questions = load_questions(qfile, session.corpus)
    for mode in modes:
        if mode not in MODES:
            raise ValueError(f"Unknown mode {mode!r}; choose from {MODES}")
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    k_values = tuple(int(k) for k in session.config["evaluation"]["k_values"])
    metrics: dict[str, Any] = {}
    per_mode_results: dict[str, Any] = {}
    for mode in modes:
        block, results = evaluate_mode(session.retriever, session.renderer(mode), questions, mode, k_values)
        metrics[mode] = block
        per_mode_results[mode] = results
    if "lexical" in per_mode_results and "graph" in per_mode_results:
        diffs = ranking_differences(per_mode_results["lexical"], per_mode_results["graph"])
        metrics["graph"]["questions_ranked_differently_from_lexical"] = list(diffs)
    metrics_path = out / "metrics.json"
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    answers_path = out / "answers.jsonl"
    with answers_path.open("w", encoding="utf-8") as fh:
        for mode in modes:
            for r in per_mode_results[mode]:
                fh.write(json.dumps(result_to_dict(r)) + "\n")
    manifest = build_manifest(
        manifest_mode,
        "completed",
        _data_block(session, qfile, questions),
        config_hash(session.config),
        int(session.config["seed"]),
        metrics_path.name,
        answers_path.name,
        started,
        now_iso(),
    )
    manifest_path = write_manifest(out / "manifest.yaml", manifest)
    return {
        "metrics": metrics,
        "metrics_file": str(metrics_path),
        "answers_file": str(answers_path),
        "manifest_file": str(manifest_path),
        "n_questions": len(questions),
    }


def export(session: Session, out_dir: str | Path) -> dict[str, Any]:
    """Write graph_export.json (nodes, edges, layout, passages, provenance) and graph_layout.json."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    lcfg = session.config["layout"]
    layout = compute_layout(session.graph, seed=int(lcfg["seed"]), iterations=int(lcfg["iterations"]))
    payload = export_graph(session.corpus, session.graph, layout)
    export_path = out / "graph_export.json"
    layout_path = out / "graph_layout.json"
    export_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    layout_path.write_text(
        json.dumps({"schema_version": 1, "layout": "spring", "seed": int(lcfg["seed"]), "positions": payload["layout"]}, indent=2),
        encoding="utf-8",
    )
    return {
        "export_file": str(export_path),
        "layout_file": str(layout_path),
        "nodes": len(payload["nodes"]),
        "edges": len(payload["edges"]),
        "node_counts": payload["counts"]["nodes"],
        "edge_counts": payload["counts"]["edges"],
    }


def smoke(session: Session, out_dir: str | Path | None = None) -> dict[str, Any]:
    """Short offline path: ingest, one query, graph-mode evaluation, schema validation of outputs."""
    out = Path(out_dir) if out_dir is not None else default_output_dir() / "smoke"
    summary = ingest(session)
    if summary["documents"] < 1:
        raise RuntimeError("smoke: corpus has no documents")
    probe = query(session, "How is the Marlow Index recomputed?", "graph")
    if probe.abstained:
        raise RuntimeError("smoke: the probe question abstained; retrieval or corpus is broken")
    result = evaluate(session, out, modes=("graph",), manifest_mode="smoke")
    metrics = load_json(result["metrics_file"])
    validate_metrics(metrics)
    manifest = load_yaml(result["manifest_file"])
    validate_manifest(manifest, expected_mode="smoke")
    for key in ("metrics_file", "answers_file", "manifest_file"):
        if not Path(result[key]).exists():
            raise RuntimeError(f"smoke: expected output missing: {result[key]}")
    return {
        "ingest": summary,
        "probe_citations": list(probe.citations),
        "metrics_file": result["metrics_file"],
        "manifest_file": result["manifest_file"],
        "graph_metrics": metrics["graph"],
    }


def _answers_markdown(session: Session, questions: Sequence[Question], modes: Sequence[str]) -> str:
    lines = [
        "# Demo answers (authored synthetic corpus v1)",
        "",
        "Rendered by the deterministic TemplateRenderer. Every citation resolves to",
        "examples/corpus/v1. Scores are BM25 or BM25 plus edge-weight bonuses on this",
        "fixture and are not benchmark results.",
        "",
    ]
    for q in questions:
        lines.append(f"## {q.id}: {q.text}")
        lines.append("")
        lines.append(f"Answerable: {q.answerable}. Gold: {', '.join(q.gold) if q.gold else 'none'}")
        lines.append("")
        for mode in modes:
            ans = query(session, q.text, mode)
            lines.append(f"### mode={mode}")
            lines.append("")
            lines.append("```")
            lines.append(ans.text)
            lines.append("```")
            lines.append("")
    return "\n".join(lines)


def demo(session: Session, out_dir: str | Path | None = None) -> dict[str, Any]:
    """Full demonstration: all modes evaluated, answers rendered, graph exported."""
    out = Path(out_dir) if out_dir is not None else default_output_dir()
    demo_dir = out / "demo"
    result = evaluate(session, demo_dir, modes=MODES, manifest_mode="demo")
    questions = load_questions(default_questions_file(), session.corpus)
    answers_md = demo_dir / "answers.md"
    answers_md.write_text(_answers_markdown(session, questions, MODES), encoding="utf-8")
    exported = export(session, out)
    ingest_summary = ingest(session, demo_dir / "ingest_summary.json")
    return {
        **result,
        "answers_markdown": str(answers_md),
        "ingest_summary": ingest_summary,
        "export": exported,
    }


def metrics_lines(metrics: Mapping[str, Any]) -> list[str]:
    """Flat, printable lines for a metrics mapping."""
    lines: list[str] = []
    for mode, block in metrics.items():
        lines.append(f"[{mode}]")
        for key, value in block.items():
            lines.append(f"  {key}: {value}")
    return lines
