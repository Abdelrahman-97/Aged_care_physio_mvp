from sqlalchemy import Integer, String, Column, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base
from user_model import User
from assessments_model import PhysioAssessment, MobilityAssessment

class Resident(Base):
    __tablename__ = "residents"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(DateTime, nullable=False)
    room = Column(Integer, nullable=False, index=True, unique=True)
    gender = Column(String, nullable=False)
    diagnosis = Column(String, nullable=False)
    created_by_physio_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    responsible_physio_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    physio_create = relationship("User", foreign_keys=[created_by_physio_id], back_populates="created_residents")
    physio_responsible = relationship("User", foreign_keys=[responsible_physio_id],back_populates="responsible_residents")
    physio_assessments = relationship("PhysioAssessment", foreign_keys=[PhysioAssessment.resident_id], back_populates="residents")
    mobillity_assessment = relationship("MobilityAssessment", foreign_keys=[MobilityAssessment.resident_id], back_populates="residents")
