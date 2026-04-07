"""
Reservation 모델 — reservations 테이블
"""

from sqlalchemy import Column, String, Date, Time, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    study_room_id = Column(String, ForeignKey("study_rooms.id"), nullable=False)
    reserved_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
