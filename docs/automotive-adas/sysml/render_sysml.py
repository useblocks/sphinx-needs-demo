"""Render every ``.gaphor`` file in this directory to a sibling ``.svg``.

This is a one-shot rendering step run from a developer / CI machine that
has Gaphor (and therefore Cairo + PyGObject) installed. The resulting SVG
is committed into the repo and embedded by the docs via plain
``.. figure::`` directives, so the documentation build itself has zero
dependency on Cairo / GTK.

Usage:

.. code:: console

   uv run --extra render python docs/automotive-adas/sysml/render_sysml.py

Each ``.gaphor`` file may contain multiple diagrams. Every diagram is
rendered as ``<gaphor stem>__<slugified diagram name>.svg``.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from gaphor.core.modeling import Diagram, ElementFactory
from gaphor.diagram.export import save_svg
from gaphor.services.modelinglanguage import ModelingLanguageService
from gaphor.storage import storage

HERE = Path(__file__).resolve().parent


def _slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "diagram"


def _render(model_path: Path) -> list[Path]:
    ef = ElementFactory()
    ml = ModelingLanguageService()
    with model_path.open(encoding="utf-8") as fp:
        storage.load(fp, ef, ml)

    written: list[Path] = []
    for diagram in ef.select(lambda e: isinstance(e, Diagram)):
        out = model_path.with_name(f"{model_path.stem}__{_slugify(diagram.name)}.svg")
        save_svg(out, diagram)
        written.append(out)
    return written


def main() -> int:
    sources = sorted(HERE.glob("*.gaphor"))
    if not sources:
        print(f"No .gaphor files found under {HERE}", file=sys.stderr)
        return 1
    for src in sources:
        for out in _render(src):
            print(f"Rendered {src.name} -> {out.name} ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
