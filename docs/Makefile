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
# ubtrace tags each build with a `variant` *dimension* (org -> project ->
# version stays single; see conf.py). Because every variant shares the same
# structural path <out>/useblocks/sphinx-needs-demo/main, the dimension — not
# the directory — is what distinguishes them once ingested into ubTrace. Two
# variant builds therefore CANNOT share one output dir on disk (they would
# overwrite each other), so each variant builds into its own dir and is ingested
# separately; ubTrace keeps them apart via the `variant` dimension.

.PHONY: html-customer-a html-customer-b ubtrace-customer-a ubtrace-customer-b variant

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
