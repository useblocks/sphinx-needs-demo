# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import jinja2
import sys

code_path = os.path.join(os.path.dirname(__file__), "../", "src/")
sys.path.append(code_path)
print(f"CODE_PATH: {code_path}")


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx-Needs Demo'
copyright = '2024, team useblocks'
author = 'team useblocks'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_needs",
    "sphinx_design",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.test_reports",
    "sphinx_simplepdf",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_preview"
]

if os.environ.get("PDF", "0") != "1":
    extensions.append("sphinx_immaterial")

###############################################################################
# SPHINX-NEEDS Config START

needs_types = [dict(directive="req", title="Requirement", prefix="R_", color="#BFD8D2", style="node"),
               dict(directive="spec", title="Specification", prefix="S_", color="#FEDCD2", style="node"),
               dict(directive="impl", title="Implementation", prefix="I_", color="#DF744A", style="node"),
               dict(directive="test", title="Test Case", prefix="T_", color="#DCB239", style="node"),
               dict(directive="person", title="Person", prefix="P_", color="#DCB239", style="actor"),
               dict(directive="team", title="Team", prefix="T_", color="#DCB239", style="node"),
               dict(directive="release", title="Release", prefix="R_", color="#DCB239", style="node"),
           ]

needs_extra_options = ['role', 'contact', 'image', 'date']


needs_extra_links = [
   {  # team -> person
      "option": "persons",
      "incoming": "is working for",
      "outgoing": "persons",
   },
   {  # req -> release
      "option": "release",
      "incoming": "contains",
      "outgoing": "release",
   },
   {  # req -> author
      "option": "author",
      "incoming": "ownes",
      "outgoing": "author",
   },
    {  # req -> req, release -> release
      "option": "based_on",
      "incoming": "supports",
      "outgoing": "based on",
   },
   {  # spec -> req
      "option": "reqs",
      "incoming": "specified by",
      "outgoing": "specifies",
   },
   {  # impl -> spec 
      "option": "implements",
      "incoming": "implemented by",
      "outgoing": "implements",
   },
   {  # test_case -> spec
      "option": "spec",
      "incoming": "test_cases",
      "outgoing": "specs",
   },
   {  # test_case -> test_run
      "option": "runs",
      "incoming": "test_cases",
      "outgoing": "runs",
   },
   {  # test_case -> spec
      "option": "specs",
      "incoming": "test_cases",
      "outgoing": "specs",
   },
]

needs_id_required = True
needs_id_regex = r".*"

tr_case = ['test_run', 'testrun', 'Test-Run', 'TR_', '#999999', 'node']

needs_global_options = {
   # Without default value
   'collapse': False,
   'runs': ("[[tr_link('id', 'case_name')]]", "type=='test'"),
   'post_template': [
       ("req_post", "type in ['req']"),
       ("spec_post", "type in ['spec']")
   ],
   
}

# SPHINX-NEEDS Config END
###############################################################################

preview_config = {
    "selector": "div.md-content a",
    "not_selector": "div.needs_head a, h1 a, h2 a, a.headerlink, a.md-content__button, a.image-reference, em.sig-param a",
    "set_icon": True,
    "icon_only": True,
    "icon_click": True,
    "icon": "🔍",
    "width": 600,
    "height": 400,
    "offset": {
        "left": 0,
        "top": 0
    },
    "timeout": 0,
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'demo_page_header.rst']

local_plantuml_path = os.path.join(os.path.dirname(__file__), "utils", "plantuml-1.2022.14.jar")
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
# plantuml_output_format = 'png'
plantuml_output_format = "svg_img"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
if os.environ.get("PDF", 0) != 1:
   html_theme = 'sphinx_immaterial'

html_static_path = ['_static']

sphinx_immaterial_override_generic_admonitions = True

html_logo = "_images/sphinx-needs-logo.png"
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github",
        "edit": "material/file-edit-outline",
    },
    "site_url": "https://jbms.github.io/sphinx-immaterial/",
    "repo_url": "https://github.com/useblocks/sphinx-needs-demo",
    "repo_name": "Sphinx-Needs Demo",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": True,
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
    'custom.css',
]

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.

    This voodoo is needed as we use the jinja command ``include``, which searches
    for the referenced file. This works locally, but hans't worked on ReadTheDocs.
    This "complex" cwd and Template-Folder operations make it working
    """
    old_cwd = os.getcwd()
    
    jinja2.FileSystemLoader(app.confdir)
    os.chdir(os.path.dirname(__file__))
    src = source[0]
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.from_string(src)
    #template = jinja2.Template(src, autoescape=True, environemnt=env)
    rendered = template.render(**app.config.html_context)
    source[0] = rendered
    os.chdir(old_cwd)


def setup(app):
    app.connect("source-read", rstjinja)