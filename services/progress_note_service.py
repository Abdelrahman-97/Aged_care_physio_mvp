from models import ProgressNote
from schemas import ProgressNoteCreate
from sqlalchemy.orm  import Session






def create_progress_note(db:Session, data:ProgressNoteCreate, resident_id:int, physio_id:int):
    obj = ProgressNote(**data.model_dump(exclude={"resident_id"}), resident_id=resident_id, physio_id=physio_id)
    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except:
        db.rollback()
        raise


def get_notes(db: Session, resident_id:int):
    return db.query(ProgressNote).filter(ProgressNote.resident_id == resident_id).all()
    



