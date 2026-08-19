import flet as ft

from config.constants import COLORS


@ft.component
def EmptyData(text: str):
    size = ft.context.page.height
    size = 25 if size is None else int(size * 0.08)
    return ft.Text(
        value=text,
        color=COLORS.aux_2,
        size=size if size > 25 else 25,
        weight=ft.FontWeight.W_500,
        margin=10,
    )
