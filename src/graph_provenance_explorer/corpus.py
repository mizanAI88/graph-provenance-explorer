"""Load and validate the authored corpus: markdown documents plus relations.yaml.

Every structure here is immutable. Validation fails fast with ``CorpusError``
carrying a message that names the offending file or identifier.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterator, Mapping

import yaml

DOC_ID_RE = re.compile(r"^DOC-[A-Z]+\d+$")
PASSAGE_ID_RE = re.compile(r"^(DOC-[A-Z]+\d+)#p(\d+)$")
CONCEPT_ID_RE = re.compile(r"^CON-[A-Z0-9]+$")
ASSERTION_ID_RE = re.compile(r"^AST-\d+$")
SOURCE_ID_RE = re.compile(r"^SRC-\d+$")
PASSAGE_BLOCK_RE = re.compile(r"^\[p(\d+)\][ \t]*(.*?)(?=^\[p\d+\]|\Z)", re.MULTILINE | re.DOTALL)
FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", re.DOTALL)

EDGE_TYPES: frozenset[str] = frozenset({"supports", "cites", "defines", "contradicts", "refines"})
FICTION_MARKER = "Authored synthetic material"
RELATIONS_FILENAME = "relations.yaml"


class CorpusError(ValueError):
    """Raised when the corpus on disk violates the expected structure."""


@dataclass(frozen=True)
class Passage:
    """One addressable passage, identified as ``DOC-A1#p3``."""

    id: str
    doc_id: str
    index: int
    text: str


@dataclass(frozen=True)
class Document:
    """One markdown guidance note with its ordered passages."""

    id: str
    title: str
    path: str
    passages: tuple[Passage, ...]

    @property
    def word_count(self) -> int:
        return sum(len(p.text.split()) for p in self.passages)


@dataclass(frozen=True)
class Concept:
    id: str
    label: str


@dataclass(frozen=True)
class Assertion:
    id: str
    text: str


@dataclass(frozen=True)
class Source:
    id: str
    label: str


@dataclass(frozen=True)
class Edge:
    """A typed, provenance-carrying relation between two node identifiers."""

    source: str
    target: str
    type: str
    provenance: str


@dataclass(frozen=True)
class Relations:
    concepts: tuple[Concept, ...]
    assertions: tuple[Assertion, ...]
    sources: tuple[Source, ...]
    edges: tuple[Edge, ...]
    statement: str


@dataclass(frozen=True)
class Corpus:
    """The loaded corpus: documents in id order plus validated relations."""

    root: str
    documents: tuple[Document, ...]
    relations: Relations

    @property
    def passages(self) -> tuple[Passage, ...]:
        return tuple(p for d in self.documents for p in d.passages)

    @property
    def passage_ids(self) -> frozenset[str]:
        return frozenset(p.id for p in self.passages)

    @property
    def node_ids(self) -> frozenset[str]:
        rel = self.relations
        ids = set(self.passage_ids)
        ids.update(d.id for d in self.documents)
        ids.update(c.id for c in rel.concepts)
        ids.update(a.id for a in rel.assertions)
        ids.update(s.id for s in rel.sources)
        return frozenset(ids)

    def get_passage(self, passage_id: str) -> Passage:
        for p in self.passages:
            if p.id == passage_id:
                return p
        raise CorpusError(f"Unknown passage id {passage_id!r}; it does not resolve in the approved corpus")

    def without_passage(self, passage_id: str) -> "Corpus":
        """Return a new corpus with one passage and every edge touching it removed."""
        if passage_id not in self.passage_ids:
            raise CorpusError(f"Cannot remove {passage_id!r}: not in corpus")
        docs = tuple(
            Document(d.id, d.title, d.path, tuple(p for p in d.passages if p.id != passage_id))
            for d in self.documents
        )
        edges = tuple(e for e in self.relations.edges if passage_id not in (e.source, e.target))
        rel = Relations(self.relations.concepts, self.relations.assertions, self.relations.sources, edges, self.relations.statement)
        return Corpus(self.root, docs, rel)


def parse_document(path: Path) -> Document:
    """Parse one corpus markdown file into a Document, validating its shape."""
    raw = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(raw)
    if match is None:
        raise CorpusError(f"{path.name}: missing YAML front matter block")
    meta = yaml.safe_load(match.group(1)) or {}
    body = match.group(2)
    doc_id = str(meta.get("id", ""))
    if not DOC_ID_RE.match(doc_id):
        raise CorpusError(f"{path.name}: front matter id {doc_id!r} is not of the form DOC-A1")
    if path.stem != doc_id:
        raise CorpusError(f"{path.name}: filename does not match document id {doc_id!r}")
    title = str(meta.get("title", "")).strip()
    if not title:
        raise CorpusError(f"{path.name}: front matter has no title")
    if FICTION_MARKER not in body:
        raise CorpusError(f"{path.name}: body does not carry the required marker {FICTION_MARKER!r}")
    blocks = PASSAGE_BLOCK_RE.findall(body)
    if not blocks:
        raise CorpusError(f"{path.name}: no passages found; passages start with [p1], [p2], ...")
    passages = []
    for expected, (idx, text) in enumerate(blocks, start=1):
        if int(idx) != expected:
            raise CorpusError(f"{path.name}: passage numbering must be consecutive from p1; found p{idx} at position {expected}")
        clean = " ".join(text.split())
        if not clean:
            raise CorpusError(f"{path.name}: passage p{idx} is empty")
        passages.append(Passage(id=f"{doc_id}#p{expected}", doc_id=doc_id, index=expected, text=clean))
    return Document(id=doc_id, title=title, path=path.name, passages=tuple(passages))


