from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db import models


class UserRepository(SQLAlchemyAsyncRepository[models.User]):
    model_type = models.User
