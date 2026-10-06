import flet as ft

from ui.colors.palette import COLORS


def LoadingRing(size: ft.Number):

    return ft.ProgressRing(
        width=size,
        height=size,
        stroke_width=size * 0.1,
        color=COLORS.main,
        bgcolor=COLORS.secundary_soft,
    )
