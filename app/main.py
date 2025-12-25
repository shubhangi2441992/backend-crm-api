from fastapi import FastAPI
from app.routers import users
from app.database.database import engine
from app.database import models

models.Base.metadata.create_all(bind=engine)

app=FastAPI(title="CRM Backend API")

app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def home():
    return {"message":"CRM Backend API running"}