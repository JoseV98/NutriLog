import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Paths:
    APP_ROOT: Path = Path(__file__).resolve().parent.parent
    APP_ASSETS: Path = APP_ROOT / "assets"
    APP_FONTS: Path = APP_ASSETS / "fonts"
    APP_TEXT: Path = APP_ASSETS / "text"


PATHS = Paths()

load_dotenv(PATHS.APP_ROOT / ".env")


@dataclass(frozen=True)
class DatabaseConst:
    URL: str = os.getenv("DATABASE_URL", "")
    KEY: str = os.getenv("DATABASE_KEY", "")


DB = DatabaseConst()
