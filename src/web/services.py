from src.typings import RawHTML, as_raw_html
from src.config import Config


config = Config()


def load_html(file_name: str) -> RawHTML:
    path = config.BASE_DIR / "src" / file_name
    return as_raw_html(path.read_text())
