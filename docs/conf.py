# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
from importlib import metadata

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pubpypack-harmony-cindytsai'
copyright = '2023, Shin-Rong Tsai'
author = 'Shin-Rong Tsai'
PACKAGE_VERSION = metadata.version("pubpypack-harmony-cindytsai")
version = PACKAGE_VERSION
release = PACKAGE_VERSION

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']


# -- Read the Doc Hook -------------------------------------------------------
if os.environ.get("READTHEDOCS"):
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).parent.parent
    PACKAGE_ROOT = PROJECT_ROOT / "src" / "imppkg"

    def run_apidoc(_):
        from sphinx.ext import apidoc
        apidoc.main([
            "--force",
            "--implicit-namespaces",
            "--module-first",
            "--separate",
            "-o", str(PROJECT_ROOT / "docs" / "reference"),
            str(PACKAGE_ROOT),
            str(PACKAGE_ROOT / "*.c"),
            str(PACKAGE_ROOT / "*.so"),
        ])


    def setup(app):
        app.connect("builder-inited", run_apidoc)

