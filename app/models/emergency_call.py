from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from .scenario import Scenario

from database import Base

class Emergency_Call(Base):
    __tablename__ = "emergency_calls"

    id = Column(Integer, primary_key=True, index=True)
    position = Column(String)
    call_timestamp = Column(DateTime)
    start_timestamp = Column(DateTime)
    completion_timestamp = Column(DateTime)
    mission_status = Column(Enum)
    mission_result = Column(Enum)

    scenario = relationship("Scenario")
    resources = relationship("Emergency_Ressource", back_populates="call")
