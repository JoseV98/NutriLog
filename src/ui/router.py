import flet as ft

from config.user_config import UserContext
from ui.pages.home import HomePage
from ui.pages.loading import LoadingView
from ui.pages.auth import LoginPage, RegisterPage, SignLayout


@ft.component
def AppRouter():
    user = ft.use_context(UserContext)
    not_login, set_not_login = ft.use_state(True)

    @ft.use_effect
    async def check_login():
        if not_login:
            await user.check_login()
            set_not_login(False)

    if not_login:
        return LoadingView()

    return UserContext(
        user,
        lambda: ft.Router(
            [
                ft.Route(
                    path="/auth",
                    component=SignLayout,
                    outlet=True,
                    children=[
                        ft.Route(path="login", component=LoginPage),
                        ft.Route(path="register", component=RegisterPage),
                    ],
                ),
                ft.Route(path="/", component=HomePage, index=True),
            ],
            manage_views=True,
        ),
    )
