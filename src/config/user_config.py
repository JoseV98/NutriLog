from dataclasses import dataclass

import flet as ft


@ft.observable
@dataclass()
class User:
    def __init__(self) -> None:
        self.is_mobile = True
        self.size = 1080

    async def check_login(self):

        if self.is_mobile is None:
            platform = ft.context.page.platform
            if platform is not None:
                self.is_mobile = platform.is_mobile()

    def get_height(self) -> int:
        size = ft.context.page.height
        if size is None:
            return 1080

        else:
            return int(size)


UserContext: ft.ContextProvider[User] = ft.create_context(User())
