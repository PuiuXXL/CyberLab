from sqlalchemy import text

from app.core.config import Settings
from app.db.connection import create_db_engine


DEMO_LABS = [
    {
        "name": "SQL Injection",
        "image": "cyberlab/sql-injection:demo",
        "category": "Baze de date",
        "description": "Vezi cum o intrare neverificată poate modifica o interogare SQL.",
    },
    {
        "name": "Cross-Site Scripting",
        "image": "cyberlab/xss:demo",
        "category": "Securitatea browserului",
        "description": "Înțelege cum ajunge un script injectat să ruleze în browser.",
    },
    {
        "name": "Broken Access Control",
        "image": "cyberlab/access-control:demo",
        "category": "Controlul accesului",
        "description": "Explorează ce se întâmplă când aplicația nu verifică permisiunile.",
    },
]

INSERT_LAB = text("""
    INSERT INTO labs (name, image, category, description)
    SELECT CAST(:name AS varchar), CAST(:image AS varchar),
           CAST(:category AS varchar), CAST(:description AS text)
    WHERE NOT EXISTS (
        SELECT 1 FROM labs WHERE image = CAST(:image AS varchar)
    )
""")


def main() -> None:
    engine = create_db_engine(Settings())

    try:
        with engine.begin() as connection:
            connection.execute(
                text("LOCK TABLE labs IN SHARE ROW EXCLUSIVE MODE")
            )
            connection.execute(INSERT_LAB, DEMO_LABS)
    finally:
        engine.dispose()

    print("Catalogul demo este pregătit.")


if __name__ == "__main__":
    main()
