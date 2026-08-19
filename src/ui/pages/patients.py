from datetime import date

import flet as ft
import flet_datatable2 as fdt

from config.constants import COLORS
from config.user_config import UserContext
from database.select import patients
from logic.general import calc_age
from ui.components.show.empty import EmptyData
from ui.components.show.error_text import ErrorText
from ui.components.show.title import PageTitle
from ui.components.table.title import TableTitle
from ui.components.view import MainAppbar, MainView
from ui.components.waiting import LoadingRing
from ui.go_to import go_to_patient


@ft.component
def AllPatients():
    user = ft.use_context(UserContext)

    table_data, set_table_data = ft.use_state([])

    loading, set_loading = ft.use_state(False)
    error, set_error = ft.use_state("")

    def DataColumn(label: str, numeric: bool = False):
        size = ft.context.page.height
        size = 30 if size is None or size < 30 else int(size * 0.1)
        return fdt.DataColumn2(
            label=TableTitle(label),
            on_sort=sort_column,
            numeric=numeric,
        )

    def sort_column(e: ft.DataColumnSortEvent):
        return

    def DataRow(data):
        size = ft.context.page.height
        size = 30 if size is None or size < 30 else int(size * 0.08)
        return fdt.DataRow2(
            specific_row_height=size,
            on_select_change=lambda _: go_to_patient(data["idpatient"]),
            cells=[
                TableCell(data["name"]),
                TableCell(data["lastname"]),
                TableCell(calc_age(date.fromisoformat(data["birth"]))),
                TableCell(
                    user.text["data"]["sex_m"]
                    if data["sex"] == "M"
                    else user.text["data"]["sex_f"]
                ),
            ],
        )

    def TableCell(data):
        return ft.DataCell(content=ft.Text(value=data, color=COLORS.text))

    async def load_patient():

        set_loading(True)

        try:
            patients_page = await patients()
            set_table_data([DataRow(data) for data in patients_page])

        except Exception:
            set_table_data([])
            set_error(user.text["errors"]["general"])

        finally:
            set_loading(False)

    ft.use_effect(setup=load_patient, dependencies=[])

    return MainView(
        path="/patients",
        appbar=MainAppbar(user.text["patients"]["appbar_title"]),
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    controls=[
                        PageTitle(user.text["patients"]["title"]),
                        LoadingRing(
                            text=user.text["patients"]["loading"],
                            is_loading=loading,
                        ),
                        ft.Container(
                            expand=True,
                            content=fdt.DataTable2(
                                visible=not loading,
                                expand=True,
                                empty=EmptyData(user.text["patients"]["no_patients"]),
                                heading_row_color=COLORS.sec,
                                horizontal_margin=12,
                                sort_ascending=True,
                                bottom_margin=10,
                                columns=[
                                    DataColumn(user.text["data"]["lastname"]),
                                    DataColumn(user.text["data"]["name"]),
                                    DataColumn(user.text["data"]["age"], numeric=True),
                                    DataColumn(user.text["data"]["sex"]),
                                ],
                                rows=table_data,
                            ),
                        ),
                        ErrorText(error=error),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment.CENTER,
            )
        ],
    )
