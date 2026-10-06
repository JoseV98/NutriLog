import os
import flet as ft

from config.constants import PATHS
from config.storage import STORAGE

from ui.router import AppRouter


async def main(app: ft.Page):

    app.vertical_alignment = ft.MainAxisAlignment.CENTER
    app.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    app.theme_mode = ft.ThemeMode.SYSTEM
    app.title = "NutriLog"

    if isinstance(app.platform, ft.PagePlatform) and app.platform.is_desktop():
        monitor_height = 1080
        try:
            from screeninfo import get_monitors

            for m in get_monitors():
                if m.is_primary:
                    monitor_height = m.height
                    break
        except ImportError:
            print(
                "Libreria screeninfo no instalada, asumiendo una pantalla de 1080px de altura"
            )

        aspect_ratio = 16 / 9
        max_height = monitor_height
        min_height = max_height * 0.8

        min_width = min_height * aspect_ratio
        max_width = max_height * aspect_ratio

        app.window.min_height = min_height
        app.window.max_height = max_height
        app.window.min_width = min_width
        app.window.max_width = max_width

        app.window.top = monitor_height * 0.1
        app.window.height = min_height
        app.window.width = min_width

        app.window.aspect_ratio = aspect_ratio
        if app.platform == ft.PagePlatform.WINDOWS:
            app.window.icon = os.fspath(PATHS.APP_ASSETS / "icon.ico")

    print("Inicio de la App")
    app.render_views(AppRouter)


ft.run(main)
