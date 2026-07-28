import flet_secure_storage as fss
import flet as ft

from config.constants import WebKey

StorageContext: ft.ContextProvider[fss.SecureStorage | None] = ft.create_context(None)


def create_storage() -> fss.SecureStorage:
    web_key = WebKey()
    return fss.SecureStorage(
        web_options=fss.WebOptions(
            db_name="NutriLog_storage",
            public_key=web_key.PUBLIC,
            wrap_key=web_key.WRAP_KEY,
            wrap_key_iv=web_key.WRAP_KEY_IV,
        ),
        android_options=fss.AndroidOptions(
            reset_on_error=True,
            migrate_on_algorithm_change=True,
            key_cipher_algorithm=fss.KeyCipherAlgorithm.AES_GCM_NO_PADDING,
            storage_cipher_algorithm=fss.StorageCipherAlgorithm.AES_GCM_NO_PADDING,
        ),
        ios_options=fss.IOSOptions(
            accessibility=fss.KeychainAccessibility.FIRST_UNLOCK
        ),
    )


class Storage:
    storage: fss.SecureStorage

    async def set_value(self, key, value):
        try:
            await self.storage.set(key=key, value=value)
        except RuntimeError as e:
            if "Session closed" not in str(e):
                raise

    async def get_value(self, key):
        try:
            return await self.storage.get(key=key)
        except RuntimeError as e:
            if "Session closed" in str(e):
                return None
            raise

    async def remove_value(self, key):
        try:
            await self.storage.remove(key=key)
        except RuntimeError as e:
            if "Session closed" not in str(e):
                raise


STORAGE = Storage()
