from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User

def get_user_by_username(session : Session, username : str) -> User | None:
    statement = select(User).where(User.username == username)
    return session.scalars(statement).one_or_none()