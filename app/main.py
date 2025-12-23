from fastapi import FastAPI
from app.routers import users

app=FastAPI(title="CRM Backend API")

app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def home():
    return {"message":"CRM Backend API running"}