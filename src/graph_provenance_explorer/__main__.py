"""Command line entry point: ``python -m graph_provenance_explorer <subcommand>``."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Sequence

from . import __version__, commands
from .config import ConfigError, default_output_dir, repo_root
from .corpus import CorpusError
from .evaluate import QuestionError
from .graph import GraphError
from .manifest import SchemaError
from .renderer import CitationError, format_path
from .retrieval import MODES, RetrievalError

EXIT_OK = 0
EXIT_FAILURE = 1
EXIT_MISSING_INPUT = 2


def _rel(path: str | Path) -> str:
    """Path relative to the repository root when inside it, else relative to the cwd, else as given."""
    p = Path(path).resolve()
    for base in (repo_root(), Path.cwd()):
        try:
            return p.relative_to(base).as_posix()
        except ValueError:
            continue
    return str(p)


def _add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--corpus", default=None, help="corpus directory (default: examples/corpus/v1)")
    parser.add_argument("--config", default=None, help="YAML config overlay (default: configs/default.yaml)")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="graph_provenance_explorer", description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("ingest", help="validate the corpus and report graph composition")
    _add_common(p)
    p.add_argument("--out", default=None, help="optional JSON file for the ingest summary")

    p = sub.add_parser("query", help="retrieve and render an answer for one question")
    _add_common(p)
    p.add_argument("question")
    p.add_argument("--mode", choices=MODES, default="graph")
    p.add_argument("--k", type=int, default=None)
    p.add_argument("--show-paths", action="store_true", help="print the traversal path of every hit")

    p = sub.add_parser("evaluate", help="run the question fixture and write metrics.json plus manifest")
    _add_common(p)
    p.add_argument("--questions", default=None, help="JSONL questions file (default: examples/questions/v1.jsonl)")
    p.add_argument("--mode", choices=(*MODES, "all"), default="all")
    p.add_argument("--out", default=None, help="output directory (default: examples/output/evaluate)")

    p = sub.add_parser("export-graph", help="write graph_export.json and graph_layout.json for the web explorer")
    _add_common(p)
    p.add_argument("--out", default=None, help="output directory (default: examples/output)")

    p = sub.add_parser("smoke", help="short offline check; exit 1 on any schema mismatch")
    _add_common(p)
    p.add_argument("--out", default=None)

    p = sub.add_parser("demo", help="documented demonstration on the authored fixture")
    _add_common(p)
    p.add_argument("--out", default=None)
    return parser


def _run(args: argparse.Namespace) -> int:
    session = commands.open_session(args.corpus, args.config)
    if args.command == "ingest":
        summary = commands.ingest(session, args.out)
        print(f"documents: {summary['documents']}  passages: {summary['passages']}")
        print(f"nodes: {summary['nodes_total']} {summary['nodes']}")
        print(f"edges: {summary['edges_total']} {summary['edges']}")
        if "written" in summary:
            print(f"written: {_rel(summary['written'])}")
        return EXIT_OK
    if args.command == "query":
        answer = commands.query(session, args.question, args.mode, args.k)
        print(answer.text)
        if args.show_paths and not answer.abstained:
            print("")
            for h in answer.hits:
                print(f"{h.passage_id}: {format_path(h)}")
        return EXIT_OK
    if args.command == "evaluate":
        modes: Sequence[str] = MODES if args.mode == "all" else (args.mode,)
        out = Path(args.out) if args.out else default_output_dir() / "evaluate"
        result = commands.evaluate(session, out, modes=modes, questions_file=args.questions)
        for line in commands.metrics_lines(result["metrics"]):
            print(line)
        print(f"metrics: {_rel(result['metrics_file'])}")
        print(f"manifest: {_rel(result['manifest_file'])}")
        return EXIT_OK
    if args.command == "export-graph":
        out = Path(args.out) if args.out else default_output_dir()
        result = commands.export(session, out)
        print(f"nodes: {result['nodes']} {result['node_counts']}")
        print(f"edges: {result['edges']} {result['edge_counts']}")
        print(f"export: {_rel(result['export_file'])}")
        print(f"layout: {_rel(result['layout_file'])}")
        return EXIT_OK
    if args.command == "smoke":
        result = commands.smoke(session, args.out)
        print(f"smoke ok: {result['ingest']['documents']} documents, {result['ingest']['nodes_total']} nodes, {result['ingest']['edges_total']} edges")
        print(f"probe citations: {result['probe_citations']}")
        print(f"metrics: {_rel(result['metrics_file'])}")
        print(f"manifest: {_rel(result['manifest_file'])}")
        return EXIT_OK
    if args.command == "demo":
        result = commands.demo(session, args.out)
        for line in commands.metrics_lines(result["metrics"]):
            print(line)
        print(f"metrics: {_rel(result['metrics_file'])}")
        print(f"answers: {_rel(result['answers_markdown'])}")
        print(f"manifest: {_rel(result['manifest_file'])}")
        print(f"graph export: {_rel(result['export']['export_file'])} ({result['export']['nodes']} nodes, {result['export']['edges']} edges)")
        print(f"layout: {_rel(result['export']['layout_file'])}")
        return EXIT_OK
    raise RuntimeError(f"unhandled command {args.command}")


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return _run(args)
    except (CorpusError, QuestionError, ConfigError) as exc:
        print(f"error (missing or invalid input): {exc}", file=sys.stderr)
        return EXIT_MISSING_INPUT
    except (GraphError, RetrievalError, CitationError, SchemaError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return EXIT_FAILURE


if __name__ == "__main__":
    sys.exit(main())
