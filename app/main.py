from fastapi import FastAPI
from app.routers import users
from app.database.database import engine
from app.database import models
from fastapi.responses import JSONResponse
from fastapi import Request, HTTPException, FastAPI

models.Base.metadata.create_all(bind=engine)

app=FastAPI(title="CRM Backend API")

app.include_router(users.router, prefix="/users", tags=["Users"])

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "data": None,
            "message": exc.detail
        }
    )

@app.get("/")
def home():
    return {"message":"CRM Backend API running"}


