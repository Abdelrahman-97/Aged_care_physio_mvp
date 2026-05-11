from sqlalchemy import Integer, String, DateTime,Column, func, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base


class ProgressNote(Base):
    __tablename__ = "progress_notes"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    subjective = Column(String, nullable=False)
    objective = Column(String, nullable=False)
    assessment = Column(String, nullable=False)
    plan = Column(String, nullable=False)
    resident_id = Column(Integer, ForeignKey("residents.id"), nullable=False, index=True)
    physio_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    resident = relationship("Resident", foreign_keys=[resident_id], back_populates="progress_notes")
    physio = relationship("User", foreign_keys=[physio_id], back_populates="progress_notes")