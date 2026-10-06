import flet as ft

from ui.components.row_responsive_sizes import ALL, STANDARD
from ui.router import UserContext


def StandarContainer(
    content: ft.Control,
    alignment: ft.Alignment = ft.Alignment.TOP_LEFT,
    bgcolor: None | str = None,
    padding: ft.PaddingValue = 0,
    margin: ft.MarginValue = 0,
    border_radius: ft.BorderRadiusValue = 0,
    row_size: dict = STANDARD,
):

    return ft.Container(
        content=content,
        bgcolor=bgcolor,
        padding=padding,
        margin=margin,
        alignment=alignment,
        expand=True,
        border_radius=border_radius,
        col=row_size,
    )


@ft.component
def NormalColumn(
    controls: list[ft.Control],
    col_distribution: dict = ALL,
    is_visible: bool = True,
    spacing: int | None = None,
    margin: ft.MarginValue = 0,
):
    user = ft.use_context(UserContext)
    if spacing is None:
        spacing = int(user.get_height() * (0.005 if user.is_mobile else 0.01))

    return ft.Column(
        controls=controls,
        spacing=spacing,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        col=col_distribution,
        visible=is_visible,
        margin=margin,
        expand=True,
    )
