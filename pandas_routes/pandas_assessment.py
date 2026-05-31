from fastapi import APIRouter, Depends
from models import User
from services import get_current_user, require_role
from pandas_services import (get_active_mobility_assessments, get_active_physio_assessments,
                                         get_physio_assessments_by_physio, 
                                         get_mobility_assessments_by_physio,
                                         get_overdue_physio_assessments,
                                         get_overdue_mobility_assessments)
from database import engine


router = APIRouter(prefix="/assessments/reports", tags=["Assessment Reports"])

@router.get("/physio_assessments_by_physio")
def physio_assessments_by_physio(current_user: User=Depends(require_role("Senior Physio"))):
    return get_physio_assessments_by_physio(engine)


@router.get("/mobility_assessments_by_physio")
def mobility_assessments_by_physio(current_user: User=Depends(require_role("Senior Physio"))):
    return get_mobility_assessments_by_physio(engine)

@router.get("/active_physio_assessments")
def active_physio_assessments(current_user: User=Depends(require_role("Senior Physio"))):
    return get_active_physio_assessments(engine)

@router.get("/active_mobility_assessments")
def active_mobility_assessments (current_user: User=Depends(require_role("Senior Physio"))):
    return get_active_mobility_assessments(engine)

@router("/overdue_physio_assessments")
def overdue_physio_assessments(current_user: User=Depends(require_role("Senior Physio"))):
    return get_overdue_physio_assessments(engine)

@router.get("/overdue_mobility_assessments")
def overdue_mobility_assessments(current_user: User=Depends(require_role("Senior Physio"))):
    return get_overdue_mobility_assessments(engine)