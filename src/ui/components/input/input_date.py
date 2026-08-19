from datetime import date
from typing import Callable

import flet as ft

from config.constants import COLORS
from config.user_config import UserContext
from ui.components.responsive_row_configuration import STANDARD


@ft.component
def InputDate(
    on_change_date: Callable,
    init_date_value: str = date.today().strftime("%d/%m/%Y"),
    col_ditribution: dict = STANDARD,
):
    user = ft.use_context(UserContext)

    today = date.today()

    text_date, set_text_date = ft.use_state(init_date_value)
    calendar_date, set_calendar_date = ft.use_state(today)

    def chage_date():

        new_date = calendar.value

        if new_date and calendar_date != new_date:
            set_calendar_date(new_date)  # type: ignore
            set_text_date(new_date.strftime("%d/%m/%Y"))
            on_change_date(new_date)

    calendar = ft.DatePicker(
        locale=ft.Locale(user.language),
        last_date=today,
        first_date=date(year=today.year - 150, month=today.month, day=today.day),
        current_date=calendar_date,
        on_change=chage_date,
        on_dismiss=chage_date,
    )

    return ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.Icons.CALENDAR_MONTH,
                    on_click=lambda _: ft.context.page.show_dialog(calendar),
                ),
                ft.Text(
                    value=text_date,
                    color=COLORS.text,
                ),
            ],
        ),
        col=col_ditribution,
    )
