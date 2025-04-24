from typing import Iterable

from advanced_alchemy.filters import StatementFilter
from advanced_alchemy.service import SQLAlchemyAsyncRepositoryService

from app.db.models import User
from app.db.repositories import UserRepository
from app.schemas.user import UserCreateDTO, UserReadDTO, UserUpdateDTO


class UserService(SQLAlchemyAsyncRepositoryService[User]):
    repository_type = UserRepository

    async def create(self, data: UserCreateDTO, **kwargs) -> UserReadDTO:
        data = await self.to_model(data, 'create')
        model = await super().create(data, **kwargs)
        return self.to_schema(model, schema_type=UserReadDTO)

    async def get(self, user_id: int) -> UserReadDTO | None:
        model = await super().get(user_id)
        return self.to_schema(model, schema_type=UserReadDTO)

    async def list_and_count(self, *filters: StatementFilter) -> Iterable[UserReadDTO]:
        models, count = await super().list_and_count(*filters)
        return self.to_schema(models, count, filters, schema_type=UserReadDTO)

    async def update(self, data: UserUpdateDTO, user_id: int):
        data = await self.to_model(data, 'update')
        model = await super().update(data, user_id)
        return self.to_schema(model, schema_type=UserReadDTO)

    async def delete(self, user_id: int) -> None:
        await super().delete(user_id)
