from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from .building_type import Building_Type  
from .staff import Staff  

from database import Base

class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    position = Column(String)
    
    type = relationship("Building_Type")
    staffs = relationship("Staff", back_populates="building")