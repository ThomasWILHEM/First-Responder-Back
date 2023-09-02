from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .scenario import Scenario

from database import Base

class Emergency_Call(Base):
    __tablename__ = "emergency_calls"

    id = Column(Integer, primary_key=True, index=True)
    position = Column(String)
    timestamp = Column(DateTime)

    type = relationship("Scenario")

