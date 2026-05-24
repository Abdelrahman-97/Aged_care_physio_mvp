from passlib.context import CryptContext
from sqlalchemy.orm import Session
from schemas import UserCreate
from models import User
from core.config import get_settings
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from core import Settings, get_settings
from database import get_db


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oath2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")

def hash_password(password:str)-> str:
    return pwd_context.hash(password)

def verify_password(plain_password:str, hashed_password:str)-> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_user(db: Session, user: UserCreate):
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, email=user.email, hashed_password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email:str):
    return db.query(User).filter(User.email==email).first()


def create_access_token(data:dict)->str:
    settings = get_settings()

    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

    return encoded_jwt

def get_user_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == int(user_id)).first()

def get_current_user(db: Session=Depends(get_db), settings: Settings=Depends(get_settings), 
                     token: str=Depends(oath2_schema)):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
        
        user = get_user_by_id(db, user_id)

        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
        
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")


def require_role(required_role:str):
    def checker(current_user: User=Depends(get_current_user)):
        if current_user.role != required_role:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail=f" Access is restricted to {required_role}")
        return current_user
    return checker