from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from ..utils.database import Base

class BuildingType(Base):
    __tablename__ = "building_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, index=True)

    #buildings = relationship("Building", back_populates="type")
