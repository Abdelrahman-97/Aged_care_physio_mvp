from fastapi import APIRouter, Depends
from services import (create_mobility_assessment, create_physio_assessment, 
                                 update_physio_assessment, update_mobility_assessment, 
                                 archive_mobility_assessment, archive_physio_assessment,
                                 get_all_mobility_assessments,get_mobility_assessment_by_filter,
                                 get_physio_assessment_by_filter, get_all_physio_assessments, 
                                 get_current_user)
from schemas import (PhysioAssessmentCreate, PhysioAssessmentResponse, 
                                PhysioAssessmentUpdate, MobilityAssessmentCreate, 
                                MobilityAssessmentResponse, MobilityAssessmentUpdate)
from database import get_db
from sqlalchemy.orm import Session
from models import User
from typing import Optional

router = APIRouter(prefix="/residents", tags=["Assessments"])

#Physio_assessments_routes---------------------------------------------
@router.post("/{resident_id}/physio-assessments", response_model=PhysioAssessmentResponse, 
             status_code=201)
def create_physio_assessment_route(data: PhysioAssessmentCreate,resident_id:int, 
                                   db: Session=Depends(get_db),
                                   current_user: User=Depends(get_current_user)):
    return create_physio_assessment(db, data, resident_id, current_user.id)

@router.get("/physio-assessments", response_model=list[PhysioAssessmentResponse])
def get_all_physio_assessments_route(db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return get_all_physio_assessments(db)

@router.get("/{resident_id}/physio-assessments", response_model=list[PhysioAssessmentResponse])
def get_physio_assessment_by_filter_route(resident_id:Optional[int]=None,
                                    physio_id: Optional[int]=None, db: Session=Depends(get_db), 
                                    current_user:User=Depends(get_current_user)):
    return get_physio_assessment_by_filter(db,resident_id, physio_id)

@router.patch("/{assessment_id}/physio-assessments", response_model=PhysioAssessmentResponse)
def update_physio_assessment_route(data: PhysioAssessmentUpdate, assessment_id:int, 
                                   db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return update_physio_assessment(db, data, assessment_id)

@router.delete("/{assessment_id}/physio-assessments", response_model=PhysioAssessmentResponse)
def archive_physio_assessment_route(assessment_id:int, db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return archive_physio_assessment(db, assessment_id)

#Mobility_assessment_routes--------------------------------------------------------------
@router.post("/{resident_id}/mobility-assessments", response_model=MobilityAssessmentResponse, 
             status_code=201)
def create_Mobility_assessment_route(data: MobilityAssessmentCreate,resident_id:int, 
                                   db: Session=Depends(get_db),
                                   current_user: User=Depends(get_current_user)):
    return create_mobility_assessment(db, data, current_user.id, resident_id)

@router.get("/mobility-assessments", response_model=list[MobilityAssessmentResponse])
def get_all_mobility_assessments_route(db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return get_all_mobility_assessments(db)

@router.get("/{resident_id}/mobility-assessments", response_model=list[MobilityAssessmentResponse])
def get_mobility_assessment_by_filter_route(resident_id:Optional[int]=None,
                                    physio_id: Optional[int]=None, db: Session=Depends(get_db),
                                    current_user:User=Depends(get_current_user)):
    return get_mobility_assessment_by_filter(db,resident_id, physio_id)

@router.patch("/{assessment_id}/mobility-assessments", response_model=MobilityAssessmentResponse)
def update_mobility_assessment_route(data: MobilityAssessmentUpdate, assessment_id:int, 
                                   db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return update_mobility_assessment(db, data, assessment_id)

@router.delete("/{assessment_id}/mobility-assessments", response_model=MobilityAssessmentResponse)
def archive_mobility_assessment_route(assessment_id:int, db: Session=Depends(get_db),current_user: User=Depends(get_current_user)):
    return archive_mobility_assessment(db, assessment_id)