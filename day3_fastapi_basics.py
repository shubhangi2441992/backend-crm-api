from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

#-----------------------------
#pydantic model (request body)
class User(BaseModel):
    name:str 
    age:int 

#------------------------------
#Get API
@app.get("/")
def home():
    return {"message":"Day 3 FastAPI started"}

#---------------------------------
#Get with path parameter
@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"user_id":user_id}

#----------------------------------
#Get with query parameter
@app.get("/search")
def search_user(active:bool=True):
    return {"active":active}

#-----------------------------------
#Post API
@app.post("/users")
def add_user(user:User):
    return {"massage":"User created successfuly",
                "user":user
                }