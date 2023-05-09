from pathlib import Path

from src.typings import RawHTML, as_raw_html


def load_html(path: Path) -> RawHTML:
    return as_raw_html(path.read_text())
