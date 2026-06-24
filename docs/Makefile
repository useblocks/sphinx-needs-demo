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

.PHONY: help Makefile

# -- Variant builds (see automotive-adas/variants.rst) ------------------------
# Build the docs for a specific customer variant. The variant name is passed to
# Sphinx as a build tag (-t).
# NOTE: `make html -t customer_a` does NOT work — make eats `-t` as its own
# flag. Use these targets instead.
#
# html has no per-version nesting, so each variant gets its own output dir.
#
# ubTrace keys every dataset by (org -> project -> version) and keeps ONE dataset
# per version (a re-ingest at the same version overwrites). So each variant is
# given its OWN version id -- conf.py folds the variant into the version
# (base -> "main", customer_a -> "main-customer_a", ...) -- and is ALSO tagged
# with a `variant` dimension so ubTrace's "Filter versions by dimensions" menu
# selects among them. Each variant builds into its own output dir; their internal
# <out>/useblocks/sphinx-needs-demo/<version> paths already differ, so the import
# just copies them in (see the bundle's import-demo-build.sh).
#
# Build EVERY variant at once with:  make ubtrace-all

.PHONY: html-customer-a html-customer-b ubtrace-customer-a ubtrace-customer-b variant ubtrace-all

# Build all current-version variants (base + customer_a + customer_b), each into
# its own output dir. This is the single command to refresh the full variant set.
ubtrace-all:
	@$(SPHINXBUILD) -b ubtrace                "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace"            $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -b ubtrace -t customer_a  "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace-customer_a" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -b ubtrace -t customer_b  "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace-customer_b" $(SPHINXOPTS) $(O)
	@echo "Built variants: base, customer_a, customer_b -> $(BUILDDIR)/ubtrace[-<variant>]"

html-customer-a:
	@$(SPHINXBUILD) -b html -t customer_a "$(SOURCEDIR)" "$(BUILDDIR)/html-customer_a" $(SPHINXOPTS) $(O)

html-customer-b:
	@$(SPHINXBUILD) -b html -t customer_b "$(SOURCEDIR)" "$(BUILDDIR)/html-customer_b" $(SPHINXOPTS) $(O)

ubtrace-customer-a:
	@$(SPHINXBUILD) -b ubtrace -t customer_a "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace-customer_a" $(SPHINXOPTS) $(O)

ubtrace-customer-b:
	@$(SPHINXBUILD) -b ubtrace -t customer_b "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace-customer_b" $(SPHINXOPTS) $(O)

# Generic variant build, parameterised by BUILDER and VARIANT, e.g.
#   make variant BUILDER=html VARIANT=customer_a
#   make variant BUILDER=ubtrace VARIANT=customer_b
# Every variant builds into its own dir; for ubtrace the `variant` dimension
# (set in conf.py from the build tag) classifies the build inside ubTrace.
BUILDER ?= html
VARIANT ?= customer_a
variant:
	@$(SPHINXBUILD) -b $(BUILDER) -t $(VARIANT) "$(SOURCEDIR)" "$(BUILDDIR)/$(BUILDER)-$(VARIANT)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
