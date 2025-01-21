#!/usr/bin/env python
"""Generate message catalog of extension."""

import logging
from copy import deepcopy
from pathlib import Path

import tomli
from babel.messages.catalog import Catalog
from babel.messages.extract import extract_from_dir
from babel.messages.pofile import read_po, write_po

from atsphinx import goto_top  # type: ignore[import-untyped]

ROOT = Path(__file__).parents[1]

logger = logging.getLogger(__name__)


def create_pot(project: str, version: str, root: Path) -> Catalog:
    """Make POT file for i18n catalog."""
    logger.debug("Create POT file from sources.")
    catalog = Catalog(project=project, version=version, charset="utf-8")
    for filename, lineno, message, comments, context in extract_from_dir(root):
        catalog.add(message, locations=[(filename, lineno)])

    return catalog


def sync_catalog(pot: Catalog, lang: str):
    """Create or update PO-file for language."""
    po_path = goto_top.locale_dir / lang / "LC_MESSAGES" / f"{goto_top.__name__}.po"
    po_path.parent.mkdir(parents=True, exist_ok=True)

    if po_path.exists():
        logger.info("PO file exists. Load from file.")
        with po_path.open(encoding="utf-8") as fp:
            catalog = read_po(fp, locale=lang)
    else:
        logger.info("PO file is not found. Create new file.")
        catalog = deepcopy(pot)
        catalog.locale = lang

    catalog.update(pot)
    with po_path.open("wb") as out:
        write_po(out, catalog)


def main():  # noqa: D103
    meta = tomli.loads((ROOT / "pyproject.toml").read_text())
    project_name = meta["project"]["name"]
    project_version = meta["project"]["version"]
    current = create_pot(project_name, project_version, Path(goto_top.__file__).parent)
    for lang in meta["tool"]["i18n"]["languages"]:
        sync_catalog(current, lang)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    goto_top.locale_dir.mkdir(parents=True, exist_ok=True)
    main()
