# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tasks'
copyright = '2025, zhipeng'
author = 'zhipeng'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_theme_options = {
    "announcement": "This is in development!",
}
html_static_path = ['_static']

# html_logo = "_static/logo.png"  # add later if you want
# html_theme_options = {
#     "sidebar_hide_name": True,
#     "light_logo": "logo-light.png",
#     "dark_logo": "logo-dark.png",
# }


# Enable extensions
extensions = [
    "myst_parser",                      # Markdown support
    "sphinx.ext.autodoc",              # Auto pull docstrings
    "sphinx.ext.napoleon",             # Google/Numpy style docstrings
    "sphinx_autodoc_typehints",        # Type hints in docs
]


# Allow both .rst and .md files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}



import os, json, pathlib

# ① add template dir & put panel into every sidebar
templates_path = ["_templates"]
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",    
        "sidebar/scroll-start.html",   
        "sidebar/task-meta.html",     
        "sidebar/scroll-end.html",   
        # any further items here would float on the left again
    ]
}

# conf.py
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]


# ② inject meta.json (if present) into Jinja context
def add_task_meta(app, pagename, templatename, context, doctree):
    md_path   = pathlib.Path(app.srcdir) / (pagename + ".md")
    meta_path = md_path.with_suffix(".meta.json")
    if meta_path.exists():
        context["task_meta"] = json.loads(meta_path.read_text())

def setup(app):
    app.connect("html-page-context", add_task_meta)