import flet as ft

from ui.colors.generator import text_color_generator
from ui.font import FONTS


def ViewTitle(
    text: str,
    bg_color: str,
    app_height: ft.Number,
    text_color: str | None = None,
):
    return ft.Text(
        value=text,
        size=app_height * 0.1,
        weight=ft.FontWeight.BOLD,
        color=text_color_generator(bg_color) if text_color is None else text_color,
        font_family="Title",
    )
