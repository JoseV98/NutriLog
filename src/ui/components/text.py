import flet as ft

from config.constants import COLORS


@ft.component
def Title(text):
    return ft.Text(
        value=text,
        size=28,
        weight=ft.FontWeight.BOLD,
        color=COLORS.text,
    )


@ft.component
def SubTitle(text):
    return ft.Text(
        value=text,
        size=16,
        weight=ft.FontWeight.BOLD,
        color=COLORS.text,
    )
