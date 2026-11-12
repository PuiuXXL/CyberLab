from collections.abc import Generator

from fastapi import Request
from sqlalchemy.orm import Session

def get_db_session(request : Request) -> Generator[Session, None, None]:
    with Session(request.app.state.db_engine) as session:
        yield session