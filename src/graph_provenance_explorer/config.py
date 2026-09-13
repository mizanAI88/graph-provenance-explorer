"""Configuration defaults, YAML overlay, and repository path discovery."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

import yaml

from .corpus import EDGE_TYPES

DEFAULT_CONFIG: dict[str, Any] = {
    "seed": 42,
    "corpus": {"source_id": "synthetic-corpus-v1", "version": "v1"},
    "bm25": {"k1": 1.5, "b": 0.75},
    "vector": {"dims": 512},
    "retrieval": {
        "seed_k": 3,
        "top_k": 5,
        "hops": 1,
        "bridge_via": ["concept", "assertion", "source"],
        "edge_weights": {
            "supports": 1.0,
            "refines": 0.8,
            "defines": 0.6,
            "cites": 0.5,
            "contradicts": 0.4,
            "contains": 0.0,
        },
    },
    "abstention": {"lexical": 3.0, "graph": 3.0, "vector": 0.2},
    "layout": {"seed": 7, "iterations": 100},
    "evaluation": {"k_values": [1, 3, 5]},
}


class ConfigError(ValueError):
    """Raised when a configuration file cannot be used."""


def repo_root() -> Path:
    """Return the repository root that contains ``src/``, ``configs/`` and ``examples/``."""
    return Path(__file__).resolve().parents[2]


def default_corpus_dir() -> Path:
    return repo_root() / "examples" / "corpus" / "v1"


def default_questions_file() -> Path:
    return repo_root() / "examples" / "questions" / "v1.jsonl"


def default_output_dir() -> Path:
    return repo_root() / "examples" / "output"


def default_config_file() -> Path:
    return repo_root() / "configs" / "default.yaml"


def _deep_merge(base: Mapping[str, Any], overlay: Mapping[str, Any]) -> dict[str, Any]:
    merged = copy.deepcopy(dict(base))
    for key, value in overlay.items():
        if isinstance(value, Mapping) and isinstance(merged.get(key), Mapping):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = copy.deepcopy(value)
    return merged


def validate_config(config: Mapping[str, Any]) -> None:
    """Check the fields the retrieval code depends on; raise ConfigError with a usable message."""
    retrieval = config.get("retrieval", {})
    for key in ("seed_k", "top_k", "hops"):
        value = retrieval.get(key)
        if not isinstance(value, int) or value < 1:
            raise ConfigError(f"retrieval.{key} must be a positive integer, got {value!r}")
    weights = retrieval.get("edge_weights", {})
    missing = sorted(EDGE_TYPES - set(weights))
    if missing:
        raise ConfigError(f"retrieval.edge_weights is missing entries for {missing}")
    for name, value in weights.items():
        if not isinstance(value, (int, float)):
            raise ConfigError(f"retrieval.edge_weights.{name} must be numeric, got {value!r}")
    for mode in ("lexical", "graph", "vector"):
        if not isinstance(config.get("abstention", {}).get(mode), (int, float)):
            raise ConfigError(f"abstention.{mode} must be numeric")
    bm25 = config.get("bm25", {})
    if not (isinstance(bm25.get("k1"), (int, float)) and isinstance(bm25.get("b"), (int, float))):
        raise ConfigError("bm25.k1 and bm25.b must be numeric")


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    """Load defaults and overlay ``path`` (or ``configs/default.yaml`` when present)."""
    candidate = Path(path) if path is not None else default_config_file()
    config = copy.deepcopy(DEFAULT_CONFIG)
    if path is not None and not candidate.exists():
        raise ConfigError(f"Config file not found: {candidate}")
    if candidate.exists():
        loaded = yaml.safe_load(candidate.read_text(encoding="utf-8")) or {}
        if not isinstance(loaded, Mapping):
            raise ConfigError(f"{candidate}: top level must be a mapping")
        config = _deep_merge(config, loaded)
    validate_config(config)
    return config


def config_hash(config: Mapping[str, Any]) -> str:
    """Stable sha256 of the resolved configuration."""
    payload = json.dumps(config, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()
