import re
from typing import Callable

import flet as ft

from config.constants import COLORS
from config.regex import PASS_REGEX
from config.user_config import UserContext
from ui.components.responsive_row_configuration import STANDARD


@ft.component
def InputPass(
    label: str,
    set_input_pass: Callable,
    check_label: str = "",
    message_unmatch: str = "X",
    message_unvalid: str = r"A, a, 0, !@#$%^&*(),.?\":{}|<>",
    col_distribution: dict = STANDARD,
):
    user = ft.use_context(UserContext)

    pass_value, set_password = ft.use_state("")
    check_value, set_check = ft.use_state("")
    message, set_message = ft.use_state("")

    def valid_pass():
        password_value = password.value
        set_password(password_value)
        valid = True

        if bool(check_label):
            set_check(check.value)
            validate_pass = PASS_REGEX

            if not re.fullmatch(validate_pass, password.value):
                valid = False
                set_message(message_unvalid)

            elif password.value == check.value:
                set_message("")

            else:
                set_message(message_unmatch)
                valid = False

        set_input_pass(password.value if valid else "")

    controls: list[ft.Control] = [
        password := ft.TextField(
            value=pass_value,
            label=label,
            hint_text=user.text["placeholder"]["pass"],
            password=True,
            can_reveal_password=True,
            border_color=ft.Colors.GREY_400,
            focused_border_color=ft.Colors.BLUE_500,
            color=COLORS.text,
            on_change=valid_pass,
            input_filter=ft.InputFilter(r"^\S*$", allow=False),
        )
    ]

    if check_label:
        controls.append(
            check := ft.TextField(
                value=check_value,
                label=check_label,
                hint_text=user.text["placeholder"]["pass"],
                password=True,
                can_reveal_password=True,
                border_color=ft.Colors.GREY_400,
                focused_border_color=ft.Colors.BLUE_500,
                color=COLORS.text,
                on_change=valid_pass,
                input_filter=ft.InputFilter(r"^\S*$", allow=False),
            )
        )
    controls.append(
        ft.Text(
            message,
            size=12,
            color=ft.Colors.RED,
            visible=bool(message),
        )
    )

    return ft.Column(controls=controls, spacing=20, col=col_distribution)
