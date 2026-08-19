import flet as ft

from config.constants import COLORS


@ft.component
def RoundedBox(
    content: ft.Control,
    bgcolor: str = COLORS.ctrs,
    shadow: str = COLORS.aux_1,
):
    return ft.Container(
        expand=True,
        padding=50,
        bgcolor=bgcolor,
        border_radius=10,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=shadow,
        ),
        content=content,
    )
