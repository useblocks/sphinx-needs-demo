# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import jinja2


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx-Needs Demo'
copyright = '2024, team useblocks'
author = 'team useblocks'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_immaterial",
    "sphinx_needs",
    "sphinx_design",
    "sphinxcontrib.plantuml",
    "sphinxcontrib.test_reports"
]


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
   'runs': ("[[tr_link('id', 'case_name')]]", "type=='test'")
}

# SPHINX-NEEDS Config END
###############################################################################

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'demo_page_header.rst']

local_plantuml_path = os.path.join(os.path.dirname(__file__), "utils", "plantuml-1.2022.14.jar")
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
# plantuml_output_format = 'png'
plantuml_output_format = "svg_img"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

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
        # "search.highlight",
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