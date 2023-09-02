from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .scenario_type import Scenario_Type  

from database import Base

class Scenario(Base):
    __tablename__ = "scenarios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    desctiption = Column(String, index=True)

    type = relationship("Scenario_Type", back_populates="scenarios")