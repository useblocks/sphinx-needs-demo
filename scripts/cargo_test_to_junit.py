#!/usr/bin/env python3
"""Parse ``cargo test`` stdout and emit JUnit XML on stdout.

Usage::

    cargo test 2>&1 | python cargo_test_to_junit.py > results.xml

The script reads the combined stdout/stderr of ``cargo test`` from
stdin, extracts every ``test <name> ... <status>`` line, and produces a
JUnit-compatible XML document that sphinx-test-reports can consume.

The JUnit ``name`` attribute is set to the corresponding test
specification ID (e.g. ``TEST_BREW_STRENGTH``) so that the
``tr_link('id', 'case_name')`` dynamic function in sphinx-needs can
automatically link test-run needs back to their test specs — no manual
``needextend`` directives required.
"""

import re
import sys
import xml.etree.ElementTree as ET

# Map each Rust test function path to the sphinx-needs test spec ID it
# verifies.  When a Rust test covers the same spec as another, both
# entries point to the same spec ID.
RUST_TEST_TO_SPEC: dict[str, str] = {
    "interfaces::tests::test_temperature_status_conversions": "TEST_TEMP_CONTROL",
    "interfaces::tests::test_sensor_data_creation": "TEST_TEMP_CONTROL",
    "interfaces::tests::test_temp_ctrl_status_fault_detection": "TEST_SAFETY_SHUTDOWN",
    "interfaces::tests::test_brew_ctrl_status_fault_detection": "TEST_SAFETY_SHUTDOWN",
    "interfaces::tests::test_brew_strength_enum": "TEST_BREW_STRENGTH",
    "interfaces::tests::test_user_command_variants": "TEST_BUTTON_DEBOUNCE",
}


def main() -> None:
    text = sys.stdin.read()
    tests = re.findall(r"test (\S+) \.\.\. (\w+)", text)

    root = ET.Element("testsuites")
    suite = ET.SubElement(
        root,
        "testsuite",
        name="coffee_machine",
        tests=str(len(tests)),
        failures=str(sum(1 for _, s in tests if s == "FAILED")),
        errors="0",
    )

    for rust_name, status in tests:
        # Use the spec ID as the JUnit test name so that tr_link can
        # match it against the test specification's need ID.
        spec_id = RUST_TEST_TO_SPEC.get(rust_name, rust_name)
        tc = ET.SubElement(
            suite,
            "testcase",
            classname=rust_name,
            name=spec_id,
            time="0.001",
        )
        if status == "FAILED":
            ET.SubElement(tc, "failure", message="Test failed")

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(sys.stdout, xml_declaration=True, encoding="unicode")
    print()  # trailing newline


if __name__ == "__main__":
    main()
