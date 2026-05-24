from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class PainChartCreate(BaseModel):
    pain_level: int= Field(ge=0, le=10)
    resident_id: int

class PainChartResponse(BaseModel):
    id: int
    pain_level: int
    resident_id: int
    physio_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

