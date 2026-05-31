from sqlalchemy.orm import Session
from schemas import PhysioAssessmentCreate, PhysioAssessmentUpdate, MobilityAssessmentCreate, MobilityAssessmentUpdate
from models import PhysioAssessment, MobilityAssessment, Resident, User
from typing import Optional
from fastapi import HTTPException, status
from core import get_settings
from email_service import send_email



def create_physio_assessment(db:Session, data: PhysioAssessmentCreate, 
                             physio_id:int, resident_id:int ):
    obj = PhysioAssessment(**data.model_dump(exclude={"resident_id"}), 
                           resident_id=resident_id, 
                           physio_id=physio_id)
    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        resident = db.query(Resident).filter(Resident.id == obj.resident_id).first()
        physio = db.query(User).filter(User.id == obj.physio_id).first()
        resident_name = f"{resident.first_name} {resident.last_name}" if resident else "Unknown Resident"
        physio_name = physio.name if physio else "Unkown Physio"


        email_body = f"""
A new Physiotherapy Assessment has been created.

Basic Details
-------------
Assessment ID: {obj.id}
Resident: {resident_name}
Resident ID: {obj.resident_id}
Created By: {physio_name}
Physio ID: {obj.physio_id}
Created At: {obj.created_at}

Assessment Details
------------------
Past History:
{obj.past_history}

Present Pain:
{obj.present_pain}

Upper Limb:
{obj.upper_limb}

Lower Limb:
{obj.lower_limb}

Hands:
{obj.hands}

Coordination:
{obj.coordination}

Standing Balance:
{obj.standing_balance}

Sitting Balance:
{obj.sitting_balance}

Functional Outcomes:
{obj.functional_outcomes}

Summary - ROM and Muscle Power:
{obj.summary_rom_muscle_power}

Summary - Balance:
{obj.summary_balance}

Goals:
{obj.goals}

Planned Interventions:
{obj.planned_interventions}

Pain Management:
{obj.pain_management}"""
        
        settings = get_settings()
        send_email(to_email=[settings.senior_physio_email, settings.admin_email, settings.facility_manager_email],
                   subject=f"A Physiotherapy Assessment was created by {physio_name} for resident: {resident_name}",
                   body= email_body)
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
    obj = MobilityAssessment(**data.model_dump(exclude={"resident_id"}), physio_id=physio_id, resident_id=resident_id)

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
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assessment not found")
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
