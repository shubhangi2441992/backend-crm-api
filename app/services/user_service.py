from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.database.models import UserModel
from app.schemas.user import UserCreate, User 

def create_user(db:Session,user:UserCreate) -> User:
    db_user=UserModel(name=user.name,age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return User(id=db_user.id,name=db_user.name,age=db_user.age)

def list_users(db:Session ,
                name:str = None,
                min_age:int = None,
                max_age:int = None,
                sort_by:str = "id",
                order:str = "asc",
                skip:int = 0,
                limit:int = 10 ) -> list[User]:
    
    query= db.query(UserModel)

    #Filtering
    if name:
        query=query.filter(UserModel.name.contains(name))
    if min_age:
        query=query.filter(UserModel.age >=min_age)
    if max_age:
        query=query.filter(UserModel.age <=max_age)
    
    #sorting
    if sort_by in ["id","name","age"]:
        column = getattr(UserModel,sort_by)
        if order =="desc":
            column = column.desc()
        else:
            column = column.asc()
        query=query.order_by(column)

    #paginetion
    users = query.offset(skip).limit(limit).all()
    return [User(id=u.id,name=u.name,age=u.age) for u in users]


def get_user(db:Session,user_id:int) -> User:
    user=db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return User(id=user.id,name=user.name,age=user.age)

def update_user(db:Session,user_id:int,user_data=UserCreate) -> User:
    user=db.query(UserModel).filter(UserModel.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")

    user.name=user_data.name
    user.age=user_data.age
    db.commit()
    db.refresh(user)
    return User(id=user.id, name=user.name, age=user.age)

def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return True
