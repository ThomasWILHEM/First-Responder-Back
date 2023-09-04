from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from .vehicule_type import Vehicule_Type  
from .building import Building  
from .call import Call

from database import Base

class Vehicule(Base):
    __tablename__ = "vehicules"

    id = Column(Integer, primary_key=True, index=True)
    position = Column(String, index=True)

    type = relationship("Vehicule_Type")
    building = relationship("Building", back_populates="staffs")
    mission = relationship("Emergency_Call", back_populates="vehicule")


