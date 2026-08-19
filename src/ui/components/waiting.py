import flet as ft

from config.constants import COLORS


@ft.component
def LoadingPage():
    return ft.Container(
        ft.ProgressRing(),
        alignment=ft.alignment.Alignment.CENTER,
        expand=True,
    )


@ft.component
def LoadingRing(text: str, is_loading: bool):
    return ft.Column(
        visible=is_loading,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.ProgressRing(
                width=60,
                height=60,
                stroke_width=6,
                color=COLORS.main,
            ),
            ft.Text(
                value=text,
                color=COLORS.text,
                size=16,
                weight=ft.FontWeight.W_500,
            ),
        ],
    )
