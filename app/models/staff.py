from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from .staff_type import Staff_Type  
from .building import Building  

from database import Base

class Staff(Base):
    __tablename__ = "staffs"

    id = Column(Integer, primary_key=True, index=True)
    fisrtname = Column(String, index=True)
    lastname = Column(String, index=True)

    type = relationship("Staff_Type")
    building = relationship("Building", back_populates="staffs")
    vehicule = relationship("Vehicule", back_populates="occupants")


