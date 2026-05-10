from database.connection import Base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from user_model import User
from residents_model import Resident


class PhysioAssessment(Base):
    __tablename__ = "physio_assessments"

    id = Column(Integer, primary_key=True,nullable=False, index=True)
    past_hisotry = Column(String, nullable=False)
    present_pain =Column(String, nullable=False)
    upper_limb = Column(String, nullable=False)
    lower_limb = Column(String,nullable=False)
    hands = Column(String, nullable=False)
    coordination = Column(String, nullable=False)
    standing_balance = Column(String, nullable=False)
    sitting_balance = Column(String, nullable=False)
    functional_outcomes = Column(String, nullable=False)
    summary_ROm_muscle_power = Column(String, nullable=False)
    sumamry_balance = Column(String, nullable=False)
    goals = Column(String, nullable=False)
    planned_Interventions = Column(String, nullable=False)
    pain_management = Column(String, nullable=False)
    resident_id = Column(Integer, ForeignKey("Resident.id"), nullable=False, index=True)
    Physio_id = Column(Integer, ForeignKey("User.id"), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    residents = relationship("Resident", foreign_key=[Resident.id], back_populates="physio_assessments")
    physio = relationship("User", foreign_keys=[User.id], back_populates="physio_assessments")

class MobillityAssessment(Base):
    __tablename__ = "mobiltiy_assessments"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    past_history = Column(String, nullable=False)
    trasnfers = Column(String, nullable=False)
    walking = Column(String, nullable=False)
    bed_mobiltiy = Column(String, nullable=False)
    resident_id = Column(Integer, ForeignKey("Resident.id"), nullable=False, index=True)
    physio_id = Column(Integer, ForeignKey("User.id"), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    residents = relationship("Resident", foreign_keys=[Resident.id], back_populates="mobillity_assessment")
    physios = relationship("User", foreign_keys=[physio_id], back_populates="mobillity_assessment")