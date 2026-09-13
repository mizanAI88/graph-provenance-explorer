"""CLI behaviour: exit codes, output files, failure paths, and the tools scripts."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from graph_provenance_explorer.__main__ import EXIT_MISSING_INPUT, EXIT_OK, main
from graph_provenance_explorer.config import DEFAULT_CONFIG, default_config_file, load_config
from graph_provenance_explorer.manifest import load_yaml, validate_manifest, validate_metrics

REPO = Path(__file__).resolve().parents[1]


def test_smoke_exits_zero_and_writes_validated_outputs(tmp_path, capsys):
    out = tmp_path / "smoke"
    assert main(["smoke", "--out", str(out)]) == EXIT_OK
    assert (out / "metrics.json").exists()
    validate_metrics(json.loads((out / "metrics.json").read_text(encoding="utf-8")))
    validate_manifest(load_yaml(out / "manifest.yaml"), expected_mode="smoke")
    assert "smoke ok" in capsys.readouterr().out


def test_smoke_with_missing_corpus_exits_two(tmp_path, capsys):
    assert main(["smoke", "--corpus", str(tmp_path / "nowhere"), "--out", str(tmp_path / "o")]) == EXIT_MISSING_INPUT
    assert "Corpus directory not found" in capsys.readouterr().err


def test_ingest_reports_counts(capsys):
    assert main(["ingest"]) == EXIT_OK
    out = capsys.readouterr().out
    assert "documents: 12" in out and "nodes:" in out and "edges:" in out


def test_query_prints_citations_and_paths(capsys):
    assert main(["query", "When is the Marlow Index recomputed?", "--mode", "graph", "--show-paths"]) == EXIT_OK
    out = capsys.readouterr().out
    assert "[DOC-A1#p2]" in out
    assert "Sources:" in out
    assert "-[" in out, "expected at least one path line"


def test_query_abstains_on_nonsense(capsys):
    assert main(["query", "zeppelin cartography pastry", "--mode", "lexical"]) == EXIT_OK
    assert "No supporting passage found in the approved corpus." in capsys.readouterr().out


def test_query_rejects_unknown_mode():
    with pytest.raises(SystemExit):
        main(["query", "x", "--mode", "hybrid"])


def test_evaluate_with_missing_questions_exits_two(tmp_path, capsys):
    code = main(["evaluate", "--questions", str(tmp_path / "none.jsonl"), "--out", str(tmp_path / "o")])
    assert code == EXIT_MISSING_INPUT
    assert "Questions file not found" in capsys.readouterr().err


def test_evaluate_single_mode_writes_only_that_mode(tmp_path):
    assert main(["evaluate", "--mode", "vector", "--out", str(tmp_path / "e")]) == EXIT_OK
    metrics = json.loads((tmp_path / "e" / "metrics.json").read_text(encoding="utf-8"))
    assert list(metrics) == ["vector"]


def test_export_graph_writes_layout_and_export(tmp_path):
    assert main(["export-graph", "--out", str(tmp_path)]) == EXIT_OK
    export = json.loads((tmp_path / "graph_export.json").read_text(encoding="utf-8"))
    layout = json.loads((tmp_path / "graph_layout.json").read_text(encoding="utf-8"))
    assert layout["seed"] == 7
    assert set(layout["positions"]) == {n["id"] for n in export["nodes"]}
    assert export["provenance"]["relations"] == ["authored-v1"]
    assert all("provenance" in e and "type" in e for e in export["edges"])


def test_export_graph_is_byte_identical_across_two_runs(tmp_path):
    assert main(["export-graph", "--out", str(tmp_path / "a")]) == EXIT_OK
    assert main(["export-graph", "--out", str(tmp_path / "b")]) == EXIT_OK
    assert (tmp_path / "a" / "graph_layout.json").read_bytes() == (tmp_path / "b" / "graph_layout.json").read_bytes()
    assert (tmp_path / "a" / "graph_export.json").read_bytes() == (tmp_path / "b" / "graph_export.json").read_bytes()


def test_committed_layout_matches_a_fresh_run(tmp_path):
    committed = REPO / "examples" / "output" / "graph_layout.json"
    assert committed.exists()
    assert main(["export-graph", "--out", str(tmp_path)]) == EXIT_OK
    committed_layout = json.loads(committed.read_text(encoding="utf-8"))
    fresh_layout = json.loads((tmp_path / "graph_layout.json").read_text(encoding="utf-8"))
    # Same seed and same node set are exact requirements; coordinates may differ
    # in the third decimal between numpy builds (spring layout arithmetic), so
    # they are compared with a tolerance rather than bit for bit.
    assert committed_layout["seed"] == fresh_layout["seed"]
    assert set(committed_layout["positions"]) == set(fresh_layout["positions"])
    for node, (x, y) in committed_layout["positions"].items():
        fx, fy = fresh_layout["positions"][node]
        assert abs(x - fx) < 0.02 and abs(y - fy) < 0.02, node


def test_demo_exits_zero_and_writes_answers_markdown(tmp_path):
    assert main(["demo", "--out", str(tmp_path)]) == EXIT_OK
    assert (tmp_path / "demo" / "answers.md").exists()
    assert (tmp_path / "demo" / "metrics.json").exists()
    assert (tmp_path / "graph_export.json").exists()
    validate_manifest(load_yaml(tmp_path / "demo" / "manifest.yaml"), expected_mode="demo")


def test_broken_config_exits_two(tmp_path, capsys):
    cfg = tmp_path / "bad.yaml"
    cfg.write_text("retrieval:\n  top_k: 0\n", encoding="utf-8")
    assert main(["ingest", "--config", str(cfg)]) == EXIT_MISSING_INPUT
    assert "top_k" in capsys.readouterr().err


def test_default_yaml_matches_code_defaults():
    assert load_config(default_config_file()) == DEFAULT_CONFIG


def test_module_entry_point_runs_as_subprocess():
    env = {**os.environ, "PYTHONPATH": str(REPO / "src")}
    proc = subprocess.run([sys.executable, "-m", "graph_provenance_explorer", "--version"], capture_output=True, text=True, cwd=REPO, env=env)
    assert proc.returncode == 0
    assert "0.1.0" in proc.stdout


def test_render_figure_is_deterministic(tmp_path):
    script = REPO / "tools" / "render_figure.py"
    a, b = tmp_path / "a.svg", tmp_path / "b.svg"
    for target in (a, b):
        proc = subprocess.run([sys.executable, str(script), "--out", str(target)], capture_output=True, text=True, cwd=REPO)
        assert proc.returncode == 0, proc.stderr
    assert a.read_bytes() == b.read_bytes()
    assert a.read_bytes() == (REPO / "docs" / "figures" / "graph_retrieval.svg").read_bytes()


def test_check_corpus_validates_committed_fixture():
    proc = subprocess.run([sys.executable, str(REPO / "tools" / "check_corpus.py"), "--no-write"], capture_output=True, text=True, cwd=REPO)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "ok: 12 documents" in proc.stdout

