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

# Build the ubtrace output for every variant, each into its own directory:
# _build/ubtrace-<variant>. Note that upload.sh expects _build/ubtrace
# (single-variant flow, see .github/workflows/ubtrace.yml); adjust its
# BUILD_DIR when uploading one of these.
.PHONY: ubtrace-all
ubtrace-all:
	@set -e; for v in $(VARIANTS); do \
		echo "==> ubtrace build for variant $$v"; \
		$(SPHINXBUILD) -b ubtrace -D needs_variant_data_file=variants/$$v.json "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace-$$v" $(SPHINXOPTS) $(O); \
	done

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
