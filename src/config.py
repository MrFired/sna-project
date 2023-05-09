from pathlib import Path
from typing import Optional

from pydantic import BaseSettings

from src import ROOT_DIR


class Config(BaseSettings):
    PORT: int = 5000
    LOG_LEVEL: str = "info"

    STATIC_FILES: Optional[Path] = None

    class Config(BaseSettings.Config):
        env_file = ROOT_DIR / ".env"
