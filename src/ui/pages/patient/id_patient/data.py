import flet as ft

from config.patient_config import PatientContext
from config.user_config import UserContext
from database.select import PatientDataDict, patient_by_id
from ui.components.buttons.icon import IconTextButton
from ui.components.show.data import BlockData, NormalData
from ui.components.show.error_text import ErrorText
from ui.components.show.text import NormalText
from ui.components.show.title import PageTitle
from ui.components.view import MainAppbar, MainView
from ui.components.waiting import LoadingRing
from ui.go_to import go_to_home, go_to_patients, got_to_patient_new_data


@ft.component
def PatientDataPage():

    user = ft.use_context(UserContext)
    patient = ft.use_context(PatientContext)
    params = ft.use_route_params()

    default_exam = {"date": "", "exam": ""}

    default_disease = {"date": "", "disease": ""}

    patient_exam, set_exam = ft.use_state(default_exam)
    patient_disease, set_disease = ft.use_state(default_disease)

    loading, set_loading = ft.use_state(False)
    error, set_error = ft.use_state("")

    async def load_patient_data():
        set_loading(True)
        try:
            data: PatientDataDict | None = await patient_by_id(params["patient_id"])
            if data is None:
                go_to_home()
                return

            patient.update_data(
                name=data["name"],
                lastname=data["lastname"],
                birth=data["birth"],
                sex=data["sex"],
            )

            if data["patient_exams"]:
                exam = data["patient_exams"][0]
                set_exam({"date": exam["date"], "exam": exam["exam"]})

            if data["patient_diseases"]:
                disease = data["patient_diseases"][0]
                set_disease({"date": disease["date"], "disease": disease["disease"]})

        except Exception:
            set_error(user.text["errors"]["general"])
        finally:
            set_loading(False)

    ft.use_effect(setup=load_patient_data, dependencies=[])

    def main_data():

        controls: list[ft.Control] = [
            NormalData(
                label=user.text["patient_data"]["fullname"],
                data=f"{patient.name} {patient.lastname}",
            ),
            NormalData(
                label=user.text["data"]["age"],
                data=str(patient.age),
                unit=user.text["general"]["age_unit"],
            ),
            NormalData(
                label=user.text["data"]["sex"],
                data=user.text["data"]["sex_m"]
                if patient.sex == "m"
                else user.text["data"]["sex_f"],
            ),
        ]

        return (
            ft.Column(controls=controls)
            if user.is_mobile
            else ft.Row(controls=controls)
        )

    def potential():
        return

    def actions_buttons():
        buttons: list[ft.Control] = [
            IconTextButton(
                ft.Icons.EDIT_ROUNDED,
                user.text["patient_data"]["edit"],
                lambda: print(""),
            ),
            IconTextButton(
                ft.Icons.POST_ADD_ROUNDED,
                user.text["patient_data"]["add_data"],
                lambda: got_to_patient_new_data(params["patient_id"]),
            ),
            IconTextButton(
                ft.Icons.NOTE_ADD_ROUNDED,
                user.text["patient_data"]["add_report"],
                lambda: print(""),
            ),
        ]
        return buttons

    return MainView(
        path=ft.use_view_path(),
        appbar=MainAppbar(title=patient.name, back=go_to_patients),
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[
                        PageTitle(
                            f"{user.text['patient_data']['title']} {patient.name} {patient.lastname}"
                        ),
                        ErrorText(error=error),
                        LoadingRing(
                            text=user.text["patient_data"]["loading"],
                            is_loading=loading,
                        ),
                        ft.Row(controls=actions_buttons()),
                        ft.Column(
                            expand=True,
                            controls=[
                                NormalText(user.text["patient_data"]["main_data"]),
                                main_data(),
                                ft.ResponsiveRow(
                                    controls=[
                                        BlockData(
                                            f"{user.text['patient_data']['disease']} {patient_exam['date']}",
                                            f"{patient_exam['exam']}",
                                            bool(patient_exam["date"]),
                                            is_toggle=True,
                                        ),
                                        BlockData(
                                            f"{user.text['patient_data']['exam']} {patient_disease['date']}",
                                            f"{patient_disease['disease']}",
                                            bool(patient_disease["date"]),
                                            is_toggle=True,
                                        ),
                                    ],
                                ),
                            ],
                            scroll=ft.ScrollMode.ADAPTIVE,
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
