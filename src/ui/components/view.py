from typing import Callable

import flet as ft

from config.constants import COLORS
from config.user_config import UserContext
from ui.go_to import go_to_home, go_to_new_patient, go_to_patients


@ft.component
def MainView(path: str, appbar: ft.AppBar, controls: list[ft.BaseControl]):

    return ft.View(
        route=path,
        appbar=appbar,
        controls=controls,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        vertical_alignment=ft.MainAxisAlignment.START,
        bgcolor=COLORS.ctrs,
        padding=20,
    )


@ft.component
def MainAppbar(title: str, back: Callable | None = None):

    user = ft.use_context(UserContext)

    icon_bar = (
        ft.context.page.platform.is_mobile()
        if ft.context.page.platform is not None
        else True
    )
    leading: list[ft.Control] = []

    if back is not None:
        leading.append(
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=COLORS.ctrs,
                on_click=lambda _: back(),
            )
        )

    leading.append(
        ft.IconButton(
            icon=ft.Icons.HOME_ROUNDED,
            icon_color=COLORS.ctrs,
            on_click=lambda _: go_to_home(),
        )
    )

    actions: list[ft.Control] = (
        [
            ft.IconButton(
                icon=ft.Icons.PERSON_ADD,
                icon_color=COLORS.ctrs,
                on_click=lambda: go_to_new_patient(),
            ),
            ft.IconButton(
                icon=ft.Icons.BOOK_ROUNDED,
                icon_color=COLORS.ctrs,
                on_click=lambda: go_to_patients(),
            ),
        ]
        if icon_bar
        else [
            ft.TextButton(
                icon=ft.Icon(ft.Icons.PERSON_ADD, color=COLORS.ctrs),
                content=ft.Text(user.text["appbar"]["new"], color=COLORS.ctrs),
                style=ft.ButtonStyle(color=COLORS.ctrs),
                on_click=lambda: go_to_new_patient(),
            ),
            ft.TextButton(
                icon=ft.Icon(ft.Icons.BOOK_ROUNDED, color=COLORS.ctrs),
                content=ft.Text(user.text["appbar"]["log"], color=COLORS.ctrs),
                style=ft.ButtonStyle(color=COLORS.ctrs),
                on_click=lambda: go_to_patients(),
            ),
        ]
    )

    return ft.AppBar(
        leading=ft.Row(controls=leading),
        bgcolor=COLORS.main,
        actions=actions,
        title=ft.Text(value=title, color=COLORS.ctrs),
        center_title=True,
    )
