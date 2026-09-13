"""Shared fixtures: the authored corpus, its graph, and a retriever session."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from graph_provenance_explorer.commands import Session, open_session
from graph_provenance_explorer.config import default_corpus_dir, default_questions_file, load_config
from graph_provenance_explorer.corpus import Corpus, load_corpus
from graph_provenance_explorer.evaluate import Question, load_questions

REPO = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def corpus_dir() -> Path:
    return default_corpus_dir()


@pytest.fixture(scope="session")
def corpus(corpus_dir: Path) -> Corpus:
    return load_corpus(corpus_dir)


@pytest.fixture(scope="session")
def config() -> dict:
    return load_config()


@pytest.fixture(scope="session")
def session() -> Session:
    return open_session()


@pytest.fixture(scope="session")
def questions(corpus: Corpus) -> tuple[Question, ...]:
    return load_questions(default_questions_file(), corpus)


@pytest.fixture()
def corpus_copy(tmp_path: Path, corpus_dir: Path) -> Path:
    """A writable copy of the corpus directory for mutation tests."""
    dst = tmp_path / "corpus"
    shutil.copytree(corpus_dir, dst)
    return dst
