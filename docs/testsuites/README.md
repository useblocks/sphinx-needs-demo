# Test Suites

This directory holds JUnit XML reports consumed by `sphinx-test-reports`.

## `coffee_machine_junit.xml`

**Do not check this file in** — it is generated automatically before each
Sphinx build and is listed in `.gitignore`.

### How it is generated

1. `cargo test` runs the Rust unit tests in `crates/coffee-machine/`.
2. Its output is piped through `scripts/cargo_test_to_junit.py`, which
   converts the test results to JUnit XML.
3. The script maps each Rust test function to its sphinx-needs test
   specification ID (e.g. `TEST_BREW_STRENGTH`) so that `tr_link` can
   automatically link test-run needs to their test specs.

### Manual regeneration

```bash
cd crates/coffee-machine
cargo test 2>&1 | python ../../scripts/cargo_test_to_junit.py > ../../docs/testsuites/coffee_machine_junit.xml
```

### Automatic regeneration

The top-level `Makefile` runs this step automatically before every docs
build:

```bash
make html        # runs cargo test → JUnit XML → Sphinx build
make test-report # just regenerate the XML without building docs
```
