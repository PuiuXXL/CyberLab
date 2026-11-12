from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db_session
from app.repositories.labs import list_labs
from app.schemas.labs import LabResponse

router = APIRouter(prefix="/labs",tags = ["labs"])

@router.get("",response_model = list[LabResponse])
def get_labs(session: Annotated[Session,Depends(get_db_session)]):
    return list_labs(session)