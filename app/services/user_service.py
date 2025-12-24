from app.schemas.user import UserCreate, User 

users_db=[]


def create_user(user:UserCreate) -> User:
    user_data=User(id=len(users_db)+1, **user.dict())
    """user_data=User(
    id=len(users_db)+1,
    name=user.name,
    age=user.age)"""

    users_db.append(user_data)
    return user_data

def list_users() -> list[User]:
    return users_db

def get_user(user_id:int) -> User:
    for user in users_db:
        if user.id==user_id:
            return user
    return None

def update_user(user_id:int,user_data=UserCreate) -> User:
    for index,user in enumerate(users_db):
        if user.id==user_id:
            updated_data=User(id=user_id, **user_data.dict())
            users_db[index]=updated_data
            return updated_data
    return none

def delete_user(user_id:int) ->bool:
    for user in users_db:
        if user.id==user_id:
            users_db.remove(user)
            return True
    return False
