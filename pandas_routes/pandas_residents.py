from fastapi import APIRouter, Depends
from models import User
from services import get_current_user, require_role
from pandas_services import (get_all_active_residents, get_all_resdidents, 
                get_residents_by_dob, get_the_gender_count, how_long_residents)
from database import engine

router = APIRouter(prefix="/residents/reports", tags=["residents Reports"])

@router.get("/total")
def all_resdidents(current_user: User=Depends(require_role("Senior Physio"))):
    return get_all_resdidents(engine)

@router.get("/active_residents")
def active_residents(current_user: User=Depends(require_role("Senior Physio"))):
    return get_all_active_residents(engine)

@router.get("/residents_by_dob")
def residents_by_dob(current_user: User=Depends(require_role("Senior Physio"))):
    return get_residents_by_dob(engine)

@router.get("/gender_count")
def the_gender_count(current_user: User=Depends(require_role("Senior Physio"))):
    return  get_the_gender_count(engine)

@router.get("/residents_stay")
def residents_stay(current_user: User=Depends(require_role("Senior Physio"))):
    return how_long_residents(engine)