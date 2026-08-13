import flet as ft

from config.constants import COLORS
from config.user_config import UserContext
from ui.components.input import SimpleSwitch


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


@ft.component
def ErrorText(error: str):
    return ft.Text(
        error,
        size=12,
        color=ft.Colors.RED,
        visible=bool(error),
    )


@ft.component
def PageTitle(title: str):
    size = ft.context.page.height
    size = 30 if size is None or size < 30 else int(size * 0.1)
    return ft.Text(
        value=title,
        color=COLORS.main,
        size=size,
        weight=ft.FontWeight.BOLD,
    )


@ft.component
def SubTitle(text):
    size = ft.context.page.height
    size = 20 if size is None or size < 30 else int(size * 0.07)
    return ft.Text(
        value=text,
        color=COLORS.sec,
        size=size,
        weight=ft.FontWeight.BOLD,
    )


@ft.component
def EmptyData(text: str):
    size = ft.context.page.height
    size = 25 if size is None else int(size * 0.08)
    return ft.Text(
        value=text,
        color=COLORS.aux_2,
        size=size if size > 25 else 25,
        weight=ft.FontWeight.W_500,
        margin=10,
    )


@ft.component
def TableTitle(text: str):
    size = ft.context.page.height
    size = 15 if size is None else int(size * 0.04)
    return ft.Text(
        value=text,
        color=COLORS.ctrs,
        size=size if size > 15 else 15,
        weight=ft.FontWeight.W_600,
    )


@ft.component
def NormalText(text: str):
    size = ft.context.page.height
    size = 15 if size is None else int(size * 0.03)
    return ft.Text(
        value=text,
        color=COLORS.text,
        size=size if size > 15 else 15,
        weight=ft.FontWeight.NORMAL,
    )


@ft.component
def NormalData(label, data):
    size = ft.context.page.height
    text_size = 15

    mobile = (
        True
        if ft.context.page.platform is None
        else ft.context.page.platform.is_mobile()
    )
    if size is not None:
        size = int(size * 0.03)
        text_size = size if size > 15 else 15

    controls: list[ft.Control] = [
        ft.Text(
            value=f"{label}:",
            color=COLORS.text,
            size=text_size + 2,
            weight=ft.FontWeight.W_600,
        ),
        ft.Text(
            value=data,
            color=COLORS.text,
            size=text_size,
            weight=ft.FontWeight.NORMAL,
        ),
    ]

    return (
        ft.Column(
            controls=controls,
            col={
                ft.ResponsiveRowBreakpoint.XS: 12,
                ft.ResponsiveRowBreakpoint.SM: 6,
                ft.ResponsiveRowBreakpoint.MD: 4,
                ft.ResponsiveRowBreakpoint.LG: 3,
                ft.ResponsiveRowBreakpoint.XL: 2,
                ft.ResponsiveRowBreakpoint.XXL: 2,
            },
        )
        if mobile
        else ft.Row(
            controls=controls,
            col={
                ft.ResponsiveRowBreakpoint.XS: 12,
                ft.ResponsiveRowBreakpoint.SM: 12,
                ft.ResponsiveRowBreakpoint.MD: 6,
                ft.ResponsiveRowBreakpoint.LG: 4,
                ft.ResponsiveRowBreakpoint.XL: 3,
                ft.ResponsiveRowBreakpoint.XXL: 3,
            },
        )
    )


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
        col={
            ft.ResponsiveRowBreakpoint.XS: 12,
            ft.ResponsiveRowBreakpoint.SM: 12,
            ft.ResponsiveRowBreakpoint.MD: 12,
            ft.ResponsiveRowBreakpoint.LG: 6,
            ft.ResponsiveRowBreakpoint.XL: 6,
            ft.ResponsiveRowBreakpoint.XXL: 6,
        },
    )


@ft.component
def Loading(text: str, is_loading: bool):
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
