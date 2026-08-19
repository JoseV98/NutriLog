import flet as ft


@ft.component
def ErrorText(error: str):
    return ft.Text(
        error,
        size=12,
        color=ft.Colors.RED,
        visible=bool(error),
    )
