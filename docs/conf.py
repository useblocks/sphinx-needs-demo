# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import jinja2
import sys

# We need to make Python aware of our project source code, which is stored outside `/docs`, 
# under `src/`
code_path = os.path.join(os.path.dirname(__file__), "../", "src/")
sys.path.append(code_path)
print(f"CODE_PATH: {code_path}")


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinx-Needs Demo'
copyright = '2024, team useblocks'
author = 'team useblocks'
version = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# List of Sphinx extension to use.
extensions = [
    "sphinx_needs",
    "sphinx_design",
    "sphinxcontrib.plantuml",
    # "sphinxcontrib.test_reports",
    "sphinx_simplepdf",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_preview"
]

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

###############################################################################
# SPHINX-NEEDS Config START
###############################################################################

# Build also the needs.json file with each HTML build
needs_build_json = True

# List of need type, we need in our documentation.
# Docs: https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-types
needs_types = [dict(directive="req", title="Requirement", prefix="R_", color="#FFB300", style="node"),
               dict(directive="spec", title="Specification", prefix="S_", color="#ec6dd7", style="node"),
               dict(directive="impl", title="Implementation", prefix="I_", color="#fa8638", style="node"),
               dict(directive="test", title="Test Case", prefix="T_", color="#A6BDD7", style="node"),
               dict(directive="person", title="Person", prefix="P_", color="#C10020", style="actor"),
               dict(directive="team", title="Team", prefix="T_", color="#CEA262", style="node"),
               dict(directive="release", title="Release", prefix="R_", color="#817066", style="node"),
               dict(directive="arch", title="Architecture", prefix="_", color="#4aac73", style="node"),
               dict(directive="need", title="Need", prefix="_", color="#F6768E", style="node"),
               dict(directive="swarch", title="SW_Architecture", prefix="SWARCH_", color="#2d86c1", style="node"),
               dict(directive="swreq", title="SW_Requirement", prefix="SWREQ_", color="#a8f578", style="node"),
           ]

# Additional options, which shall be available for all need types.
# Docs: https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-options
needs_extra_options = ['role', 'contact', 'image', 'date', 'customer', 'github', 'jira', 'config']

# Extra link types, which shall be available and allow need types to be linked to each other.
# We use a dedicated linked type for each type of a conncetion, for instance from 
# a specification to a requirement. This makes filtering and visualization of such connections
# much easier, as we can sure the target need of a link has always a specific type.
# Docs: https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-extra-links
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

# We force the author to set anb ID by hand.
# Otherwise Sphinx-Needs would create on based on the Need title.
# So a title change will change the ID and all set links will get invalid.
# Therefore setting a stable ID by hand is always a good idea.
# Docs: https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-id-required
needs_id_required = True

# The format of a need gets defined here.
# Docs: https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-id-regex
needs_id_regex = r"[A-Z_]{3,10}(_[\d]{1,3})*"

# We override the default test-case need of Sphinx-Test-Reports, so that is called
# ``test_run`` instead.
# Docs: https://sphinx-test-reports.readthedocs.io/en/latest/configuration.html#tr-case
tr_case = ['test_run', 'testrun', 'Test-Run', 'TR_', '#999999', 'node']

# `needs_global_options` allows us to set values for Sphinx-Need objects globally, based on
# filters.
# Docs: https://sphinx-needs.readthedocs.io/en/latest/configuration.html#needs-global-options
needs_global_options = {
   # The meta-area of all Sphinx-Needs objects shall be hidden. 
   # Supported only, if a "collapse button" is used in the selected need layout.
   'collapse': "False",
   # Automatically link test-runs with test-cases.
   # We use here the dynamic function ``tr_link`` so link 2 needs, 
   # if the ID of need A is the same as the case_name of need B.
   # But we do this only for objects of type ``test``.
   # Docs: https://sphinx-test-reports.readthedocs.io/en/latest/functions.html#tr-link
   #'runs': ("[[tr_link('id', 'case_name')]]", "type=='test'"),
   # By setting ``post_template``, we can add some extra content below a need object.
   # What gets added is set in the related template file under ``/needs_templates``.
   # In our case a traceability flow chart is generated, plus the same information as table.
   'post_template': [
       ('all_post', "type not in ['person'] and 'automotive-adas' in docname"),
       ('person_post', "type in ['person']"),
    ],
   'constraints': [
       (["status_set", "release_set"], "type in ['req'] and 'automotive-adas' in docname")
   ],
   'layout': [
       ('req_constraint', "type in ['req']"),
       ('adas', "type not in ['req']"),
   ]
}

needs_constraints = {
    "status_set": {
        "check_0": "status is not None and status in ['open', 'in progress', 'closed']",
        "severity": "LOW",
        "error_message": "Status is invalid or not set!"
    },
    "release_set": {
        "check_0": "len(release)>0",
        "severity": "CRITICAL",
        "error_message": "Requirement is not planned for any release!"
    },
}

