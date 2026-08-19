import flet as ft

from config.patient_config import PatientContext
from config.user_config import UserContext
from ui.pages.home import HomePage
from ui.pages.loading import LoadingView
from ui.pages.auth import LoginPage, RegisterPage, SignLayout

from ui.pages.patient.id_patient.data import PatientDataPage
from ui.pages.patient.id_patient.new_data import PatientNewData
from ui.pages.patient.new import NewPatient
from ui.pages.patients import AllPatients


@ft.component
def AppRouter():
    user = ft.use_context(UserContext)
    not_loading, set_not_loading = ft.use_state(True)

    patient = ft.use_context(PatientContext)

    @ft.use_effect
    async def check_loading():
        if not_loading:
            await user.check_login()
            set_not_loading(False)

    if not_loading:
        return LoadingView()

    return UserContext(
        user,
        lambda: ft.Router(
            [
                ft.Route(component=HomePage, index=True),
                ft.Route(path="patients", component=AllPatients),
                ft.Route(
                    path="patient",
                    children=[
                        ft.Route(path="new", component=NewPatient),
                        PatientContext(
                            patient,
                            lambda: ft.Route(
                                path=":patient_id",
                                children=[
                                    ft.Route(path="data", component=PatientDataPage),
                                    ft.Route(path="new-data", component=PatientNewData),
                                ],
                            ),
                        ),
                    ],
                ),
                ft.Route(
                    path="auth",
                    component=SignLayout,
                    outlet=True,
                    children=[
                        ft.Route(path="login", component=LoginPage),
                        ft.Route(path="register", component=RegisterPage),
                    ],
                ),
            ],
            manage_views=True,
        ),
    )
