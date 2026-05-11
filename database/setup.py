from database.connection import engine
from models.user_model import User
from models.residents_model import Resident
from models.assessments_model import PhysioAssessment, MobilityAssessment
from models.progress_note_model import ProgressNote
from models.chart_model import PainChart
from database.connection import Base

Base.metadata.create_all(bind=engine)
