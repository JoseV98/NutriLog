import flet as ft

from config.user_config import UserContext
from ui.components.to_route import to_loading
from ui.pages import loading
from ui.pages.loading import LoadingView


@ft.component
def AppRouter():
    user = ft.use_context(UserContext)
    is_loading, set_is_loading = ft.use_state(True)

    if is_loading:
        to_loading()

    return UserContext(
        user,
        lambda: ft.Router(
            [
                ft.Route(path="/loading", component=LoadingView),
            ],
            manage_views=True,
        ),
    )
