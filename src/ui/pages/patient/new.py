import flet as ft

from config.constants import COLORS
from config.user_config import UserContext
from database.insert import new_patient
from logic.general import calc_age
from ui.components.buttons.form import FormButton
from ui.components.buttons.simple_switch import SimpleSwitch
from ui.components.input.input_date import InputDate
from ui.components.input.input_float import InputFloat
from ui.components.input.input_multiline import InputMultiLineText
from ui.components.input.input_text import InputText
from ui.components.show.error_text import ErrorText
from ui.components.show.title import PageTitle
from ui.components.view import MainAppbar, MainView
from ui.go_to import go_to_patient
from ui.styles.texts import NORMAL


@ft.component
def NewPatient():

    user = ft.use_context(UserContext)

    name, set_name = ft.use_state("")
    last_name, set_last_name = ft.use_state("")
    sex, set_sex = ft.use_state("")
    birthday, set_birthday = ft.use_state(None)

    minor_age, set_minor_age = ft.use_state(False)
    genetic_potential, set_potential = ft.use_state(False)
    mother_height, set_mother_height = ft.use_state("")
    father_height, set_father_height = ft.use_state("")

    medical_record, set_record = ft.use_state(False)
    medical_record_value, set_record_value = ft.use_state("")
    medical_exam, set_exam = ft.use_state(False)
    medical_exam_value, set_exam_value = ft.use_state("")

    new_patient_valid, set_new_patient_valid = ft.use_state(False)

    loading, set_loading = ft.use_state(False)
    error, set_error = ft.use_state("")

    def birthday_change(new_date):
        set_birthday(new_date)
        set_minor_age(18 > calc_age(new_date))

    @ft.use_effect
    def check_values():

        basic = bool(name) and bool(last_name) and bool(birthday) and bool(sex)
        potential = (
            bool(mother_height) and bool(father_height)
            if minor_age and genetic_potential
            else True
        )
        exam = bool(medical_exam_value) if medical_exam else True
        record = bool(medical_record_value) if medical_record else True

        set_new_patient_valid(basic and potential and exam and record)

    async def save_new_patient():

        set_loading(True)

        try:
            patient_id = await new_patient(
                user=user.user,
                name=name,
                lastname=last_name,
                sex=sex,
                birthday=birthday,  # type: ignore
                potential=genetic_potential,
                mother=float(mother_height) if bool(mother_height) else 0,
                father=float(father_height) if bool(father_height) else 0,
                is_exam=medical_exam,
                exam=medical_exam_value,
                is_disease=medical_record,
                disease=medical_record_value,
            )
            go_to_patient(str(patient_id))

        except Exception:
            set_error(user.text["errors"]["general"])
        finally:
            set_loading(False)

    return MainView(
        path="/patient/new",
        appbar=MainAppbar(user.text["home"]["appbar_title"]),
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[
                        PageTitle(user.text["new_patient"]["title"]),
                        ft.Container(
                            expand=True,
                            padding=10,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    ft.ResponsiveRow(
                                        expand=True,
                                        controls=[
                                            InputText(
                                                label=user.text["data"]["name"],
                                                set_input_data=set_name,
                                            ),
                                            InputText(
                                                label=user.text["data"]["lastname"],
                                                set_input_data=set_last_name,
                                            ),
                                            InputDate(
                                                init_date_value=user.text[
                                                    "new_patient"
                                                ]["birthday"],
                                                on_change_date=birthday_change,
                                            ),
                                        ],
                                    ),
                                    ft.Row(
                                        controls=[
                                            ft.Text(
                                                user.text["data"]["sex"],
                                                color=COLORS.text,
                                            ),
                                            ft.RadioGroup(
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Radio(
                                                            value="M",
                                                            label=user.text["data"][
                                                                "sex_m"
                                                            ],
                                                            label_style=NORMAL,
                                                        ),
                                                        ft.Radio(
                                                            value="F",
                                                            label=user.text["data"][
                                                                "sex_f"
                                                            ],
                                                            label_style=NORMAL,
                                                        ),
                                                    ],
                                                ),
                                                value=sex,
                                                on_change=lambda e: set_sex(e.data),  # type: ignore
                                            ),
                                        ],
                                    ),
                                    SimpleSwitch(
                                        value=genetic_potential,
                                        label=user.text["new_patient"]["potential"],
                                        is_visible=minor_age,
                                        on_change_data=set_potential,
                                    ),
                                    InputFloat(
                                        label=user.text["data"]["mother"],
                                        set_input_data=set_mother_height,
                                        placeholder=user.text["placeholder"]["number"],
                                        unit="m",
                                        empty_valid=True,
                                        visible=genetic_potential,
                                    ),
                                    InputFloat(
                                        label=user.text["data"]["father"],
                                        set_input_data=set_father_height,
                                        placeholder=user.text["placeholder"]["number"],
                                        unit="m",
                                        empty_valid=True,
                                        visible=genetic_potential,
                                    ),
                                    SimpleSwitch(
                                        value=medical_record,
                                        label=user.text["new_patient"]["disease"],
                                        on_change_data=set_record,
                                    ),
                                    InputMultiLineText(
                                        label=user.text["new_patient"]["disease"],
                                        set_input_data=set_record_value,
                                        visible=medical_record,
                                    ),
                                    SimpleSwitch(
                                        value=medical_exam,
                                        label=user.text["new_patient"]["exam"],
                                        on_change_data=set_exam,
                                    ),
                                    InputMultiLineText(
                                        label=user.text["new_patient"]["exam"],
                                        set_input_data=set_exam_value,
                                        visible=medical_exam,
                                    ),
                                ],
                                scroll=ft.ScrollMode.ADAPTIVE,
                            ),
                        ),
                        ErrorText(error=error),
                        FormButton(
                            label=user.text["new_patient"]["summit"],
                            is_enabled=new_patient_valid,
                            on_click=save_new_patient,
                            loading=loading,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment.CENTER,
            ),
        ],
    )
