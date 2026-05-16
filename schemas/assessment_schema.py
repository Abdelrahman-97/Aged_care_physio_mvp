from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class PhysioAssessmentCreate(BaseModel):
    past_history: str
    present_pain: str
    upper_limb: str
    lower_limb: str
    hands: str
    coordination: str
    standing_balance: str
    sitting_balance: str
    functional_outcomes: str
    summary_rom_muscle_power: str
    summary_balance: str
    goals: str
    planned_interventions: str
    pain_management: str
    resident_id: int

class PhysioAssessmentResponse(BaseModel):
    id: int
    past_history: str
    present_pain: str
    upper_limb: str
    lower_limb: str
    hands: str
    coordination: str
    standing_balance: str
    sitting_balance: str
    functional_outcomes: str
    summary_rom_muscle_power: str
    summary_balance: str
    goals: str
    planned_interventions: str
    pain_management: str
    resident_id: int
    physio_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class PhysioAssessmentUpdate(BaseModel):
    past_history: Optional[str] = None
    present_pain: Optional[str] = None
    upper_limb: Optional[str] = None
    lower_limb: Optional[str] = None
    hands: Optional[str] = None
    coordination: Optional[str] = None
    standing_balance: Optional[str] = None
    sitting_balance: Optional[str] = None
    functional_outcomes: Optional[str] = None
    summary_rom_muscle_power: Optional[str] = None
    summary_balance: Optional[str] = None
    goals: Optional[str] = None
    planned_interventions: Optional[str] = None
    pain_management: Optional[str] = None
    


class MobilityAssessmentCreate(BaseModel):
    past_history: str
    transfers: str
    walking: str
    bed_mobility: str
    resident_id: int

class MobilityAssessmentResponse(BaseModel):
    id: int
    past_history: str
    transfers: str
    walking: str
    bed_mobility: str
    resident_id: int
    physio_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class MobilityAssessmentUpdate(BaseModel):
    past_history: Optional[str] = None
    transfers: Optional[str] = None
    walking: Optional[str] = None
    bed_mobility: Optional[str] = None
    