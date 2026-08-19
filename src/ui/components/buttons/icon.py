from typing import Callable

import flet as ft

from config.constants import COLORS


@ft.component
def IconTextButton(
    icon: ft.IconData,
    text: str,
    function: Callable,
):

    size = ft.context.page.height
    size = 10 if size is None or size < 10 else int(size * 0.035)

    return ft.Button(
        icon=ft.Icon(icon=icon, color=COLORS.aux_1, size=size),
        content=ft.Text(value=text, color=COLORS.aux_1, size=size),
        bgcolor=COLORS.sec,
        on_click=lambda: function(),
    )
