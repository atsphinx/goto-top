"""Add navigation buttion that scroll to top of page."""

from pathlib import Path
from typing import Optional

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.config import Config

__version__ = "0.0.0"

here = Path(__file__).parent


def register_config(app: Sphinx, config: Config):
    """Add config values for using extension."""
    config.templates_path.append(str(here / "templates"))
    config.html_static_path.append(str(here / "static"))
    config.html_js_files.append("goto-top/main.js")
    config.html_css_files.append("goto-top/style.css")


def append_template_element(
    app: Sphinx,
    pagename: str,
    templatename: str,
    context: dict,
    doctree: Optional[nodes.document],
) -> None:
    """Inject <template> into metadata."""
    context.setdefault("metatags", "")
    context["metatags"] += app.builder.templates.render(
        "goto-top/navigation.html", context
    )


def setup(app: Sphinx):  # noqa: D103
    app.connect("config-inited", register_config)
    app.connect("html-page-context", append_template_element)
    return {
        "version": __version__,
        "env_version": 1,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
