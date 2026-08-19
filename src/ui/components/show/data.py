import flet as ft

from config.constants import COLORS
from config.user_config import UserContext
from ui.components.buttons.simple_switch import SimpleSwitch
from ui.components.responsive_row_configuration import ALL_OR_HALF, STANDARD
from ui.components.show.text import NormalText


@ft.component
def NormalData(
    label: str, data: str, unit: str = "", col_distribution: dict = STANDARD
):

    size = ft.context.page.height
    text_size = 15

    if size is not None:
        size = int(size * 0.03)
        text_size = size if size > 15 else 15

    controls: list[ft.Control] = [
        ft.Text(
            value=f"{label}:",
            color=COLORS.text,
            size=text_size + 2,
            weight=ft.FontWeight.W_600,
            col=ALL_OR_HALF,
        ),
        ft.Text(
            value=f"{data} {unit}" if bool(unit) else data,
            color=COLORS.text,
            size=text_size,
            weight=ft.FontWeight.NORMAL,
            col=ALL_OR_HALF,
        ),
    ]

    return ft.ResponsiveRow(controls=controls, col=col_distribution)


@ft.component
def BlockData(label: str, data: str, visible: bool = True, is_toggle: bool = False):

    user = ft.use_context(UserContext)

    toggle, set_toggle = ft.use_state(False)

    controls: list[ft.Control] = [NormalText(label)]

    if is_toggle:
        controls.append(
            SimpleSwitch(
                toggle, user.text["general"]["toggle"], lambda _: set_toggle(not toggle)
            )
        )

    return ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                ft.Row(controls=controls),
                ft.Text(
                    value=data,
                    expand=True,
                    color=COLORS.text,
                    visible=toggle if is_toggle else True,
                ),
            ]
        ),
        visible=visible,
        col=ALL_OR_HALF,
    )
