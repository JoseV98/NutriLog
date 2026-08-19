from typing import Callable

import flet as ft

from ui.components.responsive_row_configuration import SMALL
from ui.styles.texts import NORMAL


@ft.component
def SimpleSwitch(
    value: bool,
    label: str,
    on_change_data: Callable,
    is_visible: bool = True,
):

    def on_change():
        on_change_data(not value)

    return ft.Container(
        content=ft.Switch(
            value=value,
            label=label,
            label_text_style=NORMAL,
            on_change=on_change,
            visible=is_visible,
        ),
        col=SMALL,
    )
