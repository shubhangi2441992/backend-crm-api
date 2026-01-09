from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.routers import users
from app.database.database import engine
from app.database import models
from app.auth import auth_router
from app.routers import admin

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRM Backend API")

# Include routers
app.include_router(auth_router.router, prefix="/auth", tags=["Authentication"])
app.include_router(admin.router)
app.include_router(users.router, prefix="/users", tags=["Users"])

# Global HTTP exception handler
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

# Root endpoint
@app.get("/", response_model=dict)
def home():
    return {"success": True, "data": None, "message": "CRM Backend API running"}

# Optional startup event
@app.on_event("startup")
async def startup_event():
    print("CRM Backend API started successfully!")
