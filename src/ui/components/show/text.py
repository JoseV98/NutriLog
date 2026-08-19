import flet as ft

from config.constants import COLORS
from ui.components.responsive_row_configuration import STANDARD


@ft.component
def NormalText(text: str, col_distribution: dict = STANDARD):
    size = ft.context.page.height
    size = 15 if size is None else int(size * 0.03)
    return ft.Text(
        value=text,
        color=COLORS.text,
        size=size if size > 15 else 15,
        weight=ft.FontWeight.NORMAL,
        col=col_distribution,
    )
