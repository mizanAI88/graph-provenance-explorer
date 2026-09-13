"""Run manifests (schema_version 1) and lightweight schema validation for outputs."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

import yaml

from . import PROJECT_ID

MANIFEST_MODES: tuple[str, ...] = ("smoke", "demo", "experiment")
MANIFEST_STATUSES: tuple[str, ...] = ("completed", "failed", "interrupted")
MANIFEST_REQUIRED: tuple[str, ...] = (
    "schema_version",
    "project_id",
    "run_id",
    "status",
    "mode",
    "git_commit",
    "data",
    "configuration_hash",
    "seed",
    "environment",
    "checkpoint_hash",
    "metrics_file",
    "predictions_file",
    "started_at",
    "finished_at",
)
METRICS_REQUIRED: tuple[str, ...] = (
    "mode",
    "n_questions",
    "n_answerable",
    "n_unanswerable",
    "recall_at_1",
    "recall_at_3",
    "recall_at_5",
    "mrr",
    "source_path_validity_rate",
    "unsupported_citation_rate",
    "abstention_accuracy_unanswerable",
)


class SchemaError(ValueError):
    """Raised when an output file does not match its expected schema."""


def sha256_file(path: str | Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def run_id(mode: str, when: datetime | None = None) -> str:
    stamp = (when or datetime.now(timezone.utc)).strftime("%Y%m%dT%H%M%SZ")
    return f"{stamp}-{PROJECT_ID}-{mode}"


def build_manifest(
    mode: str,
    status: str,
    data: Mapping[str, Any],
    configuration_hash: str,
    seed: int,
    metrics_file: str | None,
    predictions_file: str | None,
    started_at: str,
    finished_at: str,
) -> dict[str, Any]:
    if mode not in MANIFEST_MODES:
        raise SchemaError(f"manifest mode must be one of {MANIFEST_MODES}, got {mode!r}")
    if status not in MANIFEST_STATUSES:
        raise SchemaError(f"manifest status must be one of {MANIFEST_STATUSES}, got {status!r}")
    return {
        "schema_version": 1,
        "project_id": PROJECT_ID,
        "run_id": run_id(mode),
        "status": status,
        "mode": mode,
        "git_commit": None,
        "data": dict(data),
        "configuration_hash": configuration_hash,
        "seed": int(seed),
        "environment": {"lockfile_hash": None, "device": "cpu"},
        "checkpoint_hash": None,
        "metrics_file": metrics_file,
        "predictions_file": predictions_file,
        "started_at": started_at,
        "finished_at": finished_at,
    }


def write_manifest(path: str | Path, manifest: Mapping[str, Any]) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(yaml.safe_dump(dict(manifest), sort_keys=False), encoding="utf-8")
    return p


def validate_manifest(manifest: Mapping[str, Any], expected_mode: str | None = None) -> None:
    missing = [k for k in MANIFEST_REQUIRED if k not in manifest]
    if missing:
        raise SchemaError(f"manifest is missing fields {missing}")
    if manifest["schema_version"] != 1:
        raise SchemaError("manifest schema_version must be 1")
    if manifest["mode"] not in MANIFEST_MODES:
        raise SchemaError(f"manifest mode {manifest['mode']!r} is invalid")
    if expected_mode is not None and manifest["mode"] != expected_mode:
        raise SchemaError(f"manifest mode is {manifest['mode']!r}, expected {expected_mode!r}")
    if manifest["status"] not in MANIFEST_STATUSES:
        raise SchemaError(f"manifest status {manifest['status']!r} is invalid")
    data = manifest["data"]
    for key in ("source_id", "version", "split_manifest_hash", "sample_counts"):
        if key not in data:
            raise SchemaError(f"manifest.data is missing {key!r}")
    if not isinstance(data["split_manifest_hash"], str) or len(data["split_manifest_hash"]) != 64:
        raise SchemaError("manifest.data.split_manifest_hash must be a sha256 hex digest")


def validate_metrics(metrics: Mapping[str, Any]) -> None:
    """Metrics file: a mapping of mode name to a metrics block with the required keys."""
    if not isinstance(metrics, Mapping) or not metrics:
        raise SchemaError("metrics.json must be a non-empty mapping keyed by mode")
    for mode, block in metrics.items():
        if not isinstance(block, Mapping):
            raise SchemaError(f"metrics[{mode!r}] must be a mapping")
        missing = [k for k in METRICS_REQUIRED if k not in block]
        if missing:
            raise SchemaError(f"metrics[{mode!r}] is missing {missing}")
        for key in ("recall_at_1", "recall_at_3", "recall_at_5", "mrr", "source_path_validity_rate"):
            value = block[key]
            if value is not None and not (0.0 <= float(value) <= 1.0):
                raise SchemaError(f"metrics[{mode!r}].{key} out of range: {value}")


def load_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def load_yaml(path: str | Path) -> Any:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
