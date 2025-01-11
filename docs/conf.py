from atsphinx.goto_top import __version__ as version
from atsphinx.mini18n import get_template_dir as get_mini18n_template_dir

# -- Project information
project = "atsphinx-goto-top"
copyright = "2025, Kazuya Takei"
author = "Kazuya Takei"
release = version

# -- General configuration
extensions = [
    # Bundled extensions
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    # Third-party extensions
    "atsphinx.mini18n",
    "sphinx_toolbox.confval",
    # This extension
    "atsphinx.goto_top",
]
templates_path = ["_templates", get_mini18n_template_dir()]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for i18n
gettext_compact = False
locale_dirs = ["_locales"]

# -- Options for HTML output
html_theme = "bulma-basic"
html_static_path = ["_static"]
html_title = f"{project} v{release}"
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
]
html_theme_options = {
    "navbar_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/atsphinx/goto-top/",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}

# -- Options for extensions
# sphinx.ext.intersphinx
intersphinx_mapping = {
    "sphinx": ("https://www.sphinx-doc.org/en/master", None),
}
# sphinx.ext.todo
todo_include_todos = True
# atsphinx.mini18n
mini18n_default_language = "en"
mini18n_support_languages = ["en", "ja"]
mini18n_basepath = "/goto-top/"
# atsphinx.goto_top
goto_top_design = "image"

html_static_path = []
templates_path = [get_mini18n_template_dir()]
