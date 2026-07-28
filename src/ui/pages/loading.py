import flet as ft


@ft.component
def LoadingView():
    return ft.View(
        route="/loading",
        appbar=ft.AppBar(title=ft.Text("Cargando...")),
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.ProgressRing(),  # Indicador de carga circular
                        ft.Text("Cargando datos, por favor espera..."),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                alignment=ft.Alignment.CENTER,
                expand=True,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
