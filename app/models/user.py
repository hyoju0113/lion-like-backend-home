"""
User 모델 — users 테이블을 파이썬 클래스로 정의한 것
"""

from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    username = Column(String(50))
    password_hash = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)
    nickname = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
