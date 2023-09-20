from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .scenario_type import ScenarioType  

from ..utils.database import Base

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255) , unique=True, index=True)
    description = Column(String(255) )
    type_id = Column(Integer, ForeignKey("scenario_types.id"))

    type = relationship("ScenarioType", back_populates="scenarios")
