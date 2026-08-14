# Configuration file for the Sphinx documentation builder.
#
# This is an independent Sphinx project (its own conf.py + ubproject.toml).
# It only shares this repo's uv-managed virtual environment with the other
# demo projects (basic_example, coffee-machine, automotive-adas, safety_example).
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import shutil

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sphinx-Needs Demo - Coffee Machine"
copyright = "2026, team useblocks"
author = "team useblocks"
version = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# List of Sphinx extension to use.
extensions = [
    "sphinx_needs",
    "sphinx_codelinks",  # Enable code-to-documentation traceability
    "sphinx_design",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.test_reports",
]

###############################################################################
# SPHINX-NEEDS Config START
###############################################################################

# Read the configuration from an external TOML file.
# This makes it possible to use ubCode and its tools directly with
# the project. Declarative configuration formats are also preferred as they
# cannot contain logic and can be consumed by almost all languages.
needs_from_toml = "ubproject.toml"

###############################################################################
# SPHINX-NEEDS Config END
###############################################################################


###############################################################################
# SPHINX-CODELINKS Config START
###############################################################################

# Read the codelinks configuration from the same TOML file.
# This enables traceability between source code and documentation.
# Docs: https://codelinks.useblocks.com/
src_trace_config_from_toml = "ubproject.toml"

###############################################################################
# SPHINX-CODELINKS Config END
###############################################################################


###############################################################################
# SPHINX-TEST-REPORTS Config START
###############################################################################

# Override the default test-case need of Sphinx-Test-Reports, so that is called
# ``test_run`` instead.
# Docs: https://sphinx-test-reports.readthedocs.io/en/latest/configuration.html#tr-case
tr_case = ["test-run", "testrun", "Test-Run", "TR_", "#999999", "node"]

# Use a different field name for test report files to avoid conflict with codelinks
# Default is "file" but sphinx-codelinks also uses "file" for source code paths
tr_file_option = "test_file"

###############################################################################
# SPHINX-TEST-REPORTS Config END
###############################################################################

templates_path = ["_templates"]

# Use a custom test-report template that removes the broken self-referencing literalinclude
tr_report_template = "_static/test_report_template.txt"

# List of files/folder to ignore.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# Sphinx-Needs features like ``needflow``/``needsequence`` render via Graphviz.
# If `dot` is missing, rendering embeds the error inside the generated SVG
# instead of failing the build, which sphinx-build -W cannot catch. Fail fast
# at config load time.
if shutil.which("dot") is None:
    raise RuntimeError(
        "Graphviz 'dot' executable not found on PATH. "
        "needflow/needsequence require it to render diagrams. Install graphviz "
        "(e.g. 'apt-get install graphviz') and retry."
    )

# We bring our own plantuml jar file.
# These options tell Sphinxcontrib-PlantUML we it can find this file.
local_plantuml_path = os.path.join(
    os.path.dirname(__file__), "utils", "plantuml-1.2022.14.jar"
)
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
plantuml_output_format = "svg"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

html_static_path = ["_static"]

html_logo = "_images/sphinx-needs-logo.png"
html_favicon = "_images/sphinx-needs-logo.svg"

html_theme_options = {
    "sidebar_hide_name": True,
    "top_of_page_buttons": ["view", "edit"],
    "source_repository": "https://github.com/useblocks/sphinx-needs-demo",
    "source_branch": "main",
    "source_directory": "docs/coffee-machine/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/useblocks/sphinx-needs-demo",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}

html_css_files = [
    "furo.css",
    "custom.css",
]
