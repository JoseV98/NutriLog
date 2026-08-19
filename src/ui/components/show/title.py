import flet as ft

from config.constants import COLORS


@ft.component
def PageTitle(title: str):

    size = ft.context.page.height
    size = 30 if size is None or size < 30 else int(size * 0.1)
    return ft.Text(
        value=title,
        color=COLORS.main,
        size=size,
        weight=ft.FontWeight.BOLD,
    )


@ft.component
def SubTitle(text):
    size = ft.context.page.height
    size = 20 if size is None or size < 30 else int(size * 0.07)
    return ft.Text(
        value=text,
        color=COLORS.sec,
        size=size,
        weight=ft.FontWeight.BOLD,
    )
