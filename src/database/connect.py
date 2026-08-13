from supabase import create_client, Client
from supabase_auth import Session
from config.constants import DB


CLIENT: Client = create_client(DB.URL, DB.KEY)


def update_token(self, access_token: str, refresh_token: str):
    self.access_token = access_token
    self.refresh_token = refresh_token


def db_register(name: str, email: str, password: str) -> Session:

    try:
        user, session = CLIENT.auth.sign_up(
            {
                "email": email.lower(),
                "password": password,
                "options": {"data": {"first_name": name, "language": "es"}},
            }
        )
        return session[1]
    except Exception as e:
        raise e


def db_login(email: str, password: str) -> Session:
    try:
        user, session = CLIENT.auth.sign_in_with_password(
            {"email": email.lower(), "password": password}
        )
        return session[1]
    except Exception as e:
        raise e


def refresh_session(refresh_token: str):
    try:
        CLIENT.auth.set_session(access_token="", refresh_token=refresh_token)

        session = CLIENT.auth.get_session()
        return session if session else None
    except Exception:
        raise
