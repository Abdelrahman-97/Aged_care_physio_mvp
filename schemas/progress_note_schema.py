from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProgressNoteCreate(BaseModel):
    subjective: str
    objective: str
    assessment: str
    plan: str
    resident_id: int

class ProgressNoteResponse(BaseModel):
    id: int
    subjective: str
    objective: str
    assessment: str
    plan: str
    resident_id: int
    physio_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
