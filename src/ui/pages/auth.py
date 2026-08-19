import asyncio
import re

import flet as ft
from supabase import AuthApiError

from config.constants import COLORS, EMAIL_FORMAT, NO_SPACE
from config.user_config import UserContext
from database.connect import db_login, db_register
from ui.components.buttons.form import FormButton
from ui.components.container.box import RoundedBox
from ui.components.container.column import NormalColumn, ScrollColumn
from ui.components.input.input_password import InputPass
from ui.components.input.input_text import InputText
from ui.components.show.success_or_wrong import SuccessWrongText
from ui.components.text import SubTitle, Title
from ui.go_to import go_to_home, go_to_login, go_to_register


@ft.component
def SignLayout():
    user = ft.use_context(UserContext)
    outlet = ft.use_route_outlet()

    return ft.View(
        route=ft.use_view_path(),
        controls=[
            RoundedBox(
                NormalColumn(controls=[Title(user.text["login"]["title"]), outlet])
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        bgcolor=COLORS.main,
        padding=20,
    )


@ft.component
def LoginPage():

    user = ft.use_context(UserContext)

    email_value, set_email_value = ft.use_state("")
    pass_value, set_pass_value = ft.use_state("")

    wrong_login, set_wrong = ft.use_state("")
    loading, set_loading = ft.use_state(False)
    success_login, set_success = ft.use_state("")

    async def sign_in():

        set_loading(True)

        try:
            result = await asyncio.to_thread(db_login, email_value, pass_value)

            set_success(user.text["login"]["success_login"])

            await user.save_logged(result)

            go_to_home()

        except AuthApiError as e:
            if re.fullmatch(e.message, "Invalid login credentials"):
                set_wrong(user.text["login"]["wrong_credentials"])
            else:
                set_wrong(user.text["errors"]["register"])
        except Exception:
            set_wrong(user.text["errors"]["general"])
        finally:
            set_loading(False)

    return ScrollColumn(
        controls=[
            SubTitle(user.text["login"]["login"]),
            InputText(
                label=user.text["login"]["email"],
                placeholder=user.text["placeholder"]["email"],
                set_input_data=set_email_value,
                filter=ft.InputFilter(NO_SPACE, allow=False),
                validate_regex=EMAIL_FORMAT,
                error_message=user.text["unvalid_field_messages"]["email_error"],
            ),
            InputPass(label=user.text["login"]["pass"], set_input_pass=set_pass_value),
            SuccessWrongText(wrong=wrong_login, success=success_login),
            FormButton(
                label=user.text["login"]["sign_in_button"],
                is_enabled=bool(email_value) and bool(pass_value),
                on_click=sign_in,
                loading=loading,
            ),
            ft.TextButton(
                content=user.text["login"]["sign_up_link"],
                on_click=lambda: go_to_register(),
                style=ft.ButtonStyle(color=ft.Colors.BLUE_500),
            ),
        ],
    )


@ft.component
def RegisterPage():

    user = ft.use_context(UserContext)

    name_value, set_name_value = ft.use_state("")
    email_value, set_email_value = ft.use_state("")
    pass_value, set_pass_value = ft.use_state("")

    wrong_register, set_wrong = ft.use_state("")
    loading, set_loading = ft.use_state(False)
    success_register, set_success = ft.use_state("")

    async def sign_up():
        set_loading(True)

        try:
            result = await asyncio.to_thread(
                db_register, name=name_value, email=email_value, password=pass_value
            )

            set_success(user.text["login"]["success_register"])

            await user.save_logged(result)

            go_to_home()

        except AuthApiError as e:
            if re.fullmatch(e.message, "User already registered"):
                set_wrong(user.text["login"]["used_email"])
            else:
                set_wrong(user.text["errors"]["register"])
        except Exception:
            set_wrong(user.text["errors"]["general"])
        finally:
            set_loading(False)

    return ft.Column(
        expand=True,
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            SubTitle(user.text["login"]["register"]),
            ScrollColumn(
                controls=[
                    InputText(
                        label=user.text["login"]["name"], set_input_data=set_name_value
                    ),
                    InputText(
                        label=user.text["login"]["email"],
                        placeholder="email@email.com",
                        set_input_data=set_email_value,
                        filter=ft.InputFilter(NO_SPACE, allow=False),
                        validate_regex=EMAIL_FORMAT,
                        error_message=user.text["unvalid_field_messages"][
                            "email_error"
                        ],
                    ),
                    InputPass(
                        label=user.text["login"]["pass"],
                        set_input_pass=set_pass_value,
                        check_label=user.text["login"]["check_pass"],
                        message_unvalid=user.text["unvalid_field_messages"][
                            "unvalid_password"
                        ],
                        message_unmatch=user.text["unvalid_field_messages"][
                            "unmatch_password"
                        ],
                    ),
                    SuccessWrongText(wrong=wrong_register, success=success_register),
                ],
            ),
            FormButton(
                label=user.text["login"]["sign_up_button"],
                is_enabled=bool(email_value) and bool(pass_value) and bool(name_value),
                on_click=sign_up,
                loading=loading,
            ),
            ft.TextButton(
                content=user.text["login"]["sign_in_link"],
                on_click=lambda: go_to_login(),
                style=ft.ButtonStyle(color=ft.Colors.BLUE_500),
            ),
        ],
    )
