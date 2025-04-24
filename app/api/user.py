from typing import Annotated

from advanced_alchemy.extensions.litestar import filters, providers, service
from litestar import Controller, HttpMethod, route
from litestar.params import Dependency

from app.schemas.user import UserCreateDTO, UserReadDTO, UserUpdateDTO
from app.services.user import UserService


class UserController(Controller):
    path = '/user'
    tags = ['user']
    dependencies = providers.create_service_dependencies(
        UserService,
        key='user_service',
        filters={
            'id_filter': int,
            'pagination_type': 'limit_offset',
        },
    )

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
        user = await user_service.get(user_id=user_id)
        return user

    @route(http_method=HttpMethod.GET)
    async def get_users(
        self,
        user_service: UserService,
        filters: Annotated[list[filters.FilterTypes], Dependency(skip_validation=True)],
    ) -> service.OffsetPagination[UserReadDTO]:
        return await user_service.list_and_count(*filters)

    @route(http_method=HttpMethod.PATCH, path='/{user_id:int}')
    async def update_user(
        self, user_id: int, data: UserUpdateDTO, user_service: UserService
    ) -> UserReadDTO:
        return await user_service.update(user_id=user_id, data=data)

    @route(http_method=HttpMethod.DELETE, path='/{user_id:int}')
    async def delete_user(self, user_id: int, user_service: UserService) -> None:
        return await user_service.delete(user_id=user_id)
