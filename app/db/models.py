from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped


class User(BigIntAuditBase):
    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]
