import datetime as dt

import msgspec


class UserCreateDTO(msgspec.Struct):
    name: str
    surname: str
    password: str


class UserUpdateDTO(msgspec.Struct):
    name: str | None = msgspec.UNSET
    surname: str | None = msgspec.UNSET
    password: str | None = msgspec.UNSET


class UserReadDTO(msgspec.Struct):
    id: int
    name: str
    surname: str
    created_at: dt.datetime
    updated_at: dt.datetime | None = None
