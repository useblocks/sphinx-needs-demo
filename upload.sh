#!/usr/bin/env bash
# Usage: UBTRACE_INGEST_TOKEN=<token> bash upload.sh
# The token needs "Ingest" permissions for the target ubTrace instance
# at team.useblocks.com.
# UBTRACE_VERSION may be overridden from the environment (CI sets it to
# the tag name); it defaults to "main" for local manual runs.

export UBTRACE_URL=https://api.team.useblocks.com/api
: "${UBTRACE_INGEST_TOKEN:?UBTRACE_INGEST_TOKEN is not set (create a token with Ingest permissions on team.useblocks.com and export it first)}"
export UBTRACE_ORG=useblocks
export UBTRACE_PROJECT=sphinx-needs-demo
export UBTRACE_VERSION="${UBTRACE_VERSION:-main}"

# Build the docs. ubt_sphinx writes its output under
#   docs/_build/ubtrace/<ubtrace_organization>/<ubtrace_project>/<ubtrace_version>/
# so the values above must match the conf.py settings (or the -D
# override passed to sphinx-build at build time).
# sphinx-build -b ubtrace docs docs/_build/ubtrace

# Package the version directory (the one that directly contains needs.json):
BUILD_DIR="docs/_build/ubtrace/${UBTRACE_ORG}/${UBTRACE_PROJECT}/${UBTRACE_VERSION}"
tar -czf /tmp/build.tar.gz -C "${BUILD_DIR}" .

# Upload it:
curl --fail-with-body --show-error \
  -H "Authorization: Bearer ${UBTRACE_INGEST_TOKEN}" \
  -F "file=@/tmp/build.tar.gz" \
  "${UBTRACE_URL}/v1/ingest/${UBTRACE_ORG}/${UBTRACE_PROJECT}/${UBTRACE_VERSION}?overwrite=true"
