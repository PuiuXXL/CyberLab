from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine

from app.core.config import Settings


def create_db_engine(settings: Settings) -> Engine:
    url = URL.create(
        drivername="postgresql+psycopg",
        username=settings.postgres_user,
        password=settings.postgres_password.get_secret_value(),
        host=settings.postgres_host,
        port=settings.postgres_port,
        database=settings.postgres_db,
    )

    return create_engine(
        url,
        pool_pre_ping=True,
        connect_args={"connect_timeout": 5},
    )