from fastapi import APIRouter, Depends
from services import (create_pain_chart, get_all_pain_charts, 
                      get_pain_chart_by_filter, get_current_user)
from schemas import (PainChartCreate, PainChartResponse)
from models import User
from database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/residents", tags=["Charts"])

@router.post("/{resident_id}/Charts", response_model=PainChartResponse, status_code=201)
def create_pain_chart_route(resident_id:int, data: PainChartCreate, 
                            current_user: User=Depends(get_current_user), 
                            db: Session=Depends(get_db)):
    return create_pain_chart(db, data, resident_id, current_user.id)

@router.get("/{resident_id}/Charts", response_model=list[PainChartResponse])
def get_pain_chart_by_filter_route(resident_id:int, db: Session=Depends(get_db),
                             current_user:User=Depends(get_current_user)):
    return get_pain_chart_by_filter(db, resident_id=resident_id)

@router.get("/Charts", response_model=list[PainChartResponse])
def get_all_pain_charts_route(db:Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    return get_all_pain_charts(db)
