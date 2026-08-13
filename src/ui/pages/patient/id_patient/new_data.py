import flet as ft

from config.user_config import UserContext
from database.select import patient_old_data
from ui.components.show import ErrorText, Loading, PageTitle
from ui.components.view import MainAppbar, MainView
from ui.go_to import go_to_patient


@ft.component
def PatientNewData():
    user = ft.use_context(UserContext)
    params = ft.use_route_params()

    loading, set_loading = ft.use_state(False)
    error, set_error = ft.use_state("")

    async def get_old_data():
        set_loading(True)
        set_error("")

        try:
            old_data = await patient_old_data(params["patient_id"])
        except Exception:
            set_error(user.text["errors"]["general"])
        finally:
            set_loading(False)

    return MainView(
        path=ft.use_view_path(),
        appbar=MainAppbar(title="", back=lambda: go_to_patient(params["patient_id"])),
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    PageTitle(user.text["patient_new_data"]["title"]),
                    ErrorText(error=error),
                    Loading(
                        text=user.text["patient_data"]["loading"],
                        is_loading=loading,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
    )
