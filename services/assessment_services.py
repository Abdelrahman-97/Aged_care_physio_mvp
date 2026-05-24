from sqlalchemy.orm import Session
from schemas import PhysioAssessmentCreate, PhysioAssessmentUpdate, MobilityAssessmentCreate, MobilityAssessmentUpdate
from models import PhysioAssessment, MobilityAssessment
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

def update_physio_assessment(db:Session, data:PhysioAssessmentUpdate, assessment_id:int):
    obj = db.query(PhysioAssessment).filter(PhysioAssessment.id == assessment_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assessment Not found")

    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(obj,k,v)
    
    try:
        db.commit()
        db.refresh(obj)
        return obj
    except:
        db.rollback()
        raise

def archive_physio_assessment(db:Session, assessment_id:int):
    obj = db.query(PhysioAssessment).filter(PhysioAssessment.id == assessment_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assessment Not found")
    obj.is_active = False
    try:
        db.commit()
        return obj
    except:
        db.rollback()
        raise


def create_mobility_assessment(db:Session, 
                               data:MobilityAssessmentCreate, 
                               physio_id:int, resident_id:int):
    obj = MobilityAssessment(**data.model_dump(), physio_id=physio_id, resident_id=resident_id)

    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except:
        db.rollback()
        raise

def get_all_mobility_assessments(db:Session):
    return db.query(MobilityAssessment).filter(MobilityAssessment.is_active==True).all()

def get_mobility_assessment_by_filter(db:Session, 
                                      physio_id:Optional[int]=None, 
                                      resident_id:Optional[int]=None):
    query = db.query(MobilityAssessment)
    if physio_id is not None:
        return query.filter(MobilityAssessment.physio_id == physio_id).all()
    if resident_id is not None:
        return query.filter(MobilityAssessment.resident_id == resident_id).all()
    return query.all()

def update_mobility_assessment(db:Session, data:MobilityAssessmentUpdate, assessment_id:int):
    obj = db.query(MobilityAssessment).filter(MobilityAssessment.id == assessment_id).first()

    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(obj,k,v)

    try:
        db.commit()
        db.refresh(obj)
        return obj
    except:
        db.rollback()
        raise

def archive_mobility_assessment(db:Session, assessment_id:int):
    obj = db.query(MobilityAssessment).filter(MobilityAssessment.id == assessment_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assessment Not Found")

    obj.is_active = False
    try:
        db.commit()
        return obj
    except:
        db.rollback()
        raise
