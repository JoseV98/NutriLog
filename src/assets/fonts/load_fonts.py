import flet as ft
import os
from config import CONFIG


def load_fonts(app: ft.Page):

    app.fonts = {
        "primary": os.fspath(CONFIG.APP_FONTS / "NotoSansArmenian.ttf"),
        "secundary": os.fspath(CONFIG.APP_FONTS / "Sarabun_Regular.ttf"),
    }
    app.theme = ft.Theme(font_family="primary")
    return app
