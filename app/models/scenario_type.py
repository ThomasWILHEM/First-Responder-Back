from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..utils.database import Base

class ScenarioType(Base):
    __tablename__ = "scenario_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255) , unique=True, index=True)

    scenarios = relationship("Scenario", back_populates="type")
