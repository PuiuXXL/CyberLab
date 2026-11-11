from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class LabCompletion(Base):
    __tablename__ = "lab_completions"

    user_id : Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key = True)
    lab_id : Mapped[int] = mapped_column(ForeignKey("labs.id"), primary_key = True)
    completed_at : Mapped[datetime] = mapped_column(DateTime(timezone = True), server_default = func.now())

