from fastapi import APIRouter, Depends
from services import (get_notes, create_progress_note,get_current_user)
from schemas import (ProgressNoteCreate, ProgressNoteResponse)
from sqlalchemy.orm import Session
from models import User
from database import get_db

router = APIRouter(prefix="/residents", tags=["Progress_notes"])

@router.post("/{resident_id}/Progress_notes", response_model=ProgressNoteResponse, status_code=201)
def create_pain_chart_route(data:ProgressNoteCreate,resident_id:int,
                            db:Session=Depends(get_db),
                            current_user:User=Depends(get_current_user)):
    return create_progress_note(db,data,resident_id, current_user.id)

@router.get("/{resident_id}/Progress_notes", response_model=list[ProgressNoteResponse])
def get_notes_route(resident_id:int, db: Session=Depends(get_db), current_user:User=Depends(get_current_user)):
    return get_notes(db, resident_id)