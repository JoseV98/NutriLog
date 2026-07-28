from typing import Callable

import flet as ft


@ft.component
def FormButton(label: str, is_enabled: bool, on_click: Callable, loading: bool = False):

    return ft.Button(
        content=ft.Row(
            controls=[
                ft.ProgressRing(width=20, height=20, stroke_width=2, visible=loading),
                ft.Text(label, visible=not loading),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLUE_700 if is_enabled else ft.Colors.GREY_700,
        on_click=on_click,
        disabled=not is_enabled or loading,
        width=280,
    )