def _require(mapping: Mapping[str, Any], key: str, where: str) -> Any:
    if key not in mapping or mapping[key] in (None, ""):
        raise CorpusError(f"{where}: missing required field {key!r}")
    return mapping[key]


def _parse_items(items: Any, where: str, id_re: re.Pattern[str], text_key: str) -> Iterator[tuple[str, str]]:
    for i, item in enumerate(items or []):
        if not isinstance(item, Mapping):
            raise CorpusError(f"{where}[{i}]: expected a mapping")
        item_id = str(_require(item, "id", f"{where}[{i}]"))
        if not id_re.match(item_id):
            raise CorpusError(f"{where}[{i}]: id {item_id!r} does not match the expected pattern")
        yield item_id, str(_require(item, text_key, f"{where}[{i}]"))


def parse_relations(path: Path, passage_ids: frozenset[str]) -> Relations:
    """Parse relations.yaml and validate every edge against known node ids."""
    if not path.exists():
        raise CorpusError(f"{path.name} not found in corpus root {path.parent}")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, Mapping):
        raise CorpusError(f"{path.name}: top level must be a mapping")
    statement = str(_require(data, "statement", path.name))
    if FICTION_MARKER not in statement:
        raise CorpusError(f"{path.name}: statement must contain {FICTION_MARKER!r}")
    concepts = tuple(Concept(i, t) for i, t in _parse_items(data.get("concepts"), "concepts", CONCEPT_ID_RE, "label"))
    assertions = tuple(Assertion(i, t) for i, t in _parse_items(data.get("assertions"), "assertions", ASSERTION_ID_RE, "text"))
    sources = tuple(Source(i, t) for i, t in _parse_items(data.get("sources"), "sources", SOURCE_ID_RE, "label"))
    known = set(passage_ids)
    for group in (concepts, assertions, sources):
        for item in group:
            if item.id in known:
                raise CorpusError(f"{path.name}: duplicate node id {item.id!r}")
            known.add(item.id)
    edges: list[Edge] = []
    seen: set[tuple[str, str, str]] = set()
    for i, raw in enumerate(data.get("edges") or []):
        where = f"{path.name} edges[{i}]"
        if not isinstance(raw, Mapping):
            raise CorpusError(f"{where}: expected a mapping")
        src = str(_require(raw, "source", where))
        dst = str(_require(raw, "target", where))
        etype = str(_require(raw, "type", where))
        prov = str(_require(raw, "provenance", where))
        if etype not in EDGE_TYPES:
            raise CorpusError(f"{where}: edge type {etype!r} is not one of {sorted(EDGE_TYPES)}")
        for endpoint in (src, dst):
            if endpoint not in known:
                raise CorpusError(f"{where}: endpoint {endpoint!r} does not resolve to any passage, concept, assertion or source")
        if src == dst:
            raise CorpusError(f"{where}: self-loop on {src!r}")
        key = (src, dst, etype)
        if key in seen:
            raise CorpusError(f"{where}: duplicate edge {key}")
        seen.add(key)
        edges.append(Edge(src, dst, etype, prov))
    return Relations(concepts, assertions, sources, tuple(edges), statement)


def load_corpus(root: str | Path) -> Corpus:
    """Load every ``DOC-*.md`` under ``root`` plus ``relations.yaml``."""
    root_path = Path(root)
    if not root_path.is_dir():
        raise CorpusError(f"Corpus directory not found: {root_path}. Pass --corpus pointing at a directory of DOC-*.md files plus relations.yaml")
    files = sorted(root_path.glob("DOC-*.md"))
    if not files:
        raise CorpusError(f"No DOC-*.md files found under {root_path}")
    documents = tuple(parse_document(f) for f in files)
    ids = [d.id for d in documents]
    if len(set(ids)) != len(ids):
        raise CorpusError("Duplicate document ids in corpus")
    passage_ids = frozenset(p.id for d in documents for p in d.passages)
    relations = parse_relations(root_path / RELATIONS_FILENAME, passage_ids)
    return Corpus(root=str(root_path), documents=documents, relations=relations)


def parse_passage_id(passage_id: str) -> tuple[str, int]:
    """Split ``DOC-A1#p3`` into ``("DOC-A1", 3)``; raise CorpusError otherwise."""
    match = PASSAGE_ID_RE.match(passage_id)
    if match is None:
        raise CorpusError(f"Invalid passage id {passage_id!r}; expected the form DOC-A1#p3")
    return match.group(1), int(match.group(2))
