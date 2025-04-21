import os

from advanced_alchemy.extensions.litestar import (
    SQLAlchemyAsyncConfig,
)

DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'postgres')
DB_NAME = os.getenv('POSTGRES_DB', 'postgres')

DATABASE_URL = (
    f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

sa_config = SQLAlchemyAsyncConfig(
    connection_string=DATABASE_URL, session_dependency_key='session'
)
