import flet as ft

from config.user_config import UserContext
from ui.components.container import StandarContainer


@ft.component
def CenterView(
    path: str,
    content: ft.Control,
    bg_color: None | str = None,
    appbar: ft.AppBar | None = None,
):
    user = ft.use_context(UserContext)

    return ft.View(
        route=path,
        appbar=appbar,
        controls=[
            StandarContainer(
                content=content,
                alignment=ft.Alignment.CENTER,
                bgcolor=bg_color,
                padding=user.get_height() * (0.025 if user.is_mobile else 0.05),
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.START,
        vertical_alignment=ft.MainAxisAlignment.START,
        padding=0,
    )
