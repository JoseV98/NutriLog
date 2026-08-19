import re

import flet as ft
from typing import Callable

from config.constants import COLORS
from ui.components.responsive_row_configuration import STANDARD
from ui.components.show.error_text import ErrorText


@ft.component
def InputText(
    label: str,
    set_input_data: Callable,
    placeholder: str = "",
    filter: ft.InputFilter | None = None,
    validate_regex: str = "",
    error_message: str = "",
    empty_valid: bool = False,
    visible: bool = True,
    unit: str = "",
    col_distribution: dict = STANDARD,
    init_value: str = "",
):

    message, set_message = ft.use_state("")
    value, set_value = ft.use_state(init_value)

    def on_change():

        input_value = text.value

        set_value(input_value)

        if not validate_regex:
            valid = bool(empty_valid or input_value)
        else:
            try:
                if re.fullmatch(validate_regex, input_value):
                    set_message("")
                    valid = bool(empty_valid or input_value)

                else:
                    set_message(error_message)
                    valid = False

            except re.error:
                set_message("")
                valid = False

        set_input_data(input_value if valid else "")

    controls = (
        ft.Row(
            controls=[
                text := ft.TextField(
                    label=label,
                    value=value,
                    hint_text=placeholder,
                    border_color=ft.Colors.GREY_400,
                    focused_border_color=ft.Colors.BLUE_500,
                    color=COLORS.text,
                    input_filter=filter,
                    on_change=on_change,
                    suffix_icon=ft.Icons.ERROR if bool(message) else None,
                ),
                ft.Text(
                    value=unit,
                    color=COLORS.text,
                    visible=bool(unit),
                    weight=ft.FontWeight.BOLD,
                    size=20,
                ),
            ]
        )
        if unit
        else (
            text := ft.TextField(
                label=label,
                value=value,
                hint_text=placeholder,
                border_color=ft.Colors.GREY_400,
                focused_border_color=ft.Colors.BLUE_500,
                color=COLORS.text,
                input_filter=filter,
                on_change=on_change,
                suffix_icon=ft.Icons.ERROR if bool(message) else None,
            )
        )
    )

    return ft.Column(
        controls=[
            controls,
            ErrorText(message),
        ],
        spacing=5,
        col=col_distribution,
        visible=visible,
    )
