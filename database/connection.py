from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DB_url = os.getenv("DATABASE_URL")

engine = create_engine(DB_url)

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
