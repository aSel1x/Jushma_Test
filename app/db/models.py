import datetime as dt

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime, String


class User(BigIntAuditBase):
    name: Mapped[str] = mapped_column(String, nullable=False, unique=False)
    surname: Mapped[str] = mapped_column(String, nullable=False, unique=False)
    password: Mapped[str] = mapped_column(
        String, nullable=False, unique=False
    )  #  так вообще hashed_password и LargeBinary

    #  В Mixin обычно выношу:
    created_at: Mapped[dt.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[dt.datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True, server_onupdate=func.now()
    )
