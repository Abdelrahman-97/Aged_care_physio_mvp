from sqlalchemy.orm import Session
from schemas import ResidentCreate, ResidentUpdate
from models import Resident
from fastapi import HTTPException, status

def get_resident_by_id(db:Session, resident_id:int):
    obj= db.query(Resident).filter(Resident.id == resident_id).first()
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resident Not found")
    return obj

def get_all_residents(db:Session):
    return db.query(Resident).filter(Resident.is_active == True).all()


def create_resident(db:Session, data: ResidentCreate, physio_id: int):
    obj = Resident(**data.model_dump(), created_by_physio_id=physio_id)
    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except Exception:
        db.rollback()
        raise

def update_resident(db: Session, data:ResidentUpdate, resident_id:int):
    obj = get_resident_by_id(db, resident_id)

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, key, value)
    
    try:
        db.commit()
        db.refresh(obj)
        return obj
    except:
        db.rollback()
        raise

def archive_resident(db:Session, assessment_id:int):
    obj = get_resident_by_id(db, assessment_id)
    
    obj.is_active = False
    try:
        db.commit()
        return obj
    except:
        db.rollback()
        raise