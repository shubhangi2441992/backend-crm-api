from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.auth.auth_schema import RegisterSchema
from app.auth.auth_service import register_user
from app.schemas.response import ResponseModel
from app.auth.auth_schema import LoginSchema
from app.auth.auth_service import login_user

router = APIRouter()

@router.post("/register", response_model=ResponseModel)
def register(user: RegisterSchema, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.post("/login", response_model=ResponseModel)
def login(user: LoginSchema, db: Session = Depends(get_db)):
    return login_user(db, user)

