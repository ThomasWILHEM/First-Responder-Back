from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from .staff_type import StaffType
from .vehicle import Vehicle

from ..utils.database import Base


class Staff(Base):
    __tablename__ = "staffs"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(255) , index=True)
    lastname = Column(String(255) , index=True)
    type_id = Column(Integer, ForeignKey("staff_types.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    building_id = Column(Integer, ForeignKey("buildings.id"))

    type = relationship("StaffType", back_populates="staffs")
    vehicle = relationship("Vehicle", back_populates="occupants")
    building = relationship("Building", back_populates="staffs")


