from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from database import Base

class Building_Type(Base):
    __tablename__ = "building_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
