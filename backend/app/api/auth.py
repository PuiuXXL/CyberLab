from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db_session
from app.repositories.user import get_user_by_username
from app.schemas.auth import LoginRequest, UserResponse
from app.models.user import User


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", response_model=UserResponse)
def login(
    payload: LoginRequest,
    session: Annotated[Session, Depends(get_db_session)],
) -> User:
    user = get_user_by_username(session, payload.username)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user