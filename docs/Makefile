# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= uv run sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# All ADAS variants, derived from the variant definition files.
VARIANTS = $(basename $(notdir $(wildcard $(SOURCEDIR)/variants/*.json)))

# Build the ubtrace output for every variant and assemble one import-ready
# tree under _build/ubtrace-variants/ for the local (non-API) ubTrace import.
#
# ubTrace variant rules (no variant level exists in the directory tree):
#   - the version FOLDER name is the unique technical key (versionId); two
#     variants of the same version must live in differently-named folders,
#   - the `version` field inside config/ubtrace_project.toml is the shared
#     display name (versionGroupId) that groups the variants in ubTrace; the
#     folder name != toml version mismatch is the intended mechanism.
# ubt_sphinx derives both from the single ubtrace_version value, so each
# variant is built separately (kept in _build/ubtrace-<variant> as incremental
# build cache) and its version folder is then copied into the assembled tree
# as <version>-<variant>, leaving the toml untouched.
#
# Note that upload.sh / the API flow is different: it uploads one build at a
# time from _build/ubtrace and derives the folder name server-side (see
# .github/workflows/ubtrace.yml).
UBTRACE_VARIANTS_DIR = $(BUILDDIR)/ubtrace-variants

.PHONY: ubtrace-all
ubtrace-all:
	@set -e; \
	rm -rf "$(UBTRACE_VARIANTS_DIR)"; \
	for v in $(VARIANTS); do \
		echo "==> ubtrace build for variant $$v"; \
		$(SPHINXBUILD) -b ubtrace -D needs_variant_data_file=variants/$$v.json "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace-$$v" $(SPHINXOPTS) $(O); \
		for rel in $$(cd "$(BUILDDIR)/ubtrace-$$v" && ls -d */*/*/); do \
			rel=$${rel%/}; \
			ver=$$(basename "$$rel"); proj=$$(dirname "$$rel"); \
			mkdir -p "$(UBTRACE_VARIANTS_DIR)/$$proj"; \
			cp -a "$(BUILDDIR)/ubtrace-$$v/$$rel" "$(UBTRACE_VARIANTS_DIR)/$$proj/$$ver-$$v"; \
			echo "    -> $(UBTRACE_VARIANTS_DIR)/$$proj/$$ver-$$v"; \
		done; \
		cp "$(BUILDDIR)/ubtrace-$$v/ubtrace_server.toml" "$(UBTRACE_VARIANTS_DIR)/" 2>/dev/null || true; \
	done

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
