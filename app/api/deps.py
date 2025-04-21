from sqlalchemy.ext.asyncio import AsyncSession

from app.services.user import UserService


async def provide_user_service(session: AsyncSession) -> UserService:
    return UserService(session)
