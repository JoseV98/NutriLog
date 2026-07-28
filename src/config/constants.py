import json
import os

from dotenv import load_dotenv
from pathlib import Path
from dataclasses import dataclass


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


@dataclass(frozen=True)
class WebKey:
    PUBLIC: str = os.getenv("WEB_PUBLIC_KEY", "")
    WRAP_KEY: str = os.getenv("WEB_WRAP_KEY", "")
    WRAP_KEY_IV: str = os.getenv("WEB_WRAP_KEY_IV", "")


@dataclass(frozen=True)
class Colors:
    with open(PATHS.APP_ASSETS / "colors.json", "r", encoding="utf-8") as colors:
        palette = json.load(colors)
    main = palette["main"]
    sec = palette["secundary"]
    aux_1 = palette["auxiliary"]
    aux_2 = palette["auxiliary2"]
    aux_3 = palette["auxiliary3"]
    ctrs = palette["contrast"]
    text = palette["main_text"]


COLORS = Colors()
DB = DatabaseConst()

# Regex
NO_SPACE = r"^\S*$"
EMAIL_FORMAT = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
