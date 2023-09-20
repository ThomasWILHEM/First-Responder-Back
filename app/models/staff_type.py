from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship

from ..utils.database import Base


class StaffType(Base):
    __tablename__ = "staff_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255) , unique=True, index=True)

    staffs = relationship("Staff", back_populates="type")
