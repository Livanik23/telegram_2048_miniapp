from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BigInteger, String, Integer
from typing import Optional
from app.database import Base

class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[Optional[str]] = mapped_column(String(100))
    first_name: Mapped[Optional[str]] = mapped_column(String(50))
    last_name: Mapped[Optional[str]] = mapped_column(String(50))
    best_score: Mapped[int] = mapped_column(Integer, default=0)
