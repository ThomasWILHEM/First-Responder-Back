from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum, Float
from sqlalchemy.orm import relationship
from .vehicle_type import VehicleType

from ..utils.database import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    coordinates_latitude = Column(Float)
    coordinates_longitude = Column(Float)
    type_id = Column(Integer, ForeignKey("vehicle_types.id"))
    building_id = Column(Integer, ForeignKey("buildings.id"))
    call_id = Column(Integer, ForeignKey("calls.id"))

    type = relationship("VehicleType", back_populates="vehicles")

    occupants = relationship("Staff", back_populates="vehicle")
    building = relationship("Building", back_populates="vehicles")
    call = relationship("Call", back_populates="vehicles")


