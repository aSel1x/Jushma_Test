from dotenv import load_dotenv
from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from litestar.openapi.plugins import SwaggerRenderPlugin
from litestar.plugins.sqlalchemy import SQLAlchemyPlugin
from litestar_granian import GranianPlugin

from app.api.user import UserController
from app.db.core import sa_config

load_dotenv()

app = Litestar(
    route_handlers=[
        UserController,
    ],
    plugins=[SQLAlchemyPlugin(sa_config), GranianPlugin()],
    openapi_config=OpenAPIConfig(
        title='Jushma Test', version='0.1.0', render_plugins=[SwaggerRenderPlugin()]
    ),
    debug=True,
)
