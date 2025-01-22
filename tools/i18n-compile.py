#!/usr/bin/env python
"""Generate message objects."""

import logging
from pathlib import Path

from babel.messages.mofile import write_mo
from babel.messages.pofile import read_po

from atsphinx import goto_top  # type: ignore[import-untyped]

try:
    import tomllib  # type: ignore[import-not-found]
except ImportError:
    import tomli as tomllib  # type: ignore[import-not-found]

ROOT = Path(__file__).parents[1]

logger = logging.getLogger(__name__)


def compile_catalog(lang):
    """Generate MO-file from PO-file."""
    po_path = goto_top.locale_dir / lang / "LC_MESSAGES" / f"{goto_top.__name__}.po"
    mo_path = goto_top.locale_dir / lang / "LC_MESSAGES" / f"{goto_top.__name__}.mo"
    with po_path.open("rb") as fp:
        catalog = read_po(fp, locale=lang)
    with mo_path.open("wb") as fp:
        write_mo(fp, catalog)


def main():  # noqa: D103
    meta = tomllib.loads((ROOT / "pyproject.toml").read_text())
    for lang in meta["tool"]["i18n"]["languages"]:
        compile_catalog(lang)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    goto_top.locale_dir.mkdir(parents=True, exist_ok=True)
    main()
