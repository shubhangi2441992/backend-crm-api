from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas.user import UserCreate, User
from app.services import user_service

router = APIRouter()

@router.post("/",response_model=User)
def create_user(user:UserCreate,db:Session = Depends(get_db)):
    return user_service.create_user(db,user)

@router.get("/",response_model=list[User])
def list_users(
    name:str = None,
    min_age:int = None,
    max_age:int = None,
    sort_by:str = "id",
    order:str = "asc",
    skip:int = 0,
    limit:int = 10,
    db:Session = Depends(get_db)):
    return user_service.list_users(db,name, min_age, max_age, sort_by, order, skip, limit)

@router.get("/{user_id}", response_model=User )
def get_user(user_id:int,db:Session = Depends(get_db)):
    return user_service.get_user(db,user_id)

@router.put("/{user_id}",response_model=User)
def update_user(user_id:int,user_data:UserCreate,db:Session = Depends(get_db)):
    return user_service.update_user(db,user_id,user_data)

@router.delete("/{user_id}")
def delete_user(user_id:int,db:Session = Depends(get_db)) ->bool:
    user_service.delete_user(db,user_id)
    return {"message": "User deleted successfully"}