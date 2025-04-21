import datetime as dt

import msgspec

from app.db.models import User


class UserCreateDTO(msgspec.Struct):
    name: str
    surname: str
    password: str

    def to_orm(self) -> User:
        return User(name=self.name, surname=self.surname, password=self.password)


class UserUpdateDTO(msgspec.Struct):
    name: str | None = None
    surname: str | None = None
    password: str | None = None

    def to_dict(self) -> dict:
        return {k: getattr(self, k) for k in self.__annotations__ if hasattr(self, k)}


class UserReadDTO(msgspec.Struct):
    id: int
    name: str
    surname: str
    created_at: dt.datetime
    updated_at: dt.datetime | None = None

    @classmethod
    def from_orm(cls, orm: User) -> 'UserReadDTO':
        return cls(
            id=orm.id,
            name=orm.name,
            surname=orm.surname,
            created_at=orm.created_at,
            updated_at=orm.updated_at,
        )
