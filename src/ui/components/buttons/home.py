from typing import Callable

import flet as ft

from config.constants import COLORS


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
