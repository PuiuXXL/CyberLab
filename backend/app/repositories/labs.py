from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.lab import Lab

def list_labs(session : Session) -> list[Lab]:
    statement = select(Lab).order_by(Lab.id)
    return list(session.scalars(statement).all())

