# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys

import jinja2

# We need to make Python aware of our project source code, which is stored outside `/docs`,
# under `src/`
code_path = os.path.join(os.path.dirname(__file__), "../", "src/")
sys.path.append(code_path)
print(f"CODE_PATH: {code_path}")


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sphinx-Needs Demo"
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
    "sphinx_simplepdf",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_preview",
    "sphinx_design",
    "ubt_sphinx",
]

ubtrace_organization = "useblocks"
ubtrace_project = "sphinx-needs-demo"
ubtrace_version = "main"

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

# The config for the preview features, which allows to "sneak" into a link.
# Docs: https://sphinx-preview.readthedocs.io/en/latest/#configuration
preview_config = {
    # Add a preview icon only for this type of links
    # This is very theme and HTML specific. In this case the Furo main article area.
    "selector": "article#furo-main-content a",
    # A list of selectors, where no preview icon shall be added, because it makes often no sense.
    # For instance the own ID of a need object, or the link on an image to open the image.
    "not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.back-to-top, a.image-reference, em.sig-param a, a.paginate_button, a.sd-btn",
    "set_icon": True,
    "icon_only": True,
    "icon_click": True,
    "icon": "🔍",
    "width": 600,
    "height": 400,
    "offset": {"left": 0, "top": 0},
    "timeout": 0,
}

templates_path = ["_templates"]

# List of files/folder to ignore.
# Sphinx builds all ``.rst`` files under ``/docs``, no matte if they are part
# of a toctree or not. So as we have some rst-templates, we need to tell Sphinx to ignore
# these files.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "demo_page_header.rst",
    "demo_hints",
]

# We bring our own plantuml jar file.
# These options tell Sphinxcontrib-PlantUML we it can find this file.
local_plantuml_path = os.path.join(
    os.path.dirname(__file__), "utils", "plantuml-1.2022.14.jar"
)
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
# plantuml_output_format = 'png'
plantuml_output_format = "svg_img"


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
    "source_directory": "docs/",
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

# Some special vodoo to render each rst-file by jinja, before it gets handled by Sphinx.
# This allows us to use the powerfull jinja-features to create content in a loop, react on
# external data input, or include templates with parameters.
# In our case we use it mostly to set the "demo page details" header in each page.
# A good blog post about this can be found here:
# Docs: https://ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
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
    # template = jinja2.Template(src, autoescape=True, environemnt=env)
    rendered = template.render(**app.config.html_context)
    source[0] = rendered
    os.chdir(old_cwd)


# This function allows us to register any kind of black magic for Sphinx :)
def setup(app):
    # We connect our jinja-function from above with the "source-read" event of Sphinx,
    # which gets called for every file before Sphinx starts to handle the file on its own.
    # This allows us to manipulate the content.
    app.connect("source-read", rstjinja)
