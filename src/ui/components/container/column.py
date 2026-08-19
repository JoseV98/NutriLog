import flet as ft


@ft.component
def NormalColumn(controls: list[ft.Control]):
    return ft.Column(
        controls=controls,
        expand=True,
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


@ft.component
def ScrollColumn(controls: list[ft.Control]):

    return ft.Column(
        controls=controls,
        expand=True,
        scroll=ft.ScrollMode.ADAPTIVE,
        spacing=20,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
