from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.main import create_app
from app.models.lab import Lab


def test_catalog_returns_metadata_from_database():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    try:
        Lab.__table__.create(engine)
        with Session(engine) as session:
            session.add_all([
                Lab(
                    name="SQL Injection redenumit",
                    image="cyberlab/sql-injection:demo",
                    category="Baze de date",
                    description="Descriere actualizată în catalog.",
                ),
                Lab(name="Laborator fără metadate", image="cyberlab/custom:demo"),
            ])
            session.commit()

        with TestClient(create_app(db_engine=engine)) as client:
            response = client.get("/labs")

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": 1,
                "name": "SQL Injection redenumit",
                "category": "Baze de date",
                "description": "Descriere actualizată în catalog.",
            },
            {
                "id": 2,
                "name": "Laborator fără metadate",
                "category": None,
                "description": None,
            },
        ]
    finally:
        engine.dispose()
