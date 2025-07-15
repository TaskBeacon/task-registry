# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TaskBeacon'
copyright = '2025, Zhipeng Cao'
author = 'Zhipeng Cao'
release = ''
html_title = "TaskBeacon"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ['_static']


html_logo = "_static/logo-nobg.png"  # add later if you want
html_theme_options = {
    "sidebar_hide_name": True,
    # "light_logo": "logo-light.png",
    # "dark_logo": "logo-dark.png",
    "source_repository": "https://github.com/TaskBeacon/task-registry/",
    "source_branch": "main",
    "source_directory": "source/",
}

# Enable extensions
extensions = [
    "myst_parser",                      # Markdown support
    "sphinx.ext.autodoc",              # Auto pull docstrings
    "sphinx.ext.napoleon",             # Google/Numpy style docstrings
    "sphinx_autodoc_typehints",        # Type hints in docs
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
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
        "sidebar/search.html",       # pinned
        "sidebar/scroll-start.html", # begin scrollable
        "sidebar/entries.html",  
        "sidebar/navigation.html",    
        "sidebar/scroll-end.html",   # end scrollable
    ]
}

# conf.py
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]

import sys; 
sys.setrecursionlimit(200)