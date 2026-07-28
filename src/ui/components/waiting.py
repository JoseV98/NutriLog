import flet as ft


@ft.component
def LoadingPage():
    return ft.Container(
        ft.ProgressRing(),
        alignment=ft.alignment.Alignment.CENTER,
        expand=True,
    )
