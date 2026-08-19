from dataclasses import dataclass
from datetime import date

import flet as ft

from logic.general import calc_age


@ft.observable
@dataclass
class Patient:
    def __init__(self) -> None:
        self.name: str = ""
        self.lastname: str = ""
        self.age: int = 0
        self.sex: str = ""

    def update_data(self, name: str, lastname: str, birth: str, sex: str):

        self.name = name
        self.lastname = lastname
        self.age = calc_age(date.fromisoformat(str(birth)))
        self.sex = sex

    def default_data(self, default_name: str = ""):
        self.name = default_name
        self.lastname = ""
        self.age = 0
        self.sex = ""


PatientContext: ft.ContextProvider[Patient] = ft.create_context(Patient())
