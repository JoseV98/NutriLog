import flet as ft

from config.constants import COLORS


@ft.component
def SuccessWrongText(wrong: str, success: str):
    return ft.Column(
        controls=[
            ft.Text(
                wrong,
                size=12,
                color=ft.Colors.RED,
                visible=bool(wrong),
            ),
            ft.Text(
                success,
                size=12,
                color=ft.Colors.GREEN,
                visible=bool(success),
            ),
        ]
    )
