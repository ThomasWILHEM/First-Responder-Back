from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from .staff_type import StaffType

from ..utils.database import Base


class Staff(Base):
    __tablename__ = "staffs"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    type_id = Column(Integer, ForeignKey("staff_types.id"))

    type = relationship("StaffType", back_populates="staffs")
    #building = relationship("Building", back_populates="staffs")
    #vehicule = relationship("Vehicule", back_populates="occupants")


