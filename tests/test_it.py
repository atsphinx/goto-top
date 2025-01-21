"""Standard tests."""

import pytest
from bs4 import BeautifulSoup  # type: ignore[import-untyped]
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__en(app: SphinxTestApp):
    """Test to pass."""
    app.build()
    assert (app.outdir / "_static" / "goto-top/main.js").exists()
    assert (app.outdir / "_static" / "goto-top/style.css").exists()
    soup = BeautifulSoup((app.outdir / "index.html").read_text(), "html.parser")
    assert soup.find("template", {"id": "tmpl_gotoTop"})
    template = soup.find("template", {"id": "tmpl_gotoTop"})
    assert "Back to top" in template.text


@pytest.mark.sphinx("html", confoverrides={"language": "ja"})
def test__ja(app: SphinxTestApp):
    """Test to pass."""
    app.build()
    assert (app.outdir / "_static" / "goto-top/main.js").exists()
    assert (app.outdir / "_static" / "goto-top/style.css").exists()
    soup = BeautifulSoup((app.outdir / "index.html").read_text(), "html.parser")
    assert soup.find("template", {"id": "tmpl_gotoTop"})
    template = soup.find("template", {"id": "tmpl_gotoTop"})
    assert "トップへ戻る" in template.text