needs_constraint_failed_options = {
    "CRITICAL": {
        "on_fail": ["warn"],
        "style": ["red_bar"],
        "force_style": False
    },

    "HIGH": {
        "on_fail": ["warn"],
        "style": ["orange_bar"],
        "force_style": False
    },

    "MEDIUM": {
        "on_fail": ["warn"],
        "style": ["yellow_bar"],
        "force_style": False
    },
    "LOW": {
        "on_fail": [],
        "style": ["blue_bar"],
        "force_style": False
    }
}

# needs_variants allows us to set specific option values based on the currently active variant.
# A use case is a different ``status``, depending on if the implementation needs to be done for 
# customer A or customer B.
# In the rst-code, the variant-values can then be set like this:
# ``:status: customer_a:open, customer_b:closed``
needs_variants = {
  "customer_a": "customer == 'A' or customer not in ['A', 'B']",
  "customer_b": "customer == 'B'"
}
# Activates variants handling for these options only.
# All other options get not checked, to save some build time, as these checks are quite time consuming.
needs_variant_options = ["author", "status"]

needs_layouts = {
    "adas": {
        "grid": "simple_footer",
        "layout": {
            "head": [
                '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>>  <<collapse_button("meta", '
                'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=False)>> '
            ],
            "meta": ["<<meta_all(no_links=True, exclude=['constraints_error'])>>", "<<meta_links_all()>>"],
            "footer": ["**Status**: <<meta('status')>>"]
        },
    },
    "req_constraint": {
        "grid": "simple_footer",
        "layout": {
            "head": [
                '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>>  <<collapse_button("meta", '
                'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=False)>> '
            ],
            "meta": ["<<meta_all(no_links=True, exclude=['constraints_error'])>>", "<<meta_links_all()>>"],
            "footer": ["**Process feedback**: <<meta('constraints_error')>>"]
        },
    },
}

needs_string_links = {
    # Adds link to the Sphinx-Needs configuration page
    'config_link': {
        'regex': r'^(?P<value>\w+)$',
        'link_url': 'https://sphinx-needs.readthedocs.io/en/latest/configuration.html#{{value | replace("_", "-")}}',
        'link_name': 'Sphinx-Needs docs for {{value | replace("_", "-") }}',
        'options': ['config']
    },
    # Links to the related github issue
    'github_link': {
        'regex': r'^(?P<value>\w+)$',
        'link_url': 'https://github.com/useblocks/sphinx-needs-demo/issues/{{value}}',
        'link_name': 'SN Demo #{{value}}',
        'options': ['github']
    },
    # Links to the related jira issue
    'jira_link': {
        'regex': r'^(?P<value>\w+)$',
        'link_url': 'https://useblocks.atlassian.net/browse/ADAS-{{value}}',
        'link_name': 'JIRA ADAS #{{value}}',
        'options': ['jira']
    }
}

needs_services = {
    'github-issues': {
        'url': 'https://api.github.com/',
        'need_type': 'swreq',
        'max_amount': 2,
        'max_content_lines': 20,
        'id_prefix': 'GH_ISSUE_'
    },
    'github-prs': {
        'url': 'https://api.github.com/',
        'need_type': 'impl',
        'max_amount': 2,
        'max_content_lines': 20,
        'id_prefix': 'GH_PR_'
    }
}

###############################################################################
# SPHINX-NEEDS Config END
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
    "offset": {
        "left": 0,
        "top": 0
    },
    "timeout": 0,
}

templates_path = ['_templates']

# List of files/folder to ignore.
# Sphinx builds all ``.rst`` files under ``/docs``, no matte if they are part
# of a toctree or not. So as we have some rst-templates, we need to tell Sphinx to ignore
# these files.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'demo_page_header.rst', 'demo_hints']

# We bring our own plantuml jar file.
# These options tell Sphinxcontrib-PlantUML we it can find this file.
local_plantuml_path = os.path.join(os.path.dirname(__file__), "utils", "plantuml-1.2022.14.jar")
plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
# plantuml_output_format = 'png'
plantuml_output_format = "svg_img"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster' # Sphinx Defaul Theme

# Set ``html_theme`` to ``sphinx_immaterial`` only, if we do NOT perform a PDF build.
if os.environ.get("PDF", 0) != 1:
   html_theme = 'sphinx_immaterial'

html_static_path = ['_static']

sphinx_immaterial_override_generic_admonitions = True

html_logo = "_images/sphinx-needs-logo.png"
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
    'custom.css',
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
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.from_string(src)
    #template = jinja2.Template(src, autoescape=True, environemnt=env)
    rendered = template.render(**app.config.html_context)
    source[0] = rendered
    os.chdir(old_cwd)

# This function allows us to register any kind of black magic for Sphinx :)
def setup(app):
    
    # We connect our jinja-function from above with the "source-read" event of Sphinx,
    # which gets called for every file before Sphinx starts to handle the file on its own.
    # This allows us to manipulate the content.
    app.connect("source-read", rstjinja)
