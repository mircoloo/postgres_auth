from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func
from .database import Base
from sqlalchemy.orm import Mapped, relationship
from pydantic import EmailStr
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    email: Mapped[EmailStr] = Column(String, unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
