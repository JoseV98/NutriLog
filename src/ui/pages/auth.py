import asyncio
import re

import flet as ft
from supabase import AuthApiError

from config.constants import COLORS, EMAIL_FORMAT, NO_SPACE
from config.user_config import UserContext
from database.connect import db_login, db_register
from ui.components.buttons import FormButton
from ui.components.input import InputPass, InputText
from ui.components.show import SuccessWrongText
from ui.components.text import SubTitle, Title


@ft.component
def SignLayout():
    user = ft.use_context(UserContext)
    outlet = ft.use_route_outlet()

    return ft.View(
        route=ft.use_view_path(),
        controls=[
            ft.Container(
                padding=50,
                bgcolor=ft.Colors.WHITE,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=15,
                    color=ft.Colors.GREY_300,
                ),
                content=ft.Column(
                    spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[Title(user.text["login"]["title"]), outlet],
                ),
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        bgcolor=COLORS.main,
        padding=20,
    )


@ft.component
def LoginPage():

    user = ft.use_context(UserContext)
    email_ref = ft.Ref[ft.TextField]()
    pass_ref = ft.Ref[ft.TextField]()

    is_email_valid, set_email_valid = ft.use_state(False)
    is_pass_valid, set_pass_valid = ft.use_state(False)

    wrong_login, set_wrong = ft.use_state("")
    loading, set_loading = ft.use_state(False)
    success_login, set_success = ft.use_state("")

    async def sign_in():

        set_loading(True)

        email_value = email_ref.current.value if email_ref.current else ""
        pass_value = pass_ref.current.value if pass_ref.current else ""

        try:
            result = await asyncio.to_thread(db_login, email_value, pass_value)

            set_success(user.text["login"]["success_login"])

            await user.save_logged(result)

            ft.context.page.navigate("/")

        except AuthApiError as e:
            if re.fullmatch(e.message, "Invalid login credentials"):
                set_wrong(user.text["login"]["wrong_credentials"])
            else:
                set_wrong(user.text["errors"]["register"])
        except Exception:
            set_wrong(user.text["errors"]["general"])
        finally:
            set_loading(False)

    return ft.Column(
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            SubTitle(user.text["login"]["login"]),
            InputText(
                label=user.text["login"]["email"],
                placeholder="email@email.com",
                ref=email_ref,
                valid_data=set_email_valid,
                filter=ft.InputFilter(NO_SPACE, allow=False),
                validate_regex=EMAIL_FORMAT,
                error_message=user.text["unvalid_field_messages"]["email_error"],
            ),
            InputPass(
                label=user.text["login"]["pass"],
                ref=pass_ref,
                valid_data=set_pass_valid,
            ),
            SuccessWrongText(wrong=wrong_login, success=success_login),
            FormButton(
                label=user.text["login"]["sign_in_button"],
                is_enabled=is_email_valid and is_pass_valid,
                on_click=sign_in,
                loading=loading,
            ),
            ft.TextButton(
                content=user.text["login"]["sign_up_link"],
                on_click=lambda: ft.context.page.navigate("/auth/register"),
                style=ft.ButtonStyle(color=ft.Colors.BLUE_500),
            ),
        ],
    )


@ft.component
def RegisterPage():

    user = ft.use_context(UserContext)
    email_ref = ft.Ref[ft.TextField]()
    pass_ref = ft.Ref[ft.TextField]()

    is_email_valid, set_email_valid = ft.use_state(False)
    is_pass_valid, set_pass_valid = ft.use_state(False)

    wrong_register, set_wrong = ft.use_state("")
    loading, set_loading = ft.use_state(False)
    success_register, set_success = ft.use_state("")

    async def sign_up():
        set_loading(True)

        email_value = email_ref.current.value if email_ref.current else ""
        pass_value = pass_ref.current.value if pass_ref.current else ""

        try:
            result = await asyncio.to_thread(db_register, email_value, pass_value)

            set_success(user.text["login"]["success_register"])

            await user.save_logged(result)

            ft.context.page.navigate("/")

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
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            SubTitle(user.text["login"]["register"]),
            InputText(
                label=user.text["login"]["email"],
                placeholder="email@email.com",
                ref=email_ref,
                valid_data=set_email_valid,
                filter=ft.InputFilter(NO_SPACE, allow=False),
                validate_regex=EMAIL_FORMAT,
                error_message=user.text["unvalid_field_messages"]["email_error"],
            ),
            InputPass(
                label=user.text["login"]["pass"],
                ref=pass_ref,
                valid_data=set_pass_valid,
                check_label=user.text["login"]["check_pass"],
                message_unvalid=user.text["unvalid_field_messages"]["unvalid_password"],
                message_unmatch=user.text["unvalid_field_messages"]["unmatch_password"],
            ),
            SuccessWrongText(wrong=wrong_register, success=success_register),
            FormButton(
                label=user.text["login"]["sign_up_button"],
                is_enabled=is_email_valid and is_pass_valid,
                on_click=sign_up,
                loading=loading,
            ),
            ft.TextButton(
                content=user.text["login"]["sign_in_link"],
                on_click=lambda: ft.context.page.navigate("/auth/login"),
                style=ft.ButtonStyle(color=ft.Colors.BLUE_500),
            ),
        ],
    )
