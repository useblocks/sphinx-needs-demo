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
# A build is classified along TWO dimensions, each passed to Sphinx as a build
# tag (-t): a LOCATION (eu | uk | asia) and a vehicle TYPE (combi | cabrio |
# motorcycle). Combine one of each, e.g. `-t asia -t cabrio`.
# NOTE: `make html -t uk` does NOT work — make eats `-t` as its own flag. Use
# the targets below instead.
#
# html has no per-version nesting, so each combination gets its own output dir.
#
# ubTrace keys every dataset by (org -> project -> version) and keeps ONE dataset
# per version (a re-ingest at the same version overwrites). So each combination
# is given its OWN version id -- conf.py folds (location, type) into the version
# (eu/combi -> "main", uk/cabrio -> "main-uk-cabrio", ...) -- and is ALSO tagged
# with `location` and `type` dimensions so ubTrace's "Filter versions by
# dimensions" menu can slice by either axis. Each combination builds into its own
# output dir; their internal <out>/useblocks/sphinx-needs-demo/<version> paths
# already differ, so the import just copies them in (see import-demo-build.sh).
#
# Build EVERY location x type combination at once with:  make ubtrace-all

.PHONY: html-uk-cabrio html-asia-motorcycle ubtrace-all variant

# Build all 9 location x type combinations, each into its own output dir. This
# is the single command to refresh the full variant set for ubTrace; the two
# dimension filters (location, type) are then fully populated.
ubtrace-all:
	@for loc in eu uk asia; do \
	  for typ in combi cabrio motorcycle; do \
	    echo ">> building $$loc / $$typ"; \
	    $(SPHINXBUILD) -b ubtrace -t $$loc -t $$typ "$(SOURCEDIR)" "$(BUILDDIR)/ubtrace-$$loc-$$typ" $(SPHINXOPTS) $(O); \
	  done; \
	done
	@echo "Built 9 combinations (eu/uk/asia x combi/cabrio/motorcycle) -> $(BUILDDIR)/ubtrace-<location>-<type>"

# A couple of convenience html targets for spot-checking specific combinations.
html-uk-cabrio:
	@$(SPHINXBUILD) -b html -t uk -t cabrio "$(SOURCEDIR)" "$(BUILDDIR)/html-uk-cabrio" $(SPHINXOPTS) $(O)

html-asia-motorcycle:
	@$(SPHINXBUILD) -b html -t asia -t motorcycle "$(SOURCEDIR)" "$(BUILDDIR)/html-asia-motorcycle" $(SPHINXOPTS) $(O)

# Generic variant build, parameterised by BUILDER, LOCATION and TYPE, e.g.
#   make variant BUILDER=html LOCATION=uk TYPE=cabrio
#   make variant BUILDER=ubtrace LOCATION=asia TYPE=motorcycle
# Each combination builds into its own dir; for ubtrace the `location`/`type`
# dimensions (set in conf.py from the build tags) classify the build in ubTrace.
BUILDER ?= html
LOCATION ?= eu
TYPE ?= combi
variant:
	@$(SPHINXBUILD) -b $(BUILDER) -t $(LOCATION) -t $(TYPE) "$(SOURCEDIR)" "$(BUILDDIR)/$(BUILDER)-$(LOCATION)-$(TYPE)" $(SPHINXOPTS) $(O)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
