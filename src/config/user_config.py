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
        self.text = self.change_text_language("es")
        self.logged: bool = False
        self.db_auth: str = ""
        self.db_auth_expiration: datetime

    async def check_login(self):

        token_session = await STORAGE.get_value("session")

        if token_session:
            session: Session | None = refresh_session(token_session)
            if session:
                await self.save_logged(session)
                return

        self.logged = False

    def change_text_language(self, language: str):
        with open(
            PATHS.APP_ASSETS / "text" / f"{language}.json", "r", encoding="utf-8"
        ) as text:
            return json.load(text)

    async def save_logged(self, user_session: Session):

        await STORAGE.set_value("session", user_session.refresh_token)

        self.db_auth = user_session.access_token
        self.db_auth_expiration = datetime.now() + timedelta(
            seconds=user_session.expires_in
        )

        self.logged = True


UserContext: ft.ContextProvider[User] = ft.create_context(User())
