import flet as ft


def go_to_home():
    ft.context.page.navigate("/")


def go_to_login():
    ft.context.page.navigate("/auth/login")


def go_to_register():
    ft.context.page.navigate("/auth/register")


def go_to_patients():
    ft.context.page.navigate("/patients")


def go_to_new_patient():
    ft.context.page.navigate("/patient/new")


def go_to_patient(id: str):
    ft.context.page.navigate(f"/patient/{id}/data")


def got_to_patient_new_data(id: str):
    ft.context.page.navigate(f"/patient/{id}/new-data")
