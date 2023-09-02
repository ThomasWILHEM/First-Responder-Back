from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from .emergency_call import Emergency_Call
from .vehicule import Vehicule

from database import Base

class Emergency_Ressource(Base):
    __tablename__ = "emergency_ressources"

    id = Column(Integer, primary_key=True, index=True)
    
    call = relationship("Emergency_Call", back_populates="resources")
    vehicule = relationship("Vehicule", back_populates="mission")
