from typing import Callable

import flet as ft
from postgrest.base_request_builder import C

from config.constants import COLORS


@ft.component
def FormButton(label: str, is_enabled: bool, on_click: Callable, loading: bool = False):

    return ft.Button(
        content=ft.Row(
            controls=[
                ft.ProgressRing(width=20, height=20, stroke_width=2, visible=loading),
                ft.Text(label, visible=not loading),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE_700 if is_enabled else ft.Colors.GREY_700,
        on_click=on_click,
        disabled=not is_enabled or loading,
        width=280,
    )


@ft.component
def HomePageButton(label: str, icon: ft.IconData, go_to: Callable):
    size = ft.context.page.height
    size = 30 if size is None or size < 30 else int(size * 0.1)
    return ft.Button(
        content=ft.Column(
            controls=[
                ft.Icon(
                    icon=icon,
                    color=COLORS.aux_1,
                    size=size,
                ),
                ft.Text(
                    value=label,
                    weight=ft.FontWeight.BOLD,
                    color=COLORS.aux_1,
                    size=int(size / 2),
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        on_click=lambda _: go_to(),
        style=ft.ButtonStyle(
            bgcolor=COLORS.main,
            padding=30,
        ),
    )


@ft.component
def IconTextButton(icon: ft.IconData, text: str, function: Callable):

    size = ft.context.page.height
    size = 10 if size is None or size < 10 else int(size * 0.035)

    return ft.Button(
        icon=ft.Icon(icon=icon, color=COLORS.aux_1, size=size),
        content=ft.Text(value=text, color=COLORS.aux_1, size=size),
        bgcolor=COLORS.sec,
        on_click=lambda: function(),
    )
