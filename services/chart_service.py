from sqlalchemy.orm import Session
from schemas import PainChartCreate
from models import PainChart
from typing import Optional


def create_pain_chart(db: Session, data:PainChartCreate, resident_id:int, physio_id:int):
    obj = PainChart(**data.model_dump(), resident_id=resident_id, physio_id=physio_id)
    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except:
        db.rollback()
        raise

def get_all_pain_charts(db:Session):
    return db.query(PainChart).filter(PainChart.is_active == True).all()

def get_pain_chart_by_filter(db:Session, resident_id:Optional[int]=None, 
                             physio_id:Optional[int]=None):
    query = db.query(PainChart)
    if physio_id is not None:
        return query.filter(PainChart.physio_id == physio_id).all()
    if resident_id is not None:
        return query.filter(PainChart.resident_id == resident_id).all()
    return query.all()
