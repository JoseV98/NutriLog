from supabase import AuthApiError, create_client, Client
from supabase_auth import Session
from config.constants import DB


CLIENT: Client = create_client(DB.URL, DB.KEY)


def update_token(self, access_token: str, refresh_token: str):
    self.access_token = access_token
    self.refresh_token = refresh_token


def db_register(email: str, password: str) -> Session:

    try:
        user, session = CLIENT.auth.sign_up({"email": email, "password": password})
        return session[1]
    except Exception as e:
        raise e


def db_login(email: str, password: str) -> Session:
    try:
        user, session = CLIENT.auth.sign_in_with_password(
            {"email": email, "password": password}
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


# user = User(
#     id='a1ec1497-3e05-41b2-a6c1-c1e468f9949a',
#     app_metadata={
#         'provider': 'email',
#         'providers': ['email']
#     },
#     user_metadata={'email': 'prueba@email.com', 'email_verified': True, 'phone_verified': False, 'sub': 'a1ec1497-3e05-41b2-a6c1-c1e468f9949a'},
#     aud='authenticated',
#     confirmation_sent_at=None,
#     recovery_sent_at=None,
#     email_change_sent_at=None,
#     new_email=None,
#     new_phone=None,
#     invited_at=None,
#     action_link=None,
#     email='prueba@email.com',
#     phone='',
#     created_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 449097, tzinfo=TzInfo(0)),
#     confirmed_at=None,
#     email_confirmed_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 485238, tzinfo=TzInfo(0)),
#     phone_confirmed_at=None,
#     last_sign_in_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 492608, tzinfo=TzInfo(0)),
#     role='authenticated', updated_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 512204, tzinfo=TzInfo(0)),
#     identities=[UserIdentity(id='a1ec1497-3e05-41b2-a6c1-c1e468f9949a', identity_id='97ebcf35-a2a4-4f3e-9542-9beb012a8776', user_id='a1ec1497-3e05-41b2-a6c1-c1e468f9949a', identity_data={'email': 'prueba@email.com', 'email_verified': True, 'phone_verified': False, 'sub': 'a1ec1497-3e05-41b2-a6c1-c1e468f9949a'}, provider='email', created_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 479447, tzinfo=TzInfo(0)), last_sign_in_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 479400, tzinfo=TzInfo(0)), updated_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 479447, tzinfo=TzInfo(0)))],
#     is_anonymous=False,
#     is_sso_user=False,
#     factors=None,
#     deleted_at=None,
#     banned_until=None
# )
#
# session=Session(
#     provider_token=None,
#     provider_refresh_token=None,
#     access_token='eyJhbGciOiJFUzI1NiIsImtpZCI6ImRjNDkzZDg0LTA5Y2YtNDAyNC04M2ZhLTU1MzBlMGZmMGMwNCIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2lnZnpiaWhvZm5sZmRld3FjaXpsLnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJhMWVjMTQ5Ny0zZTA1LTQxYjItYTZjMS1jMWU0NjhmOTk0OWEiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzg0OTEyMDM5LCJpYXQiOjE3ODQ5MDg0MzksImVtYWlsIjoicHJ1ZWJhQGVtYWlsLmNvbSIsInBob25lIjoiIiwiYXBwX21ldGFkYXRhIjp7InByb3ZpZGVyIjoiZW1haWwiLCJwcm92aWRlcnMiOlsiZW1haWwiXX0sInVzZXJfbWV0YWRhdGEiOnsiZW1haWwiOiJwcnVlYmFAZW1haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiYTFlYzE0OTctM2UwNS00MWIyLWE2YzEtYzFlNDY4Zjk5NDlhIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE3ODQ5MDg0Mzl9XSwic2Vzc2lvbl9pZCI6IjE5YzFkODViLTc5N2EtNGQ5ZS1iNzgyLWYyYjNjNzQzNzNkZSIsImlzX2Fub255bW91cyI6ZmFsc2V9.lOiQJF9f5EjLO4XW1Xl5hxeI-khGY67CO2EctNSph0ffxaq3_O5CC9hd66_p-NbPjGNyTKDDW6GXAWknFSsW-w',
#     refresh_token='utlltecdwja3',
#     expires_in=3600,
#     expires_at=1784912039,
#     token_type='bearer',
#     user=User(id='a1ec1497-3e05-41b2-a6c1-c1e468f9949a', app_metadata={'provider': 'email', 'providers': ['email']}, user_metadata={'email': 'prueba@email.com', 'email_verified': True, 'phone_verified': False, 'sub': 'a1ec1497-3e05-41b2-a6c1-c1e468f9949a'}, aud='authenticated', confirmation_sent_at=None, recovery_sent_at=None, email_change_sent_at=None, new_email=None, new_phone=None, invited_at=None, action_link=None, email='prueba@email.com', phone='', created_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 449097, tzinfo=TzInfo(0)), confirmed_at=None, email_confirmed_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 485238, tzinfo=TzInfo(0)), phone_confirmed_at=None, last_sign_in_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 492608, tzinfo=TzInfo(0)), role='authenticated', updated_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 512204, tzinfo=TzInfo(0)), identities=[UserIdentity(id='a1ec1497-3e05-41b2-a6c1-c1e468f9949a', identity_id='97ebcf35-a2a4-4f3e-9542-9beb012a8776', user_id='a1ec1497-3e05-41b2-a6c1-c1e468f9949a', identity_data={'email': 'prueba@email.com', 'email_verified': True, 'phone_verified': False, 'sub': 'a1ec1497-3e05-41b2-a6c1-c1e468f9949a'}, provider='email', created_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 479447, tzinfo=TzInfo(0)), last_sign_in_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 479400, tzinfo=TzInfo(0)), updated_at=datetime.datetime(2026, 7, 24, 15, 53, 59, 479447, tzinfo=TzInfo(0)))], is_anonymous=False, is_sso_user=False, factors=None, deleted_at=None, banned_until=None)
# )
