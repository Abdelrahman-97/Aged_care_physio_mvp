from sqlalchemy import Integer, String, DateTime, Boolean, Column,func
from database.connection import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, index=True, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="Physio", nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(),onupdate=func.now())

    created_residents = relationship("Resident", foreign_keys="Resident.created_by_physio_id", back_populates="physio_create")
    responsible_residents = relationship("Resident", foreign_keys="Resident.responsible_physio_id", back_populates="physio_responsible")
    physio_assessments = relationship("PhysioAssessment", back_populates="physio")
    mobility_assessment = relationship("MobilityAssessment", back_populates="physios")
    progress_notes = relationship("ProgressNote", back_populates="physio")
    pain_level = relationship("PainChart", back_populates="physio")