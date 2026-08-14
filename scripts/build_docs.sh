#!/usr/bin/env bash
# Builds every independent Sphinx-Needs demo project under docs/ with the
# shared uv-managed virtual environment (this repo's pyproject.toml/uv.lock).
#
# Each project (docs/, docs/basic_example, docs/coffee-machine,
# docs/automotive-adas, docs/safety_example) has its own conf.py and
# ubproject.toml and is built independently. Their outputs are placed
# side by side under one output directory so the plain hyperlinks between
# them (e.g. docs/index.rst -> ../basic_example/index.html) resolve.
#
# Usage: scripts/build_docs.sh [output_dir] [sphinx-build extra args...]
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${1:-${REPO_ROOT}/docs/_build/site}"
if [ "$#" -gt 0 ]; then
  shift
fi

mkdir -p "${OUTPUT_DIR}"

build() {
  local project_dir="$1"
  local out_subdir="$2"
  shift 2
  echo "::group::Build ${project_dir#"${REPO_ROOT}/"}"
  uv run sphinx-build -W -b html "$@" "${project_dir}" "${OUTPUT_DIR}/${out_subdir}"
  echo "::endgroup::"
}

# Landing project builds straight into the output root.
build "${REPO_ROOT}/docs" "." "$@"

build "${REPO_ROOT}/docs/basic_example" "basic_example" "$@"
build "${REPO_ROOT}/docs/coffee-machine" "coffee-machine" "$@"
build "${REPO_ROOT}/docs/safety_example" "safety_example" "$@"

# automotive-adas is the only variant-aware project; build the default variant
# for the plain HTML site (the ubtrace workflow uploads all variants separately).
build "${REPO_ROOT}/docs/automotive-adas" "automotive-adas" \
  -D needs_variant_data_file=variants/eu_left.json "$@"

echo "All projects built into ${OUTPUT_DIR}"
