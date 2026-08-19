from datetime import date
from typing import cast

import flet as ft

from config.constants import COLORS
from config.patient_config import PatientContext
from config.user_config import UserContext
from database.select import patient_old_data
from logic.nutrition_functions import (
    calc_bmi,
    calc_bmr_harris_benedict,
    calc_bmr_schofield,
    calc_ideal_weight,
)
from ui.components.input.input_date import InputDate
from ui.components.input.input_float import InputFloat
from ui.components.responsive_row_configuration import ALL_OR_HALF, BIG
from ui.components.show.data import NormalData
from ui.components.show.error_text import ErrorText
from ui.components.show.text import NormalText
from ui.components.show.title import PageTitle
from ui.components.view import MainAppbar, MainView
from ui.components.waiting import LoadingRing
from ui.go_to import go_to_patient


@ft.component
def PatientNewData():
    user = ft.use_context(UserContext)
    patient = ft.use_context(PatientContext)
    params = ft.use_route_params()

    data_date, set_date = ft.use_state(date.today())

    weight, set_weight = ft.use_state("")
    height, set_height = ft.use_state("")

    bmi, set_bmi = ft.use_state("")
    bmi_class, set_bmi_class = ft.use_state("")
    ideal_weight, set_ideal_weight = ft.use_state("")
    bmr, set_bmr = ft.use_state("")
    bmr_equation, set_bmr_equation = ft.use_state("")

    loading, set_loading = ft.use_state(False)
    error, set_error = ft.use_state("")

    bmi_classification_dict = {
        "l": user.text["data"]["bmi"]["l"],
        "n": user.text["data"]["bmi"]["n"],
        "h": user.text["data"]["bmi"]["h"],
        "vh": user.text["data"]["bmi"]["vh"],
    }

    register_date = [
        NormalText(user.text["data"]["date"]),
        InputDate(on_change_date=set_date),
    ]

    def bmr_component() -> ft.Control:
        bmr_options = ["Harris-Benedict"]
        if patient.age >= 18:
            bmr_options.append("Schofield")

        if len(bmr_options) > 1:
            return ft.ResponsiveRow(
                controls=[
                    ft.Dropdown(
                        key=bmr_equation,
                        editable=True,
                        label=user.text["general"]["equation"],
                        options=[
                            ft.DropdownOption(
                                key=option,
                                content=NormalText(option),
                                # style=ft.ButtonStyle(bgcolor=COLORS.aux_1),
                            )
                            for option in bmr_options
                        ],
                        color=COLORS.text,
                        on_select=lambda e: set_bmr_equation(
                            cast(str, e.control.value)
                        ),
                        bgcolor=COLORS.aux_1,
                        col=ALL_OR_HALF,  # type: ignore
                    ),
                    NormalData(
                        label=user.text["data"]["bmr"]["text"],
                        data=bmr,
                    ),
                ],
            )
        else:
            set_bmr_equation("Harris-Benedict")
            return NormalData(
                label=user.text["data"]["bmr"]["text"],
                data=bmr,
            )

    def change_bmi():
        if weight and height:
            new_bmi, new_bmi_class = calc_bmi(weight=weight, height=height)
            set_bmi(new_bmi)
            set_bmi_class(bmi_classification_dict[new_bmi_class])
            set_ideal_weight(calc_ideal_weight(height=height, sex=patient.sex))

    def change_bmr():
        if weight and height and bmr_equation:
            if bmr_equation == "Schofield":
                set_bmr(
                    calc_bmr_schofield(
                        weight=weight,
                        age=patient.age,
                        sex=patient.sex,
                        minor_text=user.text["data"]["bmr"]["minor"],
                    )
                )
            else:
                set_bmr(
                    calc_bmr_harris_benedict(
                        weight=weight,
                        height=height,
                        age=patient.age,
                        sex=patient.sex,
                    )
                )

    async def get_old_data():
        set_loading(True)
        set_error("")

        try:
            old_data = await patient_old_data(params["patient_id"])
            print(old_data)

        except Exception:
            set_error(user.text["errors"]["general"])
        finally:
            set_loading(False)

    ft.use_effect(setup=get_old_data, dependencies=[])
    ft.use_effect(setup=change_bmi, dependencies=[weight, height])
    ft.use_effect(setup=change_bmr, dependencies=[weight, height, bmr_equation])

    return MainView(
        path=ft.use_view_path(),
        appbar=MainAppbar(
            title=patient.name, back=lambda: go_to_patient(params["patient_id"])
        ),
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    PageTitle(
                        f"{user.text['patient_new_data']['title']}\n{patient.name}"
                    ),
                    ErrorText(error=error),
                    LoadingRing(
                        text=user.text["patient_data"]["loading"],
                        is_loading=loading,
                    ),
                    ft.Column(
                        expand=True,
                        scroll=ft.ScrollMode.ADAPTIVE,
                        controls=[
                            ft.Column(register_date)
                            if user.is_mobile
                            else ft.Row(register_date),
                            ft.ResponsiveRow(
                                controls=[
                                    InputFloat(
                                        label=user.text["data"]["weight"],
                                        placeholder=user.text["placeholder"][
                                            "big_number"
                                        ],
                                        set_input_data=set_weight,
                                        unit="Kg",
                                    ),
                                    InputFloat(
                                        label=user.text["data"]["height"],
                                        placeholder=user.text["placeholder"]["number"],
                                        set_input_data=set_height,
                                        unit="m",
                                    ),
                                ]
                            ),
                            ft.ResponsiveRow(
                                controls=[
                                    NormalData(
                                        label=user.text["data"]["bmi"]["text_mobile"]
                                        if user.is_mobile
                                        else user.text["data"]["bmi"]["text"],
                                        data=bmi,
                                        unit="Kg/m²",
                                        col_distribution=BIG,
                                    ),
                                    NormalData(
                                        label=user.text["data"]["bmi"][
                                            "classification"
                                        ],
                                        data=bmi_class,
                                    ),
                                    NormalData(
                                        label=user.text["data"]["ideal_weight"],
                                        data=ideal_weight,
                                        unit="Kg",
                                    ),
                                    bmr_component(),
                                ]
                            ),
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ],
    )
