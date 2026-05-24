from fastapi import HTTPException, status, Depends, APIRouter
from schemas import ResidentCreate, ResidentResponse, ResidentUpdate
from sqlalchemy.orm import Session
from services import (create_resident, get_current_user, 
                      get_all_residents, get_resident_by_id,
                      update_resident, archive_resident)
from database import get_db
from models import User



router = APIRouter(prefix="/residents", tags=["Residents"])

@router.post("/", response_model=ResidentResponse, status_code=201)
def create_resident_route( data:ResidentCreate, 
                    db: Session=Depends(get_db), current_user: User=Depends(get_current_user)):
    return create_resident(db, data, current_user.id)

@router.get("/", response_model=list[ResidentResponse])
def get_all_residents_route(db: Session=Depends(get_db), 
                            current_user: User=Depends(get_current_user)):
    return get_all_residents(db)


@router.get("/{resident_id}", response_model=ResidentResponse)
def get_resident_by_id_route(resident_id:int, db: Session=Depends(get_db),  
                             current_user: User=Depends(get_current_user)):
    return get_resident_by_id(db,resident_id)

@router.patch("/{resident_id}", response_model=ResidentResponse)
def update_resident_route(resident_id:int,data:ResidentUpdate, db: Session=Depends(get_db),
                          current_user: User=Depends(get_current_user)):
    return update_resident(db,data, resident_id)

@router.delete("/{resident_id}", response_model=ResidentResponse)
def archive_resident_route(resident_id:int, db:Session=Depends(get_db),  
                           current_user:User=Depends(get_current_user)):
    return archive_resident(db, resident_id)