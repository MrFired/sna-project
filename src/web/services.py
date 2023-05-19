from src import ROOT_DIR
from src.config import Config
from src.typings import RawHTML, as_raw_html


def load_html(file_name: str, config: Config) -> RawHTML:
    path = ROOT_DIR / config.STATIC_FILES / file_name
    return as_raw_html(path.read_text())
