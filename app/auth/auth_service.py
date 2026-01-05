from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database.models import UserModel
from app.auth.auth_utils import hash_password,verify_password, create_access_token
from app.schemas.response import ResponseModel
from app.auth.auth_schema import RegisterSchema, LoginSchema

def register_user(db: Session, user: RegisterSchema):
    existing_user = db.query(UserModel).filter(UserModel.name == user.name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = UserModel(
        name=user.name,
        age=user.age,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return ResponseModel(
        success=True,
        data={"id": new_user.id, "name": new_user.name},
        message="User registered successfully"
    )

def login_user(db: Session,user: LoginSchema):
    db_user = db.query(UserModel).filter(UserModel.name == user.name).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": str(db_user.id), "role": db_user.role})


    return ResponseModel(
        success=True,
        data={"access_token": access_token, "token_type": "bearer"},
        message="Login successful"
    )
