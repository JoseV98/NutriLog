import json
from dataclasses import dataclass

from config.constants import PATHS


@dataclass(frozen=True)
class Colors:
    with open(
        PATHS.APP_ASSETS / "default_colors.json", "r", encoding="utf-8"
    ) as colors:
        palette = json.load(colors)

    main = palette["main"]
    main_dark = palette["main_dark"]
    main_darker = palette["main_darker"]
    main_darkest = palette["main_darkest"]
    main_light = palette["main_light"]
    main_lighter = palette["main_lighter"]
    main_soft = palette["main_soft"]
    main_whisper = palette["main_whisper"]

    secundary = palette["secundary"]
    secundary_dark = palette["secundary_dark"]
    secundary_darker = palette["secundary_darker"]
    secundary_light = palette["secundary_light"]
    secundary_lighter = palette["secundary_lighter"]
    secundary_soft = palette["secundary_soft"]

    auxiliary = palette["auxiliary"]
    auxiliary_dark = palette["auxiliary_dark"]
    auxiliary_light = palette["auxiliary_light"]
    auxiliary_soft = palette["auxiliary_soft"]

    auxiliary2 = palette["auxiliary2"]
    auxiliary2_dark = palette["auxiliary2_dark"]
    auxiliary2_light = palette["auxiliary2_light"]

    auxiliary3 = palette["auxiliary3"]
    auxiliary3_dark = palette["auxiliary3_dark"]
    auxiliary3_light = palette["auxiliary3_light"]

    background = palette["background"]
    background_alt = palette["background_alt"]
    surface = palette["surface"]
    surface_variant = palette["surface_variant"]
    surface_elevated = palette["surface_elevated"]
    surface_sunken = palette["surface_sunken"]
    overlay = palette["overlay"]

    border = palette["border"]
    border_strong = palette["border_strong"]
    divider = palette["divider"]
    divider_soft = palette["divider_soft"]

    shadow = palette["shadow"]
    shadow_soft = palette["shadow_soft"]
    shadow_medium = palette["shadow_medium"]
    shadow_strong = palette["shadow_strong"]

    contrast = palette["contrast"]
    contrast_soft = palette["contrast_soft"]

    success = palette["success"]
    success_dark = palette["success_dark"]
    success_light = palette["success_light"]
    success_soft = palette["success_soft"]

    warning = palette["warning"]
    warning_dark = palette["warning_dark"]
    warning_light = palette["warning_light"]
    warning_soft = palette["warning_soft"]

    error = palette["error"]
    error_dark = palette["error_dark"]
    error_light = palette["error_light"]
    error_soft = palette["error_soft"]

    info = palette["info"]
    info_dark = palette["info_dark"]
    info_light = palette["info_light"]
    info_soft = palette["info_soft"]

    lime = palette["lime"]
    emerald = palette["emerald"]
    teal = palette["teal"]
    cyan = palette["cyan"]
    mint = palette["mint"]
    olive = palette["olive"]
    sage = palette["sage"]
    basil = palette["basil"]
    matcha = palette["matcha"]
    avocado = palette["avocado"]
    terracotta = palette["terracotta"]
    amber = palette["amber"]
    orange = palette["orange"]
    carrot = palette["carrot"]
    tomato = palette["tomato"]
    beet = palette["beet"]
    grape = palette["grape"]
    blueberry = palette["blueberry"]
    rose = palette["rose"]
    indigo = palette["indigo"]
    slate = palette["slate"]
    gray = palette["gray"]


COLORS = Colors()
