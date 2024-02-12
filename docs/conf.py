# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

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
   {  # test_case -> test_run
      "option": "runs",
      "incoming": "test_cases",
      "outgoing": "runs",
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
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']

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