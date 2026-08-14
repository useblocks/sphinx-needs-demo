#!/usr/bin/env bash
# Builds every independent Sphinx-Needs demo project under docs/ with the
# shared uv-managed virtual environment (this repo's pyproject.toml/uv.lock).
#
# Each project (docs/, docs/basic_example, docs/coffee-machine,
# docs/automotive-adas, docs/safety_example) has its own conf.py and
# ubproject.toml and is built independently. Their outputs are placed
# side by side under one output directory so the cross-project sidebar nav
# and intersphinx :doc: references between them resolve.
#
# Build order matters: the landing project (docs/) and safety_example use
# intersphinx to link to other projects, so their targets must be built
# first so the target's objects.inv already exists. If a future edit adds a
# cross-reference that creates a cycle (e.g. two projects linking to each
# other), this single-pass order will no longer be sufficient and the
# build would need a priming pass instead.
#
# Usage: scripts/build_docs.sh [output_dir] [sphinx-build extra args...]
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${1:-${REPO_ROOT}/docs/_build/site}"
if [ "$#" -gt 0 ]; then
  shift
fi

mkdir -p "${OUTPUT_DIR}"

# Prefer `uv run` (used locally and in CI, resolves this repo's shared venv
# from any project directory). Fall back to a plain sphinx-build if uv isn't
# on PATH - e.g. on Read the Docs, where dependencies are installed with
# `pip install .` into RTD's own active venv and uv is never installed.
if command -v uv >/dev/null 2>&1; then
  SPHINX_BUILD=(uv run sphinx-build)
else
  SPHINX_BUILD=(sphinx-build)
fi

build() {
  local project_dir="$1"
  local out_subdir="$2"
  shift 2
  echo "::group::Build ${project_dir#"${REPO_ROOT}/"}"
  "${SPHINX_BUILD[@]}" -W -b html "$@" "${project_dir}" "${OUTPUT_DIR}/${out_subdir}"
  echo "::endgroup::"
}

# Build the four demo projects first (in any order among themselves - none
# of them link to each other or to the landing project).
build "${REPO_ROOT}/docs/basic_example" "basic_example" "$@"
build "${REPO_ROOT}/docs/coffee-machine" "coffee-machine" "$@"

# automotive-adas is the only variant-aware project; build the default variant
# for the plain HTML site (the ubtrace workflow uploads all variants separately).
build "${REPO_ROOT}/docs/automotive-adas" "automotive-adas" \
  -D needs_variant_data_file=variants/eu_left.json "$@"

# safety_example links to automotive-adas via intersphinx, so it must build
# after it.
build "${REPO_ROOT}/docs/safety_example" "safety_example" "$@"

# The landing project links to all four demos via intersphinx, so it must
# build last, and straight into the output root.
build "${REPO_ROOT}/docs" "." "$@"

echo "All projects built into ${OUTPUT_DIR}"
