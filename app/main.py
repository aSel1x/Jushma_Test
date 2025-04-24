from dotenv import load_dotenv
from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin

from app.api.user import UserController
from app.db.core import alchemy

load_dotenv()


app = Litestar(
    route_handlers=[
        UserController,
    ],
    plugins=[alchemy],
    openapi_config=OpenAPIConfig(
        title='Jushma Test', version='0.1.0', render_plugins=[SwaggerRenderPlugin()]
    ),
)
