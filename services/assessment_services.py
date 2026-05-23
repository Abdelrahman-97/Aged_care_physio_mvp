from sqlalchemy.orm import Session
from schemas import PhysioAssessmentCreate, PhysioAssessmentUpdate
from models import PhysioAssessment
from typing import Optional
from fastapi import HTTPException, status



def create_physio_assessment(db:Session, data: PhysioAssessmentCreate, physio_id:int, resident_id:int ):
    obj = PhysioAssessment(**data.model_dump(), 
                           resident_id=resident_id, 
                           physio_id=physio_id)
    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except:
        db.rollback()
        raise

def get_all_physio_assessments(db:Session):
    return db.query(PhysioAssessment).filter(PhysioAssessment.is_active == True).all()

def get_physio_assessment_by_filter(db:Session, resident_id: Optional[int]=None, 
                                physio_id:Optional[int] =None):
    query = db.query(PhysioAssessment)
    if resident_id is not None:
        return query.filter(PhysioAssessment.resident_id == resident_id).all()
    if physio_id is not None:
        return query.filter(PhysioAssessment.physio_id == physio_id).all()
    return query.all()

def updaate_physio_assessment(db:Session, data:PhysioAssessmentUpdate, resident_id:int):
    obj = get_physio_assessment_by_filter(db, resident_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assessment Not found")

    for k, v in data.model_dump(exclude_unset=True):
        setattr(obj,k,v)
    
    try:
        db.commit()
        db.refresh(obj)
        return obj
    except:
        db.rollback()
        raise

def archive_physio_assessment(db:Session, resident_id:int):
    obj = get_physio_assessment_by_filter(db, resident_id)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assessment Not found")
    obj.is_active = False
    try:
        db.commit()
        return obj
    except:
        db.rollback()
        raise