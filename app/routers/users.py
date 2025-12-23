from fastapi import APIRouter,HTTPException
from app.schemas.user import UserCreate, User 

router = APIRouter()

users_db=[]

@router.post("/",response_model=User)
def create_user(user:UserCreate):
    user_data=User(id=len(users_db)+1, **user.dict())
    """user_data=User(
    id=len(users_db)+1,
    name=user.name,
    age=user.age)"""

    users_db.append(user_data)
    return user_data

@router.get("/",response_model=list[User])
def list_users():
    return users_db

@router.get("/{user_id}", response_model=User )
def get_user(user_id:int):
    for user in users_db:
        if user.id==user_id:
            return user
    raise HTTPException(status_code=404,detail="User not found")