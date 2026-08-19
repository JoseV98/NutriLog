import flet as ft

from config.constants import COLORS


@ft.component
def TableTitle(text: str):
    size = ft.context.page.height
    size = 15 if size is None else int(size * 0.04)
    return ft.Text(
        value=text,
        color=COLORS.ctrs,
        size=size if size > 15 else 15,
        weight=ft.FontWeight.W_600,
    )
