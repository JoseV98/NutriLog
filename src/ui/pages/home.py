import flet as ft

from config.constants import COLORS
from config.user_config import UserContext
from ui.components.buttons.home import HomePageButton
from ui.components.show.title import PageTitle
from ui.components.view import MainAppbar, MainView
from ui.go_to import go_to_login, go_to_new_patient, go_to_patients


@ft.component
def HomePage():

    user = ft.use_context(UserContext)

    def check_login():
        if not user.logged:
            go_to_login()

    ft.use_effect(setup=check_login, dependencies=[])

    return MainView(
        path="/",
        appbar=MainAppbar(user.text["home"]["appbar_title"]),
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Column(
                            controls=[
                                PageTitle(
                                    "NutriLog",
                                ),
                                ft.Text(
                                    value=f"{user.text['home']['title']} {user.name}",
                                    color=COLORS.text,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[
                                HomePageButton(
                                    label=user.text["home"]["new_patient"],
                                    icon=ft.Icons.PERSON_ADD,
                                    go_to=go_to_new_patient,
                                ),
                                HomePageButton(
                                    label=user.text["home"]["patients"],
                                    icon=ft.Icons.BOOK_ROUNDED,
                                    go_to=go_to_patients,
                                ),
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=20,
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment.TOP_CENTER,
            )
        ],
    )
