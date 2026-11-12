from sqlalchemy import text

from app.core.config import Settings
from app.db.connection import create_db_engine


def main() -> None:
    engine = create_db_engine(Settings())

    try:
        with engine.begin() as connection:
            connection.execute(
                text("""
                    INSERT INTO users (username)
                    VALUES (:username)
                    ON CONFLICT (username) DO NOTHING
                """),
                {"username": "demo"},
            )
    finally:
        engine.dispose()


if __name__ == "__main__":
    main()