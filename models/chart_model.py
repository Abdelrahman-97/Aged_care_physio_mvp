from sqlalchemy import Integer, Column, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base


class PainChart(Base):
    __tablename__ = "pain_chart"
    
    id = Column(Integer,index=True, primary_key=True, nullable=False)
    pain_level = Column(Integer, nullable=False)
    resident_id = Column(Integer, ForeignKey("residents.id"), nullable=False, index=True)
    physio_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    physio = relationship("User", foreign_keys=[physio_id], back_populates="pain_level")
    resident = relationship("Resident", foreign_keys=[resident_id], back_populates="pain_level")

