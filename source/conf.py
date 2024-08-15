import os
import sys

# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath('../'))

# Add specific subdirectories to sys.path if needed
sys.path.insert(0, os.path.abspath('../views'))
sys.path.insert(0, os.path.abspath('../classes'))
sys.path.insert(0, os.path.abspath('../databaseFiles'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TheHaroldHotel'
copyright = '2024, Harold Flint, Mariia Kim, Macy Varga, Jonathan Aghachi'
author = 'Harold Flint, Mariia Kim, Macy Varga, Jonathan Aghachi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # For Google-style docstrings
    'sphinx.ext.viewcode',  # To add links to the source code
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
