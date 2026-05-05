"""Programmatically author the ADAS Traffic Sign Recognition BDD.

This script regenerates ``adas-tsr-bdd.gaphor`` from scratch using Gaphor's
Python API, so the model can be tracked as code rather than a binary-ish
diagram blob. Run it whenever you change the structure:

.. code:: console

   uv run python docs/automotive-adas/sysml/author_adas_bdd.py

The generated file is committed alongside this script and consumed by
Sphinx via the ``gaphor.extensions.sphinx`` extension and the
``gaphor_models`` mapping in ``docs/conf.py``.
"""

from __future__ import annotations

from pathlib import Path

from gaphor.core.modeling import ElementFactory
from gaphor.storage import storage
from gaphor.SysML import sysml
from gaphor.SysML.blocks import BlockItem, PropertyItem
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


def build() -> ElementFactory:
    ef = ElementFactory()

    pkg = ef.create(uml.Package)
    pkg.name = "ADAS"

    tsr = _make_block(ef, pkg, "TrafficSignRecognition")
    cam = _make_block(ef, pkg, "FrontCamera")
    interpreter = _make_block(ef, pkg, "SignInterpreter")
    veh_ctl = _make_block(ef, pkg, "VehicleControl")

    p_cam = _make_part(ef, tsr, "camera", cam)
    p_int = _make_part(ef, tsr, "interpreter", interpreter)
    p_veh = _make_part(ef, tsr, "control", veh_ctl)

    diag = ef.create(sysml.BlockDefinitionDiagram)
    diag.name = "TSR Block Definition"
    diag.element = pkg

    # Parent block with parts compartment
    tsr_item = diag.create(BlockItem, subject=tsr)
    tsr_item.matrix.translate(80, 60)
    tsr_item.width = 480
    tsr_item.height = 220

    for i, prop in enumerate((p_cam, p_int, p_veh)):
        item = diag.create(PropertyItem, subject=prop)
        col_x = 100 + i * 150
        item.matrix.translate(col_x, 160)
        item.width = 130
        item.height = 60

    # Sub-block definitions below (typical BDD layout)
    for i, sub in enumerate((cam, interpreter, veh_ctl)):
        sub_item = diag.create(BlockItem, subject=sub)
        sub_item.matrix.translate(80 + i * 200, 380)
        sub_item.width = 160
        sub_item.height = 70

    return ef


def main() -> None:
    ef = build()
    with OUTPUT.open("w", encoding="utf-8") as fp:
        storage.save(fp, ef)
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
