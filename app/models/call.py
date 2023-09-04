from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Tuple

from ..utils.database import Base

class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)
    coordinates_latitude = Column(Float)
    coordinates_longitude = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    completion_timestamp = Column(DateTime)
    scenario_id = Column(Integer, ForeignKey("scenarios.id"))
    mission_status = Column(String)

    scenario = relationship("Scenario")
    #resources = relationship("Emergency_Ressource", back_populates="call.py")
