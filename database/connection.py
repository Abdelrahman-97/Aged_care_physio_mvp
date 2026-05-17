from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import get_settings

settings = get_settings()

engine = create_engine(settings.database_url, connect_args={"check_same_thread": False})

Base = declarative_base()

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()
