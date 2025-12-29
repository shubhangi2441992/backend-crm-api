from pydantic import BaseModel

class RegisterSchema(BaseModel):
    name: str
    age: int
    password: str

class LoginSchema(BaseModel):
    name: str
    password: str
