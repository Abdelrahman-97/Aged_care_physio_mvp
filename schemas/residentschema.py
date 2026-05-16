from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ResidentCreate(BaseModel):
    first_name: str
    last_name: str
    dob: datetime
    room: int
    gender: str
    diagnosis: str
    responsible_physio_id: int

class ResidentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    dob: datetime
    room: int
    gender: str
    diagnosis: str
    created_by_physio_id: int
    responsible_physio_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class ResidentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    dob: Optional[datetime] = None
    room: Optional[int] = None
    gender: Optional[str] = None
    diagnosis: Optional[str] = None
    responsible_physio_id: Optional[int] = None
