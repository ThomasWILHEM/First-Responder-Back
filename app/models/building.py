from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from .building_type import BuildingType
from .staff import Staff  

from ..utils.database import Base

class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    coordinates_latitude = Column(Float)
    coordinates_longitude = Column(Float)
    type_id = Column(Integer, ForeignKey("building_types.id"))

    type = relationship("BuildingType")
    #staffs = relationship("Staff", back_populates="building")