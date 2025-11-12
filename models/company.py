from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from db.db import Base

class Company(Base):
    __tablename__ = "company"

    id: Mapped[int | None] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    web: Mapped[str] = mapped_column(String(50))
    year: Mapped[int] = mapped_column(Integer)
