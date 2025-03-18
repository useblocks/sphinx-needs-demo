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
copyright = "2024, team useblocks"
author = "team useblocks"
version = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# List of Sphinx extension to use.
extensions = [
    "sphinx_needs",
    "sphinx_design",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.test_reports",
    "sphinx_simplepdf",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_preview",
    "ubt_sphinx",
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
# SPHINX-TEST-REPORTS Config START
###############################################################################

# Override the default test-case need of Sphinx-Test-Reports, so that is called
# ``test_run`` instead.
# Docs: https://sphinx-test-reports.readthedocs.io/en/latest/configuration.html#tr-case
tr_case = ["test-run", "testrun", "Test-Run", "TR_", "#999999", "node"]

###############################################################################
# SPHINX-TEST-REPORTS Config END
###############################################################################

# The config for the preview features, which allows to "sneak" into a link.
# Docs: https://sphinx-preview.readthedocs.io/en/latest/#configuration
preview_config = {
    # Add a preview icon only for this type of links
    # This is very theme and HTML specific. In this case "div-mo-content" is the content area
    # and we handle all links there.
    "selector": "div.md-content a",
    # A list of selectors, where no preview icon shall be added, because it makes often no sense.
    # For instance the own ID of a need object, or the link on an image to open the image.
    "not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a, a.paginate_button, a.sd-btn",
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

html_css_files = []
html_static_path = ["_static"]
html_logo = "_static/sphinx-needs-logo.svg"
html_favicon = "_static/favicon.ico"

if os.getenv("UBTRACE_BUILD", "0") == "1":
    ubtrace_license = "AAAAA-BBBBB-CCCCC-DDDDD"  # license not checked currently

    ubtrace_db_mode = "new"  # wipe, new, update, no
    html_theme = "alabaster"
    extensions.append("sphinx_copybutton")
    html_css_files.extend(
        [
            "custom_ubtrace.css",
            "sphinx_needs_common.css",
            "sphinx_needs_modern.css",
            "sphinx_needs_dark.css",
            "sphinx_needs_fixes.css",
            "font_awesome/font_awesome_all.min.css",  # Add CSS for FontAwesome icons
        ],
    )
    ubtrace_project_id = "sphinx-needs-demo"  # used as ubtrace identifier for APIs
    ubtrace_tag = "main"  # used as ubtrace version
    ubtrace_roles = {
        "open": [],
        "authenticated": ["authenticated"],
        "lic_ubtrace": ["lic_ubtrace", "authenticated"],
        "lic_partner": ["lic_partner", "lic_ubtrace", "authenticated"],
        "int_developer": [
            "int_developer",
            "lic_partner",
            "lic_ubtrace",
            "authenticated",
        ],
        "admin": [
            "admin",
            "int_developer",
            "lic_partner",
            "lic_ubtrace",
            "authenticated",
        ],
    }

    ubtrace_users = [
        {
            "email": "developer@useblocks.com",
            "username": "developer",
            "password": "developer",
            "active": True,
            "roles": ["int_developer"],
        },
    ]

    # Relative to the current working dir, so /ubdocs/
    ubtrace_server_port = 3000
    ubtrace_conf_overwrite = True

    # Pattern to secure pages manually.
    # Example: {"developer_handbook/features/": ["int_developer"]}
    ubtrace_secure_pattern = {}

    # ubTrace Theme Options
    ubtrace_theme_options = {
        "logo": {
            "desktop": {
                "light": "_static/sphinx-needs-logo.svg",
                "dark": "_static/sphinx-needs-logo.svg",
            },
            "mobile": {
                "light": "_static/sphinx-needs-logo.svg",
                "dark": "_static/sphinx-needs-logo.svg",
            },
        },
        "repo_url": "https://github.com/useblocks/sphinx-needs-demo/",
        "edit_uri": "/edit/main/docs/",
        "view_source_uri": "/blob/main/docs/",
    }

else:
    html_theme = "alabaster"  # Sphinx Defaul Theme

    # During a PDF build with Sphinx-SimplePDF, a special theme is used.
    # But adding "sphinx_immaterial" to the extension list, the "immaterial" already
    # does a lot of sphinx voodoo, which is not needed and does not work during a PDF build.
    # Therefore we add it only, if a special ENV-Var is not set.
    #
    # As we can't ask Sphinx already in the config file, which Builder will be used, we need
    # to set this information by hand, or in this case via an ENV var.
    #
    # To build HTML, just call ``make html
    # To build PDF, call ``env PDF=1 make simplepdf"
    if os.environ.get("PDF", "0") != "1":
        extensions.append("sphinx_immaterial")

    # Set ``html_theme`` to ``sphinx_immaterial`` only, if we do NOT perform a PDF build.
    if os.environ.get("PDF", 0) != 1:
        html_theme = "sphinx_immaterial"

    sphinx_immaterial_override_generic_admonitions = True

    html_theme_options = {
        "font": False,
        "icon": {
            "repo": "fontawesome/brands/github",
            "edit": "material/file-edit-outline",
        },
        "site_url": "https://jbms.github.io/sphinx-immaterial/",
        "repo_url": "https://github.com/useblocks/sphinx-needs-demo",
        "repo_name": "Sphinx-Needs Demo",
        "edit_uri": "blob/main/docs",
        "globaltoc_collapse": False,
        "features": [
            "navigation.expand",
            # "navigation.tabs",
            # "toc.integrate",
            "navigation.sections",
            # "navigation.instant",
            # "header.autohide",
            "navigation.top",
            # "navigation.tracking",
            "search.highlight",
            "search.share",
            "toc.follow",
            "toc.sticky",
            "content.tabs.link",
            "announce.dismiss",
        ],
        "palette": [
            {
                "media": "(prefers-color-scheme: light)",
                "scheme": "default",
                "primary": "blue",
                "accent": "light-cyan",
                # "toggle": {
                #     "icon": "material/lightbulb-outline",
                #     "name": "Switch to dark mode",
                # },
            },
            # {
            #     "media": "(prefers-color-scheme: dark)",
            #     "scheme": "slate",
            #     "primary": "blue",
            #     "accent": "light-cyan",
            #     "toggle": {
            #         "icon": "material/lightbulb",
            #         "name": "Switch to light mode",
            #     },
            # },
        ],
        "toc_title_is_page_title": True,
    }

    html_css_files = [
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
