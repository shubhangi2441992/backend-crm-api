from fastapi import APIRouter,HTTPException
from app.schemas.user import UserCreate, User
from app.services import user_service

router = APIRouter()

@router.post("/",response_model=User)
def create_user(user:UserCreate):
    return user_service.create_user(user)

@router.get("/",response_model=list[User])
def list_users():
    return user_service.list_users()

@router.get("/{user_id}", response_model=User )
def get_user(user_id:int):
    user = user_service.get_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@router.put("/{user_id}",response_model=User)
def update_user(user_id:int,user_data:UserCreate):
    user=user_service.update_user(user_id,user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}")
def delete_user(user_id:int) ->bool:
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}