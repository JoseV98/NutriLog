import secrets

import flet as ft
from flet.security import encrypt, decrypt
from pydantic import Base64Encoder


STORAGE_KEY = "storage_key"


class Storage:
    async def storage_key(self) -> str:

        storage_key = await ft.SharedPreferences().get(STORAGE_KEY)

        if storage_key is None:
            raw_key = secrets.token_bytes(32)
            encoded_key = Base64Encoder.encode(raw_key).decode("utf-8")
            await ft.SharedPreferences().set(STORAGE_KEY, encoded_key)
            return encoded_key

        return str(storage_key)

    async def set_value(self, key: str, value: str):

        storage_key = await self.storage_key()

        await ft.SharedPreferences().set(key=key, value=encrypt(value, storage_key))

    async def get_value(self, key: str) -> str | None:
        storage_key = await self.storage_key()
        data = await ft.SharedPreferences().get(key=key)

        if data is not None:
            try:
                return decrypt(str(data), storage_key)

            except Exception:
                return None

        return None

    async def remove_value(self, key: str):

        await ft.SharedPreferences().remove(key=key)


STORAGE = Storage()
