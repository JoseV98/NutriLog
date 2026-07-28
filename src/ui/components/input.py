import re
import flet as ft
from typing import Callable
from config.constants import COLORS


@ft.component
def InputText(
    label: str,
    placeholder: str,
    ref: ft.Ref[ft.TextField],
    valid_data: Callable,
    filter: ft.InputFilter | None = None,
    validate_regex: str = "",
    error_message: str = "",
    empty_valid: bool = False,
):

    message, set_message = ft.use_state("")
    value, set_value = ft.use_state("")
    is_valid, set_valid = ft.use_state(False)

    def on_change():
        valid = is_valid
        set_value(text.value)

        if not validate_regex:
            set_message("")
            valid = bool(empty_valid or text.value)
        else:
            try:
                if re.fullmatch(validate_regex, text.value):
                    set_message("")
                    valid = bool(empty_valid or text.value)

                else:
                    set_message(error_message)
                    valid = False

            except re.error:
                set_message("")
                valid = False

        if valid != is_valid:
            set_valid(valid)
            valid_data(valid)

    return ft.Column(
        controls=[
            text := ft.TextField(
                ref=ref,
                value=value,
                label=label,
                hint_text=placeholder,
                border_color=ft.Colors.GREY_400,
                focused_border_color=ft.Colors.BLUE_500,
                color=COLORS.text,
                input_filter=filter,
                on_change=on_change,
                suffix_icon=ft.Icons.ERROR if bool(message) else None,
            ),
            ft.Text(
                message,
                size=12,
                color=ft.Colors.RED,
                visible=bool(message),
            ),
        ],
        spacing=5,
    )


@ft.component
def InputPass(
    label: str,
    ref: ft.Ref[ft.TextField],
    valid_data: Callable,
    check_label: str = "",
    message_unmatch: str = "X",
    message_unvalid: str = r"A, a, 0, !@#$%^&*(),.?\":{}|<>",
):

    pass_value, set_password = ft.use_state("")
    check_value, set_check = ft.use_state("")
    message, set_message = ft.use_state("")
    is_valid, set_valid = ft.use_state(False)

    def valid_pass():
        set_password(password.value)

        valid = bool(password.value)

        if bool(check_label):
            set_check(check.value)
            validate_pass = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>])[A-Za-z\d!@#$%^&*(),.?\":{}|<>]{8,}$"

            if not re.fullmatch(validate_pass, password.value):
                valid = False
                if not bool(message == message_unvalid):
                    set_message(message_unvalid)

            elif password.value == check.value:
                if bool(message):
                    set_message("")

            else:
                if not bool(message == message_unmatch):
                    set_message(message_unmatch)
                valid = False

        if valid != is_valid:
            set_valid(valid)
            valid_data(valid)

    controls: list[ft.Control] = [
        password := ft.TextField(
            value=pass_value,
            ref=ref,
            label=label,
            hint_text="**********",
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
                hint_text="**********",
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

    return ft.Column(controls=controls, spacing=20)
