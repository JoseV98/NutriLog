from datetime import date
import re
import flet as ft
from typing import Callable
from config.constants import COLORS, NUMERIC_FORMAT, NUMERIC_VALUE
from config.user_config import UserContext
from ui.styles.texts import NORMAL


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
):

    message, set_message = ft.use_state("")
    value, set_value = ft.use_state("")

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

    return ft.Container(
        content=ft.Column(
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
                    col={},
                ),
                ft.Text(
                    message,
                    size=12,
                    color=ft.Colors.RED,
                    visible=bool(message),
                ),
            ],
            spacing=5,
        ),
        col={
            ft.ResponsiveRowBreakpoint.XS: 12,
            ft.ResponsiveRowBreakpoint.SM: 6,
            ft.ResponsiveRowBreakpoint.MD: 4,
            ft.ResponsiveRowBreakpoint.LG: 3,
        },
        visible=visible,
    )


@ft.component
def InputFloat(
    label: str,
    placeholder: str,
    set_input_data: Callable,
    error_message: str = "",
    empty_valid: bool = False,
    visible: bool = True,
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
    )


@ft.component
def InputPass(
    label: str,
    set_input_pass: Callable,
    check_label: str = "",
    message_unmatch: str = "X",
    message_unvalid: str = r"A, a, 0, !@#$%^&*(),.?\":{}|<>",
):

    pass_value, set_password = ft.use_state("")
    check_value, set_check = ft.use_state("")
    message, set_message = ft.use_state("")

    def valid_pass():
        password_value = password.value
        set_password(password_value)
        valid = True

        if bool(check_label):
            set_check(check.value)
            validate_pass = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>])[A-Za-z\d!@#$%^&*(),.?\":{}|<>]{8,}$"

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


@ft.component
def InputDate(init_date_value: str, on_change_date: Callable):
    user = ft.use_context(UserContext)

    today = date.today()

    text_date, set_text_date = ft.use_state(init_date_value)
    calendar_date, set_calendar_date = ft.use_state(today)

    def chage_date():

        new_date = calendar.value

        if new_date and calendar_date != new_date:
            set_calendar_date(new_date)  # type: ignore
            set_text_date(new_date.strftime("%d/%m/%Y"))
            on_change_date(new_date)

    calendar = ft.DatePicker(
        locale=ft.Locale(user.language),
        last_date=today,
        first_date=date(year=today.year - 150, month=today.month, day=today.day),
        current_date=calendar_date,
        on_change=chage_date,
        on_dismiss=chage_date,
    )

    return ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.CALENDAR_MONTH,
                    on_click=lambda _: ft.context.page.show_dialog(calendar),
                ),
                ft.Text(
                    value=text_date,
                    color=COLORS.text,
                ),
            ],
        ),
        col={
            ft.ResponsiveRowBreakpoint.XS: 12,
            ft.ResponsiveRowBreakpoint.SM: 6,
            ft.ResponsiveRowBreakpoint.MD: 4,
            ft.ResponsiveRowBreakpoint.LG: 3,
        },
    )


@ft.component
def SimpleSwitch(
    value: bool, label: str, on_change_data: Callable, is_visible: bool = True
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
        col={
            ft.ResponsiveRowBreakpoint.XS: 12,
            ft.ResponsiveRowBreakpoint.SM: 6,
            ft.ResponsiveRowBreakpoint.MD: 4,
            ft.ResponsiveRowBreakpoint.LG: 3,
            ft.ResponsiveRowBreakpoint.XL: 2,
            ft.ResponsiveRowBreakpoint.XXL: 1,
        },
    )


@ft.component
def InputMultiLineText(label: str, set_input_data: Callable, visible: bool = True):
    value, set_value = ft.use_state("")

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
    )
