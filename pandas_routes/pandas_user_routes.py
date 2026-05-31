from fastapi import APIRouter, Depends
from models import User
from services import get_current_user, require_role
from database import engine
from pandas_services import (get_all_users, get_active_users, started_work_since, physio_roles)


router = APIRouter(prefix=("/reports/users"), tags=["User reports"])

@router.get("/total")
def total_users(current_user: User= Depends(require_role("Senior Physio"))):
    return get_all_users(engine)

@router.get("/active")
def active_users(current_user: User= Depends(require_role("Senior Physio"))):
    return get_active_users(engine)

@router.get("/time_since_start_work")
def time_since_start_work(current_user: User=Depends(require_role("Senior Physio"))):
    return started_work_since(engine)

@router.get("/physio_roles")
def retrun_physio_roles(current_user: User=Depends(require_role("Senior Physio"))):
    return physio_roles(engine)