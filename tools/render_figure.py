"""Render docs/figures/graph_retrieval.svg by hand-written SVG (no plotting dependency).

The figure shows the retrieval path: question -> BM25 seeds -> one-hop typed
expansion -> rerank -> template renderer with citations or abstention.
White background, black labels. Deterministic output: running twice yields
byte-identical files.

Usage: python tools/render_figure.py [--out docs/figures/graph_retrieval.svg]
"""

from __future__ import annotations

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

WIDTH = 960
HEIGHT = 420
FONT = "font-family='Helvetica, Arial, sans-serif'"


def box(x: int, y: int, w: int, h: int, lines: list[str], dashed: bool = False) -> list[str]:
    dash = " stroke-dasharray='6,4'" if dashed else ""
    out = [f"<rect x='{x}' y='{y}' width='{w}' height='{h}' rx='6' fill='white' stroke='black' stroke-width='1.5'{dash}/>"]
    line_h = 16
    start = y + h / 2 - (len(lines) - 1) * line_h / 2 + 5
    for i, text in enumerate(lines):
        weight = " font-weight='bold'" if i == 0 else ""
        size = 13 if i == 0 else 11
        out.append(
            f"<text x='{x + w / 2:.1f}' y='{start + i * line_h:.1f}' text-anchor='middle' font-size='{size}'{weight} {FONT} fill='black'>{escape(text)}</text>"
        )
    return out


def arrow(x1: float, y1: float, x2: float, y2: float, label: str = "") -> list[str]:
    out = [f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='black' stroke-width='1.5' marker-end='url(#arrow)'/>"]
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 6
        out.append(f"<text x='{mx:.1f}' y='{my:.1f}' text-anchor='middle' font-size='10' {FONT} fill='black'>{escape(label)}</text>")
    return out


def render() -> str:
    parts = [
        f"<svg xmlns='http://www.w3.org/2000/svg' width='{WIDTH}' height='{HEIGHT}' viewBox='0 0 {WIDTH} {HEIGHT}'>",
        "<defs><marker id='arrow' markerWidth='10' markerHeight='10' refX='9' refY='3' orient='auto' markerUnits='strokeWidth'>"
        "<path d='M0,0 L0,6 L9,3 z' fill='black'/></marker></defs>",
        f"<rect x='0' y='0' width='{WIDTH}' height='{HEIGHT}' fill='white'/>",
        f"<text x='{WIDTH / 2}' y='28' text-anchor='middle' font-size='16' font-weight='bold' {FONT} fill='black'>"
        "graph-provenance-explorer: graph-neighbourhood retrieval with source paths</text>",
    ]
    # Stage boxes along the top row
    parts += box(20, 60, 150, 70, ["Question", "free text"])
    parts += box(210, 60, 170, 70, ["BM25 seeds", "top seed_k passages", "in-repo lexical index"])
    parts += box(420, 60, 190, 70, ["1-hop expansion", "typed edges: supports,", "refines, defines, cites, contradicts"])
    parts += box(650, 60, 140, 70, ["Rerank", "lexical + mean", "edge weight"])
    parts += box(830, 60, 110, 70, ["Renderer", "template"])
    parts += arrow(170, 95, 208, 95)
    parts += arrow(380, 95, 418, 95)
    parts += arrow(610, 95, 648, 95)
    parts += arrow(790, 95, 828, 95)
    # Graph example in the lower left
    parts.append(f"<text x='20' y='175' font-size='13' font-weight='bold' {FONT} fill='black'>Example neighbourhood (authored synthetic corpus v1)</text>")
    parts += box(40, 200, 130, 46, ["DOC-A1#p2", "seed, lexical"])
    parts += box(260, 200, 130, 46, ["DOC-D1#p2", "expanded"])
    parts += box(260, 300, 130, 46, ["CON-MARLOW", "concept (bridge)"], dashed=True)
    parts += box(40, 300, 130, 46, ["DOC-A1#p1", "seed, lexical"])
    parts += box(480, 300, 130, 46, ["DOC-L1#p3", "expanded via concept"])
    parts += arrow(170, 223, 258, 223, "refines")
    parts += arrow(170, 323, 258, 323, "defines")
    parts += arrow(390, 323, 478, 323, "refines")
    parts.append(f"<text x='40' y='385' font-size='11' {FONT} fill='black'>Path recorded for DOC-L1#p3: (DOC-A1#p1, defines, CON-MARLOW), (DOC-L1#p3, refines, DOC-A1#p1); each step is an edge of the graph.</text>")
    # Renderer outcomes in the lower right
    parts += box(660, 190, 280, 60, ["Answer", "verbatim passages with [DOC-A1#p2] citations", "every id asserted to resolve in corpus"])
    parts += box(660, 280, 280, 60, ["Abstention", "top score below threshold:", "No supporting passage found in the approved corpus."])
    parts += arrow(885, 130, 885, 188)
    parts += arrow(800, 250, 800, 278, "else")
    parts.append(f"<text x='{WIDTH - 20}' y='{HEIGHT - 12}' text-anchor='end' font-size='10' {FONT} fill='black'>Drawn by tools/render_figure.py. Fictional identifiers.</text>")
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default=str(Path(__file__).resolve().parents[1] / "docs" / "figures" / "graph_retrieval.svg"))
    args = parser.parse_args(argv)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(), encoding="utf-8")
    print(f"wrote {out.name} ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
