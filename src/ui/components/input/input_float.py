from typing import Callable

import flet as ft

from config.constants import NUMERIC_FORMAT, NUMERIC_VALUE
from config.user_config import UserContext
from ui.components.input.input_text import InputText
from ui.components.responsive_row_configuration import STANDARD


@ft.component
def InputFloat(
    label: str,
    placeholder: str,
    set_input_data: Callable,
    error_message: str = "",
    empty_valid: bool = False,
    visible: bool = True,
    unit: str = "",
    col_distribution: dict = STANDARD,
):
    user = ft.use_context(UserContext)
    error = (
        error_message
        if bool(error_message)
        else user.text["unvalid_field_messages"]["format_error"]
    )
    return InputText(
        label=label,
        set_input_data=set_input_data,
        placeholder=placeholder,
        validate_regex=NUMERIC_FORMAT,
        error_message=error,
        filter=ft.InputFilter(regex_string=NUMERIC_VALUE),
        empty_valid=empty_valid,
        visible=visible,
        unit=unit,
        col_distribution=col_distribution,
    )
