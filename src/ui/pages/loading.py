import flet as ft

from config.user_config import UserContext
from ui.colors.palette import COLORS
from ui.components.container import NormalColumn
from ui.components.figures.loading_ring import LoadingRing
from ui.components.text.title import ViewTitle
from ui.components.view import CenterView


@ft.component
def LoadingView():
    user = ft.use_context(UserContext)
    app_height = user.get_height()
    bg_color = COLORS.background

    return CenterView(
        path="/loading",
        bg_color=bg_color,
        content=NormalColumn(
            controls=[
                ViewTitle(
                    text="NutriLog",
                    text_color=COLORS.main,
                    bg_color=bg_color,
                    app_height=app_height,
                ),
                LoadingRing(app_height * 0.1),
            ]
        ),
    )
