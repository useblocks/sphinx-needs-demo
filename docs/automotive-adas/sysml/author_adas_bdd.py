"""Programmatically author the ADAS Traffic Sign Recognition BDD.

This script regenerates ``adas-tsr-bdd.gaphor`` from scratch using Gaphor's
Python API. The model can then be opened and tweaked in the Gaphor GUI, and
re-exported to SVG via :mod:`render_sysml`. Re-run after structural changes:

.. code:: console

   uv run python docs/automotive-adas/sysml/author_adas_bdd.py
   uv run python docs/automotive-adas/sysml/render_sysml.py

The generated file is committed alongside the rendered SVG; the doc build
itself does **not** depend on Gaphor or Cairo (it just embeds the SVG via
``.. figure::``).
"""

from __future__ import annotations

from pathlib import Path

from gaphor.core.modeling import ElementFactory
from gaphor.storage import storage
from gaphor.SysML import sysml
from gaphor.SysML.blocks import BlockItem
from gaphor.UML import uml

OUTPUT = Path(__file__).with_name("adas-tsr-bdd.gaphor")


def _make_block(ef: ElementFactory, package, name: str):
    block = ef.create(sysml.Block)
    block.name = name
    block.package = package
    return block


def _make_part(ef: ElementFactory, parent, name: str, type_block):
    prop = ef.create(uml.Property)
    prop.name = name
    prop.aggregation = "composite"
    prop.type = type_block
    prop.class_ = parent
    return prop


def _place_block(diag, block, x: float, y: float, width: float = 180, height: float = 80, *, show_parts: bool = False):
    item = diag.create(BlockItem, subject=block)
    item.matrix.translate(x, y)
    item.width = width
    item.height = height
    item.show_parts = 1 if show_parts else 0
    return item


def build() -> ElementFactory:
    ef = ElementFactory()

    pkg = ef.create(uml.Package)
    pkg.name = "ADAS"

    tsr = _make_block(ef, pkg, "TrafficSignRecognition")
    cam = _make_block(ef, pkg, "FrontCamera")
    interpreter = _make_block(ef, pkg, "SignInterpreter")
    veh_ctl = _make_block(ef, pkg, "VehicleControl")

    # Parts on the parent block (rendered automatically by Gaphor inside a
    # "parts" compartment when ``show_parts`` is on).
    _make_part(ef, tsr, "camera", cam)
    _make_part(ef, tsr, "interpreter", interpreter)
    _make_part(ef, tsr, "control", veh_ctl)

    diag = ef.create(sysml.BlockDefinitionDiagram)
    diag.name = "TSR Block Definition"
    diag.element = pkg

    # Parent block at top centre, parts compartment turned on so the named
    # parts render inside the block instead of as separate items that would
    # otherwise overlap the parent label.
    _place_block(diag, tsr, x=200, y=40, width=240, height=160, show_parts=True)

    # Sub-block definitions in a row below.
    spacing = 40
    sub_w, sub_h = 160, 70
    row_y = 280
    start_x = 200 + (240 - (3 * sub_w + 2 * spacing)) / 2
    for i, sub in enumerate((cam, interpreter, veh_ctl)):
        _place_block(diag, sub, x=start_x + i * (sub_w + spacing), y=row_y, width=sub_w, height=sub_h)

    return ef


def main() -> None:
    ef = build()
    with OUTPUT.open("w", encoding="utf-8") as fp:
        storage.save(fp, ef)
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
