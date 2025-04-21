from typing import Iterable

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories import UserRepository
from app.schemas.user import UserCreateDTO, UserReadDTO, UserUpdateDTO


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.repo = UserRepository(session=session)

    async def create(self, data: UserCreateDTO) -> UserReadDTO:
        created_user = await self.repo.add(data.to_orm())
        await self.session.commit()
        await self.session.refresh(created_user)

        return UserReadDTO.from_orm(created_user)

    async def read(self, user_id: int) -> UserReadDTO | None:
        print(user_id)
        user = await self.repo.get_one_or_none(id=user_id)
        if not user:
            return None

        return UserReadDTO.from_orm(user)

    async def read_all(self) -> Iterable[UserReadDTO]:
        users = await self.repo.list()
        return [UserReadDTO.from_orm(u) for u in users]

    async def update(self, user_id: int, data: UserUpdateDTO):
        user = await self.repo.get(user_id)
        if not user:
            return None

        for k, v in (data.to_dict()).items():
            if v is not None:
                setattr(user, k, v)

        await self.session.commit()
        await self.session.refresh(user)

        return UserReadDTO.from_orm(user)

    async def delete(self, user_id: int) -> None:
        await self.repo.delete(user_id)
        await self.session.commit()
