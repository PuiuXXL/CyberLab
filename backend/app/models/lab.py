from sqlalchemy import Identity, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Lab(Base):
    __tablename__ = "labs"

    id : Mapped[int] = mapped_column(Identity(), primary_key = True)
    name : Mapped[str] = mapped_column(String(200))
    image : Mapped[str] = mapped_column(String(255))

    