from fastapi import APIRouter, status, HTTPException, Depends
from schemas import  TokenResponse, UserLogin, UserCreate, UserResponse
from services import (get_user_by_email, verify_password, create_access_token, 
                      create_user, get_current_user, get_user_by_id)
from database import get_db
from sqlalchemy.orm import Session
from models import User

router = APIRouter(prefix=("/auth"), tags=["Auth"])




@router.post("/login", response_model=TokenResponse)
def login(user_data:UserLogin, db: Session= Depends(get_db)):
    user = get_user_by_email(db, user_data.email)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid password or email")
    
    password_verify = verify_password(user_data.password, user.hashed_password)

    if not password_verify:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid password or email")
    access_token = create_access_token(data={"sub": str(user.id)})

    return{"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session=Depends(get_db)):
    user = get_user_by_email(db, user_data.email)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="User is already found")
    new_user = create_user(db, user_data)

    return new_user


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User=Depends(get_current_user)):
    return current_user