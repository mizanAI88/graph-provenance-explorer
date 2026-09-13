"""Question fixture, metric arithmetic, and the evaluate/manifest pipeline."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from graph_provenance_explorer.commands import evaluate
from graph_provenance_explorer.config import config_hash
from graph_provenance_explorer.evaluate import (
    QuestionError,
    evaluate_mode,
    load_questions,
    ranking_differences,
    recall_at_k,
    reciprocal_rank,
)
from graph_provenance_explorer.manifest import SchemaError, load_yaml, validate_manifest, validate_metrics


def test_fixture_has_twenty_answerable_and_five_unanswerable(questions):
    assert sum(q.answerable for q in questions) == 20
    assert sum(not q.answerable for q in questions) == 5


def test_every_gold_id_resolves_in_corpus(questions, corpus):
    for q in questions:
        for g in q.gold:
            assert g in corpus.passage_ids, (q.id, g)


def test_recall_at_k_arithmetic():
    ranked = ["a", "b", "c", "d"]
    assert recall_at_k(ranked, ["a", "c"], 1) == 0.5
    assert recall_at_k(ranked, ["a", "c"], 3) == 1.0
    assert recall_at_k(ranked, ["z"], 5) == 0.0
    assert recall_at_k(ranked, [], 5) == 0.0


def test_reciprocal_rank_arithmetic():
    assert reciprocal_rank(["a", "b", "c"], ["c"]) == pytest.approx(1 / 3)
    assert reciprocal_rank(["a", "b", "c"], ["a", "c"]) == 1.0
    assert reciprocal_rank(["a"], ["z"]) == 0.0


def test_ranking_differences_detects_changed_lists():
    from graph_provenance_explorer.evaluate import QuestionResult

    a = [QuestionResult("Q1", "lexical", True, False, ("x", "y"), ("x", "y"), ((), ()), 1.0)]
    b_same = [QuestionResult("Q1", "graph", True, False, ("x", "y"), ("x", "y"), ((), ()), 1.0)]
    b_diff = [QuestionResult("Q1", "graph", True, False, ("y", "x"), ("y", "x"), ((), ()), 1.0)]
    assert ranking_differences(a, b_same) == ()
    assert ranking_differences(a, b_diff) == ("Q1",)


def test_evaluate_mode_produces_every_required_metric(session, questions):
    metrics, results = evaluate_mode(session.retriever, session.renderer("graph"), questions, "graph")
    for key in ("recall_at_1", "recall_at_3", "recall_at_5", "mrr", "source_path_validity_rate", "unsupported_citation_rate", "abstention_accuracy_unanswerable"):
        assert key in metrics
    assert metrics["source_path_validity_rate"] == 1.0
    assert metrics["path_step_validity_rate"] == 1.0
    assert len(results) == len(questions)
    assert 0.0 <= metrics["mrr"] <= 1.0


def test_source_path_validity_is_one_in_every_mode(session, questions):
    for mode in ("lexical", "graph", "vector"):
        metrics, _ = evaluate_mode(session.retriever, session.renderer(mode), questions, mode)
        assert metrics["source_path_validity_rate"] == 1.0, mode


def test_questions_file_missing_raises(tmp_path):
    with pytest.raises(QuestionError, match="not found"):
        load_questions(tmp_path / "missing.jsonl")


def test_questions_with_unresolvable_gold_raise(tmp_path, corpus):
    f = tmp_path / "q.jsonl"
    f.write_text(json.dumps({"id": "Q1", "question": "x", "gold": ["DOC-Z9#p1"], "answerable": True}) + "\n", encoding="utf-8")
    with pytest.raises(QuestionError, match="DOC-Z9#p1"):
        load_questions(f, corpus)


def test_unanswerable_question_with_gold_raises(tmp_path):
    f = tmp_path / "q.jsonl"
    f.write_text(json.dumps({"id": "U1", "question": "x", "gold": ["DOC-A1#p1"], "answerable": False}) + "\n", encoding="utf-8")
    with pytest.raises(QuestionError, match="must have empty gold"):
        load_questions(f)


def test_malformed_json_line_raises(tmp_path):
    f = tmp_path / "q.jsonl"
    f.write_text('{"id": "Q1", "question": ', encoding="utf-8")
    with pytest.raises(QuestionError, match="invalid JSON"):
        load_questions(f)


def test_evaluate_writes_metrics_answers_and_valid_manifest(session, tmp_path):
    result = evaluate(session, tmp_path / "eval", modes=("lexical", "graph"))
    metrics = json.loads(Path(result["metrics_file"]).read_text(encoding="utf-8"))
    validate_metrics(metrics)
    assert set(metrics) == {"lexical", "graph"}
    assert "questions_ranked_differently_from_lexical" in metrics["graph"]
    manifest = load_yaml(result["manifest_file"])
    validate_manifest(manifest, expected_mode="demo")
    assert manifest["project_id"] == "graph-provenance-explorer"
    assert manifest["configuration_hash"] == config_hash(session.config)
    assert manifest["data"]["sample_counts"]["test"] == 25
    assert manifest["git_commit"] is None
    lines = Path(result["answers_file"]).read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2 * 25


def test_manifest_validation_rejects_wrong_mode_and_missing_fields():
    good = {
        "schema_version": 1, "project_id": "x", "run_id": "r", "status": "completed", "mode": "demo",
        "git_commit": None, "data": {"source_id": "s", "version": "v1", "split_manifest_hash": "0" * 64, "sample_counts": {}},
        "configuration_hash": "h", "seed": 42, "environment": {}, "checkpoint_hash": None,
        "metrics_file": None, "predictions_file": None, "started_at": "t", "finished_at": "t",
    }
    validate_manifest(good, expected_mode="demo")
    with pytest.raises(SchemaError, match="expected 'smoke'"):
        validate_manifest(good, expected_mode="smoke")
    with pytest.raises(SchemaError, match="missing fields"):
        validate_manifest({k: v for k, v in good.items() if k != "seed"})
    with pytest.raises(SchemaError, match="sha256"):
        validate_manifest({**good, "data": {**good["data"], "split_manifest_hash": "short"}})


def test_metrics_validation_rejects_out_of_range_and_missing():
    block = {k: 0.5 for k in ("recall_at_1", "recall_at_3", "recall_at_5", "mrr", "source_path_validity_rate", "unsupported_citation_rate", "abstention_accuracy_unanswerable")}
    block.update({"mode": "graph", "n_questions": 1, "n_answerable": 1, "n_unanswerable": 0})
    validate_metrics({"graph": block})
    with pytest.raises(SchemaError, match="out of range"):
        validate_metrics({"graph": {**block, "mrr": 1.5}})
    with pytest.raises(SchemaError, match="missing"):
        validate_metrics({"graph": {k: v for k, v in block.items() if k != "mrr"}})
    with pytest.raises(SchemaError):
        validate_metrics({})
