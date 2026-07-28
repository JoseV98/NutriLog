import flet as ft

from config.user_config import UserContext


@ft.component
def HomePage():
    user = ft.use_context(UserContext)
    if not user.logged:
        ft.context.page.navigate("/auth/login")

    return ft.View(
        route=ft.use_view_path(),
        appbar=ft.AppBar(title=ft.Text("Página Principal")),  # Sí tiene AppBar
        controls=[],
    )
