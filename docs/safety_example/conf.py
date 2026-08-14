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

import jinja2

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sphinx-Needs Demo - Safety Example"
copyright = "2026, team useblocks"
author = "team useblocks"
version = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# List of Sphinx extension to use.
extensions = [
    "sphinx_needs",
    "sphinxcontrib.plantuml",
    "sphinx_design",
    "sphinx_simplepdf",
    "sphinx_preview",
    "sphinx.ext.intersphinx",
]

###############################################################################
# INTERSPHINX Config START
###############################################################################

# This project links to automotive-adas (see system_requirements.rst).
# intersphinx validates that :doc: reference at build time instead of using a
# hand-typed <a href> link, which can silently rot. The inventory is only
# built when scripts/build_docs.sh builds all projects into one output tree;
# a standalone build of this project alone won't have it.
intersphinx_mapping = {
    "automotive-adas": ("../automotive-adas", "../_build/site/automotive-adas/objects.inv"),
}

###############################################################################
# INTERSPHINX Config END
###############################################################################

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

# The config for the preview features, which allows to "sneak" into a link.
# Docs: https://sphinx-preview.readthedocs.io/en/latest/#configuration
preview_config = {
    "selector": "article#furo-main-content a",
    "not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.back-to-top, a.image-reference, em.sig-param a, a.paginate_button, a.sd-btn, a[href*='#L'], div.highlight a",
    "set_icon": True,
    "icon_only": True,
    "icon_click": True,
    "icon": "🔍",
    "width": 600,
    "height": 400,
    "offset": {"left": 0, "top": 0},
    "timeout": 0,
}

# _shared_templates is the single source for projects-nav.html, used by
# every project directly (see html_sidebars below) instead of being copied.
templates_path = ["../_shared_templates"]

# List of files/folder to ignore.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "demo_page_header.rst",
]

# Sphinx-Needs features like ``needflow`` render via PlantUML, which itself
# renders node/graph diagrams via Graphviz. If `dot` is missing, rendering
# embeds the error inside the generated SVG instead of failing the build,
# which sphinx-build -W cannot catch. Fail fast at config load time.
if shutil.which("dot") is None:
    raise RuntimeError(
        "Graphviz 'dot' executable not found on PATH. "
        "needflow requires it to render diagrams. Install graphviz "
        "(e.g. 'apt-get install graphviz') and retry."
    )

# The plantuml jar file lives once at docs/utils/, shared by every project
# that needs it, instead of being duplicated per project.
local_plantuml_path = os.path.join(
    os.path.dirname(__file__), "..", "utils", "plantuml-1.2022.14.jar"
)
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
plantuml_output_format = "svg"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

# Shared with every project instead of duplicated per project.
html_static_path = ["../_static"]

# Shared with every project instead of duplicated per project.
html_logo = "../_images/sphinx-needs-logo.png"
html_favicon = "../_images/sphinx-needs-logo.svg"

html_theme_options = {
    "sidebar_hide_name": True,
    "top_of_page_buttons": ["view", "edit"],
    "source_repository": "https://github.com/useblocks/sphinx-needs-demo",
    "source_branch": "main",
    "source_directory": "docs/safety_example/",
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

# Used by _templates/projects-nav.html (synced from
# docs/_shared_templates/projects-nav.html by scripts/build_docs.sh) to
# highlight the current project in the cross-project sidebar nav.
html_context = {
    "current_project": "safety_example",
}

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "projects-nav.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}


def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.

    This voodoo is needed as we use the jinja command ``include``, which searches
    for the referenced file. This works locally, but has't worked on ReadTheDocs.
    These more "complex" cwd and Template-Folder operations make it working.
    """
    old_cwd = os.getcwd()

    jinja2.FileSystemLoader(app.confdir)
    os.chdir(os.path.dirname(__file__))
    src = source[0]
    env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    template = env.from_string(src)
    rendered = template.render(**app.config.html_context)
    source[0] = rendered
    os.chdir(old_cwd)


def setup(app):
    app.connect("source-read", rstjinja)
