from typing import Callable

import flet as ft

from ui.components.responsive_row_configuration import ALL_OR_HALF
from ui.styles.texts import NORMAL


@ft.component
def InputMultiLineText(
    label: str,
    set_input_data: Callable,
    visible: bool = True,
    init_value: str = "",
    col_distribution: dict = ALL_OR_HALF,
):
    value, set_value = ft.use_state(init_value)

    def on_change(value):
        set_value(value)
        set_input_data(value)

    return ft.TextField(
        label=label,
        value=value,
        on_change=lambda e: on_change(e.control.value),
        visible=visible,
        multiline=True,
        min_lines=5,
        max_lines=10,
        text_style=NORMAL,
        expand=True,
        col=col_distribution,
    )
