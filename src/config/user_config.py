from dataclasses import dataclass

from datetime import datetime, timedelta
import json
import flet as ft
from supabase_auth import Session
from config.constants import PATHS
from config.storage import STORAGE
from database.connect import refresh_session


@ft.observable
@dataclass
class User:
    def __init__(self) -> None:
        self.user = ""
        self.name = ""
        self.language = "es"
        self.text = self.change_text_language()
        self.logged: bool = False
        self.db_auth: str = ""
        self.db_auth_expiration: datetime
        self.app_width: int
        self.app_height: int

    async def check_login(self):

        token_session = await STORAGE.get_value("session")

        if token_session:
            try:
                session: Session | None = refresh_session(token_session)
                if session:
                    await self.save_logged(session)
                    return
                else:
                    await STORAGE.remove_value("session")
            except Exception:
                await STORAGE.remove_value("session")

        self.logged = False

    def change_text_language(self):
        with open(
            PATHS.APP_ASSETS / "text" / f"{self.language}.json", "r", encoding="utf-8"
        ) as text:
            return json.load(text)

    async def save_logged(self, user_session: Session):

        await STORAGE.set_value("session", user_session.refresh_token)

        self.name = user_session.user.user_metadata["first_name"]
        self.user = user_session.user.id
        self.db_auth = user_session.access_token
        self.db_auth_expiration = datetime.now() + timedelta(
            seconds=user_session.expires_in
        )

        self.logged = True


UserContext: ft.ContextProvider[User] = ft.create_context(User())
