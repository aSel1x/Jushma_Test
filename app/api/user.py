from litestar import Controller, HttpMethod, route
from litestar.di import Provide
from litestar.exceptions import NotFoundException

from app.api.deps import provide_user_service
from app.schemas.user import UserCreateDTO, UserReadDTO, UserUpdateDTO
from app.services.user import UserService


class UserController(Controller):
    path = '/user'
    tags = ['user']
    dependencies = {'user_service': Provide(provide_user_service)}

    @route(http_method=HttpMethod.POST)
    async def create_user(
        self,
        data: UserCreateDTO,
        user_service: UserService,
    ) -> UserReadDTO:
        return await user_service.create(data=data)

    @route(http_method=HttpMethod.GET, path='/{user_id:int}')
    async def get_user_id(
        self,
        user_id: int,
        user_service: UserService,
    ) -> UserReadDTO:
        user = await user_service.read(user_id=user_id)
        if not user:
            raise NotFoundException(detail=f'User {user_id} not found')
        # так вообще в сервис кастом ошибку, глобально обработчик. Но в рамках этого тестового мне лень
        return user

    @route(http_method=HttpMethod.GET)
    async def get_users(self, user_service: UserService) -> list[UserReadDTO]:
        return await user_service.read_all()

    @route(http_method=HttpMethod.PATCH, path='/{user_id:int}')
    async def update_user(
        self, user_id: int, data: UserUpdateDTO, user_service: UserService
    ) -> UserReadDTO:
        #  так вообще авторизацию бы
        return await user_service.update(user_id=user_id, data=data)

    @route(http_method=HttpMethod.DELETE, path='/{user_id:int}')
    async def delete_user(self, user_id: int, user_service: UserService) -> None:
        return await user_service.delete(user_id=user_id)
